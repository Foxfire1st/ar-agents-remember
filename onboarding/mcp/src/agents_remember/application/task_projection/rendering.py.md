# mcp/src/agents_remember/application/task_projection/rendering.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/task_projection/rendering.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T10:30+02:00 |
| lastVerifiedCommitHash | `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| lastVerifiedCommitDate | 2026-09-16T10:52:30+02:00|
| governingOverview      | `../overview.md`                           |

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

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking the configured sources. | N/A | N/A |

## Repo-Internal References

The render entry point, the binding block that makes a projection self-locating, and the closure.

| Finding | Anchor | Source |
| --- | --- | --- |
| The complete model-visible document, in the operation's channel order. | `render_markdown` | mcp/src/agents_remember/application/task_projection/rendering.py:45-58 |
| The binding block: task reference, branch, memory surface, contract and revision. | `_binding_block` | mcp/src/agents_remember/application/task_projection/rendering.py:65-89 |
| The requirement section, and the single context line an adjacent obligation gets instead of its body. | `_requirements`; `_owned_requirement`; `_adjacent_line` | mcp/src/agents_remember/application/task_projection/rendering.py:96-132; mcp/src/agents_remember/application/task_projection/rendering.py:135-163; mcp/src/agents_remember/application/task_projection/rendering.py:166-167 |
| The closure: expansion references and gaps, so "not injected" is visible rather than silent. | `_closure` | mcp/src/agents_remember/application/task_projection/rendering.py:234-258 |
| The channel vocabulary and its renderer table. | `_CHANNEL_RENDERERS`; `_CHANNEL_ORDER`; `ProjectionChannel` | mcp/src/agents_remember/application/task_projection/rendering.py:261-271; mcp/src/agents_remember/application/task_projection/rendering.py:27-36; mcp/src/agents_remember/application/task_projection/types.py:45-57 |
| The value the rendered bytes are digested into, which is why the revision is not in the prose twice. | `task_context_of` | mcp/src/agents_remember/application/task_projection/provider.py:37-52 |
| The case that proves an owned obligation is carried verbatim into the rendered document. | `test_every_owned_obligation_is_carried_verbatim_and_a_missing_section_is_a_gap` | mcp/tests/test_task_projection.py:801-830 |

## Cross-Repo References

No sibling-repository contract consumes this renderer.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History

- 2026-09-16T10:30+02:00 — 260915-CAPS-L3 curator: created this card for the Markdown renderer added
  by the scoped-task-context leaf (`CAPS-R03@v1`). Records the fixed channel order and renderer
  table, the self-locating binding block that lets L5/L7 deliver `markdown` verbatim, the deliberate
  exclusion of the diagnostic half from model-visible prose, and the two surviving rules (nothing
  clipped; referenced is not omitted). Verification metadata is left at the leaf base commit because
  the source is uncommitted — the governed closeout stamps the real code commit.
