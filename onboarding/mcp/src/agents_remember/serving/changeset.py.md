# mcp/src/agents_remember/serving/changeset.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/src/agents_remember/serving/changeset.py` |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-07-04T23:43+02:00 |
| lastVerifiedCommitHash | `c522779df57ddee8192816d2f2769fdf20d75f3a`     |
| lastVerifiedCommitDate | 2026-07-04T23:51:13+02:00|
| governingOverview      | `overview.md`                                  |

## Governing Overview

[overview.md](overview.md)

## Purpose

`changeset.py` is the read-only **change-set API** (L3 of the operations-integration
series): the serving endpoints that compute a task's — and the master's accumulated —
change-set. It mirrors the L1 files API pattern (GET-only, 127.0.0.1-bound, reusing
`serving/scope.py` for scope resolution + the 404/400 error map and
`kernel/sidecar_pairing` for sidecar pairing). It feeds the L4 Change-Set Viewer:
code + memory line counters, and BEFORE/AFTER file content for a CodeMirror MergeView.
L4a adds the **doc-reader leaf views** — a single leaf's `committed` (landed) or `working`
(uncommitted) change-set, resolved by leaf-id straight off the persisted enclosure contract,
so the viewer works with no live worktree.

## Code Commentary

### Logic

`register_changeset_routes(app, config)` registers three GET routes and
**must** be called before the greedy static `/` mount (it is, between
`register_files_routes` and `mount_static` in `serving/app.py`): `GET
/api/changeset/task`, `/api/changeset/file-diff`, `/api/changeset/master`. The `task` and
`file-diff` routes share a **selection precedence `leaf > master > scope`** (L4a): a `leaf`
param (qualified by `master`, with a `mode`) → the leaf view; `master` alone → the series net;
otherwise the enclosure `scope` → `run_scoped` (the shared error map). The leaf branch goes
through `_leaf_json` — it validates the selector (a `leaf` without `master`, or an unknown
`mode`, is a `400`) and maps domain errors to the same `400`/`404` idiom. `file-diff`'s
`master`-only branch keeps its own `JSONResponse` mapping; `master` (the list route) wraps its own.

`task_changeset(scope)` (L56-L75) is the per-**enclosure** change-set.
`_require_contract(scope)` (L37-L44) loads the leaf contract for the base commits and
raises `FileNotFoundError` (→ `404 not-found`) for a mainline scope or an unreadable
contract — mainline has no base, so it has no change-set. Code = `changed_files_with_counts(scope.code_root,
contract.code_base_commit, None)` (base → the live worktree), each entry tagged with
`hasSidecar` via `route_sidecar_status`; memory = the same over `contract.memory_worktree`
+ `contract.memory_base_commit` (skipped when there is no memory tree). `_sum` (L47-L53)
produces the `{files, insertions, deletions}` counters (binary `None` counts → 0).

`file_diff(scope, kind, rel)` (L78-L103) emits BEFORE + AFTER content (not unified-diff
text) so the L4 pane feeds CodeMirror MergeView `a`/`b` directly. `kind="memory"` diffs
the memory worktree, anything else the code worktree; `before =
commit_text_or_none(root, base, relp)` (the `git show base:path` reader — `None` for an
added file) and `after` = the worktree read (`None` for a deleted file); `language` comes
from `language_for`. The path is confined with `confine_rel`.

