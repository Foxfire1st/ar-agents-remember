# mcp/src/agents_remember/serving/projections/snapshots.py

## Governing Overview

[serving projections overview](overview.md)

## Purpose

`snapshots.py` holds the file-surface readers the projection assembles — the
structural readers the *named* tree needs (provider current-state, surface 1; and
worktree enclosures — the contract, surface 6, plus the group layout, surface 5)
from slice 3a, plus the slice-3b analytical readers (drift snapshot, sidecar
staleness, setup summaries/progress, route coverage, tool reports, ledger), and the
slice-5e Engine Room readers (`read_engine_process_facts` — one status-guidance
fact bundle per contract — and `read_start_progress_entries` — the pre-contract
worktree-start blocks, §5.4). Every reader reuses the producing subsystem's own
parser rather than re-parsing.

## Code Commentary

### 260712-PTS-L2 Shared Per-Tick Contract Snapshot

`read_enclosures` and `read_engine_process_facts` gained a keyword-only
`contracts: ContractSnapshot | None = None` parameter. The projection tick passes the ONE
`ContractSnapshot` that `projection_store` builds per tick (see `contract_snapshot.py`), so these
readers add ZERO contract enumerations or parses of their own; a standalone call (`contracts=None`)
builds a local one-shot snapshot via `build_contract_snapshot`, preserving the public signature and
the walk-and-skip behavior each reader had before. `_enclosure_from_contract` now takes an
already-parsed `WorktreeContract` (the parse-and-skip moved into the snapshot builder). The snapshot's
`WorktreeContract` instances are cached across ticks — readers must treat them as immutable and never
mutate them.

### 260707-HFX2-L13 Task Summaries And On-Demand Bodies

Task-document scans still share the short TTL parse cache, and the always-on task and series surfaces
project **every** canonical task document — the newest bounded window of 250 nodes each was removed by
260916-TDPU, so no summary bound remains (see that entry in the Update History and the rationale at
`snapshots_impl/_common.py:65-71`). The summary surfaces still omit reader bodies; `_task_doc_node`
computes `bodyRevision` from the omitted fields and receives an explicit `include_body` choice.
Lifecycle binding was factored into `_TaskDocumentLifecycleMaps` so summary and on-demand paths resolve
the same runtime context.

Since 260731-EFA-L2 that map arrives **whole**: `_task_doc_node(doc, path, maps, now, *,
include_body)` takes the `_TaskDocumentLifecycleMaps` and calls `_task_doc_lifecycle_id` itself,
rather than receiving a pre-computed `lifecycle_id` beside a bare `lifecycle_by_dir`. The doc's own
lifecycle id and its cross-folder link resolution are two reads of the same index, and passing the
id separately let the two callers (`read_task_documents`, `read_task_document_body`) disagree.
Both call sites shrank to one line each as a result.

`read_task_document_body` accepts a projected `docPath`, resolves candidates, requires the final path
to be a real file under `coordination_root/tasks` (including after symlink resolution), validates the
task-document schema, and returns the full node. This confinement is necessary because the HTTP
endpoint accepts a client-provided path. The summary window no longer truncates at all — its 250-node
bound was removed by 260916-TDPU, so every canonical task document is projected (see the Update
History); the summary surfaces still carry full per-document step/sub-task lists, which is an accepted
round-1 N4 follow-up, not a claim of completion in L13.

### 260707-HFX2-L12 CS-6 Update

Snapshot readers gained three CS-6 hot-path bounds: one directory scan + one read per gate log per
tick, task and series document readers share a short TTL task-json cache, and engine-process git
status probes are TTL-cached and pruned to live leaf contracts. (The gate half of this originally
read `compact_current()` with the physical rewrite throttled by `GATE_COMPACT_TTL_SECONDS`. **The
single read survived L5; the throttled rewrite did not** — both the constant and the
`_last_gate_compact` dict it keyed are deleted, and this module now rewrites nothing at all. See the
L5 section below.)

### 260731-EFA-L5: this module no longer writes, and reads that only render read tolerantly

Two readers changed, and the rule underneath them is worth stating before either:

