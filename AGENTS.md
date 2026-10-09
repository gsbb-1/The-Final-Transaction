# AGENTS.md

Guidance for AI agents (and humans) working in this repository.

## Project

**The Final Transaction** is a writing project: a ~400-page thriller/action novel with suspense and drama, set in the financial industry. See [IDEA.md](IDEA.md) for the concept.

This repository holds a manuscript, not software. There is nothing to build or test.

## Working documents

Read these before starting work, and keep them current as you go.

| File | Purpose | Update when |
| --- | --- | --- |
| [IDEA.md](IDEA.md) | The concept: premise, genre, audience, scope, open questions | The premise or scope changes |
| [PLAN.md](PLAN.md) | How the book gets written: milestones, structure, targets, decisions | A milestone is reached or a decision is made |
| [TODO.md](TODO.md) | Concrete next tasks, ordered by priority | A task is started, finished, or discovered |
| [WORKFLOW.md](WORKFLOW.md) | The writing loop: consistency checks, branching, plot development | The way of working changes |
| [RELEASE.md](RELEASE.md) | Draft history and the path to publication | A draft is completed or the publishing plan changes |

Flow: **IDEA** → **PLAN** → **TODO** → **RELEASE**. The idea becomes a plan, the plan is broken into tasks, finished drafts are recorded as releases.

## Repository layout

Folders are created as they are needed.

```
manuscript/   one Markdown file per chapter (01-chapter-title.md)
outline/      synopsis, act breakdown, chapter-by-chapter outline
characters/   one profile per major character
research/     finance mechanics, locations, procedures, sources
notes/        ideas, cut scenes, loose material
```

## Workflow

1. Read `IDEA.md` and `PLAN.md` to understand the story and the current milestone.
2. Before touching a chapter, read its entry in `outline/`, the profiles of the characters in it, and the chapters on either side.
3. Read `outline/style.md` before drafting any prose.
4. Pick the top unchecked item in `TODO.md`, or the one you were asked to do.
5. Do the work in small, focused commits: one chapter or one kind of change per commit.
6. After a chapter is written or revised, run the loop in `WORKFLOW.md`: check consistency, then suggest branches and plot development.
7. Check the item off in `TODO.md` and add any follow-up tasks you discovered.
8. Record significant story decisions in the decision log in `PLAN.md`.

## Rules for working on the story

The author owns the story. An agent's job is to help write the author's book, not its own.

- **Do not invent canon.** Do not decide plot points, character facts, backstory or endings on your own. Propose options and let the author choose. Once chosen, record them in `outline/`, `characters/` or `PLAN.md`.
- **Do what was asked.** A request to proofread is not a request to rewrite. Keep edits to the scope given, and preserve the author's voice, point of view and tense.
- **Stay consistent.** Check names, dates, timelines, amounts of money and character knowledge against the outline, the profiles and earlier chapters. Report contradictions rather than silently choosing one version.
- **Get the finance right.** Financial, legal and procedural details must be accurate or deliberately fictional. Keep sources in `research/`. Say so plainly when you are unsure a detail is correct.
- **Serve the genre.** Every scene should raise tension, reveal character or advance the plot. Explain finance only as far as the reader needs to feel the stakes.
- **Label drafts.** When you write new prose, say that it is a draft for the author to review. Do not overwrite the author's text with your own without being asked.
- **Give honest feedback.** When asked for critique, name real problems with pacing, logic, character or prose, with the specific passage.

## Manuscript conventions

- One chapter per file in `manuscript/`, numbered with two digits so files sort in reading order.
- Each file starts with the chapter heading as `# Chapter N` (and a title, if chapters have titles).
- Mark scene breaks with a line containing only `***`.
- Put notes to self in HTML comments (`<!-- TODO: ... -->`) so they stay out of the exported text.
- Language, point of view and tense: British English; Jonas's chapters are first-person past-tense record entries, other characters are close third person, past tense. Full conventions and shared minor details are in `outline/style.md`. Working choices made on 2026-10-09; the author may change them.

## Tracking progress

- Count words with `wc -w manuscript/*.md`. The target is about 100,000.
- Mark the end of each complete draft with a git tag, as described in [RELEASE.md](RELEASE.md).

## Repository conventions

- Commit messages: short imperative subject line that names the chapter or document, such as `Draft chapter 12` or `Revise midpoint in outline`.
- Never delete cut material; move it to `notes/`.
- Ask before destructive or hard-to-reverse actions: force pushes, deleting or rewriting whole chapters, sending the manuscript to anyone, or publishing.
