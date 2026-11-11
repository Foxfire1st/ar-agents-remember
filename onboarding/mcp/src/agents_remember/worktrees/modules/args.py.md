# mcp/src/agents_remember/worktrees/modules/args.py

## Purpose

Defines the typed cross-layer DTO that carries worktree operation inputs from
the MCP application entry points and the worktree CLI into the worktree domain functions.
`WorktreeArgs` gives every layer a single explicit field set to read and write
instead of a loosely typed `argparse.Namespace`.
## Code Commentary

### Logic

The internal transport carries one normalized code/memory closeout input and the actual landed code/memory-content commits. Integration has no separate ledger commit message, and PR landing has no ledger commit argument. Consumer-cache data never enters the Git output tuple.

`WorktreeArgs` carries the optional `certification_profile: Path | None` field: the configured repository-relative certification profile reference forwarded by the application entry points and lifecycle worker into closeout/integration, which the quality gate resolves and admits before any code commit.

`WorktreeArgs` carries worker-injected operation key/generation, candidate-tree, and progress callback fields; CLI namespaces cannot populate these plane-owned controls.

The DTO carries no authored knowledge-reconciliation field (`knowledge_resolution` does not exist), and `sync_input_refusal` admits only `continue` or `cancel` as a resolution action.

`WorktreeArgs` is a `@dataclass(frozen=True)`. Every field carries a default, so
any operation can construct just the subset it needs without supplying the rest;
fields are grouped by concern (coordination/repository resolution, start inputs,
provider setup, lifecycle flags, and normalized closeout input and integration facts). The
frozen dataclass means callers that need a variant produce a new instance rather
than mutating an existing one.

`from_namespace` builds an instance from an `argparse.Namespace`, falling back to
the field defaults. It iterates the dataclass `fields`, copies only attributes
the namespace actually defines (`hasattr` guard), and applies them onto a default
instance via `replace`. This tolerates argparse subparsers that only populate the
arguments they declare and tests that construct partial namespaces, so any field
the namespace omits keeps its dataclass default rather than raising.

`retry_provider_setup: bool = False` is an internal DTO field.
Existing-contract retry refuses while a live setup heartbeat exists, then uses
the normal provider preflight. Both retired CGC/GrepAI provider IDs are always
disabled, so this path does not relaunch their background setup.

`stale_base_choice: str | None = None`: the stale-base preflight
recovery selector for worktree start — `fast-forward` (ff stale local source
branches, then proceed) or `proceed-stale` (explicit override); `None` means
block when a source branch is behind/diverged from its upstream.

`memory_sync_choice: MemorySyncChoice | None` narrows the admitted memory plan to
`merge-memory` or `skip-memory`. `resolution_action: SyncResolutionAction | None` narrows recovery
control to `continue` or `cancel`. Both aliases are owned by the public worktree model and travel
unchanged through application/registration/CLI adapters. The transaction journals the admitted
memory choice; a later continue/cancel addresses the same contract generation and cannot silently
change it.

`sync_source: SyncSource | None = None` names the one selectable sync source besides the contract's
own source line: `repository-default`, which makes a sync pull each repository's default branch
while keeping the contract's base pair. `None` means the contract's own line. The alias lives in the
public worktree model with the other sync vocabularies, and the MCP `worktree_sync` tool carries it in
through the application layer's resolution input; the worktree CLI parser declares no argument for
it, so a CLI namespace leaves it `None`. `sync_input_refusal` refuses any other value, and the
transaction journals the admitted source so a continue or cancel cannot change it.

`lifecycle_id: str = ""`: the observable-lifecycle id the application entry point
resolves (the active lifecycle's id, or a fresh mint when none is active) and
threads through to `_build_start_contract`, which stamps it into the contract's
`lifecycle:` block — the durable resume anchor.

`gate_policy: GatePolicy = DEFAULT_GATE_POLICY` is the parsed
server-side gate delegation policy threaded from MCP config into worktree
closeout. Existing CLI/tests that omit it keep the all-human default.
### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.
### Invariants And Boundaries

The ledger is a computed consumer cache; it cannot supply an additional Git output or lifecycle prerequisite.
### Todos

None recorded for the ledger-retirement boundary.
## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

- `WorktreeArgs` implements the retained boundary described above. The following current source boundaries establish the ledger-retirement behavior. [10]

The following current source boundaries establish the ledger-retirement behavior.

- `report_operation_progress` publishes progress through the exact worker-owned callback. [13]

- Public sync choice and resolution-action vocabularies are owned once by the worktree model. [14]

- Provider setup config is typed through the companion worktree models module. (`WorktreeProviderSetupConfig`) [15]


- Worktree CLI builds argparse namespaces that this DTO adapts via `from_namespace`. [16]


- Gate delegation policy model (kernel-owned since L9). [17]

### Cross-Repo References

No separately configured cross-repository implementation governs this file; any external-memory repository is addressed by the task contract.

No additional cross-repository evidence applies.
## Series-Contract Notes

`WorktreeArgs` carries `parent_task` and `leaf_id` through CLI, MCP, and source API entrypoints, giving all operations the same active-task and leaf-selection inputs.
## L23 Final Candidate Disposition

The internal worktree argument DTO carries accepted candidate, task contract, and operation-progress
facts between modules. Public callers still address the canonical task and never supply private
operation, process, lease, or approval identifiers.
## 260821-CLIVE-L1 Internal Transport

`WorktreeArgs` carries no raw code and memory closeout message strings. Closeout execution receives one optional `EffectiveCloseoutInput`, populated only after validation; integration and PR landing carry only their actual code/memory output facts. This prevents worker, preview, recovery, and commit code from independently normalizing or defaulting closeout subjects.
## 260821-CLIVE-L2 Current Contract

The current source seams include `WorktreeArgs`, `report_operation_progress`. This module remains a public execution adapter over closed admission and exact mutation-owner reread; it does not duplicate reader exception families or lifecycle authority.
### Reconciled Source Evidence

- Inputs shared by the worktree application layer, CLI, and domain functions. [11]


- Advance the plane-owned operation when this call runs under its detached worker. Source caption: `report_operation_progress` [12]


## Current Landed Composition

The internal `integration_certification_owner` field carries the typed journal-owned integration certification continuation. It defaults to absent and is not a public authorization token; the integration owner validates its own authority.

## Governing Overview

[Governing route overview](overview.md)
