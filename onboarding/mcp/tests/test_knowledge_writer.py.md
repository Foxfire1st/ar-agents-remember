# mcp/tests/test_knowledge_writer.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R12: the curator writer creates and updates every knowledge kind as validated files.** Registered
in the `unit-regression` lane, using real Git repository fixtures. This card records current source assertions, not a Curator test execution or a fresh case-count grade.

## Code Commentary

### Logic

- Conforming example: a decision, a realization with blob and content (blob equals `git rev-parse`,
  content is the sha256 of the symbol's lines), and a proof from tested evidence. The source checks
  post-write validation against the explicit memory `HEAD` comparison base, not a baseless run.
- `knowledge-ingest --commit` round-trips every kind: all ten record kinds, a realization, a proof, a
  `moved` invariant row and a `no_impact` family row; a second run exits 0.
- Idempotence: a rerun is byte-identical with every action `unchanged`.
- Evidence naming no resolvable test is reported and kept; four problems refuse in one report; a colliding
  ID is refused by `R22.2-identity` with the tree unchanged.
- A meaning change increments the revision once against the base; evidence on another leaf's record goes to
  this leaf's row reason (`storedIn` names the row), and without the row the run is refused. The base
  record's kept origin now includes its `legacyId` (`legacy-invariant-landing-pair`), because the base
  records are genuine exports since MIK-R27 (leaf 260928-MIK-L27).
- `incidental` is written as `support`; a closed history file is frozen.
- Planning writes nothing; unconverted memory is not this route; the bootstrap writes as a wave, and the
  `knowledge-bootstrap` command dispatches converted memory to the file writer.
- A contradicted history row refuses until named again; an entry naming no record is refused; a rerun that
  changes a locator removes only this leaf's old entry; a blank authorization is refused.
- The MIK-R04 route rules are reports in the writer and refusals at `require_valid_commit`.
- **MIK-R27 inside the writer** (leaf 260928-MIK-L27): a new invariant claiming `guarded_by_test` with no
  proof is refused (`[R27.2-new-record]`, naming the criterion) and the memory tree is byte-identical;
  the same entry with a `proofs` item is written. This is the refusing `R27.2-new-record` rule, not
  a blanket admission-rule policy: `R27.2-existing-record` carries `writer_reports=True` and
  `merge_reports=True`, allowing authoring reports while ordinary commit/publication still refuses
  outside the named sync-merge exception.
- **A moved row relocates its entry** (leaf 260928-MIK-L06, ruling Q6):
  `test_a_moved_row_whose_after_names_another_path_relocates_the_entry` moves a file with `git mv` and
  prepares the destination Markdown before ingestion. A new sidecar without its card is new
  migration debt and refuses immediately, so relocation cannot rely on permanent report-only
  debt. The fixture preparation is not broader writer acceptance. An
  `extended` row that only relocates the existing entry is refused because it covers no added entry; the current parser no longer blanket-refuses its path solely for that disposition. A cover path `../outside.py`,
  `/abs/landing.py` or `""`, and a cover with both `remove` and `path`, are each refused as a named problem
  with the memory tree byte-identical (review F1 and N7). A `moved` row relocates `RLZ-BASE01` into
  `onboarding/pkg/moved/landing.py.json` with its role kept, its `blob` the moved file's blob at C and its
  content unchanged; the row's `before` and `after` name the old and new paths and validate as `moved`; a
  rerun is byte-identical.
- **MIK-R13 decision records** (leaf 260928-MIK-L13). `_requirement_packet` writes MIK-R04@v2 under the world's
  coordination root (`tasks/agents-remember/260928_family/…`); `_lifted_d12` lifts D12 as a `records` item with a
  `constrains` and a `reconsider_on` link (alternative 1) to the base invariant and two `motivated_change_to` links to
  MIK-R04, at v2 and v9.
  - `test_a_lifted_decision_round_trips_and_its_requirement_endpoints_are_reported` first asserts refusal and byte-identical memory for the v9 packet mismatch while still reporting resolved/unresolved endpoint observations. After `_repair_lifted_endpoint` supplies the actual v9 packet, ingestion succeeds and an exact rerun reports the record unchanged. The endpoint refusal is not an R13 validator violation.
  - `test_a_decision_that_breaks_a_content_rule_is_refused_and_nothing_is_written`: a deferred alternative without
    `reconsider_when` is refused by exactly `R13.1-reconsider-when` with the tree unchanged, and the endpoint is still
    reported `unresolved` (no coordination root on the direct API).
  - **The bootstrap dispatch case carries the coordination root.** It first asserts a refused wave with resolved/unresolved endpoint observations, repairs the lifted endpoint, then asserts successful wave publication with both links resolved. The bare-list writer fixture remains a distinct admission path; this is a static account of assertions, not a newly run bootstrap.

### Conventions

- Helpers `_write`, `_decision`, `_conforming` and `_every_kind` build requests and documents.

### Invariants And Boundaries

- The family-route test fails if the writer split is disabled (verified by the reviewer's mutation check).

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The cases.

- Every kind through the command line. [2]
- Unresolvable evidence reported and kept. [3]
- A bootstrap of converted memory writes as a wave. [4]
- A rerun that changes a locator removes this leaf's old entry only. [5]
- The bootstrap command dispatch. [6]
- MIK-R27: the writer refuses an unsupported admission claim and writes nothing, and writes once the proof is added. [7]
- Route rules: report in the writer, refusal at commit. [8]
- The requirement packet the owner resolves, and D12 lifted with governs, reconsider and requirement links. [10]


- The lifted decision first refuses the endpoint mismatch, then writes after repair and reruns unchanged [11]


- A content-rule break refuses the write and writes nothing. [12]


- The root-aware bootstrap wave refuses its unresolved new link, then writes with both endpoints resolved after repair [13]



- A master line's crossing records its rows through the writer. [15]

- A cover revises a realization entry's rationale in place. [16]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.

- knowledge-bootstrap refuses unconverted memory with or without converted memory elsewhere. [14]

- The conforming post-write example validates against the explicit memory HEAD comparison base. [1]


- Relocation preserves ID and assertions; extended-only relocation needs an added entry, and malformed/remove-plus-path covers refuse [9]


- Current source delta inspected statically: Explain HEAD comparison and destination Markdown; remove blanket admission writer-policy claim, retaining malformed-cover and idempotence assertions. [17]


## Current writer regression boundaries

The leaf fixtures supply the persisted worklist the current admission requires. Refused report assertions explicitly expose empty committed-action collections and honest nothing-written text. Relocation coverage still proves the moved path and stable entry fields, not permission to use this leaf's repaired writer for its own memory. Endpoint cases now distinguish refusal-time observations from post-repair publication. No tests were executed by this curation pass.

- The validator refusal reports no committed records, entries, rows or carries. [18]
