import json, re, csv, os

films = json.load(open("films.json"))
TOP = 100
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                   "top_100_hollywood_movies_based_on_books.csv")

COMIC = [r"comic|manga|manhwa|webtoon|graphic novel|superhero|DC Comics|\bDC\b|Marvel|"
         r"Stan Lee|Jack Kirby|Steve Ditko|Bob Kane|Bill Finger|Jerry Siegel|Joe Shuster|"
         r"William Moulton Marston|Fabian Nicieza|Rob Liefeld|Chris Claremont|Jim Starlin|"
         r"Don Heck|Larry Lieber|Joe Simon|Dan Abnett|Andy Lanning|"
         r"Spider-Man|Batman|Superman|Iron Man|Captain America|Black Panther|Wolverine|"
         r"Deadpool|Aquaman|Wonder Woman|Guardians of the Galaxy|X-Men|Venom|\bThor\b"]

BOOK = [r"\bnovel\b|novella|short story|fairy tale|picture book|\bbook\b|novels|"
        r"\bplay\b|memoir|biography|autobiography|\bpoem\b|epic poem|literary character|"
        r"\bTolkien\b|Rowling|Ian Fleming|Suzanne Collins|Stephenie Meyer|Rudyard Kipling|"
        r"Lewis Carroll|Hans Christian Andersen|\bHomer\b|Homeric|William Steig|"
        r"Chris Van Allsburg|American Prometheus|\bOdyssey\b|novel by|books by|"
        r"\bmemoirs\b|diary|diaries|\bletters\b"]

OTHER = [r"video game|video-game|\bMinecraft\b|Mojang|Nintendo|\bMario\b|Sonic the Hedgehog|Pokémon",
         r"action figures|Hasbro|\btoy\b|\btoys\b|board game|card game",
         r"theme[- ]park|attraction at|\bride\b|Disneyland",
         r"\btelevision\b|TV series|television series|web series",
         r"Walt Disney Animation Studios|Disney's (The|Sleeping|Beauty)",
         r"animated film|\bremake\b|Lilo & Stitch \(franchise\)",
         r"\bfranchise\b|\bproductions\b|film series"]

WORK = re.compile(r"novel|book|comic|manga|play|Tolkien|Rowling|Fleming|literary character|"
                  r"picture book|Odyssey|Prometheus|Wonderland|Hobbit|Snow Queen|Shrek|"
                  r"Jumanji|Catching Fire|Breaking Dawn|On Stranger Tides|Harry Potter|"
                  r"Jurassic Park|fairy tale|poem|biography|memoir|Steig|Kipling|Carroll|"
                  r"Allsburg|Meyer|Collins|Andersen", re.I)


def classify(f):
    bo = (f.get("based_on") or "").strip()
    lead = f.get("lead") or ""
    lb = re.search(r"based on ([^.]{0,170})", lead, re.I)
    lb = lb.group(1) if lb else ""
    blob = bo + " || " + lb

    book = any(re.search(p, blob, re.I) for p in BOOK)
    comic = any(re.search(p, blob, re.I) for p in COMIC)
    other = any(re.search(p, blob, re.I) for p in OTHER)

    characters_only = bool(re.search(r"characters", bo, re.I)) and not WORK.search(bo)

    if comic:
        cat = "comic book"
    elif book:
        cat = "book"
    elif other:
        cat = "other medium"
    else:
        cat = "original"

    note = ""
    if characters_only and cat in ("book", "comic book"):
        note = "based only on pre-existing characters (franchise continuation)"

    src = re.sub(r"\s*;\s*", ", ", bo).strip()
    if src in ("", "-", "None") or re.fullmatch(r"[\s,&\-]+", src or ""):
        src = re.sub(r"\s*;\s*", ", ", lb).strip()
    return cat, src, note


for i, f in enumerate(films, 1):
    f["overall_rank"] = i
    f["hollywood"] = bool(re.search(r"United States", f.get("country") or ""))
    cat, src, note = classify(f)
    f["category"], f["source"], f["note"] = cat, src, note
    yr = re.search(r"\b(19|20)\d{2}\b", f.get("lead") or "")
    if not yr:
        yr = re.search(r"(19|20)\d{2}", f.get("url") or "")
    f["year"] = yr.group(0) if yr else ""

json.dump(films, open("films_classified.json", "w"))

rowsel = [f for f in films[:TOP]
          if f["hollywood"] and f["category"] in ("book", "comic book")]

with open(OUT, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["rank", "title", "year", "worldwide_gross_usd", "source_type",
                "based_on", "country", "wikipedia_url", "gross_source", "notes"])
    for f in rowsel:
        title = re.sub(r"\s*\((19|20)\d{2} film\)$|\s*\(film\)$", "", f["title"])
        w.writerow([f["overall_rank"], title, f["year"], f["worldwide"],
                    f["category"], f["source"], f["country"],
                    "https://en.wikipedia.org" + f["url"], f["gross_source"], f["note"]])

print("qualifying rows:", len(rowsel))
for f in rowsel:
    print(f"{f['overall_rank']:>3} {f['worldwide']:>13,}  {f['category']:<10} "
          f"{re.sub(r' \((19|20)\d{2} film\)| \(film\)', '', f['title'])[:44]:<46} {f['note']}")
print("wrote", OUT)