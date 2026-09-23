# mcp/src/agents_remember/application/review_family_rosters.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_family_rosters.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T22:10:00+02:00 |
| lastVerifiedCommitHash | `fdf3e4b6cfe73040d35cbfd4d8b93fd55369e499` |
| lastVerifiedCommitDate | 2026-09-23T22:41:36+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The recorded roster of one selected family revision, read and stated for the review context
(ICR-R31@v1).** For one exact family revision, `ICR-R31@v1`'s context needs the roster its author
recorded: every membership row, each member's exact invariant revision and its recorded content, the
realization claims that reach source expressions, and the page and cursor that reach the rest. This
module owns that read and the values it states; *which* families and revisions a review context is about
is the composition's decision, one module over in
`mcp/src/agents_remember/application/review_family_context.py`, which calls this module.

**Three owners are called and none is duplicated** (`:10-16`): the **selection policy** runs through the
shipped read operation `read_knowledge_scope` with an exact `FamilyRevisionSeed`, so the roster, its
counts and its snapshot-bound continuation are the read owner's own; the **authored guarantee** comes
from the family owner, which verifies the revision's payload seal on the way out; and the **sharing
fact** — the other family revisions one member revision is recorded in — comes from the membership
owner.

**What it refuses is the shape of every value below** (`:18-21`): a side that was not read states which
fact it is instead of an empty roster, a membership row whose revision content fell outside the page is
stated as `content_not_on_page` rather than filled in from a second selection, and the guarantee is
never assembled from the members it is stored beside.

## Code Commentary

### Logic

**The collection name is a constant because a cursor and the walk it belongs to must not be paired by
guesswork.** `FAMILY_MEMBERS_COLLECTION` (`:81-84`) is `family_members`: the name a request presents its
cursor under and the name the payload's page states. `_CURSOR_MISMATCH` (`:86-88`) is the read owner's
own refusal code for "this cursor binds another selection" — the one answer that means the cursor belongs
to a walk this read is not positioned in.

**Two small request values, each keeping one request's parts together.** `RosterReadRequest`
(`:91-103`) carries the page bound, the relationship union's movements and the cursor, because a caller
able to pass two of them could state a page whose bound and position disagree. `RosterContext`
(`:106-124`) carries which revision the read is for and the two facts that qualify it: the family
owner's own `recorded_revision_ids` for the side, and `not_recorded_detail` — the sentence stating which
fact a one-sided selection is, which **differs by the axis the selection was made on** (an invariant
records no membership here; a family records no such revision), so the composition that knows the axis
supplies the sentence rather than this module guessing it.

**One snapshot, opened once, and its failure kept as a state.** `FamilyRosterSide` (`:130-148`) is one
bound snapshot: its store, its read context, every authored `(successor, predecessor)` edge, and
`unreadable` — the reason the side could not be opened at all, in which case every family context on
that side states that reason rather than an absence. `open_family_side` (`:167-188`) opens all three and
turns a storage error, an OS error or a value error into `unreadable` with the error's own type and
message rather than raising. `_authored_edges` (`:191-203`) reads the predecessor edges over a read-only
connection — the same values `ICR-R07@v1`'s selection reads — so a head rule applied to them is applied
to the snapshot's own authored lineage and to nothing a caller derived.

**The read states each fact it established and nothing it did not.** `read_family_roster` (`:209-272`)
answers one snapshot's context for one family: a selection that established no revision on this side
returns the `not_recorded` sentence the composition supplied (`:217-221`); a side that could not be
opened or read returns `unreadable` with the owner's or the opener's own words (`:222-247`), including
the case where the family revision is in the selected set but the family owner returned no sealed
aggregate for it — no guarantee is then presented for it; and the recorded path composes the side from
the guarantee, the page, the members and the exact revision (`:256-272`). `FamilyRosterRead` (`:151-164`)
carries what the offered cursor did: `bound` is true when *this* read served the presented cursor, which
is how the response knows which of its family contexts the published page belongs to, and
`cursor_refusal` is the owner's own refusal when the cursor was offered here and this walk did not mint
it.

