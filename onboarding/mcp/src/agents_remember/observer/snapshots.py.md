# mcp/src/agents_remember/observer/snapshots.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/snapshots.py`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `2dea095cd68454a7a68893e37c07dbd8daa86d32`       |
| lastVerifiedCommitDate | 2026-08-09T18:00:39+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[observer overview](overview.md)

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

### 260707-HFX2-L13 Bounded Task Summaries And On-Demand Bodies

Task-document scans still share the short TTL parse cache, but the always-on task and series surfaces
now take the newest bounded window (250 nodes each) and omit reader bodies. `_task_doc_node` computes
`bodyRevision` from the omitted fields and receives an explicit `include_body` choice. Lifecycle
binding was factored into `_TaskDocumentLifecycleMaps` so summary and on-demand paths resolve the same
runtime context.

Since 260731-EFA-L2 that map arrives **whole**: `_task_doc_node(doc, path, maps, now, *,
include_body)` takes the `_TaskDocumentLifecycleMaps` and calls `_task_doc_lifecycle_id` itself,
rather than receiving a pre-computed `lifecycle_id` beside a bare `lifecycle_by_dir`. The doc's own
lifecycle id and its cross-folder link resolution are two reads of the same index, and passing the
id separately let the two callers (`read_task_documents`, `read_task_document_body`) disagree.
Both call sites shrank to one line each as a result.

`read_task_document_body` accepts a projected `docPath`, resolves candidates, requires the final path
to be a real file under `coordination_root/tasks` (including after symlink resolution), validates the
task-document schema, and returns the full node. This confinement is necessary because the HTTP
endpoint accepts a client-provided path. The summary window currently truncates silently and still
carries full per-document step/sub-task lists; those are accepted round-1 N4 follow-ups, not claims of
completion in L13.

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
cit:(["def read_engine_process_facts("], mcp/src/agents_remember/observer/snapshots_impl/_runtime.py:236-236): `read_engine_process_facts`
constructs `EngineProcessFacts` with a plain dictionary guidance payload. The same
widening is applied to the cached local status in cit:(["def _cached_local_status(  # pragma: no cover"], mcp/src/agents_remember/observer/snapshots_impl/_runtime.py:383-383), where the
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
`except (OSError, subprocess.SubprocessError)` cit:(["def _git_commit_meta("], mcp/src/agents_remember/observer/snapshots_impl/_analytics.py:334-334), not the `except OSError` it was before this
leaf. `subprocess.TimeoutExpired` is a `SubprocessError` and `SubprocessError` is **not** a subclass
of `OSError`, so the moment the call moved onto a runner that has a bound, the bound's own exception
became something the old handler could not see. It would have escaped `_git_commit_meta` through
`_enrich_ledger_rows` and failed the whole projection tick — precisely the promise both entry points
make: `_ledger_window`'s "best-effort … so the projection tick never fails" and the `LedgerNode`
builder in `read_ledger`. The degrade is hash-only rows, never an exception, and
`test_observer_projection.py::LedgerCommitMetaTests::test_a_wedged_git_log_degrades_to_hash_only_rows_instead_of_failing_the_tick`
cit:([`test_a_wedged_git_log_degrades_to_hash_only_rows_instead_of_failing_the_tick`], mcp/tests/test_observer_projection_ledger.py:171-197) drives **both** paths through a patched `run_git` that raises `TimeoutExpired`.

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
  Attention dismissals, orchestration nudges and agent-notifier signals are tolerant only — their single
  `read` is the tolerant one, and it drives their rewrites, so those three drop an unparseable row
  permanently. That is safe only because none of the three carries authority.
  This module is a rendering surface, so it takes the tolerant half — but note the direction of the
  danger: the strict half raises `pydantic.ValidationError`, which **subclasses `ValueError`**, so a
  `contextlib.suppress(OSError, ValueError)` around a strict read does not degrade one row, it
  discards the whole file silently. That is exactly what `read_expectation_rows` was doing.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `read_task_documents` projects all active task docs, with optional lifecycle attachment for leaves and root masters (`_task_document_lifecycle_maps` + `_task_doc_node(..., include_body=False)`). | "def _task_document_lifecycle_maps(enclosures: list[EnclosureNode]) -> _TaskDocumentLifecycleMaps:"; "def _task_doc_node(" | mcp/src/agents_remember/observer/snapshots_impl/_task_documents.py:113-113; mcp/src/agents_remember/observer/snapshots_impl/_task_documents.py:296-296 |
