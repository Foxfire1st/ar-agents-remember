# mcp/src/agents_remember/application/review_family_context.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_family_context.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T22:10:00+02:00 |
| lastVerifiedCommitHash | `fdf3e4b6cfe73040d35cbfd4d8b93fd55369e499` |
| lastVerifiedCommitDate | 2026-09-23T22:41:36+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The composition the accepted family-centred reviewer needs, and neither `ICR-R09@v1`'s flat subject
catalogue nor `ICR-R08@v1`'s movement union produces (ICR-R31@v1).** For the review's selected subject
it composes *which recorded families that subject belongs to on each of the two bound snapshots, each
selected family revision's own authored joint guarantee, and that revision's complete recorded member
roster — unchanged siblings included* — into the values declared by
`mcp/src/agents_remember/models/knowledge/review_family_context.py`.

**It composes; it duplicates no owner** (`:10-27`). Three owners are called:

| Owner | What it answers here |
| --- | --- |
| the selection policy `recorded-family-frontier/v1`, through the shipped read operation `read_knowledge_scope` | one read per side with the reviewed identity's own seed answers which family revisions the seed reaches directly — the policy's frozen family set, computed before any page is cut and therefore complete whatever budget the page applied |
| `ICR-R07@v1`'s own `revision_heads` | run over the selected family revisions and the snapshots' own authored predecessor edges: this module chooses no revision by label, by version or by order, and an ambiguous or cyclic lineage is carried as exactly that with its inspectable candidate heads |
| `mcp/src/agents_remember/application/review_family_rosters.py` | reads one selected revision's guarantee, roster, member content and page, and verifies the family revision's seal; the recorded movements are `ICR-R08@v1`'s own values, passed in and *referenced* by identity |

**What it refuses** (`:29-34`): no family is inferred from a folder, a label, a shared source file or a
similarity score; no guarantee is derived from members; no revision is chosen when the authored lineage
leaves several heads; and no verdict about a member's consequence for its family's guarantee exists
anywhere in the value this returns. A snapshot that does not record the reviewed identity reports
`not_recorded` on that side, a read the owner refused reports `unreadable` with the owner's own words,
and a measured zero is spelled `no_family_recorded` rather than `empty`.

**Continuation** (`:36-41`): the one bounded collection this composition continues is *one family
revision's recorded member roster*, under the review surface's `family_members` collection name. The
cursor is the read owner's own, minted for one snapshot and one family revision and presented back
through the same owner, so a cursor for another snapshot or another family revision is refused by that
owner rather than reinterpreted here, and the response serves the first page of every family context it
composed instead of a page stitched from two states.

## Code Commentary

### Logic

**One value carries everything one measurement read.** `FamilyContextSources` (`:113-133`) holds the two
datasets, the namespace they are bound to, the two bound code trees, the reviewed selector, the
relationship union and the page size, because they are one measurement: a roster read from another
snapshot, a guarantee read under another namespace, or a movement reference taken from another review
would be a different comparison wearing this one's identity. `FamilyContextOutcome` (`:136-148`) carries
the composed context with **either** the continued page **or** the refusal a presented cursor earned —
never both, because a cursor is either continued or refused.

**The axis is a value because each one names a different recorded fact.** `_AXIS_FAMILY_IDENTITY`,
`_AXIS_FAMILY_REVISION` and `_AXIS_INVARIANT` (`:151-157`) say which question a family selection asked,
which decides both the population the head rule runs over and the sentence the selection publishes.
`_SELECTION_BASIS` (`:159-167`) and `_ADDED_BASIS` (`:169-174`) supply each axis's own clause for the
paired and the one-sided case, so no sentence borrows another axis's wording.

**Two populations travel together, and they are deliberately different.** `_FamilyRevisions`
(`:177-211`) carries the populations the head rule runs over (`before`/`after`), the heads it established
(`before_heads`/`after_heads`), and the family owner's own lists (`before_recorded`/`after_recorded`).
`other_recorded` (`:197-211`) reads the two snapshots as **one history**: a revision both retain is one
revision, so a count over it can never be inflated by a revision recorded twice and can never understate
the history either, because it is the owner's own list rather than the population this composition
selected. `_Applicable` (`:214-251`) is one side's populations or the stated reason none could be
reported; its `absent` is the **measured** answer that this snapshot records no such identity (so no
family is applicable and none is missing), while `reason` is a read that did not serve a page at all —
the two are never collapsed, because one is a fact about the snapshot and the other a part this
composition could not establish.

