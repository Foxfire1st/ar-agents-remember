# mcp/src/agents_remember/application/role_capsules/sources.py

## Governing Overview

[application overview](../overview.md)

## Purpose

Source admission: read an explicit, root-confined source set from a canonical tree. This is the
**one place in the role-capsule path that touches the filesystem**.

## Code Commentary

### Logic

Admission is deliberately explicit rather than eager: cit:([`CapsuleAdmissionRequest`], mcp/src/agents_remember/application/role_capsules/sources.py:38-77) names every path the
caller wants admitted, and cit:([`admit_capsule_sources`], mcp/src/agents_remember/application/role_capsules/sources.py:78-94) resolves each one inside the root,
proves it is a regular file, reads its bytes, and records their digest. It does **not** consult
the manifest to decide what to read — *the compiler needs to be able to discover that a required
block was not admitted, and a loader that only ever fetched what the manifest asked for could not
express that.*

Containment is proven **before any byte is read**, so a traversal attempt fails without the root
ever being probed outside itself. cit:([`_require_confined_relative`], mcp/src/agents_remember/application/role_capsules/sources.py:169-196) rejects an absolute path or any
path containing an empty, `.`, or `..` segment; cit:([`_require_root`], mcp/src/agents_remember/application/role_capsules/sources.py:97-113) proves the root is an existing
directory; cit:([`_read`], mcp/src/agents_remember/application/role_capsules/sources.py:114-149) performs the confined read and the
one-admission duplicate check.

The returned order is fixed — manifest first, then the four composition roots in contract order,
each alphabetically — so the admitted set itself is reproducible and two admissions of one tree
are directly comparable. cit:([`_identity_for`], mcp/src/agents_remember/application/role_capsules/sources.py:150-158) gives the manifest the reserved metadata
identity `meta:composition-manifest` rather than a block identity, because the manifest is
metadata: it is composed into no capsule and must still be read so selections can be validated
against what it declares.

### Conventions

Every requested path is a **root-relative POSIX path**. `CapsuleAdmissionRequest.manifest` is kept
separate from the four instruction-root tuples for exactly that reason.

### Invariants And Boundaries

- **Containment before reading.** No byte is read before the path is proven confined; a traversal
  attempt must not probe outside the root.
- The manifest path is read but is **not** an instruction block; its identity is the reserved
  metadata identity and it is composed into no capsule.
- The admitted order is fixed (manifest, then `core`, `role`, `operation`, `specialization`, each
  alphabetical). Do not derive it from directory listing order.
- A missing file, an unreadable root, and a path requested twice in one admission are typed
  refusals — never a skip, and never a silent dedupe.
- This module reads bytes and computes their digest. It holds no selection or composition rule;
  a rule added here would put policy in the I/O tier.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The loaded-source value this module produces and the digest it records. [1]
- The refused source set is validated against the locked plan in both directions after admission. [2]
- The application entry point that admits and then compiles, returning a refusal as a value. [3]
- The typed source-refusal base and the codes raised here. `source-root-invalid`, `source-root-missing`, `source-path-invalid`, `source-path-escapes-root`, `source-missing`, and `duplicate-identity` are raised by this module and are deliberately **not** members of `CAPSULE_STATUSES`. [4]
- Traversal, missing-source, non-directory-root, double-request and unreadable-source cases. [5]

### Cross-Repo References

No sibling-repository contract defines source admission.

No meaningful cross-repo references found.
