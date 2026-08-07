# mcp/src/agents_remember/serving/conversation/control/capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `b252c42cca200933d5c9c36e26de47a526a569ce`|
| lastVerifiedCommitDate |  2026-08-07T23:58:52+02:00|
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

Per-harness fixture ids and version pins are module constants,
cit:([`_CODEX_FIXTURE`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:41-41): codex
`0.144.5`/`codex-0.144.5-installed-20260718`, claude `2.1.211` plus the separate interrupt pin
`2.1.217`/`claude-2.1.217-installed-20260722`, pi `0.80.7`. `_fixture`,
cit:([`_fixture`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:64-71), cit:([`_adapter`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:91-97), cit:([`_unavailable`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:100-101), and cit:([`_image_capability`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:104-128)
build the typed `FeatureCapability`/`AttachmentCapability` products; cit:([`_no_asset_kind`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:131-142)
reports a kind the harness cannot stage. `_codex_controls`, cit:([`_codex_controls`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:145-173), `_claude_controls`, cit:([`_claude_controls`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:176-209), and `_pi_controls`, cit:([`_pi_controls`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:212-237), plus the telemetry builders `_codex_telemetry`, cit:([`_codex_telemetry`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:240-263), `_claude_telemetry`, cit:([`_claude_telemetry`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:266-276), and `_pi_telemetry`, cit:([`_pi_telemetry`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:279-302), assemble the static per-harness
control/telemetry capability sets, keyed in cit:([`_CONTROLS`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:305-309) and cit:([`_TELEMETRY`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:311-315).
cit:([`control_capabilities_for`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:318-328) and
cit:([`telemetry_capabilities_for`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:342-352) select by `HarnessId` and now DISCARD the snapshot
(`del snapshot`): the fixture-declared state stands on its own contract evidence and is never
demoted by a version comparison — the `_observed_version`/`_demote_attachments`/`for_observed_runtime`
demotion machinery is REMOVED. Claude's `_CLAUDE_MISMATCH` reason,
cit:([`_CLAUDE_MISMATCH`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:56-59), is now the honest
never-probed contract note ("control contract not yet probed through a captured production fixture
… never a version gate"), not an installed-vs-locked version note. The attachment MIME allow-list
is cit:([`_ATTACHMENT_MIME_TYPES`], mcp/src/agents_remember/serving/conversation/control/capabilities.py:61-61), sorted from the L2E `SUBMIT_ASSET_MIME_TYPES`.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The capability DTOs and the shared demotion rule live in the contract module; the fixture rows and
asset limits come from the L2E substrate; the L1 page-level view is the conservative sibling.

| Finding | Anchor | Source |
| --- | --- | --- |
| `ControlCapabilities`, `AttachmentCapabilities`, "class TelemetryCapabilities(WireModel):" DTOs; `FeatureCapability` carries the documenting NOTE that there is deliberately no `for_observed_runtime` version-demotion. | "class FeatureCapability(WireModel):", "class AttachmentCapabilities(WireModel):", "class ControlCapabilities(WireModel):", `TelemetryCapabilities` | mcp/src/agents_remember/serving/conversation/_models_status.py:339-339; mcp/src/agents_remember/serving/conversation/_models_status.py:325-325; mcp/src/agents_remember/serving/conversation/_models_status.py:331-331; mcp/src/agents_remember/serving/conversation/_models_status.py:262-262 |
| The L2E asset MIME/count/byte constants used by this gate. | `MAX_SUBMIT_ASSETS`, `MAX_SUBMIT_ASSET_BYTES`, `SUBMIT_ASSET_MIME_TYPES` | mcp/src/agents_remember/serving/harness_control_models.py:116-116; mcp/src/agents_remember/serving/harness_control_models.py:119-119; mcp/src/agents_remember/serving/harness_control_models.py:122-122 |
| The L1 conservative page-level control/telemetry view (stale post-L2E; L4 gates on this module instead). | `capabilities_for` | mcp/src/agents_remember/serving/conversation/active/capabilities.py:342-357 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
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

- 2026-08-03T02:32:19+02:00 — Curator W3-B02 converted 3 legacy prose line citations and repaired 3 Repo-Internal rows, resolving 9 manifest findings with exact capability, fixture, and active-view anchors; verification metadata was preserved.
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