**The entry guards answer before any side is opened.** `review_family_context` (`:254-301`) returns a
stated context for a review that selected no subject (`no_subject_selected`, because a task-context
review compares no knowledge operand and claims nothing) and for a seed kind whose recorded families
this composition does not resolve (`unavailable`, substituting no identity), then opens both sides and
closes both in a `finally` block. `_compose` (`:304-338`) reads both sides' applicable families, states
`unavailable` when **neither** side's scope could be read, states the measured zero when no family is
applicable, and otherwise composes one entry per applicable family.

**The outcome's state is composed from the entries, not asserted.** `_outcome` (`:341-379`) reports
`recorded` only when every entry is complete **and** neither side is unread, `partial` otherwise, with
`limitations` naming each unread side and its reason. `_context_detail` (`:395-419`) states the complete
sentence or names every incomplete part with its reason, truncated to the model's own prose bound.
`_unique_members` (`:382-392`) counts the **distinct** member revisions behind every roster carried, so
a member shared by two families is visibly one revision and two rows.

**Every one-sided sentence states the axis's own recorded fact.** `_axis` (`:422-430`) maps the selector
to its axis; `_not_recorded_detail` (`:433-458`) states, for the axis the selection was made on, why a
side selected nothing — an invariant whose membership this snapshot does not record, a selection naming
an exact revision this snapshot does not record, or a family this snapshot records no revision of at all
— and each sentence also names **how many revisions of the family this snapshot does record**, so an
empty selection is never read as an empty family. `_no_family` (`:461-489`) states the measured zero, or
the stated failure to measure it when a side could not be read; for a family selection it is reachable
only when neither snapshot records the family at all, because a family a snapshot records with no
memberships has a context of its own (its guarantee and a measured empty roster). `_required_selector`
(`:501-512`) states for the type checker what the entry guard already established.

**The fix this leaf needed is the population rule, and it is split by axis.**
`_applicable` (`:515-535`) dispatches on the selector: a family selection is answered from the family
owner, an invariant selection keeps the policy's own answer. `_applicable_family` (`:538-562`) reads
`families.list_family_revision_ids` and `families.get_family`, and its population for a family-identity
selection is **every revision the family owner records** — because the selection *is* the family and a
revision that cites no member is still a revision of it; a `FamilyRevisionSeed` instead names one exact
revision, so its population is that revision where the snapshot records it (an explicit revision choice
is not a head selection) while the family's whole recorded list still travels for the counts. A snapshot
that records neither the identity nor any revision of it answers `absent`. This is the fix: deriving the
population from membership-bearing read rows made a memberless head invisible, which silently resolved
an authored ambiguity and made a family with a recorded guarantee and no members read as no family at
all. `_applicable_invariant` (`:565-597`) keeps the policy's frozen family set — the families whose
recorded memberships cite a selected revision are the applicable families, and the revisions that cite
it are the ones whose rosters that subject's context is about — while still reading each applicable
family's **whole** recorded revision list from the owner for the counts the sentences publish. A
`selector_absent` refusal is that side's `absent` (a measured fact); any other refusal is its `reason`.

**One entry per family, and the head rule is the packet's own.** `_entry` (`:603-662`) builds the
`_FamilyRevisions`, states the selection, and — for an unresolved or ambiguous selection — returns the
unresolved entry with its candidate guarantees and no roster read at all. Otherwise it reads both sides'
rosters, offering the presented cursor to the before side first and to the after side only when the
before read did not bind it (`:644`), so a continuation advances exactly one walk. `_roster_request`
(`:665-670`) carries the page bound, the movement union and the cursor; `_bound_page` (`:673-678`) names
the page of the one read that served the cursor; `_heads` (`:681-686`) applies `revision_heads` to the
population with `_touching` (`:689-701`), which keeps only the authored edges whose two endpoints are
both inside that population — so a head is decided by the snapshot's own lineage and nothing else.