**A cursor another walk minted is a routing fact, not a fact about the side.** `_read_roster`
(`:275-305`) offers the request's cursor to this walk; when the owner refuses it with
`continuation_binding_mismatch` the side is read **again from its own first page** and the refusal is
carried back so the response can state once that no walk it composed bound the cursor. `_roster_read`
(`:308-328`) is one read at the request's own page bound. `_roster_page` (`:331-355`) states the read
owner's own page — its counts, its `enumeration_complete` and its continuation — with a scope naming the
exact side, family revision, policy version and page size, so a reader never has to guess which of the
response's family contexts the published page is about.

**Every sentence is built from the values the read returned.** `cursor_refusal_detail` (`:358-363`)
names the case where the read returned neither a page nor a usable refusal. `_roster_detail`
(`:366-381`) states either that the roster was read whole with its count, or how many memberships the
page carried against the owner's total, the remainder and the fact that the continuation reaches it.
`side_statement` (`:384-394`) is the one side context that carries no roster and no count at all.

**The guarantee comes from the owner that verifies its seal.** `family_guarantee` (`:400-418`) reads one
family revision through the family owner and returns its stored `joint_guarantee` with the display
version, origin state, acceptance reference, provenance and payload digest — or `None`, in which case the
caller states an unreadable side rather than presenting a guarantee it did not get.

**A membership row is the recorded fact and is always carried.** `_members` (`:421-455`) walks the
page's membership rows; each member's revision **statement** is carried only when the same page selected
that revision, and is otherwise stated as `content_not_on_page` rather than filled in from a second read
of a different selection. `_RosterLookups` (`:458-470`) keeps one page's own lookups together — content
items, claim references and union identities — because a content item paired with another page's claims,
or a movement identity taken from another review, would be a different roster wearing this one's
membership rows. `_member` (`:473-499`) composes the row: the exact `invariant_revision_id`, the
member's identity and label, its content when the page carried it, the other family revisions the
membership owner records it in, the realization-claim references, and a `movement_reference` set only
when the relationship union's own values display this membership row. `_member_identity` (`:502-515`)
falls back to the store owner for the identity when the page did not carry the revision;
`_other_families` (`:518-534`) reads the sharing fact from the membership owner and excludes this family
revision; `_source` (`:537-557`) states one realization claim with the address this read observed and
the resolution it reached, or states that no address was observed; `_member_detail` (`:560-582`) states
which facts of the row the read established, including how many further family revisions record the same
exact revision; `_movement_identities` (`:585-595`) collects the membership identities the union's own
movement values display.

**The page and the refusals are the surface's own vocabulary.** `family_member_page` (`:601-623`) states
one continued roster walk as `ICR-R10@v1`'s `ReviewCollectionPage`, carrying the read owner's own
`primary_items_total`, `primary_items_returned` and `primary_items_remaining` and its opaque
snapshot-bound continuation, with a scope naming the exact side and family revision.
`family_collection_refusal` (`:626-644`) answers a request that named the collection **without** a
cursor: this collection is a *set* of per-family walks rather than one walk, so naming it addresses no
single page, and the response still carries every walk's first page on the family contexts themselves.
`family_context_cursor_refusal` (`:647-685`) answers a cursor that bound no composed walk in the
surface's own vocabulary: a malformed token earns `comparison_page_unreadable` with the action sentence
naming what a real cursor looks like, while a well-formed cursor that bound nothing earns
`comparison_page_reset` with this collection's own action — open a new comparison, because a roster
cursor is a position in one family revision's walk of two named snapshots and cannot be continued once
either moved.

### Conventions

`__all__` (`:66-79`) publishes the twelve names the composition consumes, in one alphabetical list. The
module imports the shipped read operation and its request/seed/budget/context values, the family and
membership owners, the read-only connection and predecessor-edge query, the store opener, the refusal
type, the review surface's page and refusal values, and the values it states (`:24-64`). It defines no
SQL of its own and opens no store it does not close: `open_family_side` returns the side and the
composition closes both sides in a `finally` block.

### Invariants And Boundaries

- **One implementation of the roster read, called by the composition.** This module decides nothing
  about *which* family revisions a review context is about; it reads the revision it is told to read and
  states what it found.
- **A truncated roster can never be presentable as a whole one.** The page carries the owner's
  `enumeration_complete`, and the member value's own validator refuses content beside
  `content_not_on_page` or the reverse — a member whose revision content fell outside the page is listed
  with that state rather than silently missing.
- **A cursor never crosses a walk or a generation.** A cursor another walk minted is refused and the
  side is re-read from its own first page; a cursor that bound nothing leaves every composed walk's
  first page published beside it.
