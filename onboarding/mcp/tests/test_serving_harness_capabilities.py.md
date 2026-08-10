# mcp/tests/test_serving_harness_capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_serving_harness_capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T06:15+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Regression authority for the daemon's token-free, install-aware native harness capability cache and
its frozen `ar-harness-capabilities/v1` envelope.

## Code Commentary

### Logic

A fake discoverer records the exact `LaunchSpec` and current environment used for enumeration. The
ordinary hit case proves one discover call, resolved executable argv, current auth/account
environment, model-local effort nesting, and category-keyed `configOptions`. Explicit refresh
re-enumerates and replaces the single retained entry; an executable stat change creates a miss and
new fingerprint without growing the cache.

The failed-refresh cases pin the auth invalidation boundary. A failed explicit refresh quarantines
the exact prior entry, so the next ordinary read must rediscover before it can become a hit. A
concurrent later success is not erased by the older failed refresh. Two ordinary requests for the
same install fingerprint share one in-flight discovery and return miss/hit around one adapter call.

### Conventions

`unittest.IsolatedAsyncioTestCase` runs against a temporary executable whose content and stat
identity can change deterministically. `_Factory` supplies queued snapshots/errors and records
launches and environments; no vendor process, prompt, thread, or model turn is started.

### Invariants And Boundaries

- Discovery uses only the native adapter's token-free `discover()` port and the current process
  environment; no hardcoded fallback catalog is tested or allowed.
- Effort remains nested under each model and the ACP Sense 1 projection remains category-keyed.
- The cache retains at most one successful entry per harness id and automatically misses when the
  installed executable fingerprint changes.
- Explicit refresh is the auth/account invalidation boundary: failure cannot expose the prior entry
  as a healthy hit, but it also cannot delete a later concurrent success.
- Same-fingerprint ordinary requests share one in-flight enumeration.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

The test source directly proves cache behavior and envelope shape; the catalog implementation owns
fingerprinting, quarantine, bounded retention, and native discovery composition.

| Finding | Anchor | Source |
| --- | --- | --- |
| The cache test proves the first lookup is a miss, the second is a hit, and the hit does not launch a second discovery; normalized JSON preserves model-gated effort and category-keyed config options. | "test_cache_hit_is_discover_only_and_preserves_model_gating" | mcp/tests/test_serving_harness_capabilities.py:90-107 |
| Focused tests prove explicit refresh re-enumerates and replaces the bounded entry, while executable change yields a miss with a new fingerprint and still one retained entry. | "test_refresh_reenumerates_and_replaces_the_bounded_entry"; "test_executable_change_invalidates_without_growing_the_cache" | mcp/tests/test_serving_harness_capabilities.py:109-133 |
| Failed explicit refresh quarantines stale data until ordinary rediscovery, while an older failure cannot delete a later concurrent success. | `_refresh_entry`; `get` | mcp/src/agents_remember/serving/harness_capability_catalog.py:110-135; mcp/src/agents_remember/serving/harness_capability_catalog.py:137-155 |
| Same-fingerprint concurrent callers share one in-flight discovery. | `_refresh_entry` | mcp/src/agents_remember/serving/harness_capability_catalog.py:137-155 |
| The daemon envelope nests the unchanged normalized snapshot and carries only schema, harness, cache status, and install fingerprint around it. | `CapabilityCatalogResult`; `to_json` | mcp/src/agents_remember/serving/harness_capability_catalog.py:49-65 |
| Cache lookup is bounded per native harness, single-flight under one lock, and conditionally removes only the observed entry on failed explicit refresh. | `HarnessCapabilityCatalog`; `get`; `_refresh_entry` | mcp/src/agents_remember/serving/harness_capability_catalog.py:81-196 |
| Discovery resolves the installed executable, uses current environment, normalizes effective argv, and calls only the adapter `discover()` port. | `_installed_harness`; `_discover` | mcp/src/agents_remember/serving/harness_capability_catalog.py:157-179; mcp/src/agents_remember/serving/harness_capability_catalog.py:181-196 |

## Cross-Repo References

No sibling repository is needed to prove this own-adapter daemon cache.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T13:54+02:00 — 260731-EFA-L6 S18-B13 curator: corrected cache-hit semantics and reissued whole-claim evidence for miss, refresh, and executable-change behavior for same-reviewer closure.

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: created the one-to-one sidecar for dynamic
  token-free cache hit/refresh, executable invalidation, failed-refresh quarantine and recovery,
  concurrent-success protection, single-flight enumeration, bounded retention, and normalized
  model-gated output. The source is new and uncommitted, so verification hash and date remain empty
  until closeout.
