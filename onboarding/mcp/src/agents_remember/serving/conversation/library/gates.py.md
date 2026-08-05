# mcp/src/agents_remember/serving/conversation/library/gates.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/gates.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate |  2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The live production-path capability gates for the dormant native library: a harness's history
features report `supported` only after a real CONTRACT probe against the installed runtime passes
(Codex proves `thread/list` over a real app-server connection; Claude/Pi prove the repository
helper's handshake plus a real native `list` call), and a missing binary or a failed probe demotes
the whole surface with an exact reason — fail closed and visible, never invented parity.

THE CONTRACT IS THE ONLY GATE (developer ruling 2026-07-21, 260718-CHATS-L5F R4): the probe result
alone decides the state. The observed CLI/runtime/helper version is recorded as informational
evidence and is NEVER compared to a locked constant to demote a capability — harnesses auto-update,
and a version predicate is exactly what made a natively-working install fail closed.

## Code Commentary

### Logic

`LibraryGateRegistry.history_capabilities` resolves the harness from the L0 registry, resolves
the installed executable, and gates once per installed-executable fingerprint (path + size +
mtime), cached per harness and bounded by construction to the three normalized harnesses; an
executable change re-runs the contract probe. The Codex gate runs a real app-server connect +
initialize + `thread/list` probe: if it succeeds the history contract verified against the running
app-server and the surface is enabled; the observed CLI version rides the evidence as informational
metadata only and is NEVER compared to `LOCKED_CODEX_RUNTIME_VERSION` (0.144.5), which now survives
as a published reference/skip-guard constant, not a gate. The Claude/Pi helper gates run
`helper_preflight` (node, locked entry, installed locked dependencies) plus a real native `list`
call through the helper host; the per-spawn handshake reports the observed runtime/helper versions
as informational evidence only, and the OPERATION result is the gate. Supported profiles are
honest: Codex and Claude
stay `partial` on historical/tool completeness with permanent notes; Pi is fully `supported`
because its append-only entries are the complete session line.

### Conventions

Every `FeatureCapability` carries `runtime-fixture` evidence (observed versions, gate fixture
id, observation time); `unavailable` means the harness/binary is absent, `unverified` means the
contract probe ran and failed closed, with the exact probe-failure reason (never a
version-comparison reason).

### Invariants And Boundaries

- No `supported` without live production-path CONTRACT evidence; fixture or helper presence alone
  never enables a capability. No version-string comparison gates or demotes any capability.
- A failed probe demotes to `unverified` with the probe's typed reason, never `unavailable` and
  never a raw exception.
- The cache key is the executable fingerprint, so a reinstall or upgrade honestly re-gates by
  re-running the contract probe.

### Todos

None. (Before the R4 version-gate removal, Claude fell `unverified` whenever the installed runtime
drifted from the locked gate version; that version predicate is gone — Claude now gates on the live
helper contract probe, so an auto-updated runtime that answers `list` enables the surface.)

## Docs References

No Domain Documentation source is configured for this internal gate registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The gate suite now covers contract-probe pass/fail (a version drift still enables when the probe
passes), missing binaries, and helper preflight; the installed suite re-proves the same gates live;
the helper host reports the runtime/helper versions as informational evidence (no version compare).

| Finding | Anchor | Source |
| --- | --- | --- |
| A codex version drift still ENABLES the surface when the connect+list probe passes; a failed probe demotes to unverified. | "def test_version_drift_still_enables_codex_when_the_probe_passes(self) -> None:"; "def test_failed_probe_is_unverified_not_unavailable(self) -> None:" | mcp/tests/test_conversation_library_gates.py:100-100; mcp/tests/test_conversation_library_gates.py:119-119 |
| Helper success enables Pi fully; helper failure and missing locked dependencies demote to unverified. | "def test_helper_success_enables_pi_with_full_completeness(self) -> None:"; "def test_helper_failure_is_unverified(self) -> None:"; "def test_missing_helper_dependencies_are_unverified(self) -> None:" | mcp/tests/test_conversation_library_gates.py:165-165; mcp/tests/test_conversation_library_gates.py:184-184; mcp/tests/test_conversation_library_gates.py:201-201 |
| The helper host reports observed runtime/helper versions as informational evidence only; the operation result is the gate (no version comparison). | "def helper_preflight(" | mcp/src/agents_remember/serving/conversation/library/helper_host.py:74-74 |
| The installed-runtime suite re-proves the Codex and Pi gates on real harnesses (the exact-identity checks still skip on version drift — recorded conservatism). | "def test_live_gate_supports_list_read_and_partial_completeness(self) -> None:"; "def test_live_helper_gate_supports_pi_history(self) -> None:"; "def test_open_real_pi_session_proves_exact_identity(self) -> None:" | mcp/tests/test_conversation_library_installed.py:136-136; mcp/tests/test_conversation_library_installed.py:217-217; mcp/tests/test_conversation_library_installed.py:366-366 |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local gate registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L2 Current Delta

**`GateProbes`** (`codex_probe`, `which`, `environment`; module default `DEFAULT_GATE_PROBES`) is
now how the registry finds out what is actually installed, as one substitutable surface. A gate
answers "can this harness serve a library here?" only by probing the machine — the codex app-server
probe, PATH lookup and the process environment are the three ways it looks — and faking one while
leaving the others live probes two different machines. `None` on `codex_probe`/`which` keeps the
real probe. The gate verdicts themselves are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 4 citation rows with exact anchors and current source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `GateProbes` / `DEFAULT_GATE_PROBES` as the one substitutable installed-ness surface.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: version-gate REMOVAL (developer ruling
  2026-07-21, R4). Corrected the now-false "passes at the exact locked versions" gating doctrine:
  the real connect+list (codex) / helper `list` (claude/pi) CONTRACT probe is the only gate;
  `LOCKED_CODEX_RUNTIME_VERSION` is no longer compared (now a published reference/skip-guard
  constant); the observed version rides evidence as informational metadata; cleared the stale
  Claude version-drift Todo (Claude now gates on the live contract probe). Uncommitted; closeout
  re-stamps verification.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the live capability gate registry
  sidecar. Verification is blank until closeout commits and stamps the new source.
