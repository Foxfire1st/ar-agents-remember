# mcp/src/agents_remember/worktrees/worktree_contract.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/worktree_contract.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-19T04:05+02:00 |
| lastVerifiedCommitHash | `e41ea31d6df3e35a92f526edef8420ae9bd56c57` |
| lastVerifiedCommitDate | 2026-08-18T19:37:20+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`worktree_contract.py` reads, writes, validates, and renders the `c-09-git-worktree-manager` skill
`series-contract.md` files. A root series contract records a master task's integration branch; a leaf
enclosure contract records one concrete worktree under `enclosures/<leaf-id>/series-contract.md`, with
new writes persisting the canonical task document id as `coordination.leaf_id` when the task tree can
prove the leaf mapping. Since 260712-PTS-L1 the module also owns `heal_contract_leaf_ids`, the explicit
one-shot migration that rewrites legacy stem-shaped leaf ids to doc ids on disk — reads themselves never
normalize.

## Code Commentary

### Logic

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
| `IntegrationStatus` | `not-started`, `completed`, `blocked` | `DEFAULT_INTEGRATION_STATUS` |
| `CleanupStatus` | `pending`, `completed`, `abandoned`, `reopened` | `DEFAULT_CLEANUP_STATUS = "pending"` |

Each `VALID_*` frozenset is `frozenset(get_args(<Alias>))`, derived rather than retyped, so a member
can only ever be added in one place. `VALID_MEMORY_MODES` was previously a hand-written set literal;
`VALID_KINDS` is unchanged and is still a plain set (`kind` has no `Literal`).

