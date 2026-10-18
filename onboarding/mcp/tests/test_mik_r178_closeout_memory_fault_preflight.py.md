# mcp/tests/test_mik_r178_closeout_memory_fault_preflight.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Guard that the worktree closeout refuses a memory fault it can already see from the code candidate
and the memory worktree, before any code commit is published, and that the refusal names the fault
rather than a bare Git message. The module also guards that an edited evidence row is recomputed
over the code commit's own tree, that the curator's memory-quality check reports a row citing a
path the candidate lacks, and that an add-only leaf still closes out as it did.

## Code Commentary

### One verdict, asked before either commit

The cases enter through two different routes, and they are not the same seam. `_preview` calls
`closeout.closeout_preview_payload` directly with only its context resolution and progress reporting
pinned: three `contract_context` readers (`closeout`, `closeout_external`, `onboarding`) and
`report_operation_progress`. The apply cases call `_public_closeout`, borrowed whole from
`test_knowledge_reopen`, which runs `closeout.closeout_result`: it stubs the entry resolution, the
unsatisfied-gate refusal, the candidate revalidation, the approval claim, the ordinary-worktree
check, progress reporting and the recovery module's progress, and pins **two** context readers —
`closeout_external`'s and `onboarding`'s — not the same three the local preview patches. The third
seam is closed differently there: `closeout._closeout_entry` is replaced outright, so the closeout
module's own `contract_context` is never reached and never needs patching. Either route reaches
`candidate_gate_verdict`, so a case that asserts a refusal at the preview and again at the apply is
asserting one object, not two. The deleted-evidence and unreadable-route-cache cases assert both
sides' HEADs are unchanged after the refusal, which is what the fixtures can show: rule 1's claim
that no approval is spent rests on the source path, not on a live approval store.

### What the refusal says

The deleted-evidence case asserts the refusal names the catalogue file, the `Evidence Holder` row
and `pkg/gone.py`, and the re-point remedy. The compound case asserts one refusal carries an
unsupported algorithm and **every** absent evidence path of the same row, so clearing the algorithm
cannot disclose a second, previously hidden cause on the next attempt. Its two controls keep the
refusal honest: a row whose evidence is all present names only the algorithm, and a planned row
without a value is refused with the missing-value text and its row named — that control does not
assert the clearing action, which the implementation emits but no case here checks.

### The recompute and the curator's finding

`test_a_repointed_row_is_recomputed_and_the_closeout_lands` runs twice — once with the new evidence
set still touching a changed path, once with unchanged files only — and compares the committed value
with an independently computed `git-blob-set-v1` over the set at the code commit's tree. The
unchanged-files parameter is the one the base fails, because the old rule only recomputed rows that
touched a changed path. `test_the_memory_quality_check_names_an_entity_row_citing_a_path_the_candidate_lacks`
runs the curator harness and asserts the finding is reported once, with `curatorActionableCount`
rising by exactly one, and is absent once the row is re-pointed.

### Bounds

These cases are source-level regressions over the closeout's candidate verdict, the entity refresh
and the curator checklist seam, on real disposable repositories built by the borrowed fixture
worlds. They assert behaviour, not a run: the Worker's focused transcripts beside its freeze are its
own receipts, and no case here speaks for the whole suite, an installed host or a live approval
store.

## Evidence

- An add-only leaf still previews `would-closeout` and lands, and an existing row whose evidence set is unchanged from the memory base and touches no changed path keeps its recorded value; an edited or new row is recomputed even when no changed path touches it. [3]
- A planned row without a fingerprint value is still refused, naming the missing value and the row. [11]

- A deleted evidence path stops the preview and the apply's preflight, naming the catalogue, the row, the path and the re-point remedy, with both HEADs unchanged. [1]
- A re-pointed row is recomputed over the code commit's tree, both when its new set keeps a changed path and when it names unchanged files only, and the value equals an independent `git-blob-set-v1`. [2]
- The curator's memory-quality check names the row and the absent path and counts it as one actionable finding, and reports nothing once the row is re-pointed. [4]
- An unexpected Git failure inside the refresh is reported with its step, its evidence paths and the tree it read. [5]
- A row whose only evidence the leaf deletes is refused before the code commit even though the refresh plan never selects it. [6]
- The same leaf lands once the row is re-pointed at a retained file. [7]
- An unreadable route-index cache is refused before the code commit, naming the step and the offending path, with both HEADs unchanged. [8]
- One refusal names an unsupported algorithm together with every absent evidence path of the same row. [9]
- A row whose evidence is all present names only the algorithm, so no absent path is invented. [10]
