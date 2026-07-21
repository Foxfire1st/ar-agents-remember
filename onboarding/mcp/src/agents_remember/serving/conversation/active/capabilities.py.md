# mcp/src/agents_remember/serving/conversation/active/capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate | 2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

Exact-session capability evidence for the active conversation surface: per-session
`ConversationCapabilities` built only from landed installed-runtime fixture evidence through the
production seam — a feature is `supported`/`partial` only with fixture evidence, a native shape
whose contract has never been probed through a captured fixture is `unverified`, and a contract
the harness cannot provide is `unavailable`.

THE CONTRACT IS THE ONLY GATE (developer ruling 2026-07-21, executed in 260718-CHATS-L5F R4):
no capability is gated, locked, or demoted by a version-string comparison. The observed
runtime/helper version rides the evidence record as informational metadata only; a capability
demotes solely when its contract fails verification or has never been probed — never because an
installed version drifts from a fixture's captured version. The prior observed-version read-time
demotion is REMOVED: harnesses auto-update, and a version predicate is exactly what made the
natively-succeeding claude surface unusable (the image3 "unverified: observed runtime/helper
version differs from capability evidence" banner).

## Code Commentary

### Logic

Three builders assemble the per-harness sets from the pinned fixture/runtime constants
(L30-L40): codex (L97-L189) reports live text `supported` (fixture-observed
userMessage/agentMessage through the production evidence seam), live completeness `partial`
(bounded evidence window; ephemeral threads have no native page), history read `partial`
(thread/read pages fixture-observed on persisted threads; ephemeral threads refuse typed), and
historical tool completeness honestly `partial` ("historical tool details are lossy") — the
documented codex history loss stays visible on the wire; claude (L197-L238) is uniformly
`unverified` with the honest NEVER-PROBED contract reason ("frame contract not yet probed
through a captured production fixture … never a version gate"), and history read `unavailable`
(claude has no native page — stream/replay-only); pi (L241-L331) reports live text `partial`
(messages mint from durable entries; in-flight deltas stay buffered until completion), history
read `supported` (get_entries durable pages fixture-observed), and history completeness `partial`
(branch/label/custom entries surface as unknown-vendor evidence). List/resume are `unavailable`
everywhere (the L2 library leaf owns them); attachment kinds are `unavailable` (the L3 control
leaf owns staging); telemetry/control rows stay `unverified` or `unavailable` with their
owning-leaf reasons. `capabilities_for` (L334-L347) now DISCARDS the snapshot (`del snapshot`):
the observed runtime version is no longer a gate, so each builder mints its honest fixture-declared
or never-probed state directly and nothing is demoted at read time by a version comparison. The
runtime constants (`_CODEX_RUNTIME`/`_CLAUDE_RUNTIME`/`_PI_RUNTIME`, L39-L43) survive only as
informational metadata on the `CapabilityEvidence` records.

### Conventions

Capabilities are per-session evidence, never a global harness marketing table: no feature is
enabled by documentation or changelog text, and fixture presence alone never enables anything —
only fixture-observed shapes through the production seam count.

### Invariants And Boundaries

- Every `supported`/`partial` claim names its fixture evidence (runtime version, fixture id,
  observed-at); `unverified` claims name the un-probed contract (never a version).
- NO version-string comparison gates or demotes any capability. A capability demotes solely when
  its contract fails verification or was never probed; the observed runtime version is
  informational evidence only. `capabilities_for` deliberately ignores the snapshot version.
- Cross-leaf features stay `unavailable` with the owning leaf named — no active-route feature
  claims library (L2) or control (L3) surface.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. The capability evidence rows are
the repository-owned installed-runtime fixtures cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this evidence module. | — | — |

## Repo-Internal References

The capability wire models define states/tiers and the demotion rule; the three runtime fixtures
record the observed evidence rows these builders draw on; the service embeds the result in every
page.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `FeatureCapability` deliberately carries NO `for_observed_runtime` version-demotion (documenting NOTE); the contract is the only gate. | L653-L658 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| `ConversationCapabilities` fixes the live/history/controls/telemetry group shape. | L733-L738 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The contract-only gate is pinned: `FeatureCapability` has no `for_observed_runtime` predicate. | (test) | [test_conversation_contracts.py](agents-remember/mcp/tests/test_conversation_contracts.py) |
| The runtime fixtures record the observed (never enabling) evidence rows per harness. | L34-L58 | [codex-0.144.5.json](agents-remember/mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json) |
| The service assembles capabilities into every atomic page response. | L212-L227 | [service.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/service.py) |

## Cross-Repo References

No cross-repository implementation participates in this evidence module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: version-gate REMOVAL (developer ruling
  2026-07-21, R4). Corrected the now-false read-time version-demotion doctrine: `capabilities_for`
  discards the snapshot, no version-string comparison gates/demotes any feature, and claude's
  reasons are the honest never-probed contract language (not the installed-vs-locked mismatch).
  Fixed the stale `FeatureCapability.for_observed_runtime` citation (method removed; only a
  documenting NOTE remains) and refreshed the codex/claude/pi builder line numbers. Uncommitted;
  closeout re-stamps verification.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for exact-session
  capability evidence — fixture-gated per-harness states, visible codex tool loss, claude
  version-gate honesty, read-time version demotion. Verification is blank because the new
  source file is uncommitted; closeout owns its first source stamp.
