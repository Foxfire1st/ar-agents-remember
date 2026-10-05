# kernel/primitives/ — Kernel Primitive Vocabulary Overview

## Paseo runtime settings and launch authority

paseo_runtime_settings supplies strict nested runtime fields and runtime_config carries the selected native host authority without inferring readiness, source ownership or model availability from a folder. Model, effort and service tier remain independent role settings, resolved by the existing settings chain and validated against the selected native catalog. Unconfigured runtime and unsupported configured capability retain explicit refusals.

- Current imported source owns this scoped route boundary. [4]
- Current imported source owns this scoped route boundary. [5]
- Current imported source owns this scoped route boundary. [6]
- Current imported source owns this scoped route boundary. [7]

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/kernel/primitives/` |
| onboardingRoute | `mcp/src/agents_remember/kernel/primitives/overview.md` |
| parentOverview | [`mcp/overview.md`](../../../../overview.md) |

## What This Area Is

The kernel-owned primitive vocabulary extracted by 260731-EFA-L9 so kernel stops importing
upward: runtime configuration (`runtime_config.py`, moved from `mcp/config.py` — the leaf's
centre of gravity), checkout coordination isolation, gate policy/vocabulary, provider identity, inbox backoff, memory cap, drift
snapshot/observer paths, command capture, tool reports, provider-degradation settings, and
version identity. Every layer above kernel reads these without importing `mcp`, `controlplane`,
`providers`, or `worktrees`.

## Hot Path Summary

The imported native Paseo role route retains canonical task/workspace identity, exact launch/replay and independent model/effort/tier validation alongside the existing converted MIK memory and publication owners.

`runtime_config.py::McpRuntimeConfig` is the trusted authority settings record;
`checkout_coordination.py` keeps unpublished linked-checkout coordination writes inside the
leaf's disposable coordinator, permits operational artifacts only inside the exact enclosure
`reports/` root, admits the explicit plane-owned lifecycle-operation worker without granting a
daemon role, and refuses undeclared primary-checkout access; `gate_policy.py`
owns the human-first gate delegation policy; `provider_degradation_settings.py` parses the
`providerDegradation` block; `inbox_backoff.py` owns redelivery backoff; `memory_cap.py` plans
explicit opt-in hard caps while uncapped full gates stay host-managed; `identity.py` owns provider instance naming;
`version.py` resolves installed distribution metadata through a function seam and falls back to the
committed source-checkout release identity when package metadata is unavailable.

`RepositoryScope.certification_profile` carries an optional configured profile reference.
The runtime parser admits only canonical, traversal-free repository-relative POSIX paths;
absolute paths, backslashes, drive prefixes, and normalization-changing spellings refuse.
The profile loader and executor remain downstream owners.

## What Belongs Here

| Path | Role |
| --- | --- |
| `checkout_coordination.py` | Loaded-checkout classification, execution-mode declaration, and leaf-local durable-write containment. |
| `runtime_config.py` | Runtime configuration record + parsing (from `mcp/config.py`). |
| `command_capture.py` | Package-local command-module adapter helpers. |
| `drift_snapshot.py` | Drift-snapshot path/removal primitives. |
| `gate_policy.py` | Gate delegation policy. |
| `gate_vocab.py` | Gate-kind vocabulary. |
| `identity.py` | Provider instance identity/naming. |
| `inbox_backoff.py` | Inbox redelivery backoff + rate limiting. |
| `memory_cap.py` | Optional explicit full-gate hard-cap planning; default host memory/swap remains untouched. |
| `observer_paths.py` | Observer store-root path conventions. |
| `provider_degradation_settings.py` | Provider degradation settings parsing. |
| `tool_reports.py` | Bulk tool-report retention/redaction. |
| `version.py` | Installed package identity with an explicit metadata-or-source fallback resolver. |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Policy/record stores or lifecycle machinery | `controlplane/`, `worktrees/`, `application/` |
| Wire/response models | `models/` |
| Provider runtime/teardown | `application/provider_runtime.py` |

## Structures Found Here

- Settings records with fail-loud `ConfigError`/typed error families.
- Policy/vocabulary literals with single-declaration ownership.
- Pure path, checkout-containment, backoff, cap-planning, and identity helpers.

## Operating Model

1. Kernel owns the vocabulary; models re-export wire names, controlplane/worktrees consume them
   through models/application ports.
2. The armed layering rail enforces `rank(Q) < rank(P)` for every import from this route.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `checkout_coordination.py` | checkout write policy | Prevents unpublished worktree code from selecting or writing the deployed coordinator through supported paths. | covered |
| `runtime_config.py` | config authority | Every layer reads the same runtime record. | covered |
| `gate_policy.py` | policy | Human-first gate decisions. | covered |
| `memory_cap.py` | gate economics | Plans explicit opt-in full-wrapper caps; uncapped runs remain host-managed. | covered |

## Local Invariants And Traps

- Kernel never imports upward; if a primitive needs a producer above it, the producer supplies a
  port/implementation instead.
- Single declaration per vocabulary (gate kinds, decision roles, provider ids); wire layers
  re-export, never retype.
- Checkout execution mode is declared once in kernel. Undeclared linked worktrees own only
  `<worktree-group>/provider-runtime/dev-ar-coordination` for coordination rows and the exact
  enclosure `reports/` root for operational artifacts; undeclared primary checkout access is
  refused and tests declare their mode explicitly.
- The `lifecycle-operation` mode belongs only to the detached task worker. It admits live
  operation authority but does not populate the MCP/dashboard daemon writer role.

## Evidence

### Repo-Internal References

- Checkout policy derives from the loaded package path, separates coordination rows from enclosure reports, and centrally refuses targets outside both exact leaf-local roots. [1]
- The layering rail enforces the total order this route anchors. [2]
- Structural gate models import the producer-owned gate vocabulary from kernel. [3]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.

### Docs References

No Domain Documentation source is configured.

No configured domain documentation was available.

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `checkout_coordination.py` | [`checkout_coordination.py.md`](checkout_coordination.py.md) | covered | Checkout execution and durable-write isolation policy. |
| `runtime_config.py` | [`runtime_config.py.md`](runtime_config.py.md) | covered | Config authority. |
| `command_capture.py` | [`command_capture.py.md`](command_capture.py.md) | covered | Command adapter. |
| `drift_snapshot.py` | [`drift_snapshot.py.md`](drift_snapshot.py.md) | covered | Snapshot primitives. |
| `gate_policy.py` | [`gate_policy.py.md`](gate_policy.py.md) | covered | Gate policy. |
| `gate_vocab.py` | [`gate_vocab.py.md`](gate_vocab.py.md) | covered | Gate vocabulary. |
| `identity.py` | [`identity.py.md`](identity.py.md) | covered | Provider identity. |
| `inbox_backoff.py` | [`inbox_backoff.py.md`](inbox_backoff.py.md) | covered | Backoff policy. |
| `memory_cap.py` | [`memory_cap.py.md`](memory_cap.py.md) | covered | Memory cap. |
| `observer_paths.py` | [`observer_paths.py.md`](observer_paths.py.md) | covered | Observer paths. |
| `provider_degradation_settings.py` | [`provider_degradation_settings.py.md`](provider_degradation_settings.py.md) | covered | Degradation settings. |
| `tool_reports.py` | [`tool_reports.py.md`](tool_reports.py.md) | covered | Tool reports. |
| `version.py` | [`version.py.md`](version.py.md) | covered | Version identity. |

## Child Overviews

None.

## How To Use This Area

When adding a primitive:

1. Read this overview and the closest sibling sidecar.
2. Keep it import-free of higher packages; declare the vocabulary once.
3. Run the layering check and structural-coverage suite.

## 260815-DAG-L4 L4 Configured Repository Identity

Runtime configuration is part of protected-ref authority: code and memory Git common directories, memory mode, coordination root, and canonical task tree must match the durable contract before lifecycle journaling or mutation.
