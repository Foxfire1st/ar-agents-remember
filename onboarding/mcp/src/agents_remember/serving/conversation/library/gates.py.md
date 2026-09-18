# mcp/src/agents_remember/serving/conversation/library/gates.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/gates.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T18:50+02:00 |
| lastVerifiedCommitHash |  `5e4eb651be0691e2d2a90ea59bc662f92050db25`|
| lastVerifiedCommitDate |  2026-09-18T20:35:53+02:00|
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
| Codex history support follows the real connection/list probe; observed version is informational and a failed probe is unverified. | `_codex_gate` | mcp/src/agents_remember/serving/conversation/library/gates.py:265-292 |
| Helper preflight or native list failure is unverified; successful Pi helper proof supplies the supported history shape. | `_helper_gate` | mcp/src/agents_remember/serving/conversation/library/gates.py:294-332 |
| The set of harnesses the helper can serve is derived from the helper host's own entry table, so a gate and its helper cannot disagree about it. | `_HELPER_HARNESS_IDS` | mcp/src/agents_remember/serving/conversation/library/gates.py:58-58 |
| A normalized harness the helper has no implementation for is refused by name through the shared unavailable path, not by a helper lookup that would raise `KeyError`. | `_helper_harness`; `_unavailable_history` | mcp/src/agents_remember/serving/conversation/library/gates.py:61-68; mcp/src/agents_remember/serving/conversation/library/gates.py:78-78 |
| The helper host reports observed runtime/helper versions as informational evidence only; the operation result is the gate (no version comparison). | "def helper_preflight(" | mcp/src/agents_remember/serving/conversation/library/helper_host.py:74-74 |
| Historical evidence (retired with the d3610903 suite reduction): The installed-runtime suite re-historically exercised the Codex and Pi gates on real harnesses (the exact-identity checks still skip on version drift — recorded conservatism). These removed artifacts provide no current execution or capability-enablement proof. | N/A | N/A |

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

- 2026-09-18T18:50+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **wrote the one guard this card did not describe, and re-derived the two ranges this source's own growth moved.** The source gained `_HELPER_HARNESS_IDS`, derived from the helper host's `HELPER_ENTRY_BY_HARNESS`, and `_helper_harness`, which turns "the helper serves no such harness" into an `unavailable` refusal by name instead of a `KeyError` from the helper lookup; the new paragraph in the body states that, and two reference rows cite it. The same 16-line insertion shifted every construct below it, so the `_codex_gate` and `_helper_gate` rows — which named `:243-270` and `:272-310` — now name `:265-292` and `:294-332`; both were re-read at their new extents and the claims are unchanged. The `history_capabilities` dispatch itself (the `if harness_id == "codex"` branch and the guarded helper branch) was read and is what the paragraph describes. Verification stamp advanced to `c5a74a85`, the revision read; closeout re-stamps.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

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
