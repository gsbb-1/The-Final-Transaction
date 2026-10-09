# Style guide

Shared conventions for everyone drafting chapters, human or agent. The outline for each act is in this folder; facts are in [continuity.md](continuity.md); profiles are in [../characters/](../characters/README.md).

## Language

- British English spelling and usage (colour, realise, programme, lift, flat, mobile).
- Dialogue in single quotation marks, with double quotes for quotes within speech.
- Numbers: words up to ten, figures above, except money and times, which are always figures (£14m, 7.02am). Entry numbers are written `#1400`.

## Point of view and tense

- **Jonas's chapters** are entries from his record, in first person, past tense, written on the evening of the day they describe. He may address no one, or occasionally Elsie. He never knows what he could not know by the time he writes.
- **Other characters' chapters** are close third person, past tense, one viewpoint character per chapter, named in the outline. No head-hopping.
- Chapter 13 has two viewpoint sections, Jonas then Laura, separated by a scene break.

## Chapter format

Each chapter is one file in `manuscript/`, named `NN-title-slug.md`:

```
<!-- DRAFT: written by agent on YYYY-MM-DD for the author's review. Not canon until accepted. -->
# Chapter N: Title

#1400

Text...

***

Text after a scene break.
```

- The entry number line comes first, alone, exactly as in chapter 1. For third-person chapters it is the entry number of that day.
- Scene breaks are a line containing only `***`.
- Notes to self go in HTML comments. Mark any financial, legal or procedural detail you are not sure of with `<!-- VERIFY: ... -->` immediately after it.
- Length: 1,600 to 2,000 words per chapter. Chapter 1 is the author's and is exempt.

## Voice

- **Jonas:** short sentences, fragments, numbers. He counts things. Dry, precise, not self-pitying. His entries are a man thinking on paper, not a man performing. Match the tone of chapter 1.
- **Third-person chapters:** plainer, controlled, no authorial comment. Let the character's own habits of thought colour the prose: Strand is lawyerly, Crane amused, Al-Mansouri formal, Kessler exact, Pryce hedged, Laura clinical.

## Craft rules

- Every scene raises tension, reveals character or advances the plot. Preferably two of the three.
- Finance is explained only when a character needs it explained to them, and then in plain words, in a paragraph at most. No lectures. The reader must always know what is at stake without knowing how a repo works.
- End every chapter on a turn: a new fact, a decision or a threat. Never on a summary.
- No clichés of the genre: no "little did he know", no mirrors, no characters explaining the plot to each other for the reader's benefit.
- Do not invent major facts (new named characters with speaking parts, large sums, new institutions) beyond the outline and the list below. If a scene needs one, invent the smallest thing possible and list it in your report so it can go in the ledger.
- Do not contradict `continuity.md`. If the outline and the ledger disagree, follow the ledger and report it.

## Shared minor details

Use these so chapters written separately agree.

| Item | Detail |
| --- | --- |
| Whitlock home | A terraced house in Herne Hill, south London. Study on the first floor at the back |
| Laura's surgery | Brixton |
| Elsie's nursery | A few streets from the house |
| The lock-up | A rented garage in a row behind a railway arch in Lewisham, in Jonas's late father's name, rent still paid by Jonas |
| Priya's flat | Bethnal Green, second floor |
| Walbrook Clearing House | Offices near Bank station in the City; trading-floor-style risk room with wall screens |
| Walbrook chief executive | Richard Haldane, 60, smooth, political |
| Walbrook board member close to Crane | Sir Anthony Pell |
| Pryce's Treasury contact | Simon Carrow, a director at the Treasury |
| Greywether Capital | An office on a quiet street in Mayfair; Crane's room has no screens |
| Kessler's firm | Unnamed in act I; three staff; two she uses for surveillance |
| Laura's mother | Margaret, a widow, in a village near Norwich |
| Dinner guests in ch. 3 | Two old friends, Tom and Aisha, a couple; Tom knew Jonas in his trading years |
| Priya's journalist | Rhys Calloway, financial correspondent at a national paper; named in ch. 11, not seen in act I |
| Jonas's notebooks | Plain black A5 hardbacks; about one per five months; nine so far |
| Market timing | Walbrook's main morning margin call at 7am London time; Asian markets open late Sunday evening London time <!-- VERIFY --> |
