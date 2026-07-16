# harness_capability_catalog.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_capability_catalog.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T06:15+02:00 |
| lastVerifiedCommitHash | `a1b0aa9143fa777efd8389892e3283ff257ef44d`|
| lastVerifiedCommitDate | 2026-07-16T06:37:02+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The normalized type layer owns the public capability shape, while the factory and runner helpers
provide the same native adapter construction and argv normalization used by hosted sessions.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The capability snapshot serializer retains model-local effort and the ACP Sense-1 projection. | L76-L133; L162-L194 | [harness_capabilities.py](agents-remember/mcp/src/agents_remember/serving/harness_capabilities.py) |
| The adapter port limits normalized native discovery to the built-in protocol harness set. | L31-L80 | [harness_control_adapter.py](agents-remember/mcp/src/agents_remember/serving/harness_control_adapter.py) |
| The shared runner helper converts Codex registry argv to the native app-server boundary without dropping supplied arguments. | L262-L271 | [harness_control_runner.py](agents-remember/mcp/src/agents_remember/serving/harness_control_runner.py) |
| Focused tests pin cache hits, refresh quarantine, concurrent-success protection, executable invalidation, single flight, and the fixed cache bound. | L88-L188 | [test_serving_harness_capabilities.py](agents-remember/mcp/tests/test_serving_harness_capabilities.py) |

## Cross-Repo References

No external repository or ACP transport is used by this catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: created the pre-session catalog sidecar for
  dynamic own-adapter discovery, bounded install-aware single flight, explicit auth refresh, and
  exact-entry quarantine after failed refresh. Verification remains empty until closeout stamps the
  new source file.
