# harness_capability_catalog.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_capability_catalog.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T06:15+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns token-free, pre-session capability discovery for AR's three built-in native harness adapters
and exposes it through a bounded, install-aware cache. It is the daemon-side catalog authority for
dynamic model and model-gated effort data; it does not contain a fallback enum or start a model turn.

## Code Commentary

### Logic

`HarnessCapabilityCatalog.get` first resolves the requested registry entry and executable, rejects
unknown, non-native, and uninstalled harnesses, and fingerprints the harness id, effective argv,
canonical executable, and executable stat identity. A matching non-refresh request is a cache hit.
Misses and explicit refreshes pass the current process environment into a transient own-adapter
`discover()` call, with Codex argv normalized to `app-server` by the shared runner helper.

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
- Effort remains nested under each model in the returned `CapabilitySnapshot`.
- A failed explicit refresh cannot reopen the prior entry as an ordinary healthy hit.
- The cache and lock sets are bounded by AR's three built-in native harness ids.
- This module does not own HTTP routing, live-session mutation, settings authoring, ACP transport,
  Toad hosting, or frontend state.

### Todos

None known for the L4 pre-session catalog boundary.

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
| The adapter port limits normalized native discovery to the built-in protocol harness set. | `HarnessCapabilityDiscoverer`; `BUILTIN_PROTOCOL_HARNESSES` | mcp/src/agents_remember/serving/harness_control_adapter.py:62-65; mcp/src/agents_remember/serving/harness_control_adapter.py:136-136 |
| The shared runner helper converts Codex registry argv to the native app-server boundary without dropping supplied arguments. | `adapter_argv`; "app-server" | mcp/src/agents_remember/serving/harness_control_runner.py:311-319 |
| Focused tests pin cache hits, refresh quarantine, concurrent-success protection, executable invalidation, single flight, and the fixed cache bound. | `test_cache_hit_is_discover_only_and_preserves_model_gating`; `test_failed_refresh_quarantines_stale_entry_until_ordinary_recovery`; `test_failed_refresh_does_not_delete_a_later_concurrent_success`; `test_executable_change_invalidates_without_growing_the_cache`; `test_same_fingerprint_requests_share_one_inflight_discovery`; `test_refresh_reenumerates_and_replaces_the_bounded_entry` | mcp/tests/test_serving_harness_capabilities.py:88-105; mcp/tests/test_serving_harness_capabilities.py:107-117; mcp/tests/test_serving_harness_capabilities.py:119-131; mcp/tests/test_serving_harness_capabilities.py:133-150; mcp/tests/test_serving_harness_capabilities.py:152-175; mcp/tests/test_serving_harness_capabilities.py:177-187 |

## Cross-Repo References

No external repository or ACP transport is used by this catalog.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-03T03:08:11+02:00 — W3-B04 curator: curated 4 table citations (4 total), supplying exact anchors and paths; the scoped fixer generated all final extents.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: created the pre-session catalog sidecar for
  dynamic own-adapter discovery, bounded install-aware single flight, explicit auth refresh, and
  exact-entry quarantine after failed refresh. Verification remains empty until closeout stamps the
  new source file.
