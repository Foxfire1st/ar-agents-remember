# mcp/src/agents_remember/application/review_family_rosters.py

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

## Evidence

### Docs References

No configured domain documentation could be consulted for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category — its whole body is "No entries
configured yet." — so there is no external or domain source to check and no documentation row is
recorded here.

### Repo-Internal References

Every claim on this card is checkable in the module's own declarations and in the owners it calls. The
three details a reader should carry: **the collection is a set of per-family walks, so naming it without
a cursor earns the collection's own refusal rather than an arbitrary walk's page**; **a cursor another
walk minted is a routing fact, and the side is still read from its own first page**; and **the guarantee
comes from the owner that verifies its seal, so a missing aggregate is an unreadable side and never a
synthesized guarantee**.

- **The three owners this module calls and the fact that none is duplicated.** [1]
- The published surface: the twelve names the composition consumes. [2]
- **The review surface's collection name for one family revision's recorded member roster, so a cursor and its walk are never paired by guesswork.** [3]
- The read owner's own refusal code for a cursor that binds another selection. [4]
- One roster read's page bound, movement union and cursor, travelling as one request. [5]
- **Which revision one roster read is for, the family owner's recorded list, and the axis's own sentence for a one-sided selection.** [6]
- One bound snapshot as this composition reads it, with the reason it could not be opened when it could not. [7]
- One side's roster read of one family revision, with what the offered cursor did. [8]
- **The opener that turns a storage, OS or value error into a stated unreadable side rather than an exception.** [9]
- The authored predecessor edges, read over a read-only connection so the head rule sees the snapshot's own lineage. [10]
- **The read that states each fact it established: the selected revision, its guarantee, its roster page and its members — or the side's own unreadable reason.** [11]
- **The cursor offer, where a cursor another walk minted leaves the side read from its own first page.** [12]
- One read of one family revision's recorded scope at the request's own page bound. [13]
- The read owner's own page stated for one family revision's roster, with the scope naming the walk. [14]
- The sentence for a read that returned neither a page nor a usable refusal. [15]
- **The sentence stating how much of the roster the page carried and how the remainder is reached.** [16]
- The one side context that states which fact it is and carries no roster and no count. [17]
- **The guarantee read from the owner that verifies the revision's seal, or nothing when no sealed aggregate exists.** [18]
- **The membership rows the page carried, each member's content carried only when the same page selected that revision.** [19]
- One page's own lookups travelling together, so another page's claims cannot be paired with this roster. [20]
- One membership row composed as a member context with its exact revision, its sharing fact and its source references. [21]
- The member identity taken from the page, or from the store owner when the page did not carry the revision. [22]
- **The sharing fact, read from the membership owner and excluding this family revision, so one revision referenced twice is not one fact copied twice.** [23]
- **Each recorded realization claim projected by the dedicated source module — with its per-side locator, resolved ranges and locator state — rather than by a private projection here.** [24]
- The sentence stating which facts of one membership row this read established. [25]
- The membership identities the relationship union's own movement values display. [26]
- **One continued roster walk stated as the review surface's own page, with the read owner's own counts and cursor.** [27]
- **The refusal for naming the collection without a cursor: it is a set of per-family walks, so no single page was addressed.** [28]
- **The refusal a cursor that bound no composed walk earns, in `ICR-R10@v1`'s own vocabulary with this collection's own action sentence.** [29]
- The composition that decides which families and revisions this read is called for. [30]
- **The values this read states, whose validators refuse a truncated roster presented as a whole one.** [31]
- The production review read that asks for this roster and publishes its page. [32]
- The cases that drive the roster read through the production review over a real enclosure. [33]

| The page-local join emits members only for carried membership items. | `_members` | mcp/src/agents_remember/application/review_family_rosters.py:433-467 |

### Cross-Repo References

No cross-repository behavior is implemented in this module. The snapshots it opens, the namespace it
binds them to and the code roots it passes to the read context are all values the caller's own resolution
selected for one leaf's enclosure; the predecessor edges come from the same local store, and no remote,
credential, network or external system is involved. No cross-repo reference row is recorded here because
no cited range proves a repository or external-system boundary.
