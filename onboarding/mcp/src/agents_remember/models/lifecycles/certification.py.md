# mcp/src/agents_remember/models/lifecycles/certification.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/certification.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:06:50+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing lifecycle overview](overview.md)

## Purpose

Defines the immutable closeout certification selection held by one lifecycle journal generation and the legal append-only transitions.

## Code Commentary

### Logic

`RetainedCertificationBytes` binds nonempty serialized owner output to exact UTF-8 SHA-256. `SelectedRecoveryDecision` pairs an original recovery-object reference with the optional exact memory observation used for its compilation. A predecessor names the original generation and frozen run/candidate-authority/admission references. Selected gate terminals bind the result, optional green certificate, retained publication bytes and optional certified predecessor.

`OperationCertificationState` keeps original authority, inherited inputs, recovery decisions, current terminals and original uncertified terminal history. It checks reference kinds, ordered unique current/input gates, required predecessor identity for inherited inputs, and canonical uncertified history. Adjacent duplicate recovery decisions are refused, while a meaningful A→B→A observation sequence remains representable within the 256-entry bound.

Owner validation binds selection to the exact closeout operation key/generation. Changed transitions require a live noncancelled owner, retain immutable admission fields, append recovery decisions and append terminals. Replacing the last uncertified terminal is permitted only at the same gate with the earlier prefix preserved and the exact original appended to history. An unchanged transition is an idempotent no-op.

### Conventions

Decode retained bytes with their domain owner before selection or use. The journal/store performs CAS; these models and validators do not publish objects or select themselves.

### Invariants And Boundaries

- Object existence or constructing a valid model does not confer selected journal authority.
- Predecessor reuse requires a certificate; uncertified original attempts remain in history.
- Recovery decisions bind their actual memory observations; identical adjacent selections cannot be appended twice.
- Removal, replacement of frozen authority, or loss of original uncertified history is refused on a changed transition.

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
| `RetainedCertificationBytes` owns the described value or transition boundary. | `RetainedCertificationBytes` | mcp/src/agents_remember/models/lifecycles/certification.py:17-30 |
| `SelectedRecoveryDecision` owns the described value or transition boundary. | `SelectedRecoveryDecision` | mcp/src/agents_remember/models/lifecycles/certification.py:33-43 |
| `CertificationPredecessor` owns the described value or transition boundary. | `CertificationPredecessor` | mcp/src/agents_remember/models/lifecycles/certification.py:46-62 |
| `SelectedGateTerminal` owns the described value or transition boundary. | `SelectedGateTerminal` | mcp/src/agents_remember/models/lifecycles/certification.py:65-80 |
| `OperationCertificationState` owns the described value or transition boundary. | `OperationCertificationState` | mcp/src/agents_remember/models/lifecycles/certification.py:83-131 |
| `validate_certification_owner` owns the described value or transition boundary. | `validate_certification_owner` | mcp/src/agents_remember/models/lifecycles/certification.py:134-146 |
| `validate_certification_transition` owns the described value or transition boundary. | `validate_certification_transition` | mcp/src/agents_remember/models/lifecycles/certification.py:149-178 |
| `_validate_terminal_transition` owns the described value or transition boundary. | `_validate_terminal_transition` | mcp/src/agents_remember/models/lifecycles/certification.py:181-198 |

## Cross-Repo References

No cross-repository implementation boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | N/A | N/A |

## Update History

- 2026-09-06T15:06:50+00:00 — Created from actual source at c69d5171187fa1957025e393270db9f5a864ab14; documented exact selection, refusal and transition ownership. Source verification does not assert runtime execution or CCR acceptance.
