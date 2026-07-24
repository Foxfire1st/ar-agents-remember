# mcp/tests/test_harness_control_plane.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_plane.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T00:08+02:00 |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

R10 contract suite for the 260718-CHATS-L2E native control-plane substrate: pins the interrupt
write, the paged never-bodies operation-timeline enumeration, the digest-verified asset channel,
and the once-only withdrawal-recovery payload across fake/capable adapters, fake codex/pi
transports, a real IPC socket, and the validated blocking client — 25 tests plus 35 subtests.

## Code Commentary

### Logic

`InterruptBridgeTests` pins the bridge dispatch contract: epoch stamp on the acknowledgement,
replay-once without a second adapter call, adapter-mint-epoch refusal, and the structural
unsupported refusal naming the adapter (`_PlainAdapter` vs `_CapableAdapter`).
`CodexInterruptTests` drives `_FakeCodexTransport`: exact-active-turn `turn/interrupt` write with
replay, no-active typed refusal, and RPC failure mapped to a `rejected` acknowledgement.
`PiInterruptTests` drives `_FakePiTransport`: the `expected_operation_id` pre-write guard,
replay-once per (expected, active) pair, the successor stale-reconcile typed refusal with zero
second writes, no-active typed refusal, the content-less `message_end` evidence mapping with
preserved role strictness, and native failure as a `rejected` acknowledgement.
`OperationTimelineTests` enumerates all three prompt sources plus set-model/set-effort kinds with
the exact ten-key never-bodies shape, proves paged-union completeness without overlap, discloses
the eviction floor with converging re-reads, and measures the full 256-record ledger against the
shared byte budget (multi-page, worst page within budget, union == 1..256), with epoch flip and
cross-domain cursor coordinates failing typed at the client. `AssetChannelTests` runs the schema
battery (12 bad shapes typed), the traversal battery (either component, NUL-translated, no
out-of-root access), size/digest/missing verification, the non-capable `unsupported` receipt with
the timeline state marking, and the asset-conditional idempotence digest (conflict on
same-text-with-asset, dedupe on identical asset set). `AssetNativeConstructionTests` proves codex
`localImage` blocks and pi base64 `images[]` content with construction-time re-verification
(corrupted staged bytes → clean `rejected` receipt, zero native writes) plus additive receipt
`assetIds`. `WithdrawalRecoveryTests` proves the exact body crosses once at the true transition
with the tombstone/`cockpit_only` posture byte-preserved and the replay carrying none.
`ClientValidationTests` pins the strict validators: bad acknowledgement, epoch mismatch,
non-monotonic items, invalid kind/source, zero/duplicate sequence, floor above high-water,
non-boolean/empty-truncated pages, `latestSequence` behind the last item, and malformed recovery.

### Conventions

Focused contract suite in the L0E `test_harness_control_evidence.py` posture: fake transports and
a real IPC socket, no fixture-only production authority, no installed-runtime dependence (that
capture lives in `test_harness_control_plane_installed.py`). Every battery asserts typed refusal
reasons, not bare exception classes.

### Invariants And Boundaries

- The full pre-existing suite stays green unmodified; this file is the additive regression pin,
  never a rewrite of existing IPC semantics.
- Timeline assertions never expect bodies — the ten-key item shape with digest-presence only.
- Interrupt assertions prove settlement flows through the landed completion path, never the
  acknowledgement.
- Asset assertions prove no filesystem access outside `<endpoint-root>/assets` and byte-identical
  asset-free digests/receipts.

### Todos

None.

## Docs References

No Domain Documentation source is configured. The repository sources under test are the direct
evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The bridge epoch-guarded interrupt dispatch and timeline delegation under test. | L241-L290 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The authority's paged ledger enumeration, recovery capture, and asset channel under test. | L436-L485; L515-L531; L1053-L1073 | [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py) |
| The codex/pi interrupt and asset implementations under fake-transport test. | L276-L342 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py); [pi_rpc_adapter.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_adapter.py) L393-L477 |
| The IPC asset admission and the two additive actions exercised over a real socket. | L212-L215; L252-L325; L449-L490 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| The strict client validators exercised by the validation battery. | L667-L790 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| The installed-runtime companion that captures the same seams live into the redacted fixtures. | L126-L364 | [test_harness_control_plane_installed.py](agents-remember/mcp/tests/test_harness_control_plane_installed.py) |

## Cross-Repo References

No neighboring repository participates in this contract suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260718-CHATS-L5I Current Delta

The control-plane suite now pins native interrupt transport, structured pending-interaction payloads, and the raised but finite IPC payload budget at the real bridge boundary.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: created the control-plane contract-suite
  sidecar (interrupt/timeline/asset/recovery batteries plus client validation, 25 tests + 35
  subtests). Verification is blank until closeout commits and stamps the new source.
