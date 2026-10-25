# dashboard/src/panels/review/markerUnknown.memberUnknown.captured.json

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Retained test-only response body. This retained fixture has an unreadable after-family scope, a partial/unavailable family context and unavailable judgment history while selected invariant source remains readable.

## Code Commentary

This retained fixture has an unreadable after-family scope, a partial/unavailable family context and unavailable judgment history while selected invariant source remains readable. Its failed family read is not a measured zero and does not supply a missing member row.

### Retained Input Facts

- `state`: "review"
- `operation`: "read_knowledge_review"
- `repository_id`: "agents-remember"
- `candidate`: {"repository_id": "agents-remember", "master": "260928_maintained-invariant-knowledge", "leaf_id": "260928-MIK-L34", "task_ref": "260928_maintained-invariant-knowledge"}
- `knowledge.selection_state`: "subject_selected"
- `knowledge.revision_selection`: {"record_kind": "invariant", "record_id": "c7c5be49-164f-56e0-923d-fb5f5259d80c", "state": "compared", "before_revision_id": "a1c28709-da32-5ca3-91c4-5e43f5c498da", "after_revision_id": "a1c28709-da32-5ca3-91c4-5e43f5c498da", "before_retained": ["a1c28709-da32-5ca3-91c4-5e43f5c498da"], "after_retained": ["a1c28709-da32-5ca3-91c4-5e43f5c498da"]}
- `knowledge.statement_states`: {"before_statement": "present", "after_statement": "present"}
- `judgment`: {"state": "unavailable", "detail": "the after memory index is incomplete (1 file(s) failed: knowledge/families/FAM-4V4GSQCS-Bounded-notes-listing-with-unchanged-meaning.json); history it did not read cannot be reported as absent"}
- `judgment.rows`: []
- `judgment.proofs`: []
- `meaning_effects`: {"records": [{"record": "c7c5be49-164f-56e0-923d-fb5f5259d80c", "kind": "invariant", "state": "unavailable", "detail": "the after memory index is incomplete (1 file(s) failed: knowledge/families/FAM-4V4GSQCS-Bounded-notes-listing-with-unchanged-meaning.json); history it did not read cannot be reported as absent", "steps": []}, {"record": "8519c70b-92ae-5ad6-9c6c-2fcf83d498ea", "kind": "family", "state": "unavailable", "detail": "the after memory index is incomplete (1 file(s) failed: knowledge/families/FAM-4V4GSQCS-Bounded-notes-listing-with-unchanged-meaning.json); history it did not read cannot be reported as absent", "steps": []}]}
- `source.inventory`: {"state": "measured", "listed_total": 4, "partial": false, "detail": "the two requested code trees differ at 4 path(s); every one is listed with the change status Git reported for it, whether or not its content can be rendered"}
- `family_context.state`: "partial"
- `family_context.detail`: "this family context is partial: every part it did establish is carried, and the parts it could not establish are stated with their reason -- 8519c70b-92ae-5ad6-9c6c-2fcf83d498ea (unavailable: family presence could not be established on after: the after family scope could not be fully read: knowledge/families/FAM-4V4GSQCS-Bounded-notes-listing-with-unchanged-meaning.json: a knowledge document names its format in a string 'schema' field), the after snapshot's scope was not read"
- `family_context.entries`: {"family_id": "8519c70b-92ae-5ad6-9c6c-2fcf83d498ea", "display_label": "Bounded notes listing with unchanged meaning", "state": "unavailable", "selection": {"state": "unresolved"}, "before": {"state": "not_resolved", "members_total": 0, "detail": "family presence could not be established on after: the after family scope could not be fully read: knowledge/families/FAM-4V4GSQCS-Bounded-notes-listing-with-unchanged-meaning.json: a knowledge document names its format in a string 'schema' field", "returned_members": 0, "guarantee": {}, "page": {}, "continuation_present": false, "continued_from_present": false}, "after": {"state": "unreadable", "members_total": 0, "detail": "the after family scope could not be fully read: knowledge/families/FAM-4V4GSQCS-Bounded-notes-listing-with-unchanged-meaning.json: a knowledge document names its format in a string 'schema' field", "returned_members": 0, "guarantee": {}, "page": {}, "continuation_present": false, "continued_from_present": false}, "change_kinds": {"guarantee": "unknown", "member_primary_counts": {}}}
- `removed_channels_absent`: {"payload.evidence": true, "knowledge.signals": true, "knowledge.assessments": true}

