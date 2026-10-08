# test_terminal.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks real PTY write/read, cleanup when spawning never starts, and real tmux ensure/attach behavior independent of launcher identity. The tmux case remains conditioned on its actual environment availability. The file no longer claims the broad fake-registry, copy-mode, resize and terminal-death matrix.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Readiness And Resource Isolation

`_read_until` accumulates actual PTY output until the named marker arrives, with the shared hang
guard only preventing an endless read. Test assertions do not measure scheduler speed. The ordinary
pytest environment provides a private tmux server directory and scrubs inherited launcher identity.
The integration teardown closes the host and kills only its named session with a bounded command
using the sanitized tmux client environment. Availability skips remain explicit.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Write then read roundtrip [1]
- A spawn that never started leaves no pty fd behind [2]
- Real tmux ensure and attach ignore launcher identity [3]

- Actual PTY marker arrival governs readiness under the shared guard. [4]
- The real tmux test reclaims its named test session through the sanitized client environment. [5]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
