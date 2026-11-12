# coding-guidelines.md

## Purpose

This file is the coding-guidelines starter for a memory layer.

## Code Commentary

L23 adds clean-quality guidance for native POSIX subprocesses, enclosure-owned self-overwriting
reports, configured pytest parallelism, and the single pinned Dagger Ubuntu graph. For Agents
Remember, Dagger is the only acceptance environment: one targeted leaf-closeout run and one full
master-integration run both use an explicit diff base. Leaf integration and series closeout do not
rerun acceptance. Host pytest/wrapper runs are refused, and a failed Dagger run never falls back.

### Logic

The example tells users to keep concrete project preferences in the target repository's memory layer. It provides starter guidance for compatibility, legacy code, deletion, cleanup, and protected artifacts.

### Conventions

The generic example lives under the memory-repo example folder because coding rules are normally repository-specific.

### Invariants And Boundaries

Compatibility layers are discouraged unless required by public contracts, persisted data, staged rollout, or explicit user request.

### Todos

None.

### Docs References

No external documentation is needed.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The example says repository-specific coding guidance belongs in the target memory root. [1]
- The example documents compatibility and cleanup rules for memory-layer coding guidance. [2]

### Cross-Repo References

No sibling repository evidence is needed.

No meaningful cross-repo references found.

## R39 Generic Acceptance Example

The default guidelines require onboarding to name the repository permitted executor/environment,
scopes, bases, resource policy, retry rules, evidence, and refusal behavior. They fix cadence at
leaf closeout and master integration while forbidding inherited runner assumptions, compatibility
fallbacks, and self-disabling required gates.