> **Every rewrite of an authority-bearing log reads strictly**, and the tolerant reader this module
> takes never drives a rewrite. That is what makes it impossible for a compaction to erase an
> authority record it could not parse: each of the three strict stores — gate, expectation rows,
> operator inbox — drives its rewrites from its own strict `read`, which raises on a torn line, so
> the rewrite never happens; the tolerant read used here skips the line, and nothing it returns is
> ever written back on this route, so the skip lasts exactly one tick.
>
> **Do not generalise that to all six.** The other three — `AttentionDismissalStore.dismiss` /
> `_prune_locked`, `OrchestrationNudgeStore.compact`, `AgentNotifierSignalCooldownStore._compact_locked`
> — rewrite from the list their *tolerant* `read()` produced, so a row that read could not parse is
> absent from what the rewrite writes back: those three drop it **permanently**, not for one tick.
> That is acceptable only because none of the three carries authority, and it stops being acceptable
> the moment one does.

**`read_gates` stopped compacting.** `GATE_COMPACT_TTL_SECONDS` and the module-level
`_last_gate_compact: dict[str, datetime]` are gone, and the body is now one call —
`store.projected_current(lifecycle_id, now=now)` — per lifecycle log. The old path called
`GateStore.compact_current(..., rewrite=prune)`, which physically rewrote every gate log every 30
seconds *from the projection tick*: a whole-file replace performed by the process that owns nothing
about gates, racing the MCP server's appends. That is where the measured 11.50% gate-snapshot loss
came from. **The projection output is unchanged** — `projected_current` applies the same
`gate_keep_ids` keep-filter in memory that `compact_current` applied, so the dashboard renders the
same live gate set; only the on-disk reclamation moved, to `GateStore.compact` in
`mcp/tools/gates.py::_reclaim_gate_log`, in the MCP process. `projected_current` also reads through
the **tolerant** `GateStore.read_for_projection`, so one torn line costs this tick one row instead
of the whole log; the strict `GateStore.read` still backs the enforcement fold and still raises.

**`read_expectation_rows` reads per-row now, and the bug it closes is a trap worth remembering.**
The call was `store.pending()` inside `with contextlib.suppress(OSError, ValueError)`. `pending()`
goes through the strict `ExpectationRowStore.read`, which raises pydantic's `ValidationError` — and
`ValidationError` **subclasses `ValueError`**. So the suppress that looks like it guards file I/O
was swallowing a parse failure and discarding *every* deadline in the file: one torn row, and the
dashboard told an operator that nothing was due. It now calls `pending_for_projection()`, which
folds the same rows over a tolerant per-row read. The suppress stays for the I/O it was written for;
it is no longer load-bearing for a malformed row.

`read_providers(config, *, now)` reads the persisted provider snapshot at
`providers.current_state.current_state_path(config)`, stamps `snapshotStaleSeconds`
from the file's `checkedAt`, and delegates provider-node policy to
`observer.provider_nodes.workspace_provider_nodes`. That helper expands CGC
`resources.watchers` into one workspace-scoped `ProviderNode` per covered repo when
the snapshot carries watcher evidence, and expands providers with explicit
`targetRepos` into repo-scoped nodes. Providers without watcher or target evidence
remain aggregate workspace nodes. The snapshot is call-triggered and stale between
calls, so its age is surfaced, never faked live. A missing or malformed file yields
`[]`.

For admitted worktree stacks, `_worktree_providers` reads each group's static
`provider-runtime/provider-state.json`, but now follows the recorded isolated provider
settings path to discover expected CGC/GrepAI container names and inspects Docker for
their live state. Batch inspect is attempted first, then per-container inspect lets
missing containers be represented as failed/degraded facts instead of losing the whole
worktree provider row. If Docker itself is unavailable or times out, runtime summary
is intentionally omitted and the provider remains configured-only; this failure
containment is necessary because Docker control-plane access is outside the observer's
durable file surfaces. Task 29 adds the `active_worktree_groups` gate: source/workspace
providers still project from the workspace current-state snapshot, but worktree provider-state
files are ignored when the projection store supplies an active-group filter and their group was not
admitted from active enclosure + lifecycle state. Direct reader calls that omit the filter preserve the
full file-surface read used by lower-level tests and diagnostics.

`read_enclosures(coordination_root, *, contracts=None)` maps each active leaf
`enclosures/<leaf-id>/series-contract.md` to an `EnclosureNode` — since 260712-PTS-L2 the parsed
contracts come from the shared per-tick `ContractSnapshot` when the projection passes one (a
standalone call builds a local snapshot; the snapshot builder owns the
`iter_leaf_enclosure_contracts` walk + `load_contract` parse). Root `series-contract.md` files
represent integration branches and are not live worktree
processes; `0_archive/` is excluded. A malformed contract is skipped (`ContractError`/`OSError`), never
fatal to the whole projection. Since L11 `_enclosure_from_contract` also stats the worktree paths at
snapshot time — `codeWorktreeExists = contract.code_worktree.exists()` and `memoryWorktreeExists =
contract.memory_worktree.exists()` (or `False` with no memory worktree) — the same probes
`status_payload` uses, so the projection carries physical worktree-existence truth for the tasks
surface's visibility rule instead of clients inferring liveness from `cleanup` state.

