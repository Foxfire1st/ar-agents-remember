# mcp/tests/test_serving_response_conformance_cases_2.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_serving_response_conformance_cases_2.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-09-04T01:06+02:00 |
| lastVerifiedCommitHash | `1993dd25bdf8331a2c1e28171dff2bf92ea090e2` |
| lastVerifiedCommitDate | 2026-09-04T00:57:29+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Serving response-conformance suite for notes, changesets, actions, inbox, terminal catalog/control, harness control, and conversation routes.


## 260831-CCR-L23 Requirement-Route Conformance Cases

L23 added `test_requirement_routes_conform` to the shared conformance driver:
`GET /api/requirements/list` is driven to 200 (seeded context), 400
(wrong-document context), and 404 (unknown repo), and `GET /api/requirements/read`
to 200 (seeded packet), 400 (traversal path), and 404 (ghost packet) — each validated
against the declared response model.

## Code Commentary

### Logic

Cases pin public action/inbox and catalog bodies after task-document identity replaced leaf ownership, while preserving typed success/refusal unions for each route family.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the registered or owning seam directly.

### Invariants And Boundaries

Internal model changes cannot leak undeclared fields or revive removed leaf-address vocabulary on served responses.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `ServingResponseConformance2` | mcp/tests/test_serving_response_conformance_cases_2.py:21-21 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: recorded the `test_requirement_routes_conform` driver cases for the requirement endpoints.

- 2026-08-11T19:58+02:00 — Reconciled `test_serving_response_conformance_cases_2.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
