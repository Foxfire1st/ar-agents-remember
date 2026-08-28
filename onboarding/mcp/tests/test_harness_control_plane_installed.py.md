# mcp/tests/test_harness_control_plane_installed.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_plane_installed.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
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

Two live-seam classes are opt-in (`AR_RUN_CONTROL_PLANE_INSTALLED=1`) and carry the registered
`@pytest.mark.ar_run_control_plane_installed` marker, so the pair can also be selected or
deselected by name; `ClaudeInstalledHonestyTests` is the unmarked fixture-honesty class and has no
environment gate. All three are version-locked and skip with an exact reason where a precondition
is absent. `CodexInstalledControlPlaneTests` (pinned
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
machines without the pinned runtimes skip. Cockpit submissions are issued as
`submit_control_prompt(entry, text, ControlSubmission(...))`, with the source, request id,
`expected_bridge_epoch` guard, and any staged `assets` travelling inside that one parameter object.
The `_version_of` probe skips a missing executable. Once an opted-in executable is selected,
process-start and subprocess failures remain real test failures rather than unavailable evidence.

### Invariants And Boundaries

- Every test skips honestly with an exact reason where the pinned runtime is absent or
  version-mismatched; no synthetic capability evidence is ever produced.
- The production seam is exercised end-to-end (adapter → bridge → IPC → client); no fixture-only
  production authority.
- Captured fixture rows retain only allow-listed field presence — no prompts, paths, ids, or
  conversation material.
- Claude rows stay `not-exercised` with the exact version-mismatch + CL-3 reason until a locked
  2.1.211 install exercises the seam.
- A missing installed command skips before live-seam evidence is claimed; a selected command that
  cannot run fails the opted-in proof.

### Todos

Re-run under a locked Claude 2.1.211 install to replace the `not-exercised` control-plane row
with observed evidence through the same redaction policy.

## Docs References

No Domain Documentation source is configured. The installed runtimes and the repository fixture
contract are the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The runtime fixtures recording (never enabling) the `control-plane/*` rows this suite captures. | "control-plane/interrupt-write-ack"; "control-plane/abort-write-ack"; "control-plane/interrupt-and-assets" | mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json:94-137; mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json:71-102; mcp/tests/fixtures/conversation_runtime/claude-2.1.211.json:45-50 |
| The client helpers driven against the live socket (`interrupt_control`, `read_operation_timeline`, asset-carrying submit, withdrawal). | "def withdraw_control_submission("; "def submit_control_prompt("; "def interrupt_control("; "opaque cursor coordinates are invalid in the operation timeline domain" | mcp/src/agents_remember/serving/harness_control_client.py:190-190; mcp/src/agents_remember/serving/harness_control_client.py:216-216; mcp/src/agents_remember/serving/harness_control_client.py:431-431; mcp/src/agents_remember/serving/harness_control_client.py:454-478 |
| The contract-suite companion pinning the same seams over fake transports. | "Contract tests for the native control-plane substrate." | mcp/tests/test_harness_control_plane.py:1-45 |
| The L0E installed-suite precedent for opt-in version-locked capture. | "LIVE_OPT_IN = \"AR_RUN_EVIDENCE_INSTALLED\""; "class CodexInstalledEvidenceTests(unittest.IsolatedAsyncioTestCase):" | mcp/tests/test_harness_control_evidence_installed.py:64-64; mcp/tests/test_harness_control_evidence_installed.py:133-133 |
| The installed-version probe skips absent commands and executes selected commands strictly. | `_version_of` | mcp/tests/test_harness_control_plane_installed.py:96-105 |

## Cross-Repo References

No neighboring repository participates in this installed-runtime suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-28T06:28+02:00 — No content impact: extracted the exact Claude fixture path into one
  literal constant for source-observable lifecycle ownership; control-plane assertions are
  unchanged.

- 2026-08-12T08:41+02:00 — 260731-EFA-L20 narrowed the installed-runtime skip boundary: absent executables still skip, but a selected executable that cannot start or complete now fails the opted-in proof.
- 2026-08-11T22:28+02:00 — 260731-EFA-L19 final curator pass: recorded the unavailable-harness
  skip when the installed version process cannot start or complete. No observed fixture evidence
  follows from that skip; verification metadata remains pinned until closeout.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 4 citation rows: the three runtime fixtures now carry one `path:start-end` citation each (codex L94-L137, pi L71-L102, claude L45-L50 — the ` · ` separator form replaced), plus the client helpers, the contract-suite companion, and the L0E precedent; removed one superseded history line-spelling. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the runtime-fixture citation. One shared
  range was being applied to three files of different lengths and overran the 139-line codex
  fixture; the row now carries one range per fixture, each covering exactly that file's
  `control-plane/*` entries: `codex-0.144.5.json` L94-L137 (interrupt-write-ack, operation-timeline,
  asset-local-image-submit, withdrawal-recovery), `pi-0.80.7.json` L71-L102 (abort-write-ack,
  operation-timeline, asset-image-submit), and `claude-2.1.211.json` L45-L50 (interrupt-and-assets,
  `not-exercised`). The path separator in that cell changed from `;` to ` · ` so ranges and paths
  pair up positionally, as elsewhere in this tree.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 quality gate: the two live-seam classes now carry the
  registered `@pytest.mark.ar_run_control_plane_installed` marker (`ClaudeInstalledHonestyTests` is
  unmarked and has no environment gate), and every cockpit submission passes a single
  `ControlSubmission` parameter object carrying the source, request id, `expected_bridge_epoch`, and
  staged `assets`. Corrected the Logic opening, which counted three environment-opt-in classes, and
  documented the submission parameter object under Conventions.

- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: created the installed-runtime control-plane
  capture sidecar (codex/pi live proofs plus Claude version honesty, opt-in and version-locked).
  Verification is blank until closeout commits and stamps the new source.
