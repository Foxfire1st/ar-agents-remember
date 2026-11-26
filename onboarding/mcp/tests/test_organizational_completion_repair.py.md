# mcp/tests/test_organizational_completion_repair.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Protects journal-owned organizational completion repair in `worktrees/integration/organizational_completion_repair.py`: pure reset-digest calculation, contract reopening with successor `waiting` closeout-door publication, unclaimed-door refusal, and idempotent retry recovery after an interrupted door publication.

## Code Commentary

Fixture helpers build a real temporary organizational leaf (`_closed_organizational_leaf`, reusing `_organizational_fixture`, `_commit_on`, and `_git` from `test_source_lineage.py`) whose code and memory commits are committed with `human_review_status="approved"`, `closeout_status="completed"`, and `integration_status="not-started"`, alongside valid `CloseoutDoorGeneration` records (`_door_generation`) and sprint-super `LifecycleOperationRecord` records (`_integration_record`).

- `test_organizational_completion_repair_evidence_builds_reset_digest_without_mutating_disk` verifies that `organizational_completion_repair_evidence` populates the operation key, candidate state, commits, task-document paths, `acceptedContractSha256`, and `resetContractSha256` (matching `_expected_reset_contract`) while leaving both the on-disk contract bytes and the live `claimed` closeout door untouched.
- `test_prepare_organizational_completion_repair_resets_contract_and_publishes_waiting_door` writes a cancelled integration record carrying `OrganizationalCompletionRepairEvidence` to the located lifecycle store, invokes `prepare_organizational_completion_repair`, and asserts that the contract resets to `pending-review` / `not-started` / `not-started` with cleared approval/commit/integration/memory-state fields and matching `resetContractSha256`, that the live closeout door advances to a `waiting` successor chaining `predecessorGenerationId` to the prior `claimed` generation with `declaredBy == "organizational-quality-repair"`, `declaredAt == cancelled_record.queuedAt`, and cleared claim fields, and that a second call converges idempotently.
- `test_organizational_completion_repair_refuses_unclaimed_live_door` publishes a `waiting` live door and asserts `organizational_completion_repair_evidence` raises `CloseoutQueueError` with status `organizational-completion-door-mismatch`.
- `test_prepare_organizational_completion_repair_recovers_after_interrupted_door_publication` monkeypatches `repair_module.publish_door_intent` to raise `OSError` once, asserting `OrganizationalRepairPublicationError` (`status == "organizational-completion-door-publication-interrupted"`, `next_action == "cancel"`) with the reset contract already on disk, the old `claimed` door still live, and `classify_organizational_completion_repair` returning `"reset-door-pending"`; retrying on the reloaded contract publishes the `waiting` successor door, transitions classification to `"reset"`, and makes a further retry a no-op without calling `publish_door_intent` again.

## Relationships

Tests [`organizational_completion_repair.py`](../src/agents_remember/worktrees/integration/organizational_completion_repair.py.md) and reuses Git/organizational leaf fixture builders from [`test_source_lineage.py`](test_source_lineage.py.md). Declared in the `unit-regression` lane of [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md), and named in [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md) as an exact consumer of `_user_settings_guard.py`, the Node-profile `package-lock.json` and `package.json`, and `repository_profile_test_support.py`.

## Evidence

- `organizational_completion_repair_evidence` computes the exact `acceptedContractSha256` and `resetContractSha256` without mutating the contract file or live `claimed` door. [1]
- `prepare_organizational_completion_repair` reopens the contract to match `resetContractSha256`, publishes a chained `waiting` successor door declared by `organizational-quality-repair`, and converges idempotently on repeat calls. [2]
- Repair evidence calculation refuses with `CloseoutQueueError(status="organizational-completion-door-mismatch")` when the live closeout door is not `claimed`. [3]
- An `OSError` during door publication raises `OrganizationalRepairPublicationError(status="organizational-completion-door-publication-interrupted", next_action="cancel")`, classifies as `reset-door-pending`, completes door publication on retry (`reset`), and turns subsequent retries into a pure no-op. [4]
