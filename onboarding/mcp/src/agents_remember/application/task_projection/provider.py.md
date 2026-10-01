# mcp/src/agents_remember/application/task_projection/provider.py

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

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking the configured sources.

### Repo-Internal References

The protocol implementation, the conversion, and the seam owner on the other side.

- The protocol implementation, and the binding check that keeps one scope to one task and branch. [1]
- The conversion into the compiler's frozen DTO, with the digest of exactly the rendered bytes. [2]
- The single origin vocabulary a capsule names its task context by. [3]
- The frozen one-method protocol this class fills. [4]
- The frozen DTO and the shared digest primitive, both consumed rather than redefined. [5]
- The compiler that accepts this source and re-verifies the supplied digest. [6]
- The refusal this module raises instead of returning `None`. [7]
- The case that proves the provider serves the compiler protocol and the knowledge seam stays optional. [8]

### Cross-Repo References

No sibling-repository contract consumes this provider directly.

No meaningful cross-repo references found.
