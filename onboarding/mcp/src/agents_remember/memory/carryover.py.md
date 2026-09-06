# mcp/src/agents_remember/memory/carryover.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/memory/carryover.py`                |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview      | `../../../overview.md`                                      |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

`carryover.py` plans and applies evidence-backed onboarding memory carryover after code lands. It is
the package service behind the `c-11-memory-carryover-from-branch` skill and MCP plan/apply tools.

## Code Commentary

### Logic

The service compares base, source, and official code/memory states; classifies file-sidecar, route-
overview, memory-only-doc, and entity-catalog candidates; and applies only proven or explicitly
selected changes. It preserves the existing exact-landed-commit, review-required, ledger mapping,
entity fingerprint validation, and guarded route-index refresh. Writes and commits belong to the
ordinary recovery leaf; integrating that leaf is a separate lifecycle operation.

**Three frozen parameter objects (260731-EFA-L2)** carry the comparison frame and the ledger handle
that were previously spread across long keyword lists:

- **`CarryoverRefs(code_repository_root, official_ref, source_ref, old_base, target_memory,
  source_memory)`** — the two states of the world a carryover compares and the base they diverged
  from. Every candidate builder judges one path against exactly this pair of sides, and the pair is
  **constant for a whole plan**, so it is built once in `build_plan_for_request` and passed down.
  That is the point: candidates from two different plans can no longer be assembled against
  mismatched refs. `candidate_for_path(refs, source_path, *, replace_existing)` and
  `memory_only_doc_candidates(refs, *, existing)` both take it.
- **`MemoryOnlyDoc(branch_doc, target_file, rel, source_path)`** — one onboarding doc that changed
  only in branch memory: the branch copy, its target counterpart, its path relative to the
  onboarding root, and the source path it documents. `_memory_only_evidence(refs, doc, mem_base)`
  takes the refs frame plus one of these.
- **`TargetLedger(ledger, path, memory_root, commit_message)`** — the recovery-leaf ledger as carryover
  writes it. A ledger without its file path and its memory tree cannot be persisted, so they are
  one handle. `_nothing_to_carry_result(plan, target_ledger, *, cleaned_note, carried,
  official_head)` takes it.

Apply first proves configured repository identity and the exact open ordinary external-memory leaf.
Both its code base and code HEAD must equal the selected official tip, with a clean code checkout.
After the plan and clean target-memory check, `required_target_storage(target_memory)` resolves
explicit effective settings before any content or ledger mutation. The same settings feed
`_refresh_target_route_indexes`; source-memory defaults cannot grant target write authority.

cit:([`_require_carryover_authority`], mcp/src/agents_remember/memory/carryover.py:856-892)
cit:([`_apply_carryover_for_request`], mcp/src/agents_remember/memory/carryover.py:759-853)

**Git now runs through the one owner (260731-EFA-L3).** This module no longer carries a local
`subprocess.run` adapter. It imports `run_git` from `agents_remember.kernel.git_command` and keeps
only `require_git`, which adds this module's contract — a non-zero exit is fatal — and returns the
stripped stdout every caller here wants:

```python
def require_git(repo: Path, args: list[str], *, input_text: str | None = None) -> str:
    result = run_git(repo, args, input_text=input_text)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout.strip()
```

`patch_id` is the only caller in the package that feeds git's stdin —
`run_git(repo, ["patch-id", "--stable"], input_text=diff_text)` — which is why `input_text` is a
keyword parameter of the shared runner rather than of a local copy. The ambient-selector scrubbing
this module used to perform for itself with `git_environment()` is now unconditional inside
`run_git` (`env=git_environment()`), and every carryover git call additionally inherits the shared
runner's `timeout=GIT_LOCAL_TIMEOUT_SECONDS` (300s) default, `encoding="utf-8"` and
`errors="surrogateescape"`. The removed local adapter had none of the last three.

### Conventions

CLI and MCP surfaces remain adapters around `CarryoverRequest`, `build_plan_for_request()`, and
`apply_carryover_for_request()`. Derived indexes are regenerated, never copied. Parser-default
settings may support read/topology discovery, but only explicit effective target settings may
authorize mutation.

### Invariants And Boundaries

- Only proven evidence tiers auto-carry; every source-branch commit touching a path must be an
  ancestor of the official ref for `exact-landed-commit`.
- Review-required paths must be selected explicitly.
- Target recovery-leaf storage/path-rule authority is established once before all mutation and reused
  for index refresh. Source-worktree settings cannot substitute for target settings.
- Authority refusal is exact zero mutation: target HEAD, Git status, non-Git bytes, source bytes,
  route-index presence, and ledger state remain unchanged.
