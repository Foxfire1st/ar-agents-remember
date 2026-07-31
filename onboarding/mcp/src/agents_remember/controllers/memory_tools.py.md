# mcp/src/agents_remember/controllers/memory_tools.py

| Field                  | Value                                                      |
| ---------------------- | ---------------------------------------------------------- |
| repository             | agents-remember                                            |
| path                   | `mcp/src/agents_remember/controllers/memory_tools.py`       |
| doc_type               | `file-level-onboarding`                                    |
| lastUpdated            | 2026-07-31T15:31+02:00                                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                 |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                              |

## Governing Overview

[Controllers overview](overview.md)

## Purpose

`memory_tools.py` is the typed controller surface for onboarding drift, memory quality, route-index
refresh, memory initialization, baseline adoption, and memory carryover MCP operations.

## Code Commentary

### Logic

Since 260731-EFA-L2 three controllers take parameter objects defined here:
`MemoryBranches(source_branch, work_branch)` (default `DEFAULT_MEMORY_BRANCHES`) on
`memory_baseline_adopt_tool`; `CarryoverSelection(repo_id, source_memory, official_code_ref,
source_code_ref, old_base, replace_existing)` — everything the plan compares — passed positionally
to both carryover tools; and `CarryoverCommitMessages(memory, ledger)` (default
`DEFAULT_CARRYOVER_MESSAGES`) on apply. `intent_note` stays a separate keyword argument on apply
because it is the approval, not part of the selection.

The module resolves repository authority through `McpRuntimeConfig` and coordination context, then
delegates to package services. `route_index_refresh_tool` passes both
`context.code_repository_name` and the resolved `context.storage` into `build_route_indexes`; the
builder therefore receives the exact repository identity and path-rule authority already selected
by the resolver. Drift artifacts stay under the coordination temp root. Baseline and carryover
controllers preserve their separate service contracts.

### Conventions

Controllers translate validated tool arguments into service calls and JSON-compatible payloads.
Path confinement and repository authorization use the shared `_guards` helpers rather than local
filesystem checks.

### Invariants And Boundaries

- Tool callers cannot supply arbitrary source, onboarding, coordination, or storage roots.
- Route-index refresh must forward resolver-owned repository and storage authority explicitly; it
  must not reconstruct path rules from directory layout or parser defaults.
- Drift reports are temporary coordination artifacts, not durable onboarding content.
- Effectful refresh/init/baseline operations act by default and expose `dry_run` for preview;
  carryover remains an explicit plan/apply operation.

### Todos

None known for the MX-FIX-4 controller boundary.

## Docs References

No Domain Documentation source is configured for this repository; this card is grounded in the
package controller and resolver contracts.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The controller resolves context and forwards repository/storage authority to the route-index builder. | L80-L110 | [memory_tools.py](agents-remember/mcp/src/agents_remember/controllers/memory_tools.py) |
| The builder requires explicit repository and `StorageSettings` arguments. | L101-L123 | [route_index.py](agents-remember/mcp/src/agents_remember/kernel/route_index.py) |
| Coordination context is the repository and storage authority consumed by the controller. | context resolver | [coordination context overview](../kernel/coordination_context/overview.md) |

## Cross-Repo References

The controller can target configured sibling repositories, but no external implementation governs
this package-local dispatch contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-31T15:31+02:00 — 260731-EFA-L2: added `MemoryBranches`, `CarryoverSelection` and
  `CarryoverCommitMessages` (plus their shared defaults) and moved the baseline-adopt and carryover
  keyword lists onto them; `intent_note` deliberately stays outside the selection. Resolver
  authority, drift artifacts and the plan/apply split are unchanged. Verification metadata pinned
  until closeout stamps the L2 code commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: documented explicit resolved repository/storage
  authority at the route-index controller boundary.
- 2026-05-31T12:30+02:00 — Repo/path guards moved to shared `_guards`
  (`require_repo`/`require_within_coordination`) raising `AuthorityError`, and
  `memory_baseline_status` now returns `ok=False` on blocked drift (1.0.0 review remediation).
- 2026-05-28T19:52+02:00 — Created when memory/onboarding MCP controllers moved into their own
  domain module.
