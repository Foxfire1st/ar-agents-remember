# mcp/src/agents_remember/serving/conversation/control/capabilities.py

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

## Evidence

### Docs References

No Domain Documentation source is configured; capability evidence is fixture/seam-bound.

No configured domain documentation was available.

### Repo-Internal References

The capability DTOs and the shared demotion rule live in the contract module; the fixture rows and
asset limits come from the L2E substrate; the L1 page-level view is the conservative sibling.

- `ControlCapabilities`, `AttachmentCapabilities`, "class TelemetryCapabilities(WireModel):" DTOs; `FeatureCapability` carries the documenting NOTE that there is deliberately no `for_observed_runtime` version-demotion. [1]
- The L2E asset MIME/count/byte constants used by this gate. [2]
- The L1 conservative page-level control/telemetry view (stale post-L2E; L4 gates on this module instead). [3]
- eve's control set: exact-turn interrupt and policyRead supported on recorded native evidence, every other control `unavailable` because the adapter does not implement the surface. [4]
- eve's telemetry declaration: every metric absent with a reason naming the stream, never borrowed. [5]
- eve's own fixture id, runtime pin and observation time, distinct from the other three harnesses'. [6]
- The adapter capability that decides the asset rows: no `submit_with_assets`, so no supported kind. [7]
- The cases: the asset-carrying submission is refused by the authority, and eve's telemetry is declared absent rather than borrowed. [8]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.

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
