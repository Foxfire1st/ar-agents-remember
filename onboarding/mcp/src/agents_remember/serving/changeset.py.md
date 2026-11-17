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

`serving/changeset.py` registers the read-only change-set API: enclosure, leaf and master selectors with the 400/404 JSON idiom. Both routes accept a recorded-comparison selector that reads the comparison's immutable trees through `serving/changeset_comparison.py`, refusing any `mode` combination.
## Current read lifetime

`register_changeset_routes` creates and returns one app-owned `ChangesetCache`, and the three locally defined JSON change-set routes run inside its read context with its weak body ETag — the cache reuses keyed reads, not responses. The bytes route shares their scheduler but bypasses cache.response. Reused from their keys with no observation on a hit are an id-keyed commit-range changed-file list and its counters, and the master net's two sides, which are one read keyed by the endpoint digest and the onboarding root, with every route index and mirror path its `hasSidecar` flags consult observed before it is read. File-diff sides now use diff_side instead of the cached commit-text reader. Not reused: every working view is computed natively, the master's endpoint selection and currentness are resolved per request, and the per-leaf breakdown rows stay per-request — so a repeated master read is not served from the cache as a whole. Native reads share captured input generations and retain values only after fresh observations agree; unreadable/changing inputs do not become reusable. HTTP conditional handling hashes the actual successful response body, so a matching ETag can avoid a body without substituting a different comparison or an unrecorded endpoint. Cache currentness is not task/closeout authority or a measured latency result.

   The earlier 100 ms revisit is relaxed by the same decision, is not a landing condition, and is not claimed as met.

## Code Commentary

### JSON declarations and media route

- `GET /api/changeset/task` declares `response_model=ComparisonChangeSet | LeafChangeSet | TaskChangeSet`
  with `responses=CHANGESET_READ_RESPONSES`. There are three success shapes: a recorded `comparison`
  selects the comparison response; otherwise a `leaf` selects the committed/working leaf view,
  and the enclosure scope selects the task view. `comparison` combined with `mode` is refused.
- `GET /api/changeset/file-diff` cit:(["/api/changeset/file-diff"], mcp/src/agents_remember/serving/changeset.py:880-880) declares `response_model=FileDiff` with
  `responses=CHANGESET_READ_RESPONSES`.
- `GET /api/changeset/master` cit:(["/api/changeset/master"], mcp/src/agents_remember/serving/changeset.py:915-915) declares `response_model=MasterChangeSet` with
  `responses=CHANGESET_READ_RESPONSES`. An *unknown* master (no series contract) still degrades to empty lists, but a master the contract names whose code endpoints are missing is refused by name (`MasterEndpointAbsent` → the shared 400/404 map) instead of being answered from a later branch tip. That absence is a fact about the generation-bound selection, not an omission.

`CHANGESET_READ_RESPONSES` (from `serving/response_contract.py`) retains the shared 400/404 refusal map and declares conditional 304 responses for these change-set routes. It covers both refusal paths this module has: `run_scoped`'s error
map on the `scope` branch, and the hand-rolled `JSONResponse` mapping the `leaf`/`master`
branches keep (`_leaf_json`, and the `file-diff` master branch's own
`bad-path`/`not-found` try/except).

Handlers build their explicit response bodies; the model declaration alone is not offered as an executed validation/control. The former broad conformance suite was removed in IAS cleanup. Current conditional reads add weak body ETags, no-cache and a bodyless 304 only for a matching successful response; non-200 responses pass through unchanged. The declaration still specifies the body contract without reinstating the removed suite.

Note that the `Conventions` line below — "plain camelCase `dict[str, Any]` responses (no
pydantic models)" — remains true of the *handlers*: they still build dicts. The response models declare the shape those dictionaries must have.



### Logic

