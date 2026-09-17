# harness_capability_catalog.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_capability_catalog.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:43+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634`|
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l17-ar` uncommitted source; base `0346da9c572e1eb913a8eb4130e9a9e9d37343c8` |
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns token-free, pre-session capability discovery for AR's built-in native harness adapters and
exposes it through a bounded, install-aware cache. It is the daemon-side catalog authority for
dynamic model and model-gated effort data; it does not contain a fallback enum or start a model turn.

**The install gate is a readiness question, not a `which` question.** `_installed_harness` used to ask
`shutil.which(harness.command)` directly, so a harness whose runtime is an application the session
adapter starts itself answered `404 harness not installed` here even with its runtime present. It now
consumes `harness_runtime_verdict`, so the registry's own readiness answer decides, and a not-ready
harness refuses with the **probe's sentence** — naming the component that is actually missing — instead
of a generic not-installed message.

## Code Commentary

### Logic

`HarnessCapabilityCatalog.get` first resolves the requested registry entry, asks readiness, rejects
unknown, non-native, and not-ready harnesses, and fingerprints the install identity. A matching
non-refresh request is a cache hit. Misses and explicit refreshes pass the current process environment
into a transient own-adapter `discover()` call, with Codex argv normalized to `app-server` by the
shared runner helper.

The install gate has two branches, and which one runs is decided by `harness.runtime_probe`:

- **A PATH harness** resolves its command and fingerprints the harness id, effective argv, canonical
  executable and executable stat identity, as before.
- **A runtime-probed harness** has no command to fingerprint. `_probed_install` takes the locations the
  probe already resolved — both halves of readiness — and uses the **interpreter** as the install
  identity, because a changed interpreter is a different install exactly as a replaced binary is for a
  PATH harness. `_runtime_fingerprint` hashes the harness id, the probe name, the interpreter path and
  its `stat` identity (device, inode, mode, size, mtime in ns), with `stat: null` when the interpreter
  is not on disk. That last case is deliberate and stated in the code: an interpreter the operator
  **declared** but which is absent still identifies the install, because readiness accepted the
  declaration and the spawn is where a bad path fails naming itself — refusing to fingerprint here
  would turn that into a generic lookup error one layer too early.

One lock per built-in harness provides single-flight discovery. The cache holds at most one
successful snapshot per harness. An explicit refresh is also the auth/account invalidation boundary:
if it fails, the exact entry that refresh evaluated is removed. A later concurrent success is not
removed, and the next ordinary request must rediscover rather than report stale data as a hit.

`CapabilityCatalogResult.to_json` wraps the unchanged normalized snapshot in the stable
`ar-harness-capabilities/v1` daemon envelope with cache status and install fingerprint.

### Conventions

Cache status is `hit`, `miss`, or `refreshed`. Installation changes invalidate mechanically through
the fingerprint; auth/account changes are caller-triggered with explicit refresh. Vendor catalog
shapes are normalized by the adapter before this module sees them.

### Invariants And Boundaries

- Discovery calls only the built-in own-adapter port and is token-free; no prompt or model turn is
  submitted.
- No hardcoded model or effort catalog is used on the default path.
- Effort remains nested under each model in the returned `CapabilitySnapshot`, and a snapshot may
  legitimately advertise **no** effort options (`supports_effort=False`, `effort_options=()`) — the
  catalog publishes what the adapter's own snapshot declares and never fills an axis in itself. Which
  way eve's snapshot falls is decided **in the adapter, by whether its runtime consumes the axis**, not
  here: at this leaf's candidate the pinned application reads `AR_EVE_EFFORT` through
  `defineAgent({ reasoning })`, so `serving/eve_adapter.py` publishes the axis and this module carries
  it; the axis was withheld before that consumer existed and is withheld again if it is removed.
  Either way this catalog adds no option of its own — a published axis is always one the adapter's
  snapshot named a runtime consumer for.
- **Never ask `which` for a probe-declaring harness.** The install gate must go through
  `harness_runtime_verdict`; a direct `resolver(harness.command)` reintroduces the defect where a
  present runtime is reported as not installed.
- A failed explicit refresh cannot reopen the prior entry as an ordinary healthy hit.
- The cache and lock sets are bounded by AR's built-in native harness ids.
- This module does not own HTTP routing, live-session mutation, settings authoring, ACP transport,
  Toad hosting, or frontend state.

### Todos

None known for the pre-session catalog boundary.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The normalized type layer owns the public capability shape, while the factory and runner helpers
provide the same native adapter construction and argv normalization used by hosted sessions.

| Finding | Anchor | Source |
| --- | --- | --- |
| The capability snapshot serializer retains model-local effort and the ACP Sense-1 projection. | `model_capability_json`; "Project the catalog into category-keyed options without duplicating state." | mcp/src/agents_remember/serving/harness_capabilities.py:85-85; mcp/src/agents_remember/serving/harness_capabilities.py:171-184 |
| The adapter port limits normalized native discovery to the built-in protocol harness set. | `HarnessCapabilityDiscoverer`; `BUILTIN_PROTOCOL_HARNESSES` | mcp/src/agents_remember/serving/harness_control_adapter.py:64-67; mcp/src/agents_remember/serving/harness_control_adapter.py:138-138 |
| The shared runner helper converts Codex registry argv to the native app-server boundary without dropping supplied arguments. | `adapter_argv`; "app-server" | mcp/src/agents_remember/serving/harness_control_runner.py:402-410 |
| The readiness verdict the install gate now consumes, so a probe-declaring harness is gated on its runtime rather than on `PATH`. | `harness_runtime_verdict`; `harness_availability_detail` | mcp/src/agents_remember/kernel/harnesses.py:82-103; mcp/src/agents_remember/kernel/harnesses.py:106-139 |
| The probed-install identity: the interpreter is the fingerprint for a harness with no command, and a declared-but-absent interpreter still identifies the install. | `_probed_install`; `_runtime_fingerprint`; `_InstalledHarness` | mcp/src/agents_remember/serving/harness_capability_catalog.py:77-81; mcp/src/agents_remember/serving/harness_capability_catalog.py:215-224; mcp/src/agents_remember/serving/harness_capability_catalog.py:227-256 |
| The adapter-side snapshot the catalog normalizes, whose effort axis is published at this candidate because the runtime consumes it. | `_capability_snapshot` | mcp/src/agents_remember/serving/eve_adapter.py:699-748 |
| The cases: discovery through the existing factory, the not-ready refusal before discovery, the probed-interpreter fingerprint, and the unknown-harness refusal. | `EveCapabilityDiscoveryTests` | mcp/tests/test_eve_product_integration.py:1018-1131 |


## Cross-Repo References

No external repository or ACP transport is used by this catalog.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `adapter_argv`; "app-server" repointed to mcp/src/agents_remember/serving/harness_control_runner.py:402-410; mcp/src/agents_remember/serving/harness_control_runner.py:410-410. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `EveCapabilityDiscoveryTests` repointed to mcp/tests/test_eve_product_integration.py:1018-1131. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T10:32+02:00 — 260915-CAPS-L17 curator: corrected one invariant that this leaf's candidate
  falsifies. The card said a snapshot advertising no effort options is "what eve's pinned runtime
  requires because it reads no effort value"; the candidate's pinned application **does** read
  `AR_EVE_EFFORT` (through `defineAgent({ reasoning })`), so eve's snapshot now publishes the axis and
  this catalog carries it. The invariant is restated as the rule that survives either direction: this
  module never fills an axis in — it publishes what the adapter's snapshot declares, and which way
  eve's snapshot falls is decided in the adapter by whether its runtime consumes the axis. The
  reference row naming the adapter snapshot was re-anchored from the pre-candidate `688-718` to the
  candidate's `699-748`. No other claim in this card was in question: nothing in
  `harness_capability_catalog.py` changed in this leaf. **Checker result (post-sync,
  verbatim).** The refusal this entry first recorded was resolved by the leaf's `worktree_sync`:
  the pair is now `leaf-candidate` / `acceptanceEligible:true` on code base `d8ed8c21`, and the
  contract-scoped `memory_quality_check` ran against this worktree. Headline: `ok:false`,
  `checklistStatus:"action-required"`,
  `coherenceStatus:"not-evaluated-quality-action-required"`, `closeoutReady:false`,
  `curatorActionableCount:1690`; census `ready-for-adjudication` (13 rows, 0 blockers, 0
  unonboarded). This card's own contribution: one `integrity.onboarding_drift_check.summary`
  finding — `onboarding_drift_drifted`, "Source has local staged changes not represented in
  HEAD", which is the expected shape for documenting a staged, uncommitted candidate rather than
  a claim about the wording. Verification metadata moves to the synced base `d8ed8c21`; the
  candidate is deliberately uncommitted, so the governed closeout stamps the real code commit
  and no hash or fingerprint was invented here.

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: **the install gate is a readiness question, not a
  `which` question.** `_installed_harness` no longer asks `shutil.which(harness.command)` directly: it
  consumes `harness_runtime_verdict`, so a harness whose runtime is an application the session adapter
  starts itself is gated on its runtime instead of answering `404 harness not installed` while the
  runtime is present, and a not-ready harness refuses with the probe's own sentence naming the missing
  component. Added `_probed_install`/`_runtime_fingerprint`: with no command to fingerprint, the probed
  **interpreter** is the install identity, and a declared-but-absent interpreter still identifies the
  install because the spawn is where a bad path fails naming itself. Recorded that the catalog may
  legitimately publish no effort options, since it reports what the adapter's snapshot declares.
  Verification metadata moves to the leaf's synced base `ff97072c`; the candidate is deliberately
  uncommitted, so the governed closeout stamps the real code commit and no hash or fingerprint was
  invented here.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:08:11+02:00 — W3-B04 curator: curated 4 table citations (4 total), supplying exact anchors and paths; the scoped fixer generated all final extents.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: created the pre-session catalog sidecar for
  dynamic own-adapter discovery, bounded install-aware single flight, explicit auth refresh, and
  exact-entry quarantine after failed refresh. Verification remains empty until closeout stamps the
  new source file.
