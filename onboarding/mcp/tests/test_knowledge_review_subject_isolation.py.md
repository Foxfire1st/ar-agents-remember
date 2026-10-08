# mcp/tests/test_knowledge_review_subject_isolation.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Checks selected-subject isolation of published curator assessments, their retained bindings and the independently complete source inventory.

## Code Commentary

The journey classifies own assessments as direct, sibling assessments as context, unrelated ones as counted but not displayed, and malformed/unresolved bindings as unresolved. A previous immutable generation is historical rather than current. Page size does not change classification, direct labels must cite a retained list containing the record, and every supplied collection reports its own complete population. The fixture publishes through `_publish_assessments`; canonical detection/evidence-claim/observation/effect producers and their old helpers were removed. A source inventory denominator is independent of record selection. This card claims test assertions, not a thirteen-case or runtime PASS.

## Evidence

### Repo-Internal References

- `test_a_sibling_subjects_assessment_is_context_and_never_the_selected_subjects` owns the current boundary described above. [21]
- `test_every_page_size_classifies_the_same_records_the_same_way` owns the current boundary described above. [22]
- `test_the_source_inventory_is_independent_of_the_record_selection` owns the current boundary described above. [23]
- `_publish_assessments` owns the current boundary described above. [24]
