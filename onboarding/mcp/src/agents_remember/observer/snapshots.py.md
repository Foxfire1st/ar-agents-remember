# mcp/src/agents_remember/observer/snapshots.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/snapshots.py`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-12T20:02+02:00 |
| lastVerifiedCommitHash | `b120efbfda76931cfa8eb9f24c9a808a62c10d1e`       |
| lastVerifiedCommitDate | 2026-07-13T12:33:57+02:00|
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

`read_task_document_body` accepts a projected `docPath`, resolves candidates, requires the final path
to be a real file under `coordination_root/tasks` (including after symlink resolution), validates the
task-document schema, and returns the full node. This confinement is necessary because the HTTP
endpoint accepts a client-provided path. The summary window currently truncates silently and still
carries full per-document step/sub-task lists; those are accepted round-1 N4 follow-ups, not claims of
completion in L13.

### 260707-HFX2-L12 CS-6 Update

Snapshot readers gained three CS-6 hot-path bounds: gate logs fold through `compact_current()` with rewrite throttled by `GATE_COMPACT_TTL_SECONDS`, task and series document readers share a short TTL task-json cache, and engine-process git status probes are TTL-cached and pruned to live leaf contracts.

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
`lifecycle_guidance(contract)` — both pure — plus `status` from `_safe_status_payload`. `status_payload`
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
It returns `{}` on any failure (no repo path / git absent / non-zero exit), and `--ignore-missing` drops a
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
now compacts gate logs through `GateStore.compact` before projecting, so untouched open/terminal
interaction gates cannot sit in the dashboard forever. `read_agent_pickups(coordination_root, *, now)`
projects pending operator-inbox responses as `AgentPickupNode`s for task-row feedback: fresh pending
entries show `waiting-for-agent`, entries older than the 5-minute pickup TTL show `check-chat`, L3
metadata (sender/recipient roles, message kind, artifact path, delivery state/session/detail) is carried
through from the inbox row, and consumed/dismissed/24h-expired entries disappear because the inbox store
physically removes them. Since 260707-HFX2-L1, `read_agent_pickups` also carries the R1 ack/backoff
fields (`attemptCount`/`lastAttemptAt`/`nextAttemptAt`/`escalatedAt`) and the R4 owner fields
(`ownerRole`/`ownerAgentId`/`ownerLifecycleId`) straight off the entry. A new
`read_expectation_rows(coordination_root, *, now)` (R5) reads `ExpectationRowStore.pending()`,
computes an `overdue` flag per row (`now >= dueAt`), and returns `ExpectationRowNode`s sorted by
`dueAt` — surfacing only, for dashboard/architect observability; an L2 predicate reads the store
directly and never this projection.

**Task 28 S5.2** adds `read_attention_dismissals(coordination_root)`, returning the compact
`{itemId: AttentionDismissalRecord}` acknowledgement map from
`AttentionDismissalStore(observer_logs_root(coordination_root))`. The projection tick uses the same
store directly when it needs to prune after reduction; this reader remains the call-edge helper for
consumers that only need current acknowledgement state. Task 29 lets that map include targetless
actionable-drift records while lifecycle rows are still pruned by `projection_store`.

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
- **Attention acknowledgements are current state:** `read_attention_dismissals` returns compact
  lifecycle-scoped acknowledgement records, not append-only suppression history.
- **Drift is read, never classified here:** the reducer reads the persisted drift
  snapshot (cheap, staleness-stamped); the git-per-sidecar classification stays in
  the on-demand `drift_check`/`memory_quality_check` tools (slice 3b, b1).
- **Git is best-effort at the call edge (5e):** only `status_payload` touches git;
  `read_engine_process_facts` routes it through `_safe_status_payload`, so one
  worktree's broken/absent git state yields `status=None`, never a failed tick.
  `contract_payload` and `lifecycle_guidance` are pure and always populated.
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
- **Interactions are TTL-bound:** gate and operator-inbox readers may compact their own interaction
  logs. Durable task docs, contracts, and ledger rows remain separate work-record surfaces.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `read_task_documents` projects all active task docs, with optional lifecycle attachment for leaves and root masters. | L584-L640 | [snapshots.py](snapshots.py) |
| `read_series_documents` projects master objective, sub-tasks, sections, decisions, and age into the folder-keyed `SeriesNode` aggregation surface. | L653-L700 | [snapshots.py](snapshots.py) |
| Series sub-task rows resolve sibling leaf JSON `createdAt` values and sort oldest-first only when every row has one. | L703-L736 | [snapshots.py](snapshots.py) |
| Lifecycle task docs now carry their JSON-primary `createdAt` timestamp. | L757-L783 | [snapshots.py](snapshots.py) |
| The projection nodes these readers build, including optional `TaskDocNode.lifecycleId`, `TaskDocNode.createdAt`, `SeriesSubTaskNode.createdAt`, and `SeriesNode.objective`. | L412-L507 | [projection.py](projection.py) |
| The provider current-state path + snapshot shape (surface 1). | L1-L49 | [providers/current_state.py](../../providers/current_state.py) |
| The provider-node projection policy used by `read_providers`. | L1-L92 | [provider_nodes.py](provider_nodes.py) |
| Worktree provider readers derive isolated provider container names, inspect Docker, and convert observed runtime into ready/degraded/failed summaries. | L134-L187; L280-L375 | [snapshots.py](snapshots.py) |
| `read_providers` always reads workspace providers and filters worktree provider-state files by admitted active groups. | L112-L203 | [snapshots.py](snapshots.py) |
| `read_engine_process_facts` accepts an active group filter before status-guidance and git probes are built. | L496-L535 | [snapshots.py](snapshots.py) |
| `read_enclosures` and `read_engine_process_facts` take the keyword-only `contracts` snapshot; `contracts=None` builds a local one-shot snapshot. | L476-L494; L639-L668 | [snapshots.py](snapshots.py) |
| The shared per-tick contract snapshot + stat-identity parse cache these readers consume. | L1-L112 | [contract_snapshot.py](contract_snapshot.py) |
| PTS-L2 tests pin reader-output parity with and without the shared snapshot and one enumeration per full projection tick. | L592-L663 | [test_projection_scaling_cs6.py](../../../tests/test_projection_scaling_cs6.py) |
| `read_setup_progress_nodes` accepts the same active worktree-group filter used by provider setup projection. | L778-L805 | [snapshots.py](snapshots.py) |
| `read_drift_snapshots` carries checked/source/memory/report provenance from the persisted snapshot. | L675-L711 | [snapshots.py](snapshots.py) |
| Task 29 tests pin active-group provider admission, parked provider rejection, setup-progress filtering, and engine-process group filtering. | L169-L258; L1034-L1132; L1863-L1907; L3109-L3134 | [test_observer_projection.py](../../../tests/test_observer_projection.py) |
| The worktree contract loader + fields (surfaces 5/6). | L1-L116 | [worktrees/worktree_contract.py](../../worktrees/worktree_contract.py) |
| The setup-progress projection (`progress_status`) reused for surface 3. | L1-L75 | [providers/setup_progress.py](../../providers/setup_progress.py) |
| The memory ledger loader read for surface 8. | L1-L104 | [kernel/memory_ledger.py](../../kernel/memory_ledger.py) |
| The data-surface inventory the structural/analytical split follows. | L91-L118; L332-L344 | [docs/design/observable-lifecycle.md](../../../../docs/design/observable-lifecycle.md) |

## Update History
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
