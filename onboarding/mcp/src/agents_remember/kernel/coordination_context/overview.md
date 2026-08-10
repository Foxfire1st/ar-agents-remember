# mcp/src/agents_remember/kernel/coordination_context/ — Coordination Context Modules

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/kernel/coordination_context/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-08-01T00:00+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

- `models.py` owns dataclasses and typed dictionaries — with one deliberate exception since
  260731-EFA-L4: `CoordinationContext.memory_mode` (line 151) is no longer an independently
  declared `Literal["internal", "external", "disabled"]` but
  `worktrees.worktree_contract.MemoryMode`, imported at line 8. The two were the same three
  members, written twice, and this package is a *consumer* of that vocabulary rather than an
  author of it: `resolver._resolve` assigns `contract.memory_mode` straight into the field
  (line 284, reaching the constructor at line 307) whenever a contract is in scope, and falls
  back to `_memory_mode(topology)` (line 342, `internal`/`external` only — a resolved context
  is `disabled` only because a contract said so) when none is. Retype it here and the two
  copies can disagree again, which is a type error at line 284 in the good case and, in the
  bad one, a value this dataclass accepts that the contract writer refuses.
- `paths.py` owns path/topology primitives.
- `resolver.py` composes a `CoordinationContext` without performing mutation.
- `settings.py` chooses JSON settings over Markdown fallback and delegates
  concrete parsers.
- `json_settings.py`, `markdown_settings.py`, and `setting_values.py` own
  settings parsing details.
- `markdown_cross_repo.py` and `markdown_global_rules.py` keep the Markdown
  parser below complexity and maintainability thresholds.
- `storage.py` owns storage/path-rule decisions.
- `contracts.py` and `cross_repo.py` load external facts used by the resolver; contract lookup goes through active task-root resolution plus alias-aware leaf-enclosure resolution, excluding archived task roots.
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The package-local facade keeps existing callers pointed at the split implementation. | "_resolver.resolve_coordination_context" | mcp/src/agents_remember/kernel/coordination_context_resolver.py:131-146 |
| Resolver behavior is covered by resolver parity and worktree support tests. | "def test_external_memory_resolution_reports_expected_context(self) -> None:", "def test_resolver_returns_repo_task_root_without_task_name(self) -> None:" | mcp/tests/test_resolver_parity.py:57-57; mcp/tests/test_worktree_support_tests_1.py:386-386 |

## 260731-EFA-L2 Resolver API

`resolve_coordination_context` is now
`(code_repository_name=None, workspace_root=None, code_repository_root=None, *, hints:
CoordinationHints | None = None, selector: EnclosureSelector | None = None)`. The nine former
resolution arguments live on the two frozen bundles in `models.py`, which also owns
`CodeRepository` (replacing the untyped repo dict the private helpers passed around) and
`CoordinationRoots`. `build_coordination_context(repo, *, roots, storage, cross_repo, selector)`
and `contracts.resolve_contract(selector, coordination_root, code_repository_name)` match. All four
models are re-exported from the `kernel.coordination_context_resolver` facade, which is the
supported import path for callers outside this package. Resolution order, the onboarding-root
branch and contract-lookup precedence are unchanged.

## 260731-EFA-L9 Route Impact

The resolver CLI moved to `cli/coordination_resolver.py` (the `cli` package sits above kernel),
and the resolver now consumes a `ContractReaderPort` bound to
`worktrees/modules/contract_reader.py::WorktreeContractReader` instead of importing worktrees
directly. The coordination-context detection/assembly behavior is unchanged.

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 route impact: recorded the CLI move and the
  contract-reader port seam. Verification metadata pinned until closeout stamps the L9 code
  commit.

