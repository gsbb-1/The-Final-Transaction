"""Collect candidate films from Wikipedia box-office lists, fetch infobox data,
and rank by worldwide gross.  Output: candidates.json, articles.json, films.json
"""
import json, re, html, time, os, urllib.parse, urllib.request

API = "https://en.wikipedia.org/w/api.php"
UA = {"User-Agent": "HollywoodBoxOfficeResearch/1.0 (personal research script)"}

PAGES = [
    ("List_of_highest-grossing_films", "WW-main", [0]),
    ("List_of_highest-grossing_animated_films", "WW-animated", [0, 1]),
    ("List_of_highest-grossing_non-English_films", "WW-non-english", [0, 8]),
    ("List_of_highest-grossing_films_in_the_United_States_and_Canada", "US-top100", [0]),
    ("List_of_films_based_on_comics", "WW-comics", [0]),
    ("List_of_highest-grossing_films_based_on_video_games", "WW-videogames", [0]),
    ("List_of_films_based_on_television_programs", "WW-tvseries", [0]),
    ("List_of_highest-grossing_independent_films", "WW-independent", [0]),
    ("List_of_highest-grossing_R-rated_films", "WW-rrated", [0]),
    ("List_of_films_based_on_comic_strips", "WW-comicstrips", [0]),
    ("List_of_highest-grossing_superhero_films", "WW-superhero", [0]),
    ("List_of_highest-grossing_Japanese_films", "WW-japanese", [0]),
    ("List_of_highest-grossing_Indian_films", "WW-indian", [0]),
    ("List_of_highest-grossing_films_in_Hong_Kong", "WW-hongkong", [0]),
    # franchise / series pages: candidate discovery only (their box-office column is
    # often domestic, so their figures are not trusted for ranking)
    ("List_of_Marvel_Cinematic_Universe_films", "WW-MCU", None),
    ("List_of_films_based_on_DC_Comics_publications", "WW-DC", None),
    ("List_of_Star_Wars_films", "WW-StarWars", None),
    ("The_Lord_of_the_Rings_(film_series)", "WW-LOTR", None),
    ("The_Hobbit_(film_series)", "WW-Hobbit", None),
    ("Pirates_of_the_Caribbean_(film_series)", "WW-POTC", None),
    ("Fast & Furious", "WW-FF", None),
    ("Jurassic_World_(franchise)", "WW-JurassicWorld", None),
    ("Jurassic Park (franchise)", "WW-JurassicPark", None),
    ("List_of_Harry_Potter_films", "WW-HarryPotter", None),
    ("Mission:_Impossible_(film_series)", "WW-MI", None),
    ("List_of_James_Bond_films", "WW-Bond", None),
    ("The_Hunger_Games_(film_series)", "WW-HungerGames", None),
    ("Fantastic_Beasts_(film_series)", "WW-FantasticBeasts", None),
    ("The_Chronicles_of_Narnia_(film_series)", "WW-Narnia", None),
    ("Dune_(film_series)", "WW-Dune", None),
    ("Maleficent_(film_series)", "WW-Maleficent", None),
    ("The_Twilight_Saga_(film_series)", "WW-Twilight", None),
]

# lists whose "worldwide gross" column is verified (relative to the main top-50 table)
TRUSTED = {"WW-main", "WW-animated", "WW-non-english", "WW-comics", "WW-superhero",
           "WW-rrated", "WW-independent", "WW-videogames", "WW-tvseries", "WW-comicstrips",
           "WW-japanese", "WW-indian", "WW-hongkong"}
KEEP_LABELS = {"WW-main", "US-top100"}


def api(params, retries=5):
    p = dict(params)
    p.update({"format": "json", "formatversion": 2})
    url = API + "?" + urllib.parse.urlencode(p)
    for a in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read())
        except Exception as e:
            if a == retries - 1:
                raise
            time.sleep(4 * (a + 1))


def clean(c):
    c = re.sub(r"<style.*?</style>", "", c, flags=re.S)
    c = re.sub(r"<sup.*?</sup>", "", c, flags=re.S)
    c = re.sub(r"<[^>]+>", "", c)
    return html.unescape(re.sub(r"\s+", " ", c)).strip()


def money(s):
    if not s:
        return None
    ms = list(re.finditer(r"\$\s*([\d,]+(?:\.\d+)?)", s))
    if not ms:
        return None
    last = ms[-1]
    v = float(last.group(1).replace(",", ""))
    tail = s[last.end():last.end() + 24]
    if re.search(r"\bbillion\b|\bbn\b", tail, re.I):
        v *= 1000
    elif not re.search(r"\bmillion\b|\bmn\b", tail, re.I):
        return int(round(v))
    return int(round(v * 1_000_000))


