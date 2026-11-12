# mcp/src/agents_remember/models/role_capsules/sources.py

## Governing Overview

[models overview](../overview.md)

## Purpose

The **locked instruction-unit plan**, the loaded-source value, and the identity helpers that give
every block and skill reference one canonical spelling. Building the plan before reading anything
is what makes the "a required block is missing" check non-vacuous.

## Code Commentary

### Logic

cit:([`CapsuleDeclaredInstruction`], mcp/src/agents_remember/models/role_capsules/sources.py:32-49) is one *declared* instruction unit — a composition root
plus the block identity it must resolve to, plus the authorities that routed it.
cit:([`CapsuleSource`], mcp/src/agents_remember/models/role_capsules/sources.py:50-104) is the loaded counterpart: identity, composition root,
root-relative path, raw `content` bytes, and the `revision` that is the content digest of
those bytes.

The ordering rule is explicit: *the plan says which identities must resolve, and loading is
validated **against** the plan rather than defining it.* A loader that only ever fetched what
the manifest asked for could not express "this required block was never admitted" — which is
exactly the defect class the compiler must be able to report.

`CapsuleSource` carries **three guards of its own**, all reachable and all tested:

- its declared `revision` must equal the digest of its own bytes, or the value is refused — a
  source whose revision is not content-addressed breaks determinism at its root;
- cit:(["except UnicodeDecodeError as error:"], mcp/src/agents_remember/models/role_capsules/sources.py:85-101) decodes the bytes as UTF-8 and refuses
  **`source-not-utf8`** when they do not decode; and
- a source that decodes to nothing but whitespace is refused as **`source-empty`**, a typed
  `CapsuleSourceError` on the same boundary — *not* a bare `ValueError` escaping
  `CapsuleSource.text` (defect **D25**, repaired by `260915-CAPS-L11`). The two refusals are one
  class of defect and take one shape deliberately: `compile_admitted_capsule` catches only
  `CapsuleCompilationError`, so an untyped raise here would surface to an operator as a
  traceback rather than as the named refusal the compiler's own boundary promises. Emptiness is
  discovered while blocks are composed — *after* admission succeeded and a real manifest parsed —
  so the guard is reachable only through a real composition, which is why the leaf's case drives
  the shipped corpus rather than a fixture.

**The identity helpers are one vocabulary, and they cover skills as well as blocks.**
cit:([`instruction_identity`], mcp/src/agents_remember/models/role_capsules/sources.py:145-148) renders a block identity as `"<root>:<name>"`;
cit:([`specializations_declared_identity`], mcp/src/agents_remember/models/role_capsules/sources.py:151-172) resolves a nested
`specializations/<group>/<name>.md` to the same identity regardless of grouping folder;
cit:([`skills_declared_identity`], mcp/src/agents_remember/models/role_capsules/sources.py:175-185) renders a **skill** identity as `"<origin>#<skill>"` —
the origin is part of the identity because a bare skill name collides across servers, so the same
name from two servers is deliberately two different references; cit:([`shared_core_reference`], mcp/src/agents_remember/models/role_capsules/sources.py:205-208) names a
shared core block; and cit:([`root_of_identity`], mcp/src/agents_remember/models/role_capsules/sources.py:188-202) answers which composition root an identity belongs to
**for both shapes** — `<root>:<name>` carries its root, while a skill identity does not and is
recognised by its separator instead. Having exactly one function answer that is what keeps the
admitted-root agreement check and the identity index from disagreeing about skill identities.

Two module constants carry the on-disk convention: cit:([`INSTRUCTION_FILE_SUFFIX`], mcp/src/agents_remember/models/role_capsules/sources.py:27-28) and
cit:([`SPECIALIZATION_ROOT_DIRECTORY`], mcp/src/agents_remember/models/role_capsules/sources.py:27-28).

### Conventions

Every path here is **root-relative POSIX**. A `CapsuleSource.revision` is always the digest of
the bytes actually held in `content`; it is never copied from the manifest. Skill identities use
`#` and block identities use `:`; do not conflate the separators.

### Invariants And Boundaries

- This module holds values, their guards, and identity rules only. It reads no file — the
  filesystem lives in `mcp/src/agents_remember/application/role_capsules/sources.py`.
- A declared plan is built **before** any read. Do not reorder that: deriving the plan from what
  was successfully loaded would make a missing mandatory block unrepresentable.
- The declared identity of a nested specialization is path-invariant across grouping folders;
  two paths that resolve to one identity are a duplicate, not two blocks.
- `content` and `revision` must agree. A source whose revision was not computed from its own
  bytes breaks the "same bytes compile to the same capsule" property at its root.
- **`source-not-utf8` is raised here**, in the value layer, not in the application layer. A
  source that does not decode is a defect; it is never truncated, replaced, or decoded leniently.
- **`source-empty` is raised here too**, as a typed `CapsuleSourceError` rather than a
  `ValueError` (D25, `260915-CAPS-L11`). An admitted source that decodes to whitespace only is a
  source defect of the same class as the non-UTF-8 one: it is refused by name, with the source
  path and a next action, and it never escapes `CapsuleSource.text` as an exception the
  compiler's refusal boundary does not catch.
- `skills_declared_identity` requires a **non-blank** origin and name and raises `ValueError`
  otherwise; identity is `origin + skill`, so dropping the origin silently merges two servers'
  skills into one reference.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The value types these shapes are composed from and the shared digest guards. [1]
- The admission boundary that reads the bytes these values carry. [2]
- The module that proves the admitted set agrees with this declared plan in both directions, including every declared skill root. [3]
- The resolution step that reduces each declared identity to one block. [4]
- The identity helper the carried skill reference is built from: `skills_declared_identity` renders the skill identity, and the compiler's `skill_references` calls it once per skill the seat declares. [5]
- Admission preserves content-addressed revisions and refuses a missing source. [6]
- The value guards for this module's declared `CapsuleSource.text`, including the non-UTF-8 refusal. [7]

### Cross-Repo References

No sibling-repository contract defines these values.

No meaningful cross-repo references found.