- Git children use scrubbed repository-selection environment and never inherit the MCP stdio pipe.
  Both guarantees are the single `kernel.git_command.run_git`'s, not a module-local copy's: it always
  passes `env=git_environment()`, and `stdin=subprocess.DEVNULL` unless a caller supplies
  `input_text`. This module must not grow a second runner.
- Post-merge head mapping runs only when no auto-carry or review-required candidate remains.
- Apply commits only in the exact recovery-leaf memory checkout. It does not advance memory `main`
  or the selected integration branch; normal leaf integration owns publication.

### Todos

None known for the MX-FIX-4 carryover boundary.

## Docs References

No Domain Documentation source is configured for this repository. The service and raw target-settings preflight
define the current write-authority contract; deleted tests provide no current coverage claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Target JSON/Markdown settings are scanned for effective write authority with typed-parser equivalence. | `required_target_storage` | mcp/src/agents_remember/memory/carryover_authority.py:32-66 |
| Route-index rendering requires and reuses explicit repository/storage authority. | "Build route indexes using explicit Git and onboarding-storage authority", `RouteIndexBuildResult` | mcp/src/agents_remember/kernel/route_index.py:85-100; mcp/src/agents_remember/kernel/route_index.py:184-197 |
| Ledger updates remain delegated to the kernel memory-ledger service. | `load_ledger`, `write_ledger` | mcp/src/agents_remember/kernel/memory_ledger.py:187-190; mcp/src/agents_remember/kernel/memory_ledger.py:193-215 |
| The one git runner owns selector scrubbing (`GIT_REPOSITORY_SELECTOR_ENV`, `git_environment`), the `input_text` stdin path used by `patch_id`, and the timeout classes (`GIT_LOCAL_TIMEOUT_SECONDS = 300`). | `GIT_REPOSITORY_SELECTOR_ENV`, `git_environment`, `run_git`, `GIT_LOCAL_TIMEOUT_SECONDS` | mcp/src/agents_remember/kernel/git_command.py:33-42; mcp/src/agents_remember/kernel/git_command.py:70-70; mcp/src/agents_remember/kernel/git_command.py:76-82; mcp/src/agents_remember/kernel/git_command.py:85-151 |

## Cross-Repo References

Carryover intentionally spans the configured code and external-memory repositories, but its
authorization implementation remains package-local.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external implementation governs official-memory write authority. | — | — |

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-03T03:59:59+02:00 — Curated 10 citation claims (5 table rows, 5 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-07-31T20:52+02:00 — 260731-EFA-L3 curator: the module's local `run_git` (the only copy that
  accepted `input_text`) was deleted and every git call re-pointed at
  `kernel.git_command.run_git`; `require_git` now just wraps it. Rewrote the MX-FIX-4 note that
  claimed a "local input-bearing Git adapter" scrubs selectors — that adapter no longer exists —
  and recorded what the shared runner adds on top of the deleted copy (300s local timeout,
  `encoding="utf-8"`, `errors="surrogateescape"`). Added a `git_command.py` L24-L96 reference row.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `CarryoverRefs`, `MemoryOnlyDoc` and `OfficialLedger` parameter objects and
  re-signed `candidate_for_path`, `memory_only_doc_candidates`, `_memory_only_evidence` and
  `_nothing_to_carry_result` onto them. `build_plan_for_request` now builds one `CarryoverRefs` and
  passes it to both candidate builders, so a plan's comparison frame is constructed once instead of
  re-listed per call. Evidence tiers, decisions, reasons, the ledger-mapped-head path and the
  emitted plan/apply payloads are all unchanged. Verification metadata pinned until closeout stamps
  the L2 commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: apply now requires effective official-memory storage
  authority before mutation, reuses it for route-index refresh, and scrubs ambient Git selectors.
- 2026-06-11T15:05+02:00 — Documented `memory-only-doc` and `entity-catalog` candidate kinds,
  evidence helpers, fingerprint validation, and apply reporting.
- 2026-06-10T09:45+02:00 — Issue #54 sub-task C added ff-only memory-main advancement and result
  reporting.
- 2026-06-10T05:50+02:00 — Issue #56 sub-task 3 added route-overview candidates and guarded
  official-side route-index regeneration.
- 2026-06-10T05:30+02:00 — Git children stopped inheriting the MCP stdio protocol pipe.
- 2026-06-02T04:00+02:00 — Apply began mapping an unmapped official code HEAD when nothing is
  actionable to carry.
- 2026-05-31T12:30+02:00 — `exact-landed-commit` began requiring every path-touching source commit
  to be an official-ref ancestor.
- 2026-05-29T18:35+02:00 — Narrowed plan candidates for Pyright; behavior unchanged.
- 2026-05-24T00:35+02:00 — Added carryover request/service entry points for MCP controllers.
- 2026-05-23T13:09+02:00 — Copied into the MCP package and patched to package imports.
