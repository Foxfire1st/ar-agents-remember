# mcp/src/agents_remember/worktrees/modules/quality/execution/sandbox.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Composes fresh or explicitly selected repository-profile admission and retained execution inputs inside the exact prepared candidate sandbox.

## Code Commentary

### Logic

`_admit_prepared_profile` loads and admits the configured profile for an ordinary fresh closeout execution. It resolves the requested mode, observes actual base/candidate source selection and admits the plan against the prepared Git tree. An explicit selected execution instead uses `_selected_profile`.

The selected path validates the supplied execution and matches frozen candidate tree, mode and repository identity. It resolves the configured profile file in the candidate and reads bounded raw bytes for source provenance. Semantic profile, selection, repository plan, executor, decoder and applicable publication declarations come from the selected frozen run; this path does not reload or reselect semantic authority from current settings.

`_write_sandbox_manifest` reobserves actual source selection and requires equality with the frozen plan. Its admission manifest binds the source/bundle/staged-overlay identities, resolved comparison base, raw profile provenance, canonical profile/plan, selected adapters, admitted runtime snapshot and declared publications. Selected suffixes also copy the verified retained report inventory and serialize the exact code-execution payload before atomic manifest publication.

### Conventions

The outer clean executor owns preparation, runtime admission, gate starts and cleanup. Keep semantic selected authority distinct from the configured file’s raw-byte provenance and from the fresh physical source observation.

### Invariants And Boundaries

- A selected execution cannot silently change candidate, mode, repository or source-selection authority.
- The manifest records an already admitted runtime; writing it does not allocate or impersonate one.
- Retained report copying uses explicit original publications and the existing sandbox lifecycle.
- This module does not run the suite, select journal terminals or finalize a worktree.

### Todos

None recorded for this file's bounded responsibility.

## Evidence

### Docs References

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References

- Fresh preparation loads configured authority and observes actual source selection. [1]
- Selected preparation retains frozen semantic authority and bounded raw-file provenance. [2]
- Manifest publication rechecks source selection and binds actual retained transport. [3]

### Cross-Repo References

No separately configured cross-repository source is used for this card.
