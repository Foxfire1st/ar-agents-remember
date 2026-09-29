# mcp/src/agents_remember/memory_quality/knowledge_validator/markers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/markers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047`|
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview | `../overview.md` |

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

### Conventions

- Indented code blocks are **not** treated as code, because they are ambiguous with list continuation (worker choice 7, accepted by review: no real onboarding token sits on an indented line).
- `[1](url)` link text counts as a marker, which is R21's literal rule.

### Invariants And Boundaries

- Only fenced blocks and inline spans hide a marker; escaping is the author's other way out.
- Real prose such as `signals[0]` or `line(s) [153]` is a marker; the L24 conversion must escape such tokens (review R1 finding 7, routed to L24).

### Todos

L24 must escape marker-like tokens in real onboarding prose (about 190 in 50 files, per review R1).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The grammar and its tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fence and marker patterns. | `_FENCE`; `_MARKER` | mcp/src/agents_remember/memory_quality/knowledge_validator/markers.py:21-21; mcp/src/agents_remember/memory_quality/knowledge_validator/markers.py:22-22 |
| A marker is valid only as a reference number. | `Marker` | mcp/src/agents_remember/memory_quality/knowledge_validator/markers.py:28-34 |
| Fenced blocks, inline spans and escapes are excluded. | `_paragraphs`; `_prose_spans`; `_escaped` | mcp/src/agents_remember/memory_quality/knowledge_validator/markers.py:48-67; mcp/src/agents_remember/memory_quality/knowledge_validator/markers.py:70-90; mcp/src/agents_remember/memory_quality/knowledge_validator/markers.py:93-99 |
| The entry point. | `find_markers` | mcp/src/agents_remember/memory_quality/knowledge_validator/markers.py:102-119 |
| The grammar cases. | `test_markers_are_unescaped_bracketed_numbers_outside_code` | mcp/tests/test_knowledge_validator.py:555-558 |

## Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
