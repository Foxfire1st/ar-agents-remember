# skills/l-01-agent-lifecycles/reference/consolidation-pass.md

## Governing Overview

[overview](../overview.md)

## Purpose

Provides step-detail reference rules for the Consolidator during a pass: worklist preparation, clean named proof-test execution, per-rule/per-family outcome decisions, and handover report contents.

## Code Commentary

Explicitly defers scope, writer, and boundary authority to `roles/consolidator.md` and `operations/consolidation.md`. `Prepare the pass` requires stopping and notifying the Manager if `consolidationList` is missing or empty, then running contract-scoped `memory_quality_check` to persist deduplicated `consolidation_target` items. `Run named proof tests cleanly` limits execution strictly to named `proves` entries or newly linked existing tests, isolates caches/temps (`--basetemp`, `PYTEST_CACHE_DIR`, `TMPDIR`, coverage) to the scratch directory, requires an empty `git status --porcelain` in the code worktree, and logs unrunnable tests in `testsNotRun` with reason. `Decide each outcome` treats age/similarity/usage only as hints and defines `stands` (including title-only additions without revision bump), corrected (preserving conditions/exclusions across merges/splits, naming predecessors in `supersedes`, and using today's rows for card-only edits), and `unresolved` (leave rule untouched on undecidable contradiction or failing proof test, report up chain, continue), plus mandatory proof evidence (`testsRun`/`testsNotRun`/`noProofRecorded: true`) and single-row closure when a listed subject is also touched/reached. `Report and hand over` enumerates the six mandatory report sections and specifies passing the exact 40-character memory Git tree (`candidateTree`) and report path to Reviewer via `role_message` while notifying Manager of `unresolved` items and gaps.

## Relationships

Registered in `skills/l-01-agent-lifecycles/composition-manifest.json` (`references.consolidation-pass`, `injected: false`, `step_detail: true`), linked from `roles/consolidator.md`'s Reference index (`{{detail:reference/consolidation-pass.md}}`), verified for unique detail-pointer resolution by `mcp/tests/test_l84_unique_detail_pointers.py`, and packaged into runtime `package_data`.

## Evidence

- `## Prepare the pass` requires stopping on a missing/empty `consolidationList` and persisting deduplicated `consolidation_target` items via contract-scoped `memory_quality_check`. [1]
- `## Run named proof tests cleanly` restricts runs to named/newly-linked proof tests, confines caches/temps to scratch, verifies an unchanged code worktree, and records unrunnable tests in `testsNotRun`. [2]
- `## Decide each outcome` defines `stands`, corrected, and `unresolved` rules, mandatory `testsRun`/`testsNotRun`/`noProofRecorded` proof evidence, condition/exclusion preservation, and single-row closure of listed-plus-touched items. [3]
- `## Report and hand over` specifies the six required report elements, direct Reviewer handover with the 40-character memory Git tree (`candidateTree`), and Manager notification of `unresolved` items and gaps. [4]
