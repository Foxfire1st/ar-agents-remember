# mcp/tests/test_historical_committed_leaf_review.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The cases that measure `ICR-R12@v1`'s produced behaviour through the real production composition**
— a real enclosure, a real linked worktree, the real capture and resolution owners, the real comparison,
R11's real freeze and the real HTTP route — rather than through a preconstructed payload. The packet's
own verification requirement is what shapes the module: "Compare a live frozen leaf and its
closed/cleaned/restarted view byte-for-byte; advance the branch and prove no contamination", and "tests
that merely mirror implementation or assert returned prebuilt payloads are insufficient for production
composition claims". Every assertion here therefore reads **served bytes** or an owner's own value, never
a value this module assembled.

The module carries the intake defect as its subject: a cleaned leaf's Intent Review answered
`candidate_not_live` because the history route required `contract.code_worktree.exists()`. Eight cases
measure the eight properties that replace it, one each:

- a leaf frozen while it was live, its worktree group removed exactly as cleanup removes it, serves
  **byte for byte the same** recorded comparison — the served bytes are compared, not a summary of them;
- a **fresh interpreter** reconstructs the same comparison from the coordination root and the record
  alone, so "reopen after a process restart" is measured rather than simulated;
- a **later task** landing on the repository and on the leaf's protected branch changes neither the
  bytes nor the provenance of the recorded comparison, and its content never enters the inventory;
- a **pre-feature leaf** — source history, no intent generation ever recorded — exposes its recorded
  source range and states that absence explicitly, as a typed absence and not as missing content;
- a generation that recorded **no intent half at all** states that absence as its own fact on the pane
  and on both refusals, and never as a channel that does not resolve (this leaf's F1 fix);
- a **recorded range the repository cannot resolve** answers `candidate_unresolved` with the restore
  action rather than the intake defect's `candidate_not_live` (this leaf's F2 fix);
- expected content that no longer resolves is reported unavailable on the channel it affects, with the
  record's own deletion statement, and nothing falls back to the current tip or to today's knowledge;
- a closed leaf that recorded **neither** a comparison nor a landed commit is still refused by name,
  which is the one state in which `candidate_not_live` is the honest answer.

## Code Commentary

### Logic

