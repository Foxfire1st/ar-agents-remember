# mcp/tests/test_knowledge_review_evidence_channels.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose
Checks review evidence-channel states and currentness measurement of published immutable curator assessments.

## Code Commentary
The converted fixture publishes assessments through their own authority. Cases distinguish unpublished from corrupt/unreadable authority, the retired matrix collection (unavailable with its removal as the reason), measured binding/currentness axes and stale candidates. Retained immutable generations survive damage to the live authority; an unresolvable candidate leaves collections unavailable. Channel counts are refused when their owner did not measure them. Canonical detection, evidence-claim and verification-observation producers and their former tests are removed; no empty-count replacement or executed run is claimed.

### Invariants And Boundaries
- **The production port is the entry under test.** The cases that call `recorded.payload()` or `review_through_port` read through `serving_collaborators(...).knowledge_review`. Other retained cases drive the record bundle, currentness owner or channel/pane/schema models directly; the production-port claim is limited to its actual callers.
- **Absent, unreadable and not-measured are asserted as three different states**, each on its own case,
  and an unreadable collection is asserted to carry **no** count.
- **No case asserts a favourable default**: the currentness case asserts that nothing is promoted to
  current, and the vocabulary case asserts the refusals that keep a favourable default unrepresentable.

### Todos
None recorded.

## Evidence

### Repo-Internal References

Every claim on this card is checkable in the module's own docstring, fixture and cases, in the
production port they drive, in the composition and vocabulary under test, and in the two catalogs that
register the module.



### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Cross-Repo References

No cross-repository behavior is implemented in this file. Its fixtures are in-process or local
temporary directories and it touches no repository boundary.

No meaningful cross-repo references found.

- `test_the_composition_measures_the_bindings_it_reads` owns the current boundary described above. [18]
- `test_a_retained_curator_generation_survives_a_damaged_live_authority` owns the current boundary described above. [19]
- `test_the_channel_model_refuses_a_count_no_owner_measured` owns the current boundary described above. [20]
- `test_an_unresolvable_candidate_reports_every_collection_unavailable` owns the current boundary described above. [21]

- **The retained live-enclosure fixture exposes records() (the direct record bundle), payload() (through the knowledge_review port), and candidate dataset/tree bindings. Direct owner/model/schema cases do not all use these reads.** [22]


- **The production knowledge_review port used by review_through_port/recorded.payload cases, through the same serving_collaborators factory as the dashboard; other retained cases exercise owners/models directly.** [23]

- The publication helper the assessment channel is produced through, and the channel index the cases state states with. [24]
- **The case that measures the two states the defect collapsed, side by side on one fixture.** [25]

- The retained matrix case asserts the retired authored-effects collection is unavailable with no count and the MIK-R74 removal reason; it does not measure an empty matrix. [26]

- **The case that proves the composition measures the bindings it reads rather than inferring from a mapping's presence, and that a partial measurement promotes nothing to current.** [27]
- **The case that an unresolvable candidate reports every collection unavailable rather than empty.** [28]
- **The case that measures the vocabulary's own refusals, and the wire case that the channels travel in the served schema.** [29]