| `read_series_documents` selects `kind == "master"` docs and builds the folder-keyed `SeriesNode` aggregation (`seriesId` = the task folder, `doneCount`/`totalCount` from the declared `subTasks`, plus `ageSeconds`). | "def read_series_documents(" | mcp/src/agents_remember/observer/snapshots_impl/_task_documents.py:174-174 |
| Series sub-task rows resolve sibling leaf JSON `createdAt` values (`_series_subtask_nodes` + `_series_subtask_created_at`) and sort oldest-first only when every row has one. | "def _series_subtask_nodes(path: Path, doc: TaskDocument) -> list[SeriesSubTaskNode]:"; "def _series_subtask_created_at(base_dir: Path, ref_file: str) -> s" | mcp/src/agents_remember/observer/snapshots_impl/_task_documents.py:220-220; mcp/src/agents_remember/observer/snapshots_impl/_task_documents.py:241-241 |
| Lifecycle task docs now carry their JSON-primary `createdAt` timestamp (`_task_doc_node`, `createdAt=doc.createdAt`). | "def _task_doc_node(" | mcp/src/agents_remember/observer/snapshots_impl/_task_documents.py:296-296 |
| The projection nodes these readers build, including optional `TaskDocNode.lifecycleId`, `TaskDocNode.createdAt`, `SeriesSubTaskNode.createdAt`, and `SeriesNode.objective`. | `TaskDocNode`; `SeriesSubTaskNode`; `SeriesNode` | mcp/src/agents_remember/observer/projection.py:608-654; mcp/src/agents_remember/observer/projection.py:657-672; mcp/src/agents_remember/observer/projection.py:685-711 |
| The provider current-state path + snapshot shape (surface 1). | `current_state_path` | mcp/src/agents_remember/providers/current_state.py:52-62 |
| The provider-node projection policy used by `read_providers`. | `read_providers` | mcp/src/agents_remember/observer/snapshots.py:163-181 |
| Worktree provider readers derive isolated provider container names (`_worktree_providers` → `_worktree_runtime_specs`), inspect Docker (`_inspect_containers`), and convert observed runtime into ready/degraded/failed summaries (`_worktree_runtime_summary`). | `_worktree_providers` | mcp/src/agents_remember/observer/snapshots.py:199-259 |
| `read_providers` always reads workspace providers and filters worktree provider-state files by admitted active groups (`if active_worktree_groups is not None and group not in active_worktree_groups: continue`). | `read_providers` | mcp/src/agents_remember/observer/snapshots.py:163-181 |
| `read_engine_process_facts` accepts an `active_worktree_groups` filter and skips a non-admitted group before the derived payload is built. | "def read_engine_process_facts("; "contract.worktree_group.name not in active_worktree_groups"; "cp = contract_payload(contract)" | mcp/src/agents_remember/observer/snapshots_impl/_runtime.py:236-236; mcp/src/agents_remember/observer/snapshots_impl/_runtime.py:264-264; mcp/src/agents_remember/observer/snapshots_impl/_runtime.py:267-267 |
| `read_enclosures` and `read_engine_process_facts` take the keyword-only `contracts` snapshot; `contracts=None` builds a local one-shot snapshot via `build_contract_snapshot`. | "def read_enclosures("; "def read_engine_process_facts(" | mcp/src/agents_remember/observer/snapshots_impl/_runtime.py:59-59; mcp/src/agents_remember/observer/snapshots_impl/_runtime.py:236-236 |
| The shared per-tick contract snapshot + stat-identity parse cache these readers consume. | `ContractSnapshot`; `ContractSnapshotCache` | mcp/src/agents_remember/observer/contract_snapshot.py:37-49; mcp/src/agents_remember/observer/contract_snapshot.py:60-126 |
| PTS-L2 tests pin reader-output parity with and without the shared snapshot and one enumeration per full projection tick. | `test_full_projection_tick_enumerates_once_and_reparses_nothing_unchanged`; `test_reader_outputs_equal_with_and_without_shared_snapshot` | mcp/tests/test_projection_scaling_cs6.py:690-728; mcp/tests/test_projection_scaling_cs6.py:730-761 |
| `read_setup_progress_nodes` accepts the same active worktree-group filter used by provider setup projection. | "def read_setup_progress_nodes(  # pragma: no cover" | mcp/src/agents_remember/observer/snapshots_impl/_analytics.py:192-192 |
| `read_drift_snapshots` carries `checkedAt`/`sourceRoot`/`memoryRoot`/`reportPath` provenance from the persisted snapshot. | "def read_drift_snapshots(coordination_root: Path, *, now: datetime) -> list[DriftSnapshotNode]:" | mcp/src/agents_remember/observer/snapshots_impl/_analytics.py:80-80 |
| `_git_commit_meta` is this module's only git call, runs on the package's one runner, `kernel.git_command.run_git`, and guards it with `except (OSError, subprocess.SubprocessError)` so the runner's own `TimeoutExpired` cannot escape. | "def _git_commit_meta(" | mcp/src/agents_remember/observer/snapshots_impl/_analytics.py:334-334 |
| That runner strips the `GIT_DIR`-family selectors, adds `safe.directory`, DEVNULLs stdin, and bounds the call at `GIT_LOCAL_TIMEOUT_SECONDS` (300) by default — the bound whose `subprocess.TimeoutExpired` the widened guard above exists to absorb. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:85-151 |
| A wedged `git log` degrades both ledger entry points to hash-only rows instead of failing the tick: a patched `run_git` raising `TimeoutExpired` is driven through `_ledger_window` **and** `read_ledger`. | `test_a_wedged_git_log_degrades_to_hash_only_rows_instead_of_failing_the_tick` | mcp/tests/test_observer_projection_ledger.py:171-197 |
| Task 29 tests pin active-group provider admission, parked provider rejection, setup-progress filtering, and engine-process group filtering. | `WorktreeProviderAdmissionTests`; `test_rejects_parked_terminal_and_non_provider_phase_groups`; `test_read_providers_ignores_unadmitted_worktree_stacks`; `test_active_group_filter_skips_parked_progress`; `test_reader_skips_inactive_engine_process_groups_when_filtered` | mcp/tests/test_observer_projection.py:134-242; mcp/tests/test_observer_projection_engine.py:435-464; mcp/tests/test_observer_projection_readers.py:316-330; mcp/tests/test_observer_projection_snapshot.py:296-322 |
| The worktree contract loader + fields (surfaces 5/6). | `WorktreeContract` | mcp/src/agents_remember/worktrees/worktree_contract.py:232-287 |
| The setup-progress projection (`progress_status`) reused for surface 3. | `progress_status` | mcp/src/agents_remember/providers/setup_progress.py:200-225 |
| The memory ledger loader read for surface 8. | `load_ledger` | mcp/src/agents_remember/kernel/memory_ledger.py:187-190 |
| The data-surface inventory the structural/analytical split follows. | `# Observable Lifecycle, Events, and Gates — the Agents Remember 3.0 Design` | docs/design/observable-lifecycle.md:1-402 |
| The gate reader's two halves: the tolerant `read_for_projection` this module now uses, and `projected_current`, which folds + keep-filters from that one read and rewrites nothing (`now=None` folds without the retention filter). | `projected_current` | mcp/src/agents_remember/controlplane/store.py:279-300 |
| The expectation-row reader's two halves: the tolerant `read_for_projection` and the `pending_for_projection` wrapper `read_expectation_rows` calls; the docstring names this module's `suppress`-plus-strict-read defect as the reason it exists. | `read_for_projection`; `pending_for_projection` | mcp/src/agents_remember/controlplane/expectation_rows.py:191-209; mcp/src/agents_remember/controlplane/expectation_rows.py:221-223 |
| Where the gate-log rewrite went: reclamation in the log's owner process, guarded by a non-raising ownership question and run on terminal decisions. | `_reclaim_gate_log` | mcp/src/agents_remember/controlplane/gate_decisions.py:74-80 |

