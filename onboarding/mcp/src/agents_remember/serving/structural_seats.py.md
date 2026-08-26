# mcp/src/agents_remember/serving/structural_seats.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/structural_seats.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T23:19+02:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
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

### Todos

None.

## Docs References

No Domain Documentation source is configured.


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolver and error family centralize structural qualification. | `StructuralSeatResolver` | mcp/src/agents_remember/serving/structural_seats.py:24-157 |
| Parent/child canonical addresses are derivable through vacancy. | `parent_address`; `child_address` | mcp/src/agents_remember/serving/structural_seats.py:48-65; mcp/src/agents_remember/serving/structural_seats.py:67-77 |
| Task containment resolves real sprint/master/leaf documents. | `TaskDocumentTopology` | mcp/src/agents_remember/tasks/document_refs.py:35-252 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.


## Update History

- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — No content impact: final ARSPAWN-L2 review confirmed vacancy-safe
  address derivation and current-generation resolution remain separated exactly as documented.
  Verification remains closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: separated canonical address derivation from current
  occupant resolution and consumed the shared incumbent/heir selector. Verification remains
  closeout-owned.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created; absorbs qualified binding behavior formerly split across leaf validation and sprint-role binding helpers.
