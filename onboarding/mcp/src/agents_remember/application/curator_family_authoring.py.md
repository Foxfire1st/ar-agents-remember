# mcp/src/agents_remember/application/curator_family_authoring.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/curator_family_authoring.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T07:54+02:00 |
| lastVerifiedCommitHash | `0d7910f9d646161c414ed6543453536a3c749d49` |
| lastVerifiedCommitDate | 2026-09-24T08:10:24+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The curator's family plane as *authored*: the guarantees, memberships and outcomes one hand-off list
declares (ICR-R28@v2).** `read_family_plane` reads that plane out of the list and refuses what is
incoherent, before anything is resolved against a candidate or written. It is the read half of a
three-part seam: `curator_family_planning.py` resolves what this module read into exact identities and
batch commands, and `curator_family_coverage.py` reports what became of it.

**Four decisions are the whole of it, and each refuses something a reader might find convenient:**

| Decision | What is refused |
| --- | --- |
| Nothing is grouped by inference (`:13-17`) | A family exists here exactly when the curator declared one. Two entries citing two constructs of one file, route or label are two obligations with **no** family until a joint obligation between them is authored — no path, label, prefix, shared anchor or shared family key is read as one |
| The guarantee is the family's own text (`:18-19`) | A member's statement is never concatenated into it; the declared text is what travels to the revision that seals it |
| An unexamined entry is not a family-free one (`:20-24`) | Three outcomes stay apart end to end: placed in families, a *deliberate* no-family outcome with its basis, and no family decision at all. The third is reported as unexamined coverage — a measured zero and an unmeasured one lead to opposite actions |
| Reuse is by identity, never by label (`:25-27`) | A declaration naming a `family_id` is checked against the candidate by the planning half; a later guarantee carrying the same label is a **different** record |

**`basis` is required wherever the curator makes a family decision** (`:29-31`): a membership's
justification and a no-family outcome's basis are both authored text, and a blank one is refused rather
than stored as an unexplained claim.

## Code Commentary

### Logic

**The hand-off key is a curator-side key, and its absence is a fact rather than an empty answer.**
`ENTRY_FAMILY_KEY` (`:64-67`) is `"family"`; the producer's thirteen fields are unchanged, and a list
that carries no such key is a list whose family coverage the run reports as **unexamined** rather than
as empty. `FAMILY_MEMBER_STATE` (`"member"`) and `FAMILY_ABSENT_STATE` (`"no_family"`) are the only two
authored states (`:69-75`); an entry with no family key at all is neither, so the three never merge.
`_KEY_MAX` (`:77-79`) bounds one local key at 120 characters, because a hand-off key is a handle rather
than prose and a malformed list is refused **by name**.