## 260727-CHATS-IM-L2 Current Delta

Task and series readers now share `TaskDocumentPayloadCache`, which enumerates the live set but
reparses only changed/new stat identities and removes deleted entries. The new
`refresh_engine_process_landing` updates only the volatile landing tail of retained Engine Room
facts on heartbeat ticks.

## Update History
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.


- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: now a facade over the `snapshots_impl/` subpackage (`_common`, `_analytics`, `_runtime`, `_task_documents`); full public+private surface re-exported and pinned. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: rebound Engine Room facts and Task 29
  regression references to exact anchors, preserved the filter-before-payload dataflow, removed
  duplicated source ranges, and restored the stale projection-schema history's true L412-L507
  referent as explicitly historical text beside the live per-class definition citations.
- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 23 repeated path:start-end Citation objects from 5 same-claim citation group(s) at card line(s) 417, 419, 425, 426, 439; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0.
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 16 citation claims; scoped result 0 findings.

- 2026-08-01T20:45+02:00 — 260731-EFA-L5 worker: **`read_attention_dismissals` is deleted, together
  with the `AttentionDismissalRecord` / `AttentionDismissalStore` imports that existed only to serve
  it.** It never had a caller. Verified independently before deleting rather than on report: the name
  occurs nowhere in `agents_remember`, nowhere in `mcp/tests`, and nowhere at the leaf's base commit
  `e52edaf5` either (`git grep` over the base tree returns the definition line and nothing else), it
  is absent from `observer/__init__.py`'s `__all__` and from every `from ...snapshots import` list,
  and no dynamic access reaches it — the only `import_module`/`globals()` machinery in the tree is
  the providers' lifecycle packages. The sharper proof is the one this leaf produced by accident:
  narrowing the function's `contextlib.suppress(OSError, ValueError)` made the gate report the `with`
  statement itself uncovered under the full suite, so the body never executed. **The defect was the
  dead function, not the exception tuple inside it**, and the docstring that recorded the narrowing
  attempt went with the function it was about. The projection is unaffected — it never used this
  reader: `ProjectionInputState._refresh_workspace` calls `AttentionDismissalStore(...).current()`
  directly and the map lands on `AnalyticalInputs.attention_dismissals`. One neighbouring docstring
  was corrected in the same change: `read_agent_pickups` said its named `ValidationError` was
  load-bearing "unlike the two readers above", and only `read_gates` is above it now.
  *Citations.* Every line citation into `snapshots.py` on this card was re-derived from the file
  after the deletion and each range's **end** re-checked against the symbol its claim names. They
  needed it for two reasons and the larger one was not this deletion: they were already stale by
  ~34 lines before it (`read_task_documents` was cited L1146-L1174 while the staged file had it at
  L1180-L1208), and the deletion moved everything below the removed function up by a further 27.
  Corrected: `read_providers` L183-L201 and the active-group guard L232-L233; `_worktree_providers`
  L216-L276 and `_worktree_provider_ids`…`_worktree_runtime_summary` L279-L464; `read_enclosures`
  L467-L484; `read_engine_process_facts` L637-L696 and the boundary widening L679-L681;
  `_cached_local_status` L781-L798; `_git_commit_meta` `def` L824, guard L842, `return {}` L848;
  `read_drift_snapshots` L932-L968; `read_setup_progress_nodes` L1039-L1073; `read_task_documents`
  L1153-L1181; `read_series_documents` L1276-L1317; `_series_subtask_nodes` /
  `_series_subtask_created_at` L1320-L1353; `_task_doc_node` L1374-L1463 with
  `createdAt=doc.createdAt` at L1406. One body/table disagreement was resolved against the file: the
  prose cited `test_a_wedged_git_log_degrades_to_hash_only_rows_instead_of_failing_the_tick` at
  L2474-L2504 while the references table had L2895-L2921 — the table was right. One row carried the
  defect shape this master's audits look for — a range that covers the first symbol its claim names
  and stops before the rest: the `read_task_documents` row also names
  `_task_document_lifecycle_maps` and `_task_doc_node`, which live at L1217-L1250 and L1374-L1463,
  outside the L1153-L1181 it cited. Both ranges are now in the cell, with the `include_body=False`
  call site at L1180. Citations into
  `projection.py`, `contract_snapshot.py`, `provider_nodes.py`, `kernel/git_command.py`,
  `worktree_contract.py`, `setup_progress.py`, `current_state.py`, `test_projection_scaling_cs6.py`
  and `test_observer_projection.py` were re-opened and all resolved correctly; none were touched.
  Verification metadata untouched — the source is uncommitted and closeout owns the first stamp.