The **slice-3b analytical readers** add the cockpit's charts/feeds, each cheap and
reusing a producer's parser: `read_drift_snapshots(coordination_root, *, now)`
reads the persisted `ar-drift-snapshot/v1` JSON the memory_quality run writes
(`logs/observer/drift/*.json`) with a `snapshotStaleSeconds` age — the reducer
never re-classifies drift (that is git-per-sidecar). Task 29 carries through
`checkedAt`, `sourceRoot`, `memoryRoot`, and `reportPath` from that snapshot so actionable-drift rows
can show concrete provenance and use the snapshot time as their one-shot dismissal anchor.
`read_sidecar_staleness`
(git-free) parses each supported sidecar's `lastVerifiedCommitDate` via the drift
package's `discover_onboarding_files` + `parse_table_metadata`;
`read_setup_summaries` reads `logs/providers/setup/last-*.json` (skipping the
`-full` debug copies); `read_setup_progress_nodes` projects each worktree group's
`provider-runtime/setup-progress.json` through the producer's own `progress_status`
(so a stale heartbeat reads `stale`) and, when supplied, filters to admitted active worktree
groups; `read_route_coverage` reads each
`overview.index.json`'s `coverageCounts`; `read_tool_reports` lists the newest
report per `temp/tool-reports/<tool>/`; and `read_ledger(memory_root)` returns the
ledger closeout **count + currency** (rows carry no timestamps, so no time series).
`read_task_documents` (slice 3c) reads every active `ar-task-document/v1` JSON, skipping `0_archive/`
and `enclosures/`, into a selectable `TaskDocNode` (surface 7). `lifecycleId` is optional runtime
context, not the admission ticket: light/subTask docs use their direct `lifecycleId`, a matching
`enclosures[].enclosurePath`, or — the L10 repair — a **case-insensitive** join of the same task
root's served enclosure `leafId` against the doc's own authored `id` (with the filename stem kept as a
legacy alternative). The case fold matters because enclosure leaf ids are slugified lowercase
directory names (`260628-l7`) while doc ids are authored uppercase labels (`260628-L7`), and series
leaf docs carry no `enclosures[]` refs in practice; suffixed reopen enclosures (`…-r1`) deliberately
do not bind here and stay a sidebar admission. Planning docs still project before an
enclosure exists. Master docs project here too; a leaf `series-contract.md` is enclosure state, not task
reader content.
Small coercion helpers (`_as_int`/`_as_float`/`_text_or_none`/`_report_label`/
`_file_age_seconds`/`_current_phase_text`) keep each reader resilient and short.

**Slice-05 (5c)** widened two readers for the cockpit's real model. `read_providers` now also reads
**surface 4** — each worktree group's `provider-runtime/provider-state.json` via `_worktree_providers`
(the workspace read split into `_workspace_providers`) — emitting the isolated CGC/GrepAI engines bound
to their worktree group + repo + role, so the engine room shows each worktree's own stack, not just
main's. Task 12 S2 moves the provider-node construction into `provider_nodes.py`: workspace CGC
current-state watcher rows become repo-scoped provider nodes, and GrepAI `targetRepos` become
repo-scoped memory provider nodes when current state carries configured repo targets. GrepAI remains one
aggregate provider instance; the split is a topology projection of addressable project targets.
Task 31 extends the worktree side from static inventory to live-enough runtime truth:
`isolatedProviderSettings.path` is read to derive the expected provider containers, and
Docker inspect classifies them as ready/degraded/failed when available. The reader still
does not start or repair providers.
`read_task_documents` now carries the **full task content** (objective /
requirements / design / steps+substeps / codeExamples / decisions / openQuestions / references) into
`TaskDocNode`, so the dashboard is the task reader — the JSON content is read in the UI, never the
filesystem. Since L14 `_task_doc_node` also copies `doc.orchestrates` (as a fresh list) onto
`TaskDocNode.orchestrates` — the orchestration-command relation the dashboard nests masters by;
docs without the field project `[]`.

