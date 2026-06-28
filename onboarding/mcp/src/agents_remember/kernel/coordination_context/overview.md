# mcp/src/agents_remember/kernel/coordination_context/ — Coordination Context Modules

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/kernel/coordination_context/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-28T19:10+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`coordination_context/` contains the extracted implementation for the `c-08-ar-coordination-context-resolver` skill
package resolver. The public import and `python -m` entrypoint remain
`agents_remember.kernel.coordination_context_resolver`, while this package owns
the focused resolver, settings, storage, contract, cross-repo, serialization,
and CLI responsibilities.

## Hot Path Summary

Start in `resolver.py` for topology and context assembly, `settings.py` for
JSON-first settings selection, `json_settings.py` and `markdown_settings.py`
for settings formats, `markdown_cross_repo.py` and
`markdown_global_rules.py` for legacy Markdown parser branches, `storage.py`
for path-rule eligibility, `cross_repo.py` for branch-gated adjacent repo facts,
`contracts.py` for root/leaf series-contract fact loading, and `serialize.py` plus
`cli.py` for output adapters.

## Route Model

The package is intentionally split by responsibility:

- `models.py` owns dataclasses and typed dictionaries.
- `paths.py` owns path/topology primitives.
- `resolver.py` composes a `CoordinationContext` without performing mutation.
- `settings.py` chooses JSON settings over Markdown fallback and delegates
  concrete parsers.
- `json_settings.py`, `markdown_settings.py`, and `setting_values.py` own
  settings parsing details.
- `markdown_cross_repo.py` and `markdown_global_rules.py` keep the Markdown
  parser below complexity and maintainability thresholds.
- `storage.py` owns storage/path-rule decisions.
- `contracts.py` and `cross_repo.py` load external facts used by the resolver; contract lookup goes through active task-root and leaf-enclosure resolution, excluding archived task roots.
- `serialize.py` and `cli.py` adapt the context to text/JSON output.

## Invariants And Boundaries

- `c-08-ar-coordination-context-resolver` skill remains facts-only; this package does not create memory roots, modify
  Git worktrees, or write onboarding.
- MCP settings and explicit arguments are resolver authority; source-checkout
  `.env` and `.env.example` are not runtime coordination-root inputs.
- The facade preserves the public resolver import path and selected test seams,
  but implementation code belongs in the focused modules.
- Settings parsing is JSON-first; Markdown fenced settings are accepted only
  when a sibling `settings.json` is absent.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The package-local facade keeps existing callers pointed at the split implementation. | [coordination_context_resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |
| Resolver behavior is covered by resolver parity and worktree support tests. | [test_resolver_parity.py](agents-remember/mcp/tests/test_resolver_parity.py); [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): re-recorded main's worktree_name route note that the series carryover dropped — `contracts.py` gained a `worktree_name` fallback in `resolve_contract` plus `find_worktree_contract`, `resolver.py` forwards `worktree_name`, and the facade re-exports it (#90, MCP 2.9.3); **no route impact** (module responsibilities, structure, and invariants unchanged), detail lives in the `contracts.py` / `resolver.py` file sidecars.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: coordination context now resolves active task names, optional nested `parent_task`, and optional `leaf_id` into root or leaf `series-contract.md` paths instead of looking for sibling `contract.md` files. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-06T12:15: Re-verified against the current 15-file coordination-context package; purpose, hot path, route model, and invariants still match.
- 2026-05-25T20:57+02:00: Created after the monolithic `c-08-ar-coordination-context-resolver` skill package resolver was split into focused implementation modules, then amended when Markdown fallback parser branches moved into submodules.