- 2026-08-01T20:15+02:00 — 260731-EFA-L5 curator (correction): **the central property was stated
  wrongly on this card, in the one place the tolerant readers are documented.** The 13:20 entry
  below introduced a blockquote calling "Every rewrite reads strictly. The tolerant reader backs the
  dashboard only and never drives a rewrite" *the rule underneath* both readers. It is false for
  half the contract. `durable_store.py` says so under a heading that begins "DO NOT GENERALISE
  'EVERY REWRITE READS STRICTLY' TO ALL SIX -- it is false": `AttentionDismissalStore.dismiss` /
  `_prune_locked`, `OrchestrationNudgeStore.compact` and
  `SupervisorSignalCooldownStore._compact_locked` each rewrite from the list their **tolerant**
  `read()` produced, so for those three the tolerant read *does* drive a rewrite, what it returns
  *is* written back, and the skip is **permanent** rather than one tick. The blockquote now scopes
  the strict-rewrite rule to authority-bearing logs and states the tolerant three by name, in the
  same words `controlplane/overview.md` and `controlplane/durable_store.py.md` already used — no
  third phrasing was invented. The Invariants row made the second error too: "Every store on the
  durable-store contract now offers both" generalises past the parenthetical that follows it, which
  lists exactly the two stores that qualify. **Only `GateStore` and `ExpectationRowStore` offer both
  readers**; `OperatorInboxStore` is strict only; the other three are tolerant only, their single
  `read` being the tolerant one. That row now says so, and its heading is scoped to "rewrites a log
  that carries authority" rather than "rewrites", which the tolerant three also contradicted.

  *Citations.* One defect of the shape the L4 audit found — a range that starts correctly and stops a
  few lines short. The `controlplane/store.py` row cited `projected_current` at **L187-L208**; the
  `def` is at **L209**, one line past the end of the range, so the row named a symbol it did not
  cover. Both halves of that row are now symbol-name citations with no range
  (`GateStore.read_for_projection`, read at L108; `GateStore.projected_current`, read at L209),
  because a number that was wrong within the hour is worse than no number. The
  `controlplane/expectation_rows.py` row (`read_for_projection` L185-L203, `pending_for_projection`
  L215-L217) and the `mcp/tools/gates.py` row (`_reclaim_gate_log` L453-L473, called L539) were
  re-read at their cited ranges and are correct; they were left alone. Verification metadata pinned
  until closeout stamps the L5 code commit.
- 2026-08-01T13:20+02:00 — 260731-EFA-L5 curator: **this module stopped writing.** Recorded the two
  reader changes and repaired every citation the change shifted.

  *Content.* `read_gates` no longer compacts: `GATE_COMPACT_TTL_SECONDS` and `_last_gate_compact`
  are deleted and the body is `store.projected_current(lifecycle_id, now=now)` per log. Stated the
  part that is easy to overstate — **the projection output is unchanged**, because
  `projected_current` applies the same `gate_keep_ids` filter in memory that `compact_current` did;
  what moved is the on-disk rewrite, to `mcp/tools/gates.py::_reclaim_gate_log` in the MCP process,
  because a 30-second whole-file replace driven from the dashboard tick raced the MCP's appends and
  cost 11.50% of gate snapshots at the base commit. `read_expectation_rows` now calls
  `pending_for_projection()`; the old `pending()` went through a strict read whose
  `pydantic.ValidationError` **subclasses `ValueError`**, so the `suppress(OSError, ValueError)`
  around it discarded every deadline in the file on one torn row. Added the strict/tolerant rule as
  a route-level invariant, plus a second invariant that no reader here may rewrite a control-plane
  log, each naming what breaks if undone. Corrected the HFX2-L12 CS-6 paragraph and the Task 23/24
  paragraph, which both still described the throttled rewrite as current.

  *Citations.* The L5 diff removes 6 lines at L123-L134 and 6 more inside `read_gates`, and adds 6
  inside `read_expectation_rows`, so **every** `snapshots.py` citation past L134 moved. All eleven
  were re-derived against the staged file and read back at their new range, not shifted
  arithmetically: `read_task_documents` L1152-L1180 → **L1146-L1174**; `read_series_documents`
  L1275-L1316 → **L1269-L1310**; `_series_subtask_nodes`/`_series_subtask_created_at` L1319-L1352 →
  **L1313-L1346**; `_task_doc_node` L1373-L1462 → **L1367-L1456** (`createdAt=doc.createdAt`
  L1405 → **L1399**); the worktree-provider pair L223-L283; L286-L471 → **L218-L278; L281-L466**
  (both ends widened by one to reach `def _worktree_providers` L218 and the close of
  `_worktree_runtime_summary` L466 — the old range stopped short of both); `read_providers` +
  admission filter L190-L207; L237-L240 → **L185-L203; L232-L235** (the second range now includes
  the `continue` at L235, which the claim quotes and the old range excluded);
  `read_engine_process_facts` L636-L695 → **L630-L689** (two rows); `read_enclosures` L475-L492 →
  **L469-L486**; `read_setup_progress_nodes` L1038-L1072 → **L1032-L1066**; `read_drift_snapshots`
  L931-L967 → **L925-L961**; `_git_commit_meta` `def` L823 → **L817**, guard L841 → **L835**,
  `return {}` L847 → **L841**. Three `test_observer_projection.py` citations moved too (that file
  gained 8 lines at L1530): the wedged-`git log` test L2887-L2913 → **L2895-L2921**,
  `test_active_group_filter_skips_parked_progress` L2678-L2692 → **L2686-L2700**,
  `test_reader_skips_inactive_engine_process_groups_when_filtered` L4069-L4098 → **L4077-L4106**.
  `WorktreeProviderAdmissionTests` L239-L347 and `test_read_providers_ignores_unadmitted_worktree_stacks`
  L1289-L1315 sit above that insertion and were re-read unchanged. Citations into `projection.py`,
  `contract_snapshot.py`, `provider_nodes.py`, `kernel/git_command.py`,
  `test_projection_scaling_cs6.py` and `kernel/memory_ledger.py` L1-L104 are unaffected — none of
  those files changed above the cited ranges.

  Verification metadata pinned until closeout stamps the L5 code commit.
