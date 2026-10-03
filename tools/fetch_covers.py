"""Download book covers from Open Library into covers/<id>.jpg.

Run from the repo root:  python3 tools/fetch_covers.py
It only fetches books that don't have a cover yet, then marks each one it
finds with "cover": true in books.js. Books it can't match are listed at the
end; add those covers by hand (any JPG saved as covers/<id>.jpg works).
"""
import json, re, time, urllib.parse, urllib.request
from difflib import SequenceMatcher

UA = {"User-Agent": "HomeLibrary/1.0 (personal catalogue)"}

def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def simplify(s):
    return re.sub(r"[^a-z0-9 ]", "", s.lower().split(":")[0]).strip()

def find_cover(title, author):
    q = {"title": title.split(":")[0], "limit": 5, "fields": "title,author_name,cover_i"}
    surname = author.replace("(ed.)", "").split("&")[0].split(",")[0].strip()
    if surname and surname not in ("Anthology", "Various", "Various authors"):
        q["author"] = surname
    docs = json.loads(get("https://openlibrary.org/search.json?" + urllib.parse.urlencode(q))).get("docs", [])
    for d in docs:
        if d.get("cover_i") and SequenceMatcher(None, simplify(d["title"]), simplify(title)).ratio() > 0.75:
            return d["cover_i"]
    return None

src = open("books.js", encoding="utf8").read()
lines = src.split("\n")
missed = []
for n, line in enumerate(lines):
    m = re.match(r"^  (\{.*\}),$", line)
    if not m:
        continue
    b = json.loads(m.group(1))
    if b.get("cover") or b.get("language") == "Tamil":
        continue
    try:
        cid = find_cover(b["title"], b["author"])
        if cid:
            open(f"covers/{b['id']}.jpg", "wb").write(get(f"https://covers.openlibrary.org/b/id/{cid}-M.jpg"))
            b["cover"] = True
            lines[n] = "  " + json.dumps(b, ensure_ascii=False) + ","
            print("found  ", b["title"])
        else:
            missed.append(b["title"])
    except Exception as e:
        missed.append(f"{b['title']} ({e})")
    time.sleep(0.4)

open("books.js", "w", encoding="utf8").write("\n".join(lines))
print(f"\nNo cover found for {len(missed)} books:")
for t in missed:
    print("  -", t)
