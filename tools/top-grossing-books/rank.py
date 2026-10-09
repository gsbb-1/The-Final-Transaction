import json, re

cands = json.load(open("candidates.json"))
arts = json.load(open("articles.json"))

TRUSTED = ["WW-main", "WW-animated", "WW-non-english", "WW-comics", "WW-superhero",
           "WW-rrated", "WW-independent", "WW-videogames", "WW-tvseries", "WW-comicstrips",
           "WW-japanese", "WW-indian", "WW-hongkong"]


def sig(v):
    return len(re.sub(r"[^\d]", "", str(v)))


def to_dollars(n, u):
    if u == "b":
        return int(round(n * 1_000_000_000))
    if u == "m":
        return int(round(n * 1_000_000))
    return int(round(n))


def parse_infobox(s):
    if not s:
        return None
    ms = list(re.finditer(r"(?:US)?\$\s*([\d,]+(?:\.\d+)?)", s))
    if not ms:
        return None
    vals = []
    for m in ms:
        num = float(m.group(1).replace(",", ""))
        tail = s[m.end():m.end() + 18].lower()
        if "billion" in tail or re.search(r"\bbn\b", tail):
            unit = "b"
        elif "million" in tail or re.search(r"\bmn\b", tail):
            unit = "m"
        else:
            unit = "d"
        vals.append((m.start(), m.end(), num, unit))
    for st, en, num, unit in vals:
        if re.search(r"\(worldwide\)|\bworldwide\b", s[en:en + 140], re.I):
            return to_dollars(num, unit)
    if len(vals) > 1:
        low = s.lower()
        if ("worldwide" not in low and "domestic" in low) or re.search(r"^\s*\*|\n\s*\*", s):
            return sum(to_dollars(n, u) for _, _, n, u in vals)
    num, unit = vals[-1][2], vals[-1][3]
    return to_dollars(num, unit)


def norm_title(t):
    t = re.sub(r"\s*\(\d{4}[^)]*\)\s*$", "", t)
    t = t.lower().replace("&", "and")
    return re.sub(r"[^a-z0-9]+", "", t)


BAD = re.compile(r"(list of|^lists of|\btrilogy\b|film series|\bfranchise\b|cinematic universe"
                r"|\bphase (one|two|three|four|five|six|seven|eight)\b|soundtrack|film score|album)", re.I)

merged = {}
for url, c in cands.items():
    art = arts.get(url)
    if not art or art.get("no_infobox") or BAD.search(art["title"]):
        continue
    key = norm_title(art["title"]) or url
    options = []
    for lab in TRUSTED:
        w = c["lists"].get(lab, {}).get("w")
        if w:
            options.append((sig(w), 1 if lab == "WW-main" else 0, w, lab))
    ib = parse_infobox(art.get("gross_raw"))
    if ib:
        options.append((sig(ib), -1, ib, "infobox"))
    if not options:
        continue
    options.sort(key=lambda o: (-o[0], -o[1]))
    best = options[0]
    if not (600_000_000 <= best[2] <= 3_200_000_000):
        continue
    rec = merged.get(key)
    if rec is None or best[2] > rec["worldwide"]:
        merged[key] = {
            "url": url, "title": art["title"], "worldwide": best[2],
            "gross_source": best[3], "gross_raw": art.get("gross_raw"),
            "country": art.get("country"), "based_on": art.get("based_on"),
            "based_on_note": art.get("based_on_note"), "lead": art.get("lead", ""),
            "lists": sorted(c["lists"].keys()),
            "options": sorted({(o[2], o[3]) for o in options}, reverse=True)[:5],
        }

films = sorted(merged.values(), key=lambda f: -f["worldwide"])
json.dump(films, open("films.json", "w"))
print(f"{'#':>4} {'worldwide':>15} {'src':<13} country / title")
for i, f in enumerate(films[:120], 1):
    print(f"{i:>4} {f['worldwide']:>15,} {f['gross_source']:<13} {(f['country'] or '')[:20]:22s} {f['title'][:52]}")