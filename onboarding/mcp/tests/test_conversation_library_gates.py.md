# mcp/tests/test_conversation_library_gates.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_gates.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate |  2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Live capability gate registry tests for 260718-CHATS-L2 with doubled native boundaries: proves
the CONTRACT-PROBE gate rules (the connect+list/read probe is the only gate; version drift stays
informational — 260718-CHATS-L5F R4), probe-failure honesty, missing-binary posture, and
helper-preflight gates without touching real harness processes.

## Code Commentary

### Logic

The async tests drive `LibraryGateRegistry` with injected codex probes, `which` resolvers,
and environments: a passing Codex connect+list/read probe enables list/read/resume with honestly
`partial` completeness, and (260718-CHATS-L5F R4)
`test_version_drift_still_enables_codex_when_the_probe_passes` proves a drifted CLI version STILL
enables the surface as long as the contract probe passes — the observed version rides as
informational evidence, no longer a demotion gate; a failed probe is `unverified` (never
`unavailable`); missing binaries and unknown harnesses are `unavailable`; helper success enables Pi
with full completeness; helper failure and missing locked dependencies are `unverified`. The former
"version mismatch demotes the whole surface" case is removed — version equality no longer gates a
capability anywhere.

### Conventions

Executable fingerprints ride real `tmp_path` files so the per-fingerprint cache behaves exactly
as in production; all native boundaries stay doubled (the installed suite covers them live).

### Invariants And Boundaries

- No test may produce `supported` without a passing contract probe through the production seam —
  mirroring the model-enforced honesty rule; runtime-fixture evidence records the shapes, never a
  version equality.
- A capability demotes only on a failed or never-run contract probe; a version difference alone
  never demotes (260718-CHATS-L5F R4), and demotion reasons carry the contract-verification detail,
  not an observed-versus-locked version comparison.

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

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: corrected the version-gate language for the R4
  removal — the suite now proves the CONTRACT PROBE is the only gate
  (`test_version_drift_still_enables_codex_when_the_probe_passes`: a drifted CLI version still enables
  codex when the connect+list probe passes; observed version rides as informational evidence). Removed
  the false "version mismatch demotes the whole surface" description and the observed-versus-locked
  demotion invariant. Verification metadata stays pinned (uncommitted); closeout re-stamps.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the capability gate registry suite
  sidecar. Verification is blank until closeout commits and stamps the new source.
