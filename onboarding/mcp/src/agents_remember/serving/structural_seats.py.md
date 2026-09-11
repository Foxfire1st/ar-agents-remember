# mcp/src/agents_remember/serving/structural_seats.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/structural_seats.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T12:00+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Serving overview](overview.md)

## Purpose

Qualifies current structural seats from canonical task-document containment and role. It is the one
resolver used by structural operations and replacement-aware routing.

## Code Commentary

### Logic

`StructuralSeatResolver` reads task topology and catalog bindings, enforces the role's natural
altitude, derives authorized parents/children, and selects exactly one live occupant. Missing,
ambiguous, wrong-level, and out-of-scope cases become typed `StructuralSeatError`s.
`parent_address` and `child_address` derive and authorize the canonical document-and-role pair
without requiring a live occupant; `parent` and `child` layer current-generation resolution on top.
Current selection is delegated to `controlplane.seats.current_seat_occupant`.

`authorize_child` exposes the four reviewer contexts without creating four roles: managers own leaf
and master reviewers, the architect owns the sprint plan reviewer, and the orchestrator owns the
sprint super-exit reviewer. `_reviewer_parent_address` validates the parent stamp against the target
altitude before routing. Only a pre-polymorphic unstamped leaf reviewer retains its one
deterministic manager owner. Unstamped master and sprint reviewers fail closed rather than inventing
an owner for a review manifestation that did not exist in the legacy leaf-only model.
Manager child authorization distinguishes an invalid same-master role from a leaf owned by a
different master. The latter returns the specific outside-manager-scope refusal instead of being
collapsed into the generic child-vocabulary error.

### Conventions

The resolver uses structural task references for identity and runtime ids only as internal catalog
occupant/provenance evidence.

### Invariants And Boundaries

- Exactly one live occupant may satisfy a singular document+role seat.
- Parent and child lookup never escapes the containing sprint/master.
- Spawn ancestry is neither public identity nor a fallback resolver here; topology plus role
  establishes the authorized relation.
- No first-running-role or workspace-global fallback exists.
- An address remains valid while its seat is vacant; occupancy is required only for operations that
  act on a current generation.
- Reviewer is polymorphic by task altitude and generation-bound parent; sprint ownership is never
  guessed from the shared reviewer address.

### Todos

None.

## Docs References

No Domain Documentation source is configured.


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolver and error family centralize structural qualification. | `StructuralSeatResolver` | mcp/src/agents_remember/serving/structural_seats.py:24-157 |
| Parent/child canonical addresses are derivable through vacancy. | `parent_address`; `child_address` | mcp/src/agents_remember/serving/structural_seats.py:48-65; mcp/src/agents_remember/serving/structural_seats.py:67-77 |
| Reviewer parent resolution validates the plane stamp and permits unstamped migration only for historical leaf rows. | `_reviewer_parent_address` | mcp/src/agents_remember/serving/structural_seats.py:160-197 |
| Task containment resolves real sprint/master/leaf documents. | `TaskDocumentTopology` | mcp/src/agents_remember/tasks/document_refs.py:35-252 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.


## Update History

- 2026-08-31T12:00+02:00 — ARSPAWN-L5 A005 review repair restored the specific
  outside-manager-master refusal and extracted manager authorization to keep the resolver below its
  complexity bound. Verification remains closeout-owned.

- 2026-08-31T04:59+02:00 — Tightened the ARSPAWN-L5 migration boundary to the actual
  pre-polymorphic population: only unstamped leaf reviewers have a deterministic historical owner;
  master and sprint rows require plane-stamped parent provenance. Verification remains closeout-owned.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: documented the four
  reviewer contexts, their plane-specific child authorization, and the bounded legacy versus
  fail-closed sprint-parent rule. Verification remains closeout-owned.

- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — No content impact: final ARSPAWN-L2 review confirmed vacancy-safe
  address derivation and current-generation resolution remain separated exactly as documented.
  Verification remains closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: separated canonical address derivation from current
  occupant resolution and consumed the shared incumbent/heir selector. Verification remains
  closeout-owned.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created; absorbs qualified binding behavior formerly split across leaf validation and sprint-role binding helpers.
