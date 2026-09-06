# mcp/src/agents_remember/worktrees/integration/certification.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/certification.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:12:42+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

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

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `IntegrationCertificationOwner` owns the described selection or observation boundary. | `IntegrationCertificationOwner` | mcp/src/agents_remember/worktrees/integration/certification.py:61-63 |
| `IntegrationCertificationRequest` owns the described selection or observation boundary. | `IntegrationCertificationRequest` | mcp/src/agents_remember/worktrees/integration/certification.py:67-72 |
| `LoadedIntegrationCertification` owns the described selection or observation boundary. | `LoadedIntegrationCertification` | mcp/src/agents_remember/worktrees/integration/certification.py:76-95 |
| `_current` owns the described selection or observation boundary. | `_current` | mcp/src/agents_remember/worktrees/integration/certification.py:112-156 |
| `authorize_integration_start` owns the described selection or observation boundary. | `authorize_integration_start` | mcp/src/agents_remember/worktrees/integration/certification.py:159-163 |
| `_identity` owns the described selection or observation boundary. | `_identity` | mcp/src/agents_remember/worktrees/integration/certification.py:166-189 |
| `prepare_integration_certification` owns the described selection or observation boundary. | `prepare_integration_certification` | mcp/src/agents_remember/worktrees/integration/certification.py:192-216 |
| `protected_integration_generations` owns the described selection or observation boundary. | `protected_integration_generations` | mcp/src/agents_remember/worktrees/integration/certification.py:225-232 |
| `_load` owns the described selection or observation boundary. | `_load` | mcp/src/agents_remember/worktrees/integration/certification.py:235-296 |
| `_select` owns the described selection or observation boundary. | `_select` | mcp/src/agents_remember/worktrees/integration/certification.py:299-315 |
| `_require_interrupted` owns the described selection or observation boundary. | `_require_interrupted` | mcp/src/agents_remember/worktrees/integration/certification.py:318-340 |
| `require_resumable_integration` owns the described selection or observation boundary. | `require_resumable_integration` | mcp/src/agents_remember/worktrees/integration/certification.py:343-349 |
| `select_integration_terminals` owns the described selection or observation boundary. | `select_integration_terminals` | mcp/src/agents_remember/worktrees/integration/certification.py:352-364 |
| `select_completed_integration` owns the described selection or observation boundary. | `select_completed_integration` | mcp/src/agents_remember/worktrees/integration/certification.py:367-441 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | N/A | N/A |

## Update History

- 2026-09-06T15:12:42+00:00 — Created from actual source at c69d5171187fa1957025e393270db9f5a864ab14; documented original evidence, current owner checks and selection/completion boundaries. Source verification does not claim suite execution or CCR acceptance.
