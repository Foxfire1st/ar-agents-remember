# mcp/src/agents_remember/application/review_family_rosters.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_family_rosters.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T16:55:00+02:00 |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28` |
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview | `overview.md` |

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

**Three owners are called and none is duplicated**: the **selection policy** runs through the
shipped read operation `read_knowledge_scope` with an exact `FamilyRevisionSeed`, so the roster, its
counts and its snapshot-bound continuation are the read owner's own; the **authored guarantee** comes
from the family owner, which verifies the revision's payload seal on the way out; and the **sharing
fact** — the other family revisions one member revision is recorded in — comes from the membership
owner.

**What it refuses is the shape of every value below**: a side that was not read states which
fact it is instead of an empty roster, a membership row whose revision content fell outside the page is
stated as `content_not_on_page` rather than filled in from a second selection, and the guarantee is
never assembled from the members it is stored beside.

## Code Commentary

### Logic

**The collection name is a constant because a cursor and the walk it belongs to must not be paired by
guesswork.** `FAMILY_MEMBERS_COLLECTION` is `family_members`: the name a request presents its
cursor under and the name the payload's page states. `_CURSOR_MISMATCH` is the read owner's
own refusal code for "this cursor binds another selection" — the one answer that means the cursor belongs
to a walk this read is not positioned in.

**Two small request values, each keeping one request's parts together.** `RosterReadRequest` carries the page bound, the relationship union's movements and the cursor, because a caller
able to pass two of them could state a page whose bound and position disagree. `RosterContext` carries which revision the read is for and the two facts that qualify it: the family
owner's own `recorded_revision_ids` for the side, and `not_recorded_detail` — the sentence stating which
fact a one-sided selection is, which **differs by the axis the selection was made on** (an invariant
records no membership here; a family records no such revision), so the composition that knows the axis
supplies the sentence rather than this module guessing it.

**One snapshot, opened once, and its failure kept as a state.** `FamilyRosterSide` is one
bound snapshot: its store, its read context, every authored `(successor, predecessor)` edge, and
`unreadable` — the reason the side could not be opened at all, in which case every family context on
that side states that reason rather than an absence. `open_family_side` opens all three and
turns a storage error, an OS error or a value error into `unreadable` with the error's own type and
message rather than raising. `_authored_edges` reads the predecessor edges over a read-only
connection — the same values `ICR-R07@v1`'s selection reads — so a head rule applied to them is applied
to the snapshot's own authored lineage and to nothing a caller derived.

**The read states each fact it established and nothing it did not.** `read_family_roster`
answers one snapshot's context for one family: a selection that established no revision on this side
returns the `not_recorded` sentence the composition supplied; a side that could not be
opened or read returns `unreadable` with the owner's or the opener's own words, including
the case where the family revision is in the selected set but the family owner returned no sealed
aggregate for it — no guarantee is then presented for it; and the recorded path composes the side from
the guarantee, the page, the members and the exact revision. `FamilyRosterRead`
carries what the offered cursor did: `bound` is true when *this* read served the presented cursor, which
is how the response knows which of its family contexts the published page belongs to, and
`cursor_refusal` is the owner's own refusal when the cursor was offered here and this walk did not mint
it.

**A cursor another walk minted is a routing fact, not a fact about the side.** `_read_roster` offers the request's cursor to this walk; when the owner refuses it with
`continuation_binding_mismatch` the side is read **again from its own first page** and the refusal is
carried back so the response can state once that no walk it composed bound the cursor. `_roster_read` is one read at the request's own page bound. `_roster_page` states the read
owner's own page — its counts, its `enumeration_complete` and its continuation — with a scope naming the
exact side, family revision, policy version and page size, so a reader never has to guess which of the
response's family contexts the published page is about.

