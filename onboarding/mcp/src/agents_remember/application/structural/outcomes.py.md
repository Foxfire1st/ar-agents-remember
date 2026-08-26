# mcp/src/agents_remember/application/structural/outcomes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/structural/outcomes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T23:19+02:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structural application services](overview.md)

## Purpose

Defines the stable caller-facing structural outcome and its runtime-id-free payload projection.

## Code Commentary

### Logic

`StructuralOutcome` carries operation status, canonical task document, role, optional detail, and
delivery state. `structural_payload` serializes only populated public fields and deliberately has
no occupant/session coordinate.

### Conventions

Structural application modules construct this typed value instead of independently rebuilding
response dictionaries.

### Invariants And Boundaries

- Public work identity is task document plus role.
- Runtime session, lifecycle, inbox-owner, and lock identities have no field in this type.
- Optional fields are omitted rather than emitted as invented evidence.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| The outcome vocabulary contains no runtime occupant identifier. | `StructuralOutcome` | mcp/src/agents_remember/application/structural/outcomes.py:11-20 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The single structural payload projector emits stable work identity and delivery state. | `structural_payload` | mcp/src/agents_remember/application/structural/outcomes.py:23-40 |

## Cross-Repo References

No cross-repository dependency governs this unit.

## Update History

- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — No content impact: final ARSPAWN-L2 review confirmed the shared
  runtime-id-free structural payload contract remains exactly as documented. Verification remains
  closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: extracted the shared structural response boundary
  so dispatch reconciliation and existing structural tools cannot drift. Verification remains
  closeout-owned.