def parse_tables(h, only=None):
    tabs = re.findall(r'<table class="wikitable[^"]*".*?</table>', h, re.S)
    for idx, tab in enumerate(tabs):
        if isinstance(only, (list, tuple)) and idx not in only:
            continue
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", tab, re.S)
        if len(rows) < 3:
            continue
        hdr = [clean(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", rows[0], re.S)]
        ti = next((i for i, x in enumerate(hdr)
                   if any(k in x.lower() for k in ("title", "film", "series"))), None)
        if ti is None:
            continue

        def norm(x):
            return "".join(x.split()).lower()
        wi = next((i for i, x in enumerate(hdr)
                   if norm(x).startswith("worldwidegross") or norm(x).startswith("worldwide")
                   or norm(x) in ("boxoffice",) or norm(x).startswith("boxoffice")), None)
        yi = next((i for i, x in enumerate(hdr) if x.strip().lower() == "year"), None)
        ci = next((i for i, x in enumerate(hdr) if "country" in x.lower()), None)
        for r in rows[1:]:
            cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, re.S)
            if len(cells) <= ti:
                continue
            m = re.search(r'href="(/wiki/[^"#]*)"', cells[ti])
            if not m:
                continue
            u = urllib.parse.unquote(m.group(1))
            if u.startswith(("/wiki/List_of", "/wiki/Category:", "/wiki/File:", "/wiki/Template:")):
                continue
            yield {
                "url": u,
                "w": money(clean(cells[wi])) if wi is not None and len(cells) > wi else None,
                "year": clean(cells[yi]) if yi is not None and len(cells) > yi else None,
                "country": clean(cells[ci]) if ci is not None and len(cells) > ci else None,
            }


def collect():
    cands = {}
    for page, label, tidx in PAGES:
        cache = f"cache_{label}.json"
        if os.path.exists(cache):
            rows = json.load(open(cache))
        else:
            try:
                h = api({"action": "parse", "page": page, "prop": "text", "redirects": 1})["parse"]["text"]
            except Exception as e:
                print(f"{label:18s} FAILED {page[:40]} {e}")
                continue
            rows = [{"url": r["url"],
                     "w": r["w"] if label in TRUSTED else None,
                     "year": r["year"], "country": r["country"]}
                    for r in parse_tables(h, only=tidx)]
            json.dump(rows, open(cache, "w"))
            print(f"{label:18s} {page[:42]:44s} rows={len(rows)}")
            time.sleep(2.0)
        for rec in rows:
            c = cands.setdefault(rec["url"], {"url": rec["url"], "lists": {}})
            prev = c["lists"].get(label)
            if prev is None or (prev.get("w") is None and rec.get("w")):
                c["lists"][label] = {"w": rec.get("w")}
    FRANCHISE = {l for _, l, _ in PAGES} - TRUSTED - {"US-top100"}
    trimmed = {}
    for u, c in cands.items():
        ws = [v.get("w") for v in c["lists"].values() if v.get("w")]
        if max(ws or [0]) >= 300_000_000 or set(c["lists"]) & (KEEP_LABELS | FRANCHISE):
            trimmed[u] = c
    print("unique candidates:", len(cands), "-> pool:", len(trimmed))
    json.dump(trimmed, open("candidates.json", "w"))
    return trimmed


# ---------------- infobox parsing ----------------

def slice_template(wt, i0):
    depth, i = 0, i0
    while i < len(wt) - 1:
        two = wt[i:i + 2]
        if two == "{{":
            depth += 1; i += 2; continue
        if two == "}}":
            depth -= 1; i += 2
            if depth == 0:
                return wt[i0:i]
            continue
        i += 1
    return wt[i0:]


def infobox(wt):
    m = re.search(r"\{\{\s*Infobox\s+(film|movie|tv film|anim film|short)\s*(?=[|\n}])", wt, re.I)
    return slice_template(wt, m.start()) if m else None


def infobox_params(ib):
    """Line-based top-level parameter splitter for a template body."""
    body = ib[2:-2]
    params, name, buf = {}, None, []
    depth = 0
    for line in body.split("\n"):
        stripped = line.lstrip()
        if depth == 0 and stripped.startswith("|") and stripped[1:2] != "|":
            if name is not None:
                params[name] = "\n".join(buf).strip()
            m = re.match(r"\|\s*([^=]+?)\s*=(.*)", stripped)
            name = m.group(1).strip() if m else None
            buf = [m.group(2)] if m else []
        else:
            buf.append(line)
        depth += line.count("{{") + line.count("[[") - line.count("}}") - line.count("]]")
    if name is not None:
        params[name] = "\n".join(buf).strip()
    return params


def strip_markup(s):
    if not s:
        return ""
    s = re.sub(r"<ref[^>]*/>", "", s)
    s = re.sub(r"<ref[^>]*>.*?</ref>", "", s, flags=re.S)
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    # currency templates keep their numeric argument
    s = re.sub(r"\{\{\s*(?:US\$|USD|US Dollar|Currency|GBP|\u20ac)\s*\|\s*([^{}]*?)\s*\}\}", r"\1", s, flags=re.I)
    # "transparent" templates: drop the template name, keep the contents
    TRANSPARENT = (r"(?:plain\s*list|unbulleted\s*list|ub\s*l|flat\s*list|h\s*list|bulleted\s*list|"
                   r"nowrap|nobr|nbsp|non\s*breaking\s*space|based\s*on|sortname|sort|small|center|lang)")
    for _ in range(8):
        s2 = re.sub(r"\{\{\s*" + TRANSPARENT + r"\s*\|", " ", s, flags=re.I)
        if s2 == s:
            break
        s = s2
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"\{\{[^{}]*\}\}", " ", s)
    s = s.replace("{{", " ").replace("}}", " ").replace("|", "; ")
    s = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]|]*)\]\]", r"\1", s)
    s = re.sub(r"\[https?://\S+\s+([^\]]*)\]", r"\1", s)
    s = re.sub(r"\[https?://\S+\]", "", s)
    s = re.sub(r"'{2,}", "", s)
    s = re.sub(r"<br\s*/?>", "<br>", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s*\*\s*", "; ", s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\s*;\s*;\s*", "; ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip(" ;")

def plain_body(wt):
    out, i = [], 0
    while i < len(wt):
        if wt[i:i + 2] == "{{":
            seg = slice_template(wt, i)
            i += len(seg)
            continue
        out.append(wt[i])
        i += 1
    t = "".join(out)
    t = re.sub(r"\{\|.*?\|\}", "", t, flags=re.S)
    t = re.sub(r"<ref[^>]*>.*?</ref>", "", t, flags=re.S)
    t = re.sub(r"<ref[^>]*/>", "", t)
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]|]*)\]\]", r"\1", t)
    t = re.sub(r"\[https?://\S+\s+([^\]]*)\]", r"\1", t)
    t = re.sub(r"'{2,}", "", t)
    t = re.sub(r"<[^>]+>", "", t)
    return t


