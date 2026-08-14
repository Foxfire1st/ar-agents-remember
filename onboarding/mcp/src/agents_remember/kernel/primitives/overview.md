# kernel/primitives/ — Kernel Primitive Vocabulary Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/kernel/primitives/` |
| onboardingRoute | `mcp/src/agents_remember/kernel/primitives/overview.md` |
| parentOverview | [`mcp/overview.md`](../../../../overview.md) |
| lastUpdated | 2026-08-13T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|

## What This Area Is

The kernel-owned primitive vocabulary extracted by 260731-EFA-L9 so kernel stops importing
upward: runtime configuration (`runtime_config.py`, moved from `mcp/config.py` — the leaf's
centre of gravity), checkout coordination isolation, gate policy/vocabulary, provider identity, inbox backoff, memory cap, drift
snapshot/observer paths, command capture, tool reports, provider-degradation settings, and
version identity. Every layer above kernel reads these without importing `mcp`, `controlplane`,
`providers`, or `worktrees`.

## Hot Path Summary

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
| `memory_cap.py` | gate economics | Caps full-wrapper memory at integration. | covered |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Checkout policy derives from the loaded package path, separates coordination rows from enclosure reports, and centrally refuses targets outside both exact leaf-local roots. | `resolve_checkout_location`; `require_durable_write_target` | mcp/src/agents_remember/kernel/primitives/checkout_coordination.py:90-108; mcp/src/agents_remember/kernel/primitives/checkout_coordination.py:132-155 |
| The layering rail enforces the total order this route anchors. | `load_contract` | mcp/src/agents_remember/code_quality/layering.py:62-62 |
| Structural gate models import the producer-owned gate vocabulary from kernel. | "from agents_remember.kernel.primitives.gate_vocab import (" | mcp/src/agents_remember/models/structural/gates.py:15-20 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

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

## Update History

- 2026-08-13T00:00+02:00 — 260731-EFA-L23 post-closeout worker-authority repair: added the narrow lifecycle-operation execution mode for the plane-owned detached task worker while retaining an empty daemon role and ordinary checkout isolation. The owner reports 46 focused tests, Ruff clean, and diff-check clean. Verification remains closeout-owned.
- 2026-08-12T22:24+02:00 — 260731-EFA-L23 async-closeout follow-up: separated checkout-local coordination authority from the exact enclosure report-artifact target; reports do not become a coordinator and every other durable target remains refused. Verification remains closeout-owned.
- 2026-08-12T22:04+02:00 — 260731-EFA-L23 post-code curator: documented the committed version resolver seam: installed package metadata is authoritative and a source checkout falls back to the `3.0.0rc7` release identity. Final verification stamping remains closeout-owned.

- 2026-08-12T10:08+02:00 — No route impact: the rc7 leaf changes the existing version fallback
  literal and names its metadata/fallback resolver so targeted CRAP can score it; primitive
  vocabulary, import direction, and route ownership are unchanged. Verification metadata remains
  pinned until closeout.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24: changed memory-cap
  ownership from a mandatory default to an explicit opt-in primitive; host-
  managed full gates bypass it. Verification metadata remains pinned until
  closeout stamps L24.

- 2026-08-10T18:31+02:00 — 260731-EFA-L21: added the checkout-coordination primitive, its
  loaded-package detection rule, explicit execution modes, deterministic leaf dummy root, and
  central durable-target containment. Verification metadata remains pinned until approved closeout.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created the route overview for the new
  `kernel/primitives/` package. Verification metadata pinned until closeout stamps the L9 code
  commit.
