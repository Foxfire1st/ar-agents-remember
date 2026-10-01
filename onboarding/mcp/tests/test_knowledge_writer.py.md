# mcp/tests/test_knowledge_writer.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R12: the curator writer creates and updates every knowledge kind as validated files.** Registered
in the `unit-regression` lane; 20 collected cases, each over real Git repositories.

## Code Commentary

### Logic

- Conforming example: a decision, a realization with blob and content (blob equals `git rev-parse`, content
  the sha256 of the symbol's lines) and a proof from tested evidence, all validated.
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
  the same entry with a `proofs` item is written. The admission rules set no `writer_reports`, so the
  writer refuses as every commit route does.
- **A moved row relocates its entry** (leaf 260928-MIK-L06, ruling Q6):
  `test_a_moved_row_whose_after_names_another_path_relocates_the_entry` moves a file with `git mv`. An
  `extended` row whose cover names a `path` is refused ("only on a moved row"); a cover path `../outside.py`,
  `/abs/landing.py` or `""`, and a cover with both `remove` and `path`, are each refused as a named problem
  with the memory tree byte-identical (review F1 and N7). A `moved` row relocates `RLZ-BASE01` into
  `onboarding/pkg/moved/landing.py.json` with its role kept, its `blob` the moved file's blob at C and its
  content unchanged; the row's `before` and `after` name the old and new paths and validate as `moved`; a
  rerun is byte-identical.
- **MIK-R13 decision records** (leaf 260928-MIK-L13). `_requirement_packet` writes MIK-R04@v2 under the world's
  coordination root (`tasks/agents-remember/260928_family/…`); `_lifted_d12` lifts D12 as a `records` item with a
  `constrains` and a `reconsider_on` link (alternative 1) to the base invariant and two `motivated_change_to` links to
  MIK-R04, at v2 and v9.
  - `test_a_lifted_decision_round_trips_and_its_requirement_endpoints_are_reported`: `knowledge-ingest --commit`
    writes the decision with its `reconsider_when`; `requirementEndpoints` is `links.2` `resolved` and `links.3`
    `unresolved` (`task-intent-requirement-packet-version-mismatch`); no R13 violation; a rerun is `unchanged` and
    byte-identical.
  - `test_a_decision_that_breaks_a_content_rule_is_refused_and_nothing_is_written`: a deferred alternative without
    `reconsider_when` is refused by exactly `R13.1-reconsider-when` with the tree unchanged, and the endpoint is still
    reported `unresolved` (no coordination root on the direct API).
  - **The bootstrap dispatch test also proves the wave passes the root** (review F4, ruling 02:05:07): its hand-off is
    now an object with the entry and the lifted D12, the fake `admitted` carries `authority.coordination_root`, and it
    asserts `[("links.2", "resolved"), ("links.3", "unresolved")]`. The file writer's bare-list branch stays covered
    by `_write(world, [proven])`.
- **L37.** `test_knowledge_bootstrap_refuses_unconverted_memory_once_the_repository_holds_converted_memory`: the
  taskless database route is locked, naming the crossing sync (MIK-R09 rule 6).
  `test_a_master_line_crossing_records_its_rows_through_the_writer`: `knowledge-ingest --crossing` writes a
  `crossing` owner's rows into `<task-id>-crossing-<n>.json`; a non-series contract, another task's or an unopened
  crossing id, a closed file and database-only flags are refused. The leaf route passes `code_base ==
  contract.code_base_commit`, and the crossing route passes the series' code work branch (review R1 F10b).
  One earlier expectation changed with the reopen ruling: a write after a **committed** closed history file now
  writes attempt 2; a file closed only in the working tree is still refused as closed and frozen.

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

- The conforming example. [1]
- Every kind through the command line. [2]
- Unresolvable evidence reported and kept. [3]
- A bootstrap of converted memory writes as a wave. [4]
- A rerun that changes a locator removes this leaf's old entry only. [5]
- The bootstrap command dispatch. [6]
- MIK-R27: the writer refuses an unsupported admission claim and writes nothing, and writes once the proof is added. [7]
- Route rules: report in the writer, refusal at commit. [8]
- MIK-R06 (ruling Q6): a moved row relocates its entry; malformed paths and remove-plus-path are refused. [9]
- The requirement packet the owner resolves, and D12 lifted with governs, reconsider and requirement links. [10]
- A lifted decision round-trips; its endpoints are reported, resolved and unresolved. [11]
- A content-rule break refuses the write and writes nothing. [12]
- The bootstrap wave resolves a requirement endpoint through the admitted coordination root (review F4). [13]

- knowledge-bootstrap refuses unconverted memory once the repository holds converted memory. [14]
- A master line's crossing records its rows through the writer. [15]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.
