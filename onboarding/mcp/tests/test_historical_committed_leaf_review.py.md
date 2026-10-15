# mcp/tests/test_historical_committed_leaf_review.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Recorded tree comparisons survive cleanup, restart and later landings; historical JSON retains source without reopening canonical knowledge.

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
- a **recorded range the repository cannot resolve** answers `candidate_unresolved` with the restore
  action rather than the intake defect's `candidate_not_live` (this leaf's F2 fix);
- retained code and memory objects removed directly by the case produce `unavailable-history`,
  an unavailable source inventory and an unresolved knowledge statement; the named-subject route
  refuses as `candidate_dataset_absent`, and the later task's content is not substituted. This
  case supplies no record-owned deletion statement;
- a closed leaf that recorded **neither** a comparison nor a landed commit is still refused by name,
  which is the one state in which `candidate_not_live` is the honest answer.

## Code Commentary


### Logic

The real served route returns the same recorded comparison after worktree-group cleanup and in a fresh process, and excludes a later landing. [9] [10] [11]

Pre-feature source ranges remain readable with legacy-unavailable knowledge. Historical JSON that selected no intent half retains not-selected metadata while a case forbids all APSW opens. Missing recorded commits are candidate_unresolved; lost retained source/memory objects are unavailable-history without substitution. A cleaned leaf holding no comparison/range is candidate_not_live. [12] [13] [14] [16] [17]

### Invariants And Boundaries

- Historical identities never rebind to current branches or memory.
- Typed absence, retired legacy knowledge and lost objects are separate facts.

### Logic

**The restart leg is a child interpreter, not a second client.** `_served_in_a_new_process` writes a
descriptor of the four configuration roots, the route and the params, then runs `_CHILD_SERVE` in a
child `sys.executable` with only `mcp/src` on `PYTHONPATH`; the child builds the app from the
coordination root alone, calls the production port and writes its status and bytes out for the parent to
compare. Nothing is shared with the parent beyond the coordination root, which is what makes "a fresh
process reconstructs the same comparison" a measurement rather than a claim about the same object graph.

**The later-task leg lands real history and then measures contamination rather than assuming it.**
The case then compares the served bytes with the frozen read and asserts the later task's
path is absent from the inventory, the comparison binding is unchanged and the declared limitations are
stable.

A case that asserted only the machine-readable state would have passed
while the human-readable sentence still told the reader the wrong fact, which is exactly what the fix
round corrected.

### Conventions

`pytestmark = pytest.mark.evidence_unit` places the module in the ordinary unit lane, and
`mcp/tests/test-evidence-lanes.toml` registers it there (a bare TOML key, so it is named as a quoted
anchor rather than as an identifier). `mcp/tests/evidence-lifecycle.toml` currently lists six
`consumer_scope = "exact"` consumer rows for this module: anchor-fixture models, diff-scope support,
the Node fixture lockfile, row-codec support, row-writer support and read-scope support.
These are registered dependencies, not evidence of new runtime acceptance. Helper names are private and single-purpose, the child source is one module-level constant so
the child and the parent cannot drift,

### Invariants And Boundaries

- **Only served bytes and owner-produced values are asserted.** No case builds the payload it then
  checks, and the byte comparisons read the response body.
- **The enclosure is one per case.** `closed_fixture` builds a fresh fixture under the case's own
  `tmp_path`, so no case observes another's worktree, record or removed worktree group.

- **A fresh process is a fresh interpreter.** The restart leg shares no state with the parent, so the
  record-only resolution is measured rather than re-entered.

- **Browser acceptance is not claimed here.** The packet's real-browser boundary belongs to
  `ICR-R25@v1`, and the mounted-surface cases for this leaf live in the dashboard's own module.

### Todos

None recorded.

## Evidence


### Repo-Internal References


















- Current limitations are generated by the exact tree and historical owners. [18]




### Cross-Repo References

No cross-repository contract is established by this file.

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and cases,
the R01 enclosure fixture it extends, the R11 owners it drives for freezing and reclaiming, and the two
registration files that admit it to a lane and derive its consumer rows. Three details a reader should
carry: the module is **evidence_unit** and its lane row is what the collection gate reads before the
module may run at all; the six current consumer rows are `exact`-scoped, so any additional fixture dependency
must be registered rather than inferred; and the later-task and reclaimed-object legs mutate real Git
state inside the case's own fixture repository, never the source checkout.



- **The declared history tokens the cases assert, read from the resolution module's own vocabulary.** [35]

### Cross-Repo References

No cross-repository behavior is exercised by this module. Its enclosure is one repository's own leaf
worktree with an external memory half, and every case reads that repository's own records.

No meaningful cross-repo references found.

- Cleanup preserves exact recorded bytes. [9]
- Fresh-process reconstruction. [10]
- Later task isolation. [11]
- Pre-feature source and legacy-unavailable knowledge. [12]
- Typed historical absence opens no canonical database. [13]
- Lost recorded range refuses as unresolved. [14]
- Lost recorded objects remain unavailable. [16]
- Unrecorded cleaned leaf remains not live. [17]
- The exact-scope consumer row for this module in the shared diff-scope case support. [19]
- The current shared diff-scope support artifact declares this test module as an exact consumer. [20]
- The route every case drives, and the lane the module belongs to. [21]
- **The child that reopens the same comparison in an interpreter sharing no state with the parent.** [22]
- **The R01 enclosure fixture this module extends, one fresh enclosure per case.** [23]
- **The production composition the cases read through: the real route, the real collaborators, the real record loader.** [24]
- **The restart leg: a descriptor of the four roots alone, a child interpreter, and the served bytes written out for the parent to compare.** [25]
- **The byte-for-byte case: the live frozen read and the cleaned read served as bytes and compared.** [26]
- **The restart case: the same bytes from a fresh interpreter that knows only the coordination root.** [27]
- **The contamination case: bytes, binding and provenance unchanged after a later task lands, and the later path absent from the inventory.** [28]
- **The pre-feature case: the recorded source range exposed with the absence of an intent generation stated as a typed absence.** [29]
- **The F2 case: a recorded range the repository cannot resolve is `candidate_unresolved`, not the intake defect's code.** [30]

- Lost retained code and memory objects produce unavailable-history, unavailable source inventory and an unresolved knowledge statement. The named-subject request refuses as candidate_dataset_absent and later-task content is absent; this case supplies no record-owned deletion statement. [31]

- **The one state in which the intake defect's code is still the honest answer.** [32]
- The exact-scope consumer row for this module in the shared diff-scope case support.  Anchor: `test_historical_committed_leaf_review` [33]
- **The later-task leg: a real commit on the repository, and the leaf's protected source branch really moved to it.** [34]