**The reading types are the vocabulary the rest of the seam uses.** `FamilyGuarantee` (`:96-112`)
carries the local `key`, the `declared_by` entry, the label and display version, the
`joint_guarantee` text, the declared `predecessor_revision_ids` — which is what makes a changed
guarantee a separately identified **successor** rather than a rewrite of a revision an earlier
membership still cites — and an optional `family_id` that is present *only* when the declaration names
an identity the repository already holds. `FamilyMembership` (`:115-128`) carries the key it joins, its
`basis`, and exactly one of `declaration` (this membership's entry authors the guarantee) or
`stored_family_revision_id` (the membership joins a revision the repository already holds); a membership
with neither joins a key another entry in the same list declares. `FamilyRetirement` (`:131-135`) names
one stored membership by its own identity. `FamilyAssignment` (`:138-145`) is one entry's whole
decision: the state, its basis, what it places, what it retires.

**`FamilyPlaneRead` is the shape that keeps "unexamined" expressible** (`:148-171`). `assignments` is
keyed by entry id and holds **only** entries carrying a family decision, so an entry absent from it is
unexamined rather than family-free — the distinction the report depends on; `declarations` is keyed by
local family key and holds the one declaration each key has; `refusals` carries every entry whose plane
could not be read or whose membership names a key the list does not declare. Two accessors exist for
callers that must ask per entry: `assignment_of` and `refusal_of`.

**`read_family_plane` makes two passes because they are two different questions** (`:174-205`). The
first reads each entry's own decision (`_read_assignment` `:208-229`): a missing key yields neither an
assignment nor a refusal, a non-object is `family_declaration_malformed`, and a `state` outside the two
authored values is `family_state_unknown` — **no default is substituted**, because an unknown state
would silently decide the entry's family coverage. The second asks the *list-level* question one entry
cannot answer: whether every joined key is declared exactly once somewhere in this list
(`_declared_keys` `:464-490`). Both produce per-entry refusals, so a malformed plane refuses the entry
that authored it rather than the whole list, and an entry that was refused is removed from
`assignments`.

**The deliberate no-family outcome is the one that must carry its reason.** `_absent_assignment`
(`:232-252`) requires a non-blank basis (`family_basis_missing`) and refuses memberships riding along
(`family_state_conflict`), because the entry's outcome would then be both and a reader could not tell
which one the curator authored. `_member_assignment` (`:255-297`) accepts an absent `memberships` key
as an empty list — a retirement is authored alone, and an obligation can leave a family without being
placed in another one, so requiring a membership beside it would invent a placement — then still
refuses a `member` decision that authored neither a membership nor a retirement
(`family_membership_missing`), because its state would claim an outcome the curator never authored.

**One membership names exactly one join shape.** `_read_membership` (`:300-335`) requires the key and
the basis, then `_read_declaration` (`:368-410`) reads the guarantee a membership declares — label,
display version and the family's own guarantee text, all three required, with `family_id` and
`predecessor_revision_ids` validated as identities rather than trusted. `_join_shape` (`:338-365`)
refuses a membership that **both** declares a guarantee and names a stored revision
(`family_declaration_conflict`) rather than resolving it by precedence: a declaration authors a new
revision and naming one is the reuse case, so the two are different authored claims about which
revision this membership cites. `_read_retirements` (`:437-461`) requires stored membership identities,
so a removal cannot be authored against a row this run never read.

**One family key carries one guarantee.** `_declared_keys` (`:464-490`) refuses the second declaration
of a key with `family_declared_twice` rather than merging: merging would author one joint obligation out
of two, and dropping one would lose a claim the curator made.

**The question this module deliberately does not answer is the one that needs a dataset.**
`read_family_plane`'s docstring (`:183-187`) states it: whether a membership that names **no**
declaration still resolves is a question about the dataset as much as about the list — the membership
may name a stored `family_revision_id`, and only the candidate knows whether it exists — so it is
answered once, where the candidate is in hand, by `curator_family_planning.plan_entry_family`. **One
refusal, one implementation.**

**Two small helpers carry the reading conventions.** `_authored_text` (`:498-504`) is the one definition
of "authored text": a non-blank stripped `str`, so an absent or whitespace-only field is absent rather
than a stored empty claim. `_uuid_text` (`:507-519`) is the one definition of "an identity field": an
`UUID` or a `str` matching the model's own `UUID_PATTERN`, returned in canonical text, and `None`
otherwise — which is how a malformed identity is distinguished from an absent one at every call site.
`family_refusal` (`:522-525`) truncates the reason to the model's `REFERENCE_MAX_LENGTH`.

**`no_family_condition` is the one place the deliberate outcome becomes a stored sentence**
(`:528-539`). It renders `"Family examination: no joint obligation is supported. Basis: <basis>"`,
bounded by `PROSE_MAX_LENGTH`, and it travels in the revision's own recorded `conditions` — the field
the ingest already uses for the entry's provenance — so the outcome is retained **with the record**
rather than only in a run's report. Its docstring states exactly what was established, which is the same
standard the ingested condition has to meet.

### Conventions

This module reads only: it imports `models.knowledge.base`'s bounds and nothing from the store, the
candidate or the command vocabulary. The declared identities it produces are *local keys*; minting a
family identity belongs to the planning half, and reporting belongs to the coverage half. Every refusal
is an `EntryFamilyRefusal` carrying `(entry_id, code, reason)` and is attached to the entry that
authored it, never to the list.

### Invariants And Boundaries

- A family exists exactly when the curator declared one; no path, label, prefix, anchor or shared key
  is read as a family (`:13-17`).
- The stored guarantee is the family's own text; a member's statement is never concatenated into it.
- `member`, deliberate `no_family`, and no-decision are three facts and never merge (`:20-24`).
- A blank `basis` is refused rather than stored, on both a membership and a no-family outcome.
- One family key has exactly one declaration in a list; a second is refused, never merged.
- A membership both declaring and naming a stored revision is refused rather than resolved by
  precedence.
- Whether a membership naming no declaration resolves is **not** decided here; it is decided once, with
  the candidate in hand, by `plan_entry_family`.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this is the curator-side reading of the repository's
own hand-off vocabulary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for the authored family plane's reading rules. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the module's own declarations.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the four decisions and the basis rule, including that the plane is read before anything is resolved or written.** | "Four decisions are the whole of it"; "The guarantee is the family's own text."; "An unexamined entry is not a family-free one." | mcp/src/agents_remember/application/curator_family_authoring.py:1-32 |
| The published surface: the two hand-off constants, the two authored states, the reading values and the three entry points. | `__all__` | mcp/src/agents_remember/application/curator_family_authoring.py:49-62 |
| **The hand-off key is a curator-side key whose absence is unexamined coverage rather than an empty family.** | `ENTRY_FAMILY_KEY`; "a list that carries no such key is a list whose family coverage" | mcp/src/agents_remember/application/curator_family_authoring.py:64-67 |
| **The two authored states, and the third that is neither.** | `FAMILY_MEMBER_STATE`; `FAMILY_ABSENT_STATE`; `_STATES` | mcp/src/agents_remember/application/curator_family_authoring.py:69-79 |
| One entry's family plane refused: the code that names why, and the sentence that says it. | `EntryFamilyRefusal` | mcp/src/agents_remember/application/curator_family_authoring.py:82-88 |
| **One declared guarantee, whose optional `family_id` means "this names a held identity" and whose declared predecessors make a changed guarantee a successor rather than a rewrite.** | `FamilyGuarantee`; "predecessor_revision_ids" | mcp/src/agents_remember/application/curator_family_authoring.py:96-112 |
| **One membership: the key it joins, its basis, and exactly one of a declaration or a stored revision.** | `FamilyMembership` | mcp/src/agents_remember/application/curator_family_authoring.py:115-128 |
| A stored membership retired by its own identity. | `FamilyRetirement` | mcp/src/agents_remember/application/curator_family_authoring.py:131-135 |
| One entry's whole decision: the state, its basis, what it places and what it retires. | `FamilyAssignment` | mcp/src/agents_remember/application/curator_family_authoring.py:138-145 |
| **The read shape that keeps "unexamined" expressible: assignments hold only entries that decided something.** | `FamilyPlaneRead`; "an entry absent from it is unexamined rather than family-free" | mcp/src/agents_remember/application/curator_family_authoring.py:148-171 |
| **The two passes: each entry's own decision, then the list-level question of whether every joined key is declared exactly once.** | `read_family_plane`; "Two passes, because the two are different questions." | mcp/src/agents_remember/application/curator_family_authoring.py:174-205 |
| **A missing family key is neither an assignment nor a refusal, and an unknown state substitutes no default.** | `_read_assignment`; "family_state_unknown" | mcp/src/agents_remember/application/curator_family_authoring.py:208-229 |
| **The deliberate no-family outcome: its basis is required, and no membership may ride along.** | `_absent_assignment`; "family_basis_missing"; "family_state_conflict" | mcp/src/agents_remember/application/curator_family_authoring.py:232-252 |
| **A member decision that authored neither a membership nor a retirement is refused, because its state would claim an outcome the curator never authored.** | `_member_assignment`; "family_membership_missing" | mcp/src/agents_remember/application/curator_family_authoring.py:255-297 |
| One authored membership: the key it joins, the basis, and how it joins. | `_read_membership` | mcp/src/agents_remember/application/curator_family_authoring.py:300-335 |
| **Declaring and naming a stored revision are refused together rather than resolved by precedence.** | `_join_shape`; "family_declaration_conflict" | mcp/src/agents_remember/application/curator_family_authoring.py:338-365 |
| The guarantee one membership declares, with label, version and the family's own text all required. | `_read_declaration` | mcp/src/agents_remember/application/curator_family_authoring.py:368-410 |
| The declared predecessor set, read as identities rather than trusted as text. | `_predecessors` | mcp/src/agents_remember/application/curator_family_authoring.py:413-434 |
| **A retirement names a stored membership identity, so a removal is never authored against a row this run did not read.** | `_read_retirements`; "family_retirement_malformed" | mcp/src/agents_remember/application/curator_family_authoring.py:437-461 |
| **One family key carries one guarantee; a second declaration is refused rather than merged or dropped.** | `_declared_keys`; "family_declared_twice" | mcp/src/agents_remember/application/curator_family_authoring.py:464-490 |
| The one definition of authored text, and the one definition of an identity field. | `_authored_text`; `_uuid_text` | mcp/src/agents_remember/application/curator_family_authoring.py:498-504; mcp/src/agents_remember/application/curator_family_authoring.py:507-519 |
| The refusal constructor, bounded by the model's own reference length. | `family_refusal` | mcp/src/agents_remember/application/curator_family_authoring.py:522-525 |
| **The deliberate no-family outcome as the one stored sentence it becomes, travelling in the revision's own recorded conditions.** | `no_family_condition`; "Family examination: no joint obligation is supported. Basis: " | mcp/src/agents_remember/application/curator_family_authoring.py:528-539 |
| **The question this module deliberately leaves to the half that holds the candidate: whether a membership naming no declaration still resolves.** | "One refusal, one implementation." | mcp/src/agents_remember/application/curator_family_authoring.py:183-187 |
| The bounds this module reads rather than restates. | `LABEL_MAX_LENGTH`; `PROSE_MAX_LENGTH`; `REFERENCE_MAX_LENGTH`; `UUID_PATTERN` | mcp/src/agents_remember/models/knowledge/base.py:1-40 |
| The half that answers the question above, against the candidate. | `plan_entry_family` | mcp/src/agents_remember/application/curator_family_planning.py:536-595 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A hand-off list, an entry id and a local
family key are all properties of one coordination root's own curator input, and nothing here names,
reads or writes another repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base
  `63b476297708f779de8ed5c0bf3555b9d1de70c2`): created this one-to-one card for the module
  `ICR-R28@v2` introduced as **the curator's authored family plane**. The stamp basis is honest rather
  than convenient: the module is untracked at the base commit, so `lastVerifiedCommitHash` names the
  leaf's base commit and the verified basis is the working-tree delta on top of it — no commit contains
  what a stamp would otherwise claim to have verified. What a reader has to carry away is the **three
  outcomes the plane keeps apart**: an entry placed in families, an entry with a *deliberate* no-family
  outcome recorded with its basis, and an entry the curator never examined — the last being neither of
  the first two, and never reported as an empty family. The reading half also states the boundary a
  reader is most likely to misplace: whether a membership that names no declaration still resolves is
  **not** decided here, because only the candidate knows whether the stored revision exists, so it is
  answered once by `curator_family_planning.plan_entry_family`. No verification stamp beyond the leaf's
  base is advanced: the candidate is uncommitted and the governed closeout owns the real commit.
