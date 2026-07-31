# mcp/tests/test_conversation_library_open.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_open.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Deep tests for the 260718-CHATS-L2 `ConversationOpenService` with doubled launch/proof/retire
boundaries: idempotence, exact-identity proof, honest retirement, ledger bounds, the codex
resume channel, and the review-driven race/ownership regressions.

## Code Commentary

### Logic

Twenty async tests cover: the pre-launch poll race (status/reconcile stay pending, released
mismatch retires for real — review F1); absent-row retirement reporting `retire-pending` with
reconcile completing it; the codex `resume_thread_id` channel pass-through, its invalid-target
and non-codex-kind guards; identical replay after ledger-record eviction absorbing through the
live row; evicted changed-conversation replay never retiring the foreign session (review F5);
exact-identity proof with idempotent replay; changed-fingerprint conflict without launch;
unsupported resume never launching; stale expected digest and stale native resolve mapping;
launch-failure 503 shape with no identity; identity-mismatch retirement and reporting;
timeout-unknown staying reconcilable and opening later; ledger-full-of-live refusal; LRU
terminal eviction; ready-without-vendor-identity staying reconcilable; and pre-existing catalog
rows never being touched.

### Conventions

The opener, readiness, and retirement boundaries are doubled with event-parked drives and
flaky-catalog constructions so interleavings are deterministic; the installed suite covers the
same arms live.

### Invariants And Boundaries

- A poll must never settle a pre-launch record, and a tombstone claim must never precede a real
  retirement.
- An absorbed pre-existing session is never retired, whatever it proves.
- Every terminal outcome leaves the ledger evictable; no zombie pending slot survives a drive
  fault.

### Todos

None.

## Docs References

No Domain Documentation source is configured. The repository sources are direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The open service, bounded ledger, and record model under test. | L87-L184; L209-L320 | [open_service.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/open_service.py) |
| The ASGI open/status/reconcile surface mapping the same outcomes to HTTP. | L535-L703 | [test_conversation_library_api.py](agents-remember/mcp/tests/test_conversation_library_api.py) |
| The installed suite's real open E2Es for the Pi and Codex channels. | L284-L413; L416-L551 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |

## Cross-Repo References

No neighboring repository participates in this open suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation into
  `test_conversation_library_installed.py`. The two real-open E2E classes are now `PiOpenEndToEndTests`
  L284-L413 and `CodexOpenEndToEndTests` L416-L551 (was the single range L360-L539, which straddled the
  two). Verified by reading both class bodies.
- 2026-07-31T16:50+02:00 — No content impact: 260731-EFA-L2 curator checked this file against the
  leaf diff. Every `ConversationOpenService` construction now takes
  `LibraryBinding(runtime=…, shared=…, authorization=…)`, every `service.open(...)` call passes an
  `OpenRequest(request_id=…, expected_identity_digest=…, cwd=…, launch_context=…)`, and the
  `_Opener` double now receives a `TerminalLaunchRequest`/`SpawnProvenance` pair — so the launch
  assertions read `launch.harness`, `launch.control.resume_thread_id`, `launch.knobs.launch_args`
  and `launch.workspace_root` where they previously read the same values out of a kwargs dict. The
  `retire_entry` patches also absorb positional arguments. All twenty async tests keep their names
  and their asserted outcomes (`opened`, `unsupported`, `stale-identity`, `launch-failed`,
  `identity-mismatch`, `timeout-unknown`, `retire-pending`, ledger-full refusal and LRU eviction),
  and this sidecar cites no line range into this file, so the Logic enumeration and the three
  invariants stand.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the open service deep-test sidecar.
  Verification is blank until closeout commits and stamps the new source.
