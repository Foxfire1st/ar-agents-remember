# mcp/tests/test_knowledge_review_evidence_channels.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

**The production composition supplies every owner-produced record class** (`ICR-R14@v1`). **10 cases**,
all in the `unit-regression` lane (`pytestmark = pytest.mark.evidence_unit`; the module's own lane row
is `mcp/tests/test-evidence-lanes.toml:108`).

F09's defect is one omission with three faces, and this module measures each of them against the
**production port** rather than against a prebuilt payload: the dashboard's record loader supplied only
the curator assessments, collapsed "the authority published none" and "the authority could not be read"
into one empty tuple, and never supplied the detector signals, the verification observations or any
statement of the currentness nobody measured. Every case drives
`cli.dashboard.serving_collaborators` — the same port `create_app` is given — over a real leaf
enclosure with real datasets.

**Every record class is produced through the operation that owns it, never assembled by hand.** The
fixture records a detection run and its signal through `detection.record_detection_run`, a verification
observation and an evidence claim through the application evidence writer, an authored effect through
the candidate batch operation, and an assessment through the curator-coherence publication. A case that
merely asserted a returned prebuilt payload could not fail the way the packet requires the defect to
fail, which is why no case here builds one.

## Code Commentary

### Logic

**`RecordedFixture` is one live enclosure whose candidate dataset holds records written by their
owners**, and it exposes the two reads the cases use: `records()` returns the bundle
`review_records_for` resolves, and `payload()` returns the payload the production port produces
(failing loudly on a refusal). `build_recorded_fixture` builds the enclosure through the shared
endpoint fixture with `memory_mode="external"` — a real memory repo with a linked worktree, because the
assessment channel goes through the curator authority, which needs one — then produces one record of
every class and publishes the assessment last. `_channels` indexes the served payload's channel list by
collection name, which is how a case states a state rather than a collection length.

**The ten cases, one property each:**

1. `test_the_production_composition_supplies_every_owner_produced_record_class` (`:552-605`) — every
   available class arrives with its own fields intact: the signal with its condition, declared input
   set and scope limitations; the observation with its result artifact, digest and tested candidate;
   the claim link with the author, lifecycle, declared limitations and asserted coverage the owner
   holds; the authored effect and the assessment with author, role and examined inputs; and all five
   channels `recorded` with their counts. The observation recorded against a **foreign** candidate tree
   is asserted **absent**, so the execution collection is the candidate's own binding rather than a
   namespace listing.
2. `test_an_unpublished_authority_is_a_measured_absence_and_a_corrupt_one_is_unavailable` (`:607-634`)
   — the two states the defect collapsed, side by side on one fixture: the canonical authority file
   removed gives `none_recorded` with a real zero and "absent" in its detail; the same file's bytes
   replaced gives `unavailable` with **no** count, the file named in `unreadable`, a next action and
   the name in the detail; restoring the bytes returns `recorded`.
3. `test_one_unreadable_authority_leaves_every_readable_class_supplied` (`:636-653`) — the packet's own
   boundary example: a corrupt authority leaves assessments unavailable and empty while the signals,
   the observation and the claim's authored fields are still supplied.
4. `test_a_task_context_review_reports_the_matrix_collection_as_not_selected` (`:655-677`) — the same
   fixture read through the task-context entry: the matrix-owned collection is `not_selected` with no
   count and a next action, while the candidate-owned collections (claims, signals, assessments) are
   still `recorded`; the empty evidence-link list states that no matrix row selected one for display.
