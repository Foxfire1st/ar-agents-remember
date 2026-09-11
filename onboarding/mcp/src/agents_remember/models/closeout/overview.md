# Closeout Projection Models Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/models/closeout` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Models overview](../overview.md)

## What This Area Is

Strict wire and persistence models for closeout inputs, door sources, disposable queue
projections, and task-publication effects.

## Hot Path Summary

`projection.py` defines the `valid-built` / `invalid-empty` state machine and bounded member,
source-problem, invalidation, rebuild, and task-doc effect payloads.

## Local Invariants And Traps

- A projection is disposable scheduling state, never lifecycle/commit evidence.
- Invalid means empty; stale rows are not transitioned into a second lifecycle database.
- Text and population bounds are enforced at model construction.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `projection.py` | [projection.py.md](projection.py.md) | covered |

## Docs And Boundary References

No configured external source applies. Queue producers and application consumers are documented
through same-repository source references.

## Update History

- 2026-08-25T15:44+02:00 — Created for the disposable projection contract introduced by the
  closeout-lifecycle reform. Verification remains closeout-owned.
