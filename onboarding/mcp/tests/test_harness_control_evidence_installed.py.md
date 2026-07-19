# mcp/tests/test_harness_control_evidence_installed.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_evidence_installed.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T09:15+02:00 |
| lastVerifiedCommitHash | `ca9dd05a295ef5f24c479e2231fdcd174b372e04`|
| lastVerifiedCommitDate | 2026-07-19T10:04:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Installed-runtime production-seam capture for the 260718-CHATS-L0E evidence family and codex
resume channel. Opt-in (`AR_RUN_EVIDENCE_INSTALLED=1`) and version-locked to the fixtures in
`mcp/tests/fixtures/conversation_runtime/`: a real installed harness drives the real adapter →
control bridge → IPC server → blocking client path, and the redacted observations land in the
fixtures' `substrate-evidence/*` rows. Skips carry exact reasons on machines without the pinned
runtimes, so CI never spends real LLM turns.

## Code Commentary

### Logic

`CodexInstalledEvidenceTests` (locked 0.144.5) drives one ephemeral thread through the production
seam and asserts evidence frames cross with `bridgeEpoch` while `snapshot.raw` stays free of
`arEvidence`; asserts the ephemeral `thread/read` `includeTurns` refusal crosses typed with the
native reason; then opens a persisted thread, pages it through the native read with typed identity,
builds a second adapter through the factory resume channel, and proves `thread/resume` reopens the
exact persisted thread whose items page identically; a live cockpit submission's source crosses
the provenance batch with exact epoch scoping. `PiInstalledEvidenceTests` (locked 0.80.7) drives
one prompt and asserts live evidence frames, the `get_entries` native page with typed identity, the
provenance batch, and the no-leak guarantee. `ClaudeInstalledHonestyTests` keeps the Claude row
honestly `not-exercised` while the installed version (2.1.214) mismatches the locked 2.1.211 gate,
with the exact reason asserted.

### Conventions

Every captured observation is redacted to the fixture allow-list: counts, kinds, field presence,
and shape descriptors only — never content, paths, native text, or credentials. Version probes use
`--version` subprocesses; live turns use a one-word prompt.

### Invariants And Boundaries

- The opt-in environment variable is the sole activation; without it every live class skips with
  an exact reason.
- Fixture rows record `observed` only for seams actually exercised through production code;
  `enablesCapabilities` stays `false` and version-mismatched harnesses stay `not-exercised`.
- No fixture-shaped canned response can substitute for a live seam: the bridge epoch must be live.

### Todos

Delta-heavy codex streams and large-thread `thread/read` latency remain unmeasured (worker
confidence register entries 3/9); a later tuning leaf owns realistic pressure evidence.

## Docs References

No Domain Documentation source is configured. The installed production seam is the direct
evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The redacted codex `substrate-evidence/*` rows this suite captures and honors. | L35-L79 | [codex-0.144.5.json](agents-remember/mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json) |
| The redacted pi `substrate-evidence/*` rows this suite captures and honors. | L37-L69 | [pi-0.80.7.json](agents-remember/mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json) |
| The claude row whose version-mismatch reason this suite enforces. | L37-L43 | [claude-2.1.211.json](agents-remember/mcp/tests/fixtures/conversation_runtime/claude-2.1.211.json) |
| Foundation tests require non-enablement and a raw-free fixture set across these files. | L102-L137 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The deterministic contract suite whose fake-transport claims this file re-proves live. | L268-L1470 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py) |

## Cross-Repo References

No neighboring repository participates; installed harness binaries are local tools, not repo
boundaries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: created the installed-runtime evidence
  capture sidecar (3 opt-in classes: codex 0.144.5 live incl. ephemeral refusal + resume E2E, pi
  0.80.7 live, claude version-honesty). Verification is blank because the new source file is
  uncommitted; closeout owns its first source stamp.