- **The guarantee is never assembled from members and its seal is verified by its owner on the way out.**
  When the family owner returns no sealed aggregate the side is `unreadable`, not a side with a
  synthesized guarantee.
- **No scope is widened and no selection is invented.** The roster is read with an exact
  `FamilyRevisionSeed`; the module never resolves a family, chooses a head or reads a database the
  resolution did not select.

### Todos

None recorded.

## Docs References

No configured domain documentation could be consulted for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category — its whole body is "No entries
configured yet." — so there is no external or domain source to check and no documentation row is
recorded here.

## Repo-Internal References

Every claim on this card is checkable in the module's own declarations and in the owners it calls. The
three details a reader should carry: **the collection is a set of per-family walks, so naming it without
a cursor earns the collection's own refusal rather than an arbitrary walk's page**; **a cursor another
walk minted is a routing fact, and the side is still read from its own first page**; and **the guarantee
comes from the owner that verifies its seal, so a missing aggregate is an unreadable side and never a
synthesized guarantee**.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The three owners this module calls and the fact that none is duplicated.** | "Three owners are called and none is duplicated" | mcp/src/agents_remember/application/review_family_rosters.py:1-22 |
| The published surface: the twelve names the composition consumes. | `__all__` | mcp/src/agents_remember/application/review_family_rosters.py:66-79 |
| **The review surface's collection name for one family revision's recorded member roster, so a cursor and its walk are never paired by guesswork.** | `FAMILY_MEMBERS_COLLECTION` | mcp/src/agents_remember/application/review_family_rosters.py:81-84 |
| The read owner's own refusal code for a cursor that binds another selection. | `_CURSOR_MISMATCH` | mcp/src/agents_remember/application/review_family_rosters.py:86-88 |
| One roster read's page bound, movement union and cursor, travelling as one request. | `RosterReadRequest` | mcp/src/agents_remember/application/review_family_rosters.py:91-103 |
| **Which revision one roster read is for, the family owner's recorded list, and the axis's own sentence for a one-sided selection.** | `RosterContext` | mcp/src/agents_remember/application/review_family_rosters.py:106-124 |
| One bound snapshot as this composition reads it, with the reason it could not be opened when it could not. | `FamilyRosterSide` | mcp/src/agents_remember/application/review_family_rosters.py:130-148 |
| One side's roster read of one family revision, with what the offered cursor did. | `FamilyRosterRead` | mcp/src/agents_remember/application/review_family_rosters.py:151-164 |
| **The opener that turns a storage, OS or value error into a stated unreadable side rather than an exception.** | `open_family_side` | mcp/src/agents_remember/application/review_family_rosters.py:167-188 |
| The authored predecessor edges, read over a read-only connection so the head rule sees the snapshot's own lineage. | `_authored_edges` | mcp/src/agents_remember/application/review_family_rosters.py:191-203 |
| **The read that states each fact it established: the selected revision, its guarantee, its roster page and its members — or the side's own unreadable reason.** | `read_family_roster` | mcp/src/agents_remember/application/review_family_rosters.py:209-272 |
| **The cursor offer, where a cursor another walk minted leaves the side read from its own first page.** | `_read_roster` | mcp/src/agents_remember/application/review_family_rosters.py:275-305 |
| One read of one family revision's recorded scope at the request's own page bound. | `_roster_read` | mcp/src/agents_remember/application/review_family_rosters.py:308-328 |
| The read owner's own page stated for one family revision's roster, with the scope naming the walk. | `_roster_page` | mcp/src/agents_remember/application/review_family_rosters.py:331-355 |
| The sentence for a read that returned neither a page nor a usable refusal. | `cursor_refusal_detail` | mcp/src/agents_remember/application/review_family_rosters.py:358-363 |
| **The sentence stating how much of the roster the page carried and how the remainder is reached.** | `_roster_detail` | mcp/src/agents_remember/application/review_family_rosters.py:366-381 |
| The one side context that states which fact it is and carries no roster and no count. | `side_statement` | mcp/src/agents_remember/application/review_family_rosters.py:384-394 |
| **The guarantee read from the owner that verifies the revision's seal, or nothing when no sealed aggregate exists.** | `family_guarantee` | mcp/src/agents_remember/application/review_family_rosters.py:400-418 |
| **The membership rows the page carried, each member's content carried only when the same page selected that revision.** | `_members` | mcp/src/agents_remember/application/review_family_rosters.py:421-455 |
| One page's own lookups travelling together, so another page's claims cannot be paired with this roster. | `_RosterLookups` | mcp/src/agents_remember/application/review_family_rosters.py:458-470 |
| One membership row composed as a member context with its exact revision, its sharing fact and its source references. | `_member` | mcp/src/agents_remember/application/review_family_rosters.py:473-499 |
| The member identity taken from the page, or from the store owner when the page did not carry the revision. | `_member_identity` | mcp/src/agents_remember/application/review_family_rosters.py:502-515 |
| **The sharing fact, read from the membership owner and excluding this family revision, so one revision referenced twice is not one fact copied twice.** | `_other_families` | mcp/src/agents_remember/application/review_family_rosters.py:518-534 |
| One recorded realization claim as an inspectable source reference, or the statement that no address was observed. | `_source` | mcp/src/agents_remember/application/review_family_rosters.py:537-557 |
| The sentence stating which facts of one membership row this read established. | `_member_detail` | mcp/src/agents_remember/application/review_family_rosters.py:560-582 |
| The membership identities the relationship union's own movement values display. | `_movement_identities` | mcp/src/agents_remember/application/review_family_rosters.py:585-595 |
| **One continued roster walk stated as the review surface's own page, with the read owner's own counts and cursor.** | `family_member_page` | mcp/src/agents_remember/application/review_family_rosters.py:601-623 |
| **The refusal for naming the collection without a cursor: it is a set of per-family walks, so no single page was addressed.** | `family_collection_refusal` | mcp/src/agents_remember/application/review_family_rosters.py:626-644 |
| **The refusal a cursor that bound no composed walk earns, in `ICR-R10@v1`'s own vocabulary with this collection's own action sentence.** | `family_context_cursor_refusal` | mcp/src/agents_remember/application/review_family_rosters.py:647-685 |
| The composition that decides which families and revisions this read is called for. | `review_family_context` | mcp/src/agents_remember/application/review_family_context.py:254-301 |
| **The values this read states, whose validators refuse a truncated roster presented as a whole one.** | `ReviewFamilyRosterPage` | mcp/src/agents_remember/models/knowledge/review_family_context.py:225-268 |
| The production review read that asks for this roster and publishes its page. | `compose_review` | mcp/src/agents_remember/application/knowledge_review.py:371-611 |
| The cases that drive the roster read through the production review over a real enclosure. | `test_a_successor_family_revision_is_read_from_its_own_rows_not_inherited` | mcp/tests/test_review_family_context.py:342-381 |