**Slice-5e** added two Engine Room readers. `read_engine_process_facts(coordination_root, *, active_worktree_groups=None, now=None, landing_state=None, contracts=None)` reads the
*same* active leaf enclosure contracts as `read_enclosures` (since 260712-PTS-L2 via the same shared
per-tick `ContractSnapshot`, so it adds no contract parses of its own), but instead of the structural `EnclosureNode`
it builds an `EngineProcessFacts` bundle per contract carrying the status-guidance facts the map needs:
`contract_payload(contract)` (code/memory branches, base commits, worktree paths) and
`dict(lifecycle_guidance(contract))` — both pure — plus `status` from `_safe_status_payload`.
Since 260731-EFA-L4 the guidance payload is **widened at the boundary** with an explicit `dict(...)`
cit:(["def read_engine_process_facts("], mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:240-240): `read_engine_process_facts`
constructs `EngineProcessFacts` with a plain dictionary guidance payload. The same
widening is applied to the cached local status in cit:(["def _cached_local_status(  # pragma: no cover"], mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:384-384), where the
annotation `value: dict[str, Any] | None` is now declared before the `try` so the `except` branch's
`None` and the success branch's `dict(projected_status_payload(...))` share one type. Neither change
alters a served value. `status_payload`
is the **only** git-touching part, so it is wrapped best-effort: a contract pointing at an absent, dirty,
or fake worktree degrades to `status=None` (rendered as missing/derived) instead of crashing the
projection tick; a malformed contract is skipped (`ContractError`/`OSError`), never fatal. Task 29
lets the projection store pass active non-terminal enclosure groups so the reader does not git/status
probe historical contracts before the reducer would drop or hide them.
`read_start_progress_entries(coordination_root, *, now)` (§5.4) reads the transient
`temp/worktree-start/<repo>/<worktree>.json` blocks `start.py` writes when a worktree start blocks
*before* writing its contract — via the producer's own `read_start_progress` — and stamps each with its
heartbeat `ageSeconds`. A start that reached its contract has cleared this file, so these are exactly the
gated starts the contract-keyed enclosure/fact surfaces cannot see.

**Slice-5h** adds the coupler-popover ledger window. `read_ledger(memory_root)` now also surfaces the
newest `LEDGER_WINDOW` (25) rows on `LedgerNode.rows` for the OFFICIAL coupler (`closeoutCount` stays the
full total). `_ledger_window(ledger_path)` is the WORKTREE-coupler counterpart: best-effort (like
`status_payload`) it loads the worktree's own `memory.md` via `load_ledger`, windows to `LEDGER_WINDOW`, and
returns `(rows, total)`; `read_engine_process_facts` calls it per contract and carries the result on
`EngineProcessFacts.ledger_rows`/`ledger_row_count`, so the windowing is done in the I/O layer and the
reducer stays a pure fold. A missing/invalid/unreadable ledger degrades to `([], 0)`, never a failed tick.

