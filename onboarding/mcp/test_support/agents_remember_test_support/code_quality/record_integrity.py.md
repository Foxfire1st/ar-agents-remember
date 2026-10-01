# mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py

## Governing Overview

[overview](overview.md)

## Purpose

Make **a record that stopped being true** detectable. Each of the four comparisons below reads a
declared value out of one artifact and the authoritative value out of another, and reports the rows
where the two disagree, naming both sides and the number of rows compared. Nothing here interprets
prose; the module is read-only and writes no file.

The class it was written for is the drift every finding of `260918_tool-surface-and-process-integrity`
shared: a document that was true when written and silently stopped being true, with nothing able to
notice. A master report described a superseded tip in one section while another section was right; a
master row read `Completed` before any closeout had run; a register cell named a leaf its own master
does not have; a route overview stated a source's pre-repair line count while every check stayed
green.

This is a helper library, not a gate: it exposes no registry entry and the quality plan does not
invoke it. It sits beside `citations.py`, `structural_limits.py`, `scope.py` and
`instrument_discipline.py`, and it is the route's **fifth** verification-helper module — the fourth
was `instrument_discipline.py`, whose own card records it.

## Code Commentary

### Logic

Four comparisons, one per function group, plus a comparison of a **figure written in prose** against
the source it describes. Ranges are derived against the **current 1110-line** source.

- `check_leaf_document_against_contract` (441-547) — the enclosure contract is the **authority**
  side and the leaf document's `status` is the subject. Two rules are reported and they are not
  symmetric: `leaf-document-status-vs-contract-cells` for a document reading `planning`/`inProgress`
  while its contract says the work landed, and the same rule for a document reading `Completed`
  while closeout has not started. The historical case is 11 direct-child leaves in the first shape
  and 24 in the second, 22 of them in one master. A contract whose `leaf_id` matches no document is
  **counted and reported in `detail` rather than failed** — on older masters the leaf document is
  gone by design. `RULE_LEAF_CONTRACT_KEYED` (87) is the same comparison under the tolerant key:
  `leaf_key` (410-423) compares the `L<n>` suffix case-insensitively, because an exact-string match
  reported a clean zero for six leaves whose contracts write `260703-l1` against a document reading
  `260703-L1`. The two calibrations are reported separately so a reader comparing two runs can see
  which one produced the difference rather than reading it as drift.
- `check_master_rows_against_leaf_documents` (569-675) — the leaf document is the authority side and
  the master's `subTasks[].status` row is the subject. `derived_master_status` (550-566) restates the
  shipped rule from `tasks/master_sync.py`: **`Completed` requires the document to be `Completed`,
  never merely every step marked**. That conjunct is defect `D42`'s fix, and it is what the leaf's
  third review round repaired in the test suite. `row-completed-before-landing` (89) names `D42`
  itself; `row-unmarked-after-work-began` (92) is its mirror, shipped because it is the same
  two-sided comparison.
- `check_register_row_ownership` (697-758) — a register row's `→ L<n>` arrow in its **State cell**
  against the leaf ids the owning master declares (`declared_leaf_ids`, 682-694). The historical case
  is five cells still pointing at an `L20` belonging to the previous master. `STATE_COLUMN` (674)
  pins the graded column: the Owner cell names owners (`T46 | L6 / L7`), not leaf-set membership, so
  grading it reported all 45 arrows as disagreements on the check's own first run. A master with no
  leaf set **refuses** through `RecordIntegrityError` rather than reporting a licensed-looking zero.
- `check_declared_figure_currency` (872-955) — the comparison the memory layer's own checks cannot
  make, recorded as `T45`: `range_resolution` looks only at anchors *inside cited ranges* and
  `claim_reopen` only at *cited claims*, so a line count or case count written as prose is invisible
  to both. A `FigureClaim` (760-857) carries the revision the prose describes, and the authority side
  is measured **there** — by `git show <base_commit>:<path>` (through `_git_root`, 860-869) or in the
  working tree when the claim names no base. That is what stops the comparison flagging every history
  entry that correctly records a past count. Frontmatter is skipped: a metadata row states the
  candidate a card was verified against, which is a revision rather than a measurement of the
  source's size. `FIGURE_SHAPES` (955) ships `line_count` and `case_count` and deliberately no third
  shape — grading more would mean interpreting prose rather than comparing two sides.

`Comparison` (128-188) is the licence for every count this module prints: it carries `subjects`, the
`authority` population and its `detail` sentence beside the findings, because *"0 disagreements"*
without the two populations stated is a zero nobody can license. `Finding` (102-126) names both sides
(`declared`, `measured`, `authority`) and the path and line a reader can open. `counts_by_rule`
(157-162) lets one check report several classes without collapsing them.

`run_all` (1005-1033) runs the two tree-wide comparisons, joins the register comparison when a
register is named, and joins the figure comparison **only** when claims are supplied — the figure
check's authority side is a per-project declaration, so there is nothing for it to compare on its
own. `main` (1088-1110) exits 1 when any comparison has a finding, 0 when all are clean.

### Conventions

The report prefix is `REPORT_PREFIX` (62) — `record integrity:` — and `RecordIntegrityError` (97-100)
subclasses `ValueError` so a caller can distinguish a comparison that could not be made from a bad
argument. Every rule has a named constant (82-94) so a finding says which comparison produced it.

