# mcp/src/agents_remember/serving/conversation/control/capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:26+02:00 |
| lastVerifiedCommitHash |  `c1dbebf883f22710b71d40a66ec92c1ac134918f`|
| lastVerifiedCommitDate |  2026-09-16T13:48:06+02:00|
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

Per-harness fixture ids and version pins are module constants: codex
`0.144.5`/`codex-0.144.5-installed-20260718`, claude `2.1.211` plus the separate interrupt pin
`2.1.217`/`claude-2.1.217-installed-20260722`, pi `0.80.7`, and — since the eve
product-integration change set — eve `0.56.0`/`eve-0.56.0-native-20260916` with its own
`_EVE_OBSERVED_AT`. `_fixture`, `_fixture_evidence`, `_adapter`, `_unavailable` and
`_image_capability` build the typed `FeatureCapability`/`AttachmentCapability` products;
`_no_asset_kind` reports a kind the harness cannot stage. `_codex_controls`, `_claude_controls`,
`_pi_controls` and `_eve_controls`, plus the telemetry builders `_codex_telemetry`,
`_claude_telemetry`, `_pi_telemetry` and `_eve_telemetry`, assemble the static per-harness
control/telemetry capability sets, keyed in `_CONTROLS` and `_TELEMETRY`.
`control_capabilities_for` and `telemetry_capabilities_for` select by `HarnessId` and **discard** the
snapshot (`del snapshot`): the fixture-declared state stands on its own contract evidence and is never
demoted by a version comparison — the `_observed_version`/`_demote_attachments`/`for_observed_runtime`
demotion machinery is REMOVED. Claude's `_CLAUDE_MISMATCH` reason is the honest never-probed contract
note ("control contract not yet probed through a captured production fixture … never a version gate"),
not an installed-vs-locked version note. The attachment MIME allow-list is `_ATTACHMENT_MIME_TYPES`,
sorted from the L2E `SUBMIT_ASSET_MIME_TYPES`.

**`_eve_controls` is the newest set, and its conservatism is the point.** `interrupt` is the one
`supported` control, and its evidence is the pinned runtime's own recorded cancel scenario — a
`turn.cancelled` settlement for the exact observed turn — rather than a documentation claim.
`policy_read` is `supported` on the recorded `authorization.required` challenge becoming a pending
interaction. Everything else is `unavailable` rather than `unverified`, because the adapter does not
implement the corresponding surface at all: the submission authority refuses an asset-carrying prompt
for an adapter without `submit_with_assets`, so advertising a supported image/file/resource kind here
would offer a composer control that can only ever be refused. `_eve_telemetry` declares every metric
absent with a reason naming the stream, rather than borrowing another harness's rows.

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
- **An asset kind is advertised only when the adapter can stage it.** eve declares
  image/file/resource `unavailable` because its adapter has no `submit_with_assets`; a `supported` row
  here would offer a control the submission authority independently refuses.
- **No harness borrows another's telemetry.** Each telemetry builder is its own; eve's declares every
  metric absent with a reason naming the stream.

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
| `ControlCapabilities`, `AttachmentCapabilities`, "class TelemetryCapabilities(WireModel):" DTOs; `FeatureCapability` carries the documenting NOTE that there is deliberately no `for_observed_runtime` version-demotion. | "class FeatureCapability(WireModel):", "class AttachmentCapabilities(WireModel):", "class ControlCapabilities(WireModel):", `TelemetryCapabilities` | mcp/src/agents_remember/models/conversations/capabilities.py:18-18; mcp/src/agents_remember/models/conversations/capabilities.py:80-80; mcp/src/agents_remember/models/conversations/capabilities.py:86-86; mcp/src/agents_remember/models/conversations/capabilities.py:94-99 |
| The L2E asset MIME/count/byte constants used by this gate. | `MAX_SUBMIT_ASSETS`, `MAX_SUBMIT_ASSET_BYTES`, `SUBMIT_ASSET_MIME_TYPES` | mcp/src/agents_remember/models/conversations/control_wire.py:43-43; mcp/src/agents_remember/models/conversations/control_wire.py:47-47; mcp/src/agents_remember/models/conversations/control_wire.py:51-51 |
| The L1 conservative page-level control/telemetry view (stale post-L2E; L4 gates on this module instead). | `capabilities_for` | mcp/src/agents_remember/serving/conversation/active/capabilities.py:440-457 |
| eve's control set: exact-turn interrupt and policyRead supported on recorded native evidence, every other control `unavailable` because the adapter does not implement the surface. | `_eve_controls`; `_no_asset_kind` | mcp/src/agents_remember/serving/conversation/control/capabilities.py:136-147; mcp/src/agents_remember/serving/conversation/control/capabilities.py:310-342 |
| eve's telemetry declaration: every metric absent with a reason naming the stream, never borrowed. | `_eve_telemetry` | mcp/src/agents_remember/serving/conversation/control/capabilities.py:345-359 |
| eve's own fixture id, runtime pin and observation time, distinct from the other three harnesses'. | `_EVE_FIXTURE`; `_EVE_RUNTIME`; `_EVE_OBSERVED_AT` | mcp/src/agents_remember/serving/conversation/control/capabilities.py:47-47; mcp/src/agents_remember/serving/conversation/control/capabilities.py:55-55; mcp/src/agents_remember/serving/conversation/control/capabilities.py:59-59 |
| The adapter capability that decides the asset rows: no `submit_with_assets`, so no supported kind. | `EveSessionAdapter` | mcp/src/agents_remember/serving/eve_adapter.py:144-865 |
| The cases: the asset-carrying submission is refused by the authority, and eve's telemetry is declared absent rather than borrowed. | `test_an_asset_carrying_submission_is_refused_by_the_authority`; `test_the_eve_adapter_is_not_asset_submit_capable`; `test_eve_telemetry_is_declared_absent_not_borrowed` | mcp/tests/test_eve_product_integration.py:1098-1103; mcp/tests/test_eve_product_integration.py:1706-1709; mcp/tests/test_eve_product_integration.py:1711-1745 |

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
- 2026-09-16T11:42:32+00:00: Generated citation repair: `EveSessionAdapter` repointed to mcp/src/agents_remember/serving/eve_adapter.py:144-865. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: added eve's control and telemetry sets —
  `_eve_controls` (exact-turn interrupt and `policyRead` `supported` on the pinned runtime's recorded
  native evidence; every other control `unavailable` because the adapter implements no such surface,
  and image/file/resource `unavailable` because the submission authority refuses an asset-carrying
  prompt for an adapter without `submit_with_assets`) and `_eve_telemetry` (every metric absent with a
  reason naming the stream, never borrowed from another harness), with eve's own fixture id, runtime
  pin and observation time. Body updated on Logic and Invariants; five reference rows added; the nine
  inline `cit:(…)` prose citations in the Logic section were converted to prose plus audit rows in the
  required `Finding | Anchor | Source` shape. Verification metadata moves to the leaf's synced base
  `ff97072c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code
  commit and no hash or fingerprint was invented here.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

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
