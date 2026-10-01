# mcp/src/agents_remember/worktrees/integration/certification.py

## Governing Overview

[Governing integration overview](overview.md)

## Purpose

Owns original full-gate certification selection and completion publication through the live integration operation’s CAS.

## Code Commentary

### Logic

`IntegrationCertificationRequest` carries the exact contract, quality target/plan, live operation owner and optional completion attestation. `_current` requires the same running uncancelled integrate operation, key/generation/worker identity and integration authority; it verifies target repository identity, the admitted code commit, actual HEAD and staged tree. Initial preparation freezes the full run and selects its original reference before executor invocation.

`_load` compares the immutable selection with current request identity, reopens the original frozen run, verifies full mode/repository/candidate tree and all current or historical physical terminal evidence, and checks publication attestations and the certificate chain. It derives the reuse plan from those exact originals. Protected generations include both current and original interrupted publications. The executor receives original certificates and their retained result/publication bytes.

`_select` validates the proposed graph before a heartbeat-tolerant observation and expected-current CAS. Terminal selection preserves the exact interrupted last attempt when replacing it. The retained decoder must explicitly mark interruption; a selected red catalog refuses unchanged retry and requires a corrected candidate/successor operation.

`select_completed_integration` reparses the proposed completion model, requires the original selected frozen-run and terminal references, compares the original completion fingerprint/base/cap, and binds the admitted code commit, actual frozen candidate tree and exact attestation. A different already-selected completion is refused. The completed record is selected by one live journal CAS with readback.

### Conventions

Keep selected execution authority separate from completed quality certification. Obtain starts through `authorize_integration_start` after sandbox/retained-evidence preparation; original selected references remain the source of resume and pruning protection.

### Invariants And Boundaries

- A missing owner, cancellation, moved repository/HEAD/staged candidate, changed profile/base/cap or lost CAS refuses.
- The selected run is full-mode authority; merely constructing its record does not prove that full execution happened.
- Completion cannot replace the original references or substitute the operation record’s candidate tree for the admitted code output.
- Historical interrupted evidence is reopened before reuse/protection; red evidence is retained and cannot authorize unchanged retry.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

No configured domain documentation applies.

### Repo-Internal References

- `IntegrationCertificationOwner` owns the described selection or observation boundary. [1]
- `IntegrationCertificationRequest` owns the described selection or observation boundary. [2]
- `LoadedIntegrationCertification` owns the described selection or observation boundary. [3]
- `_current` owns the described selection or observation boundary. [4]
- `authorize_integration_start` owns the described selection or observation boundary. [5]
- `_identity` owns the described selection or observation boundary. [6]
- `prepare_integration_certification` owns the described selection or observation boundary. [7]
- `protected_integration_generations` owns the described selection or observation boundary. [8]
- `_load` owns the described selection or observation boundary. [9]
- `_select` owns the described selection or observation boundary. [10]
- `_require_interrupted` owns the described selection or observation boundary. [11]
- `require_resumable_integration` owns the described selection or observation boundary. [12]
- `select_integration_terminals` owns the described selection or observation boundary. [13]
- `select_completed_integration` owns the described selection or observation boundary. [14]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

No cross-repository reference is required.
