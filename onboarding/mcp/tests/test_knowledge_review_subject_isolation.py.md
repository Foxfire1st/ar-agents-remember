# mcp/tests/test_knowledge_review_subject_isolation.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

**One selected subject's review displays only the records that subject may be judged by**
(`ICR-R26@v1`). **13 cases**, all in the `unit-regression` lane (`pytestmark = pytest.mark.evidence_unit`;
the module's own lane row is registered in `mcp/tests/test-evidence-lanes.toml`, which refuses an
unregistered module at collection).

F09's defect is one omission with two faces: the review adapter handed the candidate-wide review matrix
and every supplied assessment to the selected subject's panes, so a valid assessment of a **sibling**
invariant was displayed in both panes of a different invariant. `ICR-R14@v1` delivers the complete
owner-produced collections; these cases measure the attribution half — which of those records may be
displayed beside which subject, and why — through the **production composition**
(`cli.dashboard.serving_collaborators`, the same port `create_app` is given) over a real leaf enclosure
whose records are produced by their owning operations:

- **five** assessments published through the curator-coherence authority — for the selected subject,
  for a sibling invariant the selection's recorded relationships reach, for an invariant the selection
  does **not** reach, for an identity neither snapshot records, and one that names the selected
  subject's own identity where a revision belongs (the malformed binding);
- a detection run holding two signals — one whose recorded path reaches the selection, one whose path
  reaches nothing the selection holds;
- a verification observation bound to the candidate, an evidence claim whose recorded subject is the
  selected subject's own revision, and an authored open question that records no subject at all;
- and a **source movement after publication**, so the same assessment is measured once as this
  generation's record and once as historical input of the previous one.

**No case builds a payload by hand.** A case that asserted a prebuilt body could not fail the way the
packet requires the defect to fail, which is why every supplied record comes from the operation that
owns it and every read goes through the production port.

## Code Commentary

### Logic

**`Journey` is one live enclosure plus the two reads the cases use, and it fails loudly on a refusal.**
`read(page_size)` calls the production port with the fixture's own request, copied with the page size
under test, and asserts `state == "review"` with a payload before returning it — so a refusal is a test
failure with its own reason rather than a silently different assertion. `treatments` maps each displayed
assessment identity to the treatment its label carries (`<absent>` when the pane does not display it);
`state_of` answers one identity the same way; `summary` returns the applicability summary of one
collection. The module-scoped `journey` fixture builds the enclosure once (the publication journey is
expensive and read-only afterwards), and the `moved` fixture adds one source file to the worktree and
re-reads, which is what makes the same assessment a previous generation's record.

**The thirteen cases, one property each:**

1. `test_a_sibling_subjects_assessment_is_context_and_never_the_selected_subjects` (`:221-252`) — the
   F09 shape: the sibling's assessment is in **neither** pane's assessment collection, and appears as
   exactly one labelled context row in both panes with its true subject, its recorded relationship, its
   author and role, and its **kind** as the label (`assessment/invariant-revision`) — with no
   disposition anywhere in the serialized row, because that finding belongs to the sibling's own review.
2. `test_the_selected_subjects_own_assessment_is_direct_with_its_recorded_binding` (`:255-272`) — the
   knowledge pane displays exactly the three records that may be judged by this subject; the direct one
   is `direct`, names the selected identity, carries the two recorded revisions the selection records
   and the declared candidate tree among its references, and keeps its provenance verbatim.
3. `test_an_unrelated_subjects_assessment_is_counted_and_not_displayed` (`:275-293`) — a subject the
   recorded relationships do not reach is absent from both panes and from the context rows, and the
   summary states the whole supplied population (`supplied == 5`, `direct 1 / context 1 / unresolved 2 /
   unrelated 1`) with the sentence that names how a reader reaches those records.
4. `test_an_unresolvable_binding_is_displayed_unresolved_with_its_references` (`:296-310`) — a record
   naming an identity nothing records is displayed `unresolved` with its subject, its references and
   the reason, and its binding state is the unmeasured one, never current.
5. `test_a_previous_generations_assessment_is_historical_and_never_current` (`:313-333`) — after the
   source movement the same assessment is `historical`, names the candidate tree it really examined,
   and the displayed comparison shows the new tree.
6. `test_a_malformed_revision_binding_is_unresolved_and_never_a_retained_revision` (`:336-358`) — the
   F-V1 case: an assessment that carries the selected invariant's *identity* where a revision belongs
   is `unresolved`, its detail says a reference that is not a recorded revision of the subject is never
   matched, and it claims no retained revision.
7. `test_every_page_size_classifies_the_same_records_the_same_way` (`:361-395`) — the F-V2 case: at
   every page size in the fixture's series the treatments, the context signature (identity, true
   subject and recorded relationship spelling) and the summary are identical, and exactly the one
   genuinely unreachable subject is counted `unrelated`, so no page size may report a
   recorded-reachable record as unreachable.
8. `test_a_direct_label_never_cites_a_retained_list_that_does_not_carry_the_record` (`:398-434`) — the
   F-V6 case: at every page size the `direct` sentence carries exactly one of the two bases, and citing
   ICR-R07 **requires** R07's own published retained lists — read back from the pane's own
   `revision_selection` — to carry the matched revisions.
9. `test_every_supplied_collection_reports_its_complete_population` (`:437-455`) — the owner's complete
   counts stay on the R14 channels beside the pane's own population, and every summary partitions its
   collection exactly.
