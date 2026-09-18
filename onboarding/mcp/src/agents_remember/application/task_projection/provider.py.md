# mcp/src/agents_remember/application/task_projection/provider.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/task_projection/provider.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T10:30+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[application overview](../overview.md)

## Purpose

The task-projection half of the capsule compiler's task-context seam: the class that fills L2's
frozen one-method protocol, and the conversion from a computed projection into the compiler's own
`CapsuleTaskContext`. This is the L4/L5/L7 plug-in point.

## Code Commentary

### Logic

`TaskProjectionSource` is a frozen dataclass holding one `ResolvedProjectionScope` and the
`TaskProjectionRequest`. `project_detailed(binding)` returns the full computed projection;
`project(binding)` returns the capsule-facing `CapsuleTaskContext`. Both first call
`_require_same_binding`, which compares the admitted facts' task reference and work branch against
what the scope bound — **so a caller cannot resolve a scope for one leaf and compile a capsule for
another and receive a plausible-looking projection of the wrong task**. The two disagreements get
distinct statuses, `projection-binding-mismatch` and `projection-branch-mismatch`.

**It never returns `None` for an admitted binding**, even though the protocol permits it. Returning
`None` would mean "this admitted seat has no task context", and a projection that could not read its
task has not established that — it has failed. That failure is a typed `TaskProjectionSourceError`,
because a silent `None` is exactly the fallback the requirement forbids.

`task_context_of` converts a projection into the compiler's `CapsuleTaskContext`: the rendered
`markdown`, an `origin` of the form `"<PROJECTION_ORIGIN>:<task reference>"`, the
`projection_revision`, and `content_digest` — the digest of **exactly the bytes carried in
`markdown`**. That last point is load-bearing: the compiler re-verifies the digest against the bytes
before it will carry a projection at all, so a mismatch is refused there and a forged digest cannot
be smuggled through this conversion.

`PROJECTION_ORIGIN` is the single origin string, so a capsule can name where its task context came
from without a second identity vocabulary.

### Invariants And Boundaries

- `project()` never returns `None` for an admitted binding. An unprojectable task is a typed
  refusal, not an empty context.
- The scope a source was resolved for is the **only** task and branch it will project. Do not relax
  `_require_same_binding` — it is what prevents compiling task A's capsule against task B's
  projection.
- `content_digest` covers exactly `markdown`'s UTF-8 bytes. Computing it over anything else breaks
  the compiler's re-verification.
- The origin vocabulary is `PROJECTION_ORIGIN`; do not introduce a second one.
- L2's DTO is frozen. This module consumes `CapsuleBinding`, `CapsuleTaskContext` and
  `compute_content_digest` as-is and must not redefine them.

### Todos

None recorded.

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking the configured sources. | N/A | N/A |

## Repo-Internal References

The protocol implementation, the conversion, and the seam owner on the other side.

| Finding | Anchor | Source |
| --- | --- | --- |
| The protocol implementation, and the binding check that keeps one scope to one task and branch. | `TaskProjectionSource`; `_require_same_binding` | mcp/src/agents_remember/application/task_projection/provider.py:56-103; mcp/src/agents_remember/application/task_projection/provider.py:92-103 |
| The conversion into the compiler's frozen DTO, with the digest of exactly the rendered bytes. | `task_context_of` | mcp/src/agents_remember/application/task_projection/provider.py:37-52 |
| The single origin vocabulary a capsule names its task context by. | `PROJECTION_ORIGIN` | mcp/src/agents_remember/application/task_projection/provider.py:38-38 |
| The frozen one-method protocol this class fills. | `CapsuleTaskProjectionSource` | mcp/src/agents_remember/models/role_capsules/types.py:334-346 |
| The frozen DTO and the shared digest primitive, both consumed rather than redefined. | `CapsuleTaskContext`; `compute_content_digest` | mcp/src/agents_remember/models/role_capsules/types.py:319-330; mcp/src/agents_remember/models/role_capsules/types.py:81-84 |
| The compiler that accepts this source and re-verifies the supplied digest. | `compile_admitted_capsule`; `CapsuleSuppliedProjection` | mcp/src/agents_remember/application/role_capsules/compilation.py:89-120; mcp/src/agents_remember/models/role_capsules/types.py:350-357 |
| The refusal this module raises instead of returning `None`. | `TaskProjectionSourceError` | mcp/src/agents_remember/errors.py:516-560 |
| The case that proves the provider serves the compiler protocol and the knowledge seam stays optional. | `test_the_provider_serves_the_compiler_protocol_and_the_knowledge_seam_is_optional` | mcp/tests/test_task_projection.py:1232-1287 |

## Cross-Repo References

No sibling-repository contract consumes this provider directly.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `PROJECTION_ORIGIN` repointed to mcp/src/agents_remember/application/task_projection/provider.py:38-38. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_the_provider_serves_the_compiler_protocol_and_the_knowledge_seam_is_optional` repointed to mcp/tests/test_task_projection.py:1232-1287. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T10:30+02:00 — 260915-CAPS-L3 curator: created this card for the compiler-seam provider
  added by the scoped-task-context leaf (`CAPS-R03@v1`). Records that `project()` never returns `None`
  for an admitted binding (a `None` would claim "no task context" for what is really a failure), the
  binding check that prevents compiling task A's capsule against task B's projection, and the
  `content_digest`-covers-exactly-`markdown` rule the compiler re-verifies. Verification metadata is
  left at the leaf base commit because the source is uncommitted — the governed closeout stamps the
  real code commit.