`master_changeset(config, repo_id, master)` is the series **NET** change-set —
`git diff <master-base> <series-tip>` for code + memory, **not** a sum of the leaves.
`_load_master_contract` (L129-L143) loads the series (root) contract at
`tasks/<repo>/<master>/series-contract.md`, with `master` confined to a single path segment
(no `/` `\` or leading `.`) so a wire value cannot escape the tasks tree. `_series_tip`
resolves the shared series tip for both counters and file view: it uses the contract's
`code_work_branch` / `memory_work_branch` tip while that branch exists (the in-flight series
state), then falls back to `code_source_branch` / `memory_source_branch` once the series has
landed and the work branch has been deleted. `_net_changed` runs
`changed_files_with_counts(repo, base, resolved_tip)` over the code repo and the memory repo;
code entries are tagged with `hasSidecar` via `route_sidecar_status` on
`memory_repo_path/onboarding`. `_master_leaf_summaries` (L157-L179)
keeps the per-leaf `{leafId, counters}` breakdown alongside (each leaf vs its own base, via
`_leaf_counts` L112-L126). It degrades to an empty net (never a 500) on a missing contract /
ref. `master_file_diff(config, repo_id, master, kind, rel)` makes every net-changed file
inspectable against the same resolved tip: BEFORE = `commit_text_or_none(repo, master_base,
relp)`, AFTER = `commit_text_or_none(repo, resolved_series_tip, relp)` (both committed refs).

`leaf_changeset(config, repo_id, master, leaf, mode)` + `leaf_file_diff(...)` are the L4a
doc-reader leaf views. `_load_leaf_contract` resolves the leaf enclosure contract by
`slugify(leaf) == contract.leaf_id` over `iter_leaf_enclosure_contracts`, scoped to `master`
(matched against the contract's parent/task name) and skipping `cleanup == "abandoned"` — the
contract persists after the worktree is cleaned up, so a **completed** leaf still resolves; `leaf`
is confined to a single path segment. `_leaf_range(contract, *, memory, mode)` selects the range:
`committed` = `base → code_commit` (a still-live leaf whose `code_commit` is not written yet falls
back to the worktree HEAD — committed-so-far, **not** the dirty tree); `working` =
`worktree-HEAD → worktree` (the **uncommitted delta only**), and returns `[]` for a side with no
live worktree (so a disabled memory side never fails the view, mirroring `task_changeset`'s memory
degradation). The live-**code**-worktree requirement that makes `working` meaningful is enforced
once in `leaf_changeset` (→ `404`). Both return the `task_changeset` shape (plus a `mode` echo), so
the L4 viewer renders them unchanged; two-commit `committed` diffs run against the source repo (it
shares the worktree's object store), keeping it valid post-cleanup. `_leaf_onboarding_root` picks the
live worktree's `onboarding/` for `working`, else the repo's, for the `hasSidecar` tagging.

### Conventions

Plain camelCase `dict[str, Any]` responses (no pydantic models), matching `files.py`.
The change-detection primitive is `worktrees/modules/git.changed_files_with_counts`; the
BEFORE reader is `commit_text_or_none`; scope + error map come from `serving/scope.py`;
sidecar pairing from `kernel/sidecar_pairing.route_sidecar_status`.

### Invariants And Boundaries

- **Read-only, localhost, allow-listed** — inherits the L1 / Task-6 posture via the
  shared `run_scoped` + `resolve_scope`.
- **BEFORE/AFTER content, not unified-diff text** — the master decision, so the L4
  MergeView gets `a`/`b` and the highlight-off toggle is trivial; `before`/`after` are
  `None` for pure add/delete.
- **Change-set scope is an enclosure** — mainline has no base → 404; `task_changeset`
  always sees a live worktree (only active enclosures resolve through the endpoint).
- **The master is the NET series diff** — `git diff <master-base> <series-tip>`, one
  coherent range that is per-file inspectable (via `master_file_diff`) and does not
  double-count a file two leaves touched; the per-leaf `leaves[]` counter breakdown is kept
  alongside. The resolved series tip is the work-branch tip for an in-flight series and the
  source-branch tip only after the work branch is absent, so counters and file content stay
  aligned before and after landing.
- **Leaf views are contract-resolved, not enclosure-bound** (L4a) — `committed` and `working`
  resolve by leaf-id from the persisted enclosure contract, so the change-set is reviewable from
  the doc reader with **no live worktree** (`committed` works for a completed/cleaned leaf;
  `working` is the uncommitted delta and needs a live code worktree → `404` otherwise). The
  selector is explicit and validated (`leaf` needs `master` + a valid `mode`), never inferred from
  which optional param is present.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The shared scope resolution + error map (`FileScope`, `run_scoped`, `language_for`). | [serving/scope.py](agents-remember/mcp/src/agents_remember/serving/scope.py) |
| The change-set primitive (counts/status, keeps deletions), branch existence probe, and BEFORE reader. | [worktrees/modules/git.py](agents-remember/mcp/src/agents_remember/worktrees/modules/git.py) |
| The sidecar-pairing helpers (`route_sidecar_status`, `confine_rel`) reused for `hasSidecar` + confinement. | [kernel/sidecar_pairing.py](agents-remember/mcp/src/agents_remember/kernel/sidecar_pairing.py) |
| The leaf-enclosure contract enumerator + `WorktreeContract`/`load_contract` for master accumulation. | [worktrees/task_resolver.py](agents-remember/mcp/src/agents_remember/worktrees/task_resolver.py) |
| The app factory that calls `register_changeset_routes` before `mount_static`. | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The test suite for this module. | [test_serving_changeset.py](agents-remember/mcp/tests/test_serving_changeset.py) |

## Update History

- 2026-07-04T23:43+02:00 — L8 content update: master series net diffs now resolve a shared series tip through the work branch while it exists, falling back to the source branch after landing/deletion; `master_changeset` counters and `master_file_diff` BEFORE/AFTER content use the same resolved code/memory tip. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-03T12:50+02:00 — No content impact: L15 replaced the `live` boolean alias with visible `worktree is None` narrowing in the change-set file listing and file-diff functions so pyright proves the Optional[Path] uses; behavior identical (same guards, same fallbacks).
- 2026-06-29T23:00+02:00 — L4a: doc-reader leaf views. Adds `leaf_changeset` + `leaf_file_diff`
  (resolved by leaf-id via `_load_leaf_contract`, which persists past cleanup), `_leaf_range`
  (`committed` = base→code_commit with a live-worktree-HEAD fallback; `working` = HEAD→worktree
  uncommitted delta, `[]` for a side with no worktree), `_leaf_onboarding_root`, and `_leaf_json`
  (selector validation + 400/404 idiom). The `/api/changeset/{task,file-diff}` routes gained a
  `leaf` + `mode` selector with precedence `leaf > master > scope`; `task_changeset` /
  `master_changeset` semantics unchanged. Verification metadata pinned until closeout stamps the
  L4a commit.
- 2026-06-29T17:00+02:00 — L4 follow-up: `master_changeset` is now the **NET** series diff
  `git diff <master-base> <series-tip>` for code + memory (one coherent, per-file-inspectable
  range) instead of the sum-of-leaves; adds `master_file_diff` (base→tip), `_load_master_contract`
  (loads `tasks/<repo>/<master>/series-contract.md`, `master` confined to one path segment),
  `_net_changed`, and `_master_leaf_summaries` (the per-leaf counter breakdown kept). The
  `/api/changeset/file-diff` route gained an optional `master` param → `master_file_diff`. Reflects
  the committed/landed series (an un-integrated in-flight leaf shows in `leaves` but not the net).
  Verification metadata pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T15:30+02:00 — Created for operations-integration L3: the read-only change-set API — `GET /api/changeset/{task,file-diff,master}` (registered before the static mount), computing a task's `base → current` code + memory change-set with insertion/deletion counts + A/M/D/R status + `hasSidecar`, BEFORE/AFTER file content for the L4 MergeView, and the master's accumulation across leaf enclosures (active leaf → worktree, completed leaf → integrated commit; dedup by path, sum counts). Reuses `serving/scope.py` + the L1 posture; mainline has no base → 404. Verification metadata pinned to the task base until closeout stamps the L3 code commit.
