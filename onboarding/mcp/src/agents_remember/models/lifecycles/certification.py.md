# mcp/src/agents_remember/models/lifecycles/certification.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

No configured domain documentation applies.

### Repo-Internal References

- `RetainedCertificationBytes` owns the described value or transition boundary. [1]
- `SelectedRecoveryDecision` owns the described value or transition boundary. [2]
- `CertificationPredecessor` owns the described value or transition boundary. [3]
- `SelectedGateTerminal` owns the described value or transition boundary. [4]
- `OperationCertificationState` owns the described value or transition boundary. [5]
- `validate_certification_owner` owns the described value or transition boundary. [6]
- `validate_certification_transition` owns the described value or transition boundary. [7]
- `_validate_terminal_transition` owns the described value or transition boundary. [8]

### Cross-Repo References

No cross-repository implementation boundary is owned by this file.

No cross-repository reference is required.
