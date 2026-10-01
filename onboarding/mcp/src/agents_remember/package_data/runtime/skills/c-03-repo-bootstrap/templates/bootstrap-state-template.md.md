# bootstrap-state-template.md

## Purpose

This template defines the persistent bootstrap state file that allows `c-03-repo-bootstrap` skill runs to pause and resume across sessions, including existing-memory slice maintenance and the closeout boundary.

## Code Commentary

### Logic

The template tracks run metadata, onboarding root, source inventory gate status, phase status, areas, governing routes, slice maintenance, waves, decisions, parking lot items, blockers, deferred files, closeout boundary status, and the next recommended action.

### Conventions

`bootstrap/STATE.md` is read first and updated last in each bootstrap session. It is state and coordination memory for the bootstrap, not file-level onboarding, and it records whether closeout has merely been requested after handoff.

### Invariants And Boundaries

The state file must preserve decisions, blockers, and low-confidence parking-lot items rather than promoting them into durable facts.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The state template records bootstrap mode, memory root, onboarding root, branch, topology, source inventory status, and phase status across the full `c-03-repo-bootstrap` skill lifecycle. [1]
- The state template tracks areas, governing routes, slice maintenance, waves, decisions, parking lot items, blockers, deferred files, closeout boundary status, and next action. [2]
- `c-03-repo-bootstrap` skill requires every bootstrap to maintain `bootstrap/STATE.md` from this template. [3]

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.
