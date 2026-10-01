# mcp/src/agents_remember/serving/harness_launch.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines the single typed settings-resolved native launch selection and the fail-loud boundary that
validates it against dynamic own-adapter capabilities, verifies effective startup where possible,
and applies adapter-produced launch material without duplicate authority.

## Code Commentary

### Logic

`ResolvedLaunch` binds one harness id, model key, effort, and workspace and provides a strict JSON
round trip for the runner process boundary. `resolve_settings_launch` requires a complete model and
effort instead of defaulting a role-configured spawn. `validate_launch_selection` looks up the
model in the live `CapabilitySnapshot`, requires it to be selectable, and checks effort only against
that model's launch-settable options. Pi requires an exact provider-qualified catalog key; Claude
and Codex may use one unambiguous resolved vendor identity.

`verify_effective_launch` reuses catalog validation and compares running model/effort echoes. Its
explicit `require_effort_echo` parameter preserves real protocol asymmetry: Pi requires both echoes,
while Claude can truthfully accept model echo plus catalog-validated native effort because
stream-json exposes no effort echo. Since 260718-CHATS-L5F R2 a strict catalog-KEY equality is no
longer the only acceptance path: the `_resolves_to_same_model` secondary guard accepts when the
running-reported key and the requested selection resolve to the SAME underlying model — the fix for
the claude `opus[1m]` refused-pair, where request `opus[1m]` and `default` share
`resolved_model=claude-opus-4-8[1m]` and the harness echoes the resolved id. A genuinely different
or absent resolved model still fails loudly (both directions test-pinned); codex exact-key and pi
exact-provider-qualified-key acceptance are unchanged. `apply_launch_knobs` inserts adapter argv immediately after the
executable, merges adapter env, and refuses conflicts with owned argv options or config keys. The
Codex grammar scan covers separated, equals-attached, and short-attached selector/config forms.

### Conventions

This module is vendor-neutral policy and pure data transformation; vendor adapters produce
`LaunchKnobs`, and the hosted runner owns ordering and subprocess lifecycle. Errors name the exact
requested value and advertised alternatives so daemon/readiness clients can surface useful launch
evidence.

### Invariants And Boundaries

- The dynamic per-install/auth catalog is the native validation authority; no default path uses a
  package-owned model or global effort enum.
- Effort is always validated under the selected model.
- Pi model identity is exact `provider/id`; a bare id is refused with matching alternatives.
- Adapter-owned argv/config/environment cannot coexist with a second free-form declaration.
- Duplicate-selector preflight must happen before token-free discovery starts a transient process.
- Effective launch mismatch fails loudly, EXCEPT when the reported key and the requested selection
  resolve to the same underlying model (`_resolves_to_same_model`, R2) — an alias/default collision
  on one `resolved_model` validates; a different or absent resolved model still refuses. Acceptance
  evidence is never invented where a protocol lacks an echo.
- The module performs no subprocess, settings write, ACP transport, Toad hosting, composer paste,
  or mid-session mutation.

### Todos

L4 supplies typed selections from daemon requests/defaults; L3's setters may reuse the same model
lookup and model-gating semantics without conflating launch and mid-session acceptance.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this new file.

No configured domain documentation could be checked.

### Repo-Internal References

The launch policy is carried by the shared opener/runner and consumed by each own adapter.

- The normalized capability types nest effort under each model and declare owned launch selectors. [1]
- The runner performs pure conflict preflight, transient discovery, dynamic validation, then fresh runtime construction. [2]
- Claude produces native model/effort flags and verifies the model echo without fabricating effort echo. [3]
- Codex produces thread config plus owned model/config selectors. [4]
- Pi produces native provider-qualified model/thinking flags and requires both effective echoes. [5]
- The opener serializes this typed object into the runner and persists its selected values as catalog provenance. [6]

### Cross-Repo References

No external repository boundary is implemented; installed native harnesses are reached only through
their in-repository own adapters.

No meaningful cross-repo references found.