- 2026-08-03T03:59:59+02:00 — Curated 5 citation claims (2 table rows, 3 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-08-01T00:00+02:00 — 260731-EFA-L4 curator: this route's only L4 change is
  `models.py` (+5/-2), and it moves one ownership line. `CoordinationContext.memory_mode` stopped
  declaring its own `Literal["internal", "external", "disabled"]` and now imports
  `worktrees.worktree_contract.MemoryMode` (models.py line 8, field at line 151), so the
  Route Model's "`models.py` owns dataclasses and typed dictionaries" needed the exception
  recorded rather than left implied. Verified the direction of the dependency by reading
  `resolver.py`: `contract.memory_mode` is assigned into the field at line 284 and reaches the
  constructor at line 307, with `_memory_mode(topology)` (line 342) covering the no-contract
  case in `internal`/`external` only. This is not a new package boundary — `contracts.py`
  (line 14) and `resolver.py` (line 33) already imported from `worktrees.worktree_contract`;
  what changed is that one vocabulary is now declared once instead of twice. The resolver's
  facts-only boundary, settings authority, contract-lookup precedence and the L2
  `hints=`/`selector=` API are all unchanged. Verification metadata pinned until closeout
  stamps the L4 commit.
- 2026-07-31T21:04+02:00 — 260731-EFA-L3 curator: No route impact: checked Purpose, Hot Path
  Summary, Route Model and Invariants And Boundaries against this route's only L3 change —
  `cross_repo.py` (1 file, +7/-3), where `git_branch` (line 26) and `git_head_or_empty` (line 35)
  now pass `timeout=GIT_METADATA_TIMEOUT_SECONDS` to the runner. Unlike the routes this leaf
  consolidated, `cross_repo.py` already imported `run_git` from `kernel/git_command.py` and still
  re-exports it in `__all__` (line 17), so this route never held one of the drifted unguarded
  copies and no "owns its own git runner" claim exists here to correct. Module responsibilities,
  the resolver's facts-only boundary, settings authority and the L2 `hints=`/`selector=` API are
  all unchanged; the added bound is a per-call argument documented in the `cross_repo.py` sidecar.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2: the resolver's public API moved to keyword-only
  `hints=` / `selector=` bundles (`CoordinationHints`, `EnclosureSelector`), with `CodeRepository`
  and `CoordinationRoots` typing what the private helpers pass between them. Every caller in the
  tree was updated; resolved contexts are unchanged. Verification metadata pinned until closeout
  stamps the L2 commit.
- 2026-07-07T23:30+02:00 — 260707-HFX-L4 route impact: `contracts.py` now uses the dedicated
  `worktrees.leaf_refs` adapter for explicit leaf-id contract lookup, so qualified/doc-id/legacy refs can
  find the correct enclosure while the package structure stays unchanged. Verification metadata pinned
  until closeout stamps the 260707-HFX-L4 commit.
- 2026-06-28T20:30+02:00 — No route impact: `find_worktree_contract` now skips archived (`0_archive/`) contracts and its docstring was corrected to `series-contract.md`; the route's module structure and model are unchanged (detail in the contracts.py file sidecar; task 260628_post-landing-cleanup).
- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): re-recorded main's worktree_name route note that the series carryover dropped — `contracts.py` gained a `worktree_name` fallback in `resolve_contract` plus `find_worktree_contract`, `resolver.py` forwards `worktree_name`, and the facade re-exports it (#90, MCP 2.9.3); **no route impact** (module responsibilities, structure, and invariants unchanged), detail lives in the `contracts.py` / `resolver.py` file sidecars.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: coordination context now resolves active task names, optional nested `parent_task`, and optional `leaf_id` into root or leaf `series-contract.md` paths instead of looking for sibling `contract.md` files. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-06T12:15: Re-verified against the current 15-file coordination-context package; purpose, hot path, route model, and invariants still match.
- 2026-05-25T20:57+02:00: Created after the monolithic `c-08-ar-coordination-context-resolver` skill package resolver was split into focused implementation modules, then amended when Markdown fallback parser branches moved into submodules.
