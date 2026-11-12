# mcp/src/agents_remember/application/task_projection/rendering.py

## Governing Overview

[application overview](../overview.md)

## Purpose

Render one computed projection as the Markdown a model actually reads — the model-visible half of
the projection. It carries the facts and the source links; it does not carry the diagnostic half
(the read plan, the selection record, the document digest), which stays on the value for an operator
or a reviewer.

## Code Commentary

### Logic

`render_markdown` assembles blocks in a fixed order: a header, the binding block, then each channel
the operation selected in `_CHANNEL_ORDER`, then portfolio facts, then series context, then the
closure. `_CHANNEL_RENDERERS` maps each of the nine channels to its renderer, so adding a channel is
a renderer plus a table entry rather than another branch in a growing function.

The binding block is what makes a projection self-locating: task reference, the JSON task document,
altitude/kind, seat/operation, repository, work branch with its source branch and base commit, code
worktree, memory mode and work branch, enclosure contract, and the projection revision. The rendered
document therefore carries its own binding and identity, which is why a delivering adapter (L5/L7)
can pass `markdown` through verbatim instead of re-rendering or re-ordering it.

**Why the diagnostic half stays out.** The module docstring states the reason as contract, not
style: identity and provenance diagnostics do not belong in the prose unless a decision needs them,
and **a model that can see the raw audit trail will treat it as instructions**. The read plan, the
selection record and the document digest remain on `TaskProjection`.

Two rules survive into the rendering:

- **Nothing is clipped.** A requirement, a preservation constraint, a forbidden overreach and a
  failure obligation are emitted exactly as the packet carries them. There is no length budget in
  this module.
- **Referenced is not the same as omitted.** Every source the projection did not inject is named
  under "Expansion references", so "not injected" is a visible decision with a link rather than a
  silent gap. `_closure` writes that section together with the gaps.

`_requirements` distinguishes an owned requirement (rendered with its verbatim packet sections) from
an adjacent one (`_adjacent_line`, a single context line), so a seat can see that a neighbouring
obligation exists without being handed its body.

### Conventions

A new channel is a renderer function plus a `_CHANNEL_RENDERERS` entry plus its place in
`_CHANNEL_ORDER`. Ordering belongs in `_CHANNEL_ORDER`, not in the renderers.

### Invariants And Boundaries

- **No clipping, no summarising, no length budget.** A `[:n]`, a `max_lines` or a "summary" step
  here is the defect `CAPS-R03@v1` required behaviour 5 forbids.
- The diagnostic half must stay out of the prose: no read plan, no selection record, no document
  digest in `markdown`.
- "Expansion references" and the gaps must both be rendered. Dropping either turns a visible
  decision into a silent omission.
- The binding block must name the work branch and the projection revision. A projection a consumer
  cannot locate is not deliverable verbatim.
- Renderers do not mutate the projection; they read it and return block lines.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking the configured sources.

### Repo-Internal References

The render entry point, the binding block that makes a projection self-locating, and the closure.

- The complete model-visible document, in the operation's channel order. [1]
- The binding block: task reference, branch, memory surface, contract and revision. [2]
- The requirement section, and the single context line an adjacent obligation gets instead of its body. [3]
- The closure: expansion references and gaps, so "not injected" is visible rather than silent. [4]
- The channel vocabulary and its renderer table. [5]
- The value the rendered bytes are digested into, which is why the revision is not in the prose twice. [6]
- The case that proves an owned obligation is carried verbatim into the rendered document. [7]

### Cross-Repo References

No sibling-repository contract consumes this renderer.

No meaningful cross-repo references found.
