# mcp/tests/test_dependent_deferrals_gate_and_replay.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Unit tests covering dependent-deferral closeout gating, orphan and pre-base file warnings, crossing sync ID-keyed merges, MQC Lever-1 report-only flagging, `knowledge_read` dependent/record views with reading-leaf inference, and the `DPD-GHEXS9` replay.

## Code Commentary

### Logic

- Runs against real temporary Git code/memory repositories built via `dependent_deferrals_test_support` and is registered in the `unit-regression` lane of `mcp/tests/test-evidence-lanes.toml`.
- Covers due-by-task/due-by-file firing and creating-leaf exclusion (`test_06`), file changes on another line making deferrals due after merge (`test_07`), blocking only the leaf a deferral is due in (`test_08`), cross-master orphaned deferral warnings and re-homing (`test_09`), pre-base file-change warnings on unrelated leaves (`test_12`), lifted-deferral visibility in MQC report-only findings (`test_13`), bidirectional `crossing.py` ID-keyed deferral merge and post-sync closeout refusal (`test_14`), Lever-1 `pre_base_stale_confirmation` flagging with `preBaseMovedLinks` (`test_15`), `knowledge_read` dependent/record views and `staleOnly=True` marking (`test_16`), the `DPD-GHEXS9`/`docs/install/hermes.md` pre- and post-deferral replay (`test_replay_dpd_ghexs9_hermes_pre_and_post_deferral`), and inferred reading-leaf task-due / creating-leaf file-open derivation (`test_reader_derives_task_due_in_own_leaf_and_keeps_creating_leaf_file_open`).

## Relationships

- Uses `mcp/tests/dependent_deferrals_test_support.py` and proves the closeout gate, crossing merge, MQC flag, and reader invariants.

## Evidence

- The module tests closeout due/orphan/warning gates, bidirectional crossing merge, Lever-1 flagging, reader state derivation, and the `DPD-GHEXS9` replay. [1]
