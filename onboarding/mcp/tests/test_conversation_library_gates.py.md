# mcp/tests/test_conversation_library_gates.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_gates.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Live capability gate registry tests for 260718-CHATS-L2 with doubled native boundaries: proves
the version-match/mismatch demotion rules, probe-failure honesty, missing-binary posture, and
helper-preflight gates without touching real harness processes.

## Code Commentary

### Logic

Seven async tests drive `LibraryGateRegistry` with injected codex probes, `which` resolvers,
and environments: exact Codex version match enables list/read/resume with honestly `partial`
completeness; a version mismatch demotes the whole surface to `unverified` with the
observed-versus-locked reason; a failed probe is `unverified` (never `unavailable`); missing
binaries and unknown harnesses are `unavailable`; helper success enables Pi with full
completeness; helper failure and missing locked dependencies are `unverified`.

### Conventions

Executable fingerprints ride real `tmp_path` files so the per-fingerprint cache behaves exactly
as in production; all native boundaries stay doubled (the installed suite covers them live).

### Invariants And Boundaries

- No test may produce `supported` without injected runtime-fixture evidence at the locked
  versions — mirroring the model-enforced honesty rule.
- Demotion reasons must carry the exact observed-versus-locked detail.

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
| The gate registry, locked Codex version constant, and per-fingerprint cache under test. | L146-L192; L40 | [gates.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/gates.py) |
| The installed-runtime suite re-proving the same gates on real harnesses. | L134-L152; L215-L230 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |

## Cross-Repo References

No neighboring repository participates in this gate suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the capability gate registry suite
  sidecar. Verification is blank until closeout commits and stamps the new source.
