# mcp/src/agents_remember/application/knowledge_paging/pager.py

## Governing Overview

[application route overview](../overview.md)

## Current source contract evidence

- Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance. [7]

## Purpose

**Cutting one ordered selection into pages that stay within the shared threshold (MIK-R02 rule 2).** The pager knows rows, not knowledge: a surface hands it the whole ordered selection as `PageRow` values and a `render` callback that builds the complete response for one `PageCut`.

## Code Commentary

### Logic

- `PageRow(body, group, reference)`: one indivisible row. A header row of a `group` (a family) carries the `reference` row a later page of that group starts with.
- `PageCut(start, end, total, header_reference, oversized, blocked)`: rows `[start, end)`; `remaining` and `complete` are the walk's figures.
- `PageBinding(memory_tree_id, selection_policy, policy_version, manifest_digest, code_tree_id)`: what a walk is bound to, stated on every page and carried by its continuation.
- `header_reference(rows, start)`: only a page that starts inside a group, on a non-header row whose header was on an earlier page, starts with the reference. It is the interim `page.headerReference`; MIK-R01 makes it a literal first row (ruling Q3, 19:56:40).
- `cut_page(rows, start, render, *, alone=None, budget=None)`: estimates the run from each row's own token count over the rendered empty page (`_estimated_end`), then verifies against `budget.project(rendered)` when supplied, otherwise the raw rendered response, and shortens until it fits `budget.threshold` less the envelope reserve. `CutBudget.max_rows` caps the data-row run; the returned body remains raw rendered data. **A single row that does not fit is `oversized` only when it does not fit alone either** (the `alone` render, used for a seed laid out in a `read_ar_files` block); otherwise the cut comes back empty and `blocked`, and the caller defers the seed (ruling F2, 20:40:40).
- `page_block(cut, binding)`: the `page` facts: `threshold`, `memoryTreeId`, `selectionPolicy`, `selectionPolicyVersion`, `manifestDigest`, `codeTreeId`, `start`, `rowsOnPage`, `total`, `returned` (cumulative), `remaining`, `enumerationComplete`, optional `headerReference` and `flags: ["oversized_row"]`.

### Conventions

- The default cut measures the whole rendered response. A caller-provided `CutBudget.project` measures the delivered shape instead, including its modeled envelope, counts, continuation and currentness; the return value remains the rendered body.

### Invariants And Boundaries

- **The generic pager fits its selected admission shape to the budget, except a single indivisible row too large alone, returned flagged `oversized_row`.** This internal exception does not promise that a mounted answer may bypass its final guard; row projection changes delivered representation, not the ordered selection.
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
