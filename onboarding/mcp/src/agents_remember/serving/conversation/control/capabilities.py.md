# mcp/src/agents_remember/serving/conversation/control/capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
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

Per-harness fixture ids and version pins are module constants (L41-L54): codex
`0.144.5`/`codex-0.144.5-installed-20260718`, claude `2.1.211` plus the separate interrupt pin
`2.1.217`/`claude-2.1.217-installed-20260722`, pi `0.80.7`. `_fixture`
(L64-L71), `_adapter` (L91-L97), `_unavailable` (L100-L101), and `_image_capability` (L104-L128)
build the typed `FeatureCapability`/`AttachmentCapability` products; `_no_asset_kind` (L131-L142)
reports a kind the harness cannot stage. `_codex_controls`/`_claude_controls`/`_pi_controls`
(L145/L176/L212) and the telemetry builders (L240/L266/L279) assemble the static per-harness
control/telemetry capability sets, keyed in `_CONTROLS` (L305-L309) and `_TELEMETRY` (L311-L315).
`control_capabilities_for` (L318-L328) and
`telemetry_capabilities_for` (L342-L352) select by `HarnessId` and now DISCARD the snapshot
(`del snapshot`): the fixture-declared state stands on its own contract evidence and is never
demoted by a version comparison — the `_observed_version`/`_demote_attachments`/`for_observed_runtime`
demotion machinery is REMOVED. Claude's `_CLAUDE_MISMATCH` reason (L56-L59) is now the honest
never-probed contract note ("control contract not yet probed through a captured production fixture
… never a version gate"), not an installed-vs-locked version note. The attachment MIME allow-list
is `_ATTACHMENT_MIME_TYPES` (L61), sorted from the L2E `SUBMIT_ASSET_MIME_TYPES`.

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
| `ControlCapabilities`, `AttachmentCapabilities`, `TelemetryCapabilities` DTOs; `FeatureCapability` carries the documenting NOTE that there is deliberately no `for_observed_runtime` version-demotion. | L620-L668 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The L2E asset MIME/count/byte constants and `control-plane/*` fixture discipline. | L1-L60 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The L1 conservative page-level control/telemetry view (stale post-L2E; L4 gates on this module instead). | L154-L167 | [active/capabilities.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/capabilities.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260718-CHATS-L5I Current Delta

Control capabilities now expose fixture-backed native interrupt support for the installed Codex, Claude, and Pi contracts. The evidence is still scoped to interrupt: steer, follow-up, attachments, and policy capability decisions retain their own conservative gates.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L2 Current Delta

The fixture-backed capability builders were split: `_fixture_evidence(runtime_version,
helper_version, fixture_id, observed_at)` now returns the `CapabilityEvidence` — *the captured-fixture
provenance one advertised capability rests on* — and the capability builder takes that evidence
value. Each declared capability names its runtime/fixture pair once. The advertised states,
reasons and `evidence_tier="runtime-fixture"` are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived every stale self-citation in the Logic
  paragraph after the `_fixture_evidence` split and the claude-interrupt pins shifted the module down
  (~+7 lines early, ~+13-24 lines late). Ten flagged (`_adapter` L84→L91-L97, `_unavailable`
  L87→L100-L101, `_image_capability` L96→L104-L128, `_no_asset_kind` L118→L131-L142, `_CONTROLS`
  L291→L305-L309, `_TELEMETRY` L297→L311-L315, `control_capabilities_for` L307→L318-L328,
  `telemetry_capabilities_for` L318→L342-L352, `_CLAUDE_MISMATCH` L52-L55→L56-L59,
  `_ATTACHMENT_MIME_TYPES` L57→L61) plus the same-sentence neighbours that had drifted with them
  (constants L37-L47→L41-L54, `_fixture` L57→L64-L71, the control builders L132/L164/L192→L145/L176/L212
  and the telemetry builders L225/L255/L268→L240/L266/L279). Also recorded the separate claude
  interrupt pin (`2.1.217`/`claude-2.1.217-installed-20260722`). All described behavior verified
  unchanged, including that the `_observed_version`/`_demote_attachments`/`for_observed_runtime`
  machinery is still absent from the source.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `_fixture_evidence` split; advertised capability states and evidence tier unchanged.
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
