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

## Publication checklist

The publishing route is not yet decided. Choose one, record the decision in `PLAN.md`, and delete the list that does not apply.

### Before either route

- [ ] Final manuscript complete (`final` tag)
- [ ] Title confirmed
- [ ] Synopsis written (one page)
- [ ] Back-cover blurb written
- [ ] Author biography written

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

### In progress — M0 Concept

- 2026-10-03: Project set up; brief defined as a ~400-page financial thriller. No manuscript text yet.

<!--
### draft-N — YYYY-MM-DD

- Word count:
- Chapters:
- What changed since the previous draft:
- Known problems to fix in the next pass:
-->
