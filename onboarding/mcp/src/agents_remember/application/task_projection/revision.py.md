# mcp/src/agents_remember/application/task_projection/revision.py

## Governing Overview

[application overview](../overview.md)

## Purpose

The projection's own revision identity, computed from its inputs. It answers "which selection over
which facts produced this document", so a consumer can decide whether a pinned projection is still
current. It stores nothing and is not a second task database.

## Code Commentary

### Logic

`projection_revision` builds one canonical line list and digests it through the compiler's own
`compute_content_digest`. The lines are the binding (task reference, accepted document digest, kind,
altitude), the selection (role, operation, branch, documents read, documents only referenced,
whether knowledge expansion was admitted), one line per requirement declaration, and then every
fact from every projected plane. Because the revision is computed from the **selection and the
facts** rather than from the rendered bytes, the rendered document can carry its own revision and
the digest pair stays meaningful in that order.

It moves when the admitted branch, the accepted task-document bytes, the read set, an owned
packet's content or any projected fact moves — which is exactly the property a later consumer needs
to decide whether its pinned projection is still current.

`_planes` enumerates the seven fact planes the revision covers. A new projected plane must be added
there, or a change to that plane's facts will not move the revision.

### Invariants And Boundaries

- The revision is derived from **selection plus facts**, never from `markdown`. Digesting the
  rendered bytes would make the revision a function of its own output.
- `projection_revision` is not a content digest of the document; `CapsuleTaskContext.content_digest`
  is the digest of exactly the rendered bytes. The two are separate on purpose — keep both.
- The order of the digest lines is part of the identity. Reordering them changes every revision.
- Every fact plane must appear in `_planes`. A plane missing there silently stops affecting identity.
- This module opens no file and holds no state.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking the configured sources.

### Repo-Internal References

The identity function, the plane enumeration, and the shared digest primitive it must keep using.

- One content-addressed identity over the selection plus every projected fact. [1]
- The seven fact planes identity must cover — a new plane belongs here. [2]
- The shared digest primitive the compiler also uses, so both sides agree on one algorithm. [3]
- The compiler-facing content digest, which is the rendered bytes rather than the selection. [4]
- The revision is assigned before rendering, so the document carries its own identity. [5]

### Cross-Repo References

No sibling-repository contract consumes this identity.

No meaningful cross-repo references found.
