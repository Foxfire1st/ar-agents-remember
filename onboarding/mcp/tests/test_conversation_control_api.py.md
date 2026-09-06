# mcp/tests/test_conversation_control_api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_control_api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Conversation HTTP interrupt and attachment lifecycle integration.

## Code Commentary

### Logic

A real HTTP/bridge/IPC fixture drives interrupt acceptance, pending settlement, idempotent replay and final interrupted status with one native write. Remote authorization refuses with typed 403. Attachment staging, submit, status and reconcile preserve receipt metadata and missing requests return 404.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The adapter is a harness-edge double. No retained source-scan or complete policy/telemetry response matrix is asserted by these three cases.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Interrupt ack settle replay and single write. | `test_interrupt_ack_settle_replay_and_single_write` | mcp/tests/test_conversation_control_api.py:88-120 |
| Remote peer fails closed typed 403. | `test_remote_peer_fails_closed_typed_403` | mcp/tests/test_conversation_control_api.py:122-131 |
| Attachment stage submit status reconcile. | `test_attachment_stage_submit_status_reconcile` | mcp/tests/test_conversation_control_api.py:137-193 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the switch from adapter convenience methods to shared raw event-replay helpers; HTTP interrupt and settlement assertions are unchanged.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 6 citation finding(s); scoped recheck clean.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the `control/api.py` citation. The file
  is now 686 lines and the stamped `L57-L570` both started before the routes (in the import block)
  and stopped four routes short. Counted the `@router` decorators: exactly seventeen, at L131, 160,
  190, 220, 242, 272, 300, 328, 352, 378, 420, 465, 497, 524, 551, 590 and 612 — so the claim's
  count still holds — spanning L131 through the end of `conversation_telemetry` at L631. The O4
  typed-error mapping is `_map_typed_error` at L107-L124 (epoch mismatch 409, authorization 403,
  composition 503, ref/operation/session self-describing status, control 503, re-raise otherwise).
  Split into those two ranges; claim unchanged.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2: corrected the in-file anchor for
  `test_no_paste_pty_or_native_queue_substitution_in_control_modules`, which the leaf moved from
  L354 to L355 — the terminal-wire submission dropped one line by folding `source`/`request_id`
  into `ControlSubmission`, and a `ruff format` reflow of the usage assertion added two. Named the
  new submission object in the Logic paragraph. `ControlApiTests` still opens at L26, and the
  seventeen routes, the O4 typed-error mapping, the remote-peer 403, the epoch guards, the policy
  405s and the source scan are all untouched.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the production-route
  suite — the seventeen routes over a real uvicorn wire, O4 mapping, remote-peer 403, epoch guards,
  multipart staging, policy 405s, the queue-truth privacy/withdrawal flow, and the no-paste/no-
  substitution source scan. Verification is blank because the new source file is uncommitted;
  closeout owns its first source stamp.
