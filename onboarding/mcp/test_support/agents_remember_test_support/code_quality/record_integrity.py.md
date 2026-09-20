# mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated |  2026-09-18T14:55+02:00 |
| lastVerifiedCommitHash | `3888cd8600e39a52c540d6038820759e3d4ffa7a` |
| lastVerifiedCommitDate | 2026-09-20T20:02:13+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l2-ar` uncommitted source (this file is an addition, **1110 lines**, sha256 `b860e9a2bb2ab1f7a1beb596168644d398f89e23bb858d065232ca43c6e20a90`, 47,642 bytes); base `d9becade1a373f2272501f7451746ccc259ca9ac` |
| governingOverview | `overview.md` |

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

## Docs References

No external Domain Documentation source is configured for this repository: `system/sources.md`
carries no entries, so no `Domain Documentation` category is available to cite. This card records
repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured in this memory root. | N/A | N/A |

## Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or
certification pass. Every range was derived against the current 1110-line source.

| Finding | Anchor | Source |
| --- | --- | --- |
| The report prefix every rendered comparison carries. | `REPORT_PREFIX` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:62-62 |
| The enclosure-contract glob the tree walk resolves. | `CONTRACT_GLOB` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:64-64 |
| What a "case" is, declared once so a figure check and its cases cannot disagree. | `TEST_DEFINITION` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:68-68 |
| The closed status vocabularies, so an unrecognized status is reported rather than compared. | `ACTIVE_STATUSES`; `LANDED_CONTRACT_STATUSES`; `STARTED_CONTRACT_STATUSES` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:75-79 |
| The seven named rules, so a finding says which comparison produced it. | `RULE_LEAF_CONTRACT`; `RULE_LEAF_CONTRACT_KEYED`; `RULE_MASTER_EARLY`; `RULE_OWNER`; `RULE_FIGURE` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:82-94 |
| A comparison that could not be made, named rather than returned as a silent zero. | `RecordIntegrityError` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:97-100 |
| One disagreement with both sides named and the line a reader can open. | "class Finding:" | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:102-126 |
| What one check compared, so its finding count is readable rather than merely small. | "class Comparison:" | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:128-188 |
| One enclosure contract reduced to the cells and identity a comparison needs. | "class ContractCells:" | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:190-217 |
| One task document reduced to the fields the comparisons read. | "class LeafDocument:" | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:219-234 |
| One `subTasks[]` row of a master document. | "class MasterRow:" | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:236-244 |
| Scalars and nested blocks read out of frontmatter, which is all the parsing there is. | `_scalar_fields`; `_block_fields` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:247-262 |
| The leaf/contract comparison: contract cells are the authority, the document's status is the subject. | `check_leaf_document_against_contract` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:441-547 |
| `Completed` requires the document to be `Completed`, never merely every step marked (D42's rule). | `derived_master_status` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:550-566 |
| The master-row comparison, with `row-completed-before-landing` named on every finding. | `check_master_rows_against_leaf_documents` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:569-675 |
| The tolerant `L<n>` suffix key that found six leaves an exact match reported clean. | `leaf_key`; `_index_by_leaf_key` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:410-438 |
| Only the State cell is graded, because the Owner cell names owners rather than leaf-set membership. | `STATE_COLUMN`; `ARROW` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:674-675 |
| The register's arrow comparison, refusing rather than zeroing when the master declares no leaf set. | `check_register_row_ownership`; `declared_leaf_ids` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:682-758 |
| One prose figure and the revision whose source value is the authority for it. | "class FigureClaim:" | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:760-857 |
| The prose-figure comparison `T45` records as absent from the product's own checks. | `check_declared_figure_currency` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:872-955 |
| The two shipped figure shapes, and the CLI form that declares a claim. | `FIGURE_SHAPES`; `parse_figure_claim` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:955-983 |
| The coordination root as an input rather than a hard-coded layout, or a refusal naming it. | `COORDINATION_ROOT_ENV`; `coordination_root_from_environment` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:953-1002 |
| The run that joins the figure comparison only when claims are supplied. | `run_all` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:1005-1033 |
| The runner, its repeatable inputs, and the exit status that reports a finding. | `build_parser`; `main` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:1036-1110 |
| The 37 cases that pin these behaviours against the historical artifacts, in both directions. | `LeafDocumentAgainstContractTests`; `MasterRowAgainstLeafDocumentTests`; `RegisterOwnerArrowTests`; `DeclaredFigureCurrencyTests`; `RecordIntegrityReportTests` | mcp/tests/test_record_integrity.py:257-1140 |
| The lane this module's contract suite is registered in, so the fail-closed manifest admits it. | "mcp/tests/test_record_integrity.py" | mcp/tests/test-evidence-lanes.toml:305-305 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository
allowance is empty and no external source is relied upon here. The historical artifacts these checks
were proved against are task roots in the coordination tree (`260712_task-reader-body-priority-rc5`,
`260918_tool-surface-and-process-integrity`) and the memory repository's own revision `e116e5ee`,
which are task-local evidence rather than repository boundaries; the contract suite cites them by
path and **skips with the reason named** when they are absent.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History
- 2026-09-20T17:17:10+00:00: Generated citation repair: "mcp/tests/test_record_integrity.py" repointed to mcp/tests/test-evidence-lanes.toml:305-305. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "mcp/tests/test_record_integrity.py" repointed to mcp/tests/test-evidence-lanes.toml:248-248. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:55+02:00 — 260918-TSIP-L3 curator (citation repair, `ar/260918-tsip-l3-ar`, base `a12c511f`): The five-class row was re-scoped `:158-1000 → :257-1140`: the leaf's repair round inserted 140 lines inside that extent, so a prefix-preserving move would have ended at `:1012` and missed `RecordIntegrityReportTests` entirely (which now begins at `:1015`). The range is the current extent covering all five class declarations. The claim's wording was re-read against the new bytes and is unchanged — only the range moved, because this leaf's edit to `mcp/tests/test_record_integrity.py` inserted lines above it. `lastUpdated` advances with this repair; `lastVerifiedCommitHash` is deliberately unchanged because the candidate is uncommitted and the governed closeout owns the real code commit.

- 2026-09-18T13:39+02:00 — 260918-TSIP-L2 curator (uncommitted change set on `ar/260918-tsip-l2-ar`,
  base `d9becade`): created this card for the new module the leaf added, so the source file has its
  1-to-1 onboarding pair before closeout. Every range was derived by reading the **current 1110-line**
  source in the code worktree; the module was 1041 lines when the worker delivered it and 1110 after
  the leaf's repair round, so **no range on this card is carried from any earlier figure**. The case
  count on the sibling card was measured on this candidate rather than taken from a report: 37
  collected against 37 defined. Two limits are recorded here rather than smoothed: the contract
  comparison counts its 46 unmatched contracts instead of judging them, and the register's own prose
  census has no honest check. **Six anchors on this card carry the declaration form as a
  double-quoted literal** — `"class Finding:"`, and likewise `"class Comparison:"`,
  `"class ContractCells:"`, `"class LeafDocument:"`, `"class MasterRow:"`, `"class FigureClaim:"`.
  The first reading of this card raised six `citation_claim_reopened` rows on exactly those six
  anchors and no others, each reading *"did not exist at code commit `d9becade` and resolves in the
  working tree"*, which is what an uncommitted new file looks like to a provenance check. A first
  re-wording to the backticked form cleared those six and raised six `citation_anchor_missing` rows
  instead, because the check states its own anchor grammar: *a backticked code identifier, a
  backticked `#`-prefixed heading, or a double-quoted literal* — a backticked span that is none of
  those is not an anchor. The literal form satisfies both readings, and the re-wording follows
  Addendum B's fourth method note (*a citation anchor must be a unique construct*) and the check's own
  remediation (*re-read the claim, correct or retain its wording, regenerate its range*).
  `lastUpdated` tracks this body edit;
  `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are left at the leaf's frozen code base because
  the source is an uncommitted candidate and the governed closeout owns the real code commit. This
  seat writes no source and ran no product test beyond read-only collection.