**Slice-5h Tier 2** enriches each served row with its per-side commit message + committer date so the popover
reads as a story, not bare hashes. `_git_commit_meta(repo_root, commits)` is the batched probe — ONE
`run_git` `git log --no-walk --ignore-missing --format=%H\x1f%cI\x1f%s <commits…>` per repo (never one
subprocess per commit; the window is 25), mapping each resolvable full hash → `(committer_iso_date, subject)`.
Since 260731-EFA-L3 that `run_git` is imported from `agents_remember.kernel.git_command` — the package's
single runner — rather than from `worktrees.modules.git`, which was one of six near-identical private
copies. The call site is unchanged, but the probe now runs with the `GIT_DIR`-family selectors stripped
(an inherited `GIT_DIR` would have made this reader describe commits from whatever repository that
variable named, not the worktree's own) and under the runner's `GIT_LOCAL_TIMEOUT_SECONDS` (300) default;
the retired copy carried no timeout at all, so a wedged `git log` could hold a projection tick forever.

**Gaining a timeout is what forced the handler to widen.** The guard around the probe is
`except (OSError, subprocess.SubprocessError)` cit:(["def _git_commit_meta("], mcp/src/agents_remember/serving/projections/snapshots_impl/_analytics.py:327-327), not the `except OSError` it was before this
leaf. `subprocess.TimeoutExpired` is a `SubprocessError` and `SubprocessError` is **not** a subclass
of `OSError`, so the moment the call moved onto a runner that has a bound, the bound's own exception
became something the old handler could not see. It would have escaped `_git_commit_meta` through
`_enrich_ledger_rows` and failed the whole projection tick — precisely the promise both entry points
make: `_ledger_window`'s "best-effort … so the projection tick never fails" and the `LedgerNode`
builder in `read_ledger`. The degrade is hash-only rows, never an exception, and
The production best-effort metadata boundary is `_git_commit_meta` (mcp/src/agents_remember/serving/projections/snapshots_impl/_analytics.py:327-362).
The former timeout-injection regression suite was retired; no current test execution is asserted.

It returns `{}` on any failure (no repo path / git absent / non-zero exit / a raise from the runner),
and `--ignore-missing` drops a
non-local SHA with **no HEAD fallback** — so a commit absent from the local repo simply has no entry (never
faked). `_enrich_ledger_rows(rows, *, code_root, memory_root)` runs one probe per side and builds the served
`LedgerRefNode`s (prefix-tolerant lookup via `_commit_meta_for`); a row whose commit isn't local keeps only
its hash. Both windowing sites now pass the repo roots: `_ledger_window(ledger_path,
code_root=cp["code_worktree"], memory_root=cp["memory_worktree"])` (worktree coupler) and
`read_ledger(memory_root, code_root=scope.path)` (official coupler). The metadata fields are optional and
dumped `exclude_none=True`, so an unprobed side is omitted from the wire.

**Slice 3c reopened (R1) — masters surface.** `read_series_documents(coordination_root, *, now)` is the
master aggregation companion to `read_task_documents`: it globs the *same* `tasks/*/*/*.json`, selects
`kind == "master"`, and keys each by its task **folder** (`path.parent.name`), building a `SeriesNode`.
Master docs are also projected by `read_task_documents` so Operations can select and render the concrete
master document; `_task_doc_node` copies the JSON document `id` into `TaskDocNode.id` so authored leaf
labels can use the child task's own number instead of parent fallback labels. `SeriesNode` remains the
folder-keyed checklist surface. `doneCount`/`totalCount` come
from `series_done`/`series_total` over the master's declared `subTasks[]` (each subtask is one checkbox;
`status == "Completed"` is the lever, **authoritative** over a slice's own leaf steps — a slice marked done
with open internal boxes still counts done). It carries the full master render (objective + subTasks +
sections + decisions) so older clients can keep using the series reader. `_series_subtask_nodes` resolves
each master `subTasks[].file` to a sibling leaf JSON and reads that leaf's `createdAt`; when every row has
a structured creation time, rows are sorted oldest-first with original index as the tie-breaker. If any
row lacks a resolvable leaf timestamp, authored master order is preserved, because parsing numeric
prefixes from task filenames would make the projection guess. Resilient like its peers (missing dir →
`[]`; malformed JSON / non-master / validation error → skip).

**Slice-6c** added `read_gates(coordination_root)` — every lifecycle's current
(folded) gate set plus the workspace log, read from the `GateStore` co-located with
the event store under `observer_logs_root` and folded by id (last-wins), so the
projection sees live gate state with no event machinery. A malformed log is skipped
(`OSError`/`ValueError`), never fatal; wired into `project_workspace` via
`projection_store` for the reducer's `_attach_gates` / `_gate_attention`.

**Task 23/24 interaction retention** extended this surface. `read_gates(coordination_root, *, now=...)`
applies the interaction keep-filter before projecting, so untouched open/terminal interaction gates
cannot sit in the dashboard forever. (Until 260731-EFA-L5 it also *compacted* the log on a 30s
cadence from this tick; it no longer writes anything — the filter is applied in memory by
`GateStore.projected_current` and the physical prune belongs to the MCP process. `now=None` folds
without the retention filter at all, which is what a caller holding no clock has always been given.)
`read_agent_pickups(coordination_root, *, now)`
projects pending operator-inbox responses as `AgentPickupNode`s for task-row feedback: fresh pending
entries show `waiting-for-agent`, entries older than the 5-minute pickup TTL show `check-chat`, L3
metadata (sender/recipient roles, message kind, artifact path, delivery state/session/detail) is carried
through from the inbox row, and consumed/dismissed/24h-expired entries disappear because the inbox store
physically removes them. Since 260707-HFX2-L1, `read_agent_pickups` also carries the R1 ack/backoff
fields (`attemptCount`/`lastAttemptAt`/`nextAttemptAt`/`escalatedAt`) and the R4 owner fields
(`ownerRole`/`ownerAgentId`/`ownerLifecycleId`) straight off the entry. A new
`read_expectation_rows(coordination_root, *, now)` (R5) reads
`ExpectationRowStore.pending_for_projection()` (L5 — the tolerant per-row reader; it was `pending()`
and that cost the whole file on one torn line), computes an `overdue` flag per row
(`now >= dueAt`), and returns `ExpectationRowNode`s sorted by
`dueAt` — surfacing only, for dashboard/architect observability; an L2 predicate reads the store
directly and never this projection.

