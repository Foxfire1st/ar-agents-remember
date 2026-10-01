# mcp/src/agents_remember/memory/knowledge/requirement_views.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The requirement record group's derived views: pure functions of the stored rows and nothing else.**
`KS-R19@v1` requirement 7 makes every view this record group serves derived and regenerable from the
owner's packet plus the stored revisions, disposable, and forbidden from becoming an authority. This
module is how that requirement is met **structurally rather than procedurally**: it holds no
connection, takes no store, and writes nothing, so "disposable" is a property of the code's shape
instead of a discipline a later caller has to keep.

**Why nothing is stored.** A stored derived value would need invalidation, and invalidation is exactly
the authority requirement 7 withholds. These functions therefore answer from the rows on every call,
and the record group declares no mutable "current revision", "current state" or "current route"
column anywhere.

## Code Commentary

### Logic

- `revision_scope` (248-272) is the **one projection entry**: given a decoded record and its decoded
  revisions it returns the whole `RequirementRevisionScope` — the revision views, the head set, the
  predecessor chain, the current-state view, the currentness facts and the governing-route view.
- **A fork is reported, not resolved.** `head_revision_ids` (93-108) returns every revision that
  nothing names as its predecessor. A record with two heads reports two, because picking one is the
  substrate designating a successor — an authority it does not hold and for which there is no column
  to hold it.
- **Currentness carries both values and no winner.** `currentness_fact` (167-220) derives
  `aligned` / `disagreement` from the two recorded state pairs and reports either
  `unresolved-owner` (the owner's resolution is unresolved, or nothing was consumed to compare
  against) rather than claiming an agreement it cannot show. A disagreement detail names both states
  with their provenance and states that the record chooses no winner.
- **Ungoverned is a state, never a default.** `governing_route_view` (145-153) maps an absent route to
  the explicit `ungoverned` state; the packet's own directory is deliberately not an input, because
  inferring a route from where the packet turned out to live would derive the substrate's answer from
  the operand requirement 2.3 forbids it to treat as one.
- **The chain walk is bounded, not cycle-guarded.** `predecessor_chain_view` (111-142) walks at most
  `CHAIN_BOUND = 512` edges (58) and reports `truncated=True` past that point: a damaged store is
  described, not hung on. Acyclicity itself is enforced in the transaction that writes the edge
  (`requirements.py:require_acyclic_lineage`), not here.

### Conventions

- Every function is total over its input. `head_revision_ids(())` is `()`, and a record holding no
  revision answers with every documented absence — `revisions == ()`, `predecessor_chain is None`,
  `current_state.owner is None`, `currentness == ()`, `governing_route.state == "ungoverned"` — rather
  than raising. The three detail constants (`UNRESOLVED_OWNER_DETAIL` 63-66, `NOT_COMPARED_DETAIL`
  67-70, `NO_REVISION_DETAIL` 73) exist so each absence says which absence it is.
- The currentness `state` is **derived from the two recorded pairs**, never asserted against them: a
  caller-supplied state that disagrees raises at construction in
  `models/knowledge/requirement.py:RequirementCurrentness` rather than being stored.

### Invariants And Boundaries

- **This module cannot write, and cannot become an authority, because it holds no store.** Its inputs
  are already-decoded `StoredRequirementRecord` / `StoredRequirementRevision` values from
  `requirement_records.py`; a caller that wanted a view to persist something would have to change
  this module's signature first.
- **No view is a task state.** Nothing here reads or returns a task status, a seat owner or a lifecycle
  gate; the record's own currentness is a fact about the stored revision and the owner's consumed
  resolution, and it is reported with its basis (`CurrentnessBasis`) so a reader can tell a
  not-declared basis from a measured one.
- **Boundary.** This module does not own the payload vocabulary
  (`models/knowledge/requirement.py`), the row codecs (`requirement_records.py`), the operation
  surface or its guards (`requirements.py`), or the envelope seam (`record_envelope.py`).

### Todos

None recorded. As with the rest of the record group there is no production caller yet: `revision_scope`
is reached from `requirements.py:read_requirement_revisions` and, today, only from the record group's
own tests.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The one projection entry: every derived view for one record, from the rows and nothing else.** [1]
- The fork rule — more than one head is reported as more than one head, and no successor is designated. [2]
- The bounded predecessor walk, and the constant that makes a damaged store a report rather than a hang. [3]
- **Currentness by value: both recorded states travel with their provenance, and no winner is chosen.** [4]
- The ungoverned route as an explicit state rather than a default, with the packet's directory deliberately not an input. [5]
- The three documented absences, each saying which absence it is. [6]
- The currentness value whose `state` must equal the value derived from the two recorded pairs. [7]
- The acyclicity rule the write transaction applies, which is why the walk here is bounded rather than guarded. [8]
- **The two cases that keep a view an answer rather than an authority: byte-identical rebuilds, and totality over a row set holding no revision.** [9]
- The no-winner cases: a fork, a disagreement, and an unresolved owner that has nothing to compare. [10]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
