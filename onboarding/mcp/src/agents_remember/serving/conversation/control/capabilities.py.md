# mcp/src/agents_remember/serving/conversation/control/capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

The control routes' own exact-session capability gate (interrupt, typed attachments per kind,
policyRead, telemetry per metric). A feature is `supported` only with landed installed-runtime
fixture evidence captured through the production seam (the L2E `control-plane/*` rows); a native
shape whose contract has never been probed through a captured fixture is `unverified`; a contract
the harness cannot provide on this surface is `unavailable`.

THE CONTRACT IS THE ONLY GATE (developer ruling 2026-07-21, 260718-CHATS-L5F R4): no capability is
demoted by a version-string comparison against the observed runtime/helper. The prior read-time
observed-version demotion is REMOVED; the observed version rides the evidence record as
informational metadata only.

## Code Commentary

### Logic

Per-harness fixture ids and version pins are module constants (L37-L47): codex
`0.144.5`/`codex-0.144.5-installed-20260718`, claude `2.1.211` locked, pi `0.80.7`. `_fixture`
(L57), `_adapter` (L78), `_unavailable` (L87), and `_image_capability` (L91) build the typed
`FeatureCapability`/`AttachmentCapability` products; `_no_asset_kind` (L118) reports a kind the
harness cannot stage. `_codex_controls`/`_claude_controls`/`_pi_controls` (L132/L164/L192) and the
telemetry builders (L225/L252/L265) assemble the static per-harness control/telemetry capability
sets, keyed in `_CONTROLS` (L291) and `_TELEMETRY` (L297). `control_capabilities_for` (L304) and
`telemetry_capabilities_for` (L315) select by `HarnessId` and now DISCARD the snapshot
(`del snapshot`): the fixture-declared state stands on its own contract evidence and is never
demoted by a version comparison — the `_observed_version`/`_demote_attachments`/`for_observed_runtime`
demotion machinery is REMOVED. Claude's `_CLAUDE_MISMATCH` reason (L52-L55) is now the honest
never-probed contract note ("control contract not yet probed through a captured production fixture
… never a version gate"), not an installed-vs-locked version note. The attachment MIME allow-list
is `_ATTACHMENT_MIME_TYPES` (L57), sorted from the L2E `SUBMIT_ASSET_MIME_TYPES`.

### Conventions

Nothing enables a feature from documentation or changelog text; only fixture evidence captured
through the production seam does. This is a distinct authority from L1's `active/capabilities.py`
page-level view — that view stays conservative pre-L2E and its reasons name this leaf; the control
routes gate on this module (see the L4-facing note in the governing overview).

### Invariants And Boundaries

- `supported`/`partial` requires exact runtime-fixture evidence; an un-probed contract stays
  `unverified` and the metric/action stays off. NO version-string comparison demotes any feature —
  the observed version is informational evidence only.
- Feature limits (MIME allow-list, count, byte cap) are read from the L2E asset constants, never
  re-declared here.
- The capability set is the gate every control route consults before any native call; a refused
  capability fails typed (422) before dispatch.

### Todos

None.

## Docs References

No Domain Documentation source is configured; capability evidence is fixture/seam-bound.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The capability DTOs and the shared demotion rule live in the contract module; the fixture rows and
asset limits come from the L2E substrate; the L1 page-level view is the conservative sibling.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `ControlCapabilities`, `AttachmentCapabilities`, `TelemetryCapabilities` DTOs; `FeatureCapability` carries the documenting NOTE that there is deliberately no `for_observed_runtime` version-demotion. | L630-L678 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The L2E asset MIME/count/byte constants and `control-plane/*` fixture discipline. | L1-L60 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The L1 conservative page-level control/telemetry view (stale post-L2E; L4 gates on this module instead). | L152-L165 | [active/capabilities.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/capabilities.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260718-CHATS-L5I Current Delta

Control capabilities now expose fixture-backed native interrupt support for the installed Codex, Claude, and Pi contracts. The evidence is still scoped to interrupt: steer, follow-up, attachments, and policy capability decisions retain their own conservative gates.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: version-gate REMOVAL (developer ruling
  2026-07-21, R4). Corrected the now-false read-time observed-version demotion: `control_capabilities_for`
  and `telemetry_capabilities_for` discard the snapshot, the `_observed_version`/`_demote_attachments`/
  `for_observed_runtime` machinery is gone, and `_CLAUDE_MISMATCH` is now the honest never-probed
  contract reason (not an installed-vs-locked version note). Corrected the stale
  `for_observed_runtime` reference and refreshed line numbers. Uncommitted; closeout re-stamps.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the control-domain
  capability gate — per-harness fixture-bound interrupt/attachment/policyRead/telemetry states with
  observed-runtime demotion, distinct from the L1 page-level view. Verification is blank because the
  new source file is uncommitted; closeout owns its first source stamp.
