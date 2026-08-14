# mcp/src/agents_remember/application/memory_tools.py

| Field                  | Value                                                      |
| ---------------------- | ---------------------------------------------------------- |
| repository             | agents-remember                                            |
| path                   | `mcp/src/agents_remember/application/memory_tools.py`       |
| doc_type               | `file-level-onboarding`                                    |
| lastUpdated            | 2026-08-11T14:58+02:00                                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                 |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                              |

## Governing Overview

[Application layer overview](overview.md)

## Purpose

`memory_tools.py` is the typed application entry point surface for onboarding drift, memory quality, route-index
refresh, memory initialization, baseline adoption, and memory carryover MCP operations.

## Code Commentary

### Logic

The module defines three parameter objects for separate application contracts:
`MemoryBranches` carries optional source/work branch overrides for baseline adoption
cit:([`MemoryBranches`], mcp/src/agents_remember/application/memory_tools.py:478-484);
`CarryoverSelection` carries the repository, memory/code refs, base, and replacement choice for
carryover planning/apply cit:([`CarryoverSelection`], mcp/src/agents_remember/application/memory_tools.py:491-507);
and `CarryoverCommitMessages` carries the two commit subjects for apply
cit:([`CarryoverCommitMessages`], mcp/src/agents_remember/application/memory_tools.py:510-516).
`intent_note` remains a separate apply approval argument.

The module resolves repository and leaf-memory authority through `McpRuntimeConfig` and the
coordination context; the leaf path is confined, the contract is loaded, and the leaf's own memory
worktree is required cit:([`_memory_scope`, `_leaf_memory_scope`], mcp/src/agents_remember/application/memory_tools.py:88-117; mcp/src/agents_remember/application/memory_tools.py:120-178).
For a contract-scoped quality check, `MemoryScope.unstamped_code_commit` carries the leaf's real
code-base commit as temporary comparison provenance. `memory_quality_check_tool` forwards it into
`DriftCheckContext`, so unstamped dirty-tree claims are checked before closeout without writing a
future verification stamp. The same leaf scope derives the one operational checklist path from the
contract's worktree group. A full scoped check gathers complete drift/report-only detail, current-
addition coverage, and a route-index preview, then atomically replaces that checklist; a subset or
official-memory call does not create it. A bare official-memory call leaves both leaf-only fields
absent.
`route_index_refresh_tool` then forwards the resolver-owned code root, onboarding root, repository
identity, and storage authority into `build_route_indexes`
cit:([`route_index_refresh_tool`], mcp/src/agents_remember/application/memory_tools.py:438-460).
Ordinary drift artifacts stay under the coordination temp root. The curator checklist is the
explicit enclosure-local exception and remains outside both Git worktrees. Baseline and carryover
entry points preserve their separate service contracts.

### Conventions

Application entry points translate validated tool arguments into service calls and JSON-compatible payloads.
Path confinement and repository authorization use the shared `_guards` helpers rather than local
filesystem checks.

### Invariants And Boundaries

- Tool callers cannot supply arbitrary source, onboarding, coordination, or storage roots.
- The leaf base is comparison provenance only: this module never writes it into onboarding
  verification metadata, and official-memory calls never invent an unstamped fallback.
- The full scoped checklist is an atomic operational report only. This module does not write
  onboarding, apply route indexes, or fabricate closeout provenance while producing it.
- Route-index refresh must forward resolver-owned repository and storage authority explicitly; it
  must not reconstruct path rules from directory layout or parser defaults.
- Drift reports are temporary coordination artifacts, not durable onboarding content.
- Effectful refresh/init/baseline operations act by default and expose `dry_run` for preview;
  carryover remains an explicit plan/apply operation.

### Todos

None known for the MX-FIX-4 application entry point boundary.

## Docs References

No Domain Documentation source is configured for this repository; this card is grounded in the
package application entry point and resolver contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared memory-scope resolver and its leaf confinement/temporary-provenance rules. | `MemoryScope`; `_memory_scope`; `_leaf_memory_scope` | mcp/src/agents_remember/application/memory_tools.py:42-57; mcp/src/agents_remember/application/memory_tools.py:88-117; mcp/src/agents_remember/application/memory_tools.py:120-178 |
| Contract-scoped quality forwards the temporary base while official scope leaves it absent. | "def memory_quality_check_tool("; "def test_a_contract_scoped_check_uses_the_leaf_base_for_unstamped_claims("; "def test_the_bare_check_does_not_invent_unstamped_claim_provenance(" | mcp/src/agents_remember/application/memory_tools.py:217-292; mcp/tests/test_memory_tool_enclosure_scope.py:296-321 |
| The route-index application entry point forwards resolver-owned authority. | `route_index_refresh_tool` | mcp/src/agents_remember/application/memory_tools.py:438-460 |
| The route-index builder. | `build_route_indexes` | mcp/src/agents_remember/kernel/route_index.py:182-230 |
| The route-index builder receives storage authority explicitly in its typed signature. | "def build_route_indexes(" | mcp/src/agents_remember/kernel/route_index.py:184-197 |

## Cross-Repo References

The application entry point can target configured sibling repositories, but no external implementation governs
this package-local dispatch contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-11T16:54+02:00 — Added the full scoped curator checklist composition and stable
  enclosure report path while keeping subset/official calls and code/memory content unchanged.
- 2026-08-11T14:58+02:00 — Made the temporary-provenance evidence one-to-one with the application
  declaration and its two exact scope regressions after preflight exposed the generic anchor's
  multiple current resolutions.
- 2026-08-11T14:40+02:00 — Documented contract-scoped temporary comparison provenance for
  unstamped dirty-tree claims, preserved closeout ownership of real verification stamps, and
  regenerated shifted application citations.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
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
