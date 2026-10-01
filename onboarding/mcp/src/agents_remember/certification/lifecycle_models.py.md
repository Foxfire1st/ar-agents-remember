# mcp/src/agents_remember/certification/lifecycle_models.py

## Governing Overview

[Certification overview](overview.md)

## Purpose

Owns the immutable, content-addressed lifecycle boundary records of CCR-R05: the exact-candidate
observation, prior-red disposition envelope/manifest, lifecycle admission manifest, certificate
recovery record, and durable finalization journal/manifest. The digest-bearing manifests and recovery
record verify their semantic-envelope digests; observation and journal models enforce their own
shape constraints. Shared individual corrective dispositions now live in the model-layer package.

## Code Commentary

### Logic

The durable finalization order is code commit, external-memory commit, then contract
finalization. A consumer ledger cache has no finalization leg or write intent; the journal still
binds the actual applicable outputs and permits only one unfinished intent at a time.

The local literals fix authority/generated-input status and the three durable finalization legs.
`ExactCandidateObservation` carries owner-produced identities and statuses; conflicted worktrees
must name exactly their sorted unique conflict paths. Shared `CorrectiveInputChange` and
`RedCatalogDisposition` values are imported from `models/certification/corrective.py` by their
consumers; this domain module retains the prior-red envelope and manifest.

Prior-red, admission, recovery and finalization manifests verify their own semantic-envelope
hashes. Admission declares zero gate starts in its semantic shape; recovery binds the original
admitted certificate identities, input changes and compiled reuse plan. These literals and hashes
are not process-execution evidence.

`FinalizationBoundaryObservation` carries current owner observations for the finalization
validator; constructing it does not re-observe Git, approval or door authority. `DurableFinalizationLeg`
validates authority/intended/proven-output shape. `FinalizationJournalState` preserves ordered
code, external-memory and contract legs, permits at most one unfinished intent, and
requires monotonic progress. Its `next_leg` prefers the retained intent before a pending leg.
The finalization envelope requires its explicit `nextLeg` to equal that derived journal edge.

### Conventions

Every model is a frozen `FrozenContractModel` with digest fields pattern-checked to lowercase
hex. Digest-bearing manifests verify their own envelopes; the actual authority observations and
read/write currentness remain responsibilities of the admission and finalization owners.

### Invariants And Boundaries

- Digest fields use lowercase SHA-256 shape. Each digest-bearing manifest refuses a mismatch
  with its own envelope; supplied authority digests still require their owner’s evidence.
- An applicable finalization leg always carries write authority; `not-applicable` legs carry
  none.
- The finalization journal never reorders the durable code/memory/contract legs and never
  retains two unfinished write intents.
- The candidate observation is admission input; the model checks shape, not authority truth.

### Todos

Authority observation and engine behavior are owned by `lifecycle_admission` /
`lifecycle_recovery`, not by the model layer.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The source below proves the
current journal semantics; the task history explains the retired ordering.

The historical CCR-R05@v3 plan required code, external-memory, ledger, and contract finalization
legs. LCA-L9 retires the ledger leg. The surviving requirement journals each real durable leg so
an unchanged interruption resumes the exact publication path without rerunning gates.


No configured external Domain Documentation source applies.

### Repo-Internal References

- Finalization order contains code, external memory, and contract publication only. [1]
- The exact-candidate observation is the admission boundary's owner-produced input. [2]
- Prior-red corrective and recovery records bind digests to semantic envelopes. [3]
- The durable leg journal fixes order, intent exclusivity, monotonic progress, and the resume edge. [4]
- Certificate identities and creation provenance are imported from the R21 certificate owners. [5]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

No cross-repository implementation is referenced.
