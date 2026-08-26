# mcp/src/agents_remember/models/lifecycles/door_response.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/door_response.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Lifecycle-model overview](overview.md)

## Purpose

Defines the typed public response for closeout-door commands without contaminating the canonical
door source with serving or projection results.

## Code Commentary

The response joins the canonical door generation, per-scope disposable-projection effects, and any
resulting lifecycle operation. Success and refusal shapes are exact and validated: bounded refusal
fields describe why the command did not publish, while a successful response carries the accepted
canonical result and downstream projection effects separately.

## Invariants And Boundaries

- The response is a join/result model; it is not canonical door state.
- Projection failure cannot rewrite or roll back an accepted door publication.
- Refusal fields and success fields may not be mixed into an ambiguous partial result.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The response model separates canonical publication from projection effects. | `CloseoutDoorResponse` | mcp/src/agents_remember/models/lifecycles/door_response.py:18-46 |

## Update History

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-projection model package relocation; finalized door response semantics are unchanged.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final typed response contract. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
