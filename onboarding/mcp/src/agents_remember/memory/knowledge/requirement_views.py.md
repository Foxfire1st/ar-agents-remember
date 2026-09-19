# mcp/src/agents_remember/memory/knowledge/requirement_views.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/requirement_views.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T17:15+02:00 |
| lastVerifiedCommitHash | `562cef4ca64de5b11712d5165d24e78c9a035312` |
| lastVerifiedCommitDate | 2026-09-19T17:51:43+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l19` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The one projection entry: every derived view for one record, from the rows and nothing else.** | `revision_scope` | mcp/src/agents_remember/memory/knowledge/requirement_views.py:248-272 |
|The fork rule — more than one head is reported as more than one head, and no successor is designated.|`head_revision_ids`| mcp/src/agents_remember/memory/knowledge/requirement_views.py:93-110 |
|The bounded predecessor walk, and the constant that makes a damaged store a report rather than a hang.|`predecessor_chain_view`; `CHAIN_BOUND`| mcp/src/agents_remember/memory/knowledge/requirement_views.py:111-142; mcp/src/agents_remember/memory/knowledge/requirement_views.py:58-62 |
|**Currentness by value: both recorded states travel with their provenance, and no winner is chosen.**|`currentness_fact`; `current_state_view`| mcp/src/agents_remember/memory/knowledge/requirement_views.py:167-247 |
|The ungoverned route as an explicit state rather than a default, with the packet's directory deliberately not an input.|`governing_route_view`| mcp/src/agents_remember/memory/knowledge/requirement_views.py:145-155 |
| The three documented absences, each saying which absence it is. | `UNRESOLVED_OWNER_DETAIL`; `NOT_COMPARED_DETAIL`; `NO_REVISION_DETAIL` | mcp/src/agents_remember/memory/knowledge/requirement_views.py:63-73 |
|The currentness value whose `state` must equal the value derived from the two recorded pairs.|`RequirementCurrentness`| mcp/src/agents_remember/models/knowledge/requirement.py:232-270 |
|The acyclicity rule the write transaction applies, which is why the walk here is bounded rather than guarded.|`require_acyclic_lineage`| mcp/src/agents_remember/memory/knowledge/requirements.py:324-364 |
|**The two cases that keep a view an answer rather than an authority: byte-identical rebuilds, and totality over a row set holding no revision.**|"test_every_derived_view_rebuilds_byte_identically_from_the_stored_rows"; "test_the_derived_views_are_total_over_a_row_set_holding_no_revision"| mcp/tests/test_knowledge_requirement_reference_contract.py:569-616; mcp/tests/test_knowledge_requirement_reference_contract.py:730-755 |
| The no-winner cases: a fork, a disagreement, and an unresolved owner that has nothing to compare. | "test_a_fork_is_reported_as_more_than_one_head_and_no_winner_is_chosen"; "test_a_stored_state_that_disagrees_with_the_owners_state_reports_both_and_chooses_none"; "test_an_unresolved_owner_has_nothing_to_compare_even_when_a_state_is_supplied" | mcp/tests/test_knowledge_requirement_reference_contract.py:617-646; mcp/tests/test_knowledge_requirement_reference_contract.py:647-700; mcp/tests/test_knowledge_requirement_reference_contract.py:701-729 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-19T17:15+02:00 — 260915-KS-L28 curator (uncommitted change set on `ar/260915-ks-l28`, base `497d9e9f`): M1-4 anchor repair, re-read against the code worktree at `e7998504`. The bounded-walk row had `predecessor_chain_view` and `CHAIN_BOUND` crossed: the constant is `:58-62` and the walk is `:111-142`, and the citations now pair them that way. Every other row was re-checked and stands (the literal-anchored node rows each name their own node inside their own range). No claim was deleted or softened. The stamp is unchanged because `a0665505`'s content for this file is byte-identical to `e7998504` (`git diff a0665505 HEAD` is empty).- 2026-09-18T06:05+02:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): created this one-to-one card for the requirement record group's derived views. It records the mechanism rather than the requirement: disposability is met **structurally**, because this module holds no connection and takes no store, so no view can write even if a later caller wanted it to. It states the three no-winner rules a reader would otherwise have to re-derive — a fork is reported as more than one head because designating a successor is an authority the substrate does not hold; currentness reports both recorded states with their provenance and never claims an agreement it cannot show; and an absent route is the explicit `ungoverned` state rather than an inference from the packet's directory. It also records that the predecessor walk is **bounded rather than cycle-guarded** (`CHAIN_BOUND = 512`, `truncated=True`), because acyclicity is enforced by the writing transaction and a damaged store should be described rather than hung on. Verification metadata advances to the leaf's base commit `e963a01c` because the body was read against the current source; the code commit does not exist yet and closeout owns that stamp.
