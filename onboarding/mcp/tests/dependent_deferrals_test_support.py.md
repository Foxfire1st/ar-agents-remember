# mcp/tests/dependent_deferrals_test_support.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Shared fixture and request-builder support for the dependent-deferral test suites (`test_dependent_deferrals.py` and `test_dependent_deferrals_gate_and_replay.py`), registered in `mcp/tests/evidence-lifecycle.toml` as permanent `shared-support`.

## Code Commentary

### Logic

- Wraps `knowledge_writer_test_support.build_world` to create real temporary Git code and memory repositories paired with canonical `ar-task-document/v1` master task trees (`261112-BUG` and cross-master `261124-CAP`) under `tmp_path`.
- Provides `seed_tasks`, `build_deferral_world`, `seed_deferred_world`, `write_dep`, `create_dependent`, operation builders (`defer_spec`, `defer_op`, `redefer_op`, `lift_op`, `confirm_op`, `row_op`), `dependent_doc`, `commit_memory` (refreshing `layout.json` `dependent_links` and `Code-Commit` trailer), `gate_trees`, `run_mqc`, and `read_dependents`.

## Relationships

- Consumed by `mcp/tests/test_dependent_deferrals.py` and `mcp/tests/test_dependent_deferrals_gate_and_replay.py`; governed by `mcp/tests/evidence-lifecycle.toml`.

## Evidence

- `build_deferral_world` and `seed_deferred_world` assemble real Git code/memory repositories and task-document hierarchies for deferral writer, gate, MQC, and reader tests. [1]
