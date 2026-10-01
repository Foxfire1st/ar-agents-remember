# dashboard/src/test/fixtures/submitScenarios.ts

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

Provides named, deterministic FEUI-L5 submission scenarios shared by transport, lifecycle, store,
and composer tests.

## Code Commentary

### Logic

Fixtures encode receipt/status/withdrawal shapes and request provenance for accepted, queued,
ambiguous, rejected, authority-loss, dispatch-race, and draft-recovery paths. Centralizing these
records keeps tests aligned to the exact public lifecycle alphabet and epoch/request correlation
instead of inventing subtly incompatible payloads per suite.

### Invariants And Boundaries

- Fixtures contain normalized public evidence only; vendor raw evidence is intentionally absent.
- Request ids, epochs, observation versions, text provenance, and draft revisions are explicit where
  the scenario depends on them.
- Fixtures are test data, not a second implementation of the evidence fold.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository.

No configured live domain-documentation source was available.

### Repo-Internal References

- The lifecycle algebra defines the vocabulary represented here. [1]
- The frontend authority client consumes the public status and withdrawal shapes. [2]

### Cross-Repo References

No meaningful cross-repo references found.

Fixtures are internal to this repository's dashboard tests.
