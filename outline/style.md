# Style guide

Shared conventions for everyone drafting chapters, human or agent. The outline for each act is in this folder; facts are in [continuity.md](continuity.md); profiles are in [../characters/](../characters/README.md).

## Language

- British English spelling and usage (colour, realise, programme, lift, flat, mobile).
- Dialogue in single quotation marks, with double quotes for quotes within speech.
- Numbers: words up to ten, figures above, except money and times, which are always figures (£14m, 7.02am). Entry numbers are written `#1400`.

## Point of view and tense

- **Jonas's chapters** are entries from his record, in first person, past tense, written on the day they describe, usually in the evening. An entry may be written in more than one sitting, and he says so when it is. He may address no one, or occasionally Elsie. He never knows what he could not know by the time he writes.
- **Other characters' chapters** are close third person, past tense, one viewpoint character per chapter, named in the outline. No head-hopping.
- Chapters 8 (Crane, then Jonas), 13 (Jonas, then Laura) and 28 (Jonas, then Kessler) have two viewpoint sections, separated by a scene break.

## Chapter format

Each chapter is one file in `manuscript/`, named `NN-title-slug.md`:

```
<!-- DRAFT: written by agent on YYYY-MM-DD for the author's review. Not canon until accepted. -->
# Chapter N: Title

Text...

***

Text after a scene break.
```

- There is no stand-alone entry-number line (author's decision, 2026-10-09). The day and, in Jonas's chapters, the entry number are carried in the first lines of prose, as the drafts do. The example above is therefore: draft comment, heading, then prose.
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
| Elsie's nursery | Brambles, on Half Moon Lane, a few streets from the house |
| The lock-up | A rented garage in a row behind a railway arch in Lewisham, in Jonas's late father's name, rent still paid by Jonas |
| Priya's flat | Bethnal Green, second floor |
| Walbrook Clearing House | Offices near Bank station in the City; trading-floor-style risk room with wall screens |
| Walbrook chief executive | Richard Haldane, 60, smooth, political |
| Walbrook board member close to Crane | Sir Anthony Pell |
| Pryce's Treasury contact | Simon Carrow, a director at the Treasury |
| Al-Mansouri's chief of staff | Nasser (surname not given) |
| The misdirected email | Wednesday #1400, 6.41am, from Jonas's personal webmail to his Walbrook address, subject "1399", one photo of the open spread: #1399 on the right, the end of #1398 (gilt lines, a member code, Pryce's initials, "Contained") on the left |
| The memo | Six pages on Walbrook letterhead, written when Jonas was 37, titled "Collateral re-use in cleared markets: a note on concentration and horizon"; "approximately three years" |
| The statement | Two paragraphs on Treasury paper: Walbrook's collateral arrangements are "fully sound and adequate to all foreseeable conditions"; signatures due 6am Monday; released 6.30am over Haldane's name alone |
| Greywether Capital | An office on a quiet street in Mayfair; Crane's room has no screens |
| Kessler's firm | Unnamed in act I; three staff; two she uses for surveillance |
| Laura's mother | Margaret, a widow, in a village near Norwich |
| Dinner guests in ch. 3 | Two old friends, Tom and Aisha, a couple; Tom knew Jonas in his trading years |
| Priya's journalist | Rhys Calloway, financial correspondent at a national paper; named in ch. 11, not seen in act I |
| Jonas's notebooks | Plain black A5 hardbacks with an elastic band; about one per five months. Eight full ones live in a steel toolbox in the lock-up; the ninth, in use, travels with Jonas in his bag and comes home every night. A box of six blank spares is in the study desk. All nine are together in his rucksack from ch. 13 |
| Market timing | Walbrook's overnight run finishes before 7am; calls reach members' payment banks by 8am; deadline 9am by direct debit; intraday calls are threshold-triggered. Early October, BST: Wellington opens 9.50pm, Sydney midnight, Tokyo 1am London time; New York 2.30pm |
| The supervisor | The Bank of England, named as such; the Governor and a Bank supervisor attend the Saturday meeting, neither named |
| The mechanism, in one line | Jonas reads fingerprints (paired fails, cash at nine swapped for bonds in the afternoon, substitutions, leaked position reports) and infers that the collateral behind the system is financing more than one promise. He cannot prove it and says so |
| Priya's exposure | Fri afternoon she pulled the member report under her own login at Jonas's desk after his access was cut; the police's Computer Misuse hook |
| Walbrook's civil order | Interim injunction and delivery-up order, heard by telephone Sunday night, served on the Herne Hill address Monday. "Theft" is the press's and Walbrook's word, never a charge |
| Priya's parents | Leicester; she is there Mon–Thu of week 2 with no phone |
| Jonas's hotel | A cash hotel on a street behind King's Cross; unnamed |
| Rhys Calloway | Financial correspondent at a national paper (unnamed); offices south of the river; flat in Kentish Town; met first in a café in Clerkenwell |
| The Gulf fund's London office | St James's; Al-Mansouri's cousin Faisal runs a private family office at home |
| Park Lane hotel | Where Jonas meets Al-Mansouri in ch. 28; unnamed |
