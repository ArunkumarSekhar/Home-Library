# Home Library

A personal catalogue of the books at home, with a reading record for each one:
status, rating, dates, and the lines and ideas worth keeping.

## Files

| File | What it is |
|------|------------|
| `books.js` | The catalogue: one line per book, with its genre and shelf. Add or correct books here. |
| `covers/` | Cover images, one per book, named `<id>.jpg`. |
| `tools/fetch_covers.py` | Downloads missing covers from Open Library: `python3 tools/fetch_covers.py` |
| `index.html` | The app: Library (by genre or all covers), Lines & ideas, and Stats. |
| `books-draft.md` | The first list read from the shelf photos (kept for reference; `books.js` is now the master copy). |

## Where your reading notes are saved

- **Opened inside Claude** (the published page): saved to your Claude account, so the iPad and laptop see the same data.
- **Opened as a plain file** (double-click `index.html`): saved in that browser only.

## Adding a book

Open `books.js`, copy any line, change the title, author and shelf, and give it a new `id`.
Never change an existing `id`: your notes are saved against it.

## Rating a book

There are no stars. Each book gets:
- **Verdict**: Changed me, Loved it, Glad I read it, Mixed feelings, Not for me, Didn't finish
- **What it gave me**: any of Ideas, A story, Beautiful language, Laughs, Comfort, Knowledge, A new perspective, Craft to learn from, Nostalgia
- **Would I read it again?**: Yes, Maybe, No

These lists live at the top of the script in `index.html` (`VERDICTS`, `GAVE`, `REREAD`) and can be changed freely.