**The selection states what it established, in `ICR-R07@v1`'s own vocabulary.** `_selection`
(`:704-750`) maps the head counts to `compared` / `added` / `removed` / `ambiguous` / `unresolved` and
carries each established pair with its statement; `_selection_state` (`:753-765`) is that decision table.
`_selection_sentence` (`:768-803`) states the established pair or the one-sided addition or removal and
**measures the history from the family owner's own revision lists on both snapshots**, not from the
population this composition happened to select (`:777-782`) — the fix-round-1 correction to a sentence
that printed `0 other recorded revision(s)` while the store recorded further revisions of the same
family. `_unresolved_sentence` (`:806-839`) states an ambiguous or lineage-failed selection with its
heads and its reason, and names whether the axis was an invariant's memberships or a family's own
revisions. `_unresolved_entry` (`:842-867`) carries each candidate head's **own** guarantee and no
chosen revision, with `family_guarantees` (`:870-883`) reading those guarantees from the family owner.
`_label` (`:886-902`) prefers the candidate's recorded label because that is the side a reader acts on,
and a family only the baseline records keeps the baseline's wording rather than receiving a label
nothing recorded. `_entry_state` (`:905-917`) makes an entry `unavailable`, `partial` or `recorded` from
its sides' own states, a truncated page and any member whose content fell outside the page;
`_entry_detail` (`:920-929`) carries the selection's sentence and each side's sentence together.

### Conventions

`__all__` (`:94-99`) publishes only the collection name, the two request/outcome values and the entry
point. The module imports the shipped read operation, the roster module's own values and helpers,
`revision_heads` from `ICR-R07@v1`'s comparison owner, the family owner, and the value vocabulary it
composes (`:44-92`); it defines no SQL, opens no database itself (the roster module does) and closes both
sides it opens. All prose is bounded by `PROSE_MAX_LENGTH` from the model layer, and the module-level
constants (`:101-110`, `:151-174`) are declarative tables rather than logic, so a reader can see each
axis's clauses without executing anything.

### Invariants And Boundaries

- **Forced determinacy is the failure mode this module is built against.** Several legitimate heads stay
  several: the state is `ambiguous` with every head carried as an inspectable candidate and **no**
  revision chosen, and no guarantee is presented as the family's own on such a selection.
- **A family selection's revision population is the family owner's own list, never a
  membership-derived one.** A revision that cites no member is still a revision of its family, and a
  family a snapshot records with a guarantee and no members is a `recorded` context with a **measured**
  empty roster rather than a measured zero of the family population.
- **Every count in every sentence is measured against the owner that holds the fact.** The history
  sentence reads the family owner on both snapshots and de-duplicates a revision both retain; the
  unique-member total counts distinct revisions rather than rows.
- **The composition reads and states; it concludes nothing.** No field it produces can hold a verdict
  about a member's consequence for its family's guarantee, and the relationship union's movements are
  referenced by identity and never re-stated as a transition.
- **Continuation cannot cross a walk.** The cursor is the read owner's own, offered to at most one roster
  walk per response, and every other family context is served its first page.

### Todos

None recorded.

## Docs References

No configured domain documentation could be consulted for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category — its whole body is "No entries
configured yet." — so there is no external or domain source to check and no documentation row is
recorded here.

## Repo-Internal References

