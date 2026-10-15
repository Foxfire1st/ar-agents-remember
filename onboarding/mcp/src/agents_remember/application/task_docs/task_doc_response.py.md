# mcp/src/agents_remember/application/task_docs/task_doc_response.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Own shared task-document result and dry-run rendering.

## Code Commentary

### Logic

The helpers render applied task mutations, preview JSON/Markdown diffs, progress counts, graph titles, and optional master-sync effects from the prepared candidate. For an ordinary-master preview, _render_preview loads only explicit listed children, honoring supplied path-keyed candidate overrides before disk reads, derives master Order, and supplies it to render_markdown. task_doc_preview forwards the same overrides to its own render and the nested master-sync preview; sprint/non-master inputs do not derive ordinary-master Order here. The publisher supplies the prepared document batch as the override map. Rendered diffs and wouldLose still compare against on-disk Markdown; external grant reads remain separate observations.

### Invariants And Boundaries

- Preview and apply use prepared candidate task truth; ordinary-master previews derive Order with the prepared batch overrides. Separate disk/grant observations are not an atomic freshness or byte-equality guarantee.
- Rendering does not consult queue rows or operation state.
- Graph and master-sync details are response evidence, not publication authority.

### Todos

None recorded.

## Grant-aware preview rendering

Preview Markdown is the candidate document rendered with an optional readable external leaf grant. Without that argument it retains the old rendered bytes; master rendering ignores it. Preview and publication share rendering intent but separate calls may observe different current grants. No grant is serialized into authored task JSON, and not every mutation response promises directGrant. Queue authority and authoring ownership are unchanged.

## Evidence

### Docs References

No configured domain-documentation source applies to this repository-internal route.

### Repo-Internal References

- Applied results and previews share one response shape. [1]

- Graph-title and master-sync helpers render supporting evidence; ordinary-master previews derive Order from explicit children and supplied candidate overrides. [2]
### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

- Preview Markdown is the candidate document rendered with an optional readable external leaf grant. [3]
