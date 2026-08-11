# mcp/tests/test_facade_surface.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_facade_surface.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                                        |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Static facade-exhaustiveness suite for public module names and deliberate removals.

## Code Commentary

### Logic

The suite compares top-level definitions and consumer imports with each declared facade. Its removal inventory explicitly rejects the retired leaf-attachment request and helpers from `serving.app`, preventing compatibility aliases from silently reviving them.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the public or owning internal seam directly.

### Invariants And Boundaries

Every exposed name is intentional; retired exact-id or leaf-address surfaces remain absent rather than aliased.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `FacadeSurfaceTests` | mcp/tests/test_facade_surface.py:185-185 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

- 2026-08-11T19:58+02:00 — Reconciled `test_facade_surface.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the surface pin. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