**This is where these values are born and where they die** — `worktree_start` writes the file, the
lifecycle tools rewrite it, and `models.worktree` imports these same aliases for the response
boundary. One declaration is what turns "a writer emits a value the wire model rejects" into a type
error at the writer instead of a pydantic `ValidationError` escaping an MCP tool handler that has no
`except` anywhere on its path. `cleanup: reopened` (written by `worktrees/reopen.py`) and
`workflow_kind: chat-task` (`worktree_start`'s own documented argument) were both missing from the
`Literal` the packet validated against.

`WorkflowKind` deliberately holds only the two task formats a producer can write. The bare `chat`
and `light` the pre-L4 union also carried had no writer at all and were dropped.

### 260731-EFA-L5 R6: the front matter carries a `schemaVersion`, and it is the durable-store one

`CONTRACT_SCHEMA_VERSION = SCHEMA_VERSION` cit:(["CONTRACT_SCHEMA_VERSION = SCHEMA_VERSION"], mcp/src/agents_remember/worktrees/worktree_contract.py:45-45) — imported from
`controlplane/durable_store.py`, not declared here. `contract_to_text` emits
`schemaVersion: {CONTRACT_SCHEMA_VERSION}` as the second front-matter line, directly under `schema:`
cit:([`contract_to_text`], mcp/src/agents_remember/worktrees/worktree_contract.py:689-740). The read side is cit:([`_require_supported_schema_version`], mcp/src/agents_remember/worktrees/worktree_contract.py:881-894),
called by `_contract_from_data` cit:([`_contract_from_data`], mcp/src/agents_remember/worktrees/worktree_contract.py:974-1045) immediately after the `schema` check, and it delegates the
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
  `external` decide whether there is a second repository to commit and a ledger to map, so guessing
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
helper that builds it or returns `None`. Every emitted `WorktreeContract` field is unchanged.

**The series contract's `worktree_group` is the master worktree group (260815-DAG-L10).**
`default_series_contract` records
`worktree_group=worktree_group_for(task.coordination_root, task.repo_name, task.name)` —
`worktrees/<repo>/<master>-ar`, the same folder helper a leaf's `default_contract` already used,
keyed on the master task name instead of a leaf worktree name — where it previously recorded the
task's `enclosures/` root. The series operation record/log, the detached worker's `TMPDIR` chain
feeding the citation source-index cache, and the Dagger test sandbox all derive from
`contract.worktree_group`, so rooting the group there lets `worktree_cleanup` / `worktree_abandon`
sweep them with the group. Leaf enclosure contracts are untouched: they still resolve through
`leaf_enclosure_path` to `tasks/<task>/enclosures/<leaf-id>/series-contract.md`. The matching
contract-equality checks in `lifecycle_operations.py`,
`closeout_queue_candidate_evidence.py`, `modules/terminal_validation.py`, and
`modules/start_contract.py` compare against `worktree_group_for(...)`, so a legacy series contract
still recording `task_root / "enclosures"` as its group is refused by every contract-addressed
worktree tool until re-stamped.

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

### Invariants And Boundaries

- External-memory leaf contracts must include memory repo, memory worktree, and
  ledger paths; root series contracts can point at the memory repo ledger without a leaf memory worktree.
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
- Adding a member to any of the six vocabularies means adding it to the `Literal` here. The
  `VALID_*` frozensets derive from `get_args`, and `models.worktree` imports the aliases, so there
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

## Docs References

No external documentation is needed for this local contract format.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed for the local worktree contract parser. | n/a | n/a |

## Repo-Internal References

Same-repository source defines the contract format and `c-09-git-worktree-manager` skill uses it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The front matter's `schemaVersion`: the constant reused from the durable-store contract, the line `contract_to_text` emits, and the read-side refusal `_contract_from_data` calls right after the `schema` check. | "CONTRACT_SCHEMA_VERSION = SCHEMA_VERSION"; `_require_supported_schema_version` | mcp/src/agents_remember/worktrees/worktree_contract.py:45-45; mcp/src/agents_remember/worktrees/worktree_contract.py:881-894 |
| The single version policy both this file and the six control-plane JSONL stores read through — unknown major rejected, unknown minor accepted, an unparseable version rejected. | `SCHEMA_VERSION`; `SUPPORTED_SCHEMA_MAJOR`; `schema_version_supported` | mcp/src/agents_remember/controlplane/durable_store.py:45-45; mcp/src/agents_remember/controlplane/durable_store.py:55-55; mcp/src/agents_remember/controlplane/durable_store.py:224-245 |
| The module defines the contract schema, the six vocabulary `Literal`s and their derived `VALID_*` / `DEFAULT_*` constants, the `ContractError` type (subclassing `AgentsRememberError` from `agents_remember.errors`), the total reader `_vocabulary_cell` with `_scalar` / `_memory_mode_fallback` / `_task_vocabulary`, the `ContractCells` record with `amend_contract`, and the full `WorktreeContract` state record ending in `unknown_cells`. | `WorktreeContract` | mcp/src/agents_remember/worktrees/worktree_contract.py:230-285 |
| Folder naming and default contract helpers derive task roots, worktree groups, and external-memory ledger paths; both constructors narrow the request through `_task_vocabulary`. | `_task_vocabulary` | mcp/src/agents_remember/worktrees/worktree_contract.py:161-178 |
| Contract WRITE paths normalize legacy leaf ids to canonical doc ids when the leaf-ref resolver can prove the mapping; `load_contract` performs no normalization at all. | `load_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:436-469 |
| `heal_contract_leaf_ids` sweeps the active leaf-enclosure population once, cheap-skips canonical ids via a per-root doc-id index, rewrites only changed contracts, and reports every rewrite and error. | `heal_contract_leaf_ids` | mcp/src/agents_remember/worktrees/worktree_contract.py:480-555 |
| Dedicated leaf-ref resolver supplies canonical doc ids, legacy alias policy, and the heal's bounded per-task-root doc-id index (`canonical_leaf_doc_ids`). | `canonical_leaf_doc_ids` | mcp/src/agents_remember/worktrees/leaf_refs.py:144-154 |
| The `heal-leaf-ids` CLI subcommand (`--coordination-root`, `--dry-run`) is the deliberate invocation seam for the heal. | "heal-leaf-ids" | mcp/src/agents_remember/worktrees/modules/cli.py:147-147 |
| Walk-free load tripwires, heal parity with the removed read-time normalization, idempotence, dry-run, error tolerance, and the CLI seam are pinned by the resolver test suite. | `LeafRefResolutionTests` | mcp/tests/test_leaf_ref_resolution.py:103-464 |
| Load/write/render helpers: `load_contract` (which logs the quarantined cells and passes `path=` to validation), `write_contract`, the heal, and the section renderers through `contract_to_text`. | `contract_to_text` | mcp/src/agents_remember/worktrees/worktree_contract.py:689-740 |
| The write gate and the read path: `_contract_vocabularies`, `validate_contract(contract, *, path)`, the path-naming `_extract_front_matter` / `_path`, limited YAML parsing, and `_contract_from_data` reading all six cells through `_vocabulary_cell` into `unknown_cells`. | `_contract_vocabularies`; `validate_contract`; `_extract_front_matter`; `_contract_from_data` | mcp/src/agents_remember/worktrees/worktree_contract.py:743-758; mcp/src/agents_remember/worktrees/worktree_contract.py:761-816; mcp/src/agents_remember/worktrees/worktree_contract.py:819-832; mcp/src/agents_remember/worktrees/worktree_contract.py:974-1045 |
| `WorktreeSummary` imports `WorkflowKind`, `MemoryMode`, `HumanReviewStatus`, `CloseoutStatus`, `IntegrationStatus` and `CleanupStatus` from here for the response boundary. | `WorktreeSummary` | mcp/src/agents_remember/models/worktree.py:96-136 |
| The current `WorktreeStatusFacts` shape imports the same six contract vocabularies, reports `unknown_cells` as `unknown_contract_cells`, and exposes derived source lineage without adding a persisted contract cell. | "class WorktreeStatusFacts(TypedDict):" | mcp/src/agents_remember/worktrees/modules/guidance.py:75-116 |
| `build_start_contract` converts `_task_vocabulary`'s `ContractError` into a blocked start result. | `build_start_contract` | mcp/src/agents_remember/worktrees/modules/start_contract.py:934-954 |
| Vocabulary exhaustiveness, the `ContractCells` write path, and the no-`replace`-keyword rule are pinned here. | "class ContractBoundaryTests(unittest.TestCase):" | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:153-153 |
| The worktree lifecycle modules import contract helpers and record closeout/integration commit state through these contract objects. | `# mcp/src/agents_remember/worktrees/modules Overview` | onboarding/mcp/src/agents_remember/worktrees/modules/overview.md:1-762 |

## Cross-Repo References

No meaningful cross-repo boundary is documented here; the contract points at
external memory paths, but the parser and renderer are same-repository code.

## L23 Lineage Status Consumer

The contract parser remains the durable source of repository and branch plans;
`WorktreeStatusFacts` now adds an optional `source_lineage` projection computed
from those facts. This does not add a persisted contract cell or change tolerant
read/refusing-write behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No sibling repository boundary is needed to explain this file. | n/a | n/a |

## 260815-DAG-L3 Durable Queue Binding

An admitted leaf contract now persists the immutable canonical sprint and candidate
task-document-reference keys. Empty fields mean the leaf never crossed the explicit queue boundary;
once present, lifecycle code uses them to distinguish genuine legacy absence from damaged or
deleted queue topology and fails closed instead of silently bypassing enforcement.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Update History

- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 moved `build_start_contract` within `start_contract.py`; re-pointed the citation to `start_contract.py:934-954`. Verification metadata unchanged.

- 2026-08-19T04:05+02:00 — 260815-DAG-L10 curator: `default_series_contract` now records
  `worktree_group` as `worktree_group_for(task.coordination_root, task.repo_name, task.name)`
  (`worktrees/<repo>/<master>-ar`) instead of the task `enclosures/` root, so the series operation
  log, the citation source-index cache (worker `TMPDIR` chain), and the Dagger test sandbox land
  under the terminal-swept worktree group; leaf enclosure resolution via `leaf_enclosure_path` is
  unchanged. Verification metadata stamped at the landed code commit `e41ea31d`.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: documented the additive durable sprint/candidate
  queue binding fields and their fail-closed meaning; verification remains closeout-owned.
- 2026-08-13T07:53+02:00 — 260731-EFA-L23 super-line reconciliation: re-reviewed this card and its Repo-Internal citation targets after absorbing the super-integration memory line. Retained claims remain supported by the current tree. Verification is pinned to real code HEAD `1580f92715ff93c988f9a15439ad9bec60ef4c5d`; the new-line memory mapping remains closeout-owned.
- 2026-08-12T20:24+02:00 — L23 curator: re-read the changed `WorktreeStatusFacts` consumer and confirmed lineage is a derived optional status field, not persisted contract vocabulary; verification remains closeout-owned.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B19 curator: rebased the `CONTRACT_SCHEMA_VERSION`
  citations to the assignment line, deduplicated the version-policy row, and regenerated ranges
  via the scoped fixer; exact non-fixing check returns zero findings.

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 15 citation claims and preserved verification metadata.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T20:15+02:00 — 260731-EFA-L5 curator (correction pass): **the version-policy row cited
  three symbols and covered none of them.** It read `SCHEMA_VERSION` L134-L142;
  `SUPPORTED_SCHEMA_MAJOR` L144; `schema_version_supported` L339-L348 into `durable_store.py`. That
  file grew 598 → 699 lines mid-pass: `SCHEMA_VERSION` is at **L165**, `SUPPORTED_SCHEMA_MAJOR` at
  **L175**, and `schema_version_supported` at **L410** — no cited range contains the symbol it
  names, and L339-L348 lands in the middle of the ownership register instead. Replaced with the
  three symbol names and no ranges, as this leaf's test cards do, because a number that was wrong
  within the hour is worse than no number. The claim itself is unchanged and was re-verified at the
  new locations: `schema_version_supported` compares the major for **equality** with
  `SUPPORTED_SCHEMA_MAJOR` (not `<=`) and rejects an unparseable version, which is exactly the
  "unknown major rejected" policy this file imports. The sibling row into
  this module's own source was re-read and is correct: `CONTRACT_SCHEMA_VERSION` cit:(["CONTRACT_SCHEMA_VERSION = SCHEMA_VERSION"], mcp/src/agents_remember/worktrees/worktree_contract.py:45-45) (assignment), emitted cit:([`contract_to_text`], mcp/src/agents_remember/worktrees/worktree_contract.py:689-740),
  `_require_supported_schema_version` cit:([`_require_supported_schema_version`], mcp/src/agents_remember/worktrees/worktree_contract.py:881-894), called cit:([`_contract_from_data`], mcp/src/agents_remember/worktrees/worktree_contract.py:974-1045). No other change; nothing
  on this card asserts a measured figure.
- 2026-08-01T13:20+02:00 — 260731-EFA-L5 curator: the series contract's front matter gained
  `schemaVersion`, and the card now records the three-case rule and the boundary it belongs to.
  Added a section for it: `CONTRACT_SCHEMA_VERSION = SCHEMA_VERSION` cit:(["CONTRACT_SCHEMA_VERSION = SCHEMA_VERSION"], mcp/src/agents_remember/worktrees/worktree_contract.py:45-45) (imported from
  `controlplane/durable_store.py` rather than declared here), emitted as the second front-matter
  line by `contract_to_text` cit:([`contract_to_text`], mcp/src/agents_remember/worktrees/worktree_contract.py:689-740), and enforced on read by `_require_supported_schema_version`
  cit:([`_require_supported_schema_version`], mcp/src/agents_remember/worktrees/worktree_contract.py:881-894) which `_contract_from_data` cit:([`_contract_from_data`], mcp/src/agents_remember/worktrees/worktree_contract.py:974-1045) calls straight after the `schema` check and which
  delegates to the same `schema_version_supported` the JSONL records use. **Stated the one
  distinction this file makes it easy to get wrong**: this is a *document-level* refusal, joining
  absent front matter and an unrecognized `schema` — it is not a vocabulary cell and does not
  weaken the reader-is-total rule, which is about the six cells and about not stranding a live task.
  Recorded that an absent `schemaVersion` reads as 1.0 (the guard is `if raw and not ...`), which is
  why every contract on disk still loads and why no migration exists; recorded the unknown-minor
  accept / unknown-major refuse split; and added both as invariants naming the failure — a local
  version constant gives the tree two policies that can disagree, and dropping the `raw and` refuses
  every contract written before this leaf.

  **Citations repaired.** The change inserts 1 line at L16, 11 at L36, 1 at L696 and 17 at L883, so
  all four `worktree_contract.py` ranges moved and each was re-read at its new bounds:
  `L34-L274` → **L35-L286** (`CONTRACT_SCHEMA` L35 … `unknown_cells` L286); `L323-L422` →
  **L335-L434** (`worktree_folder_name` L335 … `default_series_contract` ends L434 — the old range
  also stopped a line short of that constructor's close); `L425-L729` → **L437-L742**
  (`load_contract` L437 … `contract_to_text` ends L742); `L732-L981` → **L745-L1011**
  (`_contract_vocabularies` L745 … `_contract_from_data` ends at the file's last line, 1011). Added
  two reference rows for the new field and the shared version policy. Verification metadata pinned
  until closeout stamps the L5 code commit.
- 2026-08-01T09:36+02:00 — 260731-EFA-L4 curator: this is the leaf's largest change to any file
  (+406 lines) and the card carried none of it. Added four sections, every claim read off the
  current source: (1) the six `Literal` aliases with their members and derived `VALID_*` /
  `DEFAULT_*` constants, replacing the loose `str` fields on `WorktreeContract` and the hand-written
  `VALID_MEMORY_MODES` set — including that `WorkflowKind` dropped `chat` and `light`, which had no
  writer; (2) the total reader `_vocabulary_cell` with `_scalar`, `_memory_mode_fallback` and
  `_task_vocabulary`, the new `unknown_cells` field it feeds, and why tolerance on read is
  reachability (no lifecycle tool catches `ContractError`) while `validate_contract` refuses all six
  on write; (3) `ContractCells` + `amend_contract`, the typeshed `**changes: Any` hole they close,
  and the converted call sites; (4) the nine refusals that now interpolate a path, `path` being a
  required keyword on `validate_contract` and threaded rather than read from
  `contract.contract_path`, the two message shapes, and the dropped `SERIES_CONTRACT_FILENAME`
  import. Added six invariants and five reference rows.
  **Citation repairs — all four line ranges were broken by the +406 lines and are re-verified
  against the current file:** L16-L60 → **L34-L274** (the old range contained neither
  `ContractError`, now at L80, nor `WorktreeContract`, L219-L274; the new range runs from
  `CONTRACT_SCHEMA` at L34 through `unknown_cells` at L274); L61-L151 → **L323-L423**
  (`worktree_folder_name` L323 … `default_series_contract` ends L423); L154-L289 → **L425-L730**
  (`load_contract` L425 … `contract_to_text` ends L730); L292-L387 → **L732-L981**
  (`_contract_vocabularies` L732 … `_contract_from_data`'s final `return` at L981, the last line of
  the file). The three symbol-name citations (`load_contract`, `normalize_contract_leaf_id`,
  `heal_contract_leaf_ids`, `command_heal_leaf_ids`) were re-checked and all still resolve.
  (Range ends are the last code line of the named symbol, not the blank separator: L422 is
  `default_series_contract`'s closing paren, L729 is `contract_to_text`'s `return`.)
  Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `RepoBranchPlan`, `ContractTask` and `LeafIdentity`, and re-signed both
  constructors — `default_contract(task, *, leaf, code, memory=None)` and
  `default_series_contract(task, *, code, memory=None, task_root=None)`. The series contract's
  `protected_branch`/`integration_branch` keywords became the code plan's
  `source_branch`/`work_branch` (the same two facts under their general names), and `memory=None`
  now expresses the whole absent-memory state. Every emitted `WorktreeContract` field, including
  the `leaf_id or worktree_name` reference and the `leaf_id or slugify(worktree_name)` persisted
  id, is unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-12T19:55+02:00 — 260712-PTS-L1: `load_contract` is now read+parse+validate ONLY — the
  per-read `normalize_contract_leaf_id` call and its hidden whole-tasks-tree resolution walk are gone
  (py-spy 2026-07-12 measured that walk at ~9.7s of a 15s daemon sample; master 260712-PTS decision:
  normalization is write-time/migration-only). Added `heal_contract_leaf_ids(coordination_root,
  dry_run)`, the explicit, idempotent, loud-by-report one-shot sweep that rewrites legacy stem-shaped
  leaf ids to doc ids across the active enclosure population, cheap-skipping canonical contracts via
  `leaf_refs.canonical_leaf_doc_ids`. Legacy ids now surface RAW from reads until the heal or a
  `write_contract` rewrite heals them; the heal rewrite regenerates the whole contract file (unknown
  front-matter keys / hand prose do not survive — pre-existing `write_contract` semantics). Adversarial
  review confirmed post-heal parity for doc-id changeset lookups, enclosure lifecycle joins, and reopen.
  Verification metadata pinned until closeout stamps the 260712-PTS-L1 commit.
- 2026-07-07T23:45+02:00 — 260707-HFX-L4R2: `load_contract` now asks
  `normalize_contract_leaf_id(..., keep_unresolved=True)`, so base task-resolution failures during legacy
  id mapping leave the read contract unchanged while write/start paths remain loud for non-leaf-ref
  resolution failures. Verification metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: contract load/write now normalizes proven legacy
  stem-shaped leaf ids to canonical task doc ids while leaving unresolved legacy contracts readable;
  `default_contract` preserves explicit doc ids for future writes. Verification metadata pinned until
  closeout stamps the 260707-HFX-L4 commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: `worktree_contract.py` now owns the single `ar-series-contract/v1` schema with `kind` (`series` or `leaf`), root `series-contract.md` integration contracts, leaf `enclosures/<leaf-id>/series-contract.md` contracts, parent linkage fields, and parser compatibility only for path key names inside that schema. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-13T18:45+02:00 — Slice 2c: added the additive `lifecycle_id` field (the observable-lifecycle enclosure anchor, design §1.1) on the unchanged `v1` schema — rendered as a `lifecycle:` front-matter section, parsed back via `_section`, defaulting to "" for pre-2c contracts. Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-10T09:56+02:00 — Added the `sync_log` field + `sync:` section (compact JSON scalar, backward-compatible empty default) for issue #54 sub-task D worktree_sync bookkeeping.
- 2026-05-31T12:50+02:00 — `ContractError` re-based from `ValueError` to the shared `AgentsRememberError` (imported from `agents_remember.errors`); corrected the error-type prose in Invariants And Boundaries and Repo-Internal References to name the new domain base while noting `except ValueError` callers still catch it (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Updated after contract rendering was split into section helpers during worktree package refactoring.
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
