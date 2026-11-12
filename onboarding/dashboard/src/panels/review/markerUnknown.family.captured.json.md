# dashboard/src/panels/review/markerUnknown.family.captured.json

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Retain a test-only input/capture receipt for the reviewer.

## Code Commentary

The facts below are read from the retained source bytes, not from a fresh producer invocation.

### Retained Input Facts

- `state`: "review"
- `operation`: "read_knowledge_review"
- `repository_id`: "agents-remember"
- `candidate`: {"repository_id": "agents-remember", "master": "260928_maintained-invariant-knowledge", "leaf_id": "260928-MIK-L34", "task_ref": "260928_maintained-invariant-knowledge"}
- `knowledge.selection_state`: "subject_selected"
- `knowledge.revision_selection`: {"record_kind": "family", "record_id": "8519c70b-92ae-5ad6-9c6c-2fcf83d498ea", "state": "removed", "before_revision_id": "1b7ca0b9-0423-544f-8ba1-044bb13adc0f", "before_retained": ["1b7ca0b9-0423-544f-8ba1-044bb13adc0f"], "after_retained": []}
- `knowledge.statement_states`: {"before_statement": "present", "after_statement": "absent"}
- `judgment`: {"state": "unavailable", "detail": "the after memory index is incomplete (1 file(s) failed: knowledge/families/FAM-4V4GSQCS-Bounded-notes-listing-with-unchanged-meaning.json); history it did not read cannot be reported as absent"}
- `judgment.rows`: []
- `judgment.proofs`: []
- `meaning_effects`: {"records": [{"record": "8519c70b-92ae-5ad6-9c6c-2fcf83d498ea", "kind": "family", "state": "unavailable", "detail": "the after memory index is incomplete (1 file(s) failed: knowledge/families/FAM-4V4GSQCS-Bounded-notes-listing-with-unchanged-meaning.json); history it did not read cannot be reported as absent", "steps": []}]}
- `source.inventory`: {"state": "measured", "listed_total": 4, "partial": false, "detail": "the two requested code trees differ at 4 path(s); every one is listed with the change status Git reported for it, whether or not its content can be rendered"}
- `family_context.state`: "partial"
- `family_context.detail`: "this family context is partial: every part it did establish is carried, and the parts it could not establish are stated with their reason -- 8519c70b-92ae-5ad6-9c6c-2fcf83d498ea (unavailable: family presence could not be established on after: the after family scope could not be fully read: knowledge/families/FAM-4V4GSQCS-Bounded-notes-listing-with-unchanged-meaning.json: a knowledge document names its format in a string 'schema' field), the after snapshot's scope was not read"
- `family_context.entries`: {"family_id": "8519c70b-92ae-5ad6-9c6c-2fcf83d498ea", "display_label": "Bounded notes listing with unchanged meaning", "state": "unavailable", "selection": {"state": "unresolved"}, "before": {"state": "not_resolved", "members_total": 0, "detail": "family presence could not be established on after: the after family scope could not be fully read: knowledge/families/FAM-4V4GSQCS-Bounded-notes-listing-with-unchanged-meaning.json: a knowledge document names its format in a string 'schema' field", "returned_members": 0, "guarantee": {}, "page": {}, "continuation_present": false, "continued_from_present": false}, "after": {"state": "unreadable", "members_total": 0, "detail": "the after family scope could not be fully read: knowledge/families/FAM-4V4GSQCS-Bounded-notes-listing-with-unchanged-meaning.json: a knowledge document names its format in a string 'schema' field", "returned_members": 0, "guarantee": {}, "page": {}, "continuation_present": false, "continued_from_present": false}, "change_kinds": {"guarantee": "unknown", "member_primary_counts": {}}}
- `removed_channels_absent`: {"payload.evidence": true, "knowledge.signals": true, "knowledge.assessments": true}

These are fixture facts, not current project knowledge. A receipt states its recorded capture custody; reading it here does not recreate its command or validate an installed dashboard.

## Evidence

- The retained source supplies the facts and declared boundaries described above. [1]
