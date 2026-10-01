# mcp/src/agents_remember/worktrees/worktree_contract.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

`worktree_contract.py` reads, writes, validates, and renders the `c-09-git-worktree-manager` skill
`series-contract.md` files. A root series contract records a master task's integration branch; a leaf
enclosure contract records one concrete worktree under `enclosures/<leaf-id>/series-contract.md`, with
new writes persisting the canonical task document id as `coordination.leaf_id` when the task tree can
prove the leaf mapping. Since 260712-PTS-L1 the module also owns `heal_contract_leaf_ids`, the explicit
one-shot migration that rewrites legacy stem-shaped leaf ids to doc ids on disk — reads themselves never
normalize.

## Code Commentary

### Todos

None recorded for the ledger-retirement boundary.

### Logic

Closeout and integration persist only code and memory-content output commits. `ledger_path` remains a consumer-cache location in the memory configuration, but the model, parser, and renderer no longer have `ledger_commit` or `integrated_ledger_commit` cells. Re-rendering an older contract drops those unknown historical fields; it does not fabricate a replacement commit or consult the cache.

The module defines the single `ar-series-contract/v1` schema, the six persisted vocabularies, valid contract
`kind`s (`series` or `leaf`), the `WorktreeContract` dataclass, deterministic worktree folder helpers,
root/leaf default constructors, markdown front-matter serialization, validation, limited YAML-like parsing,
and conversion from parsed front matter back into a typed contract object. Contract rendering is split into
small section renderers for memory, sync, human review, closeout, integration, and body content. Task-folder
lookup is delegated to `worktrees/task_resolver.py`; leaf-id normalization is delegated to
`worktrees/leaf_refs.py`; this module no longer owns active-task lookup or leaf-ref policy.

### 260731-EFA-L4: the persisted vocabularies, declared here

Six `Literal` aliases replace the loose `str` fields on `WorktreeContract`:

| Alias | Members | Default constant |
| --- | --- | --- |
| `WorkflowKind` | `chat-task`, `light-task` | `DEFAULT_WORKFLOW_KIND = "light-task"` |
| `MemoryMode` | `internal`, `external`, `disabled` | (derived — see `_memory_mode_fallback`) |
| `HumanReviewStatus` | `pending-review`, `approved` | `DEFAULT_HUMAN_REVIEW_STATUS` |
| `CloseoutStatus` | `not-started`, `completed` | `DEFAULT_CLOSEOUT_STATUS` |
| `IntegrationStatus` | `not-started`, `completed`, `blocked`, `checkpointed` | `DEFAULT_INTEGRATION_STATUS` |
| `CleanupStatus` | `pending`, `completed`, `abandoned`, `reopened` | `DEFAULT_CLEANUP_STATUS = "pending"` |

Each `VALID_*` frozenset is `frozenset(get_args(<Alias>))`, derived rather than retyped, so a member
can only ever be added in one place. `VALID_MEMORY_MODES` was previously a hand-written set literal;
`VALID_KINDS` is unchanged and is still a plain set (`kind` has no `Literal`).

**These aliases are now declared in `models/worktree.py`** cit:([`WorkflowKind`, `HumanReviewStatus`, `CloseoutStatus`, `IntegrationStatus`, `CleanupStatus`], mcp/src/agents_remember/models/worktree.py:35-35; mcp/src/agents_remember/models/worktree.py:36-36; mcp/src/agents_remember/models/worktree.py:37-37; mcp/src/agents_remember/models/worktree.py:44-44; mcp/src/agents_remember/models/worktree.py:45-45) and imported back here
cit:(["from agents_remember.models.worktree import ("], mcp/src/agents_remember/worktrees/worktree_contract.py:23-23); this module derives the runtime `VALID_*` frozensets from them. The members are still
added in exactly one place, which is the property this section describes — adding one here instead
would recreate the drift it was written to prevent. `checkpointed` reached the persisted contract
this way in 260831-LOCR-L30: the checkpoint landing route writes it and `VALID_INTEGRATION_STATUSES`
accepts it with no second edit.

