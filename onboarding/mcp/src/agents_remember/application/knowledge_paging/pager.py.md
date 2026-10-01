# mcp/src/agents_remember/application/knowledge_paging/pager.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Cutting one ordered selection into pages that stay within the shared threshold (MIK-R02 rule 2).** The pager knows rows, not knowledge: a surface hands it the whole ordered selection as `PageRow` values and a `render` callback that builds the complete response for one `PageCut`.

## Code Commentary

### Logic

- `PageRow(body, group, reference)`: one indivisible row. A header row of a `group` (a family) carries the `reference` row a later page of that group starts with.
- `PageCut(start, end, total, header_reference, oversized, blocked)`: rows `[start, end)`; `remaining` and `complete` are the walk's figures.
- `PageBinding(memory_tree_id, selection_policy, policy_version, manifest_digest, code_tree_id)`: what a walk is bound to, stated on every page and carried by its continuation.
- `header_reference(rows, start)`: only a page that starts inside a group, on a non-header row whose header was on an earlier page, starts with the reference. It is the interim `page.headerReference`; MIK-R01 makes it a literal first row (ruling Q3, 19:56:40).
- `cut_page(rows, start, render, *, alone, threshold)`: estimates the run from each row's own token count over the rendered empty page (`_estimated_end`), then verifies against the rendered response and shortens until it fits the threshold less the envelope reserve. **A single row that does not fit is `oversized` only when it does not fit alone either** (the `alone` render, used for a seed laid out in a `read_ar_files` block); otherwise the cut comes back empty and `blocked`, and the caller defers the seed (ruling F2, 20:40:40).
- `page_block(cut, binding)`: the `page` facts: `threshold`, `memoryTreeId`, `selectionPolicy`, `selectionPolicyVersion`, `manifestDigest`, `codeTreeId`, `start`, `rowsOnPage`, `total`, `returned` (cumulative), `remaining`, `enumerationComplete`, optional `headerReference` and `flags: ["oversized_row"]`.

### Conventions

- The cut measures the whole rendered response, so everything a response carries beside its rows (the envelope, counts, the continuation, currentness) is inside the measurement.

### Invariants And Boundaries

- **No response exceeds the threshold, except a single row too large on its own, which is returned alone, whole and flagged `oversized_row`.** A row is never shortened.
- **Every row appears on exactly one page:** a cut covers `[start, end)` and the next page starts at `end`. A reference row repeats an identity already returned and is not counted as returned.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R02@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`02_bounded-continuation-accepted-by-the-mounted-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module statement: indivisible rows, the header reference, the exact walk. [1]
- The flag an oversized single-row page carries. [2]
- The row, the cut and the binding. [3]
- Only a page starting inside a group continues a family. [4]
- The cut: estimate, verify, shorten; blocked versus oversized. [5]
- The page facts every bounded response states. [6]

### Cross-Repo References

No meaningful cross-repo references found: the pager is pure over rows its callers hand it.

No cross-repo boundary is crossed by this file.
