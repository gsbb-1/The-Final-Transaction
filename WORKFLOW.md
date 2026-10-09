# WORKFLOW

The writing loop for The Final Transaction: write, check consistency, explore where the story can go, decide, record. Rules for agents are in [AGENTS.md](AGENTS.md); milestones are in [PLAN.md](PLAN.md).

## The loop

```
  1. Write ──► 2. Check consistency ──► 3. Suggest branches and development
     ▲                                                  │
     └──────── 5. Record ◄──────── 4. Author decides ◄──┘
```

| Step | Who | Output |
| --- | --- | --- |
| 1. Write | Author (agent drafts only when asked) | New or revised chapter in `manuscript/` |
| 2. Check consistency | Agent | A consistency report |
| 3. Suggest branches and development | Agent | Branch options and development notes |
| 4. Decide | Author | A choice: fix, keep, or pick a branch |
| 5. Record | Agent or author | Updated continuity ledger, outline and decision log |

The agent reports and suggests. The author decides. Nothing in steps 2 and 3 changes the manuscript.

## When to run it

| Trigger | Consistency check | Branching and development |
| --- | --- | --- |
| A chapter is written or revised | That chapter against canon | Branches from the chapter's ending |
| An act is finished | The whole act | Development review of all open threads |
| Before tagging a draft ([RELEASE.md](RELEASE.md)) | The whole manuscript | Not needed |
| The author is stuck | Not needed | Branches from the current point |

## How to ask

Plain requests are enough:

- "Check consistency of chapter 7."
- "Check consistency of the whole manuscript."
- "Suggest branches from the end of chapter 7."
- "Suggest plot development for act II."
- "Record the decision: we go with branch B."

## Canon: what counts as true

Checks need something to check against. In order of authority:

1. `manuscript/`: what is on the page is canon, earliest chapter first.
2. `outline/continuity.md`: the continuity ledger (below).
3. `outline/`: the synopsis and chapter outline, for what is planned.
4. `characters/` and `research/`: profiles and real-world facts.
5. `IDEA.md` and the decision log in `PLAN.md`.

When two sources disagree, that is itself a finding to report, not something for the agent to settle.

### The continuity ledger

`outline/continuity.md` is the single list of established facts. Create it with the first check and update it in step 5. It has six sections:

| Section | Tracks |
| --- | --- |
| Characters | Name, age, appearance, job, relationships, voice, and the chapter where each fact was established |
| Timeline | Dated or ordered events, in story time, with the chapter each appears in |
| Money | Every amount, account, deal, price and deadline in the plot |
| Knowledge | Who knows what, and from which chapter |
| Places and objects | Locations, layouts, and objects that matter (phones, documents, weapons) |
| Open threads | Setups, questions and promises to the reader that have not been paid off yet |

Every entry cites its chapter, so a fact can be traced to the page.

## Step 2: Consistency check

### What to check

- **Characters:** names and spellings, ages, appearance, history, and whether each person acts and speaks like themselves.
- **Timeline:** order of events, days and dates, travel times, ages against dates, market hours and time zones.
- **Money:** amounts add up and stay the same between chapters; deals, accounts and deadlines match earlier mentions.
- **Knowledge:** no character acts on something they have not learned yet; no one forgets what they know.
- **Places and objects:** locations stay the same; an object is where it was last left.
- **Finance and procedure:** mechanisms, institutions, law and jargon are accurate, or deliberately fictional and noted in `research/`.
- **Point of view and tense:** consistent with the choice recorded in `AGENTS.md`; no slips into a head the narrator cannot see.
- **Plot logic:** causes come before effects; motives are sufficient for actions; no hole a reader would notice.
- **Threads:** every setup is on the open-threads list; every payoff has a setup.

### Report format

Findings only, most serious first. No rewriting.

| # | Where | Finding | Conflicts with | Severity | Possible fix |
| --- | --- | --- | --- | --- | --- |
| 1 | ch. 7, scene 2 | Loan is $40M | $14M in ch. 3 | High | Confirm which figure is intended |

Severity:

- **High:** breaks the plot or a reader will notice.
- **Medium:** a contradiction that a careful reader might catch.
- **Low:** small slips of spelling, detail or wording.

The report ends with new facts the chapter established, ready to add to the ledger, and a list of anything the agent could not verify.

## Step 3: Branching and plot development

### Branching

A branch is one way the story could go from a decision point. The agent offers two to four branches that are genuinely different, never one favourite with weak alternatives.

Each branch states:

| Field | Content |
| --- | --- |
| Name | A short label, such as "B: the partner is the leak" |
| What happens | The next move, in two or three sentences |
| Consequences | What it changes downstream: chapters affected, threads opened and closed |
| What it gives | Effect on tension, stakes, character and the ending |
| What it costs | What it rules out, contradicts or forces to be rewritten |
| Fit | How well it serves the genre mix: thriller, action, suspense, drama |

The agent may say which branch it would choose and why, clearly marked as a recommendation.

### Plot development

A development review looks across the story rather than at one decision:

- **Open threads:** which setups are overdue for a payoff, and which are at risk of being forgotten.
- **Escalation:** whether the stakes and danger rise from chapter to chapter, and where they go flat.
- **Pacing against structure:** where the story stands against the act plan in `PLAN.md`: inciting event, point of no return, midpoint reversal, all-is-lost moment, climax.
- **Character arcs:** whether each major character is changing, and whether the plot is forcing that change.
- **Genre balance:** stretches with too little action, suspense or personal drama, or too much explanation of finance.
- **Reveals:** what the reader knows versus what the characters know, and whether the next reveal is placed for maximum effect.
- **Gaps:** missing scenes, unmotivated turns, underused characters.

Each suggestion names the chapter it applies to and says what problem it solves.

### Trying a branch in git

`main` holds the canon story. To test an alternative without disturbing it:

1. Create a branch: `git switch -c plot/<short-name>`, for example `plot/partner-is-the-leak`.
2. Write or revise the affected chapters there.
3. Run the consistency check on the branch.
4. Decide:
   - **Chosen:** merge into `main`.
   - **Not chosen:** keep the branch, or tag it `alt/<short-name>` and delete the branch. Never throw the text away.

Small alternatives that do not need full chapters go in `notes/branches.md` instead of a git branch.

## Step 5: Record

After the author decides:

- [ ] Fix accepted findings in the manuscript (author, or agent if asked).
- [ ] Add the chapter's new facts to `outline/continuity.md`.
- [ ] Update open threads: add new setups, close paid-off ones.
- [ ] Update the chapter outline in `outline/` if the plan changed.
- [ ] Add a line to the decision log in `PLAN.md` for any chosen branch, with the reason and the options rejected.
- [ ] Add follow-up tasks to `TODO.md`.