**Attention dismissals are read elsewhere, and this module no longer has a reader for them.**
Task 28 S5.2 added `read_attention_dismissals(coordination_root)` here, returning the compact
`{itemId: AttentionDismissalRecord}` acknowledgement map. 260731-EFA-L5 deleted it, along with the
`AttentionDismissalRecord`/`AttentionDismissalStore` imports that existed only to serve it: it never
had a caller. Nothing in `agents_remember` and nothing in the suite ever reached it, at the leaf's
base commit `e52edaf5` included — the projection builds its dismissal view directly, in
`ProjectionInputState._refresh_workspace` (`projection_inputs.py`), which calls
`AttentionDismissalStore(observer_root).current()` itself and hands the map to the reducer's
`AnalyticalInputs.attention_dismissals`. The proof it was unreachable rather than merely
uncalled-by-grep: narrowing the function's `contextlib.suppress(OSError, ValueError)` put its `with`
statement under the 100% changed-lines floor and the gate reported it uncovered under the full
suite. Task 29's targetless actionable-drift records still reach the map; they always did so through
the store, never through this reader.

**Series-contract leaf binding** reshaped `read_task_documents`: it builds maps from served enclosure path
to lifecycle id, from root master task folders to root lifecycle ids, and from `(taskRoot, leafId)` to
lifecycle id. Non-master JSON docs bind through direct `lifecycleId`, `enclosures[].enclosurePath`, or the
task-root + filename/`leafId` match when available; master JSON docs bind only to a structurally root
lifecycle when the enclosure lifecycle id equals the task id/name. No binding is required for projection.
The file iterator is recursive but excludes `0_archive/` and `enclosures/`, so nested active task folders
work while archived roots and contract folders stay out of the JSON scan.

### 260712-TRH-L7 landing merge boundary

Snapshot readers merge the refresher's immutable fact for each contract inside the contract-local status boundary. If the landing reader is invalid, the local status remains available and the landing detail is omitted with a warning rather than freezing the whole tick or inventing success.

## Invariants And Boundaries

- **Reuse, don't re-parse:** providers come through `current_state`, contracts
  through `load_contract` — one parser per surface, owned by its producer. Since 260712-PTS-L2 the
  contract parse itself happens at most once per projection tick: the enclosure and engine-facts
  readers consume the shared `ContractSnapshot` the projection injects, and only build their own
  when called standalone.
- **Injected contracts are shared, immutable state:** the `WorktreeContract` instances inside a
  passed `ContractSnapshot` are cached across ticks — a reader that mutated one would corrupt every
  later tick. Readers only read.
- **Resilient reads:** a missing/malformed surface degrades to empty/skip; one
  bad file never breaks the whole projection.
- File I/O lives here at the call edge; the reducer fold stays pure.
- **Attention acknowledgements are current state, and are not read here.** They are compact
  lifecycle-scoped acknowledgement records rather than append-only suppression history, and since
  260731-EFA-L5 the only reader is `projection_inputs.py`, which goes to `AttentionDismissalStore`
  directly. This module's `read_attention_dismissals` was deleted with its imports because it never
  had a caller; do not reinstate a call-edge helper here for a store the projection already reads.
- **Drift is read, never classified here:** the reducer reads the persisted drift
  snapshot (cheap, staleness-stamped); the git-per-sidecar classification stays in
  the on-demand `drift_check`/`memory_quality_check` tools (slice 3b, b1).
- **Git is best-effort at the call edge (5e):** only `status_payload` touches git;
  `read_engine_process_facts` routes it through `_safe_status_payload`, so one
  worktree's broken/absent git state yields `status=None`, never a failed tick.
  `contract_payload` and `lifecycle_guidance` are pure and always populated.
- **Git in this module goes through the one runner:** `_git_commit_meta` (the ledger-window
  probe, 5h Tier 2) calls `kernel.git_command.run_git`, never `subprocess` directly, so it
  cannot be redirected by an inherited `GIT_DIR` and cannot run unbounded. Anything added
  here that needs git uses the same runner — a private copy is what the single-runner test
  (`test_only_the_kernel_module_defines_a_git_runner`) forbids.
- **A bounded runner raises `SubprocessError`, so catch it:** any git call here must guard
  `(OSError, subprocess.SubprocessError)`, not `OSError` alone. `subprocess.TimeoutExpired` is a
  `SubprocessError` and is *not* an `OSError`, so an `OSError`-only handler leaks the timeout the
  runner exists to impose. That leak would land on `_enrich_ledger_rows` and fail the tick, which
  is the one thing `_ledger_window` and `read_ledger` both promise cannot happen.
