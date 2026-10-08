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

**Historical (retired by MIK-R26 rule 2).** L40 once carried `knowledge_resolution: AuthoredReconciliation | None` for the authored reconciliation of a refused knowledge-dataset merge. That route was removed with the canonical database's merge step: every managed sync now merges knowledge files through the structural merge (MIK-R24 rule 8 step 3), so no authored knowledge-reconciliation decision is carried on this transport and the field does not exist in the current DTO. The field's old pairing with `resolution_action='reconcile'` and `sync_input_refusal` is retained here only as history; the current DTO's normalized closeout input and integration facts are unchanged by the removal.

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

### Repo-Internal References

- `WorktreeArgs` implements the retained boundary described above. [10]
