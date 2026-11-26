# mcp/tests/test_state_conversion_worklist.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Unit-regression suite protecting `state_conversion_only` (`mcp/src/agents_remember/memory/conversion/state_conversion.py`), `KnowledgeSide.record_file_changed` (`mcp/src/agents_remember/application/knowledge_worklist/knowledge.py`), and the three worklist record-comparison sites (`classify.py`, `reconsideration.py`, `touched_records.py`) so that state-conversion-only record edits raise no worklist items while every non-conversion edit still raises.

## Code Commentary

- `test_plan_changes_satisfy_predicate_and_raise_no_worklist_items` builds a disposable converted world with invariants (`proposed`, `accepted`, `retired`), a family, an assumption with a Markdown sidecar, a decision carrying `reconsider_on` links, a dependent, and closed history supplying both `by="conversion"` and `by="agent"` stamps; it asserts every record path in `plan_state_conversion(...).changes` satisfies `state_conversion_only` and yields zero worklist items (`reachedFamilies == []`, `classifiedEntries == 0`).
- `test_predicate_accepts_every_valid_writer_stamp_source` parametrizes over `conversion`, `agent`, and `product` `WriterStamp` payloads to confirm each valid stamp source is accepted.
- `test_predicate_handles_status_only_removal_and_rejects_formatting_or_bad_stamps` checks status-only removal on an already-stamped record, rejects identical bytes, non-canonical base/candidate formatting, partial conversions (missing stamp or lingering legacy status), and malformed `WriterStamp` payloads.
- `test_rule_3_non_legacy_status_writer_change_and_field_edit_still_raise` verifies that non-legacy status changes (`retired` removed, `active` changed to `under_reconsideration`), edits or removals of an existing `writer`, edits to any other field alongside conversion, and absent records on either side still count as changed and raise their worklist items.
- `test_moved_and_converted_records_still_raise` verifies that renaming an invariant, family, or assumption while converting still raises `touched_invariant`, `reached_family`, and `reconsideration_candidate`.
- `test_changed_markdown_sidecar_still_raises_on_converted_record` parametrizes over edited, deleted, and added `.md` sidecars on a converted assumption and asserts `touched_record` still raises.
- `test_raise_mark_only_and_deferral_answering_rule_are_unchanged` verifies that the leaf's own open `raise` mark exemption (`_raise_mark_only`) and the `deferralOnly` / `record_row_open` answering rule remain intact.

## Relationships

- Registered once in `unit-regression` in `mcp/tests/test-evidence-lanes.toml` and as an exact consumer of `mcp/tests/_user_settings_guard.py` and `mcp/tests/fixtures/repository_profiles/node/package-lock.json` in `mcp/tests/evidence-lifecycle.toml`.
- Reuses `World` and `_init` from `mcp/tests/test_knowledge_worklist.py` for disposable Git-backed code and memory repositories.
- Source assertions described here are module contracts, not a fresh execution or certification claim.

## Evidence

- Every record path in a conversion plan satisfies `state_conversion_only` across both `conversion` and `agent` stamps and raises zero worklist items. [1]
- Valid `conversion`, `agent`, and `product` writer stamps satisfy `state_conversion_only`. [2]
- Status-only removal passes while identical bytes, non-canonical formatting, partial conversions, and invalid stamps return `False`. [3]
- Non-legacy status edits, existing writer modifications/removals, other field edits, and absent records still raise. [4]
- Moved and converted records still raise `touched_invariant`, `reached_family`, and `reconsideration_candidate`. [5]
- Edited, deleted, or added Markdown sidecars on converted records still raise `touched_record`. [6]
- Own-open `_raise_mark_only` exemption and `deferralOnly` answering rules in `record_row_open` remain unchanged. [7]