## Cross-Repo References

No cross-repository behavior is implemented in this module. The snapshots it opens, the namespace it
binds them to and the code roots it passes to the read context are all values the caller's own resolution
selected for one leaf's enclosure; the predecessor edges come from the same local store, and no remote,
credential, network or external system is involved. No cross-repo reference row is recorded here because
no cited range proves a repository or external-system boundary.

## Update History

- 2026-09-23T22:10:00+02:00 — 260921-ICR-L31 curator (uncommitted change set on `ar/260921-icr-l31`, base `4c000b11c5243e4a8e77c08e87984fff00c1d94b`): created this one-to-one card for the roster read `ICR-R31@v1` introduced as **the recorded roster of one selected family revision**, read and stated for the review context. The stamp basis is honest rather than convenient: the module is untracked at the base commit, so `lastVerifiedCommitHash` names the leaf's base commit, and the verified basis is the working-tree delta on top of it — no commit contains what a stamp would otherwise claim to have verified. The card records what a consumer has to act on: the collection is a **set of per-family walks**, so naming it without a cursor earns the collection's own refusal (`family_collection_refusal`) while every composed walk's first page stays published on the family contexts themselves; a cursor another walk minted is a **routing fact rather than a fact about the side**, so the side is re-read from its own first page and the refusal is carried back once (`_read_roster`); and the guarantee comes from the family owner that verifies its revision seal, so a missing sealed aggregate is an `unreadable` side and never a synthesized guarantee. Fix round 1 changed this module's request shape rather than its read: `RosterContext` now carries the family owner's own recorded revision list and the axis's own one-sided sentence, so a side context publishes the history its selected revision was chosen from — the population fix whose absence made a memberless family revision invisible in the composition next door.
