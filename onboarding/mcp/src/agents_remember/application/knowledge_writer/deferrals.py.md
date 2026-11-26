# mcp/src/agents_remember/application/knowledge_writer/deferrals.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Implements dependent-record deferral authoring (`defer`, `redefer`, `lift`, `resolveDeferrals`), task/file condition validation, unedited-confirmation refusal, and deferral history-row enforcement inside the knowledge writer.

## Code Commentary

### Logic

- Exports `DEFERRAL_OP_KEYS`, `DeferralRecordOps`, `is_deferral_only_fields`, `deferral_condition_files`, `author_dependent`, `apply_record_row_deferrals`, and `verify_lifted_deferral_rows`.
- `author_dependent` strips operation keys from authored fields, refuses direct `deferrals` edits outside `crossing` sync resolution, and routes either to deferral-only updates on an existing dependent (`_author_deferral_only`) or to confirmation writes (`_author_confirmation`).
- Deferral-only updates preserve `stands_on` and `confirmed` unchanged, bump `revision`, and refuse `resolveDeferrals`.
- Confirmation writes refuse combining `lift` with confirmation, support partial resolution via `resolveDeferrals` on edited documents, and refuse confirming any dependent (existing or newly created) while open deferrals remain and `record.document` was not edited in the leaf, naming every open deferral's ID, owner, passage, and reason.
- Condition validation requires at least one of `task` or `file` and non-empty `passage` and `reason`, checks `task` against `load_task_facts` (refusing unknown, master, or terminal tasks), checks `file` against `authoring.code.blobs` (stamping `fileBlob`), and refuses note-only re-deferrals while allowing same-file re-deferral with the new blob once `fileBlob` has moved.
- `apply_record_row_deferrals` enforces DPD-only deferral dispositions (`deferred`, `re_deferred`, `deferral_lifted`), preserves prior `deferral_lifted` status/IDs in the same leaf, and fills `deferralIds`; `verify_lifted_deferral_rows` refuses any write that lifted a deferral without a `deferral_lifted` history row.

## Relationships

- Dispatched from `application/knowledge_writer/authoring.py` (`_write_record`, `verify_lifted_deferral_rows`) and `authoring_rows.py` (`_record_row`).
- Reused by `cli/handoff_check.py` (`is_deferral_only_fields`, `deferral_condition_files`) and `tasks/task_facts.py` (`load_task_facts`).

## Evidence

- `author_dependent` enforces deferral-only confirmation preservation, condition validation, partial resolution, and unedited-confirmation refusal for new and existing dependents. [1]
- `apply_record_row_deferrals` and `verify_lifted_deferral_rows` enforce operation/row agreement and require `deferral_lifted` rows whenever a deferral is lifted. [2]