A refusal is a first-class outcome and every one names its missing input: no coordination root
(`coordination_root_from_environment`, 986-1002, reading `AR_COORDINATION_ROOT`), a root carrying no
`tasks/` directory, a `:base_commit` that does not resolve in the repository, a source outside any Git
tree when a base is declared, an unknown figure shape, and a claim that does not read as
`PATTERN:SHAPE:SOURCE:DOCUMENT[:DOCUMENT...]` (`parse_figure_claim`, 958-983). The root is an input
rather than a constant on purpose: this is shipped code and may not hard-code one machine's layout.

`TEST_DEFINITION` (68) is declared once so a figure check and the cases that check it cannot disagree
about what a "case" is. `_scalar_fields` (247-248) and `_block_fields` (251-262) parse frontmatter
into scalars and nested blocks, which is how `read_contract` (265-287), `read_leaf_document` (290-321)
and `master_rows` (324-359) reduce each artifact to the fields a comparison reads. The four frozen
dataclasses `ContractCells` (190-217), `LeafDocument` (219-234), `MasterRow` (236-244) and
`FigureClaim` are the parsed inputs; `Comparison` and `Finding` are the outputs.

### Invariants And Boundaries

- **Both populations are stated with every result.** A zero is admissible only beside the count it
  was drawn from; this is the same rule `instrument_discipline.py` enforces for a text probe, applied
  to a record comparison.
- **An unrecognized status is reported, never silently compared.** `ACTIVE_STATUSES` (75),
  `LANDED_CONTRACT_STATUSES` (76) and `STARTED_CONTRACT_STATUSES` (77-79) are closed vocabularies for
  exactly that reason.
- **A disagreement is a disagreement about two readable sides, not an interpretation.** No function
  below grades prose except `check_declared_figure_currency`, and that one grades a number against the
  source that carries the number.
- **The module writes nothing.** Both the docstring and the CLI description say so; the leaf's tests
  assert it (a run from a task root leaves the tree unchanged).
- **A shape this module does not have a check for is not given one.** The register's own prose census
  — a report stating "50 rows (22 fixed · 16 carried · 11 open)" against an artifact carrying 53 — is
  a real drift the leaf could not automate honestly: finding the census means parsing free-form
  Markdown, and its bucket rule is undeclared. Recorded as a limitation rather than papered over.

### Todos

- `check_leaf_document_against_contract`'s unmatched-contract population is **counted, not judged**:
  judging the 46 contracts with no matching leaf document needs a naming convention for where an
  older master's leaf documents live after cleanup. This is the comparison's own stated instrument
  limit, inherited from the census it re-derives.
- `check_declared_figure_currency` grades a figure only where the prose **names its source** through
  the claim's `label_pattern`. A restatement that names no file is a guess rather than a comparison
  and is deliberately not graded; the boundary is pinned by a case rather than left implicit.
- The module docstring's claim (41-43) that nothing here writes to disk holds; there is no known
  further gap carried by this file at this revision.

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository: `system/sources.md`
carries no entries, so no `Domain Documentation` category is available to cite. This card records
repository-owned behavior from the source references below; no external documentation claim is made.

External domain documentation is not configured in this memory root.

### Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or
certification pass. Every range was derived against the current 1110-line source.

- The report prefix every rendered comparison carries. [1]
- The enclosure-contract glob the tree walk resolves. [2]
- What a "case" is, declared once so a figure check and its cases cannot disagree. [3]
- The closed status vocabularies, so an unrecognized status is reported rather than compared. [4]
- The seven named rules, so a finding says which comparison produced it. [5]
- A comparison that could not be made, named rather than returned as a silent zero. [6]
- One disagreement with both sides named and the line a reader can open. [7]
- What one check compared, so its finding count is readable rather than merely small. [8]
- One enclosure contract reduced to the cells and identity a comparison needs. [9]
- One task document reduced to the fields the comparisons read. [10]
- One `subTasks[]` row of a master document. [11]
- Scalars and nested blocks read out of frontmatter, which is all the parsing there is. [12]
- The leaf/contract comparison: contract cells are the authority, the document's status is the subject. [13]
- `Completed` requires the document to be `Completed`, never merely every step marked (D42's rule). [14]
- The master-row comparison, with `row-completed-before-landing` named on every finding. [15]
- The tolerant `L<n>` suffix key that found six leaves an exact match reported clean. [16]
- Only the State cell is graded, because the Owner cell names owners rather than leaf-set membership. [17]
- The register's arrow comparison, refusing rather than zeroing when the master declares no leaf set. [18]
- One prose figure and the revision whose source value is the authority for it. [19]
- The prose-figure comparison `T45` records as absent from the product's own checks. [20]
- The two shipped figure shapes, and the CLI form that declares a claim. [21]
- The coordination root as an input rather than a hard-coded layout, or a refusal naming it. [22]
- The run that joins the figure comparison only when claims are supplied. [23]
- The runner, its repeatable inputs, and the exit status that reports a finding. [24]
- The 37 cases that pin these behaviours against the historical artifacts, in both directions. [25]
- The lane this module's contract suite is registered in, so the fail-closed manifest admits it. [26]

### Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository
allowance is empty and no external source is relied upon here. The historical artifacts these checks
were proved against are task roots in the coordination tree (`260712_task-reader-body-priority-rc5`,
`260918_tool-surface-and-process-integrity`) and the memory repository's own revision `e116e5ee`,
which are task-local evidence rather than repository boundaries; the contract suite cites them by
path and **skips with the reason named** when they are absent.

No cross-repository evidence is required for these file-local claims.
