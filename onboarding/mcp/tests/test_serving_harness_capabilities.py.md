# mcp/tests/test_serving_harness_capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_serving_harness_capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T06:15+02:00 |
| lastVerifiedCommitHash |  `a1b0aa9143fa777efd8389892e3283ff257ef44d`|
| lastVerifiedCommitDate |  2026-07-16T06:37:02+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The test source directly proves cache behavior and envelope shape; the catalog implementation owns
fingerprinting, quarantine, bounded retention, and native discovery composition.

| Finding | Citations | Source Path |
| --- | --- | --- |
| A cache hit performs one token-free discovery with current environment and preserves model-gated effort plus category-keyed config options in normalized JSON. | L88-L105 | [test_serving_harness_capabilities.py](agents-remember/mcp/tests/test_serving_harness_capabilities.py) |
| Explicit refresh and executable change replace the one retained entry and produce refreshed or miss status as appropriate. | L107-L131 | [test_serving_harness_capabilities.py](agents-remember/mcp/tests/test_serving_harness_capabilities.py) |
| Failed explicit refresh quarantines stale data until ordinary rediscovery, while an older failure cannot delete a later concurrent success. | L133-L175 | [test_serving_harness_capabilities.py](agents-remember/mcp/tests/test_serving_harness_capabilities.py) |
| Same-fingerprint concurrent callers share one in-flight discovery. | L177-L187 | [test_serving_harness_capabilities.py](agents-remember/mcp/tests/test_serving_harness_capabilities.py) |
| The daemon envelope nests the unchanged normalized snapshot and carries only schema, harness, cache status, and install fingerprint around it. | L48-L64 | [harness_capability_catalog.py](agents-remember/mcp/src/agents_remember/serving/harness_capability_catalog.py) |
| Cache lookup is bounded per native harness, single-flight under one lock, and conditionally removes only the observed entry on failed explicit refresh. | L80-L154 | [harness_capability_catalog.py](agents-remember/mcp/src/agents_remember/serving/harness_capability_catalog.py) |
| Discovery resolves the installed executable, uses current environment, normalizes effective argv, and calls only the adapter `discover()` port. | L156-L195 | [harness_capability_catalog.py](agents-remember/mcp/src/agents_remember/serving/harness_capability_catalog.py) |

## Cross-Repo References

No sibling repository is needed to prove this own-adapter daemon cache.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: created the one-to-one sidecar for dynamic
  token-free cache hit/refresh, executable invalidation, failed-refresh quarantine and recovery,
  concurrent-success protection, single-flight enumeration, bounded retention, and normalized
  model-gated output. The source is new and uncommitted, so verification hash and date remain empty
  until closeout.