**This is where these values are enforced** — `worktree_start` writes the file, the lifecycle tools
rewrite it, and every read validates each cell against the `VALID_*` frozenset derived here from the
`models.worktree` aliases. One declaration is what turns "a writer emits a value the wire model
rejects" into a type error at the writer instead of a pydantic `ValidationError` escaping an MCP tool
handler that has no `except` anywhere on its path. `cleanup: reopened` (written by
`worktrees/reopen.py`) and `workflow_kind: chat-task` (`worktree_start`'s own documented argument)
were both missing from the `Literal` the packet validated against.

`WorkflowKind` deliberately holds only the two task formats a producer can write. The bare `chat`
and `light` the pre-L4 union also carried had no writer at all and were dropped.

### 260731-EFA-L5 R6: the front matter carries a `schemaVersion`, and it is the durable-store one

`CONTRACT_SCHEMA_VERSION = SCHEMA_VERSION` cit:(["CONTRACT_SCHEMA_VERSION = SCHEMA_VERSION"], mcp/src/agents_remember/worktrees/worktree_contract.py:49-49) — imported from
`controlplane/durable_store.py`, not declared here. `contract_to_text` emits
`schemaVersion: {CONTRACT_SCHEMA_VERSION}` as the second front-matter line, directly under `schema:`
cit:([`contract_to_text`], mcp/src/agents_remember/worktrees/worktree_contract.py:694-745). The read side is cit:([`_require_supported_schema_version`], mcp/src/agents_remember/worktrees/worktree_contract.py:886-899),
called by `_contract_from_data` cit:([`_contract_from_data`], mcp/src/agents_remember/worktrees/worktree_contract.py:979-1048) immediately after the `schema` check, and it delegates the
policy to the same `schema_version_supported` the JSONL records use.

**Two version fields answering two questions.** `schema: ar-series-contract/v1` names the *document
vocabulary* — what these fields mean. `schemaVersion: 1.0` versions the *durable-record contract*
the document is written under — how the file behaves. They are deliberately not merged, and the
version policy is deliberately not a second copy: one policy function, so the two cannot drift into
disagreeing about what "unknown major" means.

**The rule, in the three cases that exist:**

| Front matter | Behaviour | Why |
| --- | --- | --- |
| no `schemaVersion` line | accepted, means 1.0 | `_scalar(data.get("schemaVersion"))` returns `""` and the guard is `if raw and not ...`. Counted for this pass: **214** `series-contract.md` files under this workspace's `ar-coordination/tasks/`, **zero** with a `schemaVersion:` line — the absent case is every contract that exists, which is why no migration was needed or written. |
| unknown **minor** (`1.7`) | accepted | additive by construction |
| unknown **major** (`2.0`) | `ContractError`, naming the file and the version this build implements | the cells would still parse, and that is the failure mode — a document that means something else answering questions as though it did not |

**This is a document-level refusal, and it does not soften the reader-is-total rule below.** The
asymmetry that section describes is about the six *vocabulary cells*: an off-vocabulary cell
degrades and is quarantined because refusing it would strand a task no lifecycle tool could touch.
`schemaVersion` joins the existing document-level refusals instead (absent or unclosed front matter,
an unrecognized `schema`, a missing required field, an empty required path, a leaf with no
`leaf_id`, an external-memory leaf with no memory repository) — and it can only ever fire on a
document some *other* build wrote, because this build writes `1.0` and accepts every 1.x.

### The reader is total; the writer is strict

`_vocabulary_cell(raw, vocabulary, field_name, fallback, quarantined) -> _Cell` **never raises**.
Blank reads as `fallback`; a member reads as itself; anything else reads as `fallback` *and* appends
`f"{field_name}={value!r} read as {fallback!r}"` to `quarantined`. `_contract_from_data` collects
that list and returns `replace(contract, unknown_cells=tuple(quarantined))` when it is non-empty;
`load_contract` logs one warning naming the file and the cells. The record then travels on the new
`WorktreeContract.unknown_cells: tuple[str, ...]` field, is surfaced on the status payload as
`unknown_contract_cells`, and on the context packet as `unknownContractCells`. It is deliberately
**not** written back by `contract_to_text`: a rewrite heals the document to the value already in
force everywhere else.

Tolerance here is not laxity — it is reachability. Every lifecycle tool loads through
`load_contract` and *none* of them catches `ContractError`, so raising on an unreadable cell would
take `worktree_closeout_apply`, `worktree_integrate`, `worktree_cleanup`, `worktree_sync` **and**
`worktree_abandon` down together, leaving a task no tool could close, integrate, clean up or even
abandon. All six cells now read by one rule with no exceptions; `workflow_kind` used to be the odd
one out (no `or <default>`), so an emptied cell was a hard refusal where its five siblings degraded.

Two supporting readers:

- `_scalar(value)` returns `value.strip()` only for a `str`, else `""`. `_parse_limited_yaml` reads
  a bare `key:` line as the *opening of a section* and stores `{}`, so a cell a developer blanked
  out arrives as a dict; `str()` would have handed the literal `"{}"` to the vocabulary check. An
  emptied cell is an absent cell, and this is where that is decided.
- `_memory_mode_fallback(memory)` is the one fallback that cannot be a constant. `internal` and
  `external` decide whether there is a second repository whose content may be committed, so guessing
  `internal` for a contract that owns a memory worktree would make closeout skip work that exists.
  It reads the facts instead: `state: disabled` → `disabled`; a recorded `worktree` or `ledger` →
  `external`; otherwise `internal`.

The **write** boundary stays closed. `_contract_vocabularies(contract)` returns all six as
`(name, value, vocabulary)` — using the names `contract_to_text` writes into the front matter, so a
refusal points at the line a developer would edit — and `validate_contract` refuses any cell outside
its set. Between the two, an off-vocabulary cell can only arrive from outside (a hand edit, an older
build, a future one) and can only leave.

`_task_vocabulary(task: ContractTask) -> tuple[WorkflowKind, MemoryMode]` is the third gate, on the
*request* side: both `workflow_kind` and `memory_mode` reach `worktree_start`'s MCP signature as
free `str`, and both contract factories funnel through this helper (which is also why the
memory-mode check is no longer written out twice). It raises `ContractError` naming the legal set,
and `start_contract.build_start_contract` turns that into a blocked `worktree_start` result.

### `ContractCells` + `amend_contract`: the typed lifecycle write

```python
@dataclass(frozen=True)
class ContractCells:
    workflow_kind: WorkflowKind | None = None
    memory_mode: MemoryMode | None = None
    human_review_status: HumanReviewStatus | None = None
    closeout_status: CloseoutStatus | None = None
    integration_status: IntegrationStatus | None = None
    cleanup: CleanupStatus | None = None
```

`amend_contract(contract, cells)` copies the contract, taking `cells.<field> or contract.<field>`
for each of the six — no member of any of these vocabularies is falsy, so `or` is the whole of "was
I given one". Omitted means "leave this one alone".

The reason it exists is a hole in a third-party stub. The lifecycle tools amended contracts with
`dataclasses.replace`, which typeshed declares as `def replace(obj, /, **changes: Any)` — one `Any`
is enough to void the guarantee this module is built on, and `replace(contract,
cleanup="reclaimed-ish")` produced **zero** pyright errors even though `cleanup` is a four-member
`Literal` that the wire model rejects everything else for. Declaring the six as `ContractCells`
fields puts them back in front of the
checker at the call site. `cast` still passes, as it must; that residue is closed by
`test_wire_vocabulary_exhaustiveness` plus the rule that **no `replace` call anywhere may carry one
of these six keywords**. `replace` still performs the copy inside `amend_contract` — the values
reaching it have simply been narrowed first.

Call sites that were converted: `abandon` (`cleanup`), `cleanup` (`cleanup`), `integrate`
(`integration_status`, and `integration_status` + `cleanup` together), `closeout`
(`human_review_status`, `closeout_status`, `integration_status`, `cleanup`) and `start`
(`memory_mode`). Where a write moves both vocabulary cells and free text, the pattern is
`amend_contract(replace(contract, <free-text fields>), ContractCells(<vocabulary cells>))` — commit
hashes, notes and strategies have no vocabulary to check them against and stay on `replace`.

### Refusals name the file

Nine refusals gained a path: five in `validate_contract` (missing required fields, invalid kind, the
vocabulary loop, missing `leaf_id`, missing external-memory field), two in `_extract_front_matter`,
one in `_path` and one in `_contract_from_data` (unsupported schema). Only `load_contract`'s
"worktree contract does not exist" already named its file. `validate_contract(contract, *, path: Path)`
takes it as a **required keyword** — passed in by both `load_contract` and `write_contract` rather
than read off `contract.contract_path`, because that field is what the *document* claims about
itself and a copied or moved contract claims the path it came from, which is the one file the reader
must not be sent to.

Two message shapes, applied consistently: a refusal about the file as a whole ends with it
(`<problem>: {path}`), matching what `load_contract`'s "does not exist" already did; a refusal about
something *inside* the file names that something first (`<problem>: <detail> (in {path})`), so the
detail a developer greps for stays where it was.

`_extract_front_matter(text, path)` gained the path parameter and stopped naming
`SERIES_CONTRACT_FILENAME` — that constant is the filename the workflow writes, not the path the
reader was handed, and printing it told a developer only what they already knew. The import of
`SERIES_CONTRACT_FILENAME` from `task_resolver` is gone. `_path(value, field, contract_path)` now
names its front-matter line as `section.key`: `repo_path` and `worktree` each appear under both
`code:` and `memory:`, so the section is part of the answer.

**The constructor parameter objects (260731-EFA-L2).** `default_contract` and
`default_series_contract` are now signed on three frozen dataclasses this module also owns and
exports:

- **`RepoBranchPlan(repo_path, source_branch="", work_branch="", base_commit="")`** — one
  repository's branch plan for a worktree pair. The contract's `code:` and `memory:` sections carry
  exactly these four facts and `start_contract` derives them per side as a unit. **On the series
  contract the pair used to read `protected_branch`/`integration_branch`** — those were only other
  names for the same fork point and landing branch, so `default_series_contract` now takes
  `code=RepoBranchPlan(source_branch=<protected>, work_branch=<integration>, …)` and still writes
  them to `code_source_branch`/`code_work_branch` as before.
- **`ContractTask(name, repo_name, coordination_root, workflow_kind, memory_mode,
  parent_task_name="", parent_contract_path=None)`** — the task a contract speaks for: its name,
  the repository it changes, the coordination tree that holds it, how it is run, and the contract
  one level up (a leaf's series, a series' enclosing task).
- **`LeafIdentity(worktree_name, leaf_id=None, lifecycle_id="")`** — which leaf a leaf-enclosure
  contract is for. `leaf_id=None` still means "derive from the worktree name": the *reference* used
  for the enclosure path is `leaf_id or worktree_name`, while the *persisted* `leaf_id` is
  `leaf_id or slugify(worktree_name)` — the same two-value rule as before.

Current signatures: `default_contract(task, *, leaf, code, memory=None)` and
`default_series_contract(task, *, code, memory=None, task_root=None)`. **`memory=None` is the whole
absent-memory state**: without a repo path there is no memory branch, no memory base and no
ledger, so the constructors expand `None` to `memory_repo_path=None` and empty branch/commit
strings rather than accepting a half-populated memory plan. `start_contract._memory_plan` is the
helper that builds it or returns `None`. These constructors still derive repository and branch identity; closeout and integration now record only the actual code and memory-content outputs.

**The series contract's `worktree_group` is the master worktree group (260815-DAG-L10).**
`default_series_contract` records
`worktree_group=worktree_group_for(task.coordination_root, task.repo_name, task.name)` —
`worktrees/<repo>/<master>-ar`, the same folder helper a leaf's `default_contract` already used,
keyed on the master task name instead of a leaf worktree name — where it previously recorded the
task's `enclosures/` root. The series operation record/log, the detached worker's `TMPDIR` chain
feeding the citation source-index cache, and the Dagger test sandbox all derive from
`contract.worktree_group`, so rooting the group there lets `worktree_cleanup` / `worktree_abandon`
sweep them with the group. Leaf enclosure contracts are untouched: they still resolve through
`leaf_enclosure_path` to `tasks/<task>/enclosures/<leaf-id>/series-contract.md`. Current
lifecycle-location, closeout-door evidence, terminal-validation, and start-contract owners all
compare against `worktree_group_for(...)`, so a legacy series contract still recording
`task_root / "enclosures"` as its group is refused by contract-addressed worktree tools until an
explicit adoption/re-stamp route proves it. No deleted queue-evidence reader is retained as a
compatibility fallback.

Since 260712-PTS-L1, `load_contract` is read + parse + validate ONLY: one file read, zero tasks-tree
traversal — no leaf-ref resolution, no series-contract iteration, no glob. A legacy stem-shaped
`coordination.leaf_id` is returned verbatim. Normalization is a write-time concern: `write_contract`
paths still run `normalize_contract_leaf_id()`, which asks the shared leaf-ref resolver to map legacy
stem-shaped ids to canonical task doc ids when the task tree can prove a unique match, and write paths
still surface non-leaf-ref task-resolution failures. `default_contract` accepts a caller-supplied doc id
without slugifying it, while still slugifying the worktree name only when no explicit leaf id is
available. (Motivation: a 2026-07-12 py-spy daemon sample put the hidden per-read resolution walk at
~9.7s of a 15s sample; the master 260712-PTS decision is that normalization is
write-time/migration-only.)

`heal_contract_leaf_ids(coordination_root, *, dry_run=False)` is the explicit, one-shot successor to the
per-read normalization `load_contract` used to run. It walks `tasks/` once via
`iter_leaf_enclosure_contracts` — the exact population the projection readers consume — maps each legacy
`leaf_id` through `normalize_contract_leaf_id(..., keep_unresolved=True)` (the same mapping the read path
used to apply), and rewrites only the contracts whose id actually changes. It is idempotent and cheap on
re-run: a contract whose `leaf_id` already is a doc id of the task root its enclosure PHYSICALLY lives in
(derived from the `enclosures/<leaf>/series-contract.md` path, never the recorded root, so a stale
recorded root degrades to the slow path instead of a wrong skip) is skipped through a per-root
`leaf_refs.canonical_leaf_doc_ids` index without any resolution walk. It is loud by report: every rewrite
logs one line and lands in the returned report (`healed` / `canonical` / `unchanged` / `errors` /
`dryRun`), and an unresolvable or malformed entry is reported, never fatal to the sweep. Nothing invokes
it implicitly from a read path — reach it through the `heal-leaf-ids` CLI subcommand
(`worktrees/modules/cli.py`) or a direct call (e.g. once at daemon startup).

`lifecycle_id` (slice 2c) remains the observable-lifecycle enclosure anchor for leaf contracts, rendered as
a `lifecycle:` front-matter section and parsed back through `_section(data, "lifecycle")`. Root series
contracts represent integration branches and do not require a lifecycle id.

`sync_log` (issue #54 sub-task D) records each `worktree_sync` base-pair
advance as a tuple of dict entries. It is a real dataclass field because the
closeout/contract rewrite regenerates the document from the model — freeform
contract prose does not survive. It serializes as one compact JSON scalar
(`sync:` / `  log: [...]`) so the limited front-matter parser (scalar one-level
sections only) round-trips it; an absent or unparseable value loads as `()`,
keeping pre-#54 contracts loadable.

### Conventions

The contract parser intentionally supports only the subset written by the
workflow: scalar top-level fields and one-level nested sections. This keeps
contract files human-readable without introducing a general YAML dependency.

#### Invariants And Boundaries

- External-memory leaf contracts must include memory repo, memory worktree, and
  cache-location paths; root series contracts can point at the memory repo cache without a leaf memory worktree. The cache path is address metadata: contract validation does not require the file to exist or parse its contents.
- Contract serialization must preserve closeout and integration state.
- Contract reads cost O(one file): `load_contract` must never traverse the tasks tree. Consumers of
  loaded contracts must therefore tolerate RAW legacy stem-shaped `leaf_id` values until
  `heal_contract_leaf_ids` (or any `write_contract` rewrite, e.g. closeout/sync bookkeeping) heals the
  file on disk — do not assume a doc-id-shaped `leaf_id` on an unhealed tree.
- The heal rewrite regenerates the whole contract file from the parsed model: unknown front-matter keys
  and hand-added prose do not survive it. This is pre-existing `write_contract` semantics (same as
  closeout rewrites), not a heal-specific behavior.
- `heal_contract_leaf_ids` is idempotent, dry-runnable, and never fatal on a malformed entry; it is only
  ever invoked explicitly (CLI `heal-leaf-ids` or a direct call), never as a read side effect.
- Leaf worktree folders use slugified names with legacy `-ar` support only where the resolver needs to find
  existing work; task-root lookup lives in `worktrees/task_resolver.py`.
- `ContractError` subclasses the shared `AgentsRememberError` (imported from
  `agents_remember.errors`); since that base itself derives from `ValueError`,
  existing `except ValueError` callers still catch contract failures while the
  error now also participates in the domain error hierarchy.
- **The read path never raises on a vocabulary cell; the write path always does.** `_vocabulary_cell`
  is total by design — every lifecycle tool loads through `load_contract` and none catches
  `ContractError`, so a refusal there strands a live task in a state no tool can move.
  `validate_contract` refuses all six cells so nothing in this package can be what put an unreadable
  one on disk.
- **Move a vocabulary cell through `ContractCells` + `amend_contract`, never through
  `dataclasses.replace`.** Typeshed types `replace`'s `**changes` as `Any`, so pyright checks
  nothing there. No `replace` call anywhere may carry `workflow_kind`, `memory_mode`,
  `human_review_status`, `closeout_status`, `integration_status` or `cleanup` as a keyword.
- `unknown_cells` is read-path-only state. It must not be rendered by `contract_to_text`: a rewrite
  is the heal, and persisting the quarantine record would make the degradation permanent.
- **Every refusal names the file it is about, and takes that path as an argument.** Do not read it
  from `contract.contract_path` — a copied contract claims the path it came from.
- Adding a member to any of the six vocabularies means adding it to the owning `Literal` in `models/worktree.py`. The
  contract imports those aliases and derives `VALID_*` through `get_args`, so there
  is no second place to update — and no place to forget.
- **`schemaVersion` is the durable-store version, reused — never a second one declared here.**
  `CONTRACT_SCHEMA_VERSION = SCHEMA_VERSION` and the read side calls
  `durable_store.schema_version_supported`. Writing a local version constant or a local
  major/minor rule would give the tree two version policies that can disagree about what an unknown
  major means, which is the drift this leaf spent itself removing everywhere else.
- **An absent `schemaVersion` must keep meaning 1.0.** The guard is `if raw and not
  schema_version_supported(raw)`; drop the `raw and` and every contract written before this leaf —
  all of them — refuses on read, which is exactly the strand-the-task failure the total reader
  exists to prevent. That is also why no migration was written: there is nothing to migrate.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `WorktreeContract` persists real code/memory outputs and the informational cache location. [1]
- `_closeout_lines` serializes code and memory-content closeout output cells only. [2]
- `_integration_lines` serializes strategy and code/memory landed outputs only. [3]
- `_contract_from_data` loads real output cells without reading retired ledger commit keys. [4]

Same-repository source defines the contract format and `c-09-git-worktree-manager` skill uses it.

- The front matter's `schemaVersion`: the constant reused from the durable-store contract, the line `contract_to_text` emits, and the read-side refusal `_contract_from_data` calls right after the `schema` check. (`CONTRACT_SCHEMA_VERSION = SCHEMA_VERSION`; `_require_supported_schema_version`) [5]
- The single version policy both this file and the six control-plane JSONL stores read through — unknown major rejected, unknown minor accepted, an unparseable version rejected. (`SCHEMA_VERSION`; `SUPPORTED_SCHEMA_MAJOR`; `schema_version_supported`) [6]
- The module defines the contract schema, the six vocabulary `Literal`s and their derived `VALID_*` / `DEFAULT_*` constants, the `ContractError` type (subclassing `AgentsRememberError` from `agents_remember.errors`), the total reader `_vocabulary_cell` with `_scalar` / `_memory_mode_fallback` / `_task_vocabulary`, the `ContractCells` record with `amend_contract`, and the full `WorktreeContract` state record ending in `unknown_cells`. [7]
- Folder naming and default contract helpers derive task roots, worktree groups, and external-memory ledger paths; both constructors narrow the request through `_task_vocabulary`. [8]
- Contract WRITE paths normalize legacy leaf ids to canonical doc ids when the leaf-ref resolver can prove the mapping; `load_contract` performs no normalization at all. [9]
- `heal_contract_leaf_ids` sweeps the active leaf-enclosure population once, cheap-skips canonical ids via a per-root doc-id index, rewrites only changed contracts, and reports every rewrite and error. [10]
- Dedicated leaf-ref resolver supplies canonical doc ids, legacy alias policy, and the heal's bounded per-task-root doc-id index (`canonical_leaf_doc_ids`). [11]
- The `heal-leaf-ids` CLI subcommand (`--coordination-root`, `--dry-run`) is the deliberate invocation seam for the heal. [12]
- Load/write/render helpers: `load_contract` (which logs the quarantined cells and passes `path=` to validation), `write_contract`, the heal, and the section renderers through `contract_to_text`. [13]
- The write gate and the read path: `_contract_vocabularies`, `validate_contract(contract, *, path)`, the path-naming `_extract_front_matter` / `_path`, limited YAML parsing, and `_contract_from_data` reading all six cells through `_vocabulary_cell` into `unknown_cells`. [14]
- `WorktreeSummary` consumes the shared vocabulary aliases owned by `models/worktree.py` for its response fields. [15]
- `WorktreeSummary` consumes the shared vocabulary aliases owned by `models/worktree.py` for its response fields. [16]
- The current `WorktreeStatusFacts` shape imports the same six contract vocabularies, reports `unknown_cells` as `unknown_contract_cells`, and exposes derived source lineage without adding a persisted contract cell. [17]
- `build_start_contract` converts `_task_vocabulary`'s `ContractError` into a blocked start result. [18]
- Vocabulary exhaustiveness, the `ContractCells` write path, and the no-`replace`-keyword rule are pinned here. (`ContractBoundaryTests`) [19]

### Cross-Repo References

No meaningful cross-repo boundary is documented here; the contract points at
external memory paths, but the parser and renderer are same-repository code.

No additional cross-repository evidence applies.

## L23 Lineage Status Consumer

The contract parser remains the durable source of repository and branch plans;
`WorktreeStatusFacts` now adds an optional `source_lineage` projection computed
from those facts. This does not add a persisted contract cell or change tolerant
read/refusing-write behavior.

No sibling repository boundary is needed to explain this file.

## Historical 260815-DAG-L3 Queue Binding (Removed)

The intermediate contract persisted sprint/candidate queue binding cells. CLIVE final deletes those
cells rather than keeping a compatibility reader. For a period the typed `closeout_door` was the sole
canonical scheduling generation on the contract; projection membership is recomputed, and claimed
lifecycle evidence transfers to the stable journal. **That contract-owned door is itself now gone** —
see "260821-CLIVE Door-Only Scheduling Authority" below.

## 260815-DAG-L4 Integration-Authority Impact

Task-derived integration refs remain mechanically non-ordinary: repository defaults, sprint supers,
and active atomic-series refs are censused across code and external memory. The contract contributes
exact repository and task facts to those owners; it no longer carries mutable queue binding state, and
it no longer carries door facts.

## 260821-CLIVE-L1 Canonical Contract Publication

`contract_publication_text` is the sole normalize + validate + serialize owner for contract publication. `write_contract`, closeout finalization hashing, lifecycle recovery identity, and organizational reset hashing all consume its exact UTF-8 text. This prevents proof from hashing a representation different from the file that is atomically published. Contract-file atomic replacement is distinct from the sequential code and memory-content Git commits.

## 260821-CLIVE-L2 Current Contract

The current source seams include `ContractError`, `ContractCells`, `amend_contract`. The contract carries exact enclosure and task facts consumed by manifest publication, but normal operation lookup is locator -> immutable root manifest -> journal. Mutable contract/task parsing is not a fallback lifecycle locator.

### Reconciled Source Evidence

- The current module exposes `ContractError`, `ContractCells`, `amend_contract` at this ownership boundary. [20]

## 260821-CLIVE Door-Only Scheduling Authority (Superseded)

The contract no longer persists `queue_sprint_task_document` or
`queue_candidate_task_document`. Canonical scheduling intent is the typed `closeout_door`; queue
membership is derived elsewhere and cannot be reconstructed as durable binding. `parse_contract_text`
parses exact retained/archive bytes using the same validation as `load_contract`, without creating a
temporary-file authority. Existing strict writer, normalization, and unknown-cell behavior remain.

## Closeout-Door Cut: The Contract No Longer Stores A Door

The closeout-door cut (commit `fad9808e`) took `closeout_door` out of `WorktreeContract` **entirely** —
field, parser, writer and the publish guard. It superseded the section above, which had named the typed
`closeout_door` as the contract's canonical scheduling generation.

The door now lives in its own journal at `<worktree_group>/reports/closeout-door.json`, plus the
operation record's own publication, and is read through the single accessor
`closeout/door.py::live_closeout_door(contract, record=None)`. A contract that still carries a
`closeout_door:` block **parses**: the key is never read, and the next `write_contract` rewrite drops
it. Nothing in this module validates, renders, or proves door bytes any more, so there is no
contract-byte before/after SHA proof to satisfy.

## CCR-R02@v2 Publishable Closeout Door (Removed)

This section recorded that `contract_publication_text` refused to publish a contract whose live
closeout door predated canonical task intent, through `_require_publishable_closeout_door` calling
`require_task_intent_identity(contract.closeout_door.taskIntent, owner="closeout-door", ...)` and
translating `TaskIntentError` into a path-naming `ContractError`. It was landed in candidate
`99dc249b`. That guard was deleted by commit `fad9808e` along with the field it read. Task-intent
identity is now proven where the door is published (the door journal / operation journal), not at
contract publication; `closeout_door.update-provenance` is likewise no longer a contract-publish
refusal. No compatibility reader for a legacy door was retained.