These are fixture facts, not current project knowledge. A receipt states its recorded capture custody; reading it here does not recreate its command or validate an installed dashboard.

## Prior Fixture Account — Historical Only

The following account describes the earlier fixtures and assertion scope. Its present-tense clauses and numbered labels are historical, not current guarantees, current evidence or a fresh run. The current source account above states what is still exercised and what was removed.

> # dashboard/src/panels/review/markerUnknown.memberUnknown.captured.json
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> **A real `GET /api/review/intent` review of INV-Z66EMHMH on comparison 3 of the MIK-L34 scratch leaf** (102,922 bytes; test
> evidence for `ReviewSurface.markers.test.tsx` and, since MIK-L33's merge round, `ReviewSurface.triageMarkers.test.tsx` and `MarkerTargetState.test.tsx`: the review a family-named unknown
> target opens).
>
> ## Code Commentary
>
> ### Logic
>
> - The review still composes FAM-4V4GSQCS's context (`recorded`, one family), so a family-named unknown target lands on
>   that family's member row, which carries the `Attribution unknown` state; a family-less target of the same invariant
>   shows the state above the tree (review R1 F3).
> - The limitations name `review:trees:3` and `knowledge-index:after:partial`.
> - **`change_kinds` (MIK-L33):** guarantee `unknown` and `members_total` absent, because the after side's
>   FAM-4V4GSQCS record does not parse; every one of the five members has membership `unknown` with that record as its
>   `membership_reasons`; INV-Z66EMHMH, INV-EJW15DXA and INV-ZJS1XY4R read `implementation` `+unknown` (the unknown mark
>   is the membership), INV-QR24S1VH and INV-DA7D417G `unknown`. So on a tree comparison the followed member row states
>   its unknown membership once, as the tagged membership line with the comparison's reason (MIK-L33 merge round).
>
> - **Re-captured in MIK-L33's merge round** over the merged tree (MIK-L34 landed; the review route now carries `change_kinds`). Against MIK-L34's capture it differs only by scratch paths, the converted memory commit, timestamps and comparison digests, and it now carries FAM-4V4GSQCS's `change_kinds` (the reviewer's structural diff, review R3 point 5).
>
> ### Conventions
>
> Keep the captured bytes and their receipt intact; a recapture rewrites both.
>
> ### Invariants And Boundaries
>
> The body describes the scratch copies under `/tmp/mik-l33-merge`: MIK-L34's scenario, rebuilt by MIK-L33's merge round with MIK-L34's own scripts (code `59daf505` with the scratch leaf's edits and the same curated blobs `9019bea5` and `b6d07091`; memory `76f5e91e1` converted and committed as scratch `main` `31ab7016`), not current project knowledge; its line numbers, blobs and keys are the scratch tree's.
>
> ### Todos
>
> No additional work is asserted by this card.
>
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.
>
> No configured live documentation source was available for this pass.
>
> ### Repo-Internal References
>
> - The composed family context. (historical reference 1)
> - The comparison token and the partial after index. (historical reference 2)
> - The receipt row for this body. (historical reference 3)
> - The family's change facts with every membership unknown (MIK-L33). (historical reference 4)
>
> ### Cross-Repo References
>
> No cross-repo boundary is crossed by this file.

## Evidence

- This retained fixture has an unreadable after-family scope, a partial/unavailable family context and unavailable judgment history while selected invariant source remains readable. Its failed family read is not a measured zero and does not supply a missing member row. [5]
