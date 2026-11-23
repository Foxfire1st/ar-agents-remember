# mcp/src/agents_remember/worktrees/queue/closeout_recovery.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Owns restart-safe proof of closeout's real code and memory outputs. Finalization recovery re-proves exact task refs and accepted source ancestry, without consulting a ledger row or creating a cache-maintenance commit.

## CCR-R12@v5 Current Recovery Boundary

Recovery proves accepted code trees and exact code and memory refs. The shared publisher stages the accepted tree for the configured pre-commit check, creates the commit and publishes its ref. Memory recovery re-proves an accepted output before refreshing its disposable cache. There is no ledger commit.

## Code Commentary

### Logic

`MemoryCloseoutOutcome` carries the real memory output plus onboarding/entity/route refresh data. Its `ledger_repair` field is informational cache status only. `prove_closeout_recovery_commits` requires the recorded code commit to equal the actual leaf HEAD or exact series work ref; non-external modes refuse an unexpected external-memory output.

`_prove_memory_output` requires a nonempty accepted memory output, reads the exact named series ref or clean leaf HEAD, and proves that the accepted memory base is its ancestor. Leaf cleanliness excludes only root `memory.md`; source content changes still refuse. Cache refresh occurs after the proof and cannot replace it.

`accepted_code_commit` proves a clean existing output or delegates publication of the accepted code tree, then proves the committed tree. An operation-supplied progress callback can receive intent and proof facts. It verifies the committed tree against the accepted candidate tree before returning. `resume_external_commits` reuses the proven memory output and publishes the code/memory recovery pair without replaying memory mutation.

### Conventions

Recovery state enters through typed `WorktreeArgs`. `report_operation_progress` sends evidence only to an explicitly supplied callback. Ordinary closeout uses exact Git and result evidence. Verified-existing outputs do not acquire fabricated mutation evidence.

#### Invariants And Boundaries

- A nonempty recorded commit is evidence to prove, never a suggestion to overwrite.
- Actual code and memory refs, the accepted code tree, and memory source ancestry must agree.
- Cache bytes, cache presence, and cached pairings carry no Git authority.
- The disposable queue owns no mutation evidence despite this module's package location.
- Contract publication remains the coordinator's responsibility; this owner proves outputs.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `MemoryCloseoutOutcome` contains the memory commit and informational refresh results. [1]
- `prove_closeout_recovery_commits` proves exact output refs without consulting a cache table. [2]
- `_prove_memory_output` checks memory source ancestry and substantive cleanliness before best-effort cache refresh. [3]

- `accepted_code_commit` commits or reuses the exact accepted code tree and records its proof. [4]

- `resume_external_commits` re-proves existing memory output and republishes only the code/memory pair. [5]

The current recovery primitives below establish exact two-output proof and cache-independent resumption.

### Cross-Repo References

No cross-repository implementation boundary is owned here.

No additional cross-repository evidence applies.

## R39 Series Closeout Recovery

Non-leaf closeout now records already-landed clean code: it requires a clean series/master checkout
and takes current HEAD. Leaf recovery retains commit/retry reconciliation. Series closeout cannot
become another code-commit or acceptance owner.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## 260821-CLIVE-L1 Evidence-Aware Commit Recovery

The historical journal route recorded accepted mutation intent before Git and exact proof afterwards. Verified-existing outputs still avoid inventing a mutation. The same monotonic evidence principle remains for memory output; the removed ledger-recovery stage has no successor commit path. Direct-landing recovery remains outside this owner.

## Closeout Git Recovery Contract

The current seams are `MemoryCloseoutOutcome`, `prove_closeout_recovery_commits`, `accepted_code_commit`, and `resume_external_commits`. They prove actual outputs against the admitted tree, refs and source ancestry. An optional operation callback receives progress facts independently of queue phase and ledger cache. The earlier package relocation did not make the queue an authority.


## Retired Ledger Recovery Boundary

The removed `integration/closeout/ledger_recovery.py` classified ledger byte/tree contradictions and recovered a third ledger mutation. That behavior is intentionally gone. Its durable principles remain here: recovery advances only proved outputs, recorded commit identity is immutable, and queue state cannot substitute for journal evidence. There is no current source owner for reconstructing a ledger commit, so its old one-to-one sidecar is retired.

The old sidecar's 2026-08-25 creation provenance was: “Created during PDLS whole-system reconciliation after source and requirement review. Verification remains closeout-owned.” This records the retired owner's history; it does not claim current ledger authority.
