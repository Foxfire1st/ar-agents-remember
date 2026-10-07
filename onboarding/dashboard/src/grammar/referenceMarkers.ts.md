# dashboard/src/grammar/referenceMarkers.ts

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

The opt-in remark plugins that let the shared Markdown renderer serve document reading (MIK-R79
rules 8 and 15): `remarkReferenceMarkers` turns prose `[n]` markers into links to the card's own
reference list, and `remarkHeadingIds` gives every heading a stable id so the "On this page" outline
and fragment links have one destination per chapter. Both stay opt-in so the Operations reader and
requirement links keep their existing rendering.

## Code Commentary

### Logic

- `remarkReferenceMarkers` walks the parsed tree and rewrites `[n]` only inside text nodes: a
  `reports[0]` inside a code span or a fenced block is never rewritten, and a real link or link
  definition that happens to be numbered is left as authored. A rewritten marker becomes a link to
  `#reference-<n>`.
- `remarkHeadingIds` assigns a slug id per heading text, suffixing repeated titles (`chapter`,
  `chapter-1`) so repeated headings still have distinct destinations.

### Conventions

- Both plugins are pure tree transforms with no I/O; the shared `Markdown` component decides when to
  include them.
- Marker links point at the card's own reference list anchor; the renderer owns nothing else about
  references.

### Invariants And Boundaries

- A marker inside code (span or fence) is text, never a link; the text's own links are never
  re-pointed.
- Heading ids are derived only from the parsed heading text; no hand-written id is required in the
  source prose.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rule 8); it lives outside the code and memory repositories, so it
is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- Prose `[n]` markers become links to the reference list, in text nodes only. [1]
- Repeated headings receive distinct stable ids for the outline and fragment links. [2]
- The shared renderer includes the plugins only when its caller asks for them. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