**Every sentence is built from the values the read returned.** `cursor_refusal_detail`
names the case where the read returned neither a page nor a usable refusal. `_roster_detail` states how many member-context updates *this page* supplies, and its completed case splits in two
because `complete` describes the **walk** rather than the page: a walk the read took in one page carried every recorded membership, so the
sentence says the roster was read whole with its count; a walk whose final page is a continuation enumerated the whole selection but carried only that page's own share, so the sentence
names the owner's total, how many this page carried, and that it completes the read walk while the
pages before it carried the rest; and an incomplete page names the remainder and the
continuation that reaches it. `side_statement` is the one side context that carries no
roster and no count at all.

**The guarantee comes from the owner that verifies its seal.** `family_guarantee` reads one
family revision through the family owner and returns its stored `joint_guarantee` with the display
version, origin state, acceptance reference, provenance and payload digest — or `None`, in which case the
caller states an unreadable side rather than presenting a guarantee it did not get.

**Each page identifies the exact revisions it represents, even when their record kinds are split across pages.** `_members` unions the revision IDs from this page's content, claims and membership items, then resolves each pair through `memberships.find_membership_by_pair` for the selected family revision. It projects only recorded associations in that bounded set. `_RosterLookups` still contains only this page's selected content and source claims, so a later claim can carry `content_not_on_page` without losing its exact membership or fabricating a statement. The client can enrich an earlier member context with that sparse update.