The master and leaf contract iterators are bounded to the exact requested
`tasks/<repo>/<master>/enclosures/*/series-contract.md` directory. Leaf lookup
slugifies both the request and persisted contract id, preserving master/repo
qualification for authored mixed-case ids. `master_changeset` defaults
`include_leaves=True`; an explicit `includeLeaves=false` omits the per-leaf
breakdown while retaining the coherent series net. The dashboard's master counter
hook uses that net-only request first, then asks for attribution with
`includeLeaves:true` pinned to the generation just received. The detail bar calls
that hook; the viewer uses it through `useInspectionCounter` and separately
loads its generation-bound file listing with `includeLeaves:false`. The former L33
account that both readers always ask for a full breakdown is superseded.

`register_changeset_routes(app, config)` registers five GET routes: four local handlers and one delegated counter handler and
**must** be called before the greedy static `/` mount (it is, between
`register_files_routes` and `mount_static` in `serving/app.py`): `GET
/api/changeset/task`, `/api/changeset/file-diff`, `/api/changeset/master`, `/api/changeset/file-bytes`, and `/api/changeset/master/counters`. `CounterRoute.register` in `serving/master_counter.py` owns the last handler; `register_changeset_routes` composes and registers it. The `task` and
`file-diff` routes share a **selection precedence `leaf > master > scope`** (L4a): a `leaf`
param (qualified by `master`, with a `mode`) → the leaf view; `master` alone → the series net;
otherwise the enclosure `scope` → `run_scoped` (the shared error map). The leaf branch goes
through `_leaf_json` — it validates the selector (a `leaf` without `master`, or an unknown
`mode`, is a `400`) and maps domain errors to the same `400`/`404` idiom. `file-diff`'s
`master`-only branch keeps its own `JSONResponse` mapping; `master` (the list route) wraps its own.

cit:([`task_changeset`], mcp/src/agents_remember/serving/changeset.py:106-125) is the per-**enclosure** change-set.
cit:([`_require_contract`], mcp/src/agents_remember/serving/changeset.py:96-103) loads the leaf contract for the base commits and
raises `FileNotFoundError` (→ `404 not-found`) for a mainline scope or an unreadable
contract — mainline has no base, so it has no change-set. Code = `changed_files_with_counts(scope.code_root,
contract.code_base_commit, None)` (base → the live worktree), each entry tagged with
`hasSidecar` via `route_sidecar_status`; memory = the same over `contract.memory_worktree` +
`contract.memory_base_commit` (skipped when there is no memory tree). The imported `change_counters` alias `_sum` from `serving/changeset_reads.py` produces the `{files, insertions, deletions}` counters (binary `None` counts → 0).

cit:([`file_diff`], mcp/src/agents_remember/serving/changeset.py:128-153) emits BEFORE + AFTER content rather than unified-diff
text. `kind="memory"` diffs
the memory worktree, anything else the code worktree; `before =
committed_side(root, base, relp)` (the classified Git side reader — `None` for an
added file) and `after` = the classified working_side read (`None` for a deleted file); `language` comes
from `language_for`. Non-text sides carry binary/media metadata instead of decoded content. The path is confined with `confine_rel`.

