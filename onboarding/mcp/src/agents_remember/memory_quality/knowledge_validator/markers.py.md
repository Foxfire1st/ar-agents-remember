# mcp/src/agents_remember/memory_quality/knowledge_validator/markers.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**Finds the `[n]` reference markers of a Markdown file (MIK-R21 rule 6).** A marker is an unescaped `[` digits `]` outside code. `find_markers(text)` returns every marker with its number and line, in order; `rules_references.check_markers` pairs them with the sidecar's references.

## Code Commentary

### Logic

- `_paragraphs` splits the text into paragraphs of (line number, line), dropping fenced code blocks: a line opening with three or more backticks or tildes, indented at most three spaces, up to a closing fence of the same character and at least the same length (`_closes`).
- `_prose_spans` removes inline code spans (a backtick run up to the next run of the same length within the paragraph); an unclosed run is prose.
- `_escaped` treats a `[` preceded by an odd number of backslashes as escaped.
- `Marker.valid` is true only when the digits match `REFERENCE_NUMBER_PATTERN`. `[0]` and `[01]` are still markers; the rule reports them as invalid and names `\[n]` or a code span.
- `escape_markers(text)` (MIK-R24) returns `text` with every marker this module would report escaped as `\[n]`, so `find_markers` then finds none. `_paragraph_marker_offsets` locates each unescaped marker of a paragraph as (line, offset), through the same `_paragraphs`, `_prose_spans` and `_escaped` rules, so exactly the brackets `find_markers` reports are escaped and nothing inside code is touched. The conversion (`memory/conversion/cards.render_card`) uses it before substituting its own reference numbers, so the only markers of a converted card are the ones the conversion wrote.

### Conventions

- Indented code blocks are **not** treated as code, because they are ambiguous with list continuation (worker choice 7, accepted by review: no real onboarding token sits on an indented line).
- `[1](url)` link text counts as a marker, which is R21's literal rule.

### Invariants And Boundaries

- Only fenced blocks and inline spans hide a marker; escaping is the author's other way out.
- Real prose such as `signals[0]` or `line(s) [153]` is a marker. The MIK-R24 conversion escapes such tokens with `escape_markers`, which uses this grammar (review R1 finding 7, routed to L24). On the real repository it escaped none: the `line(s) [n]` texts leave with Update History, and the table cells that held subscripts were already code spans.

### Todos

None recorded. (The Todo that L24 must escape marker-like prose is met by `escape_markers`; see Logic.)

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The grammar and its tests.

- The fence and marker patterns. [1]
- A marker is valid only as a reference number. [2]
- Fenced blocks, inline spans and escapes are excluded. [3]
- The entry point. [4]
- One escaping rule, the validator's own grammar: exactly the markers `find_markers` reports are escaped. [5]
- The grammar cases. [6]

### Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.