`_member` carries the stored membership identity, exact invariant revision, known identity/label, page-selected content, recorded sharing and this page's claims. `_other_families` still obtains sharing from the membership owner. **Each claim's source reference is projected by `member_source` in `application/review_family_sources.py`**, which this module imports and calls once per claim; the private `_source` projection that used to live here is gone. That projection preserves each claim's recorded and observed source identity, resolution and `detail`, and adds the side's structured recorded locator, resolved line ranges and locator state, so two members realized in one file keep two regions (see that module's card). Movement references remain the comparison union's facts. This is a projection correction, not a whole-roster fetch or another read policy.

**The page and the refusals are the surface's own vocabulary.** `family_member_page` states
one continued roster walk as `ICR-R10@v1`'s `ReviewCollectionPage`, carrying the read owner's own
`primary_items_total`, `primary_items_returned` and `primary_items_remaining` and its opaque
snapshot-bound continuation, with a scope naming the exact side and family revision.
`family_collection_refusal` answers a request that named the collection **without** a
cursor: this collection is a *set* of per-family walks rather than one walk, so naming it addresses no
single page, and the response still carries every walk's first page on the family contexts themselves.
`family_context_cursor_refusal` answers a cursor that bound no composed walk in the
surface's own vocabulary: a malformed token earns `comparison_page_unreadable` with the action sentence
naming what a real cursor looks like, while a well-formed cursor that bound nothing earns
`comparison_page_reset` with this collection's own action — open a new comparison, because a roster
cursor is a position in one family revision's walk of two named snapshots and cannot be continued once
either moved.

### Conventions

`__all__` publishes the twelve names the composition consumes, in one alphabetical list. The
module imports the shipped read operation and its request/seed/budget/context values, the family and
membership owners, the read-only connection and predecessor-edge query, the store opener, the refusal
type, the review surface's page and refusal values, the member-source projection, and the values it states. It defines no
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
- **`complete` is the walk's flag and not the page's, so no sentence claims more than the page
  carried.** A completed page may be read as *the roster, whole* only when it is also the walk's first
  page; a completed **continued** page says instead that it completes the read walk, because "all
  carried here" would be false about the store while the pages before it are what carried the rest.
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

No current projection gap is recorded here. Sparse pages still expose only their selected content and claims; a completed final page completes the walk and does not replace the accumulated roster by itself.

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
| The published surface: the twelve names the composition consumes. | `__all__` | mcp/src/agents_remember/application/review_family_rosters.py:67-80 |
| **The review surface's collection name for one family revision's recorded member roster, so a cursor and its walk are never paired by guesswork.** | `FAMILY_MEMBERS_COLLECTION` | mcp/src/agents_remember/application/review_family_rosters.py:85-85 |
| The read owner's own refusal code for a cursor that binds another selection. | `_CURSOR_MISMATCH` | mcp/src/agents_remember/application/review_family_rosters.py:89-89 |
| One roster read's page bound, movement union and cursor, travelling as one request. | `RosterReadRequest` | mcp/src/agents_remember/application/review_family_rosters.py:92-104 |
| **Which revision one roster read is for, the family owner's recorded list, and the axis's own sentence for a one-sided selection.** | `RosterContext` | mcp/src/agents_remember/application/review_family_rosters.py:107-125 |
| One bound snapshot as this composition reads it, with the reason it could not be opened when it could not. | `FamilyRosterSide` | mcp/src/agents_remember/application/review_family_rosters.py:131-149 |
| One side's roster read of one family revision, with what the offered cursor did. | `FamilyRosterRead` | mcp/src/agents_remember/application/review_family_rosters.py:152-165 |
| **The opener that turns a storage, OS or value error into a stated unreadable side rather than an exception.** | `open_family_side` | mcp/src/agents_remember/application/review_family_rosters.py:168-189 |
| The authored predecessor edges, read over a read-only connection so the head rule sees the snapshot's own lineage. | `_authored_edges` | mcp/src/agents_remember/application/review_family_rosters.py:192-204 |
| **The read that states each fact it established: the selected revision, its guarantee, its roster page and its members — or the side's own unreadable reason.** | `read_family_roster` | mcp/src/agents_remember/application/review_family_rosters.py:210-273 |
| **The cursor offer, where a cursor another walk minted leaves the side read from its own first page.** | `_read_roster` | mcp/src/agents_remember/application/review_family_rosters.py:276-306 |
| One read of one family revision's recorded scope at the request's own page bound. | `_roster_read` | mcp/src/agents_remember/application/review_family_rosters.py:309-329 |
| The read owner's own page stated for one family revision's roster, with the scope naming the walk. | `_roster_page` | mcp/src/agents_remember/application/review_family_rosters.py:332-356 |
| The sentence for a read that returned neither a page nor a usable refusal. | `cursor_refusal_detail` | mcp/src/agents_remember/application/review_family_rosters.py:359-364 |
| **The sentence stating how much of the roster the page carried and how the remainder is reached.** | `_roster_detail` | mcp/src/agents_remember/application/review_family_rosters.py:367-396 |
| The one side context that states which fact it is and carries no roster and no count. | `side_statement` | mcp/src/agents_remember/application/review_family_rosters.py:399-409 |
| **The guarantee read from the owner that verifies the revision's seal, or nothing when no sealed aggregate exists.** | `family_guarantee` | mcp/src/agents_remember/application/review_family_rosters.py:415-433 |
| **The membership rows the page carried, each member's content carried only when the same page selected that revision.** | `_members` | mcp/src/agents_remember/application/review_family_rosters.py:436-480 |
| One page's own lookups travelling together, so another page's claims cannot be paired with this roster. | `_RosterLookups` | mcp/src/agents_remember/application/review_family_rosters.py:483-495 |
| One membership row composed as a member context with its exact revision, its sharing fact and its source references. | `_member` | mcp/src/agents_remember/application/review_family_rosters.py:498-526 |
| The member identity taken from the page, or from the store owner when the page did not carry the revision. | `_member_identity` | mcp/src/agents_remember/application/review_family_rosters.py:529-542 |
| **The sharing fact, read from the membership owner and excluding this family revision, so one revision referenced twice is not one fact copied twice.** | `_other_families` | mcp/src/agents_remember/application/review_family_rosters.py:545-561 |
| **Each recorded realization claim projected by the dedicated source module — with its per-side locator, resolved ranges and locator state — rather than by a private projection here.** | `member_source` | mcp/src/agents_remember/application/review_family_rosters.py:32-32; mcp/src/agents_remember/application/review_family_rosters.py:523-523; mcp/src/agents_remember/application/review_family_sources.py:27-51 |
| The sentence stating which facts of one membership row this read established. | `_member_detail` | mcp/src/agents_remember/application/review_family_rosters.py:564-586 |
| The membership identities the relationship union's own movement values display. | `_movement_identities` | mcp/src/agents_remember/application/review_family_rosters.py:589-599 |
| **One continued roster walk stated as the review surface's own page, with the read owner's own counts and cursor.** | `family_member_page` | mcp/src/agents_remember/application/review_family_rosters.py:605-627 |
| **The refusal for naming the collection without a cursor: it is a set of per-family walks, so no single page was addressed.** | `family_collection_refusal` | mcp/src/agents_remember/application/review_family_rosters.py:630-648 |
| **The refusal a cursor that bound no composed walk earns, in `ICR-R10@v1`'s own vocabulary with this collection's own action sentence.** | `family_context_cursor_refusal` | mcp/src/agents_remember/application/review_family_rosters.py:651-689 |
| The composition that decides which families and revisions this read is called for. | `review_family_context` | mcp/src/agents_remember/application/review_family_context.py:245-292 |
| **The values this read states, whose validators refuse a truncated roster presented as a whole one.** | `ReviewFamilyRosterPage` | mcp/src/agents_remember/models/knowledge/review_family_context.py:199-251 |
| The production review read that asks for this roster and publishes its page. | `compose_review` | mcp/src/agents_remember/application/knowledge_review.py:334-574 |
| The cases that drive the roster read through the production review over a real enclosure. | `test_a_successor_family_revision_is_read_from_its_own_rows_not_inherited` | mcp/tests/test_review_family_context.py:342-381 |

| The page-local join emits members only for carried membership items. | `_members` | mcp/src/agents_remember/application/review_family_rosters.py:433-467 |

## Cross-Repo References

No cross-repository behavior is implemented in this module. The snapshots it opens, the namespace it
binds them to and the code roots it passes to the read context are all values the caller's own resolution
selected for one leaf's enclosure; the predecessor edges come from the same local store, and no remote,
credential, network or external system is involved. No cross-repo reference row is recorded here because
no cited range proves a repository or external-system boundary.

## Update History
- 2026-09-28T17:15:39+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/src/agents_remember/application/knowledge_review.py`) were re-pointed to where the same anchors now sit; each re-pointed row held its anchors at the base and holds them after the base-to-candidate line mapping. Claim wording unchanged. No stamp advanced.

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): the private `_source` projection was removed; each claim is now projected by `application/review_family_sources.member_source`, which adds the per-side structured locator, resolved ranges and locator state. Updated the member paragraph, conventions and the source row, and re-measured every range the removal shifted (the refusal row that ran past the file's end now reads its real extent). No read, cursor, refusal or guarantee behaviour changed. No verification stamp was advanced.

- 2026-09-27T02:44:54Z — L40: No content impact: reviewed the existing claim against the same named moved source owner and retained its meaning while rebinding the reference. This source artifact is unchanged; prior history and verification metadata remain intact.

- 2026-09-27T02:33:44+00:00: Generated citation repair: `review_family_context` repointed to mcp/src/agents_remember/application/review_family_context.py:245-292. No content impact: mechanical anchor-range projection bound to citation source snapshot 8d622ab90c9b13974d7092fdff43b4fba5681d634b1dc5af7229f82cc78dbdaa; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:17:12+00:00: Generated citation repair: `FAMILY_MEMBERS_COLLECTION` repointed to mcp/src/agents_remember/application/review_family_rosters.py:85-85. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:17:12+00:00: Generated citation repair: `_CURSOR_MISMATCH` repointed to mcp/src/agents_remember/application/review_family_rosters.py:89-89. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:17:12+00:00: Generated citation repair: `_RosterLookups` repointed to mcp/src/agents_remember/application/review_family_rosters.py:483-495. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:17:12+00:00: Generated citation repair: `_member_identity` repointed to mcp/src/agents_remember/application/review_family_rosters.py:529-542. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-27T01:17:12+00:00: Generated citation repair: `_movement_identities` repointed to mcp/src/agents_remember/application/review_family_rosters.py:612-622. No content impact: mechanical anchor-range projection bound to citation source snapshot 771605ffc6f78b7deb726bb881dc964bb91fad696d0375cef1a8d8e9ffd8ba84; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-27T00:59:43+00:00 — Curated exact sparse member updates for content, membership and claim pages. Recorded membership lookup stays bounded to represented revisions; selected-content, guarantee, paging and movement owners remain unchanged. The earlier page-local projection limitation is resolved; final commit stamps remain closeout-owned.
- 2026-09-26T21:21:39Z — Recorded the realization-only continuation projection limit and its reconsideration condition; storage absence is not inferred.

- 2026-09-24T02:20:00+02:00 — 260921-ICR-L31 curator, **reopened enclosure** (`260921-icr-l31b`, same base `fdf3e4b6cfe73040d35cbfd4d8b93fd55369e499`, code worktree `ar/260921-icr-l31b`): **the completed sentence on this card was re-described for the corrected completion semantics, and every range was re-anchored past this delta's +12-line insertion.** The correction is the reopen's whole subject: `complete` is the **walk's** flag rather than the page's, so `_roster_detail` (`:366-393`) no longer states two cases — a walk the read took in one **page** (`:377-381`) carried every recorded membership and is the roster whole, a walk whose **final** page is a continuation (`:382-387`) completed the enumeration having carried only that page's own share and now says so instead of "all carried here", and the incomplete branch (`:388-393`) keeps the remainder sentence. What did **not** change, and is recorded so a reader does not infer a wider fix: the module's read, its cursor handling, its refusals, its guarantee path and `complete`'s own meaning (`enumeration_complete`, read from the owner, never written here) are all untouched; this delta is 2 hunks in this module and adds no field, state, capability or policy. Every citation range was re-measured on the candidate bytes — rows at and after the insertion's first line carried +12, `_roster_detail`'s own range grew with its docstring, and the cross-file `ReviewFamilyRosterPage` row now reads `:225-277`. **Stamp accounting: no verification stamp was advanced.** The header's pair still names this leaf's base `fdf3e4b6`, because the candidate is uncommitted and the governed closeout owns the real code and memory commits; the verified basis is that base plus the working-tree delta, exactly as the first curation recorded it.

- 2026-09-23T22:10:00+02:00 — 260921-ICR-L31 curator (uncommitted change set on `ar/260921-icr-l31`, base `4c000b11c5243e4a8e77c08e87984fff00c1d94b`): created this one-to-one card for the roster read `ICR-R31@v1` introduced as **the recorded roster of one selected family revision**, read and stated for the review context. The stamp basis is honest rather than convenient: the module is untracked at the base commit, so `lastVerifiedCommitHash` names the leaf's base commit, and the verified basis is the working-tree delta on top of it — no commit contains what a stamp would otherwise claim to have verified. The card records what a consumer has to act on: the collection is a **set of per-family walks**, so naming it without a cursor earns the collection's own refusal (`family_collection_refusal`) while every composed walk's first page stays published on the family contexts themselves; a cursor another walk minted is a **routing fact rather than a fact about the side**, so the side is re-read from its own first page and the refusal is carried back once (`_read_roster`); and the guarantee comes from the family owner that verifies its revision seal, so a missing sealed aggregate is an `unreadable` side and never a synthesized guarantee. Fix round 1 changed this module's request shape rather than its read: `RosterContext` now carries the family owner's own recorded revision list and the axis's own one-sided sentence, so a side context publishes the history its selected revision was chosen from — the population fix whose absence made a memberless family revision invisible in the composition next door.
