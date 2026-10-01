# mcp/tests/test_checkpoint_landing.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Pin checkpoint/final landing cell differences, explicit candidate revalidation, and terminal abandon guards for an unfinished atomic master.

## Code Commentary

### Logic

The self-contained fixture builds a sprint, one atomic master, an unfinished leaf task, and a real code repository. Memory is disabled, so the legitimate memory output is empty and no ledger placeholder is supplied.

IntegrationCellRecordingTests contrasts checkpointed with completed and presets cleanup=reopened so an unintended rewrite is observable. CheckpointResultTests verifies the same no-reclamation result through status projection with scoped service binding. SeriesCheckpointAuthorityTests proves a completed master cannot use the weaker route, an unfinished master can publish through checkpoint authority while final authority refuses it, and a stale captured candidate prevents the callback. SeriesAbandonGuardTests preserves refusal for checkpointed/completed masters and permits the never-integrated terminal case.

### Conventions

The nine definitions use constructed contract states where state writing is the subject and real repository refs where authority is tested. Git identity is supplied locally. Assertions reload the contract instead of trusting only a correct-looking payload.

### Invariants And Boundaries

- Checkpoint leaves cleanup unchanged; final landing marks cleanup pending.
- A checkpoint cannot downgrade a completed master.
- Expected candidate data remains required and is revalidated before publication.
- Already-landed masters cannot be abandoned as if nothing had been published.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Checkpoint versus final durable integration cells. [1]
- The checkpoint result retains the pre-existing cleanup state. [2]
- Completion and stale candidate publication refusals. [3]
- The landed-master abandon guard remains enforced. [4]
- Production checkpoint capture and publication authority. [5]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
