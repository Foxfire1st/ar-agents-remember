# mcp/src/agents_remember/worktrees/modules/args.py

## Purpose

Defines the typed cross-layer DTO that carries worktree operation inputs from
the MCP application entry points and the worktree CLI into the worktree domain functions.
`WorktreeArgs` replaces the loosely typed `argparse.Namespace` that previously
flowed across those layers (F17), giving every layer a single explicit field set
to read and write.

## Code Commentary

### Logic

The internal transport carries one normalized code/memory closeout input and the actual landed code/memory-content commits. Integration has no separate ledger commit message, and PR landing has no ledger commit argument. Consumer-cache data never enters the Git output tuple.

`WorktreeArgs` now carries an optional `quality_certification` field for the organizational full-gate proof, and (CCR-R22@v1, L22, commit `685f83c44055`) the optional `certification_profile: Path | None` field: the configured repository-relative certification profile reference forwarded by the application entry points and lifecycle worker into closeout/integration, which the quality gate resolves and admits before any code commit.

L23 adds worker-injected operation fingerprint, candidate-tree, and progress callback fields to `WorktreeArgs`; CLI namespaces cannot populate these plane-owned controls.

**L40 adds the one decided input this DTO carries, and it is deliberately a typed model rather than a loose mapping.** `knowledge_resolution: AuthoredReconciliation | None` is the authored decision one `resolution_action='reconcile'` call carries: exactly one conflict the knowledge merge refused, and which side's authored value is the reconciled one. It is typed through `models.knowledge.merge` for the same reason `resolution_action` is typed through `models.worktree` — the vocabulary is owned once and this transport only carries it — and it is optional because every operation that is not an authored reconciliation has no decision to carry. `sync_input_refusal` in the sync driver is what pairs it with its action in both directions (`reconcile` without a decision, and a decision with any other action, are refused by name), so this field cannot be read as a default or as a preference.

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

`retry_provider_setup: bool = False` (GitHub #53): on an existing contract,
worktree start relaunches background provider setup instead of attaching;
refused while a live setup heartbeat exists.

`stale_base_choice: str | None = None` (GitHub #54): the stale-base preflight
recovery selector for worktree start — `fast-forward` (ff stale local source
branches, then proceed) or `proceed-stale` (explicit override); `None` means
block when a source branch is behind/diverged from its upstream.

`memory_sync_choice: MemorySyncChoice | None` narrows the admitted memory plan to
`merge-memory` or `skip-memory`. `resolution_action: SyncResolutionAction | None` narrows recovery
control to `continue` or `cancel`. Both aliases are owned by the public worktree model and travel
unchanged through application/registration/CLI adapters. The transaction journals the admitted
memory choice; a later continue/cancel addresses the same contract generation and cannot silently
change it.

`lifecycle_id: str = ""` (slice 2c): the observable-lifecycle id the application entry point
resolves (the active lifecycle's id, or a fresh mint when none is active) and
threads through to `_build_start_contract`, which stamps it into the contract's
`lifecycle:` block — the durable resume anchor.

`gate_policy: GatePolicy = DEFAULT_GATE_POLICY` (260703-L4) is the parsed
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

The following current source boundaries establish the ledger-retirement behavior.

- `WorktreeArgs` carries normalized closeout input, actual landed code/memory facts, and the one authored knowledge decision a reconcile call may carry. [1]
- `report_operation_progress` publishes progress through the exact worker-owned callback. [2]

- Public sync choice and resolution-action vocabularies are owned once by the worktree model. (`MemorySyncChoice`; `SyncResolutionAction`) [3]
- **The authored-decision vocabulary this transport carries for a reconcile call, owned by the merge model rather than restated here.** (`AuthoredReconciliation`) [4]
- Provider setup config is typed through the companion worktree models module. (`WorktreeProviderSetupConfig`) [5]
- Worktree CLI builds argparse namespaces that this DTO adapts via `from_namespace`. (`build_parser`) [6]
- Gate delegation policy model (kernel-owned since L9). (`GatePolicy`; `DEFAULT_GATE_POLICY = GatePolicy()`) [7]

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

`WorktreeArgs` no longer carries raw code and memory closeout message strings. Closeout execution receives one optional `EffectiveCloseoutInput`, populated only after validation; integration and PR landing carry only their actual code/memory output facts. This prevents worker, preview, recovery, and commit code from independently normalizing or defaulting closeout subjects.

## 260821-CLIVE-L2 Current Contract

The current source seams include `WorktreeArgs`, `report_operation_progress`. This module remains a public execution adapter over closed admission and exact mutation-owner reread; it does not duplicate reader exception families or lifecycle authority.

### Reconciled Source Evidence

- Inputs shared by the worktree application layer, CLI, and domain functions. (`WorktreeArgs`) [8]
- Advance the plane-owned operation when this call runs under its detached worker. (`report_operation_progress`) [9]

## Current Landed Composition

The internal `integration_certification_owner` field carries the typed journal-owned integration certification continuation. It defaults to absent and is not a public authorization token; the integration owner validates its own authority.

## Governing Overview

[Governing route overview](overview.md)