- **Worktree runtime readers are admission-gated when called by projection:** workspace providers remain
  always-on, while worktree providers/setup progress require strict provider admission and engine
  process facts require a broader non-terminal active-enclosure group.
- **Pre-contract starts are a distinct surface (§5.4):** `read_start_progress_entries`
  reads the transient `temp/worktree-start/` blocks — the only view of a start gated
  before its contract exists; once the contract lands the file is cleared.
- **Task-document existence is archive/delete based:** active JSON-primary task docs project regardless
  of lifecycle binding or terminal status. Moving a task doc under `0_archive/` or deleting it is what
  removes it from Operations; completed/abandoned status is filter/history state, not disappearance.
- **There is no task-document summary bound (260916-TDPU):** `TASK_DOCUMENT_SUMMARY_LIMIT`,
  `SERIES_DOCUMENT_SUMMARY_LIMIT`, `_bounded_task_document_payloads` and `_stat_mtime_ns` are gone, so
  the readers project every canonical document they enumerate — no window, no eviction, no truncation
  flag. Reintroducing a bound requires a larger one that announces its own truncation and offers a way
  to reach what it hid (`snapshots_impl/_common.py:65-71`); a silent cap is what this removal exists to
  end.
- **Masters have two surfaces:** `read_task_documents` projects the concrete active master document for
  direct Operations selection, while `read_series_documents` also projects the folder-keyed checklist
  aggregation. Series progress reads the master's *declared* `subTasks[]` status, never a slice's leaf
  steps. Contracts are not projected as task documents.
- **Creation order comes from leaf task docs, not names:** series rows sort by resolved leaf `createdAt`
  only when every row has it; otherwise the reader preserves the master-authored sub-task order.
- **Interactions are TTL-bound, but this module does not do the bounding:** the gate reader applies
  the retention keep-filter in memory and returns a filtered view; the physical reclamation lives in
  the log's owner process. Durable task docs, contracts, and ledger rows remain separate
  work-record surfaces.
- **No reader on this route rewrites a control-plane log (260731-EFA-L5).** This is the projection
  tick; it runs in the dashboard, and the dashboard owns none of the gate logs. A rewrite added back
  here is a whole-file replace racing the MCP server's appends — the defect that cost 11.50% of gate
  snapshots at the base commit — and the `applied` marker it can drop is what stops one human
  approval being consumed twice. Reclamation belongs to the process that owns the log.
- **A reader here that only renders must read tolerantly; anything that decides, or rewrites a log
  that carries authority, must read strictly.** Exactly two of the six stores offer both readers,
  and they are the two this module consumes: `GateStore.read` / `read_for_projection` and
  `ExpectationRowStore.read` / `read_for_projection`. `OperatorInboxStore` is strict only.
  Attention dismissals, orchestration nudges and supervisor signals are tolerant only — their single
  `read` is the tolerant one, and it drives their rewrites, so those three drop an unparseable row
  permanently. That is safe only because none of the three carries authority.
  This module is a rendering surface, so it takes the tolerant half — but note the direction of the
  danger: the strict half raises `pydantic.ValidationError`, which **subclasses `ValueError`**, so a
  `contextlib.suppress(OSError, ValueError)` around a strict read does not degrade one row, it
  discards the whole file silently. That is exactly what `read_expectation_rows` was doing.

## Evidence

### Repo-Internal References

- `read_task_documents` projects all active task docs, with optional lifecycle attachment for leaves and root masters (`_task_document_lifecycle_maps` + `_task_doc_node(..., include_body=False)`). [1]
- `read_series_documents` selects `kind == "master"` docs and builds the folder-keyed `SeriesNode` aggregation (`seriesId` = the task folder, `doneCount`/`totalCount` from the declared `subTasks`, plus `ageSeconds`). [2]
- Series sub-task rows resolve sibling leaf JSON `createdAt` values (`_series_subtask_nodes` + `_series_subtask_created_at`) and sort oldest-first only when every row has one. [3]
- Lifecycle task docs now carry their JSON-primary `createdAt` timestamp (`_task_doc_node`, `createdAt=doc.createdAt`). [4]
- Every one of these task-document parse sites now reads through the one tolerant `_projected_document`, so an unknown key written by a newer build no longer deletes the whole document; every other validation failure still withholds it. [5]
- The projection nodes these readers build, including optional `TaskDocNode.lifecycleId`, `TaskDocNode.createdAt`, `SeriesSubTaskNode.createdAt`, and `SeriesNode.objective`. [6]
- The provider current-state path + snapshot shape (surface 1). [7]
- The provider-node projection policy used by `read_providers`. [8]
- Worktree provider readers derive isolated provider container names (`_worktree_providers` → `_worktree_runtime_specs`), inspect Docker (`_inspect_containers`), and convert observed runtime into ready/degraded/failed summaries (`_worktree_runtime_summary`). [9]
- `read_providers` always reads workspace providers and filters worktree provider-state files by admitted active groups (`if active_worktree_groups is not None and group not in active_worktree_groups: continue`). [10]
- `read_engine_process_facts` accepts an `active_worktree_groups` filter and skips a non-admitted group before the derived payload is built. [11]
- `read_enclosures` and `read_engine_process_facts` take the keyword-only `contracts` snapshot; `contracts=None` builds a local one-shot snapshot via `build_contract_snapshot`. [12]
- The shared per-tick contract snapshot + stat-identity parse cache these readers consume. [13]

