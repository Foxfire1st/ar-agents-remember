# harness_capability_catalog.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

No configured domain documentation could be checked.

### Repo-Internal References

The normalized type layer owns the public capability shape, while the factory and runner helpers
provide the same native adapter construction and argv normalization used by hosted sessions.

- The capability snapshot serializer retains model-local effort and the ACP Sense-1 projection. [1]
- The adapter port limits normalized native discovery to the built-in protocol harness set. [2]
- The shared runner helper converts Codex registry argv to the native app-server boundary without dropping supplied arguments. [3]
- The readiness verdict the install gate now consumes, so a probe-declaring harness is gated on its runtime rather than on `PATH`. [4]
- The probed-install identity: the interpreter is the fingerprint for a harness with no command, and a declared-but-absent interpreter still identifies the install. [5]
- The adapter-side snapshot the catalog normalizes, whose effort axis is published at this candidate because the runtime consumes it. [6]
- The cases: discovery through the existing factory, the not-ready refusal before discovery, the probed-interpreter fingerprint, and the unknown-harness refusal. [7]


### Cross-Repo References

No external repository or ACP transport is used by this catalog.

No meaningful cross-repo references found.
