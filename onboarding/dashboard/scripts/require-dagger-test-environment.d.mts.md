# dashboard/scripts/require-dagger-test-environment.d.mts

## Governing Overview

[dashboard quality-scripts overview](overview.md)

## Purpose

Declare the TypeScript surface of the dashboard's canonical Dagger-environment validator.
This is a type companion only; it owns no runtime authority or fallback behavior.

## Code Commentary

### Logic

The declaration mirrors the two string constants, the pure validator returning
`string | null`, its optional environment/reader injections, and the throwing facade with
an optional subject label.

### Conventions

Keep this declaration byte-for-contract aligned with the ESM implementation's exports.

### Invariants And Boundaries

- The optional parameters exist for typing the implementation's test seams; they do not weaken
  production admission.
- The file declares no nonce writer, alternate path, bypass, configuration owner, or executor.
- Runtime truth remains in `require-dagger-test-environment.mjs`.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation governs this repository-owned declaration.

No relevant external documentation was required.

### Repo-Internal References

- The declaration exposes the constants, pure validator, and throwing facade. [1]
- Runtime validation and refusal behavior live in the paired ESM file. [2]

### Cross-Repo References

No cross-repository boundary is owned by this file.

No meaningful cross-repository references were found.