- 2026-08-01T10:40+02:00 — 260731-EFA-L4 curator (citation pass): re-verified the three
  `projection.py` node ranges after a worker moved the lifecycle-vocabulary block into that file
  (+98 lines above these classes). `TaskDocNode` L487-L533 → L585-L631, `SeriesSubTaskNode`
  L536-L561 → L634-L649 (the class now ends at its `createdAt` field; the old span also covered
  `SeriesSectionNode`, which this row does not name), `SeriesNode` L564-L590 → L662-L688. Read back
  verbatim. No body text changed.
- 2026-08-01T00:48+02:00 — 260731-EFA-L4 curator: the source change here is two boundary
  widenings, recorded in the Slice-5e paragraph. `read_engine_process_facts` now builds
  the engine-process carrier rather than passing
  the guidance producer's own return through — the carrier is the projection's untyped
  input carrier and the reducer folds it by key name, so the carrier takes a plain
  `dict[str, Any]` and does not propagate a narrower typed shape into a structure that never
  re-emits its vocabulary. cit:(["def _cached_local_status(  # pragma: no cover"], mcp/src/agents_remember/observer/snapshots_impl/_runtime.py:383-383) declares
  `value: dict[str, Any] | None` before the `try` and stores
  `dict(projected_status_payload(...))`, so the `except` branch's `None` and the success value
  share one type. No served value changes. **Citation repairs** — the two edits added three lines
  (net) above L790, so every self-citation past it slipped by three, and the L3 curator's
  ranges no longer landed: `read_engine_process_facts` L635-L693 → L636-L695 (both rows that cite
  it, including the shared-`contracts` pair, whose `read_enclosures` half L474-L492 → L475-L492);
  `read_drift_snapshots` L928-L965 → L931-L967; `read_setup_progress_nodes` L1035-L1069 →
  L1038-L1072; `read_task_documents` L1149-L1177 → L1152-L1180; `read_series_documents`
  L1272-L1313 → L1275-L1316; `_series_subtask_nodes`/`_series_subtask_created_at` L1316-L1349 →
  L1319-L1352; `_task_doc_node` L1370-L1402 → L1373-L1462 (with `createdAt=doc.createdAt` pinned
  at L1405); `_git_commit_meta` `def` L820 / guard L838 / `return {}` L844 → L823 / L841 / L847.
  Three test citations into files this leaf grew were also stale and are fixed:
  `LedgerCommitMetaTests::test_a_wedged_git_log_degrades_to_hash_only_rows_instead_of_failing_the_tick`
  L2474-L2504 → L2887-L2913; the four Task-29 tests L217-L325; L1267-L1293; L2265-L2279;
  L3656-L3685 → L239-L347; L1289-L1315; L2678-L2692; L4069-L4098; and the PTS-L2 row cited
  `test_projection_scaling_cs6.py` L592-L663, which is the `ContractSnapshotSharedPassTests`
  setup and contains neither test it names — replaced with
  `test_full_projection_tick_enumerates_once_and_reparses_nothing_unchanged` L690-L728 and
  `test_reader_outputs_equal_with_and_without_shared_snapshot` L730-L761. Ranges at or before
  L676 (`read_providers` L190-L207; L237-L240, the worktree/Docker chain L223-L283; L286-L471,
  `contract_snapshot.py` L1-L112) were re-checked against the current files and still land on
  their symbols — unchanged.
