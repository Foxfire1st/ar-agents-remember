# mcp/src/agents_remember/serving/changeset.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`changeset.py` is the read-only **change-set API** (L3 of the operations-integration
series): the serving endpoints that compute a task's — and the master's accumulated —
change-set. It mirrors the L1 files API pattern (GET-only, 127.0.0.1-bound, reusing
`serving/scope.py` for scope resolution + the 404/400 error map and
`kernel/sidecar_pairing` for sidecar pairing). It feeds the L4 Change-Set Viewer:
code + memory line counters, and BEFORE/AFTER file content for a CodeMirror MergeView.
L4a adds the **doc-reader leaf views** — a single leaf's `committed` (**the contract's two recorded
commits**) or `working` (uncommitted) change-set, resolved by leaf-id straight off the persisted
enclosure contract, so the viewer works with no live worktree.

## Code Commentary

### 260731-EFA-L4 Current Delta — The Three Routes Now Declare What They Answer With

- `GET /api/changeset/task` cit:(["/api/changeset/task"], mcp/src/agents_remember/serving/changeset.py:669-669) declares `response_model=LeafChangeSet | TaskChangeSet`
  with `responses=SCOPED_READ_RESPONSES`. **Two success shapes**, because the `leaf` selector is
  what picks between them: `LeafChangeSet` is `TaskChangeSet` plus the `mode` echo, so the union
  is the route's real answer, not a convenience.
- `GET /api/changeset/file-diff` cit:(["/api/changeset/file-diff"], mcp/src/agents_remember/serving/changeset.py:682-682) declares `response_model=FileDiff` with
  `responses=SCOPED_READ_RESPONSES`.
- `GET /api/changeset/master` cit:(["/api/changeset/master"], mcp/src/agents_remember/serving/changeset.py:708-708) declares `response_model=MasterChangeSet` with
  `responses=SCOPED_READ_RESPONSES`. **The refusal table is new in 260921-ICR-L13 and supersedes
  the earlier "no refusal shape" account below**: an *unknown* master (no series contract) still
  degrades to empty lists, but a master the contract names whose code endpoints are missing is
  refused by name (`MasterEndpointAbsent` → the shared 400/404 map) instead of being answered
  from a later branch tip. That absence is a fact about the generation-bound selection, not an omission.

`SCOPED_READ_RESPONSES` (from `serving/response_contract.py`) is the shared 400/404 map the
files and notes routes use. It covers both refusal paths this module has: `run_scoped`'s error
map on the `scope` branch, and the hand-rolled `JSONResponse` mapping the `leaf`/`master`
branches keep (`_leaf_json`, and the `file-diff` master branch's own
`bad-path`/`not-found` try/except).

Nothing on the wire changed and nothing is validated at runtime — every handler returns a
`Response` it built itself, and FastAPI applies `response_model` only to values it serializes
for you. The former broad conformance suite was removed in IAS testing cleanup. The response declaration still specifies the body contract, but this card makes no claim that the removed suite enforces it.

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
net files. **260921-ICR-L33 note: this endpoint is unchanged, and the sentence above still describes
it — but no dashboard reader is a net-only caller any more.** Both master-net readers
(`panels/changeset/ChangeSetViewer.tsx`, `panels/detail-panel/changeSetBar.tsx`) now pass
`includeLeaves: true`, because R33.2 makes the per-leaf attribution part of what a master's net must
show; the escape this sentence documents is retained API surface for any caller that genuinely renders
only the net.

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

cit:([`task_changeset`], mcp/src/agents_remember/serving/changeset.py:100-119) is the per-**enclosure** change-set.
cit:([`_require_contract`], mcp/src/agents_remember/serving/changeset.py:81-89) loads the leaf contract for the base commits and
raises `FileNotFoundError` (→ `404 not-found`) for a mainline scope or an unreadable
contract — mainline has no base, so it has no change-set. Code = `changed_files_with_counts(scope.code_root,
contract.code_base_commit, None)` (base → the live worktree), each entry tagged with
`hasSidecar` via `route_sidecar_status`; memory = the same over `contract.memory_worktree` +
`contract.memory_base_commit` (skipped when there is no memory tree). cit:([`_sum`], mcp/src/agents_remember/serving/changeset.py:91-98)
produces the `{files, insertions, deletions}` counters (binary `None` counts → 0).