5. `test_the_composition_measures_the_bindings_it_reads` (`:693-743`) — the case `260921-ICR-L15`
   renamed because its premise inverted: the composition now holds **its own** measurement
   (`records.currentness.state == "measured"`, with a value for the comparison's candidate endpoint)
   rather than a mapping whose absence stood for one, so an assessment whose declaration is wider than
   what this comparison publishes is reported **`not-measured`** — neither promoted to current nor
   claimed as moved.
6. `test_a_damaged_detection_run_is_named_while_its_siblings_are_supplied` (`:695-717`) — two healthy
   runs plus one whose stored seal was rewritten: the channel is `recorded` with `record_count == 2`
   and `unreadable == (damaged_run,)`, the two healthy signals are supplied and the damaged run's is
   not; the review still renders.
7. `test_a_damaged_evidence_claim_is_named_while_its_siblings_are_supplied` (`:719-745`) — a second
   claim whose stored payload was replaced: the channel is `recorded` with count 1 and the damaged
   identity named; the healthy claim's link keeps its author, lifecycle and limitations, and the
   damaged claim keeps its identity, is rendered with `limitations == ()` and an `unresolved` reference
   of field `claim_content` — never as a claim that declared no limitations.
8. `test_an_unresolvable_candidate_reports_every_collection_unavailable` (`:747-759`) — a candidate
   that does not resolve supplies no records, every channel is `unavailable` or `not_measured`, and the
   channel list has one entry per collection name.
9. `test_the_channel_model_refuses_a_count_no_owner_measured` (`:761-787`) — the vocabulary's own
   refusals: a count on `unavailable`, a missing next action, and a `recorded` channel with zero
   records each raise.
10. `test_the_wire_payload_carries_the_channels` (`:789-796`) — the channel list is part of the served
    payload's JSON schema (`ReviewRecordChannel`, `not_measured`), not a local return value.

**The two damage cases damage the stored row the way this repository's own damage fixtures do** — the
`record_revision_no_rewrite` trigger is dropped, the row is rewritten, and the trigger is restored with
the schema's own SQL (`APPENDED_TRIGGERS`). Dropping the trigger without restoring it would make the
whole database unreadable as this schema, which is a different failure and would hide the per-record
isolation the two cases exist to measure.

### Conventions

Cases are hermetic: a fresh enclosure per case (`tmp_path`), real databases and real curator authority
bytes, and the shared fixtures rather than per-module topology — `build_endpoint_fixture` /
`EndpointFixture` from `mcp/tests/test_knowledge_review_source_endpoints.py`,
`write_curator_task_topology` from `mcp/tests/curator_coherence_test_support.py`, and
`write_passing_route_review` from `mcp/tests/test_worktree_support.py`. The module registers **no**
artifact and no contract of its own; it is a source-derived consumer of four existing catalog rows,
each `consumer_scope = "exact"`: `mcp/tests/curator_coherence_test_support.py`,
`mcp/tests/diff_scope_test_support.py`, `mcp/tests/read_scope_test_support.py` and the Node
`package-lock.json` fixture (reached through the support modules those rows already name). Nothing in
the module writes outside its temporary root, and no shipped case was changed.

### Invariants And Boundaries

- **The production port is the entry under test.** Every case except the two that drive the bundle and
  the model directly reads through `serving_collaborators(...).knowledge_review`, so a composition that
  stopped supplying a class fails here rather than in a hand-built payload.
- **The records are produced, never fabricated.** Each class is written through the owner's own
  operation before it is read back.
- **Absent, unreadable and not-measured are asserted as three different states**, each on its own case,
  and an unreadable collection is asserted to carry **no** count.
- **One damaged record does not withdraw its class**, and is asserted to be named rather than dropped.
- **No case asserts a favourable default**: the currentness case asserts that nothing is promoted to
  current, and the vocabulary case asserts the refusals that keep a favourable default unrepresentable.
- **The fixture's external-memory mode is load-bearing** for any case whose records go through the
  curator authority; the parameter is additive on the shared endpoint fixture and defaults to
  `"disabled"`.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the module's own docstring, fixture and cases, in the
production port they drive, in the composition and vocabulary under test, and in the two catalogs that
register the module.

- The module's own statement of the defect, the ports it drives, the four record-producing operations, and the five load-bearing properties. [1]
- **The live-enclosure fixture with the two reads every case uses, and the two halves of its candidate binding.** [2]
- **The production port every case reads through — the same `serving_collaborators` the dashboard app is built with.** [3]
- **The fixture that produces one record of every class through its own owner, over an external-memory enclosure.** [4]
- The four record-producing helpers: the detection run, the claim, the observation and the authored effect. [5]
- **The damage helper that keeps the dataset readable as this schema: drop the trigger, rewrite the row, restore the trigger with the schema's own SQL.** [6]
- The publication helper the assessment channel is produced through, and the channel index the cases state states with. [7]
- **The case that proves every available class arrives with its owner's own fields, and that a foreign candidate's observation is not selected.** [8]
- **The case that measures the two states the defect collapsed, side by side on one fixture.** [9]
- **The packet's boundary example: one unreadable authority, every readable class still supplied.** [10]
- **The case that distinguishes "not read" from "read and empty" for the matrix-owned collection.** [11]
- **The case that proves the composition measures the bindings it reads rather than inferring from a mapping's presence, and that a partial measurement promotes nothing to current.** [12]
- **The two per-record damage cases: one damaged identity named while its siblings are supplied.** [13]
- **The case that an unresolvable candidate reports every collection unavailable rather than empty.** [14]
- **The case that measures the vocabulary's own refusals, and the wire case that the channels travel in the served schema.** [15]
- **The lane row that registers the module, and the four catalog consumer rows it is a source-derived consumer of.** [16]
- The composition, the resolver and the vocabulary the cases measure. [17]

### Cross-Repo References

No cross-repository behavior is implemented in this file. Its fixtures are in-process or local
temporary directories and it touches no repository boundary.

No meaningful cross-repo references found.
