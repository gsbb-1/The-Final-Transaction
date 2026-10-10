# PLAN

How [IDEA.md](IDEA.md) becomes a published novel. Tasks for the current milestone live in [TODO.md](TODO.md).

## Current milestone

**Iteration 4 of 4 complete: the first draft is finished and tagged `draft-1`.** Next: the author's read-through, then M3 Revision.

## Milestones

| # | Milestone | Goal | Done when | Status |
| --- | --- | --- | --- | --- |
| M0 | Concept | Fix the premise and the main choices | Logline, premise, protagonist, antagonist, setting and point of view are written in `IDEA.md` | Mostly done |
| M1 | Story design | Know the whole story before drafting | Character profiles, research notes, and a chapter-by-chapter outline exist | Done 2026-10-10 |
| M2 | First draft | Get the full story on the page | ~100,000 words drafted, start to finish | Done 2026-10-10: 55 chapters, about 113,000 words, tagged `draft-1` |
| M3 | Revision | Fix the story | Structure, pacing, character arcs and plot holes resolved in a second draft | Ready to start once the author has read `draft-1`; see `notes/draft-1-consistency-check.md` for the cut list and open questions |
| M4 | Feedback | Test it on readers | Beta-reader feedback collected and incorporated | Not started |
| M5 | Editing | Polish the prose | Line edit, copyedit and proofread complete | Not started |
| M6 | Publication | Release the book | Published by the chosen route; see [RELEASE.md](RELEASE.md) | Not started |

## Iteration plan

Decided 2026-10-09: the complete first draft (~100,000 words, about 55 chapters) is finished in four iterations. Each iteration runs the loop in [WORKFLOW.md](WORKFLOW.md): draft, consistency check, author review, record. Drafting is done by subagents working from the outline, the profiles and `outline/style.md`, each taking a block of two to four chapters. The author reviews between iterations and may change anything; changes are carried into the next iteration.

| Iteration | Scope | Chapters | Cumulative words | Done when |
| --- | --- | --- | --- | --- |
| 1 | Outline acts II and III. Draft act I | 1–14 | ~25,000 | Act I drafted, consistency check run, outline for the whole book exists |
| 2 | Revise act I from the author's notes. Draft act II, first half, to the midpoint | 15–28 | ~50,000 | Midpoint on the page; checks run |
| 3 | Draft act II, second half, to the all-is-lost moment | 29–42 | ~75,000 | Checks run; reveals audited against the plan |
| 4 | Draft act III. Whole-book consistency pass; fix high-severity findings; tag `draft-1` | 43–55 | ~100,000 | Complete first draft tagged, as in `RELEASE.md` |

Milestones M1 and M2 are delivered through these iterations. M3 onward starts after iteration 4.

## Targets

- **Length:** ~400 pages, about 100,000 words at 250 words per page.
- **Chapters:** about 55 chapters of 1,600 to 2,000 words: act I 14, act II 28, act III 13.
- **Drafting pace:** about 25,000 words per iteration, drafted by subagents; the author's review time between iterations sets the calendar.
- **Deadlines:** _TBD_.

## Structure

Working model: three acts, to be replaced by the real outline in M1.

| Part | Share | Pages | Job |
| --- | --- | --- | --- |
| Act I | 25% | 1–100 | Establish the protagonist's world, the inciting event, and the point of no return. Outlined in [outline/act-1.md](outline/act-1.md): 14 chapters over 7 days, #1399 to #1405 |
| Act II, first half | 25% | 100–200 | Rising danger and investigation, up to a midpoint reversal that changes the game. Outlined in [outline/act-2.md](outline/act-2.md), ch. 15–28: the state hunts Jonas, the map is built, the alliance with Al-Mansouri is made and the notebooks are lost in the same hour |
| Act II, second half | 25% | 200–300 | The antagonist closes in, allies fall away, and everything is lost. Ch. 29–42: Crane has the map, Walbrook may not open, Strand says no, Kessler turns, Jonas decides to go public |
| Act III | 25% | 300–400 | Final confrontation, the "final transaction", and the aftermath. Outlined in [outline/act-3.md](outline/act-3.md), ch. 43–55: one day from broadcast to open, then the fall and the last entry, #1500 |

## Manuscript layout

Proposed repository structure, created as each part is needed:

```
manuscript/   one Markdown file per chapter (01-chapter-title.md)
outline/      synopsis, act breakdown, chapter-by-chapter outline
characters/   one profile per major character
research/     finance mechanics, locations, procedures, sources
notes/        ideas, cut scenes, loose material
```

## Research areas

Notes in [research/](research/README.md): swaps and clearing, cybersecurity, information security (done 2026-10-09); corrections they imply in `research/corrections-from-research.md`. Still to research:

- How market panics start and spread: contagion, liquidity, margin calls, bank runs, currency and sovereign debt crises
- Past panics as models: what triggered them and how they unfolded day by day
- Geopolitical triggers: conflict, sanctions, trade and energy shocks, and how markets price them
- National politics in a crisis: governments, central banks, regulators, bailouts, capital controls, elections
- How the central financial mechanism of the plot actually works
- The institutions, roles and jargon of that world
- Regulators, law enforcement and how financial crime is investigated
- Locations

