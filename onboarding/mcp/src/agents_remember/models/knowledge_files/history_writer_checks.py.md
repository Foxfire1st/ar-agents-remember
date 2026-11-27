# mcp/src/agents_remember/models/knowledge_files/history_writer_checks.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Provides pure tree-comparison checks for history rows against caller-supplied K_B and K_C facts (MIK-R07 rules 2, 4, and 5): re-anchor matching, known-subject validation, invariant revision-step binding, and examined-member staleness.

## Code Commentary

`reanchor_mismatches(row, candidate_anchors)` verifies that every `CoveredEntry.after` on an `InvariantRow` equals the entry's anchor in K_C (or `"absent"` when missing); `sidecar_entry_anchors(sidecar_path, entries)` builds that anchor map by copying `path=sidecar_path` onto each `RealizationEntry` or `ProofEntry` anchor. `unknown_subjects(history, known_record_ids)` returns subjects of `InvariantRow`, `FamilyRow`, `RecordRow`, and `MembershipRow` (extracting the invariant ID via `membership_invariant`) that do not exist in `known_record_ids`; non-record worklist row kinds are skipped. `invariant_revision_violation(row, *, base_revision, candidate_revision, restated_revision=None)` requires `row.revision == candidate_revision`, permits `base_revision is None` or `deleted` without a base-step constraint, requires `changed` to equal `base_revision + 1` unless `candidate_revision == base_revision == restated_revision` (restatement of an earlier frozen attempt's governing `changed` row), and requires every other disposition to preserve `base_revision`. `stale_examined_members(row, candidate_revisions)` returns examined member IDs present in `candidate_revisions` whose K_C revision differs from `member.revision`; absent members are not flagged as stale. Checks structural consistency against supplied facts only; worklist item currency remains the closeout gate's concern.

## Relationships

Imported by `application/knowledge_writer/history_check.py` (all five functions) and `memory_quality/knowledge_validator/rules_history.py` (`reanchor_mismatches`, `sidecar_entry_anchors`, `unknown_subjects`). Referenced in docstrings of `models/knowledge_files/history.py` and `models/knowledge_files/history_governing_rows.py`. Depends on `models.knowledge_files.history`, `.shapes`, and `.sidecars`.

## Evidence

- `reanchor_mismatches` compares every covered entry's `after` value against `candidate_anchors` (defaulting absent entries to `ABSENT`) and returns mismatched entry IDs. [1]
- `unknown_subjects` checks `InvariantRow`, `FamilyRow`, `RecordRow`, and `MembershipRow` record references against `known_record_ids`, ignoring worklist-only rows. [2]
- `invariant_revision_violation` enforces `row.revision == candidate_revision`, single-step `+1` increments for `changed` (with the `restated_revision` exception), and unchanged revision for non-`changed`/`deleted` dispositions. [3]
- `stale_examined_members` returns examined members present in `candidate_revisions` whose K_C revision differs from the row's recorded member revision. [4]