| `read_setup_progress_nodes` accepts the same active worktree-group filter used by provider setup projection. | "def read_setup_progress_nodes(  # pragma: no cover" | mcp/src/agents_remember/serving/projections/snapshots_impl/_analytics.py:188-188 |
| `read_drift_snapshots` carries `checkedAt`/`sourceRoot`/`memoryRoot`/`reportPath` provenance from the persisted snapshot. | "def read_drift_snapshots(coordination_root: Path" | mcp/src/agents_remember/serving/projections/snapshots_impl/_analytics.py:79-79 |
| `_git_commit_meta` is this module's only git call, runs on the package's one runner, `kernel.git_command.run_git`, and guards it with `except (OSError, subprocess.SubprocessError)` so the runner's own `TimeoutExpired` cannot escape. | "def _git_commit_meta(" | mcp/src/agents_remember/serving/projections/snapshots_impl/_analytics.py:327-327 |
| That runner strips the `GIT_DIR`-family selectors, adds `safe.directory`, DEVNULLs stdin, and bounds the call at `GIT_LOCAL_TIMEOUT_SECONDS` (300) by default — the bound whose `subprocess.TimeoutExpired` the widened guard above exists to absorb. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:85-151 |
| Failed Git metadata probing returns an empty metadata map so ledger rows can retain their hashes without fabricated date or subject. | `_git_commit_meta` | mcp/src/agents_remember/serving/projections/snapshots_impl/_analytics.py:327-362 |

| The worktree contract loader + fields (surfaces 5/6). | `WorktreeContract` | mcp/src/agents_remember/worktrees/worktree_contract.py:230-285 |
| The setup-progress projection (`progress_status`) reused for surface 3. | `progress_status` | mcp/src/agents_remember/providers/setup_progress.py:200-225 |
| The memory ledger loader read for surface 8. | `load_ledger` | mcp/src/agents_remember/kernel/memory_ledger.py:187-190; mcp/src/agents_remember/kernel/memory_ledger.py:215-215; mcp/src/agents_remember/kernel/memory_ledger.py:221-221 |
| The data-surface inventory the structural/analytical split follows. | `# Observable Lifecycle, Events, and Gates — the Agents Remember 3.0 Design` | docs/design/observable-lifecycle.md:1-402 |
| The gate reader's two halves: the tolerant `read_for_projection` this module now uses, and `projected_current`, which folds + keep-filters from that one read and rewrites nothing (`now=None` folds without the retention filter). | `projected_current` | mcp/src/agents_remember/controlplane/store.py:279-300 |
| The expectation-row reader's two halves: the tolerant `read_for_projection` and the `pending_for_projection` wrapper `read_expectation_rows` calls; the docstring names this module's `suppress`-plus-strict-read defect as the reason it exists. | `read_for_projection`; `pending_for_projection` | mcp/src/agents_remember/controlplane/expectation_rows.py:191-209; mcp/src/agents_remember/controlplane/expectation_rows.py:221-223; mcp/src/agents_remember/controlplane/expectation_rows.py:226-226 |
| Where the gate-log rewrite went: reclamation in the log's owner process, guarded by a non-raising ownership question and run on terminal decisions. | `_reclaim_gate_log` | mcp/src/agents_remember/controlplane/gate_decisions.py:74-80 |

## 260727-CHATS-IM-L2 Current Delta

Task and series readers now share `TaskDocumentPayloadCache`, which enumerates the live set but
reparses only changed/new stat identities and removes deleted entries. The new
`refresh_engine_process_landing` updates only the volatile landing tail of retained Engine Room
facts on heartbeat ticks.
