# mcp/src/agents_remember/serving/conversation/active/capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

Exact-session capability evidence for the active conversation surface: per-session
`ConversationCapabilities` built only from landed installed-runtime fixture evidence through the
production seam — a feature is `supported`/`partial` only with fixture evidence, a native shape
whose contract has never been probed through a captured fixture is `unverified`, and a contract
the harness cannot provide is `unavailable` cit:([`_CODEX_FIXTURE`, `_CODEX_RUNTIME`, `_codex_capabilities`, `_claude_capabilities`, `_pi_capabilities`, `capabilities_for`], mcp/src/agents_remember/serving/conversation/active/capabilities.py:43-43; mcp/src/agents_remember/serving/conversation/active/capabilities.py:47-47; mcp/src/agents_remember/serving/conversation/active/capabilities.py:112-200; mcp/src/agents_remember/serving/conversation/active/capabilities.py:203-248; mcp/src/agents_remember/serving/conversation/active/capabilities.py:251-339; mcp/src/agents_remember/serving/conversation/active/capabilities.py:342-357) cit:([`interrupt_capability_for`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:331-339).

THE CONTRACT IS THE ONLY GATE (developer ruling 2026-07-21, executed in R4):
no capability is gated, locked, or demoted by a version-string comparison. The observed
runtime/helper version rides the evidence record as informational metadata only; a capability
demotes solely when its contract fails verification or has never been probed — never because an
installed version drifts from a fixture's captured version. The prior observed-version read-time
demotion is REMOVED: harnesses auto-update, and a version predicate is exactly what made the
natively-succeeding claude surface unusable (the image3 "unverified: observed runtime/helper
version differs from capability evidence" banner) cit:([`capabilities_for`], mcp/src/agents_remember/serving/conversation/active/capabilities.py:342-357).

## Code Commentary

### Conventions

Capabilities are per-session evidence, never a global harness marketing table: no feature is
enabled by documentation or changelog text, and fixture presence alone never enables anything —
only fixture-observed shapes through the production seam count cit:([`_codex_capabilities`, `_claude_capabilities`, `_pi_capabilities`, `capabilities_for`], mcp/src/agents_remember/serving/conversation/active/capabilities.py:112-200; mcp/src/agents_remember/serving/conversation/active/capabilities.py:203-248; mcp/src/agents_remember/serving/conversation/active/capabilities.py:251-339; mcp/src/agents_remember/serving/conversation/active/capabilities.py:342-357).

### Invariants And Boundaries

- Every `supported`/`partial` claim names its fixture evidence (runtime version, fixture id,
  observed-at); `unverified` claims name the un-probed contract (never a version).
- NO version-string comparison gates or demotes any capability. A capability demotes solely when
  its contract fails verification or was never probed; the observed runtime version is
  informational evidence only. `capabilities_for` deliberately ignores the snapshot version.
- Cross-leaf features stay `unavailable` with the owning leaf named — no active-route feature
  claims library or control surface.

### Todos

None.

## Update History
- 2026-08-04T13:47:55+02:00 — 260731-EFA-L6 S18-B11 same-reviewer correction: bound the all-harness capability rule to every builder, the selector, and the interrupt bridge. Verification metadata unchanged.

- 2026-07-31T16:35+02:00 — No content impact: the whole-tree `ruff format` pass changed only
  formatting in this module; the prior capability references were revalidated against the linked
  source cards after the service and model edits.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-24T13:18:47Z — Prior curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-21T11:30+02:00 — Prior curator: corrected the now-false read-time version-demotion doctrine,
  refreshed the per-harness evidence, and left the first verification stamp for closeout.
- 2026-07-19T17:35+02:00 — Prior curator: created the sidecar for exact-session capability evidence.
