# mcp/src/agents_remember/application/task_projection/revision.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/task_projection/revision.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T10:30+02:00 |
| lastVerifiedCommitHash | `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| lastVerifiedCommitDate | 2026-09-16T10:52:30+02:00|
| governingOverview      | `../overview.md`                           |

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

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking the configured sources. | N/A | N/A |

## Repo-Internal References

The identity function, the plane enumeration, and the shared digest primitive it must keep using.

| Finding | Anchor | Source |
| --- | --- | --- |
| One content-addressed identity over the selection plus every projected fact. | `projection_revision` | mcp/src/agents_remember/application/task_projection/revision.py:22-47 |
| The seven fact planes identity must cover — a new plane belongs here. | `_planes` | mcp/src/agents_remember/application/task_projection/revision.py:50-63 |
| The shared digest primitive the compiler also uses, so both sides agree on one algorithm. | `compute_content_digest` | mcp/src/agents_remember/models/role_capsules/types.py:81-84 |
| The compiler-facing content digest, which is the rendered bytes rather than the selection. | `CapsuleTaskContext` | mcp/src/agents_remember/models/role_capsules/types.py:319-330 |
| The revision is assigned before rendering, so the document carries its own identity. | `_Builder` | mcp/src/agents_remember/application/task_projection/projection.py:90-515 |

## Cross-Repo References

No sibling-repository contract consumes this identity.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History

- 2026-09-16T10:30+02:00 — 260915-CAPS-L3 curator: created this card for the projection-identity
  module added by the scoped-task-context leaf (`CAPS-R03@v1`). This module did not exist until
  `CAPS-L3-EV11`: `projection.py` crossed the 600-line refactor-pressure band while being edited, so
  the identity computation was extracted here. Records the selection-plus-facts derivation, why it is
  deliberately not a digest of the rendered bytes, and the `_planes` enumeration a new plane must
  join. Verification metadata is left at the leaf base commit because the source is uncommitted —
  the governed closeout stamps the real code commit.