10. `test_the_records_own_bindings_attribute_the_signals_and_the_claim` (`:458-503`) — a signal's own
    recorded relationship path decides whether it is `direct` or `unresolved` (the latter keeping the
    path it recorded); the evidence claim is attributed `direct` by its own recorded subject revision;
    the observation bound to the candidate is `candidate`; and the authored question that records no
    subject is `unresolved` with the reason it could not be attributed.
11. `test_the_source_inventory_is_independent_of_the_record_selection` (`:506-517`) — the inventory is a
    measurement of the two bound code trees, so it still lists a path no displayed record relates to
    and does not list the file added after the read.
12. `test_the_class_vocabulary_is_the_record_vocabulary_minus_its_measurement_channel` (`:520-525`) —
    the applicability classes and the record-class channels cannot drift apart.
13. `test_a_label_and_a_summary_refuse_a_claim_their_recorded_facts_do_not_support` (`:528-553`) — both
    shapes refuse at construction the two lies this requirement is about: a `direct` label naming no
    subject, and a summary whose counts do not partition its population.

**The fixture produces every record class through its owner, and the publication is real.** `_build_journey`
(`:561-598`) builds the enclosure through the shared endpoint fixture with an external memory half — a
real memory repo with a linked worktree, because the assessment channel goes through the curator
authority — writes the task topology the publication binds, then publishes the five assessments
(`_publish_assessments`, `:613-692`), records the detection run and its two signals
(`_record_detection_run`, `:715-775`), the evidence claim (`_record_evidence_claim`, `:821-836`), the
verification observation (`_record_observation`, `:839-862`) and the authored open question
(`_record_authored_effect`, `:865-899`), and finally reads the page-size series once
(`_read_through_port`, `:601-610`). The curator publication validates structure rather than whether the
subject's snapshot records the revision a record names, which is exactly why the malformed case is a
real publication rather than a hand-built value.

### Conventions

`pytestmark = pytest.mark.evidence_unit` puts every case in the `unit-regression` lane, and the module
carries one lane row in `mcp/tests/test-evidence-lanes.toml` plus four exact-scope consumer rows in
`mcp/tests/evidence-lifecycle.toml` (`curator_coherence_test_support.py`,
`fixtures/repository_profiles/node/package-lock.json`, `diff_scope_test_support.py`,
`read_scope_test_support.py`), each derived from the census's own missing list on all four. Helpers are
private and single-purpose (`_assessment`, `_signal`, `_destination`, `_candidate_snapshot`,
`_candidate_store`), and no case reaches a store, a snapshot file or a database directly: the port is
the only read, and the fixture's own endpoint object supplies the identities a case asserts against.

### Invariants And Boundaries

- **The port is the only read.** Every case reads through `serving_collaborators(...).knowledge_review`;
  no case builds a payload, and a refusal fails the case with its own reason.
- **Every record is produced by its owner.** Assessments through the curator-coherence publication, the
  detection run through the detector, the claim and the observation through the application evidence
  writer, the authored question through the admitted candidate batch.
- **The module does not assert beyond its leaf.** Currentness (R15), the family-context composition
  (R31), the assembled A14/A15 acceptance (R25), the accepted reviewer workspace (R24) and the browser
  journey are other leaves' measurements and are deliberately not claimed here.
- **The page is an input, never a premise.** The series exists so a bounded page can be shown to change
  nothing about a record's meaning; a case that only read the default page would not have caught the
  F-V2 defect this series pins.
- **A case measures one property.** The ten behaviour cases are one assertion family each, so a failure
  names the property that broke rather than a fixture that drifted.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The module's own statement of the defect it pins, the records its fixture produces and the properties its cases measure.** [1]
- **The live enclosure and the reads the cases use, with a refusal failing the case rather than changing the assertion.** [2]
- **The one enclosure per module, and the read after the source moved.** [3]
- **The F09 case: the sibling's record is in neither pane's assessments and is labelled context with its kind, its true subject and none of its finding.** [4]
- **The selected subject's own record, with the binding its label names and its provenance verbatim.** [5]
- **The exclusion as arithmetic: an unreachable subject is counted, not displayed, and the summary names how to reach it.** [6]
- **An unresolvable binding displayed with its references and never as support.** [7]
- **A previous generation's record labelled historical with the tree it examined, and never current.** [8]
- **The F-V1 case: a malformed revision binding is unresolved and claims no retained revision.** [9]
- **The F-V2 case: every page size classifies the same records the same way, context included.** [10]
- **The F-V6 case: a `direct` sentence cites ICR-R07 only when R07's own published list carries the matched revisions.** [11]
- **The complete populations: the channels' counts beside the pane's own, and every summary a partition.** [12]
- **The attribution of the signals, the claim, the observation and the subject-less authored question.** [13]
- **The source inventory is a measurement of the two bound trees and is untouched by record selection.** [14]
- **The two vocabulary refusals, measured at construction.** [15]
- **The fixture that produces every record class through its owner and reads the page-size series once.** [16]
- **The production port every case reads through.** [17]
- **The production policy these cases measure.** [18]
- **The vocabulary these cases read their assertions from.** [19]
- **The lane row that registers this module — `unit-regression` is a bare TOML key, so it is named here rather than anchored — and the first of the four consumer rows its cases are derived for.** [20]

### Cross-Repo References

No cross-repository behavior is exercised by this module. Its enclosure is one repository's own leaf
worktree with an external memory half.

No meaningful cross-repo references found.
