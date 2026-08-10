# kernel/primitives/ — Kernel Primitive Vocabulary Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/kernel/primitives/` |
| onboardingRoute | `mcp/src/agents_remember/kernel/primitives/overview.md` |
| parentOverview | [`mcp/overview.md`](../../../../overview.md) |
| lastUpdated | 2026-08-08T14:38+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|

## What This Area Is

The kernel-owned primitive vocabulary extracted by 260731-EFA-L9 so kernel stops importing
upward: runtime configuration (`runtime_config.py`, moved from `mcp/config.py` — the leaf's
centre of gravity), gate policy/vocabulary, provider identity, inbox backoff, memory cap, drift
snapshot/observer paths, command capture, tool reports, provider-degradation settings, and
version identity. Every layer above kernel reads these without importing `mcp`, `controlplane`,
`providers`, or `worktrees`.

## Hot Path Summary

`runtime_config.py::McpRuntimeConfig` is the trusted authority settings record; `gate_policy.py`
owns the human-first gate delegation policy; `provider_degradation_settings.py` parses the
`providerDegradation` block; `inbox_backoff.py` owns redelivery backoff; `memory_cap.py` plans
memory-capped full gate runs; `identity.py` owns provider instance naming.

## What Belongs Here

| Path | Role |
| --- | --- |
| `runtime_config.py` | Runtime configuration record + parsing (from `mcp/config.py`). |
| `command_capture.py` | Package-local command-module adapter helpers. |
| `drift_snapshot.py` | Drift-snapshot path/removal primitives. |
| `gate_policy.py` | Gate delegation policy. |
| `gate_vocab.py` | Gate-kind vocabulary. |
| `identity.py` | Provider instance identity/naming. |
| `inbox_backoff.py` | Inbox redelivery backoff + rate limiting. |
| `memory_cap.py` | Full-gate memory cap planning. |
| `observer_paths.py` | Observer store-root path conventions. |
| `provider_degradation_settings.py` | Provider degradation settings parsing. |
| `tool_reports.py` | Bulk tool-report retention/redaction. |
| `version.py` | Installed package identity. |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Policy/record stores or lifecycle machinery | `controlplane/`, `worktrees/`, `application/` |
| Wire/response models | `models/` |
| Provider runtime/teardown | `application/provider_runtime.py` |

## Structures Found Here

- Settings records with fail-loud `ConfigError`/typed error families.
- Policy/vocabulary literals with single-declaration ownership.
- Pure path, backoff, cap-planning, and identity helpers.

## Operating Model

1. Kernel owns the vocabulary; models re-export wire names, controlplane/worktrees consume them
   through models/application ports.
2. The armed layering rail enforces `rank(Q) < rank(P)` for every import from this route.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `runtime_config.py` | config authority | Every layer reads the same runtime record. | covered |
| `gate_policy.py` | policy | Human-first gate decisions. | covered |
| `memory_cap.py` | gate economics | Caps full-wrapper memory at integration. | covered |

## Local Invariants And Traps

- Kernel never imports upward; if a primitive needs a producer above it, the producer supplies a
  port/implementation instead.
- Single declaration per vocabulary (gate kinds, decision roles, provider ids); wire layers
  re-export, never retype.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The layering rail enforces the total order this route anchors. | `load_contract` | mcp/src/agents_remember/code_quality/layering.py:62-62 |
| The wire layer re-exports gate vocabulary from kernel. | "from agents_remember.kernel.primitives.gate_vocab import (" | mcp/src/agents_remember/models/gates.py:14-18 |

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

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created the route overview for the new
  `kernel/primitives/` package. Verification metadata pinned until closeout stamps the L9 code
  commit.
