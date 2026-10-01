# mcp/src/agents_remember/serving/conversation/library/gates.py

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

The helper branch is guarded by the helper host's own entry table. `_HELPER_HARNESS_IDS` is derived
from `HELPER_ENTRY_BY_HARNESS`, so there is **one authority** for the set of harnesses the locked
helper can actually serve, and `_helper_harness` returns the helper host's own name for a harness id
or `None`. A normalized harness the helper has no implementation for is therefore refused **by name**
through `_unavailable_history` ("the conversation-library history gate has no `<id>` implementation")
rather than handed to `_helper_gate`, where the helper lookup would raise `KeyError` on an id it has
never heard of. The refusal is the same `unavailable` shape every other absent-capability path
returns, so a harness this build cannot serve reads as honestly unavailable, not as a crash.

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

## Evidence

### Docs References

No Domain Documentation source is configured for this internal gate registry.

No configured domain documentation was available.

### Repo-Internal References

The gate suite now covers contract-probe pass/fail (a version drift still enables when the probe
passes), missing binaries, and helper preflight; the installed suite re-proves the same gates live;
the helper host reports the runtime/helper versions as informational evidence (no version compare).

- Codex history support follows the real connection/list probe; observed version is informational and a failed probe is unverified. [1]
- Helper preflight or native list failure is unverified; successful Pi helper proof supplies the supported history shape. [2]
- The set of harnesses the helper can serve is derived from the helper host's own entry table, so a gate and its helper cannot disagree about it. [3]
- A normalized harness the helper has no implementation for is refused by name through the shared unavailable path, not by a helper lookup that would raise `KeyError`. [4]
- The helper host reports observed runtime/helper versions as informational evidence only; the operation result is the gate (no version comparison). [5]
Historical evidence (retired with the d3610903 suite reduction): The installed-runtime suite re-historically exercised the Codex and Pi gates on real harnesses (the exact-identity checks still skip on version drift — recorded conservatism). These removed artifacts provide no current execution or capability-enablement proof.

### Cross-Repo References

No meaningful cross-repo boundary exists for this local gate registry.

No meaningful cross-repo references found.

## 260731-EFA-L2 Current Delta

**`GateProbes`** (`codex_probe`, `which`, `environment`; module default `DEFAULT_GATE_PROBES`) is
now how the registry finds out what is actually installed, as one substitutable surface. A gate
answers "can this harness serve a library here?" only by probing the machine — the codex app-server
probe, PATH lookup and the process environment are the three ways it looks — and faking one while
leaving the others live probes two different machines. `None` on `codex_probe`/`which` keeps the
real probe. The gate verdicts themselves are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
