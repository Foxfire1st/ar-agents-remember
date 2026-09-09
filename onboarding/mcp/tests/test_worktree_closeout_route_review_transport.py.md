# mcp/tests/test_worktree_closeout_route_review_transport.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_closeout_route_review_transport.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-08T16:05:21+02:00 |
| lastVerifiedCommitHash | `602143bd1d48226f4d53b83ff7c5002a695dcdff` |
| lastVerifiedCommitDate | 2026-09-09T00:26:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Registered public closeout transport proof for truthful route-review refusal responses.

## Code Commentary

### Logic

The registered preview case sends a temporary changed leaf through the real stdio MCP server and
asserts readable text plus structured content, current route-review status, exact contract-bound
`task_doc` guidance, and unchanged task, contract, and Git state. The certification projection case
keeps the original route finding while promoting its concrete status. The registered apply case
injects a typed stale-review refusal at the application seam and proves its contract guidance
survives response enrichment. These fixtures do not publish a review, commit code, or certify
closeout.

### Conventions

This file is integration evidence for public transport serialization and application-boundary
projection. The review payload remains caller-supplied; `nextRequiredArgs` names it without
inventing `nextArgs`.

### Invariants And Boundaries

- A route-review refusal leaves task documents, contracts, and code `HEAD` unchanged.
- The response keeps exact observed status/detail and task-bound recovery identity.
- Temporary transport evidence does not establish terminal rail, Dagger, aggregate review, or
  acceptance behavior.

## Docs References

No Domain Documentation entries are configured for this repository-owned integration fixture.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain evidence applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Registered preview preserves route-review reason, structured response, and exact retry bounds. | `test_registered_closeout_preview_preserves_route_review_reason_and_retry` | mcp/tests/test_worktree_closeout_route_review_transport.py:63-111 |
| Certification projection preserves the route finding while promoting status. | `test_certification_admission_refusal_keeps_route_review_status` | mcp/tests/test_worktree_closeout_route_review_transport.py:114-133 |
| Registered apply catches typed stale-review refusal with contract guidance. | `test_closeout_apply_admission_catches_route_review_with_contract_guidance` | mcp/tests/test_worktree_closeout_route_review_transport.py:136-170 |

## Cross-Repo References

No cross-repository implementation evidence is required for this disposable registered fixture.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture does not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: created the one-to-one sidecar for the frozen registered route-review transport proof. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.