**The fixture is the existing R01 enclosure fixture, extended rather than duplicated.**
`closed_fixture` calls `build_endpoint_fixture` (imported from
`test_knowledge_review_source_endpoints`), so the two real snapshots, the two real committed trees and
the real linked worktree every case drives are the ones the source-endpoint cases already own; a case
that needs a closed leaf removes the worktree group itself. `_freeze` publishes a real comparison
through `freeze_review_comparison` (R11's owner), `_composition` reads the owner's own payload through
`read_knowledge_review` with `review_records_for`, and `_serve` drives the production collaborators
through `register_review_routes` and `TestClient` — so the entry route, the subject route, the expansion
route and the refusals are measured over HTTP with the real status and the real body.

**The restart leg is a child interpreter, not a second client.** `_served_in_a_new_process` writes a
descriptor of the four configuration roots, the route and the params, then runs `_CHILD_SERVE` in a
child `sys.executable` with only `mcp/src` on `PYTHONPATH`; the child builds the app from the
coordination root alone, calls the production port and writes its status and bytes out for the parent to
compare. Nothing is shared with the parent beyond the coordination root, which is what makes "a fresh
process reconstructs the same comparison" a measurement rather than a claim about the same object graph.

**The later-task leg lands real history and then measures contamination rather than assuming it.**
`_land_a_later_task` writes a path the leaf never touched, commits it, and moves the leaf's
**protected source branch** to the new commit — the exact event that could contaminate a review reading
a branch tip. The case then compares the served bytes with the frozen read and asserts the later task's
path is absent from the inventory, the comparison binding is unchanged and the declared limitations are
stable. `_object_present` is the supporting measurement that a reclaimed object really is gone, so the
unavailable-channel case deletes objects through R11's own reclamation owner
(`release_comparison_code_object`) rather than by touching files behind it.

**The two fix-round cases assert the sentence, not only the token.** The typed-absence case freezes a
task with **no datasets at all** through R11's `freeze_review_comparison`, asserts the manifest records
`{before: not-selected, after: not-selected}`, and then asserts the wording on the task-context pane, on
the entry route and on the subject route — including that the "does not resolve now" sentence appears in
none of them. The unresolvable-range case records a real landed commit, deletes the work branch, expires
reflogs, removes the worktree group and runs `git gc --prune=now`, asserts the commit no longer resolves,
and then asserts the route answers 404 `candidate_unresolved` with the "cannot be read (unresolvable)"
detail and the restore action. A case that asserted only the machine-readable state would have passed
while the human-readable sentence still told the reader the wrong fact, which is exactly what the fix
round corrected.

### Conventions

`pytestmark = pytest.mark.evidence_unit` places the module in the ordinary unit lane, and
`mcp/tests/test-evidence-lanes.toml` registers it there (a bare TOML key, so it is named as a quoted
anchor rather than as an identifier). `mcp/tests/evidence-lifecycle.toml` derives its three
`consumer_scope = "exact"` consumer rows from the census's own finding — the two snapshot/tree fixtures
and the read-scope fixture the R01 enclosure is built over — and no artifact, no contract and no
artifact identity is added. Helper names are private and single-purpose, the child source is one module-level constant so
the child and the parent cannot drift, and no case constructs a record, a manifest or a resolution by
hand.

### Invariants And Boundaries

- **Only served bytes and owner-produced values are asserted.** No case builds the payload it then
  checks, and the byte comparisons read the response body.
- **The enclosure is one per case.** `closed_fixture` builds a fresh fixture under the case's own
  `tmp_path`, so no case observes another's worktree, record or removed worktree group.
- **History is landed, not simulated.** A later task is a real commit that really moves the protected
  source branch, and a reclaimed object is really gone before the unavailable-channel case asserts.
- **A fresh process is a fresh interpreter.** The restart leg shares no state with the parent, so the
  record-only resolution is measured rather than re-entered.
- **No case re-derives what an owner owns.** Freezing, retaining, reclaiming and reopening all go
  through R11's owners; the cases observe, they do not reimplement.
- **Browser acceptance is not claimed here.** The packet's real-browser boundary belongs to
  `ICR-R25@v1`, and the mounted-surface cases for this leaf live in the dashboard's own module.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and cases,
the R01 enclosure fixture it extends, the R11 owners it drives for freezing and reclaiming, and the two
registration files that admit it to a lane and derive its consumer rows. Three details a reader should
carry: the module is **evidence_unit** and its lane row is what the collection gate reads before the
module may run at all; the three consumer rows are `exact`-scoped, so a fourth fixture dependency would
have to be registered rather than inferred; and the later-task and reclaimed-object legs mutate real Git
state inside the case's own fixture repository, never the source checkout.

- **The module's own statement of the defect it measures, the six load-bearing properties, and that every case reads the production composition rather than a prebuilt payload.** [1]
- The route every case drives, and the lane the module belongs to. [2]
- **The child that reopens the same comparison in an interpreter sharing no state with the parent.** [3]
- **The R01 enclosure fixture this module extends, one fresh enclosure per case.** [4]
- **The production composition the cases read through: the real route, the real collaborators, the real record loader.** [5]
- **The two owners the fixture drives: freezing a real comparison and reading the owner's own payload.** [6]
- **The restart leg: a descriptor of the four roots alone, a child interpreter, and the served bytes written out for the parent to compare.** [7]
- **The later-task leg: a real commit on the repository, and the leaf's protected source branch really moved to it.** [8]
- **The byte-for-byte case: the live frozen read and the cleaned read served as bytes and compared.** [9]
- **The restart case: the same bytes from a fresh interpreter that knows only the coordination root.** [10]
- **The contamination case: bytes, binding and provenance unchanged after a later task lands, and the later path absent from the inventory.** [11]
- **The pre-feature case: the recorded source range exposed with the absence of an intent generation stated as a typed absence.** [12]
- **The F1 case: a generation that recorded no intent half states that absence as its own fact on the pane and on both refusals, and never as content that does not resolve.** [13]
- **The F2 case: a recorded range the repository cannot resolve is `candidate_unresolved`, not the intake defect's code.** [14]
- **The supporting measurement that a reclaimed object really is gone, so the unavailable-channel case deletes through R11's own reclamation owner rather than behind it.** [15]
- **The per-channel failure case: the affected channel unavailable with the record's own deletion statement, and nothing substituted.** [16]
- **The one state in which the intake defect's code is still the honest answer.** [17]
- **The declared history tokens the cases assert, read from the resolution module's own vocabulary.** [18]
- **The lane row that registers this module, and the three exact-scope consumer rows its cases are derived for.** [19]

### Cross-Repo References

No cross-repository behavior is exercised by this module. Its enclosure is one repository's own leaf
worktree with an external memory half, and every case reads that repository's own records.

No meaningful cross-repo references found.