cit:([`file_diff`], mcp/src/agents_remember/serving/changeset.py:122-148) emits BEFORE + AFTER content (not unified-diff
text) so the L4 pane feeds CodeMirror MergeView `a`/`b` directly. `kind="memory"` diffs
the memory worktree, anything else the code worktree; `before =
commit_text_or_none(root, base, relp)` (the `git show base:path` reader — `None` for an
added file) and `after` = the worktree read (`None` for a deleted file); `language` comes
from `language_for`. The path is confined with `confine_rel`.

`master_changeset(config, repo_id, master)` is the series **NET** change-set —
`git diff <master-base> <selected-result>` for code + memory, **not** a sum of the leaves.
The selection lives in the sibling `serving/master_net_generation.py` (260921-ICR-L13 moved it
out of here): cit:([`master_task_root`], mcp/src/agents_remember/serving/master_net_generation.py:120-125)
confines `master` to a single path segment (no `/` `\` or leading `.`) so a wire value cannot
escape the tasks tree, and `select_master_net` resolves the declared integrated result for a
live request or the exact recorded endpoints a pinned request names — with deliberately **no**
source-branch fallback for a missing tip. cit:([`_leaf_state`], mcp/src/agents_remember/serving/changeset.py:175-186)
labels each breakdown row `working` (its code worktree is still live — counters move with the
worktree) or `committed`, so an in-flight preview is never mixed into the net silently.
cit:([`_master_leaf_summaries`], mcp/src/agents_remember/serving/changeset.py:188-215)
keeps the per-leaf `{leafId, state, counters}` breakdown alongside (each leaf vs its own base, via
`_leaf_counts` L150-L164). An unknown master (no series contract) degrades to an empty net
(never a 500); a master the contract names but whose code endpoints are missing is refused by
name instead. `master_file_diff(config, ref)` pins the AFTER side: without pins it is the live
integrated result, with pins the exact recorded tip the listing published (R03's listing-pinned
expansion idiom), so an opened entry stays bound after the branch advances. BEFORE =
`commit_text_or_none(repo, base, relp)`, AFTER = `commit_text_or_none(repo, tip, relp)` (both
committed refs). A pinned endpoint the repository does not hold is refused by name, never
re-resolved to the current tip.

`leaf_changeset(config, repo_id, master, leaf, mode)` + `leaf_file_diff(...)` are the L4a
doc-reader leaf views. `_load_leaf_contract` resolves the leaf enclosure contract by
`slugify(leaf) == contract.leaf_id` over `_master_enclosure_contracts`, scoped to `master`
(matched against the contract's parent/task name) and skipping `cleanup == "abandoned"` — the
contract persists after the worktree is cleaned up, so a **completed** leaf still resolves; `leaf`
is confined to a single path segment. `_leaf_range(contract, *, memory, mode)` selects the range and
returns it with that side's **named absence**: **`committed` is the contract's two recorded commits**
— `base_commit` → the landed commit its closeout or integration wrote (`code_commit or
integrated_code_commit`, memory likewise) — resolved through `serving/changeset_endpoints.py`, which
reports a recorded endpoint's absence by name rather than substituting the worktree's moveable `HEAD`
(see the `260921-ICR-L1` section below); `working` = `worktree-HEAD → worktree` (the **uncommitted
delta only**), and returns `[], ""` for a side with no live worktree (so a disabled memory side never
fails the view, mirroring `task_changeset`'s memory degradation). **The second return value is the
code side's own `not-recorded` sentence when its landed commit is not written yet, and
`leaf_changeset` publishes it as the body's `state`/`stateDetail` instead of raising it** (see the
`260921-ICR-L25` section below: an unrecorded range is a state of the task's progress, not a missing
resource). The live-**code**-worktree requirement that makes `working` meaningful is enforced once in
`leaf_changeset` (→ `404`). Both return the `task_changeset` shape (plus a `mode` echo and, for a
leaf view, the `state`/`stateDetail` pair), so the L4 viewer renders them unchanged; two-commit
`committed` diffs run against the repository that holds the recorded commits (durable, and it shares
the worktree's object store), keeping it valid post-cleanup. `_leaf_onboarding_root` picks the live
worktree's `onboarding/` for `working`, else the repo's, for the `hasSidecar` tagging.

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
- **The master is the NET series diff, bound to a generation** — `git diff <master-base> <selected-result>`, one
  coherent range that is per-file inspectable (via `master_file_diff`) and does not
  double-count a file two leaves touched; the per-leaf `leaves[]` counter breakdown is kept
  alongside, each row labelled `committed`/`working`. The selection is the declared
  integrated result (series base → live integration-branch head) for a live request, or the
  exact recorded endpoints a pinned request names — published as `generation` (four commits
  + deterministic digest) with `current`/`superseded`/`unmeasured` currentness and the one
  scope `integrated`, so a completed master's recorded result keeps resolving after its
  source branch advances. A missing endpoint is refused by name, never substituted with a
  later tip; only an unknown master degrades to empty lists.
- **The net is exact when served, refusal when unreadable** — `_net_diff` degrades to `[]`
  ONLY for an empty endpoint pair (a degraded leg with nothing selected). A diff that fails
  after validation raises `MasterEndpointAbsent(kind="unresolvable")` with the reason,
  reaching the caller as a refused outcome rather than an exact-looking zero (F1 fix).
- **Leaf views are contract-resolved, not enclosure-bound** (L4a) — `committed` and `working`
  resolve by leaf-id from the persisted enclosure contract, so the change-set is reviewable from
  the doc reader with **no live worktree** (`committed` works for a completed/cleaned leaf;
  `working` is the uncommitted delta and needs a live code worktree → `404` otherwise). The
  selector is explicit and validated (`leaf` needs `master` + a valid `mode`), never inferred from
  which optional param is present.
- **A committed range is two recorded commits or nothing** (260921-ICR-L1) — `mode=committed` reads
  the contract's recorded cells through `recorded_committed_range` and never binds a branch tip or
  the worktree `HEAD`; a side whose landed commit is not recorded yet has **no committed range**, and
  only an unrecorded **memory** half degrades to an empty list (so the resolved code half is still
  published). **How the code half reports that absence changed in 260921-ICR-L25**: it is answered,
  never refused — `leaf_changeset` publishes `state="unrecorded"` with the route's own `stateDetail`
  sentence and withholds the counter total, because a `404` for a state every live leaf passes
  through was a browser console error on the page whose accepted criterion is zero (register B6).
  `working` remains the one view whose after-side is a filesystem location, and its own `mode` says
  so.

## Evidence

### Repo-Internal References

- The shared scope resolution + error map (`FileScope`, `run_scoped`, `language_for`). [1]
- The change-set primitive (counts/status, keeps deletions), branch existence probe, and BEFORE reader. [2]
- Sidecar presence is derived from governing route indexes or a mirrored sidecar-file probe. [3]
- Shared path confinement resolves the requested path and refuses repository escape. [4]
- The persisted contract model ("def load_contract(path: Path) -> WorktreeContract:") and loader ("def load_contract(path: Path) -> WorktreeContract:") behind master/leaf accumulation, with leaf-id normalization via "slug = slugify(worktree_name)". `slugify` is now defined in `tasks/task_paths.py` and re-exported by `worktrees/task_resolver.py`. [5]
- The app factory that calls `register_changeset_routes` before `mount_static`. [6]

| The task change-set envelope carries code/memory changes and counters. | "class TaskChangeSet(" | mcp/src/agents_remember/serving/response_contract.py:834-840 |
| The leaf change-set extends the task shape with the selected committed/working mode, and (260921-ICR-L25) with the `state`/`stateDetail` pair that keeps an unrecorded range apart from a measured-empty one. | "class LeafChangeSet(" | mcp/src/agents_remember/serving/response_contract.py:843-860 |
| The master change-set carries net changes and per-leaf counters, beside the generation identity it was selected at. | "class MasterChangeSet("; "class MasterNetGeneration(" | mcp/src/agents_remember/serving/response_contract.py:886-902; mcp/src/agents_remember/serving/response_contract.py:871-883 |
| The file-diff envelope carries separate optional before and after content. | "class FileDiff(" | mcp/src/agents_remember/serving/response_contract.py:905-1134 |
| The shared scoped-read refusal table declares 400 and 404 response envelopes. | "SCOPED_READ_RESPONSES: dict[int" | mcp/src/agents_remember/serving/response_contract.py:1136-1169 |
| Current production declaration; the removed broad suite supplies no current execution proof. | `register_changeset_routes` | mcp/src/agents_remember/serving/changeset.py:325-719 |

## 260731-EFA-L2 Current Delta

`leaf_file_diff` and the `GET` file-diff route now take one `ChangesetFileRef` instead of six query
parameters. The concept: **which file, in which change-set, seen through which lens** — `repo` and
`leaf`/`master` (with `scope`) locate the change-set, `kind` picks its code or memory half, `mode`
picks committed or working, and `path` names the file inside it. Any one alone selects nothing,
which is why the selector travels as one value from the query string down to the diff. The route
binds it with FastAPI `Depends()`, so the wire query parameters are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.


## 260921-ICR-L1 Current Delta — The Committed Range Binds The Recorded Commits, And Never HEAD

The leaf views' `committed` mode changed meaning, and the module gained one collaborator.

`mode=committed` is now **exactly the range between the two commits the enclosure contract recorded** —
`base_commit` and the landed commit its closeout or integration wrote — resolved by the new
`serving/changeset_endpoints.py` (`recorded_committed_range`). The superseded behaviour is what the
`### Logic` entry above described until this leaf and is corrected there: a still-live leaf whose
`code_commit` was not written yet **fell back to the worktree's `HEAD`**, which advanced with every
ordinary commit the task made. That published a range that was not the leaf's landed delta under a label
that said it was, and it answered differently on the next poll of the same URL. A leaf with no recorded
landed commit now has **no committed delta**, and says so by name: `RecordedEndpointAbsent`, a
`FileNotFoundError` so the routes keep their existing 404 mapping, carrying a `kind` and a message that
names the leaf, the missing cell, the two actions (read `mode=working` while the task is live, or reopen
after closeout records the range) — and deliberately **not** the live `HEAD`, which the leaf's own case
asserts is absent from the message.

**The two halves resolve independently, and the degradation is per side.** `_leaf_range` calls
`recorded_committed_range` for the code side and the memory side separately. An unrecorded **memory**
half (`kind == "not-recorded"`) degrades to `[]` with zeroed counters — the same degradation this side
has always published for a leaf that does not run memory — while the code half, resolved from its own
recorded commit, is still published. The **code** half carries the same `not-recorded` absence in its
own return value instead of raising it (the `260921-ICR-L25` section above corrects this paragraph's
earlier "keeps the refusal" wording: the endpoint *is* the view, so the view still publishes no list
for it, but the fact is now named in the body rather than refused). Every other absence stays
a refusal on both sides: `no-repository` (the contract names no repository for that side) and
`unresolvable` (a recorded commit this checkout does not hold, checked with `git cat-file -e`) are
broken state, and reporting either as an empty range would publish a measurement the caller never made.
`leaf_file_diff`'s committed branch now reads both sides from `recorded.repository`, so the before/after
content comes from the same recorded pair as the path list.

**The `working` mode did not change at all**, and that is deliberate: it remains
`worktree-HEAD → worktree`, the one view whose after-side is a filesystem location, and its own `mode`
says so. The two modes are never mixed.

- **The two sides resolve independently, with the code half carrying its named absence in the return value while only an unrecorded memory half degrades to empty.** [7]
- The committed branch of the file diff, now reading both sides from the recorded range's own repository. [8]
- The doc-reader entry point that publishes the `committed` view's `state`/`stateDetail` and states the live-worktree requirement for `working`. [9]
- **The new collaborator: which exact Git objects a committed range binds, the three absence kinds, and the named absence an unrecorded endpoint reports.** [10]
- **The cases that measure the change: the recorded range bound and unmoved by a later commit, the state answered instead of a `HEAD` read, the route's own `200`, and the one-half degradation.** [11]

## 260921-ICR-L13 Current Delta — The Master Net Is Generation-Bound, And Selection Moved Out

The master entry changed shape, and the module gained one collaborator plus two selectors.

`serving/master_net_generation.py` is the new sibling that owns *which exact commits* the net
binds: the declared integrated result for a live request, or the exact recorded endpoints a
pinned request names, with a deterministic digest and same-call currentness. This module is
the thin delegating entry: `master_changeset` takes optional `pins`, resolves the selection,
diffs endpoint-to-endpoint per side through the new `_net_diff`, and publishes `generation` +
`currentness` + `scope: "integrated"` on every response. The four deleted privates moved, not
vanished — `_master_task_root`/`_load_master_contract` live on as `master_task_root`/
`load_master_contract`, and `_series_tip`/`_net_changed` are superseded by `integrated_tip`
(with deliberately no source-branch fallback) plus `_net_diff` (empty pair degrades, failed
read refuses). `master_file_diff(config, ref)` now takes a bundled `MasterFileRef` — repo,
master, kind, path, pins — for the same reason the routes take theirs: any one alone
selects nothing. The list route takes `MasterChangesetRef` (with `includeLeaves` and the
four pin params) via `Depends()`, so the wire query parameters are pinned without changing;
both master routes share the one `_master_json` 400/404 mapping, so a missing endpoint's
named refusal cannot come to differ between the list and the file view. `register_changeset_routes`
complexity overflow (C901 11>10) was cleared by that extraction, with no suppressions and no
limit widening. `LeafSummary` rows carry the new `state` (`committed`/`working`, from
`_leaf_state`).

- **The thin delegating entry: pins in, selection resolved, endpoint-to-endpoint diffs per side, `generation` + `currentness` + `scope` published; unknown master degrades, missing code endpoints refuse.** [12]
- **One side's net between two validated commits: empty pair degrades to `[]`, failed read refuses as `unresolvable`, missing repository refuses as `no-repository`.** [13]
- **The pinned AFTER side: live integrated result unpinned, exact recorded tip pinned; unresolvable pins refused, never re-resolved.** [14]
- **Whether a breakdown row shows live work or its landed delta.** [15]
- **The two bundled master selectors and their pin extractors, plus the one shared master 400/404 mapping.** [16]
- **The new collaborator that owns the selection this entry delegates to.** [17]
- **The F1 refusal case: a post-validation diff failure is refused, never an empty net.** [18]

This entry supersedes the earlier `### Logic` master paragraphs and the `### 260731-EFA-L4 Current Delta`
master-route paragraph where they conflict (deleted privates, source-branch fallback, no-refusal-table);
verification metadata stays pinned to the pre-commit source history until closeout.

## 260921-ICR-L25 Current Delta — An Unrecorded Committed Endpoint Is Answered, Not Refused

**The code half of a `committed` view no longer refuses when its landed commit is not recorded yet,
and this supersedes the L1 account above.** The L1 section and the `### Logic` paragraph both said
the code endpoint "keeps the named refusal"; at this tip it is answered in the body instead. What
did **not** change is the range itself: `HEAD` is still never substituted, and the published list is
still not a measurement.

`_leaf_range` now returns `tuple[list[dict[str, Any]], str]` — the range plus that side's named
absence — and only the code side ever carries one. The `RecordedEndpointAbsent` it catches with
`kind == NOT_RECORDED` is **carried, not raised**; `no-repository` and `unresolvable` still raise on
both sides, and the memory side's unrecorded endpoint still degrades to the same `[], ""` it has
always published for a leaf that does not run memory. `leaf_changeset` publishes the carried
sentence as `state: "unrecorded"` / `stateDetail` on the body, so **the two states the L1 account
collapsed stay apart**: a leaf whose endpoint nothing has recorded yet is *unrecorded*, which is not
the same fact as a resource that does not exist.

**Why a `404` was the wrong answer, stated as the distinction rather than as a preference.** The
leaf exists; only its landed commit has not been *written* yet. That is a state of the task's
progress, and it is the state **every live leaf is in** before its closeout — while the change-set
bar probes this view as soon as a leaf document is opened, so the refusal surfaced as a browser
console error on the page whose accepted criterion is zero (register B6). The three genuinely
distinct refusals are untouched and the route's own case measures them side by side: an **unknown
leaf** is still a named `404`, a **bad or absent `mode`** is still a `400`, and an **enclosure
`scope`** view is still its own `404` selection. So the state was not bought by turning every absent
thing into a `200`.

**What keeps the answer honest.** The counters beside it are a measured zero **of nothing**, so the
response contract's `state` is what stops them being read as "the leaf landed nothing"; the client
withholds the `+0 −0` total for exactly that reason (`dashboard/src/data/changeset.ts`,
`dashboard/src/panels/detail-panel/changeSetBar.tsx`). `state` is a **discriminator, not a
constant**: the same case drives `recorded_range(...)` afterwards and reads `state="recorded"` with
an empty `stateDetail`.

- **The caller that now carries the code half's named absence instead of raising it, and the memory half that still degrades to empty.** [19]
- **The doc-reader entry point that publishes the absence as the body's `state`/`stateDetail`.** [20]
- **The served vocabulary of the two states.** [21]
- **The cases that measure this change: the state discriminator with the head absent from the detail, the route-level status, and the one-half degradation.** [22]
- **The client that carries the state and withholds the total it would misprint.** [23]