Every claim on this card is checkable in the module's own declarations and in the owners it calls. The
four details a reader should carry: **a family selection's revision population is the family owner's own
list**, which is what makes a memberless head a head and a guarantee-bearing memberless family a
recorded context rather than a measured zero; **the history sentence is measured against that same
owner on both snapshots**, never against the population this composition selected; **several legitimate
heads stay several**, carried as inspectable candidates with no revision chosen and no guarantee
presented as the family's own; and **the composition concludes nothing about a member's consequence for
its family's guarantee**.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The composition's own statement of what it builds, the three owners it calls and the four things it refuses.** | "It composes; it duplicates no owner." | mcp/src/agents_remember/application/review_family_context.py:1-42 |
| The published surface: the collection name, the two values and the entry point. | `__all__` | mcp/src/agents_remember/application/review_family_context.py:94-99 |
| The read owner's own code for "this snapshot records no such identity" — a measured answer, not a read failure. | `_SELECTOR_ABSENT` | mcp/src/agents_remember/application/review_family_context.py:101-103 |
| The seed kinds this composition resolves, and the seed kinds whose recorded families it does not. | `_FAMILY_SEED_KINDS`; `_INVARIANT_SEED_KINDS`; `_IDENTITY_SEED_KINDS` | mcp/src/agents_remember/application/review_family_context.py:105-110 |
| **Everything one measurement read travelling as one value, so a roster, a guarantee or a movement from another comparison cannot wear this one's identity.** | `FamilyContextSources` | mcp/src/agents_remember/application/review_family_context.py:113-133 |
| The composed context with either the continued page or the refusal a cursor earned, never both. | `FamilyContextOutcome` | mcp/src/agents_remember/application/review_family_context.py:136-148 |
| **The three axes a family selection can ask on, because each names a different recorded fact.** | `_AXIS_FAMILY_IDENTITY`; `_AXIS_FAMILY_REVISION`; `_AXIS_INVARIANT` | mcp/src/agents_remember/application/review_family_context.py:151-157 |
| The clause each axis states about the revision pair it selected. | `_SELECTION_BASIS` | mcp/src/agents_remember/application/review_family_context.py:161-167 |
| The clause each axis states about a one-sided selection, where there is no pair at all. | `_ADDED_BASIS` | mcp/src/agents_remember/application/review_family_context.py:170-174 |
| **The two populations that deliberately differ: the revisions the head rule runs over, and the family owner's own recorded lists.** | `_FamilyRevisions` | mcp/src/agents_remember/application/review_family_context.py:177-211 |
| **The history read as one history across both snapshots, de-duplicated so a revision recorded twice is counted once and a memberless revision is counted at all.** | `other_recorded` | mcp/src/agents_remember/application/review_family_context.py:197-211 |
| **One side's populations, where a measured absence and an unread part are never collapsed.** | `_Applicable` | mcp/src/agents_remember/application/review_family_context.py:214-251 |
| **The entry point: the guards for a subjectless review and an unresolvable seed kind, then both sides opened and closed once.** | `review_family_context` | mcp/src/agents_remember/application/review_family_context.py:254-301 |
| The compose step: both sides' applicable families, then one entry per family. | `_compose` | mcp/src/agents_remember/application/review_family_context.py:304-338 |
| **The state composed from the entries rather than asserted, with each unread side named as a limitation.** | `_outcome` | mcp/src/agents_remember/application/review_family_context.py:341-379 |
| **The distinct member revisions behind every roster carried, so a shared member is one revision and two rows.** | `_unique_members` | mcp/src/agents_remember/application/review_family_context.py:382-392 |
| The one sentence naming the state and, when partial, exactly which parts are incomplete. | `_context_detail` | mcp/src/agents_remember/application/review_family_context.py:395-419 |
| Which question the reviewed selector asks, in the vocabulary the sentences are built from. | `_axis` | mcp/src/agents_remember/application/review_family_context.py:422-430 |
| **The one-sided sentence per axis, each also naming how many revisions of the family this snapshot does record.** | `_not_recorded_detail` | mcp/src/agents_remember/application/review_family_context.py:433-458 |
| **The measured zero — reachable for a family selection only when neither snapshot records the family at all — kept apart from the stated failure to measure it.** | `_no_family` | mcp/src/agents_remember/application/review_family_context.py:461-489 |
| One context that carries a state and its sentence and no family at all. | `_stated` | mcp/src/agents_remember/application/review_family_context.py:492-495 |
| The selector every path past the entry guard has already established. | `_required_selector` | mcp/src/agents_remember/application/review_family_context.py:501-512 |
| **The dispatch by axis, where a family selection is answered from the family owner and an invariant selection keeps the policy's own answer.** | `_applicable` | mcp/src/agents_remember/application/review_family_context.py:515-535 |
| **The fix: a family selection's population is every revision the family owner records, because a revision that cites no member is still a revision of it.** | `_applicable_family` | mcp/src/agents_remember/application/review_family_context.py:538-562 |
| **The invariant selection's population from the policy's own frozen family set, with the family's whole recorded list read for the counts.** | `_applicable_invariant` | mcp/src/agents_remember/application/review_family_context.py:565-597 |
| **One family's context: its selection, its two sides, and — for a selection that chose nothing — its candidate guarantees with no roster read.** | `_entry` | mcp/src/agents_remember/application/review_family_context.py:603-662 |
| The page bound, movement union and cursor one roster read is asked for. | `_roster_request` | mcp/src/agents_remember/application/review_family_context.py:665-670 |
| The page of the one read that served the presented cursor. | `_bound_page` | mcp/src/agents_remember/application/review_family_context.py:673-678 |
| **The heads of one side's population, through `ICR-R07@v1`'s own rule.** | `_heads` | mcp/src/agents_remember/application/review_family_context.py:681-686 |
| The authored edges whose two endpoints are both inside one selected population. | `_touching` | mcp/src/agents_remember/application/review_family_context.py:689-701 |
| **The selection stated in `ICR-R07@v1`'s own value and vocabulary, with no revision chosen when several heads stand.** | `_selection` | mcp/src/agents_remember/application/review_family_context.py:704-750 |
| The decision table from head counts to the selection state. | `_selection_state` | mcp/src/agents_remember/application/review_family_context.py:753-765 |
| **The sentence whose history is measured from the family owner's own revision lists on both snapshots rather than from the selected population.** | `_selection_sentence` | mcp/src/agents_remember/application/review_family_context.py:768-803 |
| **The sentence stating an ambiguous or lineage-failed selection with its heads and its own reason, naming the axis it was made on.** | `_unresolved_sentence` | mcp/src/agents_remember/application/review_family_context.py:806-839 |
| One family context that chose no revision: its candidate heads and their own guarantees. | `_unresolved_entry` | mcp/src/agents_remember/application/review_family_context.py:842-867 |
| Each named revision's own guarantee from the family owner, or nothing when it is not readable. | `family_guarantees` | mcp/src/agents_remember/application/review_family_context.py:870-883 |
| The family's recorded label and the snapshot it was read from, with the candidate's label winning. | `_label` | mcp/src/agents_remember/application/review_family_context.py:886-902 |
| Whether two sides make a complete family context, a partial one or an unavailable one. | `_entry_state` | mcp/src/agents_remember/application/review_family_context.py:905-917 |
| The entry's detail carrying the selection's sentence and each side's own sentence. | `_entry_detail` | mcp/src/agents_remember/application/review_family_context.py:920-929 |
| The values this composition builds, whose validators refuse every false shape. | `ReviewFamilyContextEntry` | mcp/src/agents_remember/models/knowledge/review_family_context.py:337-421 |
| **The roster read that supplies each side's guarantee, members and page, and refuses a cursor another walk minted.** | `read_family_roster` | mcp/src/agents_remember/application/review_family_rosters.py:209-272 |
| **The production review read that calls this composition once, after the relationship union its member contexts reference.** | `compose_review` | mcp/src/agents_remember/application/knowledge_review.py:371-611 |
| The collection the request names to continue one roster walk. | `ReviewPagedCollection`; `REVIEW_PAGED_COLLECTIONS` | mcp/src/agents_remember/models/knowledge/review.py:171-176 |
| **The cases that pin the memberless-shape ambiguity, the recorded empty family and the owner-measured history sentence.** | `test_the_canonical_memberless_successor_shape_is_an_ambiguity`; `test_a_recorded_family_with_no_members_is_recorded_not_absent`; `test_the_history_sentence_is_measured_against_the_family_owner` | mcp/tests/test_review_family_context_population.py:94-279 |