## Decision log

Record significant decisions here, newest first.

| Date | Decision | Why |
| --- | --- | --- |
| 2026-10-10 | Iteration 4 and `draft-1`. Act III revised in the brief (`notes/act-3-drafting-brief.md`): the broadcast and arrest, the indemnity signed at 7.02, release at 8.14, the transaction built in the fund's St James's dealing room and executed from Walbrook's risk room (Walbrook had cut its data and file links at six; voice and settlement stayed), the thirteenth member, the pursuit, Laura and Kessler at Aisha's, Crane's warrant. Polling day Thursday #1436; the last entry #1500 on Friday 8 January; Jonas numbers days, not pages; no stand-alone entry-number line in any chapter; Strand is twelve years at the Bar and fourteen in the House | Author asked for iteration 4. Dates fixed so Australian daylight saving fits the early-October setting |
| 2026-10-09 | Iteration 2 begun. Research decisions (`research/corrections-from-research.md`): **P1** Jonas never sees the same gilt pledged twice; he reads the fingerprints of over-pledged collateral over four years (paired "timing" fails, cash paid at nine swapped for bonds at three, substitutions, leaked position reports) and infers the chains; the record is a pattern-match that no one can verify and he could be wrong. **P2** "Theft" stays as Walbrook's and the press's word, never a charge; Walbrook goes to court (interim injunction and delivery-up order, heard by phone on Sunday night, served Monday); the police hook is Computer Misuse: on Friday afternoon, after Jonas's access was cut, Priya logged in at his desk and pulled the member report for him, so both are exposed and Priya is the one detained. **P3** Priya is held about 20 hours (Sunday noon to Monday morning), released under investigation with phone and laptop kept and a bail condition not to contact Walbrook staff; nobody, including Jonas, knows where she is until Thursday. **P4** A clearing house has no open to miss: "Walbrook may not be able to meet its obligations; the Bank is considering resolution"; the final transaction runs through an indemnified Bank operation; the Tuesday open is delayed by the Bank and the exchanges, not Walbrook. **P5** The chapter 2 alert goes to a compliance reviewer, then the head of compliance, then Graham; Haldane's "close as personal, no action" stays as later ammunition. Also: the story is set in early October, year unfixed | Author asked for decisions that rely on existing development and maximise suspense. P1 adds doubt (he may be wrong); P2 gives Jonas and Priya a real legal exposure they caused themselves; P3 makes Priya's silence last four days; P4 makes the threat a resolution, which is bigger; P5 keeps Haldane's misconduct |
| 2026-10-09 | Complete the first draft in four iterations, drafting by subagents from the outline; British English; first-person past-tense entries for Jonas, close third person for others; style guide in `outline/style.md` | Author's instruction to start filling the story and finish the 400-page novel by iteration four |
| 2026-10-07 | Accepted the act I development suggestions (`notes/act-1-development.md`); act I outlined in 14 chapters; eight characters generated (`characters/`); setting London with real places and invented people and institutions; point of view first-person record entries for Jonas plus third-person chapters for others; the record is a daily handwritten log of collateral warning signs begun at 36 | Author instructed the agent to record the suggestions, write the outline and generate the cast. All details are proposals the author may change |
| 2026-10-03 | The plot device is a global market panic driven by geopolitical risk and national politics. This replaces the fraud at the narrator's firm in branch C; the record and its numbered entries stay | Author's decision |
| 2026-10-03 | Story direction from chapter 1 is branch C, "The record": `#1399` is an entry number in a secret record the narrator has kept since discovering a fraud at their firm around age 37; entry 1399 is the last before they act; chapter 2 shows someone else learning the record exists | Makes `#1399` a device for the whole book, brings in the finance plot without separate setup, and keeps chapter 1 as written. Rejected: A "The exit plan", B "The sentence", D "The diagnosis" (kept in `notes/branches.md`) |
| 2026-10-03 | The project is a ~400-page thriller/action novel with suspense and drama, set in the financial industry | Author's brief |
| 2026-10-03 | Plan length as ~100,000 words | 400 pages at about 250 words per page |
| 2026-10-03 | Track work in IDEA / PLAN / TODO / RELEASE at the repo root | Keeps context in the repo for both people and agents |

## Risks

- **Finance overwhelms story:** technical detail slows the pace. Every explanation has to serve tension.
- **Sagging middle:** act II loses momentum. Plan the midpoint reversal and escalating set pieces in the outline.
- **Authenticity:** errors in the finance or legal detail break trust with informed readers. Research done for clearing, cyber and information security shows act I's core mechanism (a CCP seeing the same gilt pledged twice) does not hold as written; see P1 in `research/corrections-from-research.md`. Have an expert reader check the revision.
- **Real-world politics:** using real countries, leaders and events can date the book and invite dispute. Decide early whether nations and politicians are real, thinly disguised or invented.
- **Scale swallows character:** a global panic can turn into a news report. Keep it seen through the narrator and a small cast with personal stakes.
- **Stalled draft:** a 100,000-word draft is a long haul. Set a weekly word target and track it.
