# RELEASE

Draft history and the path to publication for The Final Transaction. Milestones are defined in [PLAN.md](PLAN.md).

## Draft stages

Each complete pass over the manuscript is a release. Tag it in git so any draft can be recovered later.

| Tag | Stage | Milestone | Meaning |
| --- | --- | --- | --- |
| `draft-1` | First draft | M2 | The whole story is on the page, start to finish |
| `draft-2` | Revised draft | M3 | Structure, pacing and character arcs fixed |
| `draft-3` | Beta draft | M4 | Reader feedback incorporated |
| `final` | Final manuscript | M5 | Line edited, copyedited and proofread |
| `published` | Published edition | M6 | The text as released to readers |

Add further `draft-N` tags if more passes are needed. Corrections after publication are tagged `published-2`, `published-3`, and so on.

## Checklist for completing a draft

- [ ] Every chapter in the outline exists in `manuscript/`
- [ ] Whole-manuscript consistency check run ([WORKFLOW.md](WORKFLOW.md)) and high-severity findings resolved
- [ ] No unresolved `<!-- TODO -->` notes that block this stage
- [ ] Word count recorded in the history below (`wc -w manuscript/*.md`)
- [ ] `TODO.md` and the milestone status in `PLAN.md` updated
- [ ] Draft history entry added below
- [ ] Tag created: `git tag -a draft-N -m "Draft N"`

## Typeset PDF

A reading copy of the whole manuscript in one PDF, for the author's read-through and for beta readers. It is generated from `manuscript/` and is never edited by hand: change the Markdown, then rebuild with `build/make-pdf.sh`. The build is described in [PLAN.md](PLAN.md).

| | |
| --- | --- |
| Output | `build/the-final-transaction.pdf` |
| Current | Built 2026-10-20 from `draft-1`: 55 chapters, 361 pages, A4 |
| Contents | Title page, contents list, then the 55 chapters with running heads |
| Not printed | The `<!-- DRAFT -->` comments in the chapter files |

The PDF is a reading copy, not a submission copy. For a submission or a print interior, set the page size and margins to the target format and rebuild.

## Publication checklist

The publishing route is not yet decided. Choose one, record the decision in `PLAN.md`, and delete the list that does not apply.

### Before either route

- [ ] Final manuscript complete (`final` tag)
- [ ] Title confirmed
- [ ] Synopsis written (one page)
- [ ] Back-cover blurb written
- [ ] Author biography written
- [ ] Typeset PDF rebuilt from the final manuscript and read through

### Traditional publishing

- [ ] Query letter written
- [ ] List of literary agents who represent thrillers compiled
- [ ] Manuscript formatted to standard submission format
- [ ] Queries sent and tracked
- [ ] Agent signed
- [ ] Submitted to publishers

### Self-publishing

- [ ] Professional copyedit and proofread done
- [ ] Cover designed
- [ ] ISBN obtained
- [ ] Interior formatted for print and e-book
- [ ] Platforms chosen and accounts set up
- [ ] Price and publication date set
- [ ] Proof copy checked
- [ ] Published
- [ ] Launch plan carried out

## Draft history

Newest first.

### draft-1 — 2026-10-10

- Word count: about 113,000 words of prose (comments excluded), 55 chapters; by `wc -w` including comments about 116,000.
- Chapters: 1 (the author's paragraph opens it; an agent expansion follows) and 2–55, all agent drafts awaiting the author's review. Each carries a DRAFT comment on line 1.
- What it is: the complete first draft, written by subagents from `outline/` and `characters/` under `outline/style.md`, after background research (`research/`). Consistency-checked in four passes (notes/ for each); the findings fixed are listed there.
- Known problems to fix in the next pass: see `notes/draft-1-consistency-check.md` (pace and cut list, voice tics, the withheld seventh-book entry, unverified finance and procedure, 76 VERIFY notes, chapters over the 2,000-word guide).

### Before draft-1 — iteration 3 of 4 complete

- 2026-10-10: Act II second half drafted, chapters 29–42, to the all-is-lost moment and Jonas's decision to go live. Manuscript 42 chapters, about 91,000 words. Consistency check over chapters 1–42; high and medium findings fixed. Not yet reviewed by the author.
- 2026-10-09: Act I revised after background research (the record is inferred fingerprints; margin is cash; the Bank of England named; Priya's login is the police hook). Act II first half drafted, chapters 15–28, to the midpoint. Manuscript about 55,000 words. Consistency check run over chapters 1–28; high and medium findings fixed. Not yet reviewed by the author.
- 2026-10-09: Act I drafted by subagents, chapters 2–14, about 24,000 words in total with the author's chapter 1. Whole book outlined. Not yet reviewed by the author; not a tagged draft.
- 2026-10-03: Project set up; brief defined as a ~400-page financial thriller. No manuscript text yet.

<!--
### draft-N — YYYY-MM-DD

- Word count:
- Chapters:
- What changed since the previous draft:
- Known problems to fix in the next pass:
-->