## Cross-Repo References

No cross-repository behavior is implemented in this module. The two datasets it reads, the namespace it
binds them to and the two code trees it passes on are the values one leaf's own resolution selected; the
movement union it references belongs to the same review payload, and the cursor it continues is minted
by the same local read owner. No remote, credential, network or external system appears anywhere in this
composition, so no cross-repo reference row is recorded — no cited range proves a repository or
external-system boundary.

## Update History

- 2026-09-23T22:10:00+02:00 — 260921-ICR-L31 curator (uncommitted change set on `ar/260921-icr-l31`, base `4c000b11c5243e4a8e77c08e87984fff00c1d94b`): created this one-to-one card for the composition `ICR-R31@v1` introduced as **the comparison-bound family review context**. The stamp basis is honest rather than convenient: the module is untracked at the base commit, so `lastVerifiedCommitHash` names the leaf's base commit, and the verified basis is the working-tree delta on top of it — no commit contains what a stamp would otherwise claim to have verified. The card records what a consumer has to act on, including the leaf's one real defect and its fix, because a reader who takes only the shape away would repeat it: **a family selection's revision population is the family owner's own revision list and never a membership-derived one** (`_applicable_family`), since a family revision that cites no member is still a revision of its family — deriving the population from membership-bearing rows made the canonical memberless-successor shape look like a `compared` pair naming the superseded revision, printed `0 other recorded revision(s)` while the store recorded more, and rendered a guarantee-bearing memberless family as `no_family_recorded` with its guarantee dropped. The history sentence now measures the family owner on both snapshots and de-duplicates a revision both retain (`_selection_sentence`), the rejected-selection sentence names the axis it was made on, and several legitimate heads stay several with every head carried as an inspectable candidate and no guarantee presented as the family's own. Continuation remains one roster walk of one snapshot, served for the first page of every other family context.
