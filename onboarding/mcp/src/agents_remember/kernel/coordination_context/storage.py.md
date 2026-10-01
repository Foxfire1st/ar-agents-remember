# mcp/src/agents_remember/kernel/coordination_context/storage.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`storage.py` resolves onboarding storage mode for a source file using parsed
storage settings and path rules.

## Code Commentary

### Logic

The module normalizes rule bases, evaluates include/exclude glob variants,
handles include and exclude file types, and returns the selected storage mode,
`disabled`, or the hybrid default for unmatched files. The boolean predicate
`is_sidecar_storage()` reports whether a storage mode writes a sidecar
(`repo-sidecar` or `memory-repo`).

### Invariants And Boundaries

- Storage decisions consume already-parsed settings; this module does not read
  settings files.
- Path-rule eligibility is separate from storage location selection.
- In non-hybrid modes, unmatched files resolve to `disabled` when path rules
  exist.

## Evidence

### Docs References

No external documentation is needed for this package-local storage policy.

No relevant external documentation is needed.

### Repo-Internal References

- JSON settings parsing produces the storage settings and path-rule models. [1]
- The storage resolver consumes `StorageSettings` path rules to select storage for a source. [2]
- Missing-onboarding checks call the storage resolver through the public facade. [3]
- Drift checks classify source onboarding storage through the public facade. [4]

### Cross-Repo References

No cross-repository evidence is needed for storage policy.

No meaningful cross-repo references found.
