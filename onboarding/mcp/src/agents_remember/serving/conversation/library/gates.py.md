# mcp/src/agents_remember/serving/conversation/library/gates.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/gates.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate |  2026-07-21T11:31:07+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The gate suite now covers contract-probe pass/fail (a version drift still enables when the probe
passes), missing binaries, and helper preflight; the installed suite re-proves the same gates live;
the helper host reports the runtime/helper versions as informational evidence (no version compare).

| Finding | Citations | Source Path |
| --- | --- | --- |
| A codex version drift still ENABLES the surface when the connect+list probe passes; a failed probe demotes to unverified. | (test) | [test_conversation_library_gates.py](agents-remember/mcp/tests/test_conversation_library_gates.py) |
| Helper success enables Pi fully; helper failure and missing locked dependencies demote to unverified. | L158-L209 | [test_conversation_library_gates.py](agents-remember/mcp/tests/test_conversation_library_gates.py) |
| The helper host reports observed runtime/helper versions as informational evidence only; the operation result is the gate (no version comparison). | L145-L151 | [helper_host.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/helper_host.py) |
| The installed-runtime suite re-proves the Codex and Pi gates on real harnesses (the exact-identity checks still skip on version drift — recorded conservatism). | L134-L152; L215-L230 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local gate registry.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: version-gate REMOVAL (developer ruling
  2026-07-21, R4). Corrected the now-false "passes at the exact locked versions" gating doctrine:
  the real connect+list (codex) / helper `list` (claude/pi) CONTRACT probe is the only gate;
  `LOCKED_CODEX_RUNTIME_VERSION` is no longer compared (now a published reference/skip-guard
  constant); the observed version rides evidence as informational metadata; cleared the stale
  Claude version-drift Todo (Claude now gates on the live contract probe). Uncommitted; closeout
  re-stamps verification.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the live capability gate registry
  sidecar. Verification is blank until closeout commits and stamps the new source.