- 2026-07-31T21:45+02:00 — 260731-EFA-L3 curator, second pass on top of the 20:55 entry below. The
  20:55 entry stopped one step short: it recorded that `_git_commit_meta` moved onto a runner that
  *has* a timeout, but not the consequence a later fix had to land. `except OSError` is now
  `except (OSError, subprocess.SubprocessError)` cit:(["def _git_commit_meta("], mcp/src/agents_remember/observer/snapshots_impl/_analytics.py:334-334) — `subprocess.TimeoutExpired` **is** a
  `SubprocessError` and **is not** an `OSError`, so the bound the consolidation introduced raised
  an exception the old handler could not see. It would have escaped `_git_commit_meta` →
  `_enrich_ledger_rows` → the projection tick, contradicting the "the projection tick never fails"
  promise in `_ledger_window`'s docstring and the same degrade in the `read_ledger` `LedgerNode`
  builder. Added that to the Slice-5h Tier 2 paragraph and as a new invariant ("a bounded runner
  raises `SubprocessError`, so catch it"), and widened the `_git_commit_meta` reference row to name
  the guard. `import subprocess` was added at L22 for it. Citation repairs — snapshots.py grew
  1521 → 1527 lines (the six added at the guard), so every self-citation past L838 slipped by six:
  `_git_commit_meta` L819-L847 → L820-L853 (`def` L820, guard L838, `return {}` L844);
  `read_drift_snapshots` L922-L959 → L928-L965; `read_setup_progress_nodes` L1029-L1063 →
  L1035-L1069; `read_task_documents` L1143-L1171 → L1149-L1177; `read_series_documents`
  L1266-L1307 → L1272-L1313; `_series_subtask_nodes`/`_series_subtask_created_at` L1310-L1343 →
  L1316-L1349; `_task_doc_node` L1364-L1396 → L1370-L1402. Ranges at or before L838
  (`read_providers` L190-L207; L237-L240, `read_enclosures` L474-L492,
  `read_engine_process_facts` L635-L693, the worktree/Docker chain L223-L283; L286-L471) were
  re-checked against the current file and still land on their symbols — unchanged. Two rows into
  files this leaf did **not** touch were stale historical references and are fixed: the old
  projection-schema row pointed to the then-stale `projection.py` range L412-L507, which contained
  none of the named `TaskDocNode`, `SeriesSubTaskNode`, or `SeriesNode`; the current card now
  cites each class at its actual definition. The Task-29 test row cited
  `test_observer_projection.py` L169-L258; L1034-L1132; L1863-L1907; L3109-L3134, none of which
  held the four tests it names (L3109-L3134 was inside `test_read_series_documents_skips_leaf_docs`)
  — replaced with the named tests at L217-L325; L1267-L1293; L2265-L2279; L3656-L3685. Added a
  reference row for the new regression, `LedgerCommitMetaTests::test_a_wedged_git_log_degrades_to_hash_only_rows_instead_of_failing_the_tick` cit:([`test_a_wedged_git_log_degrades_to_hash_only_rows_instead_of_failing_the_tick`], mcp/tests/test_observer_projection_ledger.py:171-197), which drives both entry points through
  a patched `run_git` raising `TimeoutExpired`. Finally, four reference links in the same table
  carried one `../` too many and resolved to paths that do not exist — `../../providers/
  current_state.py`, `../../providers/setup_progress.py`, `../../worktrees/worktree_contract.py`,
  `../../kernel/memory_ledger.py` — while sibling rows in the same table
  (`../kernel/git_command.py`, `../../../tests/…`) used the correct depth; all four are now one
  level shallower and resolve. Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-31T20:55+02:00 — 260731-EFA-L3 curator: the source change here is one import —
  `run_git` now comes from `agents_remember.kernel.git_command` instead of
  `worktrees.modules.git` — but it is a behaviour change for `_git_commit_meta`, this module's
  only git call: the retired copy passed no `env=` and no `timeout`, so the probe could be
  redirected by an inherited `GIT_DIR` and could hang a projection tick indefinitely. Recorded
  that in the Slice-5h Tier 2 paragraph and as an invariant. Also repaired **10 stale
  self-citations** that had been left behind by an earlier restructuring of this 1521-line file
  (none of them shifted in this leaf; none pointed at their claimed symbol):
  `read_task_documents` L584-L640 → L1143-L1171; `read_series_documents` L653-L700 → L1266-L1307
  (and the claim narrowed — the bounded summary path emits `objective=""`, `sections=[]`,
  `decisions=[]`, so it no longer says it carries them); `_series_subtask_nodes` /
  `_series_subtask_created_at` L703-L736 → L1310-L1343; `_task_doc_node`'s `createdAt=doc.createdAt`
  L757-L783 → L1364-L1396; the worktree provider/Docker chain L134-L187; L280-L375 → L223-L283;
  L286-L471 (`_worktree_providers` … `_worktree_runtime_summary`'s ready/degraded/failed);
  `read_providers` + its group filter L112-L203 → L190-L207; L237-L240;
  `read_engine_process_facts` L496-L535 → L635-L693; the shared-`contracts` pair L476-L494;
  L639-L668 → L474-L492; L635-L693 (both def lines sat just outside the old ranges);
  `read_setup_progress_nodes` L778-L805 → L1029-L1063; `read_drift_snapshots` L675-L711 →
  L922-L959. Added references for `_git_commit_meta` and the runner it now uses. The
  Repo-Internal References header was `| Finding | Source Path |` while all 22 rows carried a
  third `Citations` cell, so none of these ranges rendered at all — header and separator widened
  to three columns; no row content moved. Verification metadata pinned until closeout stamps the
  L3 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `_task_doc_node` was re-signed from `(doc, lifecycle_id, path, lifecycle_by_dir, now, *,
  include_body)` to `(doc, path, maps, now, *, include_body)` — it now resolves the doc's own
  lifecycle id from the `_TaskDocumentLifecycleMaps` it receives, closing the gap where a caller
  could pass an id inconsistent with the index used for cross-folder link resolution. Private
  helper; no reader output changed. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: replaced the time-based whole
  task-corpus cache with per-file stat-identity reuse and added a heartbeat-only landing refresh
  that updates retained Engine Room facts without rerunning their Git-backed structural reader.
  Verification metadata remains pinned until closeout.
- 2026-07-12T20:02+02:00 — 260712-PTS-L2: `read_enclosures` + `read_engine_process_facts` gained
  keyword-only `contracts: ContractSnapshot | None = None` — the projection tick injects the ONE
  shared per-tick contract snapshot (built in `projection_store`, cached across ticks by
  `(mtime_ns, size, ctime_ns)` stat identity in `contract_snapshot.py`) so neither reader walks or
  parses contracts itself; `contracts=None` keeps the pre-L2 standalone behavior.
  `_enclosure_from_contract` now takes a parsed contract. Injected contracts are shared across ticks
  and must never be mutated. Verification metadata pinned until closeout stamps the PTS-L2 commit.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: recurring snapshot assembly merges immutable landing observations per contract, logs invalid snapshot readers, and keeps local status truthful when landing data cannot be read.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F6: bounded the always-on task/series summary windows,
  removed reader bodies from them, added body revisions and the path-confined on-demand full-body
  reader, and recorded accepted N4 limits. Verification metadata remains pinned until closeout stamps
  the eventual L13 code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-08T14:35+02:00 — 260707-HFX2-L1: `read_agent_pickups` now populates the R1/R4 ack/backoff/owner fields; added `read_expectation_rows` (R5) reading `ExpectationRowStore.pending()` for dashboard/architect observability — surfacing only, an L2 predicate reads the store directly. Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-07-06T23:58:06+02:00 — 260703-L14 (visual hierarchy + chat grouping): `_task_doc_node` passes
  `orchestrates=list(doc.orchestrates)` through to `TaskDocNode` — the schema's master-only
  orchestration-command list rides the projection unchanged; no reader logic or admission rules
  touched. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T02:10+02:00 — 260703-L11: `_enclosure_from_contract` now stats
  `codeWorktreeExists`/`memoryWorktreeExists` onto each `EnclosureNode` at snapshot
  time (the same `exists()` probes `status_payload` uses) so the tasks surface can
  filter on worktree-existence truth rather than a cleanup-state proxy.
  Verification metadata pinned until closeout stamps the L11 commit.
- 2026-07-04T12:31+02:00 - L3: `read_agent_pickups` now carries inbox role,
  message, artifact, and hosted-delivery metadata into `AgentPickupNode`.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-02T21:45+02:00 — L10 binding repair: `read_task_documents`' leaf-enclosure fallback is now
  keyed on `(taskRoot, enclosure.leafId.lower())` and matched against `doc.id.lower()` (stem kept as a
  lowercased legacy alternative). Root cause: enclosure leaf ids are slugified lowercase directory
  names while doc ids are authored uppercase, and series leaf docs never carry `enclosures[]` refs —
  so every existing join was dead and active-enclosure leaf docs projected with `lifecycleId: null`,
  breaking the sidebar task-content binding and the viewed-leaf chat chain. Verification metadata
  pinned until closeout stamps the L10 commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: drift snapshot reads now carry source/memory/report
  provenance, and active-group filters remain the backend boundary for worktree provider/setup/engine
  reads so inactive parked worktrees do not emit provider alarms or projection work. Verification
  metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T05:38+02:00 — Task 29: workspace/source providers remain always-on, while worktree
  provider-state and setup-progress files now require admitted active worktree groups; engine-process
  facts can also be narrowed to non-terminal active enclosure groups before git/status probes. Verification
  metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T03:52+02:00 — Task 28 S5.2 after source sync: added
  `read_attention_dismissals` returning compact `AttentionDismissalRecord` rows keyed by item id for
  lifecycle-scoped attention acknowledgement filtering. Verification metadata pinned until closeout
  stamps the task-28 code commit.
- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: documented live Docker inspection for worktree provider stacks, including the configured-only fallback when Docker control-plane reads are unavailable. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-25T13:20+02:00 — Task 23/24: `read_gates` now compacts TTL-expired interaction gates and `read_agent_pickups` projects pending inbox responses as waiting-for-agent/check-chat feedback.
- 2026-06-24T18:11+02:00 — Task 17 live-data numbering: `_task_doc_node` now passes `doc.id` into
  `TaskDocNode.id`, giving clients a clean authored task number for leaf labels. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T16:39+02:00 — Task 17 Operations projection correction: `read_task_documents` now projects
  active master/leaf/light JSON docs even without lifecycle binding, treats `lifecycleId` as optional
  runtime context, keeps master docs on both the task-document and series surfaces, and documents
  archive/delete as the disappearance boundary. Verification metadata pinned until closeout stamps the
  code commit.
- 2026-06-24T15:37+02:00 — Task 17 live leaf projection fix: `read_task_documents` now resolves a
  lifecycle for leaf JSON docs whose filename matches a served enclosure `leafId` under the same
  `taskRoot`, so active leaf taskdocs without embedded lifecycle metadata still appear in
  `Analytics.taskDocuments`. Verification metadata pinned until closeout stamps the follow-up code
  commit.
- 2026-06-24T12:21+02:00 — Task 17 series reader ordering: `read_series_documents` now carries master
  `objective`, resolves leaf `createdAt` metadata for sub-task rows, sorts rows oldest-first only when
  every referenced leaf has structured creation time, and exposes task-doc `createdAt` for leaf ordering.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T08:51+02:00 — Task-document correction: clarified and tested that `series-contract.md` remains
  enclosure state, not a `TaskDocNode`; promoted leaves must be backed by real `ar-task-document/v1` JSON
  docs. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: snapshot readers now iterate active leaf `enclosures/<leaf-id>/series-contract.md` files, skip root series contracts for live enclosure/process views, exclude `0_archive` and enclosure folders from task JSON scans, and bind task docs through `enclosures[].enclosurePath`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:31+02:00 — Clarified Task 12 S2 provider-reader wording: `read_providers` delegates both
  CGC watcher rows and explicit GrepAI `targetRepos` to `provider_nodes.py`; GrepAI target nodes are
  addressable project bindings inside one aggregate provider instance. Verification metadata pinned
  until closeout stamps the S2 code commit.
- 2026-06-23T21:46+02:00 — Task 12 S2: `read_providers` now delegates provider-node construction to
  `provider_nodes.py`; workspace CGC watcher evidence (`resources.watchers`) is projected as repo-scoped
  workspace provider nodes. Later 22:09/22:31 entries document the GrepAI `targetRepos` correction.
  Verification metadata pinned until closeout stamps the S2 code commit.
- 2026-06-21T02:44+02:00 — Slice 6g: `read_task_documents` started taking `enclosures=` for runtime attachment; extracted `_task_doc_node` (carries `subTasks`/`sections`) + `_ref_lifecycle` (resolves a cross-folder `../<task>/task.md` ref to its lifecycle) feeding each subTask's `linkedLifecycleId` and the doc's `masterLifecycleId`. Later Task 17 made lifecycle attachment optional and limited master attachment to structurally root lifecycles. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T03:17+02:00 — slice 3c reopened (R1, masters observable): added `read_series_documents` — the folder-keyed, master-only counterpart of `read_task_documents` (selects `kind == "master"`, keys by task folder) building a `SeriesNode` with `doneCount`/`totalCount` over the master's declared `subTasks[]` (subtask-as-checkbox; `Completed` is the lever, authoritative over a slice's leaf steps) plus the full render (subTasks + sections + decisions). Disjoint from the lifecycle reader (masters carry no `lifecycleId`). Verification metadata pinned until closeout stamps the R1 code commit.
- 2026-06-18T21:25+02:00 — slice 5h Tier 2 (commit messages + date-time): added `_git_commit_meta` (ONE batched `git log --no-walk --ignore-missing` per repo, best-effort `{}` on failure, no HEAD fallback) + `_enrich_ledger_rows` / `_commit_meta_for`; `_ledger_window` and `read_ledger` gained `code_root` / `memory_root` params and now enrich each served row with the per-side `codeSubject` / `codeDate` / `memorySubject` / `memoryDate` (absent — and omitted from the wire — when the commit isn't local; never faked). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover: `read_ledger` windows `LedgerNode.rows` (newest `LEDGER_WINDOW`=25, official coupler); added `_ledger_window` (worktree coupler) wired through `read_engine_process_facts` → `EngineProcessFacts.ledger_rows`/`ledger_row_count`, best-effort (`([], 0)` on a missing/invalid ledger) so the window is read in the I/O layer and the reducer stays pure. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T14:05+02:00 — Task 6 slice 6c Part A: added `read_gates(coordination_root)` — folds every lifecycle + workspace `GateStore` log into the current gate set for the projection (resilient, malformed-skip). Verification metadata pinned until closeout stamps the 6c Part A code commit.
- 2026-06-15T19:35 — slice 5e: slice 5e: read_engine_process_facts (contract + status_payload + lifecycle_guidance, status best-effort) + read_start_progress_entries (§5.4).
- 2026-06-14T23:30+02:00: Slice 05 (5c) — `read_providers` reads surface 4 (per-worktree provider stacks via `_worktree_providers`; workspace read split to `_workspace_providers`), binding isolated CGC/GrepAI engines to worktree group + repo + role; `read_task_documents` carries the full task content (objective/requirements/design/steps/codeExamples/decisions/refs) into `TaskDocNode` for the in-dashboard task reader. Verification metadata pinned until closeout stamps the 5c code commit.
- 2026-06-13T22:34: Slice 3c commit 2 — added `read_task_documents` (surface 7): reads each `ar-task-document/v1` JSON under `tasks/<repo>/<task>/` keyed by `lifecycleId` into a `TaskDocNode`; the rendered markdown is never parsed. Verification metadata pinned until closeout stamps the 3c commit-2 code commit.
- 2026-06-13T20:48+02:00: Slice 3b — added the analytical readers
  (`read_drift_snapshots`, `read_sidecar_staleness`, `read_setup_summaries`,
  `read_setup_progress_nodes`, `read_route_coverage`, `read_tool_reports`,
  `read_ledger`), each reusing its producer's parser; drift is read from a
  persisted snapshot, never re-classified here (b1). Verification metadata is
  pinned until closeout stamps the 3b code commit.
- 2026-06-13T19:30+02:00: Created for slice 3a — the structural readers
  (`read_providers`, `read_enclosures`) reusing the producers' parsers. Analytical
  readers land in 3b. Verification metadata is pinned until closeout stamps the 3a
  code commit.