def lead_text(wt):
    body = plain_body(wt).split("\n==")[0]
    paras = [re.sub(r"\s+", " ", p).strip() for p in body.split("\n\n")]
    for p in paras:
        if re.search(r"\bis (a|an|the)\b", p) and len(p) > 80:
            return p
    return " ".join(p for p in paras if len(p) > 40)[:1500]


def fetch(cands):
    arts = {}
    urls = [u for u in cands if u not in arts]
    print("fetching", len(urls), "articles")
    B = 50
    for i in range(0, len(urls), B):
        batch = urls[i:i + B]
        titles = "|".join(u.replace("/wiki/", "") for u in batch)
        d = api({"action": "query", "prop": "revisions", "rvprop": "content", "rvslots": "main",
                 "titles": titles, "redirects": 1})
        norm = {n["to"]: n["from"] for n in d.get("query", {}).get("normalized", [])}
        norm.update({r["to"]: r["from"] for r in d.get("query", {}).get("redirects", [])})
        for p in d.get("query", {}).get("pages", []):
            key = norm.get(p["title"], p["title"])
            url = "/wiki/" + key.replace(" ", "_")
            wt = p["revisions"][0]["slots"]["main"]["content"] if p.get("revisions") else ""
            ib = infobox(wt)
            pr = infobox_params(ib) if ib else {}
            arts[url] = {
                "title": p["title"],
                "gross_raw": strip_markup(pr.get("gross")) if "gross" in pr else None,
                "country": strip_markup(pr.get("country")) if "country" in pr else None,
                "based_on_raw": pr.get("based_on", "").strip() if "based_on" in pr else None,
                "based_on": strip_markup(pr.get("based_on")) if "based_on" in pr else None,
                "based_on_note": strip_markup(pr.get("based_on_note")) if "based_on_note" in pr else None,
                "lead": lead_text(wt)[:1200],
                "no_infobox": not ib,
            }
        print(f"  {min(i+B,len(urls))}/{len(urls)}")
        time.sleep(1.5)
    json.dump(arts, open("articles.json", "w"))
    return arts


if __name__ == "__main__":
    c = collect()
    a = fetch(c)
    print("done:", len(c), "candidates,", len(a), "articles")