`master_changeset(config, repo_id, master)` is the series **NET** change-set —
`git diff <master-base> <selected-result>` for code + memory, **not** a sum of the leaves.
The selection lives in the sibling `serving/master_net_generation.py` (260921-ICR-L13 moved it
out of here): cit:([`master_task_root`], mcp/src/agents_remember/serving/master_net_generation.py:120-125)
confines `master` to a single path segment (no `/` `\` or leading `.`) so a wire value cannot
escape the tasks tree, and `select_master_net` resolves the declared integrated result for a
live request or the exact recorded endpoints a pinned request names — with deliberately **no**
source-branch fallback for a missing tip. cit:([`_leaf_state`], mcp/src/agents_remember/serving/changeset.py:181-191)
labels each breakdown row `working` (its code worktree is still live — counters move with the
worktree) or `committed`, so an in-flight preview is never mixed into the net silently.
cit:([`_master_leaf_summaries`], mcp/src/agents_remember/serving/changeset.py:194-220)
keeps the per-leaf `{leafId, state, counters}` breakdown alongside (each leaf vs its own base, via
`_leaf_counts` L156-L170). An unknown master (no series contract) degrades to an empty net
(never a 500); a master the contract names but whose code endpoints are missing is refused by
name instead. `master_file_diff(config, ref)` pins the AFTER side: without pins it is the live
integrated result, with pins the exact recorded tip the listing published (R03's listing-pinned
expansion idiom), so an opened entry stays bound after the branch advances. master_file_diff reads both recorded sides through committed_side and serializes each with side_or_none. A pinned endpoint the repository does not hold is refused by name, never
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
worktree's `onboarding/` for `working`, else the repo's, for the `hasSidecar` tagging. The selected child need not exist; selection never tries the other root. `None` is returned only when the contract names no memory root for the selected mode.

### Conventions

Plain camelCase `dict[str, Any]` responses (no pydantic models), matching `files.py`.
Change-detection/count and HEAD readers come from serving/changeset_reads.py; committed and working file-side classification comes from serving/diff_side.py. Working file-diff sides use diff_side.working_side, which classifies media before loading bytes and decodes only non-binary UTF-8 text. Scope + error map come from `serving/scope.py`;
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
  an unrecorded **memory** endpoint degrades to an empty list (so the resolved code half is still
  published). **How the code half reports that absence changed in 260921-ICR-L25**: it is answered,
  never refused — `leaf_changeset` publishes `state="unrecorded"` with the route's own `stateDetail`
  sentence alongside counters. The client withholds the counter total, because a `404` for a state every live leaf passes
  through was a browser console error on the page whose accepted criterion is zero (register B6).
  `working` remains the one view whose after-side is a filesystem location, and its own `mode` says
  so.

`ChangesetTaskRef` and `ChangesetFileRef` gain `comparison: int | None`. When set, `_task_response` and `_file_response` divert to `_comparison_response`, which requires master+leaf, loads the leaf contract and produces `comparison_changeset` or `comparison_file_diff`; without it the leaf/master/scope paths run exactly as before. `_comparison_mode_refusal` rejects `comparison` combined with `mode` on both routes, and `_leaf_json` threads the new parameter through the existing Authority/FileNotFound mapping. The task route's response model widens to `ComparisonChangeSet | LeafChangeSet | TaskChangeSet`.
## Evidence

### Repo-Internal References



- The shared scope resolution + error map (`FileScope`, `run_scoped`, `language_for`). [1]


- Sidecar presence is derived from governing route indexes or a mirrored sidecar-file probe. [3]

- Shared path confinement resolves the requested path and refuses repository escape. [4]

- The persisted `WorktreeContract` model and `load_contract` loader support master/leaf accumulation; canonical leaf-ID normalization and worktree folder slugging have separate owners. `slugify` is now defined in `tasks/task_paths.py` and re-exported by `worktrees/task_resolver.py`. [5]


- The app factory that calls `register_changeset_routes` before `mount_static`. [6]


- The task change-set envelope carries code/memory changes and counters.
- The leaf change-set extends the task shape with the selected committed/working mode and the `state`/`stateDetail` pair that keeps an unrecorded range apart from a measured-empty one.
- The master change-set carries net changes and per-leaf counters, beside the generation identity it was selected at.
- The file-diff envelope carries separate optional before and after sides: text sides carry content, while non-text sides carry binary/media metadata.
- The shared scoped-read refusal table declares 400 and 404 response envelopes.
- Current production declarations do not make the removed broad suite current execution proof.

- Comparison and mode cannot be combined on either route [24]
- Both selectors carry the optional comparison number [25]
- A set comparison diverts to the recorded-trees producer [26]
- List reads divert; leaf and scope paths run as before [27]
## Bundled file selectors

`leaf_file_diff` and the `GET` file-diff route now take one `ChangesetFileRef` instead of six query
parameters. The concept: **which file, in which change-set, seen through which lens** — `repo` and
`leaf`/`master` (with `scope`) locate the change-set, `kind` picks its code or memory half, `mode`
picks committed or working, and `path` names the file inside it. Any one alone selects nothing,
which is why the selector travels as one value from the query string down to the diff. The route
binds it with FastAPI `Depends()`, so the wire query parameters are unchanged.




## The Committed Range Binds The Recorded Commits, And Never HEAD



`mode=committed` is now **exactly the range between the two commits the enclosure contract recorded** —
`base_commit` and the landed commit its closeout or integration wrote — resolved by the new
`serving/changeset_endpoints.py` (`recorded_committed_range`).   A leaf with no recorded
landed commit has **no committed delta**. `_leaf_range` catches `RecordedEndpointAbsent` with `kind == NOT_RECORDED` and carries the code side's named detail; `leaf_changeset` publishes `state="unrecorded"` and `stateDetail` instead of refusing the view. The detail names the leaf, the missing cell and the two actions (read `mode=working` while the task is live, or reopen
after closeout records the range), and deliberately excludes the live `HEAD`. Other admitted endpoint errors retain their existing refusal mapping.

**The two halves resolve independently, and the degradation is per side.** `_leaf_range` calls
`recorded_committed_range` for the code side and the memory side separately. An unrecorded **memory**
half (`kind == "not-recorded"`) degrades to `[]` with zeroed counters — the same degradation this side
has always published for a leaf that does not run memory — while the code half, resolved from its own
recorded commit, is still published. The **code** half carries the same `not-recorded` absence in its
own return value instead of raising it: the endpoint is the view, so the view publishes no list
for it and names the fact in the body rather than refusing it. Once recorded endpoint admission runs, other endpoint errors propagate. When the selected repository is `None`, the function returns an empty list and an empty detail before that admission; a missing side worktree in working mode returns the same pair. An unresolvable recorded commit is refused rather than reported as an exact range.
`leaf_file_diff`'s committed branch now reads both sides from `recorded.repository`, so the before/after
content comes from the same recorded pair as the path list.

**The `working` mode did not change at all**, and that is deliberate: it remains
`worktree-HEAD → worktree`, the one view whose after-side is a filesystem location, and its own `mode`
says so. The two modes are never mixed.

- **The caller resolves each side independently. An unselected repository returns an empty range before endpoint admission. Among entered endpoint errors, only not-recorded is caught: code carries a detail and memory carries none; other endpoint errors propagate.** [7]


- The doc-reader entry point that publishes the `committed` view's `state`/`stateDetail` and states the live-worktree requirement for `working`. [9]

- **The new collaborator: which exact Git objects a committed range binds, the three absence kinds, and the named absence an unrecorded endpoint reports.** [10]


- **The cases that measure the change: the recorded range bound and unmoved by a later commit, the state answered instead of a `HEAD` read, the route's own `200`, and the one-half degradation.** [11]


## Generation-bound master net



`serving/master_net_generation.py` is the new sibling that owns *which exact commits* the net
binds: the declared integrated result for a live request, or the exact recorded endpoints a
pinned request names, with a deterministic digest and same-call currentness. This module is
the thin delegating entry: `master_changeset` takes optional `pins`, resolves the selection,
diffs endpoint-to-endpoint per side through the new `_net_diff`, and publishes `generation` +
`currentness` + `scope: "integrated"` on every response. `master_task_root` and `load_master_contract` own master task/contract lookup; `integrated_tip` selects the integrated tip with no source-branch fallback, and `_net_diff` degrades an empty pair but refuses a failed read. `master_file_diff(config, ref)` now takes a bundled `MasterFileRef` — repo,
master, kind, path, pins — for the same reason the routes take theirs: any one alone
selects nothing. The list route takes `MasterChangesetRef` (with `includeLeaves` and the
four pin params) via `Depends()`, so the wire query parameters are pinned without changing;
both master routes share the one `_master_json` 400/404 mapping, so a missing endpoint's
named refusal cannot come to differ between the list and the file view. `register_changeset_routes`
complexity overflow (C901 11>10) was cleared by that extraction, with no suppressions and no
limit widening. `LeafSummary` rows carry the new `state` (`committed`/`working`, from
`_leaf_state`).



- **One side's net between two validated commits: empty pair degrades to `[]`, failed read refuses as `unresolvable`, missing repository refuses as `no-repository`.**


- **The pinned AFTER side: live integrated result unpinned, exact recorded tip pinned; unresolvable pins refused, never re-resolved.** [14]

- **Whether a breakdown row shows live work or its landed delta.** [15]
- **The two bundled master selectors and their pin extractors, plus the one shared master 400/404 mapping.**
- **The new collaborator that owns the selection this entry delegates to.** [17]
- **The F1 refusal case: a post-validation diff failure is refused, never an empty net.** [18]




## Current Behavior

`register_changeset_routes` creates one `_BoundedReads(threads=8, pending=8)` for the app and finalizes it with the app. Its four local async handlers use `_read_off_the_loop`; the master listing first obtains prepared pins. It also composes `MasterPreparation` with `CounterSource.read` and delegates `/api/changeset/master/counters` registration to `CounterRoute.register`. That handler asks the preparation owner for the requested net or attributed generation inside `read_async`, then uses the app cache's conditional-response path. The local scheduler's cap is its admission bound: overload returns 503 with `Retry-After: 1`, while abandonment withdraws queued work or lets running work release its slot. The conditional cache and read scheduler retain their separate responsibilities.

## An Unrecorded Committed Endpoint Is Answered, Not Refused

**The code half of a `committed` view answers an unrecorded landed endpoint in the body instead of refusing it.** `HEAD` is never substituted for the recorded range, and an unrecorded list is not a measurement of a committed delta.

`_leaf_range` now returns `tuple[list[dict[str, Any]], str]` — the range plus that side's named
absence — and only the code side ever carries one. The `RecordedEndpointAbsent` it catches with
`kind == NOT_RECORDED` is **carried, not raised**; other errors raised by endpoint admission still propagate. A missing selected repository returns `[], ""` before admission. The memory side's unrecorded endpoint still degrades to the same `[], ""` it has
always published for a leaf that does not run memory. `leaf_changeset` publishes the carried
sentence as `state: "unrecorded"` / `stateDetail` on the body: a leaf whose endpoint has not been recorded is *unrecorded*, which is not
the same fact as a resource that does not exist.

The leaf exists; only its landed commit has not been *written* yet. That is a state of the task's
progress before closeout records its landed endpoint; the change-set
bar probes this view as soon as a leaf document is opened. The three genuinely
distinct refusals are untouched and the route's own case measures them side by side: an **unknown
leaf** is still a named `404`, a **bad or absent `mode`** is still a `400`, and an **enclosure
`scope`** view is still its own `404` selection. The explicit unrecorded answer does not turn every absent resource into a `200`.

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




- **The client that carries the state and withholds the total it would misprint.** Anchor: `TaskChangeset` `ChangeSetButton` [23]






- Only actual successful response bytes get the ETag/no-cache and matching bodyless 304 path.


- The serving entry caches and reuses the worktree mutator's own NUL-delimited count/status read rather than implementing a second one. [30]

- The persisted WorktreeContract model and load_contract loader support master/leaf accumulation. normalize_contract_leaf_id resolves legacy leaf IDs through the canonical task-document reference; worktree_folder_name separately applies "slug = slugify(worktree_name)" to folder names. `slugify` is defined in `tasks/task_paths.py` and re-exported by `worktrees/task_resolver.py`.



- **The two bundled master selectors and their pin extractors, plus the one shared master 400/404 mapping.** [16]



## Additional source references





- The committed branch of the file diff, now reading both sides from the recorded range's own repository. Anchor: `leaf_file_diff` [8]

- **The thin delegating entry: pins in, selection resolved, endpoint-to-endpoint diffs per side, `generation` + `currentness` + `scope` published; unknown master degrades, missing code endpoints refuse.**  Anchor: `master_changeset` [12]


- The JSON task, file-diff and master change-set routes share and return the app-owned conditional-read cache. The media file-bytes route reads its selected side through its separate bytes path. [28]

- The master-counter hook first reads the net without leaves and requests leaf attribution against that returned generation. [31]
- The delegated master/counters route is registered by CounterRoute. [32]
