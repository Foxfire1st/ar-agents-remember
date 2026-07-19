# mcp/tests/test_harness_control_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T09:15+02:00 |
| lastVerifiedCommitHash | `ca9dd05a295ef5f24c479e2231fdcd174b372e04`|
| lastVerifiedCommitDate | 2026-07-19T10:04:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Contract suite for the 260718-CHATS-L0E native evidence and resume substrate (leaf R12 clauses
(i)–(viii)). It proves the per-harness evidence round-trips, the bounded buffer semantics, the
no-leak guarantee, native-page continuation correctness, the submission-provenance batch, the
codex resume launch channel, and zero regression of existing IPC semantics — all through the
production mapper → reserved key → bridge buffer → IPC → validated client seam.

## Code Commentary

### Logic

`EvidenceBufferTests` drives a fake adapter through the real bridge: reserved-key round-trip with
no leak into `snapshot.raw`, the projected catalog `control_raw`, or subscriber snapshots while the
evidence page carries the frame; unknown-vendor pass-through with raw preserved and semantics never
guessed; count eviction with an honest gap floor at two sizes; the visible bounded byte clip;
byte-budget paging without overlap or gap; and visible bridge failure on non-monotonic sequences or
non-object payloads. `EvidenceIpcTests` runs the real IPC server over a Unix socket: evidence
paging with epoch stamps, typed cross-domain coordinate rejection in both directions, fail-closed
native pages for unsupported adapters, bridge-stamped epochs on native pages, the full provenance
matrix (all three sources, not-found, epoch mismatch, duplicate ids, 65-id overflow) through the
bridge → queue → authority delegation, and the fixture-honesty proof that a canned fixture-shaped
response without a live epoch fails client validation. `CodexEvidenceTests` proves the previously
dropped `item/completed` and `thread/tokenUsage/updated` frames cross with native ids, and that
`thread/read` paging continues with no overlap/gap, is null-terminated, fails closed on absent
cursors and duplicate item identity, and clips an oversized single frame while still progressing.
`PiEvidenceTests` proves `message_end` and unknown frames cross with full payloads and that the
`get_entries(since)` native page carries typed identity with duplicate-id fail-closed.
`ClaudeEvidenceTests` proves assistant blocks and result usage/cost forward as full evidence
without leaking into the adapter's own snapshot raw. `ResumeChannelTests` and `ResumeOpenerTests`
pin the `resumeThreadId` payload round-trip, legacy field-less parse, malformed rejection, codex-only
factory construction with pre-spawn refusal for non-codex harnesses, the opener `bad-kind` refusals
with zero host interactions, and absent-field behavior preservation. `ClipHelperTests` covers the
clip helper's small-payload passthrough, visible marker, and non-serializable rejection.

### Conventions

Tests are `unittest.IsolatedAsyncioTestCase` classes over in-process fakes and real Unix-socket
IPC endpoints under `tmp_path`; assertions are exact-value, never vacuous shape checks. The suite
imports only the production seam it pins — no fixture-only production authority.

### Invariants And Boundaries

- Every evidence assertion proves both sides: the frame reaches the evidence page AND no projection
  (`snapshot.raw`, `control_raw`, SSE subscriber) carries `arEvidence` or payload bytes.
- Coordinate domains stay disjoint: native cursors fail typed in the deque domain and adapter
  sequences fail typed in the native domain, client-side and server-side.
- Continuation must be exact: no overlap, no gap, null-terminated, and an epoch flip mid-paging
  raises `HarnessBridgeEpochMismatchError`.
- The resume channel refuses non-codex harnesses and malformed values before any spawn.
- Existing IPC semantics stay green unmodified; this suite adds coverage without editing prior
  suites.

### Todos

Delta-heavy codex streams at realistic sizes and large-thread `thread/read` latency remain
unmeasured by design (worker confidence register entries 3/9); bounds are additive tunables.

## Docs References

No Domain Documentation source is configured. The production seam under test is the direct
evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The bounded evidence deque, reserved-key diversion, and epoch-stamped page reads under test. | L85-L88; L168-L232; L440-L471 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The three additive IPC actions exercised over a real socket. | L198-L203; L286-L313 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| The strict client validators for pages, native pages, and provenance. | L286-L358; L576-L730 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| The authority's provenance batch read exercised through the queue delegation. | L375-L412 | [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py) |
| The codex stop-dropping forwards and `thread/read` native page under test. | L334-L361; L503-L600 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| The resume payload/parse/factory/opener channel under test. | L46-L105 | [harness_control_runner.py](agents-remember/mcp/src/agents_remember/serving/harness_control_runner.py) |

## Cross-Repo References

No neighboring repository participates in this contract suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: created the evidence contract suite sidecar
  (32 tests + 6 subtests covering R12 (i)–(viii)). Verification is blank because the new source
  file is uncommitted; closeout owns its first source stamp.
