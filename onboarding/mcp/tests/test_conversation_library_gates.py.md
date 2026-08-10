# mcp/tests/test_conversation_library_gates.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_gates.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The gate registry, locked Codex version constant, and per-fingerprint cache under test. | `LibraryGateRegistry`; `LOCKED_CODEX_RUNTIME_VERSION` | mcp/src/agents_remember/serving/conversation/library/gates.py:50-50; mcp/src/agents_remember/serving/conversation/library/gates.py:173-326 |
| Codex gate behavior is covered by the focused test class. | `CodexGateTests` | mcp/tests/test_conversation_library_gates.py:63-148 |
| Helper-backed gate behavior is covered by the focused test class. | `HelperGateTests` | mcp/tests/test_conversation_library_gates.py:151-212 |

## Cross-Repo References

No neighboring repository participates in this gate suite.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-04T11:32:09+02:00 — 260731-EFA-L6 S18-B02 curator: replaced unanchored gate references with exact local anchors and generated final ranges with the scoped fixer.

- 2026-07-31T16:50+02:00 — No content impact: 260731-EFA-L2 curator checked this file against the
  leaf diff. The only change is the local `_registry` helper handing `LibraryGateRegistry` a
  `GateProbes(codex_probe=…, which=…)` parameter object instead of the two loose keyword
  arguments, plus the matching import. Every test body is untouched, all eight method names
  survive (including `test_version_drift_still_enables_codex_when_the_probe_passes`), the codex
  probe and `which` resolver are still injected doubles under a different wrapper, and this
  sidecar cites no line range into this file. The contract-probe-is-the-only-gate description and
  both honesty invariants still read true against the current source.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: corrected the version-gate language for the R4
  removal — the suite now proves the CONTRACT PROBE is the only gate
  (`test_version_drift_still_enables_codex_when_the_probe_passes`: a drifted CLI version still enables
  codex when the connect+list probe passes; observed version rides as informational evidence). Removed
  the false "version mismatch demotes the whole surface" description and the observed-versus-locked
  demotion invariant. Verification metadata stays pinned (uncommitted); closeout re-stamps.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the capability gate registry suite
  sidecar. Verification is blank until closeout commits and stamps the new source.
