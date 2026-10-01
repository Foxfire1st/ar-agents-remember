# mcp/src/agents_remember/application/role_capsules/__init__.py

## Governing Overview

[application overview](../overview.md)

## Purpose

The import surface for the admitted-context resolution and composition boundary of role
capsules — the package that owns the I/O the pure compiler refuses to do.

## Code Commentary

### Logic

The package docstring states its scope exactly: this package owns resolving a confined source
root, reading the exact source set an admitted binding names, and returning a refusal as a value
with its explanation. **It holds no selection rules of its own** — selection lives in
`agents_remember.models.role_capsules`.

Only two names are exported, and the pairing is the contract:
cit:([`CapsuleAdmissionRequest`, `admit_capsule_sources`], mcp/src/agents_remember/application/role_capsules/__init__.py:13-16) describe *what to read*, and
cit:([`CapsuleCompilationOutcome`, `compile_admitted_capsule`], mcp/src/agents_remember/application/role_capsules/__init__.py:9-12) describe *the one call that reads and compiles*.

### Conventions

Consumers import from this package rather than from `compilation` or `sources` directly. A new
public name is added to `__all__` in the same edit.

### Invariants And Boundaries

- The package is the I/O boundary: this is the only role-capsule package that opens a file.
- It holds no selection or composition rule; adding one here would put policy in the I/O tier and
  split the compiler's decision surface in two.
- `__all__` is the authoritative export list and is deliberately short — four names, matching the
  two responsibilities.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The admitted compile entry point this package exports. [1]
- The root-confined source admission this package exports. [2]
- The pure compiler this boundary feeds, which owns every selection rule. [3]
- The sibling model package whose contract this boundary resolves inputs for. [4]

### Cross-Repo References

No sibling-repository contract consumes this boundary.

No meaningful cross-repo references found.
