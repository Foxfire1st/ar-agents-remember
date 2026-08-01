# mcp/src/agents_remember/serving/changeset.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/src/agents_remember/serving/changeset.py` |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-08-01T08:46+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`     |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
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

### 260731-EFA-L4 Current Delta — The Three Routes Now Declare What They Answer With

- `GET /api/changeset/task` (L511-L515) declares `response_model=LeafChangeSet | TaskChangeSet`
  with `responses=SCOPED_READ_RESPONSES`. **Two success shapes**, because the `leaf` selector is
  what picks between them: `LeafChangeSet` is `TaskChangeSet` plus the `mode` echo, so the union
  is the route's real answer, not a convenience.
- `GET /api/changeset/file-diff` (L526) declares `response_model=FileDiff` with
  `responses=SCOPED_READ_RESPONSES`.
- `GET /api/changeset/master` (L546) declares `response_model=MasterChangeSet` and **no
  `responses=` table at all** — an unresolvable master degrades to empty lists rather than
  refusing, so this route has no refusal shape to declare. That absence is a fact about
  `master_changeset`'s degrade-never-500 behaviour, not an omission.

`SCOPED_READ_RESPONSES` (from `serving/response_contract.py`) is the shared 400/404 map the
files and notes routes use. It covers both refusal paths this module has: `run_scoped`'s error
map on the `scope` branch, and the hand-rolled `JSONResponse` mapping the `leaf`/`master`
branches keep (`_leaf_json`, and the `file-diff` master branch's own
`bad-path`/`not-found` try/except).

Nothing on the wire changed and nothing is validated at runtime — every handler returns a
`Response` it built itself, and FastAPI applies `response_model` only to values it serializes
for you. The gate is `mcp/tests/test_serving_response_conformance.py`, which drives each route
and validates the real body against the declared model under `extra="forbid"`.

Note that the `Conventions` line below — "plain camelCase `dict[str, Any]` responses (no
pydantic models)" — remains true of the *handlers*: they still build dicts. What changed is that
the shape those dicts must have is now written down.

This entry supersedes any earlier description in this sidecar that conflicts with the current
source behavior above; verification metadata stays pinned to the pre-commit source history until
closeout.

### Logic

The master and leaf contract iterators are bounded to the exact requested
`tasks/<repo>/<master>/enclosures/*/series-contract.md` directory. Leaf lookup
slugifies both the request and persisted contract id, preserving master/repo
qualification for authored mixed-case ids. `master_changeset` keeps the
coherent series net range and makes the per-leaf `leaves` breakdown opt-in;
`includeLeaves=false` avoids the extra git work for callers rendering only the
net files.

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

`task_changeset(scope)` (L78-L97) is the per-**enclosure** change-set.
`_require_contract(scope)` (L59-L66) loads the leaf contract for the base commits and
raises `FileNotFoundError` (→ `404 not-found`) for a mainline scope or an unreadable
contract — mainline has no base, so it has no change-set. Code = `changed_files_with_counts(scope.code_root,
contract.code_base_commit, None)` (base → the live worktree), each entry tagged with
`hasSidecar` via `route_sidecar_status`; memory = the same over `contract.memory_worktree` +
`contract.memory_base_commit` (skipped when there is no memory tree). `_sum` (L69-L75)
produces the `{files, insertions, deletions}` counters (binary `None` counts → 0).

`file_diff(scope, kind, rel)` (L100-L125) emits BEFORE + AFTER content (not unified-diff
text) so the L4 pane feeds CodeMirror MergeView `a`/`b` directly. `kind="memory"` diffs
the memory worktree, anything else the code worktree; `before =
commit_text_or_none(root, base, relp)` (the `git show base:path` reader — `None` for an
added file) and `after` = the worktree read (`None` for a deleted file); `language` comes
from `language_for`. The path is confined with `confine_rel`.

