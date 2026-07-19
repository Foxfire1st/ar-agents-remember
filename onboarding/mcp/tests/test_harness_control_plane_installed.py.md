# mcp/tests/test_harness_control_plane_installed.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_plane_installed.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T00:08+02:00 |
| lastVerifiedCommitHash |  `22562e0f2161c2d980385a462275dc370deb72eb`|
| lastVerifiedCommitDate |  2026-07-20T00:45:01+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Installed-runtime production-seam capture for the 260718-CHATS-L2E control-plane substrate:
exercises the REAL seam — installed harness → real adapter → control bridge → IPC server →
blocking client — for the interrupt write, operation-timeline enumeration, asset channel, and
withdrawal recovery against the pinned harness versions, and enforces the Claude version-honesty
posture on the fixture rows.

## Code Commentary

### Logic

Three opt-in classes (`AR_RUN_CONTROL_PLANE_INSTALLED=1`), each version-locked and skipping with
an exact reason where its precondition is absent. `CodexInstalledControlPlaneTests` (pinned
0.144.5) spawns the real app-server and proves one accepted `turn/interrupt` acknowledgement
(`vendorCorrelationId=turn`), the interrupted settlement crossing the existing completion path, a
post-settlement interrupt refused typed, the paged timeline over a live cockpit submission, a
staged PNG accepted as a `localImage` input block, and the exact withdrawal-recovery body
crossing once with the replay carrying none. `PiInstalledControlPlaneTests` (pinned 0.80.7)
spawns the real RPC process and proves the guarded abort accepted with the active-operation
identity on the result, a stale `expectedOperationId` after settlement refused typed with zero
writes, the timeline, and a staged PNG accepted as base64 image content.
`ClaudeInstalledHonestyTests` reads the locked 2.1.211 fixture and asserts every
`control-plane/*` row stays `not-exercised` with the locked version named in the reason while the
installed version mismatches (2.1.214); a matching locked install skips because the capture then
belongs to a locked-gate evidence run.

### Conventions

These tests are the evidence source for the redacted `control-plane/*` fixture rows: what passes
here on a qualifying machine is what the fixtures record (shape descriptors only,
`enablesCapabilities: false`, never enabling). Version locks keep the evidence version-honest; CI
machines without the pinned runtimes skip.

### Invariants And Boundaries

- Every test skips honestly with an exact reason where the pinned runtime is absent or
  version-mismatched; no synthetic capability evidence is ever produced.
- The production seam is exercised end-to-end (adapter → bridge → IPC → client); no fixture-only
  production authority.
- Captured fixture rows retain only allow-listed field presence — no prompts, paths, ids, or
  conversation material.
- Claude rows stay `not-exercised` with the exact version-mismatch + CL-3 reason until a locked
  2.1.211 install exercises the seam.

### Todos

Re-run under a locked Claude 2.1.211 install to replace the `not-exercised` control-plane row
with observed evidence through the same redaction policy.

## Docs References

No Domain Documentation source is configured. The installed runtimes and the repository fixture
contract are the direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The runtime fixtures recording (never enabling) the `control-plane/*` rows this suite captures. | L1-L140 | [codex-0.144.5.json](agents-remember/mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json); [pi-0.80.7.json](agents-remember/mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json); [claude-2.1.211.json](agents-remember/mcp/tests/fixtures/conversation_runtime/claude-2.1.211.json) |
| The client helpers driven against the live socket (`interrupt_control`, `read_operation_timeline`, asset-carrying submit, withdrawal). | L398-L450; L179-L227 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| The contract-suite companion pinning the same seams over fake transports. | L252-L1575 | [test_harness_control_plane.py](agents-remember/mcp/tests/test_harness_control_plane.py) |
| The L0E installed-suite precedent for opt-in version-locked capture. | L115-L362 | [test_harness_control_evidence_installed.py](agents-remember/mcp/tests/test_harness_control_evidence_installed.py) |

## Cross-Repo References

No neighboring repository participates in this installed-runtime suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: created the installed-runtime control-plane
  capture sidecar (codex/pi live proofs plus Claude version honesty, opt-in and version-locked).
  Verification is blank until closeout commits and stamps the new source.
