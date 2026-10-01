# mcp/src/agents_remember/application/review_legacy_comparison.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**Reopening a closed leaf in a converted repository that recorded no tree comparison (MIK-R25 rule 4).** Once a
repository's official memory line is converted, the reviewer reads no database. A closed leaf that recorded a tree
comparison reopens from it (`review_tree_comparison.reopen_review_trees`); this module answers the two other closed
leaves:

- **a comparison recorded before the conversion** (a dataset comparison generation): it keeps its code sides, read
  from the generation's own manifest (never its retained snapshots), and both knowledge sides report
  `legacy-unavailable`;
- **a leaf with no comparison record but a recorded committed range**: when the recorded memory head is converted,
  the four recorded committed trees are the comparison (number `0`, no ref, since committed endpoints need none);
  otherwise the code sides are kept and the knowledge sides are `legacy-unavailable`.

It is reached only from `review_committed_leaf._converted_repository_resolution`, gated on
`official_line_converted`, so an unconverted repository's closed leaf keeps the dataset path unchanged.

## Code Commentary

### Logic

- `legacy_comparison_resolution(config, contract, generation_id=…)`: the newest (or named) generation's manifest
  (`_latest_manifest`, read as a record; a named generation that cannot be read is refused as
  `comparison_refused`); else the recorded committed code range (`recorded_committed_range`), refused as
  `candidate_not_live` when there is none and `candidate_unresolved` when the recorded code commit does not resolve;
  else `_recorded_trees` over the recorded memory range.
- `_recorded_trees` builds a `ReviewTreeComparisonRecord` of four committed sides with `task_id` from
  `review_task_id` (the task directory name, ruling 2026-09-30T02:32:42 (a)) and a converted base when the memory
  base is unconverted, and opens it through `reopened_trees`; any unresolved endpoint returns the legacy detail
  instead.
- `_legacy` composes a `ReviewCandidateResolution` whose two databases name paths under
  `.review-knowledge-unavailable/` that are never created, whose code sides are the recorded trees, and whose
  `knowledge_unavailable` carries `(side, "legacy-unavailable", detail)` for both sides.
- The declaration helpers, used by `review_committed_leaf` for the surface: `knowledge_unavailable_refusal`
  (`candidate_dataset_absent`, naming each side and state; for a tree comparison it delegates to
  `tree_sides_refusal`), `knowledge_unavailable_limitations` (`history:legacy-comparison` plus
  `history:intent:<side>:<state>`, or the tree facts) and `knowledge_unavailable_detail`.

### Conventions

- No snapshot and no database is opened here; the manifest is read as a record.

### Invariants And Boundaries

- **A knowledge side that is unavailable names no file**, so no read can reach a database in its place. Proved by
  `test_a_comparison_recorded_before_the_conversion_keeps_its_code_sides_only` (zero database opens) and on real
  data by the worker's ICR L47 (generation) and L57 (recorded range) reviews: code inventories of 27 and 12
  entries, the subject refused, zero database opens.
- Part of the candidate invariant recorded on `review_tree_comparison.py`: a tree Git can no longer produce is
  `unavailable-history`, never substituted — the recorded-range comparison is opened through `reopened_trees`.

### Todos

- **L31 (ruling 22:22:37 Q8):** the pre-existing pydantic `string_too_long` ValidationError on ICR L47's review with
  records (a curator-owner detail over 20,000 characters) is identical on base and worktree and is carried.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R25@v1` (rule 4) with its rulings in `25_reviewer-on-git-trees.json`; they live outside the code and memory
repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The state word and the detail a pre-conversion comparison reports. [1]
- A closed leaf of a converted repository with no tree record: generation, recorded range, or refusal. [2]
- The newest or named generation, read as a record. [3]
- Converted recorded endpoints become a committed four-tree comparison named by the task directory. [4]
- The code sides kept and both knowledge sides `legacy-unavailable`, naming no file. [5]
- The refusal, declared facts and detail of a legacy or partly unavailable comparison. [6]
- The closed-leaf branch that reaches this module only for a converted official line. [7]
- Code sides kept, knowledge `legacy-unavailable`, zero database opens. [8]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