`master_changeset(config, repo_id, master)` is the series **NET** change-set —
`git diff <master-base> <series-tip>` for code + memory, **not** a sum of the leaves.
`_load_master_contract` (L160-L170) loads the series (root) contract at
`tasks/<repo>/<master>/series-contract.md`, with `master` confined to a single path segment
(no `/` `\` or leading `.`) so a wire value cannot escape the tasks tree. `_series_tip`
resolves the shared series tip for both counters and file view: it uses the contract's
`code_work_branch` / `memory_work_branch` tip while that branch exists (the in-flight series
state), then falls back to `code_source_branch` / `memory_source_branch` once the series has
landed and the work branch has been deleted. `_net_changed` runs
`changed_files_with_counts(repo, base, resolved_tip)` over the code repo and the memory repo;
code entries are tagged with `hasSidecar` via `route_sidecar_status` on
`memory_repo_path/onboarding`. `_master_leaf_summaries` (L200-L222)
keeps the per-leaf `{leafId, counters}` breakdown alongside (each leaf vs its own base, via
`_leaf_counts` L128-L142). It degrades to an empty net (never a 500) on a missing contract /
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
| The declared response models and the shared `SCOPED_READ_RESPONSES` table these three routes name (`TaskChangeSet`, `LeafChangeSet`, `FileDiff`, `MasterChangeSet`). | [response_contract.py](response_contract.py.md) |
| The suite that enforces the declarations by driving each route and validating the real body. | [test_serving_response_conformance.py](agents-remember/mcp/tests/test_serving_response_conformance.py) |

## 260731-EFA-L2 Current Delta

`leaf_file_diff` and the `GET` file-diff route now take one `ChangesetFileRef` instead of six query
parameters. The concept: **which file, in which change-set, seen through which lens** — `repo` and
`leaf`/`master` (with `scope`) locate the change-set, `kind` picks its code or memory half, `mode`
picks committed or working, and `path` names the file inside it. Any one alone selects nothing,
which is why the selector travels as one value from the query string down to the diff. The route
binds it with FastAPI `Depends()`, so the wire query parameters are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-01T08:46+02:00 — 260731-EFA-L4 curator: recorded the three `response_model`
  declarations — `LeafChangeSet | TaskChangeSet` on `/api/changeset/task` (two real success
  shapes, picked by the `leaf` selector), `FileDiff` on `/api/changeset/file-diff`, both under
  the shared `SCOPED_READ_RESPONSES`, and `MasterChangeSet` on `/api/changeset/master` with no
  refusal table at all because an unresolvable master degrades to empty lists. Noted that
  FastAPI validates none of them (every handler returns a `Response`), so the gate is
  `test_serving_response_conformance.py`, and that the `Conventions` "no pydantic models" line
  still describes the handlers. Re-derived all **7** in-file self-citations, which the leaf's
  seven-line import block shifted by exactly +7: `_require_contract` L38-L45 → L59-L66, `_sum`
  L62-L68 → L69-L75, `task_changeset` L57-L76 → L78-L97, `file_diff` L79-L104 → L100-L125,
  `_leaf_counts` L113-L127 → L128-L142, `_load_master_contract` L153-L163 → L160-L170, and
  `_master_leaf_summaries` L193-L215 → L200-L222. Every behaviour claim was re-read against the
  source and is unchanged. Verification metadata pinned until closeout stamps the L4 commit.

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations after the module grew above them. `_sum` L48-L54 → L62-L68 (L48-L54 is now inside `_require_contract`), `_load_master_contract` L130-L142 → L153-L163, and `_master_leaf_summaries` L156-L178 → L193-L215 (that old range now spans `_series_tip`/`_net_changed`). Behaviour claims unchanged and re-read against the source.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `ChangesetFileRef` as the single file-diff selector (`leaf_file_diff(config, ref)`, route bound via `Depends()`; wire query unchanged).
- 2026-07-12T12:55+02:00 — 260712-TRH-L2: bounded master/leaf contract discovery to the requested repo/master enclosure, normalized requested and persisted leaf ids, and made master per-leaf summaries optional through `includeLeaves`; committed/working/master range semantics remain unchanged. Verification metadata pinned until closeout stamps the L2 code commit.

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
