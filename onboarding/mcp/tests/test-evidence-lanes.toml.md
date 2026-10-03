# mcp/tests/test-evidence-lanes.toml

## 260928-MIK-L37 Two Lane Rows — The Reopen And Cutover Cases — **the current account**

`mcp/tests/test_knowledge_reopen.py` (the L37 reopen ruling: a reopened leaf's next attempt through the writer, the
gate, the validator's freeze, the index, the onboarding gate and record landing; attempt naming; closing the latest
attempt; 5 cases) and `mcp/tests/test_knowledge_cutover.py` (MIK-R37: the cutover lock at fourteen routes, the
converting candidate, the probe's fail-closed cases, the frozen database, no read of a converted tree's database,
and the hand-off evidence shape; 9 cases) are registered as two `unit-regression` rows at `:124` and `:125`,
directly after L09's `mcp/tests/test_knowledge_gate_routes.py` (`:123`) and before L11's
`mcp/tests/test_planned_knowledge_effects.py`, which is now at `:126`. Every later row of this file moves down by
two lines. On converted memory the references to those rows are sidecar anchors: a row that only moved is
re-recorded mechanically by the fixer, which is not a card change, so no citation was re-pointed by hand. The line
numbers in the earlier sections' prose are those of their own time. The lanes themselves are unchanged. The cutover
module imports no CLI or MCP surface (those cases sit in `test_knowledge_writer.py` and
`test_knowledge_index_surfaces.py`), so the evidence-lifecycle catalog and its pin were not touched (the
integration lane, including the dependency-ownership census, passes: 458 passed in review R2).

- The two L37 rows, after the gate-routes row and before the planned-effects row. [238]

## 260928-MIK-L33 One Lane Row — The Change-Kind Cases — **the current account**

`mcp/tests/test_review_change_kinds.py` (MIK-R33: every member occurrence's change kind from a store-authored four-tree
comparison, the shared member, returned members only, unreadable sidecars, family records and trees, definition 8 on
a changed non-text file, the moved entry, retired record and unresolved range, the unread sidecar beside an
established fact, the family's total, the derived facts and their validators, and the dataset review; 12 cases) is
registered as a `unit-regression` row at `:128`, directly after L32's `mcp/tests/test_review_unexplained_lane.py`
(`:127`) and before L25's `mcp/tests/test_review_artifact_cleanup.py`, which is now at `:129`. Every later row of this
file moves down by one line (L10's unexplained-change row is now at `:130`, L14's reconsideration row at `:131`), and
this leaf re-pointed the citations to those rows through the installed fixer or, for the rows it declined, by that
exact shift (each such row byte-identical to memory HEAD, its anchors checked in the base ranges and again in the
shifted ones). The line numbers in the earlier sections' prose are those of their own time. The lanes themselves are
unchanged, and the module imports no governed test-support module, so the evidence-lifecycle catalog and its pin were
not touched (the worker's round-1 integration lane passed, 447 passed, and the reviewer's R3 focused run of the lane,
gate and change-kind suites passed on the merged tree).

- The MIK-R33 row, after the unexplained-lane row and before the artifact-cleanup row. [1]

## 260928-MIK-L09 Two Lane Rows — The Mandatory Closeout Gate And Its Routes — **the current account**

`mcp/tests/test_knowledge_closeout_gate.py` (MIK-R09: the currentness rules and the packet's examples, the per-kind
dispatch, incomplete runs, the validator's history-row rule, each route's gate, the insertion-only symmetry, the
unconverted leaf, the prepared path, the memo and the approval state; 18 collected cases) and
`mcp/tests/test_knowledge_gate_routes.py` (the refusal at every public route entry and the review fixes: the leaf
publication rule, the closing and its receipts, net staleness, Git failures, the read set; 27 collected cases) are
registered as two `unit-regression` rows at `:122` and `:123`, directly after L30's
`mcp/tests/test_onboarding_trace_gate.py` (`:121`) and before L11's `mcp/tests/test_planned_knowledge_effects.py`,
which is now at `:124`. Every later row of this file moves down by two lines (L32's unexplained-lane row is now at
`:127`, L10's unexplained-change row at `:129`, L14's reconsideration row at `:130`), and this leaf re-pointed the
citations to those rows through the installed fixer or, for the rows it declined, by that exact shift (each such row
byte-identical to memory HEAD, its anchors checked in the base ranges and again in the shifted ones). The line
numbers in the earlier sections' prose are those of their own time. The lanes themselves are unchanged. The routes
module imports the gate module's fixture world, and neither imports a governed test-support module, so the
evidence-lifecycle catalog and its pin were not touched: the worker first tried a separate support module and a
catalog row, the dependency-ownership census refused them, and the fixture stayed module-local (the integration lane,
including the census, passes: 457 passed).

- The two MIK-R09 rows, after the onboarding-gate row and before the planned-effects row. [2]

## 260928-MIK-L32 One Lane Row — The Unexplained-Changes Lane Cases — **the current account**

`mcp/tests/test_review_unexplained_lane.py` (MIK-R32: file buckets, hunk classes at each side's recorded blob, the two
destinations and their reconciliation, the per-file response with links, revisions and membership states, the entry
count that reads no hunk, unread and partial knowledge sides, bounded reasons, unmeasured change sets, the route's
one-question rule and the typed refusal for long paths; 11 cases) is registered as a `unit-regression` row at
`:125`, directly after L25's `mcp/tests/test_review_git_trees.py` (`:124`) and before L25's
`mcp/tests/test_review_artifact_cleanup.py`, which is now at `:126`. Every later row of this file moves down by one
line (L10's unexplained-change row is now at `:127`, L14's reconsideration row at `:128`), and this leaf re-pointed
the citations to those rows through the installed fixer or, for the rows it declined, by that exact shift (each such
row byte-identical to memory HEAD, its anchors checked in the base ranges and again in the shifted ones). The line
numbers in the earlier sections' prose are those of their own time. The lanes themselves are unchanged, and the
module imports no test support module (only the sibling `test_review_git_trees.py`'s constants and `world` fixture),
so the evidence-lifecycle catalog and its pin were not touched (the worker's and reviewer's integration runs,
including the dependency-ownership test, passed without a re-pin).

- The MIK-R32 row, after the git-trees row and before the artifact-cleanup row. [3]

## 260928-MIK-L14 One Lane Row — The Reconsideration Cases — **the current account**

`mcp/tests/test_reconsideration_surfacing.py` (MIK-R14: the manifest lookup, the five triggers, one hop, the
`still_rejected` and `raise` rows with the task-document append, the reorder guard `R14.1`, route targets,
superseded decisions, and the link refresh with its reruns, carried state, new-change and stale-item refusals) is
registered as a `unit-regression` row at `:127`, directly after L10's `mcp/tests/test_unexplained_change_disposition.py`
(`:126` since L29's row at `:108`) and before `mcp/tests/test_knowledge_curator_ingest.py`, which is now at `:128`. Every
later row of this file moves down by one line, and this leaf re-pointed the citations to those rows by that exact shift (the rows the
installed fixer declined; each such row was byte-identical to memory HEAD, with its anchors checked in the base ranges
and again in the shifted ones). The line numbers in the earlier sections' prose are those of their own time. The
lanes themselves are unchanged; the leaf's one catalog consumer line and its Forty-second re-pin are recorded on
`evidence-lifecycle.toml.md` and `test_dependency_ownership_ast_helpers.py.md`.

- The MIK-R14 row, after the unexplained-change row (`:126`). [4]

## 260928-MIK-L29 One Lane Row — The Knowledge Reader Cases — **the current account**

`mcp/tests/test_knowledge_reader.py` (MIK-R29: the path-based knowledge reader's explorer, path view, bounded
directory and paged subtree, truth views, three-source timeline, census, selections, failures, route and
read-only behaviour; 21 cases) is registered as a `unit-regression` row at `:108`, directly after L23's
`mcp/tests/test_knowledge_index_surfaces.py` (`:107`) and before L02's `mcp/tests/test_knowledge_paging.py`,
which is now at `:109`. Every later row of this file moves down by one line (L05's route-chain row is now at
`:111`, L10's unexplained-change row at `:126`), and this leaf re-pointed the citations to those rows by that
exact shift where the installed fixer declined them (each such row byte-identical to memory HEAD, its anchors
checked in the base ranges and again in the shifted ones); rows inside committed Update History entries were left
as written. The line numbers in the earlier sections' prose are those of their own time. The lanes themselves are
unchanged, and the module imports no test support module, so the evidence-lifecycle catalog and its pin were not
touched (the dependency-ownership integration test passed without a re-pin).

- The MIK-R29 row, after the index-surfaces row (`:107`) and before the paging row. [5]

## 260928-MIK-L05 One Lane Row — The Route-Chain Cases — **the current account**

`mcp/tests/test_knowledge_route_chain.py` (MIK-R05: the chain over nested directories, compact entries after the
leaf content, `memberAtSeed`, `no_governing_family`, the conforming example, expansion from a family seed, the
budget and resumption, the family-seed resume rules, the v1-token refusal, and the `served_earlier` rendering)
is registered as a `unit-regression` row at `:110`, directly after L01's `mcp/tests/test_knowledge_leaf_read.py`
(`:109`) and before `mcp/tests/test_knowledge_writer.py`, which is now at `:111`. Every later row of this file
moves down by one line (L10's unexplained-change row is now at `:125`), and this leaf re-pointed the citations
to those rows by that exact shift (the rows the installed fixer declined; each such row was byte-identical to
memory HEAD, with its anchors checked in the base ranges and again in the shifted ones). The line numbers in
the earlier sections' prose are those of their own time. The lanes themselves are unchanged; the leaf's four
catalog consumer lines and its Forty-first re-pin are recorded on `evidence-lifecycle.toml.md` and
`test_dependency_ownership_ast_helpers.py.md`.

- The MIK-R05 row, after the leaf-read row (`:109`). [6]

## 260928-MIK-L10 One Lane Row — The Unexplained-Change Cases — **the current account**

`mcp/tests/test_unexplained_change_disposition.py` (MIK-R10: the two unexplained-change kinds, coverage by
realization entries or a migrated route, the `no_invariant` row, attach and author by linkage, delete-only
hunks, non-text changes, stable item IDs, the uncovered file's onboarding trace, and the writer's refusals) is
registered as a `unit-regression` row at `:124`, directly after L25's `mcp/tests/test_review_artifact_cleanup.py`
(`:123`) and before `mcp/tests/test_knowledge_curator_ingest.py`, which is now at `:125`. Every later row of this
file moves down by one line, and this leaf re-pointed the citations to those rows by that exact shift (the rows the
installed fixer declined; each such row was byte-identical to memory HEAD). The line numbers in the earlier
sections' prose are those of their own time. The lanes themselves are unchanged; the leaf's one catalog consumer
line and its Fortieth re-pin are recorded on `evidence-lifecycle.toml.md` and
`test_dependency_ownership_ast_helpers.py.md`.

- The MIK-R10 row, after the archive-hook row (`:123`). [7]

## 260928-MIK-L25 Two Lane Rows — The Reviewer On Git Trees And The Archive Hook — **the current account**

`mcp/tests/test_review_git_trees.py` (MIK-R25 rules 1–4 and 6: four trees and pins, idempotent re-reads, the tree
view, reopen and `unavailable-history`, the converted base, the legacy comparison, the no-`.sqlite` check, the
unconverted dataset review, directory-name pins) and `mcp/tests/test_review_artifact_cleanup.py` (rule 5: the
archive hook, split out by ruling 2026-09-30T02:32:42) are registered as `unit-regression` rows at `:122` and
`:123`, directly after L13's `mcp/tests/test_knowledge_decisions.py` (`:121`) and before
`mcp/tests/test_knowledge_curator_ingest.py`, which is now at `:124`. Every later row of this file moves down by two
lines, and this leaf re-pointed the citations to those rows by that exact shift (the rows the installed fixer
declined; each such row was byte-identical to memory HEAD). The line numbers in the earlier sections' prose are
those of their own time. The lanes themselves are unchanged; there is no catalog change or re-pin.

- The two MIK-R25 rows, after the decision-record row (`:121`). [8]

## 260928-MIK-L13 One Lane Row — The Decision-Record Cases — **the current account**

`mcp/tests/test_knowledge_decisions.py` (MIK-R13: the decision content rules in the validator, the derived
`superseded` status and `reconsider_on` subjects, requirement endpoints resolved by their owner and never refused,
and the review F6 case that a decision is never an export) is registered as a `unit-regression` row at `:121`,
directly after L11's `mcp/tests/test_planned_knowledge_effects.py` (`:120`) and before
`mcp/tests/test_knowledge_curator_ingest.py`, which is now at `:122`. Every later row of this file moves down by
one line, and this leaf re-pointed the citations to those rows by that exact shift (the rows the installed fixer
declined; each such row was byte-identical to memory HEAD, and the recheck found every anchor in its shifted
range). The line numbers in the earlier sections' prose are those of their own time. The lanes themselves are
unchanged; there is no catalog change or re-pin.

- The decision-record row, after the planned-effects row (`:120`). [9]

## 260928-MIK-L01 One Lane Row — The Leaf-Read Cases — **the current account**

`mcp/tests/test_knowledge_leaf_read.py` (MIK-R01: the family-complete leaf read's selection and order, one
selection on both surfaces, family names in the `invariant` view, the conforming example, the failure states,
and the obligations carried from L02) is registered as a `unit-regression` row at `:109`, directly after L02's
`mcp/tests/test_knowledge_paging.py` (`:108`) and before `mcp/tests/test_knowledge_writer.py`, which is now at
`:110`. L03's currentness row is now at `:115`, L30's onboarding-trace row at `:119` and L11's planned-effects
row at `:120`. Every later row of this file moves down by one line, and this leaf re-pointed the citations to
those rows by that exact shift. The line numbers in the earlier sections' prose are those of their own time.
The lanes themselves are unchanged.

- The leaf-read row, after the paging row (`:108`). [10]

## 260928-MIK-L06 One Lane Row — The Family Route Condition Cases — **the current account**

`mcp/tests/test_family_route_conditions.py` (MIK-R06: the four family route conditions as
`family_route_condition` worklist items, the carried dead route, the dead-at-B exemption, the rename-mapped
suggestion, and the family row that answers them) is registered as a `unit-regression` row at `:69`, in
alphabetical order after `mcp/tests/test_eve_protocol.py` (`:68`) and before
`mcp/tests/test_final_catalog_plan_attestation.py`, which is now at `:70`. Every later row of this file moves
down by one line, and this leaf re-pointed the citations to those rows by that exact shift (every re-pointed
row's anchors were checked to lie in the shifted ranges). The line numbers in the earlier sections' prose are
those of their own time. The lanes themselves are unchanged; there is no catalog change or re-pin.

- The family route condition row, after the Eve protocol row (`:68`). [11]

## 260928-MIK-L11 One Lane Row — The Planned-Effects Cases — **the current account**

`mcp/tests/test_planned_knowledge_effects.py` (MIK-R11: the `expectedKnowledgeEffects` field, matching and
the `planned`/`unplanned` marks, the planned row answering its item, the writer's planned rows and the task
owner's decision lookup, and the leaf route with the checklist, the tool rows and the fail-closed run) is
registered as a `unit-regression` row at `:118`, directly after L30's `mcp/tests/test_onboarding_trace_gate.py`
(`:117`) and before `mcp/tests/test_knowledge_curator_ingest.py`, which is now at `:119`. Every later row of
this file moves down by one line, and this leaf re-pointed the citations to those rows. The line numbers in
the earlier sections' prose are those of their own time. The lanes themselves are unchanged.

- The planned-effects row, after the onboarding-trace row (`:117`). [12]

## 260928-MIK-L02 One Lane Row — The Paging Cases — **the current account**

`mcp/tests/test_knowledge_paging.py` (MIK-R02: the cross-surface walk, threshold adherence over randomized
families, the oversized row, binding refusals, the projection over the artifact limit, the whole-block bound,
the ordering and code-tree bindings, and the empty ordering) is registered as a `unit-regression` row at
`:107`, directly after L23's `mcp/tests/test_knowledge_index_surfaces.py` (`:106`) and before
`mcp/tests/test_knowledge_writer.py`, which is now at `:108`. L03's currentness row is now at `:113` and L30's
onboarding-trace row at `:117`. Every later row of this file moves down by one line, and this leaf re-pointed
the citations to those rows. The line numbers in the earlier sections' prose are those of their own time.
The lanes themselves are unchanged.

- The paging-cases row, after the index-surfaces row (`:106`). [13]

## 260928-MIK-L30 One Lane Row — The Onboarding Trace Gate Cases — **the current account**

`mcp/tests/test_onboarding_trace_gate.py` (MIK-R30: the counted-change rule, the card and nearest-route
items, rows and unnecessary rows, moved markers, the fail-closed cases for mixed formats and unreadable
inputs, the converting leaf, the retired checks, the memory-quality count, the persisted worklist and the
unconverted leaf) is registered as a `unit-regression` row at `:116`, directly after L08's
`mcp/tests/test_knowledge_worklist_leaf.py` (`:115`) and before `mcp/tests/test_knowledge_curator_ingest.py`,
which is now at `:117`. Every later row of this file moves down by one line, and this leaf re-pointed the
citations to those rows. The line numbers in the earlier sections' prose are those of their own time. The
lanes themselves are unchanged.

- The onboarding-trace row, after the worklist-leaf row (`:115`). [14]

## 260928-MIK-L03 One Lane Row — The Currentness Cases — **the current account**

`mcp/tests/test_knowledge_currentness.py` (MIK-R03: each entry state, precedence, `unrealized`, stale proofs,
the per-side computation, the cache key, Git failures, and the `knowledge_read` and published-intent
surfaces) is registered as a `unit-regression` row at `:112`, directly after L24's
`mcp/tests/test_knowledge_anchor_content.py` (`:111`) and before L28's `mcp/tests/test_knowledge_proofs.py`,
which is now at `:113`; L08's two worklist rows are now at `:114` and `:115`. Every later row of this file
moves down by one line, and this leaf re-pointed the citations to those rows. The line numbers in the
earlier sections' prose are those of their own time. The lanes themselves are unchanged.

- The new row, after the anchor-content row (`:111`). [15]

## 260928-MIK-L08 Two Lane Rows — The Change-To-Knowledge Worklist Cases — **the current account**

`mcp/tests/test_knowledge_worklist.py` (MIK-R08 definitions 2 to 8 and rules 1 to 6 on real Git fixtures)
and `mcp/tests/test_knowledge_worklist_leaf.py` (the leaf route: pairing, sync, persistence, the tool, the
checklist, the writer's carry and the converted-base cache) are registered as `unit-regression` rows at
`:113` and `:114`, directly after L28's `mcp/tests/test_knowledge_proofs.py` (`:112`) and before
`mcp/tests/test_knowledge_curator_ingest.py`. Every later row of this file moves down by two lines, and this
leaf re-pointed the citations to those rows. The lanes themselves are unchanged.

- The two new rows, after the proof-cases row (`:112`). [16]

## 260928-MIK-L28 One Lane Row — The First-Class Test Proof Cases — **the current account**

`mcp/tests/test_knowledge_proofs.py` (MIK-R28 rules 2, 4, 5 and 6: both evidence forms and unresolvable
evidence in the writer, the facet the curator authors, the `proofs` of the `invariant` and `family` views,
the index's "without proof" list, the informational checklist section, and the migration pass) is
registered as a `unit-regression` row at `:112`. It sits directly after L24's anchor-content neighbour
`mcp/tests/test_knowledge_anchor_content.py` (`:111`) and before `mcp/tests/test_knowledge_curator_ingest.py`,
which is not alphabetical order; that is cosmetic, as for the earlier MIK leaves. Every later row of this
file moves down by one line, and this leaf re-pointed the citations to those rows. The lanes themselves are
unchanged (MIK-R28's preservation boundary).

- The new row, after the anchor-content row (`:111`). [17]

## 260928-MIK-L24 Three Lane Rows — The Conversion And Crossing Cases — **the current account**

`mcp/tests/test_knowledge_conversion.py` (MIK-R24 rules 1–4 and 6: the conversion over fixture cards and a
legacy database, determinism, the pinned version and its golden digest, the refusal that writes nothing,
and the back-to-prose render), `mcp/tests/test_knowledge_crossing.py` (rules 7 and 8: the converted base,
the item rules, reference-number collisions, the marker move, the master-line crossing history file and
the managed crossing sync on real Git repositories) and `mcp/tests/test_knowledge_conversion_toolchain.py`
(rules 5 and 9: `read_ar_files`, the reference check and fixer, memory quality on a converted tree, the
unconverted-line refusal and `memory_init`) are registered as `unit-regression` rows at `:108-110`. They sit
directly after L12's `mcp/tests/test_knowledge_writer.py` (`:107`) and before
`mcp/tests/test_knowledge_anchor_content.py`, which is not alphabetical order. That is cosmetic, as for
the earlier MIK leaves. The insertion **splits L12's two rows**: the writer row stays at `:107` and the
anchor-content row moves to `:111`. Every later row of this file moves down by three lines. Cards citing
later rows by line read three lines lower than on the base `cd3e943d`, and this leaf re-pointed those
citations.

- The three new rows, between the writer row (`:107`) and the anchor-content row (`:111`). [18]

## 260928-MIK-L12 Two Lane Rows — The Curator Writer Cases — **the current account**

`mcp/tests/test_knowledge_writer.py` (MIK-R12: every knowledge kind written as validated files through the
curator file writer and the `knowledge-ingest`/`knowledge-bootstrap` file route — the conforming example,
the command-line round trip of every kind, idempotence, unresolvable evidence, the validator refusal,
revisions against the base, history-row agreement, and the MIK-R04 route rules reported inside the writer)
and `mcp/tests/test_knowledge_anchor_content.py` (the one definition of an anchor's `content` bytes) are
registered as `unit-regression` rows directly after L23's `mcp/tests/test_knowledge_index_surfaces.py`, at
`:107-108` on L12's candidate, and before `mcp/tests/test_knowledge_curator_ingest.py`. (Since L24 the
writer row is at `:107` and the anchor-content row at `:111`, with L24's three rows between them.) The writer cases drive real
`tmp_path` Git repositories. The two-line insertion moves every later row of this file down by two lines:
cards citing later rows by line read two lines lower than on the base `6ad4e076`, and this leaf re-pointed
those citations.

- The two new rows, the index row they follow and the ingest row after them. [19]

## 260928-MIK-L20 Two Lane Rows — The Migration Census Cases — **the current account**

`mcp/tests/test_knowledge_census_files.py` (MIK-R20 rules 1–3 and 6: the `ar-census-*/v1` file formats, the
route slugs, the mechanical inventory and its Git reading, the census writer, and the nine census rules in
the validator's registry) and `mcp/tests/test_knowledge_census_report.py` (rules 4 and 5: the Doc12
measures with their counts, zero denominators, the cohort, the report on the fixture census, the governing
status across censuses and the `knowledge-census` command) are registered as `unit-regression` rows
directly after L22's `mcp/tests/test_knowledge_validator_routes.py`, at `:102-103`, and before L23's
`mcp/tests/test_knowledge_index.py`. Some cases drive real `tmp_path` Git repositories. The two-line
insertion moves every later row of this file down by two lines: L23's three index rows now sit at
`:104-106`. Cards citing later rows by line read two lines lower than on the base `aa07b1c9`, and this leaf
re-pointed those citations.

- The two new rows, the validator row they follow and the index row after them. [20]

## 260928-MIK-L04 One Lane Row — The Family Route Cases — **the current account**

`mcp/tests/test_knowledge_family_routes.py` (MIK-R04: the validator's family route rules, the reported
states, the root route `.`, the mechanical route suggestion and the `knowledge-routes` command) is
registered as a `unit-regression` row in alphabetical order, after
`mcp/tests/test_knowledge_citation_bindings.py` and before `mcp/tests/test_knowledge_file_canonical.py`,
at `:96`. The one-line insertion moves every later row of this file down by one line: L22's two validator
rows now sit at `:100-101` and L23's three index rows at `:102-104`. Cards citing later rows by line read
one line lower than on the base `ffd043f1`, and this leaf re-pointed those citations.

- The new row between its alphabetical neighbours. [21]

## 260928-MIK-L23 Three Lane Rows — The Derived Knowledge Index Cases — **the current account**

`mcp/tests/test_knowledge_index.py` (MIK-R23 rules 1–5: the two tree sources, the key, the answers, the
partial state, the cache and the `knowledge-index` command), `mcp/tests/test_knowledge_index_reuse.py`
(rule 6: the reused selection, views and comparison over the index, and the published-intent selection)
and `mcp/tests/test_knowledge_index_surfaces.py` (rule 6: the registered scope over the index, retired
records, and the mounted `knowledge_read`/`knowledge_diff`/`knowledge_project` tools) are registered as
`unit-regression` rows after L22's two validator rows, at `:101-103` when this leaf added them; since leaf
260928-MIK-L20 they follow L20's two census rows and sit at `:104-106`. The cases drive real
`tmp_path` Git repositories. The three-line insertion moves every later row of this file down by three
lines; cards citing later rows by line read three lines lower than on the base `ee5f14e5`, and this leaf
re-pointed those citations.

- The three rows and the census row they now follow. [22]

## 260928-MIK-L22 Two Lane Rows — The Knowledge Validator Cases — **the current account**

`mcp/tests/test_knowledge_validator.py` (MIK-R22's rules 1–9 over converted fixture trees) and
`mcp/tests/test_knowledge_validator_routes.py` (rule 8's integration points: the Git tree readers, the
commit-route adapter, the worktree gate, the managed sync after a merge and the `knowledge-validate` command)
are registered as `unit-regression` rows directly after `mcp/tests/test_knowledge_history_files.py`, at
`:99-100`. The route module drives real `tmp_path` Git repositories through `SyncFixture` (imported from
`test_worktree_sync.py`); the worker placed it in the unit lane because the integration lane is at its
400-case ceiling. The two-line insertion moves every later row of this file down by two lines; cards citing
later rows by line read two lines lower than on the base `4aa9a98c`, and this leaf re-pointed those
citations.

- The two new rows and the row they follow. [23]

## 260928-MIK-L07 One Lane Row — The History-File Cases — **the current account**

`mcp/tests/test_knowledge_history_files.py` (MIK-R07's per-leaf history-file cases) is registered as a
`unit-regression` row directly after `mcp/tests/test_knowledge_file_formats.py`, at `:98`. The module is
hermetic apart from one `tmp_path` git repository for the parallel-merge case, so the unit lane is the right
classification. The one-line insertion moves every later row of this file down by one line; cards citing
later rows by line read one line lower than on the base `45fe3774`, and this leaf re-pointed those
citations.

- The new row and the row it follows. [24]

## 260928-MIK-L21 Two Lane Rows — The Text Knowledge Format Cases — **the current account**

`mcp/tests/test_knowledge_file_canonical.py` and `mcp/tests/test_knowledge_file_formats.py` (MIK-R21's
formatter and format-model cases) are registered as `unit-regression` rows directly after
`mcp/tests/test_knowledge_citation_bindings.py` (since leaf 260928-MIK-L04, directly after
`mcp/tests/test_knowledge_family_routes.py`, which now sits between them). Both modules are hermetic — pure model validation, the
checked-in fixtures under `fixtures/knowledge_files/`, and a `tmp_path` tree for the command case — so the
unit lane is the right classification. The two-line insertion moves every later row of this file down by
two lines; cards citing later rows by line read two lines lower than on the base `b7ef73f8`, and this leaf
re-pointed those citations.

- The two rows, now after L04's family-routes row, which sits between them and `test_knowledge_citation_bindings.py`. [25]

## Family member-source locator cases — unit-regression row

`mcp/tests/test_review_family_member_sources.py` is registered as a `unit-regression` row inside the
review-family run, directly after `mcp/tests/test_review_family_context_values.py`. The lane is the
behaviour-preserving classification: the module is hermetic (a temporary store and a temporary Git
repository per module) and carries `evidence_unit`. The insertion moves every later row of this file down
by one line, so cards citing later rows by line read one line lower than on the base.

- The member-source locator cases' lane row. [26]
- The module's own lane marker. [27]

## Exact sibling retention regression lane

The unit-regression lane includes the public curator family-retention suite. It exercises exact stored sibling selection and publication/refusal boundaries through controlled ordinary leaf fixtures; it is not the real consumer’s publication proof.

- Register the public exact-sibling retention regression module. [28]

## 260921-ICR-L47 One Lane Row — The Changed-Intent Summary Cases

This leaf registers `mcp/tests/test_review_intent_summary.py` in `unit-regression`, inserted in sorted
position between `test_review_family_context_values.py` and `test_review_state.py`. The module is hermetic
(each case builds its own snapshots through the shipped writers), and it uses local constants rather than
the exact-consumer `read_scope_test_support` module. Without the row the lane gate refused to run the file
("test files without an explicit lane", worker event E2). Every row below the insertion moved down one line.

- The one new row in the unit-regression lane. [29]

## 260921-ICR-L7 One Lane Row — The Explicit-Revision-Comparison Cases — **the current account**

This leaf registers **one** module, `mcp/tests/test_knowledge_review_revision_selection.py`, as a
`unit-regression` row **inserted mid-list** in the knowledge run — at `:111`, immediately after
`mcp/tests/test_knowledge_review_one_sided_statements.py` at `:110` and above
`mcp/tests/test_knowledge_review_source_endpoints.py` at `:112`, so its row is
`mcp/tests/test-evidence-lanes.toml:113-113`.

The lane is the behaviour-preserving classification rather than a budget convenience: the module is
hermetic — every case builds its own snapshot pair through the public store operations under
`tmp_path` (plus two real Git trees for the pane case), drives the real comparison and the exact
head-selection function the adapter calls, and touches no live coordination tree, no network and no
service — and it carries `pytestmark = pytest.mark.evidence_unit` (`:66`). It is an ordinary unit
module with ten cases and no integration case, which is also why the `integration` lane is untouched
by this leaf.

No other manifest row, lane or digest changed. `mcp/tests/evidence-lifecycle.toml` is **not** modified by
this leaf, so `LIFECYCLE_CATALOG_SHA256` is **not** re-pinned: the module registers no contract and no
artifact and consumes no catalog-registered support module, which the census gate
(`test_dependency_ownership_ast_helpers.py`) confirms unchanged.

**Measured on this candidate, from the manifest and the modules on disk rather than by adding any earlier
account:**

| | measured on the working candidate |
| --- | --- |
| Declared lane entries | **327** |
| `mcp/tests/test_*.py` modules on disk | **327** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| File extent | **345 lines** |
| `unit-regression` | **215**, key `:5`, rows `6-220` |
| `public-contract` | **2**, key `:222`, rows `223-224` |
| `integration` | **76**, key `:226`, rows `227-302` |
| `architecture-fitness` | **20**, key `:304`, rows `305-324` |
| `provider-conformance` | **14**, key `:326`, rows `327-340` |
| `stress-durability` / `migration` | **0** / **0** (keys `:342` and `:344`) |

**The insertion moved every manifest entry below it, and that is this card's citation fact.** The row at
`:112` (L7's, listed at `:111` in the account above) sits above L16's
`mcp/tests/test_review_route_refusals.py` row (now `:120`), L3's
`mcp/tests/test_knowledge_review_source_content.py` row (now `:114`) and L1's
`mcp/tests/test_knowledge_review_source_endpoints.py` row (now `:113`). Ranges into this file are the
citation-reprojection owner's, and any row below an insertion that this card or an earlier account cites
has moved with it.

## 260921-ICR-L21 One Lane Row — The Final-Output-Receipt Cases — **the current account**

`260921-ICR-L21` (ICR-R21@v1) registers **one** module,
`mcp/tests/test_review_final_output_receipt.py`, as a `unit-regression` row: it sits at
`mcp/tests/test-evidence-lanes.toml:213`, between L12's `mcp/tests/test_review_assessments.py` row
(`:211`) and L8's `mcp/tests/test_knowledge_change_sets.py` row (`:213`). The module is hermetic — every
case builds its own enclosure, datasets and Git objects under `tmp_path` — and it drives the shipped
freeze, publication, closeout and integration owners, so `unit-regression` is the behaviour-preserving
classification rather than a budget convenience. The leaf also adds **three** `consumer_scope = "exact"`
rows to `mcp/tests/evidence-lifecycle.toml` and re-pins `LIFECYCLE_CATALOG_SHA256` in
`mcp/tests/test_dependency_ownership_ast_helpers.py` (population unchanged at 16 contracts / 66
artifacts).

**The counts this leaf changed, measured from the manifest rather than by adding to an earlier account:
declared entries 318 → 327** (the leaf's own row plus eight rows earlier leaves landed after L7's account
was written), **unit-regression 206 → 215**, **file extent 336 → 345 lines**. Every lane key at or below
the insertion moved with it — `public-contract` `:213` → `:222`, `integration` `:217` → `:226`,
`architecture-fitness` `:295` → `:304`, `provider-conformance` `:317` → `:326`, `stress-durability`
`:333` → `:342`, `migration` `:335` → `:344` — and the per-leaf tables below are **that leaf's own
as-of account**, kept as history rather than restated here; the live-state table above is the measured
one. **No claim's wording changed in this pass: the ranges were re-derived at their constructs' own
current lines.**

- **The new lane row: the explicit-revision-comparison cases, in the unit-regression lane, mid-list in the knowledge run.** [30]
- The lane key the row is a member of. [31]
- The row immediately above the insertion, and the row it displaced. [32]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [33]
- What the module measures: the real comparison over real snapshot pairs plus the adapter's own head-selection function. [34]
- The catalog digest this leaf does not move, and the census that confirms it. [35]

## 260921-ICR-L16 One Lane Row — The Review-Route Refusal Cases — **the current account**
## 260921-ICR-L13 One Lane Row — The Master-Net Generation Cases — **the current account**

This leaf registers **one** module, `mcp/tests/test_master_net_generation.py`, as a `unit-regression`
row **inserted mid-list** in the knowledge run — at `:114`, immediately after
`mcp/tests/test_knowledge_review_source_content.py` at `:113` and above
`mcp/tests/test_review_route_refusals.py` (now `:115`), so its row is
`mcp/tests/test-evidence-lanes.toml:114`.

The lane is the behaviour-preserving classification rather than a budget convenience: the module is
hermetic — `pytestmark = pytest.mark.evidence_unit`, real series/leaf contracts on disk, real code
and memory repositories with real branches, the real `master_changeset` / `master_file_diff`
resolution plus the HTTP routes that serve them. It touches no live coordination tree, no network
and no service, so it is an ordinary unit module: no budget moved for its nine cases, and the
`integration` lane does not describe it.

No other manifest row, lane or digest changed. `mcp/tests/evidence-lifecycle.toml` is **not** modified by
this leaf, so `LIFECYCLE_CATALOG_SHA256` is **not** re-pinned: the module registers no contract and no
artifact and consumes no catalog-registered support module.

**Measured on this candidate, from the manifest and the modules on disk:**

| | measured on the working candidate | at the base `6695a2a1` |
| --- | --- | --- |
| Declared lane entries | **319** | 317 |
| `mcp/tests/test_*.py` modules on disk | **319** | 317 |
| Declared-but-absent / present-but-undeclared | **0 / 0** | 0 / 0 |
| File extent | **337 lines** | 335 lines |
| `unit-regression` | **207**, key `:5`, rows `6-212` | 205, key `:5`, rows `6-210` |
| `public-contract` | **2**, key `:214` | 2, key `:212` |
| `integration` | **76**, key `:218` | 76, key `:216` |
| `architecture-fitness` | **20**, key `:296` | 20, key `:294` |
| `provider-conformance` | **14**, key `:318` | 14, key `:316` |
| `stress-durability` / `migration` | **0** / **0** (keys `:334` and `:336`) | 0 / 0 (keys `:332`, `:334`) |

**The insertion moved every manifest entry below it, and that is this card's citation fact.** The row at
`:114` is the fifth mid-list insertion this master has made into `unit-regression` (after L14's `:108`,
L3's `:111`, L16's `:113` — now `:115` — and L7's `:111` revision-selection row above it), so every lane
key and every row at or below it reads one line lower than the merged L7 account above records it:
`public-contract` `:213` → `:214`, `integration` `:217` → `:218`, `architecture-fitness` `:295` → `:296`,
`provider-conformance` `:317` → `:318`, `stress-durability` `:333` → `:334`, `migration`
`:335` → `:336`. Ranges into this file are the citation-reprojection owner's, and any row below
`:114` that this card or an earlier account cites has moved with it.

## 260921-ICR-L16 One Lane Row — The Review-Route Refusal Cases — **the previous account**

(260921-ICR-L13 note, re-derived at the sync: L13's row now reads `:114` and L16's `:115`, with keys at
`:214`/`:218`/`:296`/`:318`/`:334`/`:336`; the positions below are L16's as-of account, retained unchanged.)

This leaf registers **one** module, `mcp/tests/test_review_route_refusals.py`, as a `unit-regression`
row **inserted mid-list** in the knowledge run — at `:113`, immediately after
`mcp/tests/test_knowledge_review_source_content.py` at `:112` and above
`mcp/tests/test_knowledge_requirement_reference_contract.py` at `:114`, so its row is
`mcp/tests/test-evidence-lanes.toml:115-115`.

The lane is the behaviour-preserving classification rather than a budget convenience: the module is
hermetic — `pytestmark = pytest.mark.evidence_unit`, a bare `FastAPI()` app with the real
`register_review_routes` registered on it, injected ports, and an `McpRuntimeConfig` that names no real
root because these routes resolve nothing from it (`/nonexistent-workspace`,
`/nonexistent-coordination`, …). It touches no live coordination tree, no network, no service and no
temporary repository, so it is an ordinary unit module: no budget moved for its six cases, and the
`integration` lane does not describe it.

No other manifest row, lane or digest changed. `mcp/tests/evidence-lifecycle.toml` is **not** modified by
this leaf, so `LIFECYCLE_CATALOG_SHA256` is **not** re-pinned: the module registers no contract and no
artifact and consumes no catalog-registered support module, which the census gate
(`test_dependency_ownership_ast_helpers.py`) confirms unchanged.

**Measured on this candidate, from the manifest and the modules on disk rather than by adding any earlier
account:**

| | measured on the working candidate | at the base `8ff80ce0` |
| --- | --- | --- |
| Declared lane entries | **317** | 316 |
| `mcp/tests/test_*.py` modules on disk | **317** | 316 |
| Declared-but-absent / present-but-undeclared | **0 / 0** | 0 / 0 |
| File extent | **335 lines** | 334 lines |
| `unit-regression` | **205**, key `:5`, rows `6-210` | 204, key `:5` |
| `public-contract` | **2**, key `:212` | 2, key `:211` |
| `integration` | **76**, key `:216` | 76, key `:215` |
| `architecture-fitness` | **20**, key `:294` | 20, key `:293` |
| `provider-conformance` | **14**, key `:316` | 14, key `:315` |
| `stress-durability` / `migration` | **0** / **0** (keys `:332` and `:334`) | 0 / 0 (keys `:331`, `:333`) |

**The insertion moved every manifest entry below it, and that is this card's citation fact.** The row at
`:113` is the third mid-list insertion this master has made into `unit-regression` (after L14's `:108` and
L3's `:111`), so every lane key and every row at or below it reads one line lower than the *L14* account
above records it: `public-contract` `:211` → `:212`, `integration` `:215` → `:216`,
`architecture-fitness` `:293` → `:294`, `provider-conformance` `:315` → `:316`,
`stress-durability` `:331` → `:332`, `migration` `:333` → `:334`. Ranges into this file are the
citation-reprojection owner's, and any row below `:113` that this card or an earlier account cites has
moved with it.

## 260921-ICR-L14 Lane Row — The Production-Composition Record-Channel Cases — **the previous account**

This leaf registers **one** module, `mcp/tests/test_knowledge_review_evidence_channels.py`, as a
`unit-regression` row **inserted mid-list** in the knowledge run — at `:108`, immediately after
`mcp/tests/test_knowledge_review_comparison_generation.py` and before
`mcp/tests/test_knowledge_review_surface.py`, which is where the module's own name sorts. The
classification is the module's own rather than a budget convenience: `pytestmark = pytest.mark.evidence_unit`
declares the evidence lane, and every case runs in-process over a temporary enclosure — a real
SQLite dataset, a real memory repo and linked worktree, a real curator authority — with no DAG, no
network and no retained service.

**Measured lane populations after this insertion** (`mcp/tests/test-evidence-lanes.toml` on the
resolved candidate): `unit-regression` **203** rows, key `:5`, rows `6-208`; `public-contract` **2**
(key `:210`), `integration` **76** (key `:214`), `architecture-fitness` **20** (key `:292`),
`provider-conformance` **14** (key `:314`), and `stress-durability` / `migration` still declared with
no rows. **No other lane moved**, and the file pins no digest: the guard against an unregistered
module is collection-time, so the row is what makes these cases run at all.

**Why the module needs no artifact of its own.** It builds on `mcp/tests/test_knowledge_review_source_endpoints.py`'s
endpoint fixture and `mcp/tests/curator_coherence_test_support.py`'s publication helper rather than
introducing a third fixture, which is also why the evidence catalog's delta for this leaf is four
consumer rows and no registered artifact (`mcp/tests/evidence-lifecycle.toml`).

## 260921-ICR-L11 Lane Row — The Durable-Comparison-Generation Cases — **the previous account**

## 260918-TSIP-L2 Row — The Record-Integrity Module

This leaf adds **one row** to the same `architecture-fitness` lane, at `:246`, as that array's last
entry — between `mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py` (`:245`) and the lane's
closing bracket (`:247`):

```toml
  "mcp/tests/test_record_integrity.py",
```

`architecture-fitness` is the behaviour-preserving lane for it because the module imports the
verification package (`agents_remember_test_support.code_quality.record_integrity`) and executes
nothing over a real boundary: no process, no Node, no temporary repository. The manifest now carries
**249 module rows**, and the file is **267 lines** at that candidate — **both superseded by
`260918-TSIP-L4`, which added two further rows and re-read the shipped loader at 251 rows / 251
modules over a 269-line file** (`:165` the chain-order module in `integration`, `:244` the
response-conformance module in `architecture-fitness`) — **and superseded again by
`260918-TSIP-L5`, which added one further row at `:153` and re-read the file at 252 rows / 252
modules over 270 lines** (see its own section below).

**The insertion moved every manifest entry below it, and no other position was available.** An
`architecture-fitness` entry must sit between its own header (`:227`) and the next lane header
(`provider-conformance`, `:248`), and the array read **18** entries at `228-245` before this leaf, so
`:246` — the array's last row — is the minimum-displacement position. The one-line shift invalidated
three citations, and the shift is therefore a memory repair rather than an edit that could be
avoided:

| Affected citation | Before | After | Disposition |
| --- | --- | --- | --- |
| this card's row **"Empty former stress/migration populations"** | `:262-265` | **`:263-266`** | **BROKEN**: `migration = [` moved `265` → `266` and fell out of the range; repaired |
| this card's row **"The manifest still has no default classification for an unregistered test file"** | `:4-265` | **`:4-266`** | stale end — its anchor still resolved, so **no check reported it**; repaired by reading the file |
| `onboarding/mcp/tests/test_codex_capsule_delivery.py.md`, its `provider-conformance` lane-row citation | `:254-254` | **`:255-255`** | **BROKEN**: that row's own path moved `:254` → `:255`; repaired |
| this card's row **"Provider contract classifications"** | `:242-256` | unchanged | **INTACT**: the range still covers `provider-conformance` at `:248` |

**Not every range that moved broke**, which is why those dispositions are a list rather than a rule:
a range still containing its anchor is not a finding, and only the product's own `range_resolution`
check separates the two. It reported exactly **two** of them at this candidate — this card's
`:262-265` and the `test_codex_capsule_delivery.py.md` row. The stale `:4-265` end was found by
reading the file instead, which is `T45`'s class exactly: a range that no longer reaches the line it
described renders like a correct one.

**And the loader is not silent at this candidate — a correction to the section below.** The row above
registers this leaf's module as the fail-closed loader requires, and the manifest is still **one row
short of the modules it must classify**: `load_lane_manifest(<repository root>)` on this candidate
refuses with

```
test evidence lanes have 1 finding(s):
  - test files without an explicit lane: ['mcp/tests/test_atomic_series_chain_pair_order.py']
```

That module was added by `260915-CAPS-L25` at `f0313143` and was never registered; the gap is **one
row at every commit since**, measured `247 entries / 248 modules on disk` at `f0313143`, `248 / 249`
at `d9becade`, and `249 / 250` here. So this is not this leaf's doing and not this leaf's to repair —
registering that module is a change to this file and belongs to the lane registry's owner — but two
claims in the section below are wrong because of it and are corrected here rather than repeated:
`pytest tests/test_evidence_lanes.py tests/test_suite_budget.py -q` does **not** exercise
`load_lane_manifest` (its one registry case validates the lane *categories*), so its green says
nothing about the loader; and the loader was already refusing at the previous leaf's candidate, not
silent.

After this insertion the lane populations are: unit-regression **150** (`6-155`), public-contract
**2** (`158-159`), integration **64** (`162-225`), architecture-fitness **19** (`228-246`),
provider-conformance **14** (`249-262`), with `stress-durability` (`:264`) and `migration` (`:266`)
still empty — every lane above the insertion is unchanged.

## 260918-TSIP-L1 Row — The Instrument-Discipline Module

This leaf adds **one row** to the existing `architecture-fitness` lane, at `:232`, between
`mcp/tests/test_file_size_detector.py` (`:231`) and `mcp/tests/test_layering.py` (`:233`):

```toml
  "mcp/tests/test_instrument_discipline.py",
```

`architecture-fitness` is the behaviour-preserving lane for it because the module imports the
verification package (`agents_remember_test_support.code_quality.instrument_discipline`) and executes
nothing over a real boundary: no process, no Node, no temporary repository. `unit-regression` and
`integration` would both misdescribe it. **Corrected by the `260918-TSIP-L2` curator, and wrong when
written:** the claim that the fail-closed loader is silent at this candidate rested on
`pytest tests/test_evidence_lanes.py tests/test_suite_budget.py -q` → **4 passed in 0.54 s**, a run
that never calls `load_lane_manifest` (its one registry case validates the lane *categories*). Called
directly, the loader already refused at this candidate — `test files without an explicit lane:
['mcp/tests/test_atomic_series_chain_pair_order.py']`, an unregistered module from `260915-CAPS-L25`
that no seat on this master has registered. The module does collect into the lane, which is what the
row above establishes; the loader's silence was never measured. See the section above.

**The insertion is a one-line change that moved the 27 manifest entries below it, and that is the
fact to carry forward.** Every entry at or below `:232` gained one line; the entries above it did
not. Measured against the base commit, the two rows whose citations this invalidated are:

| Module | Before | After |
| --- | ---: | ---: |
| `mcp/tests/test_pause_is_not_publication.py` | 235 | **236** |
| `mcp/tests/test_codex_capsule_delivery.py` | 253 | **254** |

The pause suite's own row, `mcp/tests/test_pause_stop_only_end_to_end.py` at `:199`, is **above** the
insertion point and did not move — which is worth stating because the L37 lane-registration row in
`mcp/tests/overview.md` pairs that unmoved `:199` with the moved `:236`, and a reader who assumed
both had shifted would mis-cite one of them.

Four memory documents cited the pre-insertion numbers for those rows, and all four were repaired in
the same pass. Three were pure moves and the shipped citation fixer projected them mechanically
(`ccr-r10@v1`): this card's own `:235` → `:236` at line 762, `test_pause_is_not_publication.py.md`'s
`:235` → `:236`, and `test_codex_capsule_delivery.py.md`'s `:253` → `:254`. The fourth — the L37
lane-registration row in `mcp/tests/overview.md` — was **declined** by the fixer
(`projection_no_resolved_extent`: one anchor resolved to four extents) and was corrected by hand to
cite the two ranges that actually hold its two named anchors. This is the same hazard the L11 curator
recorded on this card after the six `D9` rows were added: **a row insertion renumbers every row below
it, and a cited line number is only true against one revision of this file.**

**Population.** No row was removed and no lane key moved; the module count rose by exactly one. This
card's earlier population paragraphs remain the as-of records of the leaves that wrote them and are
not restated here as current.

## 260918-TSIP-L2 Row — The Record-Integrity Module

This leaf adds **one row** to the same `architecture-fitness` lane, at `:246`, as that array's last
entry — between `mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py` (`:245`) and the lane's
closing bracket (`:247`):

```toml
  "mcp/tests/test_record_integrity.py",
```

`architecture-fitness` is the behaviour-preserving lane for it because the module imports the
verification package (`agents_remember_test_support.code_quality.record_integrity`) and executes
nothing over a real boundary: no process, no Node, no temporary repository. The manifest now carries
**249 module rows**, and the file is **267 lines** at that candidate — **both superseded by
`260918-TSIP-L4`, which added two further rows and re-read the shipped loader at 251 rows / 251
modules over a 269-line file** (`:165` the chain-order module in `integration`, `:244` the
response-conformance module in `architecture-fitness`) — **and superseded again by
`260918-TSIP-L5`, which added one further row at `:153` and re-read the file at 252 rows / 252
modules over 270 lines** (see its own section below).

**The insertion moved every manifest entry below it, and no other position was available.** An
`architecture-fitness` entry must sit between its own header (`:227`) and the next lane header
(`provider-conformance`, `:248`), and the array read **18** entries at `228-245` before this leaf, so
`:246` — the array's last row — is the minimum-displacement position. The one-line shift invalidated
three citations, and the shift is therefore a memory repair rather than an edit that could be
avoided:

| Affected citation | Before | After | Disposition |
| --- | --- | --- | --- |
| this card's row **"Empty former stress/migration populations"** | `:262-265` | **`:263-266`** | **BROKEN**: `migration = [` moved `265` → `266` and fell out of the range; repaired |
| this card's row **"The manifest still has no default classification for an unregistered test file"** | `:4-265` | **`:4-266`** | stale end — its anchor still resolved, so **no check reported it**; repaired by reading the file |
| `onboarding/mcp/tests/test_codex_capsule_delivery.py.md`, its `provider-conformance` lane-row citation | `:254-254` | **`:255-255`** | **BROKEN**: that row's own path moved `:254` → `:255`; repaired |
| this card's row **"Provider contract classifications"** | `:242-256` | unchanged | **INTACT**: the range still covers `provider-conformance` at `:248` |

**Not every range that moved broke**, which is why those dispositions are a list rather than a rule:
a range still containing its anchor is not a finding, and only the product's own `range_resolution`
check separates the two. It reported exactly **two** of them at this candidate — this card's
`:262-265` and the `test_codex_capsule_delivery.py.md` row. The stale `:4-265` end was found by
reading the file instead, which is `T45`'s class exactly: a range that no longer reaches the line it
described renders like a correct one.

**And the loader is not silent at this candidate — a correction to the section below.** The row above
registers this leaf's module as the fail-closed loader requires, and the manifest is still **one row
short of the modules it must classify**: `load_lane_manifest(<repository root>)` on this candidate
refuses with

```
test evidence lanes have 1 finding(s):
  - test files without an explicit lane: ['mcp/tests/test_atomic_series_chain_pair_order.py']
```

That module was added by `260915-CAPS-L25` at `f0313143` and was never registered; the gap is **one
row at every commit since**, measured `247 entries / 248 modules on disk` at `f0313143`, `248 / 249`
at `d9becade`, and `249 / 250` here. So this is not this leaf's doing and not this leaf's to repair —
registering that module is a change to this file and belongs to the lane registry's owner — but two
claims in the section below are wrong because of it and are corrected here rather than repeated:
`pytest tests/test_evidence_lanes.py tests/test_suite_budget.py -q` does **not** exercise
`load_lane_manifest` (its one registry case validates the lane *categories*), so its green says
nothing about the loader; and the loader was already refusing at the previous leaf's candidate, not
silent.

After this insertion the lane populations are: unit-regression **150** (`6-155`), public-contract
**2** (`158-159`), integration **64** (`162-225`), architecture-fitness **19** (`228-246`),
provider-conformance **14** (`249-262`), with `stress-durability` (`:264`) and `migration` (`:266`)
still empty — every lane above the insertion is unchanged.

## 260918-TSIP-L1 Row — The Instrument-Discipline Module

This leaf adds **one row** to the existing `architecture-fitness` lane, at `:232`, between
`mcp/tests/test_file_size_detector.py` (`:231`) and `mcp/tests/test_layering.py` (`:233`):

```toml
  "mcp/tests/test_instrument_discipline.py",
```

`architecture-fitness` is the behaviour-preserving lane for it because the module imports the
verification package (`agents_remember_test_support.code_quality.instrument_discipline`) and executes
nothing over a real boundary: no process, no Node, no temporary repository. `unit-regression` and
`integration` would both misdescribe it. **Corrected by the `260918-TSIP-L2` curator, and wrong when
written:** the claim that the fail-closed loader is silent at this candidate rested on
`pytest tests/test_evidence_lanes.py tests/test_suite_budget.py -q` → **4 passed in 0.54 s**, a run
that never calls `load_lane_manifest` (its one registry case validates the lane *categories*). Called
directly, the loader already refused at this candidate — `test files without an explicit lane:
['mcp/tests/test_atomic_series_chain_pair_order.py']`, an unregistered module from `260915-CAPS-L25`
that no seat on this master has registered. The module does collect into the lane, which is what the
row above establishes; the loader's silence was never measured. See the section above.

**The insertion is a one-line change that moved the 27 manifest entries below it, and that is the
fact to carry forward.** Every entry at or below `:232` gained one line; the entries above it did
not. Measured against the base commit, the two rows whose citations this invalidated are:

| Module | Before | After |
| --- | ---: | ---: |
| `mcp/tests/test_pause_is_not_publication.py` | 235 | **236** |
| `mcp/tests/test_codex_capsule_delivery.py` | 253 | **254** |

The pause suite's own row, `mcp/tests/test_pause_stop_only_end_to_end.py` at `:199`, is **above** the
insertion point and did not move — which is worth stating because the L37 lane-registration row in
`mcp/tests/overview.md` pairs that unmoved `:199` with the moved `:236`, and a reader who assumed
both had shifted would mis-cite one of them.

Four memory documents cited the pre-insertion numbers for those rows, and all four were repaired in
the same pass. Three were pure moves and the shipped citation fixer projected them mechanically
(`ccr-r10@v1`): this card's own `:235` → `:236` at line 762, `test_pause_is_not_publication.py.md`'s
`:235` → `:236`, and `test_codex_capsule_delivery.py.md`'s `:253` → `:254`. The fourth — the L37
lane-registration row in `mcp/tests/overview.md` — was **declined** by the fixer
(`projection_no_resolved_extent`: one anchor resolved to four extents) and was corrected by hand to
cite the two ranges that actually hold its two named anchors. This is the same hazard the L11 curator
recorded on this card after the six `D9` rows were added: **a row insertion renumbers every row below
it, and a cited line number is only true against one revision of this file.**

**Population.** No row was removed and no lane key moved; the module count rose by exactly one. This
card's earlier population paragraphs remain the as-of records of the leaves that wrote them and are
not restated here as current.

## 260921-ICR-L3 One Lane Row — The Source-Content Case Module — **the current account**

This leaf registers **one** module, `mcp/tests/test_knowledge_review_source_content.py`, as a
`unit-regression` row **inserted mid-list** in the alphabetical knowledge run — immediately after
`mcp/tests/test_knowledge_review_source_endpoints.py` at `:110` and above
`mcp/tests/test_knowledge_requirement_reference_contract.py` at `:112`, so its row is
`mcp/tests/test-evidence-lanes.toml:113-113`.

The lane is the behaviour-preserving classification rather than a budget convenience: the module is
hermetic — every case builds its own enclosure and linked worktree under `tmp_path`, drives the real
application owners over an in-process `TestClient`, and reads its evidence through one `git show`
subprocess with a pinned environment — it touches no live coordination tree, no network and no service,
and it carries `pytestmark = pytest.mark.evidence_unit` (`:62`). It is an ordinary unit module, which is
also why the twenty cases could be added without touching any budget: the module owns no data plane and
starts no server.

**Measured on this candidate, from the manifest and the modules on disk rather than by adding any earlier
account:**

| | measured on the working candidate |
| --- | --- |
| Declared lane entries | **315** |
| `mcp/tests/test_*.py` modules on disk | **315** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| File extent | **333 lines** |
| `unit-regression` | **203**, key `:5`, rows `6-208` |
| `public-contract` | **2**, key `:210`, rows `211-212` |
| `integration` | **76**, key `:214`, rows `215-290` |
| `architecture-fitness` | **20**, key `:292`, rows `293-312` |
| `provider-conformance` | **14**, key `:314`, rows `315-328` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:330` and `:332`) |

**The insertion moved every manifest entry below it, and that is this card's citation fact.** The new row
sits at `:111`, so every lane row at or below it reads one line lower than the last account in this card
recorded: the lane headers below the insertion are now `public-contract = [` `:210` (was `:209`),
`integration = [` `:214` (was `:213`), `architecture-fitness = [` `:292` (was `:291`),
`stress-durability = [` `:330` (was `:329`) and `migration = [` `:332` (was `:331`), and the rows those
sections named moved with them (`mcp/tests/test_knowledge_revision_seals.py` `:115` → `:116`,
`mcp/tests/test_knowledge_snapshot_publication.py` `:117` → `:118`, `mcp/tests/test_memory_backfill.py`
`:124` → `:125`, `mcp/tests/test_knowledge_portable_roundtrip.py` `:217` → `:218`,
`mcp/tests/test_lifecycle_playthrough_end_to_end.py` `:253` → `:254`,
`mcp/tests/test_pause_stop_only_end_to_end.py` `:259` → `:260` and
`mcp/tests/test_pause_is_not_publication.py` `:300` → `:301`). Every range this card carries into this
manifest was re-derived from the post-edit bytes rather than shifted by a remembered delta, and the new
row is the only content this leaf added to the file.

- **The new lane row: the source-content cases, in the unit-regression lane, mid-list in the knowledge run.** [36]
- The lane key the row is a member of. [37]
- The row immediately above the insertion, and the row it displaced. [38]
- **The lane headers below the insertion, each one line lower than the previous account recorded.** [39]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [40]
- What the module measures, and why it needs a real repository rather than a stub: the real routes over the real owners, and the independent Git observation every text is asserted against. [41]
- The two catalog consumer rows the same module joined, and the counts they do not move. [42]

## 260921-ICR-L11 Lane Row — The Durable-Comparison-Generation Cases — **the current account**
## 260921-ICR-L11 Lane Row — The Durable-Comparison-Generation Cases — **the previous account, superseded on the row and the populations above**

This leaf registers **one** module, `mcp/tests/test_knowledge_review_comparison_generation.py`, as a
`unit-regression` row **inserted mid-list** in the alphabetical knowledge run — after
`mcp/tests/test_knowledge_read_scope.py` at `:105` and above `mcp/tests/test_knowledge_review_surface.py`
at `:107`, so its row is `mcp/tests/test-evidence-lanes.toml:107`.

The lane is the behaviour-preserving classification rather than a budget convenience: the module is
hermetic — every case builds its own temporary enclosure, its own linked Git worktree and its own Git
object store under `tmp_path`, drives the shipped resolution, capture, comparison, snapshot and
retention owners, and touches no live coordination tree, no network and no service — and it carries
`pytestmark = pytest.mark.evidence_unit`. It is an ordinary unit module, which is also why its name
deliberately avoids the governance policy's task-shaped-proof token: a name carrying it would owe a
pinned lifecycle-catalog artifact row, and a plain unit module owes none. The real Git objects it creates
are the `260921-ICR-L1` and `260921-ICR-L18` precedent — real object store, in-process, under a fixture
the module owns.

**Measured on the merged line, from the manifest and the modules on disk rather than by adding any earlier
account:**

| | measured on the working candidate |
| --- | --- |
| Declared lane entries | **314** |
| `mcp/tests/test_*.py` modules on disk | **314** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| File extent | **332 lines** |
| `unit-regression` | **202**, key `:5`, rows `6-207` |
| `public-contract` | **2**, key `:209`, rows `210-211` |
| `integration` | **76**, key `:213`, rows `214-289` |
| `architecture-fitness` | **20**, key `:291`, rows `292-311` |
| `provider-conformance` | **14**, key `:313`, rows `314-327` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:329` and `:331`) |

This account supersedes the population numbers in the sections above it, including the ones headed
**the current account** before this leaf: those remain the as-of records of the tips that produced them.
The insertion sits **above** every other `260921-ICR` row in the knowledge run, so on this leaf's own
candidate every row below it read one line lower: this leaf's own row at `:106`, `260921-ICR-L6`'s
`mcp/tests/test_knowledge_review_one_sided_statements.py` at `:108`, and `260921-ICR-L1`'s
`mcp/tests/test_knowledge_review_source_endpoints.py` at `:109`. **On the merged line — which also carries
`260921-ICR-L20`'s row at `:89`, above this one — those read `:107`, `:109` and `:110`.** Every citation
into this manifest across the onboarding tree was re-derived against the merged bytes rather than shifted
by a carried delta, and the one new row is the only content this leaf added.

- **The new lane row: the durable-comparison-generation cases, in the unit-regression lane, mid-list in the knowledge run.** [43]
- The lane key the row is a member of. [44]
- The row immediately above the insertion, on the merged line (`:106`; `:105` on this leaf's own candidate). [45]
- **The two rows the insertion moved by one line — L6's one-sided-statement row and L1's source-endpoint row.** [46]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [47]
- What the module actually measures, and why it needs a real repository rather than a stub. [48]

## 260921-ICR-L20 One Lane Row — The Ordinary Publication Route's Case Module — **the current account**

This leaf registers **one** module, `mcp/tests/test_knowledge_ingest_publication_route.py`, as a single
row appended to the existing **`unit-regression`** array at **`:89`** — immediately after the two rows
`260921-ICR-L18` added at `:87` and `:88`, and before `mcp/tests/test_knowledge_detection_runs.py`. The
lane is its behaviour-preserving one for the same reason as its two predecessors: the module drives the
shipped CLI in-process over a `tmp_path` world with real Git repositories and real APSW databases, with
no `integration` marker, no docker and no network, so it runs in the ordinary default selection.

```toml
  "mcp/tests/test_knowledge_ingest_publication_route.py",
```

**The insertion moved every manifest entry below it, and that is this card's citation fact.** The file is
**331** lines at this candidate and carries **313** entries for the **313** modules on disk. Every range
this card — and every sibling card that cites this manifest — carries at or below `:88` shifted by one,
and those ranges were **re-derived from the post-edit bytes rather than shifted by a remembered delta**.
The lane headers below the insertion moved with them: `public-contract = [` `:206` → `:208`,
`integration = [` `:210` → `:212`, `stress-durability = [` `:326` → `:328`, and `migration = [` `:329` →
`:330` (the ranges that bracket those arrays moved with their headers). **On the sync line they moved once
more with `260921-ICR-L11`'s row: `public-contract = [` `:209`, `integration = [` `:213`,
`architecture-fitness = [` `:291`, `stress-durability = [` `:329`, `migration = [` `:331`.**

**The merged line adds `260921-ICR-L6`'s row below this one — and, on the sync line, `260921-ICR-L11`'s as
well; the count above is this leaf's own-candidate measurement, and the merged file carries `332` lines and
`314` entries for the `314` modules on disk (see that leaf's account above).**
`260921-ICR-L6` registers `mcp/tests/test_knowledge_review_one_sided_statements.py` in the same
`unit-regression` array at **`:109`** on the merged line — above
`mcp/tests/test_knowledge_review_source_endpoints.py` (`:110`) and below this leaf's own row (`:89`), with
`260921-ICR-L11`'s row at `:107` between them. The insertions are independent: this leaf's row is the
earliest of the three, `260921-ICR-L6`'s next, `260921-ICR-L11`'s the latest, and every range below all
three carries every shift, which is why the rows in this card and its siblings were re-derived against
the merged bytes rather than shifted by a remembered delta.

- **The one row this leaf added, in the lane that owns it, immediately after the two rows the previous leaf added.** [49]
- The lane key the row is a member of, and the array header it sits inside. [50]
- **The modules the two rows above it register, which is the reading this row's position confirms.** [51]
- **The row the merged line adds below this one, and the module it displaced — the second shift the merge applied.** [52]
- The lane headers below the insertion whose brackets moved with it. [53]
- **The manifest's own shape facts this account states: 331 lines, 313 entries for 313 modules on disk.** [54]
- The two consumer rows in the evidence catalog that the same module joined. [55]
- **The manifest's own shape facts this account states: 333 lines, 203 unit-regression entries.** [56]

## 260921-ICR-L18 Two Lane Rows — The Comparison-Generation And Failure-Window Modules — **the current account**

This leaf registers **two** modules, `mcp/tests/test_knowledge_ingest_comparison_generation.py` and
`mcp/tests/test_knowledge_ingest_failure_windows.py`, as `unit-regression` rows **inserted mid-list** in
the alphabetical knowledge run — after `mcp/tests/test_knowledge_curator_ingest_list.py` at `:86` and
above `mcp/tests/test_knowledge_detection_runs.py` at `:89`, so their rows are
`mcp/tests/test-evidence-lanes.toml:87` and `mcp/tests/test-evidence-lanes.toml:88`.

The lane is the behaviour-preserving classification rather than a budget convenience: both modules are
hermetic — every case builds a temporary enclosure through the shipped fixture builders, drives the
shipped CLI entry point as a subprocess, and touches no live coordination tree, no network and no
service — and neither carries an integration marker. They are ordinary unit regression modules, which is
also why the module names deliberately avoid the governance policy's task-shaped-proof token: a name
carrying it would owe a pinned lifecycle-catalog artifact row, and a plain unit module owes none.

**Measured on this candidate, from the manifest and the modules on disk rather than by adding any earlier
account:**

| | measured on the working candidate |
| --- | --- |
| Declared lane entries | **311** |
| `mcp/tests/test_*.py` modules on disk | **311** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| `unit-regression` | **199**, key `:5`, rows `6-204` |
| `public-contract` | **2**, key `:206`, rows `207-208` |
| `integration` | **76**, key `:210`, rows `211-286` |
| `architecture-fitness` | **20**, key `:288`, rows `289-308` |
| `provider-conformance` | **14**, key `:310`, rows `311-324` |
| `stress-durability` | **0**, key `:326` |
| `migration` | **0**, key `:328` |

This account supersedes the population numbers in every earlier section above it, including the one
headed **the current account** before this leaf: those remain the records of the tips that produced them.
The two insertions sit below every earlier insertion point in the knowledge run, so a citation that names
a line below `:88` reads two lines lower than it did before this leaf. **Every citation into this file
across the onboarding tree was re-derived against this candidate rather than shifted**, and the two new
rows are the only content this leaf added.

- **The first new lane row: the successful-journey module, in the unit-regression lane.** [57]
- **The second new lane row: the failure-window module, in the same lane.** [58]
- The lane key both rows are members of, and the row range it covers. [59]
- The two insertions move no existing row of the lane above them, so earlier entries keep their lines. [60]
- The two modules' own statement of what they measure, and the extraction that put the failure surface in a second module. [61]

## 260915-KS-L21 Lane Row (Declared) — **the current account**

This leaf registers **one** module, `mcp/tests/test_migration_census.py`, as a `unit-regression` row
**inserted mid-list** in the alphabetical knowledge run — after `test_memory_scope_task_derivation.py` at
`:127` and above `test_models.py` at `:129`, so its row is `mcp/tests/test-evidence-lanes.toml:129`. The
lane is the behaviour-preserving classification rather than a budget convenience: the module is hermetic —
temporary directories, in-process APSW databases built through the shipped candidate write path, no
integration marker, no repository working tree, no subprocess and no network — and the census it measures is
a read over records that one in-process candidate batch wrote. It adds **48 cases and no integration case**,
which is why the integration lane is untouched by this leaf.

**Measured on this candidate, from the manifest and the modules on disk rather than by adding any earlier
account:**

| | measured on the working candidate |
| --- | --- |
| Declared lane entries | **291** |
| `mcp/tests/test_*.py` modules on disk | **291** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| `unit-regression` | **184**, key `:5`, rows `6-189` |
| `public-contract` | **2**, key `:191`, rows `192-193` |
| `integration` | **74**, key `:195`, rows `196-269` |
| `architecture-fitness` | **17**, key `:271`, rows `272-288` |
| `provider-conformance` | **14**, key `:290`, rows `291-304` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:306` and `:308`) |

**Why every later line of this file shifted, and what it obliges.** The insertion is *mid-list*, so every
entry below it moved by one: the previously-recorded `test_knowledge_change_sets.py` row at `:187` is at
`:188` now, `test_worktree_status_terminal_next_tool.py` moved `:262` → `:263`, and every citation into this
manifest from any route card that pointed below `:128` was re-derived in this pass rather than carried. That
is the mechanical reason several of this card's own rows were re-cited, and it is inherent to the registry
rather than a mistake.

**The budget pair moved too, and this is the leaf that moved it.** `260915-KS-L21`'s 48 unit cases took the
merged unit population from **2158** (measured at its base `a7076008`) to **2206** — six past the then-declared
2200 — so `pyproject.toml`'s unit ceiling was raised to **`unit_case_budget = 2300`** at
`pyproject.toml:244`, with the measured entry recorded above the value (populations at the raise, this leaf's
delta, the increment's per-leaf growth and the zero-tests consequence). Integration is **unchanged at
`integration_case_budget = 400`** at `:245`, measured **394 collected**: this leaf adds no integration case
and its six cases of headroom are reported rather than consumed. The earlier `1500` / `2200` / `1250` / `1100`
values this card quotes in its historical sections are retained as the rulings that produced them and none
was deleted.

## 260915-KS-L22 Lane Row — The Review-Surface Module, And Why It Is A Unit Row

This leaf registers **one** module, `mcp/tests/test_knowledge_review_surface.py`, as a
`unit-regression` entry **inserted mid-list** in the alphabetical knowledge run — between
`test_knowledge_read_scope.py` at `:102` and `test_knowledge_requirement_reference_contract.py` at
`:104` — so its row is `mcp/tests/test-evidence-lanes.toml:103`. The lane is the
behaviour-preserving classification rather than a budget convenience: the module drives the review
surface over temporary directories and in-process databases it builds itself, with no integration
marker, no repository working tree, no subprocess and no network.

**Measured against the manifest and the modules on disk rather than carried from any earlier
account:**

| | measured on this candidate |
| --- | --- |
| Declared lane entries | **292** |
| `mcp/tests/test_*.py` modules on disk | **292** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| `unit-regression` | **185**, key `:5`, rows `6-190` |
| `public-contract` | **2**, key `:192`, rows `193-194` |
| `integration` | **74**, key `:196`, rows `197-270` |
| `architecture-fitness` | **17**, key `:272`, rows `273-289` |
| `provider-conformance` | **14**, key `:291`, rows `292-305` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:307` and `:309`) |

The insertion is *inside* a lane, so every entry below `:103` moves one line down — the mechanical
reason the L21 section's row numbers above read one lower than this file's current positions, and
the reason a batch of citations into this manifest needed re-projecting in the same change rather
than carried.

## 260915-KS-L23 Five Appended Lane Rows — The Line-Stable Append Point

This leaf registers **five** modules, all as `unit-regression` entries **appended to the end of the list**
(`mcp/tests/test-evidence-lanes.toml:196-200`) and never inserted mid-list:

| Row | Module | Why the unit lane |
| ---: | --- | --- |
| `:191` | `mcp/tests/test_next_step_address_binding.py` | 4 cases over `compute_next_step` and `bound_next_step`: no store, no process, no network |
| `:192` | `mcp/tests/test_terminal_preview_expectation.py` | 3 cases over the terminal-validation preview expectation: no store, no process |
| `:193` | `mcp/tests/test_knowledge_merge_right_side_writes.py` | 3 cases over in-process APSW databases the shared merge fixture builds under `tmp_path` |
| `:194` | `mcp/tests/test_evidence_catalog_gate_boundaries.py` | 2 cases over a synthetic catalogue and a disposable `git init` / `git add` repository under `tmp_path` — the only one of the five that shells out, and only against a temporary root |
| `:195` | `mcp/tests/test_curator_coherence_publication_discoverability.py` | 8 cases over the request, the refusal and the `prepare` text, with the surface's collaborators patched through `unittest.mock` |

**Why all five took the unit lane, stated as the constraint it is.** Four are focused suites over
in-process or temporary state; the fifth (`test_evidence_catalog_gate_boundaries.py`) really does shell out
to `git init` / `git add`, against a temporary root it owns. The rows are all in `unit-regression` anyway
because three constraints meet here: the loader requires every `mcp/tests/test_*.py` module to hold exactly
one lane; the integration lane is at exactly **400 / 400** in this change set, so an integration row would
refuse collection and that lane would execute zero tests; and item 16(a)'s append point is the end of a
list, so the row had to go where an append moves nothing — a mid-list or cross-lane placement would have
moved exactly the rows this leaf exists to keep still.

**The append point is the point.** These five rows are the change that makes this manifest's unit list
**not alphabetical at its tail**, and that is deliberate: an insertion in the knowledge run shifts every
row below it and stales every citation into this file (one landing staled **90** rows tree-wide at L19 —
74 inherited, 16 shifted by the leaf's own rows), while an append at the end of the list leaves **every
existing row of that list** where it was. It moves no row; the lane keys below `unit-regression` still
shift, by five here, and that residue is the pure-move class item 16 half (b) reports rather than bills as
curator work. The property is pinned by
`mcp/tests/test_memory_citation_resolution.py::InsertedRegistrationRangeDriftTests::test_the_shipped_registries_append_point_is_the_end_of_its_own_list`,
which measures the **shipped** manifest and also asserts that a contrasting mid-list insertion *does* move a
row, so it cannot pass vacuously; the paired half classifies a citation whose anchor survived a move as a
**report-only** stale range rather than as curator work. No header comment stating the new append point was
added to this file, deliberately — a line at `:1` would shift every row in it and stale hundreds of
citations, so the comment would itself be the defect. The rule lives where it is enforced, in that case.
The five rows are also the manifest's whole byte change: no row was moved, edited or removed.

**Measured on this candidate from the manifest and the modules on disk, not carried from any earlier
account:**

| | measured on this candidate |
| --- | --- |
| Declared lane entries | **297** |
| `mcp/tests/test_*.py` modules on disk | **297** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| `unit-regression` | **190**, key `:5`, rows `6-195` |
| `public-contract` | **2**, key `:197`, rows `198-199` |
| `integration` | **74**, key `:201`, rows `202-275` |
| `architecture-fitness` | **17**, key `:277`, rows `278-294` |
| `provider-conformance` | **14**, key `:296`, rows `297-310` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:312` and `:314`) |

`297` is `292 + 5`: the five modules are new in this change set, so the count moved by exactly the rows the
change set added. This section supersedes the per-lane tables above, including the L21 table whose heading
still calls itself the current account.

**The declared rails are the repository-root file's, and only one lane has headroom.** The budgets are
`unit_case_budget = 4000` at `pyproject.toml:278` and `integration_case_budget = 1000` at `:279`
(`mcp/pyproject.toml` declares no `[tool.pytest.ini_options]`, so the root file is the inifile pytest
actually reads; `mcp/tests/conftest.py` now registers the two option names **without** the dead
`default=1100`/`default=300` declarations item 12 removed). In this change set the unit population measured
**2278 / 2300** and the integration population **400 / 400** — attributed to seat W1's worktree-bound
`pytest … --collect-only` runs, not to this pass, which ran no pytest. Integration therefore has **zero**
headroom, and it matters here: `pytest_collection_finish` raises `UsageError` on an over-budget population,
and an over-budget lane **executes zero tests** — which is why all five of this leaf's rows had to take a
unit lane rather than the integration one, and why the five rows were first mis-appended to the integration
list and corrected after that `UsageError` was measured.

## 260915-CAPS-L11 Row — D9's Six Historical Modules Registered

**This leaf registers the six modules D9 had left unregistered**, all in `unit-regression`, each in a
behaviour-preserving lane chosen by what the module actually does:

| Row | Module | Line | Lane | Why that lane |
| --- | --- | ---: | --- | --- |
| 1 | `mcp/tests/test_eve_adapter.py` | 57 | unit-regression | drives the adapter over doubles; no real runtime |
| 2 | `mcp/tests/test_eve_protocol.py` | 60 | unit-regression | pure protocol encode/decode |
| 3 | `mcp/tests/test_role_capsule_admission.py` | 112 | unit-regression | hermetic over a disposable corpus copy |
| 4 | `mcp/tests/test_role_capsule_compiler.py` | 113 | unit-regression | builds its own fixture; reads no real tree |
| 5 | `mcp/tests/test_role_instruction_corpus.py` | 114 | unit-regression | reads the authored corpus, starts nothing |
| 6 | `mcp/tests/test_task_projection.py` | 139 | unit-regression | in-process projection over fixtures |

**The loader is now silent, and the six are asserted to collect.** `load_lane_manifest` returns
`LANE-REGISTRY-OK 243 0` with no unregistered-module finding, and each of the six modules carries its
own row and collects (14+55+50+11+35+33 = **198** cases under the unit selection, **0** under
`-m integration`). Registering them is not a lane judgement taken by name: the six per-module
`unit-regression` dispositions were re-derived at this leaf's tip, and the seed
`S-D9-lane-row-removed` (delete one row) makes the loader **refuse by name** rather than classify it
by default — which is what proves the rows are load-bearing rather than decorative.

**A method fact worth keeping, because this leaf lost time to it.** The registry's digest must be
**asked of the product**, never rebuilt by hand. An intermediate draft computed
`sha256("\n".join(sorted(f"file:{p}={c}") + …))` — prefixed terms and a merged sort — where
`lane_manifest.py` hashes unprefixed `path=category` pairs with overrides appended unsorted after
them. That reconstruction produced a self-consistent checksum of the *script's own rendering*
(`bfbd21af…`) that described no artifact. The product's own value for this candidate is
**`61f9fba80e5c1c78015eabfc56aac31ca2778bb79a5f75f9a73a6bf984acaaa7`** over **243** files / **0**
overrides. The counts and dispositions were never in question; only the fingerprint was.

## 260915-CAPS-L9 Row

This leaf adds **one** manifest row — `mcp/tests/test_capsule_experiment_install.py:19` — and its
module is **not** a seventh `D9` module: the fail-closed loader still names exactly the same six
at this tip as at the clean base (`test_eve_adapter`, `test_eve_protocol`,
`test_role_capsule_admission`, `test_role_capsule_compiler`, `test_role_instruction_corpus`,
`test_task_projection`). The `test_install_runtime.py` mention at `:74` is pre-existing context
for the catalog consumer proof, not a row this leaf added.

## 260915-CAPS-L20 Lane Row — The Governing-Overview Guard

This leaf added the module its change set created to the existing `unit-regression` lane, one row, so
the fail-closed loader still names no module at all:

```toml
  "mcp/tests/test_governing_overview_resolution.py",
```

The lane is the behaviour-preserving one rather than a judgement call: the module writes only into a
`TemporaryDirectory`, drives no real repository, no boundary process and no network, and its whole
subject is one pure function over a six-file synthetic tree. It is a focused hermetic suite, which is
what the default delivery lane is for.

**Measured at this leaf's frozen candidate, through the product's own loader rather than by reading
this file** (`load_lane_manifest(Path('.'))` in the candidate worktree):

```
lane rows = 244
digest    = 4354cc9f2cca2e33cd1f9e6bb31c8ef4742f61782bf9da9ce9b23cefcd922cdc
new module registered = True -> unit-regression
distribution = unit-regression 147 · integration 64 · architecture-fitness 17 ·
               provider-conformance 14 · public-contract 2
validate_lane_registry() = None
```

`244` is `243 + 1`: `D9` was already complete at this leaf's base — L11 left **243 modules / 243 rows
/ 0 unregistered, 0 stale** — so this leaf's obligation is the one new row and nothing else. The
**digest is unchanged from the base** (`4354cc9f…`, the value the owning seat and L20's reviewer both
read at `621db898`), and that is the expected result rather than a stale read: the manifest digest
covers the declared lane *structure*, and a row added to an existing lane leaves it as it was.

**Why one row is the whole obligation.** `load_lane_manifest` derives the repository's actual test
modules and refuses a manifest that omits one, so an unregistered module is a **hard load failure**
rather than a silent gap — the same fail-closed property `260831-LOCR-L30` repaired a manifest for.
`test_governing_overview_resolution.py` and the extended `test_memory_quality_runs.py` are therefore
both collectable into lanes by construction, and the delivery graph's lane-based selection sees the
regression guards this leaf added.

## Governing Overview

[Tests overview](overview.md)

| Module | Lane | Row | Why that lane |
| --- | --- | ---: | --- |
| `mcp/tests/test_knowledge_detection_runs.py` | `unit-regression` | `:71` | 19 nodes; hermetic — temporary directories, in-process APSW databases, a synthetic union built in memory, and one module-scoped real two-snapshot fixture built by the already-registered `diff_scope_test_support`; no integration marker, no process, no publication |
| `mcp/tests/test_knowledge_detection_signals.py` | `unit-regression` | `:72` | 28 collected cases (20 definitions, one a nine-parameter table) measuring a typed record's own construction boundary — which fields are required, which vocabulary a value must come from, which shape is refused |

| | measured on the working candidate |
| --- | --- |
| Declared lane entries | **249** |
| `mcp/tests/test_*.py` modules on disk | **249** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| `unit-regression` | **149**, rows `5-155` |
| `public-contract` | **2**, rows `156-159` |
| `integration` | **68**, rows `160-229` |
| `architecture-fitness` | **17**, rows `230-248` |
| `provider-conformance` | **13**, rows `249-263` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:264` and `:266`, both closed at `:267`) |

| Module | Lane | Row | Why that lane |
| --- | --- | ---: | --- |
| `mcp/tests/test_knowledge_diff_scope.py` | `unit-regression` | `:76` | 13 nodes; hermetic — temporary directories under `tmp_path`, two in-process APSW databases built through the public store operations (the candidate copied from the closed baseline and curated through the store), two local committed Git trees built by the fixture, no integration marker |
| `mcp/tests/test_knowledge_diff_boundaries.py` | `integration` | `:159` | 15 nodes over the same real trees **driving the production Git probe** rather than a substitute, a real curated candidate database, a real write that moves the logical digest, and the serialized response |

| | measured on the frozen candidate |
| --- | --- |
| Declared lane entries | **243** |
| `mcp/tests/test_*.py` modules on disk | **243** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| Duplicate declarations | **0** |
| `unit-regression` | **143**, rows `5-149` |
| `public-contract` | **2**, rows `150-153` |
| `integration` | **68**, rows `154-223` |
| `architecture-fitness` | **17**, rows `224-242` |
| `provider-conformance` | **13**, rows `243-257` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:258` and `:260`, both closed at `:261`) |

| Module | Lane | Row | Why that lane |
| --- | --- | ---: | --- |
| `mcp/tests/test_knowledge_read_scope.py` | `unit-regression` | `:75` | 21 nodes; hermetic — temporary directories under `tmp_path`, in-process APSW databases built through the public store operations, no repository working tree, no network, no integration marker |
| `mcp/tests/test_knowledge_read_boundaries.py` | `integration` | `:157` | 20 nodes over a **real committed Git tree**, a real published database and real snapshot/namespace refusals |
| `mcp/tests/test_knowledge_read_paths.py` | `integration` | `:158` | 5 nodes that measure Git's own `ls-tree` behavior with their own subprocess calls; it exists because these cases pushed the boundaries module past the 1 200-line hard limit in fix round 2, and the limit was paid rather than waived |

| | measured on the frozen candidate |
| --- | --- |
| Declared lane entries | **241** |
| `mcp/tests/test_*.py` modules on disk | **241** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| Duplicate declarations | **0** |
| `unit-regression` | **142**, rows `6-148` |
| `public-contract` | **2**, rows `150-152` |
| `integration` | **67**, rows `154-221` |
| `architecture-fitness` | **17**, rows `223-240` |
| `provider-conformance` | **13**, rows `242-255` |
| `stress-durability` / `migration` | **0** / **0** |

## 260915-KS-L16 Lane Rows (Declared) — **the current account**
This leaf registered **three** modules: two under `unit-regression`, inserted mid-list among the knowledge
suites, and one appended to `integration`. The two mid-list insertions are what moved every later line of
this file by two:
| Lane | Row | Module | Why this lane |
| --- | ---: | --- | --- |
| `unit-regression` | `:92` | `mcp/tests/test_knowledge_family_review.py` | hermetic: a composition over typed records — which matches a merge keeps, which status an owner may report, what a moved input does to a binding |
| `unit-regression` | `:93` | `mcp/tests/test_knowledge_registered_scope.py` | hermetic: a construction over recorded rows and one declaration, driven by an in-process two-snapshot fixture |
| `integration` | `:265` | `mcp/tests/test_knowledge_family_integrity_pipeline.py` | it drives a real two-snapshot comparison over two real databases and two real Git trees and publishes real bytes to a real destination, and carries `pytestmark = pytest.mark.integration` |
The classification is the **behaviour-preserving** one, not a budget convenience: the two unit modules ask
questions about records and about a declaration, and the one integration module asks the whole-pipeline
question the packet's §6/§7 worked example is about. **The declared ceilings are the ones `pyproject.toml` actually carries** — `unit_case_budget = 4000` at
`pyproject.toml:278` and `integration_case_budget = 1000` at `:279`. This section first recorded the pair as
`2200` / `400`; `260915-KS-L21` raised the unit ceiling to 2300 over the measured 2206 collected (six past
2200), so **2200 is retained here as the value this section measured and is no longer the declaration**, and
the integration value is unchanged at 400. The
three rows are a small delta inside them.
**Why every later line of this file shifted.** The two `unit-regression` rows are inserted mid-list (after
`test_knowledge_family_composition_boundaries.py`), so every entry below them — and every citation into
this file from any route card — moved by two. That is the mechanical reason several other cards' ranges
into this manifest are stale on this candidate.

## 260915-KS-L17 Lane Rows (Declared) — **the previous account, superseded on the three rows above**
This leaf registered **two** modules, both under `unit-regression`, and its insertions are what moved
every later line of this file by two:
| Lane | Row | Module | Why this lane |
| --- | ---: | --- | --- |
| `unit-regression` | `:74` | `mcp/tests/test_knowledge_family_composition.py` | hermetic: temporary directories and in-process APSW databases driven through the real admitted destination — no integration marker, no repository working tree, no subprocess |
| `unit-regression` | `:75` | `mcp/tests/test_knowledge_family_composition_boundaries.py` | the same shape, plus a byte-comparison of the dataset file around a refused read |
The classification is the **behaviour-preserving** one for both modules, not a budget convenience: the
suite's one integration-shaped question — whether composition edges move the retrieval selection — is
answered **by value** over the registered read-scope fixture inside the unit lane rather than by a
second real Git world. **The budget pair this section quotes is the one that candidate carried and is not
the current declaration:** it recorded the unit population at **1341** against the then-pinned
`"unit_case_budget = 1500"` and the integration population at **322** against
`"integration_case_budget = 400"`. The file declares `unit_case_budget = 2300` at `pyproject.toml:244` and
`integration_case_budget = 400` at `:245` on this candidate, and the measured populations are **2206** unit
and **394** integration. This leaf is a +26-unit, +0-integration delta and raises
nothing.
**Why every later line of this file shifted.** These two rows are inserted mid-list under
`unit-regression` (after `test_knowledge_facets.py`), so every entry below them — and every citation
into this file from any route card — moved by two. That is the mechanical reason several other
cards' ranges into this manifest were stale on this candidate and were re-cited during this leaf's
curation.
## 260915-KS-L14 Lane Rows (Declared) — **the current account**
## 260915-KS-L12 Lane Rows (Declared) — **the current account**
**Two new rows, and the line shifts they caused everywhere else.** `mcp/tests/test_knowledge_evidence_claims.py` and `mcp/tests/test_knowledge_evidence_observations.py` are registered in the `unit-regression` lane (rows 73 and 74), each carrying `pytestmark = pytest.mark.evidence_unit`. Every *other* file that cites a line of this manifest moved by the same insertion, and the citations in the cards that quote this file were repaired to the lines that now carry their anchors rather than left pointing at the row above. The lane membership is asserted by the gate rather than by this file alone: a module in the tree that no lane names fails the ownership check.
## 260915-KS-L14 Lane Rows (Declared) — **the previous account, superseded on the two rows above**

The KS-L14 change set adds **two** modules and their rows in the same change, and both are
behaviour-preserving classifications:

Both are inserted into the alphabetical knowledge run, which is why they are rows `:71` and `:72` rather
than appended: `test_knowledge_candidate_workspace.py` precedes them and `test_knowledge_facets.py`
follows. **A two-line insertion moves every later line of this file**, which is the mechanical reason a
number of citations to this manifest elsewhere in the memory tree need re-pointing in the same change.

**The merged measurement, taken on this leaf's working candidate** (measured from the manifest and the
module population on disk, not derived by adding any earlier account):

Against the previous account: **247 / 247** after the L11 and L24 leaves (147 / 2 / 68 / 17 / 13), so this
leaf's two modules are the whole difference. The declared budget pair is `unit_case_budget = 1500`
(`pyproject.toml:304`) and `integration_case_budget = 400` (`pyproject.toml:305`) **as this section measured
it — the pair declared now is `unit_case_budget = 4000` at `pyproject.toml:278` and
`integration_case_budget = 1000` at `:279`** — **unchanged by this
leaf**, whose measured populations are 1315 unit and 322 integration and which consolidated nothing,
skipped nothing, deselected nothing and widened no ceiling.

**This leaf's support-module decision is what keeps the artifact counts unchanged.** Both new modules are
ordinary test source; the run module uses the two **already-registered** fixtures
(`diff_scope_test_support.py` and `read_scope_test_support.py`) rather than adding a third support module,
so `mcp/tests/evidence-lifecycle.toml` gained only two `consumers` rows and its populations stay at
**13 contracts and 54 artifacts**.

## 260915-KS-L8 Lane Rows (Declared) — **the previous account, superseded on the counts above**

The KS-L8 change set adds **two** modules and their rows in the same change, and each lane is that
module's behaviour-preserving classification:

Their shared support module `mcp/tests/diff_scope_test_support.py` is **not** a lane row: it is a governed
artifact (`shared-support` / `internal-canonical` / `integration` / `local-composition`, contract
`knowledge-diff-cases`) in `mcp/tests/evidence-lifecycle.toml`, with exactly those two modules as its
declared consumers — and it is also why `mcp/tests/read_scope_test_support.py`'s consumer list gained the
same two paths in this change, because the diff fixture builds on the read fixture.

### The merged measurement, taken on this leaf's frozen candidate

**Measured from the manifest and the module population on disk, not derived by adding any earlier
account:**

Against the previous leaf: **241 / 241** after `KS-L7` (142 / 2 / 67 / 17 / 13) and **238 / 238** on the
merged base `4eb2b199` (141 / 2 / 65 / 17 / 13), so this leaf's two modules are the whole difference. The
insertions sort into the alphabetical knowledge run — the scope module into unit-regression and the
boundaries module into integration — which is why they are rows `:76` and `:159` rather than adjacent.

**The declared budget pair is unchanged by this leaf:** `unit_case_budget` is **1250** at
`pyproject.toml:286` and `integration_case_budget` is **340** at `pyproject.toml:287`, and
`git status --porcelain pyproject.toml` is **empty** — no dated entry, no comment edit, no value moved.
The raised pair and its merged-line attribution (official 1014/1100 green, KS parent 1003/1100 green,
merged 1138/1100 red *before any L7 line*) are recorded in the L7 section below and are **not re-opened
here**: this leaf's populations fit under both ceilings (unit 1172, integration 319 measured by the final
verification round against the frozen bytes), it consolidated nothing, and it skipped, xfailed,
deselected or widened nothing.

## 260915-KS-L7 Lane Rows (Declared) — **the previous account, superseded on the counts above**

The KS-L7 change set adds **three** modules and their rows in the same change, and the lane each takes is
its behaviour-preserving classification:

Their shared support module `mcp/tests/read_scope_test_support.py` is **not** a lane row: it is a governed
artifact (`shared-support` / `internal-canonical` / `unit-regression`, contract `knowledge-read-scope-cases`)
in `mcp/tests/evidence-lifecycle.toml`, with the three modules above as its exactly-declared consumers.

**The two labelled accounts this card carried below were measured against different code states and their
merged counts were recorded as pending. They have now been measured, and this is the measured account** —
counted from the manifest and the module population on disk, not derived by adding the two accounts:

For the same reason the earlier accounts are labelled rather than merged: the **merged base** `4eb2b199`
carried **238** entries and **238** modules (141 / 2 / 65 / 17 / 13), so this leaf's three test modules are the
whole difference, and neither earlier account alone describes the merged tree. Nothing here is arithmetic on
the two superseded numbers.

**The declared budget pair moved again for this leaf, and every earlier value recorded below is stale.**
`unit_case_budget` is **1250** at `pyproject.toml:286` and `integration_case_budget` is **340** at
`pyproject.toml:287`, raised by the owning seat's dated entry in the same file because the merged line's unit
population was **1138 against a ceiling of 1100** *before any L7 line* — an over-budget population raises
`UsageError` in `pytest_collection_finish`, so the whole unit run executed **zero** tests. This is a
**merged-line sizing defect and not a defect of either side**: the official line alone at `tip 8dd62345`
collected 1014 against its own 1100, and the KS parent `7db50f8f` collected 1003 against the same 1100, and
both were green. **The raise is headroom, not a target**, and the sizing question is not re-opened here: no
existing case was consolidated, deleted, skipped, xfailed or deselected, and the four earlier dated entries
are intact. This leaf's own populations: **unit 1138 → 1159** collected (its 21 unit cases), integration
**279 → 304** selected (its 25 integration cases).

## 260915-KS-L6 Lane Rows (Declared) — **the current account, which supersedes every per-lane number below**

The KS-L6 change set adds **two** modules and their rows in the same change — `test_knowledge_portable_roundtrip.py`
and `test_knowledge_portable_boundaries.py` — both in the **integration** lane at
`mcp/tests/test-evidence-lanes.toml:144-145`. The lane is not a preference here, it is forced: the unit population
sits exactly at its declared `unit_case_budget` of 1000, so a unit row would refuse collection, and both modules are
boundary executors anyway — they create real SQLite databases under `tmp_path`, publish and re-open closed files, and
measure destination bytes and directory contents.

Measured against the working manifest, the population is closed in both directions at **221 modules on disk and 221
declared entries**, with the current brackets: unit-regression **127** at rows 6-132, public-contract 2 at 135-136,
integration **63** at 139-201, architecture-fitness 16 at 204-219 and provider-conformance 13 at 222-234, with
stress-durability (236) and migration (238) empty. The two portable modules sort into the alphabetical integration
run, which is why they are rows 140-141 rather than at the end of the lane; every later integration row moved by two.

Their registration is the same precondition it has been at every KS leaf: an unregistered `test_*.py` module makes
`load_lane_manifest` refuse the repository, which `evidence_lanes.pytest_collection_modifyitems` turns into a
collection error. Classification only — never execution or acceptance evidence.

**The declared budget pair moved for that leaf, and every value in this paragraph is now superseded by `1250` / `340`.** At `KS-L6` `integration_case_budget` was raised 250 → **300** at `pyproject.toml:186` with the doctrine-required dated tradeoff above the pair, and `unit_case_budget` was **1000** at `pyproject.toml:185` with the real unit population 1003 under the warning override this host needs — the pre-existing defect recorded as **D-7**, which the incoming official line closed by raising its own ceiling to 1100. Both then had to move again for `KS-L7` when the *merged* line carried both populations (see the L7 section at the top of this card). The lane's own population at that leaf was **255 cases + 41 subtests**, green with no `--ignore`.

## Current population (measured at this leaf's synced base `23cc7a72` plus its own two rows)

**236** `test_*.py` modules on disk and **230** manifest entries, with the loader reporting **one**
finding: six test files carry no explicit lane. Those six —
`test_eve_adapter.py`, `test_eve_protocol.py`, `test_role_capsule_admission.py`,
`test_role_capsule_compiler.py`, `test_role_instruction_corpus.py`, `test_task_projection.py` — are
**pre-existing at the pristine base** and are none of them this leaf's modules; this leaf adds two rows
and closes none of that gap. Every count stated in the earlier sections below is an earlier
measurement and must be read as such.

**This paragraph is the L7 candidate's measurement, not the current one.** Measured at the L16
candidate (base `8997e184` plus its change set): **232 declared rows** against **238** modules on disk,
the same six D9 modules unregistered. The L16 section below carries that measurement; nothing in this
paragraph is a claim about the current population.

Lane brackets as measured now: unit-regression 134 entries (key `:5`), public-contract 2 (`:141`),
integration 63 (`:145`), architecture-fitness 17 (`:210`), provider-conformance 14 (`:229`), with
stress-durability (`:245`) and migration (`:247`) empty.

Case budgets are `pyproject.toml`'s and are **not** lane membership: `unit_case_budget = 1500` and
`integration_case_budget = 300` (`.tool.pytest.ini_options`). Every earlier 150/200/250/1000/1100
figure quoted in this card's history is stale.

## Purpose

**Population measured in the 260915-KS change set (this branch).** Classifies 217 retained test-shaped modules into explicit evidence categories: **126 unit-regression, 2 public-contract, 60 integration, 16 architecture-fitness and 13 provider-conformance; stress-durability and migration are empty** (measured in the 260915-KS-L4 change set, which is the account that supersedes every per-lane number recorded below). The 260915-KS-L1 change set registered `test_knowledge_store.py` in **unit-regression** (row 74 in the current manifest), the 260915-KS-L2 change set registered four further knowledge modules in that same lane (rows 69-73), and the 260915-KS-L3 change set registered `test_candidate_batch_commands.py` and `test_candidate_batch_transaction.py` (rows 18-19) plus `test_knowledge_label_operations.py` (row 70). The KS-L3 section below carries the measured current brackets; the KS-L2 and KS-L1 sections are those leaves' as-of records. The focused terminal-evidence cursor suite `test_terminal_evidence_cursors.py` and the parked-external-await separation guard `test_parked_external_await_separation.py` are unit-regression members, and 260831-LOCR-L32 added `test_worktree_status_terminal_next_tool.py` to the **integration** lane (row 175; it drives real worktree services and a real repository under `tmp_path`), while 260831-LOCR-L34 added `test_checkpoint_landing_end_to_end.py` to that same lane (row 132; it drives the public checkpoint/closeout operations over real temporary Git repositories), and 260831-LOCR-L36 added `test_cross_master_concurrency.py` to that lane as well (row 143; it drives two sprint-commanded atomic masters and the public land/resume operations over one real temporary Git world), while 260831-LOCR-L37 added `test_pause_stop_only_end_to_end.py` to that same lane (row 159; it drives the public pause over one real temporary Git world holding two atomic masters and measures refs, object databases, coordination tree, worktrees and task documents before and after) **and** `test_pause_is_not_publication.py` to **architecture-fitness** (row 191; it is an AST-only import-closure guard that executes nothing), and the 260831-LOCR seal-removal change set added `test_lifecycle_playthrough_end_to_end.py` to **integration** (row 153; it plays the whole leaf-and-master lifecycle in order over one real temporary Git world and is the regression proof for the deleted child-admission seal). The 260913-LCA-L7 change set added one more integration member.

**Population measured on the official line at the `260831-LOCR-L39` hardening tip (the incoming account).** Classifies the retained test-shaped modules into explicit evidence categories. **Current population measured at the `260831-LOCR-L39` hardening tip (code base `a5f5380b`): 224 modules on disk and 224 manifest entries — 130 unit-regression (key `:5`, rows 6-135, next key `:137`), 2 public-contract (key `:137`, rows 138-139), 62 integration (key `:141`, rows 142-203), 17 architecture-fitness (key `:205`, rows 206-222) and 13 provider-conformance (key `:224`, rows 225-237); stress-durability (`:239`) and migration (`:241`) are empty. The unit-regression bracket is `:5-135`, the integration bracket is `:141-203`.** The L05 measurement and its method are in the `## 260831-LOCR-L04 Lane Row (Declared)` and `## 260831-LOCR-L05 Lane Row (Declared)` sections below; the `## 260831-LOCR-L06 Lane Row (Declared)` section carries the immediately preceding 215-module measurement (pair code base `e9678c56`), the `## 260831-LOCR-L17 Lane Row (Declared)` section the 214-module one before that and the `## 260831-LOCR-L18 Lane Row (Declared)` section the 213-module one before that. Every count and bracket in the two paragraphs below is an earlier measurement — L23 measured 208 modules, and sibling unit-lane insertions from L01 (`:97`) and L10 then moved the later file lines down; L27's own integration row at `:183` accounts for the rest; those two declared sections are the as-of records that carry their own evidence. The focused terminal-evidence cursor suite `test_terminal_evidence_cursors.py` and the parked-external-await separation guard `test_parked_external_await_separation.py` are unit-regression members, and 260831-LOCR-L32 added `test_worktree_status_terminal_next_tool.py` to the **integration** lane (row 175; it drives real worktree services and a real repository under `tmp_path`), while 260831-LOCR-L34 added `test_checkpoint_landing_end_to_end.py` to that same lane (row 132; it drives the public checkpoint/closeout operations over real temporary Git repositories), and 260831-LOCR-L36 added `test_cross_master_concurrency.py` to that lane as well (row 143; it drives two sprint-commanded atomic masters and the public land/resume operations over one real temporary Git world), while 260831-LOCR-L37 added `test_pause_stop_only_end_to_end.py` to that same lane (row 159; it drives the public pause over one real temporary Git world holding two atomic masters and measures refs, object databases, coordination tree, worktrees and task documents before and after) **and** `test_pause_is_not_publication.py` to **architecture-fitness** (row 191; it is an AST-only import-closure guard that executes nothing), and the 260831-LOCR seal-removal change set added `test_lifecycle_playthrough_end_to_end.py` to **integration** (row 153; it plays the whole leaf-and-master lifecycle in order over one real temporary Git world and is the regression proof for the deleted child-admission seal). The 260913-LCA-L7 change set added one more integration member.

**These two accounts are each an as-of record of the state they were measured against, and neither is the merged tree's count.** The merged counts were measured by this branch's curators and are recorded in the `260915-KS-L8 Lane Rows (Declared)` section at the top of this card — **243 declared entries against 243 modules on disk** on this leaf's frozen candidate, after `KS-L7`'s measured 241/241 — so the placeholder this sentence used to carry is resolved rather than still pending. The two accounts below are kept, not deleted, under the memory doctrine's as-of rule.
`test_closeout_projection_source_classification.py` (entry row 137) — it composes the real
`QueueFixture` over temporary Git repositories and drives the production graph admission and
projection path through `graph_context` and `capture_projection_source`, so that is its
behaviour-preserving lane — bringing the manifest to 205 rows. The 260913-LCA-L3 change set registered one more unit-regression member, the new `mcp/tests/test_memory_backfill.py` (entry row 69), and 260831-LOCR-L23 registered `mcp/tests/test_terminal_liveness_registration_order.py` in that same lane (entry row 118), which was `260831-LOCR-L23`'s measured population of 208 modules on disk and 208 manifest entries. The insertions split the alphabetical run again, so the unit-regression lane now carries 117 entries at rows 5-122, public-contract its 2 at 123-126, integration its 60 at 127-188, architecture-fitness its 16 at 189-206 and provider-conformance its 13 at 207-221, while stress-durability (222-223) and migration (224-225) remain empty. The population had earlier fallen below its historical peak because the de-entanglement cut deleted four integration modules — `test_integration_ref_transaction.py`, `test_worktree_integrate_quality_gate.py`, `test_closeout_memory_certification_reuse.py` and `test_prepared_publication_recovery.py` — and the 188 rows this manifest held before 260831-LOCR-L30 were that reduced set; the eight rows added by that leaf brought it to 196, L32's row to 197, L34's to 198, L36's to 199, and L37's two to 201. Every `mcp/tests/test_*.py` module on disk is listed exactly once and no path is duplicated — 224 modules, 224 manifest entries. File counts are not collected-case counts, and the lane bracket is the unit of accounting: unit-regression is the default delivery lane, while the integration lane is capped at 300 collected cases (`pyproject.toml:168`; 260831-LOCR-L37 raised it 200 -> 250 and 260831-LOCR-L24 250 -> 300, with the unit ceiling 1,000 -> 1,100, on the explicit developer tradeoff recorded in `pyproject.toml`, and every earlier 150, 200 and 250 figure recorded in entries of this card is stale). The closeout auto-carry change registered one new module, `test_sync_parked_candidate.py`, in the existing `unit-regression` lane, and the L28 leaf registered its boundary-delivery module `test_state_signal_boundary_delivery.py` in that same lane; the per-lane counts above are the current source membership.

260831-LOCR-L30 registered eight members and, in doing so, repaired a manifest that could not load at
all. `load_lane_manifest` independently proves the declared population closed — it derives the
repository's actual test modules and refuses a manifest that omits one — so an unregistered module is
a **hard load failure**, not a silent gap. Seven tracked `test_*.py` modules (one of them,
`test_record_landing.py`, shipped by the immediately preceding leaf) had no lane row, which made every
manifest consumer fail rather than mis-classify. The eight rows are `test_checkpoint_landing.py`,
`test_closeout_kept_rules_pins.py`, `test_memory_scope_task_derivation.py`,
`test_post_integration_cleanup_guidance.py`, `test_record_landing.py`,
`test_retired_door_publication_fields.py` and `test_automatic_post_integration_cleanup.py` in the
existing lanes, plus `test_memory_quality_is_independent_of_the_closeout_plane.py` in
`architecture-fitness`. Each took its behaviour-preserving lane: the six new unit-regression rows are
hermetic focused suites and the integration lane is capped at 200 collected cases
(`pyproject.toml:135`; the "150" this card's earlier entries recorded is stale), so nothing was
moved into it beyond the one module that genuinely exercises an integration boundary.
## 260915-KS-L4 Lane Rows (Declared)

The KS-L4 change set adds **two** modules and their rows in the same change — `test_knowledge_candidate_workspace.py`
and `test_knowledge_snapshot_publication.py` — both in the **unit-regression** lane at
`mcp/tests/test-evidence-lanes.toml:69` and `:75`. Each is hermetic: temporary directories under `tmp_path`,
in-process APSW databases driven through the real admitted destination and the real publication lock, a child
interpreter used as a crash probe (not a service), no integration marker, and no repository working tree or
network. The default unit lane is therefore each one's behaviour-preserving classification, exactly as it was for
the L2 and L3 knowledge modules beside them.

The two rows sort into the alphabetical run beside the rest of the knowledge block, which is why they sit within
rows 69-76 rather than at the end of the lane.

**Measured current brackets, by entry row** — this is the current account, and it supersedes every earlier
per-lane bracket in this card: unit-regression **126** entries at rows 6-131, public-contract 2 at 134-135,
integration 60 at 138-197, architecture-fitness 16 at 200-215, provider-conformance 13 at 218-230, with
stress-durability (232) and migration (234) empty. The population is closed in both directions at **217** modules
on disk and 217 declared entries — the KS-L3 population was 215 and these are the two additions. Every knowledge
module registered by L1, L2, L3 and L4 now sits inside rows 69-76. Unit collected cases remain inside the declared
`unit_case_budget` 1000 (`pyproject.toml:149`).

Registration is still the same precondition: an unregistered `test_*.py` module makes `load_lane_manifest` refuse
the whole repository, which `evidence_lanes.pytest_collection_modifyitems` turns into a collection error.
Classification only — never execution or acceptance evidence.

## 260915-KS-L2 Lane Rows (Declared)

The KS-L2 change set adds **four** modules and their rows in the same change — `test_knowledge_family_revision.py`,
`test_knowledge_graph_reads.py`, `test_knowledge_relation_rules.py` and `test_knowledge_revision_seals.py` — at
rows `mcp/tests/test-evidence-lanes.toml:71-75`, all in the **unit-regression** lane. Each is hermetic (temporary
directories under `tmp_path`, in-process APSW databases, no integration marker, no repository or subprocess), so
the default unit lane is each one's behaviour-preserving classification. The population is closed in both
directions at **212** modules on disk and 212 declared entries — the KS-L1 population was 208 and these are the
four additions.

**Measured current brackets, by entry row** — this is the current account, and it supersedes every earlier
per-lane bracket in this card: unit-regression **121** entries at rows 6-126, public-contract 2 at 129-130,
integration 60 at 133-192, architecture-fitness 16 at 195-210, provider-conformance 13 at 213-225, with
stress-durability (226-228) and migration (229-231) empty. The knowledge modules sit at rows 67-71, inside the
alphabetical run, so the insertion shifted the lanes after it. Unit collected cases remain inside the declared
`unit_case_budget` 1000 (`pyproject.toml:149`).

`test_knowledge_revision_seals.py` arrived one round later than the other three, as the fix for sealed review
finding `260915-KS-L2-RV-1`: the round-1 mutation array could not kill the sealed predecessor field on either
payload, and the new module is where the field-isolating evidence for it now lives. Its row was added in the same
change, which is why one leaf is recorded as three rows plus one.

Registration here is not bookkeeping, and the KS-L1 note below states why: `load_lane_manifest` derives the
repository's actual test modules and refuses a manifest that omits one, so an unregistered module is a **hard load
failure** — the lane plugin raises `pytest.UsageError` during collection and the quality path swallows the same
error into a run without retry proof. These rows are classification only — never execution or acceptance evidence.

## 260915-KS-L3 Lane Rows (Declared)

The KS-L3 change set adds **three** modules and their rows in the same change — `test_candidate_batch_commands.py`,
`test_candidate_batch_transaction.py` and `test_knowledge_label_operations.py` — all in the **unit-regression**
lane. Each is hermetic (temporary directories under `tmp_path`, in-process APSW databases driven through the real
admitted destination, no integration marker, no repository and no subprocess), so the default unit lane is each
one's behaviour-preserving classification. The direct rows are
`mcp/tests/test-evidence-lanes.toml:18`, `:19` and `:70`; the two batch modules sort into the alphabetical run
near its top, which is why the first two sit at rows 18-19 rather than beside the knowledge block.

The first two are the pair the requirement's verification evidence asks for, and their third sibling exists
because a passing batch suite could not cover the standalone label guard: `test_candidate_batch_transaction.py`
carries the all-or-nothing proof (mutating the rollback to a commit fails a named node), the admission and lane
refusals, the completed-graph lineage rule and the removal receipts; `test_candidate_batch_commands.py` carries the
closed union's coverage and the receipt's fidelity; `test_knowledge_label_operations.py` drives the two standalone
label edits so deleting the CAS in `labels.py` fails a named node — the mutation that left every batch case green
before this module existed (sealed finding `260915-KS-L3-RV-4`).

The population is closed in both directions at **215** modules on disk and 215 declared entries — the KS-L2
population was 212 and these are the three additions. **Measured current brackets, by entry row** — this is the
current account, and it supersedes every earlier per-lane bracket in this card: unit-regression **124** entries at
rows 5-130, public-contract 2 at 131-134, integration 62 at 135-196, architecture-fitness 18 at 197-214,
provider-conformance 13 at 215-229, with stress-durability (230-231) and migration (232-233) empty. The five
earlier knowledge modules sit at rows 69-74, inside the alphabetical run. Unit collected cases remain inside the
declared `unit_case_budget` 1000 (`pyproject.toml:149`).

Registration is the same precondition it has been at every KS leaf: an unregistered `test_*.py` module makes
`load_lane_manifest` refuse the whole repository, which `evidence_lanes.pytest_collection_modifyitems` turns into a
collection error. Classification only — never execution or acceptance evidence.

## 260915-KS-L1 Lane Row (Declared)

The KS-L1 change set adds `mcp/tests/test_knowledge_store.py` **and** its row in the same change, so the
manifest stays closed at **208** modules on disk and 208 manifest entries — the L3 population was 207 and this is
the one addition. The row is `mcp/tests/test-evidence-lanes.toml:67`, in the **unit-regression** lane: the module
is hermetic (temporary directories under `tmp_path`, in-process APSW databases, no integration marker, no
repository or subprocess), so the default unit lane is its behaviour-preserving classification.

Registration here is not bookkeeping. `load_lane_manifest` derives the repository's actual test modules and
refuses a manifest that omits one, so an unregistered module is a **hard load failure**: the lane plugin raises
`pytest.UsageError` during collection and the quality path swallows the same error into a run without retry proof.
The leaf's own independent review confirmed both consequences before the row existed. The row is classification
only — never execution or acceptance evidence.

Measured current brackets, by entry row: unit-regression **117** entries at rows 6-122, public-contract 2 at
125-126, integration 60 at 129-188, architecture-fitness 16 at 191-206, provider-conformance 13 at 209-221, with
stress-durability (222-224) and migration (225-227) empty; the lane key itself sits at `:5`. Unit collected cases
remain inside the declared `unit_case_budget` 1000 (`pyproject.toml:149`). The insertion is at `:67`, above every
row the L3 entry above cites, so the L4/L5/L7/L8 sections' bracket numbers and row positions are unchanged by this
change and the L3 note remains their superseding account. The population is closed in both directions: 208 modules
on disk, 208 declared entries, no undeclared module and no stale row.

## 260915-CAPS-L15 Lane Row (Declared)

The L15 change set adds `mcp/tests/test_capsule_launch_wiring.py` **and** its row in the same change, so
the manifest stays closed in that change set. The row is `mcp/tests/test-evidence-lanes.toml:19`, in the
**unit-regression** lane, inserted alphabetically between `test_causal_quality_preflight.py` and
`test_capsule_serving.py`. That is its behaviour-preserving lane: the module's fourteen cases drive the
launch points, the runner preparation and the adapter factory **in process**, with the vendor boundary
recorded and the tmux host doubled — it starts no real process and calls no vendor — so the hermetic
default unit lane is where it belongs. **Lane row added; no case added to any capped population that
was not already there.**

**The loader invariant is the point of this row (defect D9).** `load_lane_manifest` independently proves
the declared population closed — it derives the repository's actual test modules and refuses a manifest
that omits one — so a new test module without a lane row is a **hard load failure** for every manifest
consumer, not a silent gap. L15 followed that rule in the same change that added the module; the six
historical D9 modules remain the final-verification leaf's, unchanged by this leaf. Classification only:
lane membership is not execution, certification or acceptance evidence.

## 260915-CAPS-L16 Lane Row (Declared)

The L16 change set adds `mcp/tests/test_citation_source_index_membership.py` **and** its row in the same
change, so the manifest stays closed in that change set. The row is
`mcp/tests/test-evidence-lanes.toml:26`, in the **unit-regression** lane, inserted alphabetically
between `test_checkpoint_landing.py` and `test_cli_discovery.py`. That is its behaviour-preserving
lane: the module's seven cases build disposable code roots and drive the real citation source index
in-process — they start no server, launch no process and touch no product surface — so the hermetic
default unit lane is where a previously-unmarked module already ran. **Lane row added; no case added
to any capped population that was not already there.**

Measured at this leaf's synced base `8997e184` **plus** this change set, by counting the manifest's
declared path rows and the modules on disk: **232 declared rows** against **238** `mcp/tests/test_*.py`
modules, so **six** modules remain unregistered — exactly the pre-existing D9 set owned by the
final-verification leaf (`test_eve_adapter.py`, `test_eve_protocol.py`, `test_role_capsule_admission.py`,
`test_role_capsule_compiler.py`, `test_role_instruction_corpus.py`, `test_task_projection.py`). This
leaf closed none of that gap. The lane keys still sit at unit-regression `:5`, public-contract `:143`,
integration `:147`, architecture-fitness `:212`, provider-conformance `:231`, with stress-durability
(`:247`) and migration (`:249`) empty; the one insertion at `:26` pushes every row below it down one
line, so the section immediately above records the previous candidate's row numbering and is that
leaf's as-of record. Classification only: lane membership is not execution, certification or
acceptance evidence.

## 260915-CAPS-L17 Lane Row (Declared)

The L17 change set adds `mcp/tests/test_eve_effort_runtime.py` **and** its row in the same change, so the
manifest stays closed over the modules it declares. The row is
`mcp/tests/test-evidence-lanes.toml:191`, in the **integration** lane, inserted alphabetically between
`test_eve_capsule_runtime.py` (`:189`) and `test_git_command.py` (`:191`). (`:188`/`:187`/`:189` were this
row's position at the L17 change set; `260918-TSIP-L6`'s two insertions moved all three by +2.) That is its
behaviour-preserving lane: each case starts the **real** runtime process with a complete verified capsule
binding, boots a real hermetic Node application and reads the request body a live recording provider
received — so it is a boundary executor, not a hermetic unit. It carries three cases and no `-m`
override; the integration lane is where they belong.

Measured at this change set by deriving the disk file list and the manifest rows and diffing them:
**240** `mcp/tests/test_*.py` modules on disk against **234** declared rows, with **no stale row** (every
declared path exists) and **six** modules unregistered — exactly the pre-existing D9 set owned by the
final-verification leaf (`test_eve_adapter.py`, `test_eve_protocol.py`, `test_role_capsule_admission.py`,
`test_role_capsule_compiler.py`, `test_role_instruction_corpus.py`, `test_task_projection.py`). **This
leaf closed none of that gap** and added no row beyond its own. Lane brackets, by entry row:
unit-regression 137 entries (key `:5`, rows 6-142), public-contract 2 (key `:144`, rows 145-146),
integration 64 (key `:148`, rows 149-212), architecture-fitness 17 (key `:214`, rows 215-231),
provider-conformance 14 (key `:233`, rows 234-247), with stress-durability (`:249`) and migration
(`:251`) empty.

**Recorded, not repaired: D27 lives in one of the six modules above.** The unregistered
`mcp/tests/test_eve_adapter.py` is also the module whose
`EveRegistryTests::test_the_registry_leaves_the_path_harnesses_on_the_ordinary_lookup` asserts an
environment fact another test in the same run can falsify; `AR_EVE_NODE` in the pytest process
environment is the confirmed one-variable trigger. Neither the missing lane row nor the assertion's
shape is this leaf's repair — both are carried with their direction and owner so the next reader finds
attribution rather than an unexplained red.

Classification only: lane membership is not execution, certification or acceptance evidence.

## 260913-LCA-L4 Pending Lane Row (Open At L4, Resolved Since)

**Resolved — see the L5 section below.** At the L4 change set the manifest was one row short.

The L4 change set added `mcp/tests/test_memory_attribution_producers.py` and did **not** register it in
this manifest, so the closed population the `Logic` section below describes does not hold for that
change set. Measured at base `5bb124d4` plus that change set, by diffing the file list against the
manifest:

- 203 `mcp/tests/test_*.py` modules exist on disk; the manifest declares 202 (114 unit-regression, 2
  public-contract, 57 integration, 16 architecture-fitness, 13 provider-conformance, 0 stress-durability,
  0 migration).
- The single undeclared path is `mcp/tests/test_memory_attribution_producers.py` — the one file in the
  disk set with no manifest row — and there is no stale row naming a file that is gone.

This is not a documentation gap but the hard failure this card already records from 260831-LOCR-L30:
`load_lane_manifest` derives the repository's actual test modules and refuses a manifest that omits one.
The derivation reaches the new module — `testpaths = ["mcp/tests"]` in the repository-root
`pyproject.toml:155` puts it inside the test roots, and its `test_` prefix classifies it as a test module
— and `mcp/test_support/agents_remember_test_support/code_quality/check.py:677` is a manifest consumer, so
every consumer fails rather than mis-classifying. The lane the module belongs in is the builder's call and
is **not** asserted here: the module is hermetic except for its two cases that compose `QueueFixture` over
real temporary Git repositories. The row is recorded as pending so the next reader finds the gap rather
than a claim of completeness.

## 260913-LCA-L5 Lane Row (Declared)

**Superseding the L4 section above, the manifest is closed again.** Measured at base `52875e7a` by
diffing the disk file list against the manifest, the L4 module `test_memory_attribution_producers.py`
does have its lane row (line `:68`, `unit-regression`, added by the commit that landed L4), so the
203-modules/203-entries population held at this leaf's base and the open gap the L4 section records is
resolved.

The L5 change set adds `mcp/tests/test_leaf_doc_master_link_binding.py` **and** its row in the same
change, so the population stays closed at 204 modules on disk and 204 manifest entries. The row is
`mcp/tests/test-evidence-lanes.toml:195`, in the **integration** lane: it drives the real public
`worktree_start` over one disposable code repository and one external memory repository per case, so it
is a boundary executor rather than a hermetic unit — that is its behaviour-preserving lane.

Measured current brackets, by entry row: unit-regression 115 entries at rows 6-120, public-contract 2
at 123-124, integration 58 at 127-184, architecture-fitness 16 at 187-202, provider-conformance 13 at
205-217, stress-durability and migration empty. The Purpose paragraph records the current L3
measurement (207 modules, 116 unit-regression, 60 integration), so these L5 brackets are that leaf's
as-of record; the insertion at `:152` shifted every integration entry after it and both later lane
blocks by one.

## 260913-LCA-L7 Lane Row (Declared)

The L7 change set adds `mcp/tests/test_closeout_projection_source_classification.py` **and** its row in
the same change, so the manifest stays closed at 205 modules on disk and 205 manifest entries — the L5
population was 204 and this is the one addition. The row is
`mcp/tests/test-evidence-lanes.toml:177`, in the **integration** lane: the module composes the real
`QueueFixture` over temporary Git repositories and drives the production graph admission and projection
path, so it is a boundary executor rather than a hermetic unit — that is its behaviour-preserving lane.
The manifest is also a fail-closed input here, not a list of cases: `test_closeout_queue.py` is a
one-to-one sidecar source whose card describes a shared fixture with no retained standalone queue tests,
and this new module is a real consumer of that fixture rather than a rename or replacement of it. No
existing row moved and no existing row changed lane: the insertion at `:137` sits inside the
alphabetical integration run and pushes only the later line numbers down by one.

Measured current brackets, by entry row: unit-regression 115 entries at rows 5-120, public-contract 2
at 122-124, integration 59 at 126-185, architecture-fitness 16 at 187-203, provider-conformance 13 at
205-218, stress-durability and migration empty. The Purpose paragraph records the current L3
measurement and the L5 section carries the 204-module brackets; these L7 numbers are that leaf's
as-of record, superseded by the L3 population. The insertion at `:137` sits before entries that this
card cites, so each of those rows is one line higher than the L5 section recorded it:
`test_leaf_doc_master_link_binding.py` `:152` → `:153`, `test_lifecycle_playthrough_end_to_end.py`
`:155` → `:156`, `test_pause_stop_only_end_to_end.py` `:161` → `:162`,
`test_worktree_status_terminal_next_tool.py` `:181` → `:182`, and
`test_pause_is_not_publication.py` `:193` → `:194`; the unit-lane
`test_memory_attribution_producers.py` row at `:68` and every row above the insertion are unchanged.

## 260913-LCA-L8 Lane Row (Declared)

The L8 change set adds `mcp/tests/test_terminal_blocker_reasons.py` **and** its row in the same
change, so the manifest stays closed at 206 modules on disk and 206 manifest entries — the L7
population was 205 and this is the one addition. The row is
`mcp/tests/test-evidence-lanes.toml:221`, in the **integration** lane: the module builds a real landed
leaf over disposable code and external-memory repositories, completes the integration through the
public `worktree_integrate_tool`, and drives the public `lifecycle_finalize_task_tool` plus a real
permission failure on the provider-runtime tree, so it is a boundary executor rather than a hermetic
unit — that is its behaviour-preserving lane.

Measured current brackets, by entry row: unit-regression 115 entries at rows 5-120, public-contract 2
at 122-124, integration 60 at 126-186, architecture-fitness 16 at 188-204, provider-conformance 13 at
206-219, stress-durability and migration empty. The L7 section above carries the 205-module brackets,
which are that leaf's as-of record; the Purpose paragraph carries the current L3 measurement (207
modules, 207 manifest entries), which supersedes these L8 numbers.

The insertion at `:177` also corrects three out-of-order entries that the earlier insertions had left
behind in the closeout-input consumer list: `test_cross_master_concurrency.py` moves after
`test_context_packet.py` (`:309` → `:312`), `test_lifecycle_finalize.py` after
`test_leaf_doc_master_link_binding.py` (`:315` → `:316`) and `test_memory_attribution_producers.py`
after `test_mcp_stdio_transport.py` (`:319` → `:320`). That is why the L5 row moves **up** one line
(`:316` → `:315`) while the L4 row moves down one (`:319` → `:320`). No existing row changed lane. Two
rows this card cites sit after the insertion and are one line higher than the L7 section recorded
them: `test_worktree_status_terminal_next_tool.py` `:182` → `:183` and
`test_pause_is_not_publication.py` `:194` → `:195`; `test_pause_stop_only_end_to_end.py` `:162`, the
playthrough `:156`, the L7 row `:137` and the L4 row's lane are unchanged.

## 260915-CAPS-L5 Lane Row (Declared)

The L5 change set adds `mcp/tests/test_codex_capsule_delivery.py` **and** its row in the same change.
The row is `mcp/tests/test-evidence-lanes.toml:260`, in the **provider-conformance** lane, inserted
alphabetically between `test_codex_app_server_adapter_turns.py` and
`test_harness_control_claude.py`. That is its behaviour-preserving lane: the module's subject is the
vendor app-server's instruction channel — an instruction-channel fixture generated from the installed
`codex-cli 0.151.0` schema, one live native case, and the Codex adapter/session seam — which is exactly
what the sibling `test_codex_app_server_*` modules are classified as. The module carries **28 collected
cases and no `integration` marker**, so nothing here spends integration budget.

**Additive proof, measured by the loader itself.** Before the row the fail-closed loader reported
**7** findings including this module; after it, **6** — and the module is absent from them. No existing
row was edited, reordered or removed.

**Measured population at this candidate.** 216 `mcp/tests/test_*.py` modules on disk, **210** manifest
rows — unit-regression **118**, public-contract 2, integration 60, architecture-fitness 16,
provider-conformance **14**, with stress-durability and migration empty — so **6 modules remain
unregistered**, and they are exactly the pre-existing D9 set owned by the final-verification leaf:
`test_eve_adapter.py`, `test_eve_protocol.py`, `test_role_capsule_admission.py`,
`test_role_capsule_compiler.py`, `test_role_instruction_corpus.py`, `test_task_projection.py`. This leaf
added its own row and **did not** touch the other six; the loader's exact output is the pin.

Classification only: lane membership is not execution or acceptance evidence, and the six D9 rows are
not this leaf's to classify.

## 260915-CAPS-L4 Lane Row (Declared) — And The Unit Population Now Refuses Collection

The L4 change set adds `mcp/tests/test_capsule_serving.py` **and** its row in the same change, so the
manifest stays closed over the modules it declares at **208 rows** — the L3 population plus this one.
The row is `mcp/tests/test-evidence-lanes.toml:19`, in the **unit-regression** lane, inserted
alphabetically between `test_causal_quality_preflight.py` and `test_certification_lane_bridge.py`. That
is its behaviour-preserving lane: 19 of the module's 21 cases are hermetic (a disposable coordination
root and a synthetic skills corpus, no integration marker) and only the two real-process exchanges are
marked `integration`, so the module's default lane is unit-regression and only its two marked items
spend integration budget.

Measured brackets at this leaf, by entry row: unit-regression **117** entries at rows 5-121,
public-contract 2 at 124-126, integration 60 at 128-189, architecture-fitness 16 at 190-207,
provider-conformance 13 at 208-222, with stress-durability (223-224) and migration (225-226) empty. The
Purpose paragraph above carries the L3 measurement (207 modules, 116 unit-regression); these are the
measured L4 numbers and the one addition is this module.

**The unit population now refuses collection on this branch, and this leaf did not cause it.** The
default unit selection collects **1083** cases against `unit_case_budget = 1000`
(`pyproject.toml:149`), and it already collected **1064** against that ceiling at the leaf's base — so
the overage is 83 and **64 of it predates this leaf**. This leaf's contribution is 19 unit cases over
two new public surfaces and it did **not** edit the ceiling, move the module into another lane to dodge
the check, or drop a case. The enforcement point is
`conftest.pytest_collection_finish`, which raises `pytest.UsageError` for the unit population **before
any case executes**, so a default `pytest` run cannot execute on this worktree at all. The integration
population is 227 against its 250 ceiling and is not implicated. This is recorded rather than repaired
because raising a declared case budget requires an explicit change tradeoff and is an owner-level
decision (the leaf's `F-L4-01`, escalated to the master's owning seat; L11 owns the ceiling and the
master-tip overage).

**Six tracked test modules remain undeclared.** The manifest declares 208 rows while **214**
`mcp/tests/test_*.py` modules exist on disk: `test_eve_adapter.py`, `test_eve_protocol.py`,
`test_role_capsule_admission.py`, `test_role_capsule_compiler.py`, `test_role_instruction_corpus.py`
and `test_task_projection.py`. These are the pre-existing master-tip gaps recorded as `D9` in
`notes/product-defects-observed.md` and owned by L11; `load_lane_manifest` names exactly these six and
`test_capsule_serving.py` is **not** among them. This leaf added its own row and deliberately touched no
other entry.

Measured current brackets, by entry row: unit-regression 117 entries at rows 5-121, public-contract 2
at 124-126, integration 60 at 128-189, architecture-fitness 16 at 190-207, provider-conformance 13 at
208-222, stress-durability and migration empty; the one insertion at `:19` moved every cited row below
it one line higher.

## 260831-LOCR-L01 Lane Row (Declared)

The LOCR-L01 change set adds `mcp/tests/test_serving_observation_loop.py` **and** its row in the same
change, so the manifest stays closed in that change set — the L3 population was 207 modules and 207
entries, and this is the one addition. The row is `mcp/tests/test-evidence-lanes.toml:98`, in the
**unit-regression** lane: the module injects fakes, issues no HTTP request, starts no process and
publishes nothing, so it is a hermetic unit rather than a boundary executor — that is its
behaviour-preserving lane.

The insertion sits inside the alphabetical unit-regression run, between
`test_semantic_topology_refusals.py` and `test_signal_routing.py`, so every entry below it and every
later lane key is one line higher than the L3 entry recorded, and the Purpose paragraph's
207-modules/207-entries / 116-unit-regression figures are that L3 measurement rather than this one.
The read-only bounds in this paragraph are that leaf's as-of record: L27's own insertion at `:182`
moved the later **file lines** again. The `## 260831-LOCR-L27 Lane Row (Declared)` section below
carries the measurement that includes both insertions. Classification only: lane membership is not
execution or acceptance evidence, and the verification stamps remain closeout-owned.

## 260831-LOCR-L27 Lane Row (Declared)

The L27 change set adds `mcp/tests/test_terminal_liveness_pane_authority.py` **and** its row in the
same change, so the manifest stays closed in that change set — the L23 population was 208 modules and
208 entries, and further unit-lane rows arrived from L01 and L10 before this leaf settled. At base
`52bee429` **plus** this change set the manifest holds 211 modules on disk and 211 manifest entries.
The row is `mcp/tests/test-evidence-lanes.toml:221`, in the **integration** lane, between
`test_terminal_liveness.py` at `:218` and `test_tools.py` at `:220`.

That is its behaviour-preserving lane even though the module is hermetic (temporary catalogs,
in-process `unittest`, no `worktree_services`): it is registered exactly as its sibling
`test_terminal_liveness.py` is at `:218`, and a new module in this family needs a row or its
application imports run inside ordinary unit collection. The module is the first member of that
family to be **added** rather than extended — an in-place extension of `test_terminal_liveness.py`
reached the coding-guidelines 900-1200 band, so the proof was split out instead and the sibling stayed
byte-unchanged. **Line-number discipline for this row:** it sat at `:181` on this candidate's own
build base `b368b661`, at `:182` on base `163ba8a9` plus this change set, and at `:183` at base
`52bee429` plus this change set. The verdict and worker report cite `:181`; every later figure is a
base effect from sibling unit-lane insertions, not a change to this leaf's delta, which is always
exactly one inserted row.

Measured current membership at base `52bee429` **plus** this change set: unit-regression 119 entries,
its key at `:5` and the next key at `:126`; public-contract 2 (key `:126`); integration **61** (key
`:130`); architecture-fitness 16 (key `:193`); provider-conformance 13 (key `:211`); stress-durability
(`:226`) and migration (`:228`) empty. This module is entry ordinal **53 of 61** in the integration
lane. No existing row changed lane and no case budget was raised; the integration ceiling stays 250
(`pyproject.toml:150`). Classification only: lane membership is not execution, certification or
acceptance evidence.

## 260831-LOCR-L17 Lane Row (Declared)

The L17 change set adds `mcp/tests/test_terminal_observer_health.py` **and** its row in the same
change, so the manifest stays closed in that change set — the population at base `99534dc5` alone was
213 modules and 213 entries, and this is the one addition. The row is
`mcp/tests/test-evidence-lanes.toml:124`, in the **unit-regression** lane, immediately below
`test_terminal_liveness_registration_order.py` at `:121` and above `test_terminal_paste.py` at `:123`.
The module drives the record, the writer, the accumulator, and the real `_state_response` handler and
`stream_events` generator against stub projectors — it issues no HTTP request, starts no server and
starts no process — so the hermetic default unit lane is its behaviour-preserving classification. The
route half deliberately avoids an ASGI app: the integration population has only three cases of
headroom against its 250-case cap and the brief forbids raising it, so the production handler and
generator are called directly instead.

Measured at base `99534dc5` **plus** this change set, by diffing the disk file list against the
manifest and by bracket position: **214** `mcp/tests/test_*.py` modules on disk and **214** manifest
entries — unit-regression **121** entries (key `:5`, rows 6-126, next key `:128`), public-contract 2
(key `:128`, rows 129-130), integration **62** (key `:132`, rows 133-194), architecture-fitness 16
(key `:196`, rows 197-212), provider-conformance 13 (key `:214`, rows 215-227), with stress-durability
(`:229`) and migration (`:231`) empty. No existing row changed lane and no case budget was raised; the
integration ceiling stays 250 (`pyproject.toml:150`). The insertion sits inside the alphabetical
unit-regression run, so it moves the later lane keys, not the rows above it — in particular
`test_serving_observation_loop.py` stays at `:97` and `test_serving_startup_prime.py` at `:98`, so
**`LOCR-R11@v1`'s and `LOCR-R18@v1`'s classifications are untouched by this leaf**. Classification
only: lane membership is not execution, certification or acceptance evidence, and the verification
stamps remain closeout-owned.

## 260831-LOCR-L18 Lane Row (Declared)

The L18 change set adds `mcp/tests/test_serving_startup_prime.py` **and** its row in the same change,
so the manifest stays closed in that change set — the population at base `d868486c` alone was 212
modules and 212 entries, and this is the one addition. The row is
`mcp/tests/test-evidence-lanes.toml:99`, in the **unit-regression** lane, immediately below its
sibling `test_serving_observation_loop.py` at `:97` and above `test_signal_routing.py` at `:99`. The
module drives the real `_serving_lifespan` under a temporary catalog, a virtual event-loop clock, an
in-process fake tmux host and parked sibling loops — it issues no HTTP request, starts no process and
publishes nothing — so the hermetic default unit lane is its behaviour-preserving classification, the
same lane its sibling already holds for the same reason.

Measured at base `d868486c` **plus** this change set, by diffing the disk file list against the
manifest and by bracket position: **213** `mcp/tests/test_*.py` modules on disk and **213** manifest
entries — unit-regression **120** entries (key `:5`, bracket `:5-125`, next key `:127`),
public-contract 2 (`:127`), integration **62** (key `:131`, bracket `:131-193`), architecture-fitness
16 (`:195`), provider-conformance 13 (`:213`), with stress-durability (`:228`) and migration (`:230`)
empty. No existing row changed lane and no case budget was raised; the integration ceiling stays 250
(`pyproject.toml:150`). The insertion sits inside the alphabetical unit-regression run, so it moves
the later lane keys, not the rows above it. Classification only: lane membership is not execution,
certification or acceptance evidence, and the verification stamps remain closeout-owned.

## 260831-LOCR-L06 Lane Row (Declared)

The L06 change set adds `mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py` **and** its row
in the same change, so the manifest stays closed in that change set. The row is
`mcp/tests/test-evidence-lanes.toml:68`, in the **unit-regression** lane, immediately below
`test_lifecycle_operation_model_helpers.py` at `:67` and above `test_memory_attribution_producers.py`
at `:69`. The module drives the real `TerminalCatalogLivenessSweeper` over a real `TerminalCatalog`
with a scripted single-seat adapter endpoint, hands the resulting native page to the production lift
(`latest_native_terminal_evidence`), and then drives the real `run_agent_notifier_sweep` to persist
the durable row — it issues no HTTP request, starts no server and starts no process, and its only
durable write is the ordinary inbox row under test — so the hermetic default unit lane is its
behaviour-preserving classification.

Measured at pair code base `e9678c56` (which already carries L17's landed row) **plus** this change
set, by diffing the disk file list against the manifest and by bracket position: **215**
`mcp/tests/test_*.py` modules on disk and **215** manifest entries, every module listed exactly once
and no path duplicated — unit-regression **122** entries (key `:5`, rows 6-127, next key `:129`),
public-contract 2 (key `:129`, rows 130-131), integration **62** (key `:133`, rows 134-195),
architecture-fitness 16 (key `:197`, rows 198-213), provider-conformance 13 (key `:215`, rows 216-228),
with stress-durability (`:230`) and migration (`:232`) empty. No existing row changed lane and no case
budget was raised; the declared case budgets live in `pyproject.toml`, which is the authority for
them. The insertion sits inside the alphabetical unit-regression run and below every row this card
cites from `LOCR-R09@v1`, `LOCR-R11@v1`, `LOCR-R18@v1` and the L17 observer-health proof, so those
classifications are untouched by this leaf — it moves the later lane keys and the rows at or below
`:68`, which is why every affected citation in this card and in `overview.md` was re-derived against
the candidate rather than carried.

Scope note: this leaf is a **preservation leaf** — `mcp/src` is byte-unchanged by it (`git status
--porcelain` = ` M mcp/tests/test-evidence-lanes.toml` plus the untracked module; `mcp/src` diff = 0
files), and the module's digest, line count and lane ordinal are measurements of an uncommitted,
unaccepted tree. Classification only: lane membership is not execution, certification or acceptance
evidence, and the verification stamps remain closeout-owned.

## 260831-LOCR-L05 Lane Row (Declared)

The L05 change set adds `mcp/tests/test_state_signal_worker_wake.py` **and** its row in the same
change, so the manifest stays closed in that change set. The row is
`mcp/tests/test-evidence-lanes.toml:105`, in the **unit-regression** lane, immediately below
`test_state_signal_restart_recovery.py` at `:104` and above `test_structural_dispatch_recovery.py`
at `:106`. The module seeds owned worker and manager seats on a real `TerminalCatalog`, drives the
real `run_agent_notifier_sweep` over a temporary coordination root with real task documents, a real
inbox log and the real durable stores, and asserts the whole inbox store rather than its state-signal
subset — it issues no HTTP request, starts no server and starts no process, and its only durable write
is the ordinary inbox row under test — so the hermetic default unit lane is its behaviour-preserving
classification.

Measured at pair code base `67c91534` (which already carries `260831-LOCR-L06`'s landed row) **plus**
this change set, by diffing the disk file list against the manifest and by bracket position: **216**
`mcp/tests/test_*.py` modules on disk and **216** manifest entries, every module listed exactly once
and no path duplicated — unit-regression **123** entries (key `:5`, rows 6-128, next key `:130`),
public-contract 2 (key `:130`, rows 131-132), integration **62** (key `:134`, rows 135-196),
architecture-fitness 16 (key `:198`, rows 199-214), provider-conformance 13 (key `:216`, rows 217-229),
with stress-durability (`:231`) and migration (`:233`) empty. The population is closed and the
fail-closed load holds: the live test-module derivation and the manifest agree module for module, so
no unregistered module can make `load_lane_manifest` refuse. No existing row changed lane and no case
budget was raised; the declared case budgets live in `pyproject.toml`, which is the authority for
them. The insertion sits inside the alphabetical unit-regression run and above every row this card
cites from `LOCR-R09@v1`, `LOCR-R11@v1`, `LOCR-R18@v1`, the L17 observer-health proof and the L06
reviewer-relay proof, so those classifications are untouched by this leaf — it moves the later lane
keys and the rows at or below `:105`, which is why every affected citation in this card and in
`overview.md` was re-derived against the candidate rather than carried.

Scope note: this leaf is a **preservation leaf** — `mcp/src` is byte-unchanged by it (`git status
--porcelain` = ` M mcp/tests/test-evidence-lanes.toml` plus the untracked module; `mcp/src` diff = 0
files), and the module's digest, line count and lane ordinal are measurements of an uncommitted,
unaccepted tree. Classification only: lane membership is not execution, certification or acceptance
evidence, and the verification stamps remain closeout-owned.
## 260831-LOCR-L04 Lane Row (Declared)

The L04 change set adds `mcp/tests/test_serving_notifier_handoff.py` **and** its row in the same change,
so the manifest stays closed in that change set — the population at base `e9678c56` alone was 214 modules
and 214 manifest entries (L17's own row already landed there at `:122`), and this is the one addition. The
row is `mcp/tests/test-evidence-lanes.toml:97`, in the **unit-regression** lane, immediately below
`test_semantic_topology_refusals.py` at `:96` and above `test_serving_observation_loop.py` at `:98`. The
module enters the real `_serving_lifespan` under a deadline-correct virtual clock and drives the real
observation loop, the real sweeper, the real catalog commit boundary and the real notifier sweep — it
issues no HTTP request, starts no server and starts no process, and publishes nothing outside a
disposable `tempfile` case root — so the hermetic default unit lane is its behaviour-preserving
classification.

The leaf's two **support** modules, `mcp/tests/_handoff_clock.py` and `mcp/tests/_serving_handoff.py`, take
no lane row: the manifest classifies `test_*.py` modules, and this is the same treatment the directory's
other support modules receive (`_store_durability.py`, `_quality_admission.py`, `_control_plane.py` and
their siblings are absent from the manifest by the same rule). Their onboarding is the pair of file cards
created with this row.

Measured at base `e9678c56` **plus** this change set, by diffing the disk file list against the manifest
and by bracket position: **215** `mcp/tests/test_*.py` modules on disk and **215** manifest entries —
unit-regression **122** entries (key `:5`, rows 6-127, next key `:129`), public-contract 2 (key `:129`,
rows 130-131), integration **62** (key `:133`, rows 134-195), architecture-fitness 16 (key `:197`, rows
198-213), provider-conformance 13 (key `:215`, rows 216-228), with stress-durability (`:230`) and
migration (`:232`) empty. No existing row changed lane and no case budget was raised or is quoted here:
`pyproject.toml` is the authority for the declared budgets, and this leaf adds no collected case to any
capped population.

**This insertion is above the previously-latest unit rows, so it moves rows rather than sitting below
them.** Every manifest line at or after `:97` shifts by one: `test_serving_observation_loop.py` `:97` →
`:98`, `test_serving_startup_prime.py` `:98` → `:99`, L17's `test_terminal_observer_health.py` `:122` →
`:123`, and every later lane key with them. The citations into the manifest were therefore **re-derived
against the current file rather than carried**: 59 live citations across this card, the tests route
overview and fifteen sibling cards were re-pointed to the line that actually carries their anchor, and
the dated `## KS-R15@v1 Lane Registrations

The leaf's two new modules are registered here: the unit module `mcp/tests/test_review_assessments.py`
in the **unit-regression** lane, and the integration module
`mcp/tests/test_curator_review_assessment_publication.py` in the **integration** lane. Both rows were
inserted at the head of their lane's list, which is why **every cited row number below the insertion
points in this card moved** — the offsets are +1 for rows after the unit insertion and the integration
insertion, and the card's own reference rows were re-derived from the current file while re-reading it
rather than left at their pre-leaf coordinates.

Every other lane row in this card that cites this file was re-pointed in the same pass, because the
regenerated table below would otherwise describe a file that no longer exists in that shape. No lane
was added, removed, renamed or re-classified: the leaf registers two modules in the lanes their
behaviour already belongs to.




- 2026-09-18T17:02+02:00 — 260918-TSIP-L4 curator (uncommitted change set on `ar/260918-tsip-l4-ar`, base `0dd04d6a`): two rows added (`:165`, `:244`), 267 → 269 lines, and the citations the insertion moved re-derived by enumeration rather than from the finding set. Verification metadata stays at the recorded verification because the candidate is uncommitted and the governed closeout owns the real code commit; `lastUpdated` advances with this body edit.

- 2026-09-17T10:45+02:00 — 260915-CAPS-L15 curator: the manifest gained one row for this leaf's own new
  module, `mcp/tests/test_capsule_launch_wiring.py`, at `:19` in the **unit-regression** lane — its
  behaviour-preserving lane, since the module drives the launch points, the real runner preparation and
  the real adapter factory in process with the vendor boundary recorded and no real process started. A
  declared section records the row, its insertion point and the D9 rule it satisfies in the same change
  that adds the module. No row was removed, moved between lanes, or added to a capped population beyond
  the one module's own. Verification metadata moves to this leaf's base `15fa0e2c`; the candidate is
  deliberately uncommitted, so the governed closeout stamps the real code commit and no hash or
  fingerprint was invented here.

- 2026-09-17T10:43+02:00 — 260915-CAPS-L17 curator: the manifest gained one row for this leaf's own new
  module, `mcp/tests/test_eve_effort_runtime.py`, at `:173` in the **integration** lane — its
  behaviour-preserving lane, since each case starts the real runtime process with a complete verified
  capsule binding and reads the body a live recording provider received. A declared section records the
  row, its insertion point, the measured population at this change set (**240** modules on disk, **234**
  declared rows, no stale row, the same six pre-existing D9 modules unregistered, this leaf closing none
  of that gap) and the D27 note that one of those six is also the environment-sensitive registry case —
  carried with its confirmed `AR_EVE_NODE` trigger and its repair direction, **not repaired here**. No
  row was removed, moved between lanes, or added to a capped population beyond this module's own.
  **Checker result (post-sync, verbatim).** The refusal this entry first recorded was resolved by the
  leaf's `worktree_sync`: the pair is now `leaf-candidate` / `acceptanceEligible:true` on code base
  `d8ed8c21`, and the contract-scoped `memory_quality_check` ran against this worktree. Headline:
  `ok:false`, `checklistStatus:"action-required"`,
  `coherenceStatus:"not-evaluated-quality-action-required"`, `closeoutReady:false`,
  `curatorActionableCount:1690`; census `ready-for-adjudication` (13 rows, 0 blockers, 0 unonboarded).
  This card's own contribution: one `onboarding_drift_drifted` finding and two
  `style.update_history.history_order` "not newest-first" findings, attributable to the future-dated
  `10:45` stamp on the L15 entry below this one (same reasoning as the `serving/overview.md` entry). The
  population figures in this section were also derived directly from the manifest and the disk file
  list, independently of the checker. Verification metadata moves to the synced base `d8ed8c21`; the
  candidate is deliberately uncommitted, so the governed closeout stamps the real code commit and no
  hash or fingerprint was invented here.
Verification metadata moves to the synced base `d8ed8c21`; the candidate is deliberately uncommitted, so
the governed closeout stamps the real code commit and no hash or fingerprint was invented here.

the dated `## Update History
- 2026-09-30T12:56:40+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db` plus the staged delta; first curated over `b54d1b03`, then merged with L29's landed curation after the sync onto code `ce459423` / memory `a6075c76`, L29's committed lines kept byte-identical): **body updated for MIK-R14.** New top section "260928-MIK-L14 One Lane Row — The Reconsideration Cases" (the `unit-regression` row, at `:126` before the sync and `:127` after it, after L10's). Every later row moved down by one line; the rows behind the 59 findings the installed fixer declined were re-pointed by that exact shift (each row byte-identical to memory HEAD, anchors checked in the base and shifted ranges), and the fixer projected the rest. The earlier sections' prose line numbers are those of their own time. One row added. No verification stamp was advanced. **After the sync:** L29's lane row at `:108` moved this leaf's row to `:127` (L10's to `:126`); L29's top section and this leaf's are both kept, this leaf's above, and the rows L29 had also re-pointed were taken from L29's text and re-pointed by the exact line shift from `ce459423` to the staged tree.
- 2026-09-30T12:15:39+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`; review R3 and post-sync pass-with-notes): **body updated for MIK-R29.** Added the section "260928-MIK-L29 One Lane Row — The Knowledge Reader Cases" as the current account (`:108`), with one row. The installed fixer re-pointed the displaced rows it could (its bullets are in this card's generated list); the rows it declined were re-pointed by the exact one-line shift below `:108`. Rows inside committed history entries were not edited. No verification stamp was advanced: the source is staged and uncommitted, and closeout owns the stamp.
- 2026-09-30T05:58:11+02:00 — 260928-MIK-L05 curator (uncommitted change set on `ar/260928-mik-l05`, code base `31d761a241055d67b85ef3908033856b78a86a57` plus the staged and unstaged delta): **body updated for MIK-R05.** Added the section "260928-MIK-L05 One Lane Row — The Route-Chain Cases" (`:110`) at the top as the current account. The rows citing lines after `:109` were re-pointed by the exact +1 shift where the installed fixer declined them (each re-pointed row was byte-identical to memory HEAD, and its anchors were checked in the base ranges before the shift); the rest were projected by the installed fixer.
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): **body updated for MIK-R10.** Added the section "260928-MIK-L10 One Lane Row — The Unexplained-Change Cases" at the top as the current account (`:124`, after L25's `:123`), one row. Rows citing later lane rows (+1 from `:124`) were re-pointed by the installed fixer or, where it declined, by the exact line shift over rows byte-identical to memory HEAD. No verification stamp was advanced.
- 2026-09-30T04:01:40+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): **body updated for MIK-R25.** Added the section "260928-MIK-L25 Two Lane Rows — The Reviewer On Git Trees And The Archive Hook" (`:122`, `:123`) at the top as the current account. The two-line insertion moved every later row: the installed `memory-citations --fix` re-pointed the single-anchor rows (its generated bullets are kept, since no claim was reworded), and the rows it declined were re-pointed by the exact base-to-staged line shift. No verification stamp was advanced.
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): **body updated for MIK-R13.** Added the section "260928-MIK-L13 One Lane Row — The Decision-Record Cases" (`:121`) at the top as the current account. The one-line insertion moved every later row: the installed `memory-citations --fix` re-pointed the single-anchor rows (its generated bullets are kept, since no claim was reworded), and the multi-anchor rows it declined were re-pointed by the exact base-to-staged line shift. No verification stamp was advanced.
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): **body updated for MIK-R01.** Added the section "260928-MIK-L01 One Lane Row — The Leaf-Read Cases" (`:109`) at the top as the current account. The rows citing lines after `:108` were re-pointed by the exact +1 shift (each re-pointed row was byte-identical to memory HEAD, and its anchors were checked to lie in the base ranges before the shift); the rest were projected by the installed fixer.
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): **body updated for MIK-R06.** Added the section "260928-MIK-L06 One Lane Row — The Family Route Condition Cases" (the `unit-regression` row at `:69`). The one-line insertion moved every later row; the flagged multi-anchor rows in this card were re-pointed by the exact +1 shift for lines at or after `:69`, each checked to hold its anchors, and the rest by the installed fixer. No verification stamp was advanced.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): Added the section "260928-MIK-L11 One Lane Row — The Planned-Effects Cases" at the top as the current account: `test_planned_knowledge_effects.py` at `:118`, after L30's onboarding-trace row. Rows below `:118` moved down by one line; their citations were re-pointed by the installed fixer or the exact line map. Earlier sections' prose line hints are left as of their own time.
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): Added the section "260928-MIK-L02 One Lane Row — The Paging Cases" (`:107`) at the top as the current account. Every later row moved down one line; the rows citing them are re-pointed by the installed fixer or the exact base-to-staged line map, with no wording change. No verification stamp was advanced.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): Added the section "260928-MIK-L30 One Lane Row — The Onboarding Trace Gate Cases" (`:116`) at the top as the current account. Every later row moved down one line; the rows citing them were re-pointed by the installed fixer or the exact base-to-working line map, with no wording change. No verification stamp was advanced.
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): Added the section "260928-MIK-L03 One Lane Row — The Currentness Cases" (`:112`) at the top as the current account. Every later row moved down one line; the rows citing them were re-pointed by the installed fixer or the exact line map.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): Added the section "260928-MIK-L08 Two Lane Rows — The Change-To-Knowledge Worklist Cases" (`:113`, `:114`), at the top as the current account.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): Added the section "260928-MIK-L28 One Lane Row — The First-Class Test Proof Cases" (`:112`) at the top as the current account. One cited row. The inserted row moved every later row down by one line; the citation rows were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map, and no claim wording changed there. No verification stamp was advanced.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): New section: "260928-MIK-L24 Three Lane Rows" (`:108-110`), with its row. The L12 section now notes that its two rows are split, with the writer at `:107` and the anchor-content row at `:111`. The three-line shift of every later row was re-pointed by the installed fixer and, for the multi-anchor rows it declined, by the exact base-to-working line map, with no wording change.
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): **body update — the curator writer's two case modules join `unit-regression`.** New section "260928-MIK-L12 Two Lane Rows" with its row (`:106-109`). The L20, L04 and L23 sections cite rows above the insertion and were re-read; their wording is retained. The rows below the insertion that the two-line shift moved were re-pointed by the installed anchor-range projection (its generated lines sit under the later `## Update History`) and the multi-anchor rows it declined by exact base-to-working line mapping, then confirmed by a per-document `memory-citations` check with 0 findings. Earlier accounts' prose line counts are history. No verification stamp was advanced.
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): **body update — the migration census's two case modules join `unit-regression`.** New section "260928-MIK-L20 Two Lane Rows" with its row (`:101-104`). The L23 section's claim that its three rows sit "directly after L22's two validator rows, at `:101-103`" is no longer true: its prose was reworded to say the rows now follow L20's census rows at `:104-106`, and its row was re-derived to name the census row they follow (`:103-106`). The L22 section's row (`:99-101`) and the L04, L07 and L21 rows above the insertion were re-read and still state the true order, so their wording is retained. Every later-row citation on this card was re-pointed by the exact two-line shift (no content impact on those rows). Earlier accounts' prose line counts (for example L04's "`:102-104`") are history. No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **body update — the family route case module joins `unit-regression`.** The L21 section's claim that its two rows follow `test_knowledge_citation_bindings.py` is no longer true as written: its prose and row were reworded to name the family-routes row now between them and re-cited to `:95-98`; the fixer's same-pass "claim bytes unchanged" bullet for that row was removed and folded into this entry. Because the one-line insertion sits inside the `unit-regression` list these rows quote, the L07, L22 and L23 section rows (`:98-99`, `:99-101`, `:101-104`) were also re-read against the working tree: each still states the true order (history files after the file formats; the two validator rows after the history files; the three index rows after the validator routes), so their wording is retained. The fixer's three same-pass "claim bytes unchanged" bullets for them were removed and folded into this entry. New section "260928-MIK-L04 One Lane Row" with its row (`:95-97`); it records that the one-line insertion moves L22's and L23's rows to `:100-101` and `:102-104`. Every later-row citation on this card was re-pointed by the exact one-line shift (no content impact on those rows). No verification stamp was advanced.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): **body update — the derived knowledge index's three case modules join `unit-regression`.** Added the section above for the three rows (`:101-103`) and re-pointed the rows below them that the three-line shift moved (the installed anchor-range projection, whose generated lines sit under the trailing `## Update History`, plus the multi-anchor rows it declined, re-pointed by exact base-to-working line mapping and then confirmed by a per-document `memory-citations` check with 0 findings). Earlier accounts' prose line counts are history. No verification stamp was advanced.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): **body update — the knowledge validator's two case modules join `unit-regression`.** Added the section above for the two rows (`:99-100`) and re-pointed the rows below them that the two-line shift moved (the installed anchor-range projection, whose generated lines sit under the trailing `## Update History`, plus the multi-anchor rows it declined, each shifted by exactly two lines and then confirmed by a per-document `memory-citations` check with 0 findings). Earlier accounts' prose line counts are history. No verification stamp was advanced.
- 2026-09-29T06:00:00+02:00 — 260928-MIK-L07 curator (uncommitted change set on `ar/260928-mik-l07`, code base `45fe37749b388de348d16ced50c28c03490dce64` plus the working-tree delta): **body update — the history-file case module joins `unit-regression`.** Added the section above for the new row (`:98`) and re-pointed the rows below it that the one-line shift moved (the installed anchor-range projection, whose generated lines sit under the trailing `## Update History`, plus 29 multi-anchor rows shifted by exactly one line where every anchor then resolved in the current file). Earlier accounts' prose line counts are history. No verification stamp was advanced.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): **body update — the text knowledge format's two case modules join `unit-regression`.** Added the section above for the two rows (`:96-97`) and re-pointed the rows below them that the two-line shift moved (the anchor-range projection plus 29 multi-anchor rows re-measured by hand against the cited file: each anchor now cites the one line of the manifest that holds it). Earlier accounts' prose line counts are history. No verification stamp was advanced.
- 2026-09-28T18:18:00+02:00 — 260921-ICR-L47 curator (post-sync re-measure after the Architect's `worktree_sync` onto code `eda947325ccbe0791973953265278597e968a34a` / memory `6ccb9b615e383174c22f110a6492e6231a4e261f`; L47 candidate tree `5f22717e68041d6819e9671cee2ab30e4d3d3e13`): No content impact: citation ranges into files L44, L45 or L47 moved (`mcp/tests/test-evidence-lanes.toml`) were re-measured against the post-sync code; each re-pointed row held its anchors in its own measurement tree (`eda94732` or the pre-sync L47 candidate `72efa4bb`) and holds them after the line mapping, or names a literal that occurs exactly once in the post-sync file within five lines of its cited place. Claim wording unchanged. No stamp advanced.
- 2026-09-28T17:13:48+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): **body update — one new unit-regression row for `test_review_intent_summary.py` (`ICR-R24@v3`).** New section and row. Every row below line 181 that this insertion displaced and that was valid at base was re-pointed from the base-to-candidate line mapping (a one-line shift). No claim reworded. No stamp advanced.

- 2026-09-27T05:43:38+00:00 — Curator-authored re-citation of 28 investigated L41 source-linked claim(s). Each named registration or declaration was selected individually after the composite guarded projection declined. Prior explanation, refusal evidence, generated history and real verification stamps are preserved.

- 2026-09-27T04:58:33+00:00 — Added the two scoped history regression modules to the onboarding account without changing other lane policy. Verification hashes/dates remain closeout-owned.

- 2026-09-27T00:34:45Z — L39: No content impact: resolved the affected registry/instruction/overview reference rows against their exact current named anchors after the scoped source changes. Existing factual meaning, verification stamps and earlier history are preserved.


- 2026-09-26T23:48:33Z — L39: Recorded the new family-retention test module in its existing unit-regression lane; no lane owner or policy change. Existing registry history is preserved.

- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — The evidence registry includes test_curator_candidate_progression.py, test_curator_scope.py, test_review_recorded_knowledge.py and test_review_unchanged_knowledge.py in the existing unit-regression lane. No lane rule, population exclusion or quality threshold changes.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **body update — the extracted sibling's lane row (D54).** `test_curator_ingest_write_and_retention.py` joins the `unit-regression` list beside its parent, which shifts the lines of the rows below it in this file — the same movement this card's citation pass re-anchored. **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
` entries — as-of records of earlier candidates — were deliberately left as
written. One citation was corrected beyond the shift because it was already stale before this leaf
(`test_checkpoint_landing_end_to_end.py`, cited at `:143-143`, which the manifest carries at `:140`).
Classification only: lane membership is not execution, certification or acceptance evidence, and the
verification stamps remain closeout-owned.

The leaf is a **preservation** requirement — `LOCR-R04@v1` requires zero production change — so the
manifest's only movement is this one row; `mcp/src` is byte-unchanged by the change set.

## 260831-LOCR-L07 Lane Row (Declared)

The L07 change set adds `mcp/tests/test_state_signal_curator_wake.py` **and** its row in the same
change, so the manifest stays closed in that change set — the population at base `e9678c56` alone is
214 modules and 214 manifest entries, and this is the one addition. The row is
`mcp/tests/test-evidence-lanes.toml:102`, in the **unit-regression** lane, immediately below
`test_state_signal_boundary_delivery.py` at `:101` and above `test_state_signal_relay.py` at `:103`,
so the state-signal siblings stay one contiguous alphabetical run. The module drives the real
`TerminalCatalogLivenessSweeper`, the real agent-notifier sweep and the real `run_agent_notifier_sweep`
entry point over temporary catalogs, an in-process tmux host and an accepting paster double — it
issues no HTTP request, starts no server and starts no process — so the hermetic default unit lane is
its behaviour-preserving classification, the same lane its three siblings already hold for the same
reason. This is a preservation leaf: `mcp/src` is unchanged by the change set, and the row is
registration only.

Measured at base `e9678c56` **plus** this change set, by diffing the disk file list against the
manifest and by bracket position: **215** `mcp/tests/test_*.py` modules on disk and **215** manifest
entries — unit-regression **122** entries (key `:5`, bracket `:5-127`), public-contract 2 (key
`:129`, rows 130-131), integration **62** (key `:133`, bracket `:134-195`), architecture-fitness 16
(key `:197`, rows 198-213), provider-conformance 13 (key `:215`, rows 216-228), with
stress-durability (`:230`) and migration (`:232`) empty. No existing row changed lane and no case
budget was raised; `pyproject.toml` remains the authority for the pinned budgets. The insertion sits
inside the alphabetical unit-regression run above every later lane key, so it moves the later lane
keys and every row this card cites from `:102` down by one, while every row at `:101` and above is
unchanged — including `test_serving_observation_loop.py` (`:97`) and
`test_serving_startup_prime.py` (`:98`), so `LOCR-R11@v1`'s and `LOCR-R18@v1`'s classifications are
untouched by this leaf. Classification only: lane membership is not execution, certification or
acceptance evidence, and the verification stamps remain closeout-owned.

## Current verification scope

The reviewer operation and copied-index capture modules have explicit unit-regression lane rows. The existing serving integration row remains unchanged; no runtime boundary test is relabelled by curation.

## Current preview-proof registration

The registered public preview module is an integration-lane operation, alongside the two preserved L40 unit-regression rows. Curation does not move the public boundary into a helper-only lane or infer certification from the declaration.

## Code Commentary

### Logic

The existing unit-regression lane registers `test_review_assessment_history.py` and `test_review_assessment_history_repairs.py`. They exercise public owner capture/history and the four sealed namespace, alias, channel-provenance and recovery-loss boundaries. The catalogue remains a declaration of the existing lane; no new execution authority or budget is introduced.

The evidence registry includes test_curator_candidate_progression.py, test_curator_scope.py, test_review_recorded_knowledge.py and test_review_unchanged_knowledge.py in the existing unit-regression lane. No lane rule, population exclusion or quality threshold changes.

Paths are explicit and unique. The root conftest reads integration/stress membership once to avoid
integration imports in default unit runs and marks selected integration items. The
`test_terminal_evidence_cursors.py` row owns the focused deque-envelope, unsupported-harness,
bounded-Pi, and liveness-containment checks for the terminal-evidence lift. Other categories
retain their classification meaning without requiring separate copies or historical edge suites.
A test-shaped helper module may remain listed for dependency classification even when it contains
no test functions; importability is not a passing test.

`load_lane_manifest` independently proves the declared population closed: it derives the
repository's actual test modules and refuses a manifest that omits a module or declares a stale
row, so an unregistered module is a hard load failure rather than a silent gap. Three modules
created by the CCR transaction-only closeout reform (`test_review_state.py`,
`test_task_doc_review_public.py`, `test_transaction_only_worktree_delivery.py`) were left
unregistered by the commit that created them, and the checking hooks that would have caught the
omission were later removed from closeout, so the gap survived until the manifest was explicitly
repaired. All three are registered as `unit-regression`, which is behaviour-preserving: they had
been running unmarked and therefore already counted as unit, and the integration lane sat at its
hard cap of 150 collected cases, so an `integration` row would have overflowed the cap and raised
during collection. Registration here is classification only; it is never execution or acceptance
evidence.

`test_dagger_registry_lock.py`, the registered activation/admission proof, the registered
route-review transport proof, and actual document/publication/durability boundaries are integration
members. The R28 `test_terminal_liveness_deferred_work.py` module is a unit-regression member: it is
hermetic (temporary catalogs, in-process `unittest` classes, no `worktree_services` use) even though
it exercises the real catalog/sweeper post-commit ordering and failure boundaries. The new diagnostic
quality, selected-case-budget and canonical terminal-evidence mapping tests are unit-regression members,
as is `test_sync_parked_candidate.py`. Three pre-existing CCR modules (`test_review_state.py`,
`test_task_doc_review_public.py`, `test_transaction_only_worktree_delivery.py`) were created by `8885939e`
in the same change that edited this manifest, but their required rows were omitted; the missing
`unit-regression` rows were restored so the manifest loads and no retained module stays unclassified.
A full run previously collected all three unmarked, so `unit-regression` is their behaviour-preserving
lane. Adding the parked-candidate row shifted every later lane block, so its citations were re-derived.
The executable case budgets live in pyproject/conftest, not in this list. Coverage percentages are
diagnostic and cannot require restoring deleted entries.

The current manifest is complete and duplicate-free: every `mcp/tests/test_*.py` module on disk is
listed exactly once, and every listed path exists. Three formerly unlisted modules
(`test_review_state.py`, `test_task_doc_review_public.py`, `test_transaction_only_worktree_delivery.py`)
were created by the CCR transaction-only delivery commit and omitted from this manifest in the same
change; they ran unmarked rather than in an explicit lane. They are registered in `unit-regression`,
which is the behaviour-preserving lane for an unmarked module, because moving them to `integration`
would push that lane past its 150-case cap. The same three rows also reached this series branch with
the LOCR-L28 landing. That repair is repo-hygiene and is not part of any LOCR requirement.

`test_cross_master_concurrency.py` (260831-LOCR-L36) is an **integration** member, and that is its
behaviour-preserving lane: it builds one real temporary Git world per case — disposable code and
external-memory repositories, real series/leaf contracts, a real ledger — and drives the public
activation, checkpoint-landing and integration operations against it, so it is a boundary executor
rather than a hermetic unit. It is the forcing module for the contract-scoped activation record: two
atomic masters commanded by one sprint share one protected source pair, so the module can prove both
progress independently and that a sibling's pause blocks nobody. Registration is classification only;
it is never execution or acceptance evidence.

`test_terminal_liveness_registration_order.py` (260831-LOCR-L23) is a **unit-regression** member, and
that is its behaviour-preserving lane: it drives the real `TerminalCatalog` over `tempfile` catalogs
and the real `TerminalCatalogLivenessSweeper.refresh` with in-process `unittest` doubles for the
registrar and the compactor, so it is hermetic — no `worktree_services`, no real repository, no
provider — despite exercising the catalog batch, the terminated-row read and the retention predicate.
It is registered at entry row 118, immediately after its sibling
`test_terminal_liveness_deferred_work.py` at `:117`, which holds the same lane for the same reason.
Registration is classification only; it is never execution or acceptance evidence.

### Invariants And Boundaries

- Unknown, duplicate or conflicting file classification must not silently acquire authority.
- Every current `mcp/tests/test_*.py` module holds exactly one explicit lane; an unlisted module is a
  manifest defect, and its behaviour-preserving lane is the default unit lane rather than the capped
  integration lane.
- Evidence class is separate from whether a test invokes a real external producer.
- Current source membership governs; old final-Codex executor/status-wait/deleted-edge lists do not.
- Host development pytest is supported; only explicit certification requires Dagger admission.
- Lane membership is additionally bounded by the declared collected-case budgets (`unit_case_budget` 1000 at `pyproject.toml:185`, `integration_case_budget` **300** at `pyproject.toml:186`; the 150, 200 and 250 values in earlier entries of this card are stale). **That pair is a historical reading of this card's own, retained as the state it measured; the pair the file declares now is `unit_case_budget = 4000` at `pyproject.toml:278` and `integration_case_budget = 1000` at `pyproject.toml:279`.** A module that was previously running unmarked already spends unit budget, so registering it as `unit-regression` preserves behaviour; moving it into `integration` can push full-suite collection past the integration cap and fail collection outright. Classification cannot be chosen for semantic tidiness alone.
- Full suites and whole-candidate review occur at master completion, not once for every lane or leaf.
- Lane membership must keep each collected population inside its declared case budget: `unit_case_budget` 1000 and `integration_case_budget` **300** (root `pyproject.toml:185-186`) **at that earlier candidate** — the file now declares `unit_case_budget = 4000` (`pyproject.toml:278`) and `integration_case_budget = 1000` (`pyproject.toml:279`) — enforced in `pytest_collection_finish`. A module that a full run previously collected unmarked - and therefore already counted as unit - belongs in `unit-regression`; moving it to `integration` can refuse collection.

- Lane membership is additionally bounded by the declared collected-case budgets (`unit_case_budget` 1500, `integration_case_budget` 250 — `pyproject.toml:158-159`; the 150/200/1000 values in earlier entries of this card are stale) **as that candidate read them. The pair declared now is `unit_case_budget = 4000` (`pyproject.toml:278`) and `integration_case_budget = 1000` (`pyproject.toml:279`).** **The unit ceiling was raised from 1000 to 1500 by 260915-CAPS-L8, executing the developer's ruling**, because the default selection had outgrown 1000 and so refused collection before any case ran; the raise restored a working default selection and is a ceiling rather than a target. A module that was previously running unmarked already spends unit budget, so registering it as `unit-regression` preserves behaviour; moving it into `integration` can push full-suite collection past the integration cap and fail collection outright. Classification cannot be chosen for semantic tidiness alone.
- Lane membership is additionally bounded by the declared collected-case budgets (`unit_case_budget` 2000, `integration_case_budget` 300 — `pyproject.toml:168-176`; the 150/200/250/1000/1500 values in earlier entries of this card are stale). **Every figure in this card is measured against the leaf's base ceiling (2000/300); the merged line this leaf syncs onto raises both to 2300/400 (`T79`), so the two ceilings must not be quoted interchangeably.** **The unit ceiling was raised from 1000 to 1500 by 260915-CAPS-L8, executing the developer's ruling**, because the default selection had outgrown 1000 and so refused collection before any case ran; the raise restored a working default selection and is a ceiling rather than a target. A module that was previously running unmarked already spends unit budget, so registering it as `unit-regression` preserves behaviour; moving it into `integration` can push full-suite collection past the integration cap and fail collection outright. Classification cannot be chosen for semantic tidiness alone.
- Full suites and whole-candidate review occur at master completion, not once for every lane or leaf.
- Lane membership must keep each collected population inside its declared case budget: `unit_case_budget` 1000 and `integration_case_budget` **300** (root `pyproject.toml:185-186`) **at that earlier candidate** — the file now declares `unit_case_budget = 4000` (`pyproject.toml:278`) and `integration_case_budget = 1000` (`pyproject.toml:279`) — enforced in `pytest_collection_finish`. A module that a full run previously collected unmarked - and therefore already counted as unit - belongs in `unit-regression`; moving it to `integration` can refuse collection.

- Lane membership is additionally bounded by the declared collected-case budgets (`unit_case_budget` 1500, `integration_case_budget` 250 — `pyproject.toml:158-159`; the 150/200/1000 values in earlier entries of this card are stale) **as that candidate read them. The pair declared now is `unit_case_budget = 4000` (`pyproject.toml:278`) and `integration_case_budget = 1000` (`pyproject.toml:279`).** **The unit ceiling was raised from 1000 to 1500 by 260915-CAPS-L8, executing the developer's ruling**, because the default selection had outgrown 1000 and so refused collection before any case ran; the raise restored a working default selection and is a ceiling rather than a target. A module that was previously running unmarked already spends unit budget, so registering it as `unit-regression` preserves behaviour; moving it into `integration` can push full-suite collection past the integration cap and fail collection outright. Classification cannot be chosen for semantic tidiness alone.
- Full suites and whole-candidate review occur at master completion, not once for every lane or leaf.
- Lane membership must keep each collected population inside its declared case budget: `unit_case_budget` 1500 and `integration_case_budget` 250 (root `pyproject.toml:158-159`) **at that earlier candidate — the declaration now reads `unit_case_budget = 4000` (`pyproject.toml:278`) and `integration_case_budget = 1000` (`pyproject.toml:279`)**, enforced in `pytest_collection_finish`. A module that a full run previously collected unmarked - and therefore already counted as unit - belongs in `unit-regression`; moving it to `integration` can refuse collection.
- Lane membership is additionally bounded by the declared collected-case budgets (`unit_case_budget` 2000, `integration_case_budget` 300 — `pyproject.toml:168-176`; the 150/200/250/1000/1500 values in earlier entries of this card are stale) **as that candidate read them. The pair declared now is `unit_case_budget = 4000` (`pyproject.toml:278`) and `integration_case_budget = 1000` (`pyproject.toml:279`).**

## Evidence

### Docs References

No external Domain Documentation source is configured; these are repository-owned implementation facts.

### Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

- Retained unit-regression membership, including the R28 deferred-work and canonical terminal-evidence mapping proofs [62]
- Small actual integration file population [63]
- Retained structural detector classifications [64]
- Provider contract classifications [65]
- The registry retains separate stress-durability and migration lanes. [66]
- L38 registered public activation/admission and route-review transport ownership [67]
- The new parked-candidate suite is registered in the unit-regression lane. [68]
- The manifest still has no default classification for an unregistered test file. [69]
- LOCR-L09 boundary-delivery forcing module registered in the unit lane [70]
- The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. [71]
- The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 272 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). [72]
- The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 218 now, after the L4, L5, L7, L8 and L3 insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. [73]
- The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 230 now, after the L4, L5, L7, L8 and L3 insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. [74]
- The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 249 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). [75]
- The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row 289 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). [76]
- The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 243 now, after the L4, L5, L7, L8 and L3 insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. [77]
- The L4 producer-census suite is registered in the unit-regression lane by the commit that landed L4, closing the gap the L4 section recorded. [78]
- The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 240 now, after the L7, L8 and L3 insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. [79]
- The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 222 now, after the L8 and L3 insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. [80]
- The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 265 now, after the L3 insertion) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. [81]
- The L2 knowledge graph suite is registered in the unit-regression lane by the same change set that created it (entry rows 69-73) — all four modules are hermetic (temporary directories, in-process APSW databases, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. [82]
- The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 69) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. [83]
- The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 265 now, after the L3 insertion) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. [84]
- The L2 knowledge graph suite is registered in the unit-regression lane by the same change set that created it (entry rows 69-73) — all four modules are hermetic (temporary directories, in-process APSW databases, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. [85]
- The L3 candidate-batch pair and the label-operations suite are registered in the unit-regression lane by the same change set that created them (entry rows 18-19, and row 71 now after the L4 insertions) — all three are hermetic (temporary directories, in-process APSW databases driven through the real admitted destination, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. [86]
- The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (row 118 now, after the L4 insertions) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. [87]
- **The L4 snapshot pair is registered in the unit-regression lane by the same change set that created them (rows 69 and 75)** — both modules are hermetic: temporary directories under `tmp_path`, in-process APSW databases driven through the real admitted destination and the real publication lock, and a child interpreter used only as a crash probe, with no integration marker, no repository working tree and no network. [88]
- **The knowledge block's current membership across all four KS leaves**, whose insertion order is why the rows are not contiguous by leaf. [89]
- **The integration lane's collected-case cap that constrains lane choice, cited as the pinned key and value — raised to 400 by this master's owning seat at the `260915-KS-L24` candidate, not by this leaf's fix round, raised to **600** with its unit half to **3000** by `260918-TSIP-L7` on 2026-09-19, and to **1000** with its unit half to **4000** by `260918-TSIP-L13` on 2026-09-20 — which is what the declaration reads now.** [90]
- **The unit ceiling, cited as the pinned key and value — raised to 1500 at the `260915-KS-L24` candidate, again to 1600 by that candidate's owning seat, again to 2200 by the merge onto the moved super line, to 2300 by `260915-KS-L21`, to **3000** with its integration half to **600** by `260918-TSIP-L7`'s developer-ruled raise of the pair, and to **4000** with its integration half to **1000** by `260918-TSIP-L13`'s second developer ruling on 2026-09-20, because an over-budget population makes `pytest_collection_finish` raise `UsageError` and run no tests at all. Every earlier value is retained as the ruling that produced it.** [91]
- **The two lane rows this leaf registered in the same change, both in `integration` because the unit population sits exactly at its declared ceiling.** [92]
- The lane manifest is fail-closed: an unregistered tracked module makes loading refuse rather than classifying it by default. [93]
- Retained unit-regression membership, including the R28 deferred-work, canonical terminal-evidence mapping and L23 registration-order proofs [94]
- The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 272 now, after the L4, seal-removal, L5, L7, L8, L3, L01 and L17 insertions). [95]
- The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 218 now, after the L4, L5, L7, L8, L3 and L01 insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. [96]
- The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 230 now, after the L4, L5, L7, L8, L3 and L01 insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. [97]
- The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 249 now, after the L4, seal-removal, L5, L7, L8, L3 and L01 insertions). [98]
- The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row 289 now, after the L4, seal-removal, L5, L7, L8, L3 and L01 insertions). [99]
- The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 243 now, after the L4, L5, L7, L8, L3 and L01 insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. [100]
- The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 240 now, after the L7, L8, L3 and L01 insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. [101]
- The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 222 now, after the L8, L3 and L01 insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. [102]
- The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 265 now, after the L3 and L01 insertions) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. [103]
- The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 69) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. [104]
- The L23 registration-order proof is registered in the unit-regression lane by the same change set that created it (entry row 118) — it drives the real catalog and sweeper over `tempfile` files with in-process registrar/compactor doubles, so it is hermetic and the default unit lane is its behaviour-preserving classification. [105]
- The L27 pane-authority proof is registered in the integration lane by the same change set that created it — entry ordinal **53** of 61 in that lane; file line `:183` at base `52bee429` **plus** this change set (`:182` at that base alone, and `:181` at this candidate's own build base `b368b661`, which is the figure the leaf's verdict and worker report cite). It is hermetic but takes the lane of its sibling `test_terminal_liveness.py`, and a new module of this family needs a row or its application imports run inside ordinary unit collection. [106]
- The unit-regression bracket the L23 row sits inside, whose upper bound has moved with each later unit-lane insertion (L23, then L01, then L10). [107]
- The L01 steady-state observation suite is registered in the unit-regression lane by the same change set that created it (entry row 97) — it drives the real lifespan finalizer, the real sweeper and the real catalog under a virtual event-loop clock and issues no HTTP request, so the default unit lane is its behaviour-preserving classification. [108]
- The L18 startup-prime proof is registered in the unit-regression lane by the same change set that created it (entry row 98), immediately below its sibling and sharing that sibling's fixture — it drives the real lifespan over a temporary catalog under a virtual clock with no HTTP request and no process, so the default unit lane is its behaviour-preserving classification. [109]
- The unit-regression bracket at the L18 candidate measurement, whose upper bound moved with each later unit-lane insertion (L23, L01, L10, then L18). [110]
- The integration bracket at the L18 candidate measurement. [111]
- The L17 observer-health proof is registered in the unit-regression lane by the same change set that created it (entry row 122, immediately below `test_terminal_liveness_registration_order.py` at `:121`) — it drives the record, the writer, the accumulator and the real `_state_response` handler and `stream_events` generator against stub projectors with no HTTP transport and no server, so the default unit lane is its behaviour-preserving classification. The insertion sits below `test_serving_observation_loop.py` (`:97`) and `test_serving_startup_prime.py` (`:98`), so no earlier row moved. [112]
- The L06 reviewer-relay proof is registered in the unit-regression lane by the same change set that created it (entry row 68, immediately below `test_lifecycle_operation_model_helpers.py` at `:67` and above `test_memory_attribution_producers.py` at `:69`) — it drives the real observer, the production terminal-evidence lift and the real notifier sweep over a temporary coordination root with no HTTP request, no server and no process, so the default unit lane is its behaviour-preserving classification. Unlike the L17/L18 insertions this row lands inside the unit run above the rows this card cites, which is why every affected citation here was re-derived against the candidate. [113]
- The L05 worker turn owner wake module is registered in the unit-regression lane by the same change set that created it (entry row 105, immediately below `test_state_signal_restart_recovery.py` at `:104` and above `test_state_signal_structural_dispatch_recovery.py` at `:106`) — it seeds owned worker and manager seats on a real `TerminalCatalog`, drives the real `run_agent_notifier_sweep` over a temporary coordination root with real task documents and the real durable stores, issues no HTTP request, starts no server and starts no process, and asserts the whole inbox store rather than its state-signal subset, so the default unit lane is its behaviour-preserving classification. The insertion sits inside the unit run above the rows this card cites, which is why every affected citation here was re-derived against the candidate rather than carried. [114]
- The L17 observer-health proof is registered in the unit-regression lane by the same change set that created it (entry row 122, immediately below `test_terminal_liveness_registration_order.py` at `:121`) — it drives the record, the writer, the accumulator and the real `_state_response` handler and `stream_events` generator against stub projectors with no HTTP transport and no server, so the default unit lane is its behaviour-preserving classification. The insertion sits below `test_serving_observation_loop.py` (`:97`) and `test_serving_startup_prime.py` (`:98`), so no earlier row moved. [115]
- The L07 curator-wake proof is registered in the unit-regression lane by the same change set that created it (entry row 102), immediately below `test_state_signal_boundary_delivery.py` at `:101` and above `test_state_signal_relay.py` at `:103` — it drives the real liveness sweeper, the real agent-notifier sweep and the real `run_agent_notifier_sweep` over temporary catalogs and an in-process tmux host, with no HTTP request, no server and no process, so the default unit lane is its behaviour-preserving classification. [116]
- The registry retains separate stress-durability and migration lanes. [117]
- The registry retains separate stress-durability and migration lanes. [118]
- Small actual integration file population [119]
- Retained structural detector classifications [120]
- Provider contract classifications [121]
- L38 registered public activation/admission and route-review transport ownership [122]
- The new parked-candidate suite is registered in the unit-regression lane. [123]
- The manifest still has no default classification for an unregistered test file. [124]
- LOCR-L09 boundary-delivery forcing module registered in the unit lane [125]
- The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. [126]
- The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 272 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). [127]
- The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 218 now, after the L4, L5, L7, L8 and L3 insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. [128]
- The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 230 now, after the L4, L5, L7, L8 and L3 insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. [129]
- The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 249 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). [130]
- The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row 289 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). [131]
- The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 243 now, after the L4, L5, L7, L8 and L3 insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. [132]
- The L4 producer-census suite is registered in the unit-regression lane by the commit that landed L4, closing the gap the L4 section recorded. [133]
- The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 240 now, after the L7, L8 and L3 insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. [134]
- The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 222 now, after the L8 and L3 insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. [135]
- The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 265 now, after the L3 insertion) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. [136]
- The L2 knowledge graph suite is registered in the unit-regression lane by the same change set that created it (entry rows 69-73) — all four modules are hermetic (temporary directories, in-process APSW databases, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. [137]
- The L3 candidate-batch pair and the label-operations suite are registered in the unit-regression lane by the same change set that created them (entry rows 18-19, and row 71 now after the L4 insertions) — all three are hermetic (temporary directories, in-process APSW databases driven through the real admitted destination, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. [138]
- The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (row 118 now, after the L4 insertions) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. [139]
- **The L4 snapshot pair is registered in the unit-regression lane by the same change set that created them (rows 69 and 75)** — both modules are hermetic: temporary directories under `tmp_path`, in-process APSW databases driven through the real admitted destination and the real publication lock, and a child interpreter used only as a crash probe, with no integration marker, no repository working tree and no network. [140]
- **The knowledge block's current membership across all four KS leaves**, whose insertion order is why the rows are not contiguous by leaf. [141]
- **The integration lane's collected-case cap that constrains lane choice, cited as the pinned key and value — raised to 400 by this master's owning seat at the `260915-KS-L24` candidate, not by this leaf's fix round, raised to **600** with its unit half to **3000** by `260918-TSIP-L7` on 2026-09-19, and to **1000** with its unit half to **4000** by `260918-TSIP-L13` on 2026-09-20 — which is what the declaration reads now.** [142]
- **The unit ceiling, cited as the pinned key and value — raised to 1500 at the `260915-KS-L24` candidate, again to 1600 by that candidate's owning seat, again to 2200 by the merge onto the moved super line, to 2300 by `260915-KS-L21`, to **3000** with its integration half to **600** by `260918-TSIP-L7`'s developer-ruled raise of the pair, and to **4000** with its integration half to **1000** by `260918-TSIP-L13`'s second developer ruling on 2026-09-20, because an over-budget population makes `pytest_collection_finish` raise `UsageError` and run no tests at all. Every earlier value is retained as the ruling that produced it.** [143]
- **The two lane rows this leaf registered in the same change, both in `integration` because the unit population sits exactly at its declared ceiling.** [144]
- The lane manifest is fail-closed: an unregistered tracked module makes loading refuse rather than classifying it by default. [145]
- Retained unit-regression membership, including the R28 deferred-work, canonical terminal-evidence mapping and L23 registration-order proofs [146]
- The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 272 now, after the L4, seal-removal, L5, L7, L8, L3, L01 and L17 insertions). [147]
- The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 218 now, after the L4, L5, L7, L8, L3 and L01 insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. [148]
- The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 230 now, after the L4, L5, L7, L8, L3 and L01 insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. [149]
- The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 249 now, after the L4, seal-removal, L5, L7, L8, L3 and L01 insertions). [150]
- The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row 289 now, after the L4, seal-removal, L5, L7, L8, L3 and L01 insertions). [151]
- The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 243 now, after the L4, L5, L7, L8, L3 and L01 insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. [152]
- The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 240 now, after the L7, L8, L3 and L01 insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. [153]
- The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 222 now, after the L8, L3 and L01 insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. [154]
- The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 265 now, after the L3 and L01 insertions) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. [155]
- The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 69) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. [156]
- The L23 registration-order proof is registered in the unit-regression lane by the same change set that created it (entry row 118) — it drives the real catalog and sweeper over `tempfile` files with in-process registrar/compactor doubles, so it is hermetic and the default unit lane is its behaviour-preserving classification. [157]
- The L27 pane-authority proof is registered in the integration lane by the same change set that created it — entry ordinal **53** of 61 in that lane; file line `:183` at base `52bee429` **plus** this change set (`:182` at that base alone, and `:181` at this candidate's own build base `b368b661`, which is the figure the leaf's verdict and worker report cite). It is hermetic but takes the lane of its sibling `test_terminal_liveness.py`, and a new module of this family needs a row or its application imports run inside ordinary unit collection. [158]
- The unit-regression bracket the L23 row sits inside, whose upper bound has moved with each later unit-lane insertion (L23, then L01, then L10). [159]
- The L01 steady-state observation suite is registered in the unit-regression lane by the same change set that created it (entry row 97) — it drives the real lifespan finalizer, the real sweeper and the real catalog under a virtual event-loop clock and issues no HTTP request, so the default unit lane is its behaviour-preserving classification. [160]
- The L18 startup-prime proof is registered in the unit-regression lane by the same change set that created it (entry row 98), immediately below its sibling and sharing that sibling's fixture — it drives the real lifespan over a temporary catalog under a virtual clock with no HTTP request and no process, so the default unit lane is its behaviour-preserving classification. [161]
- The unit-regression bracket at the L18 candidate measurement, whose upper bound moved with each later unit-lane insertion (L23, L01, L10, then L18). [162]
- The integration bracket at the L18 candidate measurement. [163]
- The L17 observer-health proof is registered in the unit-regression lane by the same change set that created it (entry row 122, immediately below `test_terminal_liveness_registration_order.py` at `:121`) — it drives the record, the writer, the accumulator and the real `_state_response` handler and `stream_events` generator against stub projectors with no HTTP transport and no server, so the default unit lane is its behaviour-preserving classification. The insertion sits below `test_serving_observation_loop.py` (`:97`) and `test_serving_startup_prime.py` (`:98`), so no earlier row moved. [164]
- The L06 reviewer-relay proof is registered in the unit-regression lane by the same change set that created it (entry row 68, immediately below `test_lifecycle_operation_model_helpers.py` at `:67` and above `test_memory_attribution_producers.py` at `:69`) — it drives the real observer, the production terminal-evidence lift and the real notifier sweep over a temporary coordination root with no HTTP request, no server and no process, so the default unit lane is its behaviour-preserving classification. Unlike the L17/L18 insertions this row lands inside the unit run above the rows this card cites, which is why every affected citation here was re-derived against the candidate. [165]
- The L05 worker turn owner wake module is registered in the unit-regression lane by the same change set that created it (entry row 105, immediately below `test_state_signal_restart_recovery.py` at `:104` and above `test_state_signal_structural_dispatch_recovery.py` at `:106`) — it seeds owned worker and manager seats on a real `TerminalCatalog`, drives the real `run_agent_notifier_sweep` over a temporary coordination root with real task documents and the real durable stores, issues no HTTP request, starts no server and starts no process, and asserts the whole inbox store rather than its state-signal subset, so the default unit lane is its behaviour-preserving classification. The insertion sits inside the unit run above the rows this card cites, which is why every affected citation here was re-derived against the candidate rather than carried. [166]
- The L17 observer-health proof is registered in the unit-regression lane by the same change set that created it (entry row 122, immediately below `test_terminal_liveness_registration_order.py` at `:121`) — it drives the record, the writer, the accumulator and the real `_state_response` handler and `stream_events` generator against stub projectors with no HTTP transport and no server, so the default unit lane is its behaviour-preserving classification. The insertion sits below `test_serving_observation_loop.py` (`:97`) and `test_serving_startup_prime.py` (`:98`), so no earlier row moved. [167]
- The L07 curator-wake proof is registered in the unit-regression lane by the same change set that created it (entry row 102), immediately below `test_state_signal_boundary_delivery.py` at `:101` and above `test_state_signal_relay.py` at `:103` — it drives the real liveness sweeper, the real agent-notifier sweep and the real `run_agent_notifier_sweep` over temporary catalogs and an in-process tmux host, with no HTTP request, no server and no process, so the default unit lane is its behaviour-preserving classification. [168]
- Retained unit-regression membership, including the R28 deferred-work and canonical terminal-evidence mapping proofs. The range moved by +2 when this change set and L4 each inserted one row additively into the same list. [169]
- Small actual integration file population [170]
- Retained structural detector classifications [171]
- Provider contract classifications [172]
- The registry retains separate stress-durability and migration lanes. [173]
- L38 registered public activation/admission and route-review transport ownership [174]
- The new parked-candidate suite is registered in the unit-regression lane. [175]
- The manifest still has no default classification for an unregistered test file. [176]
- LOCR-L09 boundary-delivery forcing module registered in the unit lane [177]
- The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. [178]
- The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 272 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). [179]
- The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 218 now, after the L4, L5, L7, L8 and L3 insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. [180]
- The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 230 now, after the L4, L5, L7, L8 and L3 insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. [181]
- The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 249 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). [182]
- The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row 289 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). [183]
- The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 243 now, after the L4, L5, L7, L8 and L3 insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. [184]
- The L4 producer-census suite is registered in the unit-regression lane by the commit that landed L4, closing the gap the L4 section recorded. [185]
- The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 240 now, after the L7, L8 and L3 insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. [186]
- The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 222 now, after the L8 and L3 insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. [187]
- The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 265 now, after the L3 insertion) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. [188]
- The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 69) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. [189]
- The integration lane's collected-case cap that constrains lane choice, cited as the pinned key and value: `integration_case_budget = 1000` at `pyproject.toml:279`, the pair `260918-TSIP-L7` raised to 600 / 3000 and `260918-TSIP-L13` raised again to 1000 / 4000. [190]
- The integration lane's collected-case cap that constrains lane choice, cited as the pinned key and value: `integration_case_budget = 1000` at `pyproject.toml:279`, the pair `260918-TSIP-L7` raised to 600 / 3000 and `260918-TSIP-L13` raised again to 1000 / 4000. [191]
- Retained unit-regression membership, including the R28 deferred-work and canonical terminal-evidence mapping proofs. **Re-derived at `260918-TSIP-L6`:** the block is `5-159`, because this leaf added `test_response_address_binding.py` at `:112`, L5 had added its own row at `:153`, and L4 inserted one row additively into the same list. [192]
- Small actual integration file population [193]
- Retained structural detector classifications [194]
- Provider contract classifications [195]
- The registry retains separate stress-durability and migration lanes. [196]
- L38 registered public activation/admission and route-review transport ownership [197]
- The new parked-candidate suite is registered in the unit-regression lane. [198]
- The manifest still has no default classification for an unregistered test file. [199]
- LOCR-L09 boundary-delivery forcing module registered in the unit lane [200]
- The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. [201]
- The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row **226** now, after the L4, seal-removal, L5, L7, L8, L3 and `260918-TSIP-L6` insertions). [202]
- The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row **172** now, after the L4, L5, L7, L8, L3 and `260918-TSIP-L6` insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. [203]
- The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row **184** now, after the L4, L5, L7, L8, L3 and `260918-TSIP-L6` insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. [204]
- The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row **203** now, after the L4, seal-removal, L5, L7, L8, L3 and `260918-TSIP-L6` insertions). [205]
- The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row **240** now, after the L4, seal-removal, L5, L7, L8, L3 and `260918-TSIP-L6` insertions). [206]
- The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row **197** now, after the L4, L5, L7, L8, L3 and `260918-TSIP-L6` insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. [207]
- The L4 producer-census suite is registered in the unit-regression lane by the commit that landed L4, closing the gap the L4 section recorded. [208]
- The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row **194** now, after the L7, L8, L3 and `260918-TSIP-L6` insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. [209]
- The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row **176** now, after the L8, L3 and `260918-TSIP-L6` insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. [210]
- The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row **219** now, after the L3 and `260918-TSIP-L6` insertions) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. [211]
- The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 69) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. [212]
- The integration lane's collected-case cap that constrains lane choice, cited as the pinned key and value: `integration_case_budget = 1000` at `pyproject.toml:279`, the pair `260918-TSIP-L7` raised to 600 / 3000 and `260918-TSIP-L13` raised again to 1000 / 4000. [213]
- The lane manifest is fail-closed: an unregistered tracked module makes loading refuse rather than classifying it by default. [214]
- The L4 capsule-and-skill-serving suite is registered in the unit-regression lane by the same change set that created it (entry row 19) — 19 of its 21 cases are hermetic over a disposable coordination root and a synthetic skills corpus and only its two real-process exchanges carry the integration marker, so that is its behaviour-preserving lane. [215]
- The unit collected-case ceiling. **Corrected four times:** it read 1000 and the default selection had outgrown it (1053 collected at the base, so `pytest mcp/tests` refused collection before any case executed); 260915-CAPS-L8 executed the developer's raise to 1500, the merged line's 2026-09-17 ruling raised it to **2000**, the merge onto the moved super line raised it to **2200** over the merged 2035-case population, `260915-KS-L21` raised it to **2300** over the measured 2206, six cases past 2200, `260918-TSIP-L7` raised the pair to **3000 / 600** by developer decision on 2026-09-19, and `260918-TSIP-L13` raised it again to **4000 / 1000** by a second developer decision on 2026-09-20 — which is what the declaration reads now. Superseded five times, never deleted: the condition each value recorded was real and is what caused the ruling that replaced it. [216]
### Cross-Repo References

No separate cross-repository authority is established by this file.

## 260918-TSIP-L4 — Two Rows, And The Citations The Insertion Moved

This leaf added **two** rows and no other content changed: `"mcp/tests/test_atomic_series_chain_pair_order.py"`
in **`integration`** at **`:165`** (`T49` — the module existed with no lane row, so the loader
refused: `test evidence lanes have 1 finding(s): test files without an explicit lane`) and
`"mcp/tests/test_tool_response_conformance.py"` in **`architecture-fitness`** at **`:244`**. The
file is **267 → 269 lines**, and the shipped loader now reports
`LOADED: f5f3c26265e1846f55b0ee6f13d56282c1fd1ffaa5a624de29474813c3db953c`, **251 rows / 251
modules**.

**The measured remap is `n ≤ 164 → n`, `165-242 → n+1`, `243-268 → n+2`.** (The worklist handed to
the curator wrote `n ≤ 163 → n`, `164-243 → n+1`, `244+ → n+2`; the boundary is one line out —
`integration = [` is old `:161` and old `:164` is the last unchanged line, so a citation anchored
exactly at old 164 or 243 would have been moved wrongly. No citation in the population anchors
there, so no repair was affected.)

**How the citations were repaired, and why the count is not the finding count.** The shipped
`citation_fix` was run tree-wide over the leaf worktree: **81 failing claims, 66 repaired, 25
documents written, 15 declined, 28 findings remaining**. The 15 declines are anchor-ambiguous
cases the fixer refuses by design (`integration` and `nextAction` occur many times;
`class LeafRefResolutionError`, `contractFingerprint`, `"AgentRole = Literal["` resolve to several
extents). The curator then **enumerated instead of trusting the finding set**: 13 changed paths ×
every active citation and prose mention into them = **290 occurrences, 165 of them moved**, against
the checker's **96 `range_resolution` findings** — so **69 moved citations were green**, the
`range_resolution` blind spot this card already records. All 98 the fixer could not reach were
repaired from the measured map and 11 by hand, and the final containment check reports **213 claims
citing a changed path with 0 missing anchors**.

**Two aggregate rows, fixed from the map rather than by the fixer.** `:861`/`:865`
(`157-221 → 157-222`) and `:867` (`4-266 → 4-268`) are the rows whose single anchor resolves to
several extents; they were repaired from the measured map and then re-read in the file.

**One correction inside this card that is not this leaf's arithmetic.** The four
`… Lane Row (Declared)` narratives (`:296`, `:400`, `:428`, `:515`) carried line numbers that were
already stale at this leaf's base — the L17 narrative's `:172`/`:173`/`:174` were 13 lines from the
rows they name (`:185`/`:186`/`:187` at base), the L27 narrative's `:182`/`:184` were 34 lines out,
and the L8 and L5 narratives 13 and 38 out. The five prose mentions in them were set to the **true
current rows** (`187`/`186`/`188`, `216`, `257`, `218`/`217`/`219`) rather than moved by `+1`/`+2`,
because moving a stale number preserves a reader-facing error that no check can see (`T45`).

## 260918-TSIP-L5 — One Row, And The Bracket Figures Re-Derived

This leaf adds **one** row and changes no other line of the manifest:
`"mcp/tests/test_tool_entry_point_sweep.py"` in **`unit-regression`** at **`:153`**, inserted
alphabetically between `test_terminal_paste.py` (`:152`) and `test_tool_response_budgets.py`
(`:154`). That is the behaviour-preserving lane: the module's whole world is a `tempfile`
coordination root with no docker, no network and no real state, it carries no `-m` override, and
its 14 cases run in the ordinary default selection. The file is **269 → 270 lines**, the manifest
entries **251 → 252**, and the modules on disk **251 → 252** — every module on disk now has
exactly one row.

**The measured remap is `n ≤ 152 → n`, `n = 153..269 → n+1`.** Verified as a pure one-line
insertion (one added line; the shifted tail compared line by line). `integration = [` is old
`:161` → new `:162`, `architecture-fitness = [` old `:228` → new `:229`, and the new row's own
line is `:153` — so the lane-bracket rows and every per-module row below `:152` move, and the
three entities the previous section named as static (`unit-regression = [` at `:5`, and the
`stress-durability`/`migration` declarations) keep their relation to the insertion.

**The population, enumerated rather than inferred (`T60`).** Every citation into this file was
enumerated from **this leaf's memory worktree** (`d185e459` — the tree the enclosure contract
names, and the only one `application/memory_tools.py::_refuse_official_memory` permits):
**115 moving anchors across 20 documents — 48 live, 67 under `## Update History` and therefore
exempt — moving 111 document lines (45 live, 66 exempt)**. The census was taken twice; the second
pass found the first **three rows short**, because those rows spell the path as the bare basename
(`test-evidence-lanes.toml:184-190`) rather than the routed path — an enumeration must match both
spellings. **No memory document cites the new module** (it did not exist at this base), so its own
card is the only artifact it needs.

**`T52` measured on this leaf: the checker saw 31 of the 48 live movers.** The baseline
`range_resolution` run reported exactly 31 `citation_anchor_absent_from_range` findings against
these documents; the other 17 moved citations were **green** because the anchor still sat inside
the cited range — the five `## … Lane Row (Declared)` prose mentions, the two ranges that span the
insertion (`test_terminal_blocker_reasons.py.md`'s `128-199`, this card's `4-268`), and the six
bracket rows whose anchor is the range's own first line. Enumerating the population rather than
the finding set is what found them.

**The bracket rows, re-derived at this candidate rather than shifted.** The reference rows at
`:866-872` have been carried across leaves by `+1` shifts since at least `621db898`, and their
values **matched no bracket of this file**: measured here, `integration` runs from its declaration
`:161` to its closing bracket `:227`, not `157-222`. They are now this candidate's measured
brackets, computed as the lane's declaration line through its closing bracket (an empty lane cited
at its declaration line, as its existing shape does): `integration` **`162-228`**,
`architecture-fitness` **`229-250`**, `provider-conformance` **`251-266`**, `stress-durability`
**`267-267`**, `migration` **`269-269`**, whole manifest **`4-269`**. **Reported, not repaired:**
the two `5-151` rows at `:865` and `:871` under-claim the unit-regression block, which is `5-157`
here (`:5` declaration → `:157` closing bracket). Their own text — "the range moved by +2 when
this change set and L4 each inserted one row additively into the same list" — declares them a
moved-range record, so they are left and reported rather than re-derived. Same disposition for the
as-of blocks that name their own base (`## Current population (measured at this leaf's synced base
23cc7a72 plus its own two rows)` at `:214` and the L2 lane-population paragraph at `:70`).

**Nine prose figures inside the reference table were 30-40 lines stale and are now the measured
rows** (`:875` `row 184 now` → `row 224 now`, `:876` 134 → 170, `:877` 146 → 182, `:878` 163 →
201, `:879` 196 → 238, `:880` 157 → 195, `:882` 154 → 192, `:883` 138 → 174, `:884` 178 → 217).
Each of those cells cites its module's current row in the Source column, so prose and citation
contradicted each other once this leaf's shift landed; no check reads either number.

**A fifth `… Lane Row (Declared)` prose mention, missed by the L4 pass.** The `260913-LCA-L5`
narrative at `:366-367` said the master-link module's row "is `…:153`"; at this leaf's base that
row is `:191` — **38 lines stale**, the same class `260918-TSIP-L4` repaired in four sibling
narratives, and one row short of L4's own list. It now names the true row, `:192`. That narrative
carries no routed path, so neither a citation enumeration nor any checker ever saw it: the
preceding card said "the five `… Lane Row (Declared)` sections" and there are six.

**And one claim's provenance had to be re-worded to survive being touched.** The
`test_automatic_post_integration_cleanup.py.md` row at `:140` was already demoted as pre-existing
debt because its literal anchor `Path("mcp/tests/test_automatic_post_integration_cleanup.py")`
resolves **twice** in `dependency_ownership.py` (`:65` and `:111`) — ambiguous provenance, which
the check enforces on any document a task touches ("touch it, own it"). This leaf must repair that
row's citation anyway, so the anchor is now the unique owning key
`"AMBIENT_ROLE_RUNNER_PATH: frozenset("` at `dependency_ownership.py:62-65`, which resolves once,
and the `integration = [` range moved `161` → `162` with the rest of the population.

## 260918-TSIP-L6 The Two Insertions, And Every Figure Re-Derived From This Candidate

**This leaf added two rows, both pure insertions, both `unit-regression`.** `270 → 272` lines,
`2 insertions, 0 deletions`, two hunks: `test_response_address_binding.py` at **`:112`** and
`test_tool_refusal_conformance.py` at **`:155`**. The insertion coordinates in the pre-change file
are OLD lines **112** and **154** — the boundary is `old_start + old_len`, and reading the hunk
header's `+109` straight off is off by one, which is the trap this card's own shift rule exists to
prevent. The rule is `new = old + (1 if old >= 112) + (1 if old >= 154)`; it reproduces the
file's own line map exactly (`270/270` base lines have an exact counterpart, `0` replaced).

**The population, enumerated from this leaf's memory worktree at `4e21dd22`** (not the official
checkout, `T65`) and with **both spellings** of the path (`T60`'s one-spelling-down lesson):

| | routed spelling only | both spellings |
| --- | --- | --- |
| documents citing the target | 53 | 53 |
| anchored occurrences | 218 (105 live / 113 exempt) | **226 (106 live / 120 exempt)** |
| unanchored mentions | 53 | 98 (includes `path:(N, N)` tuple records) |

The eight extra anchored rows are basename-spelled; **one is live** —
`onboarding/mcp/tests/test-evidence-lanes.toml.md:961`, the `:184-190` row L5's `F2` also found —
and the other seven are exempt `## Update History` bullets. The 45 extra unanchored mentions are
prose and tuple records, not citations.

**`T52` measured on this leaf.** The checker's `range_resolution` reported **102** stale rows
across **93** documents-and-lines. An independent enumeration of the same population found
**117** stale rows across **99** lines: the checker is silent on **15 rows / 6 lines** because
those rows pool several ranges and another range still holds the anchor. So the blind spot here is
**13 % of rows** — much smaller than L4's 58 % or L5's 65 %, because this leaf's change moved its
anchors *out* of their ranges rather than leaving them inside.

**Every bracket row and every `row N` figure in this card was re-derived from THIS candidate**,
not shifted: `unit-regression` is `5-159`, `public-contract` `160-163`, `integration` `164-230`,
`architecture-fitness` `231-252`, `provider-conformance` `253-268`, `stress-durability` `269-270`,
`migration` `271-272`, and the manifest holds **254 entries for 254 modules on disk**
(`153 + 2 + 65 + 20 + 14`). Five narratives that state a *current* position were stale and are
corrected: the L17 row is `:190` (was `:188`, with its neighbours `:189`/`:191`), the L5
master-link row `:194` (was `:192`), the L7 capacity-refusal row `:176` (was `:138` — 38 lines),
the L8 terminal-blocker row `:219` (was `:217`), and the L5 codex row `:260` (was `:258`).

**Post-sync note (`T75`'s precedent).** This leaf's anchors are true of the **272-line** file at
the leaf's base. After the governed closeout and the master sync, the same file is **323 lines**
with the two new rows at `145` and `188`, and every anchor below OLD 112 moves by a different
amount — the loader must be re-run after that sync rather than carried.

## 260921-ICR-L1 Lane Row — The Source-Endpoint Module, Inserted In The Knowledge Run

This leaf registers **one** module, `mcp/tests/test_knowledge_review_source_endpoints.py`, as a
`unit-regression` entry **inserted mid-list** in the alphabetical knowledge run — between
`test_knowledge_review_surface.py` at `:104` and `test_knowledge_requirement_reference_contract.py` at
`:106` — so its row is `mcp/tests/test-evidence-lanes.toml:105`. The lane is the module's own declared
one: it carries `pytestmark = pytest.mark.evidence_unit`, and the loader requires every
`mcp/tests/test_*.py` module to hold exactly one lane. Its boundary is the one this manifest already
admits for `test_evidence_catalog_gate_boundaries.py`: everything runs in-process over state under
`tmp_path` — the cases build a real leaf enclosure, a real linked Git worktree and real commits, and read
the real resolution, capture and comparison — with no network, no Node and no service boundary.

**Measured on this candidate, from the manifest and the modules on disk rather than by adding any
earlier account:**

| | measured on this candidate |
| --- | --- |
| Declared lane entries | **309** |
| `mcp/tests/test_*.py` modules on disk | **309** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| File extent | **328 lines** |
| `unit-regression` | **197**, key `:5`, rows `6-202` |
| `public-contract` | **2**, key `:204`, rows `205-206` |
| `integration` | **76**, key `:208`, rows `209-284` |
| `architecture-fitness` | **20**, key `:286`, rows `287-306` |
| `provider-conformance` | **14**, key `:308`, rows `309-322` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:324` and `:326`) |

**The insertion moves every row below it by one, and that is what this leaf owed the rest of memory.**
The new row sits at `:105`, so every entry from the old `:105` down — every lane key and every later
row — is one line lower now: the previously-recorded `test_knowledge_requirement_reference_contract.py`
row at `:105` is at `:106`, the `public-contract` key moved `:203` → `:204`, the `integration` key
`:207` → `:208`, and every citation into this manifest from any route card that pointed at or below
`:105` was re-derived from the anchor's real position in the same pass rather than carried. The two
counts that do **not** move are the lane keys of the empty lanes relative to each other and the
per-lane populations other than `unit-regression`, which rises by exactly one. Older per-candidate
accounts above state the numbers *their* candidate measured and are retained as that record.

- **The registered row itself, in the alphabetical knowledge run between the review-surface module and the requirement-reference contract.** [217]
- The lane key the population is counted from, and the key of the next occupied lane after the insertion. [218]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [219]
- The precedent for a `unit-regression` row whose cases really do create Git objects under a temporary root they own. [220]
- **The catalog consumer rows the same registration produced, which is the other half of this leaf's footprint in the evidence registries.** [221]

## 260921-ICR-L6 Lane Row — The One-Sided-Statement Cases, Beside The Ingest Modules

This leaf registers **one** module, `mcp/tests/test_knowledge_review_one_sided_statements.py`, as a
`unit-regression` entry **inserted mid-list** in the alphabetical knowledge run, with
`test_knowledge_review_surface.py` at `:106` above it and `test_knowledge_review_source_endpoints.py`
at `:108` below it — so its row is `mcp/tests/test-evidence-lanes.toml:108`. At the sync this row moved
up from the `:105` the pre-sync candidate measured, because leaf `260921-ICR-L18` registered its two
ingest modules at `:87`/`:88`, above it. The lane is the module's own declared one: it carries
`pytestmark = pytest.mark.evidence_unit`, and the loader requires every `mcp/tests/test_*.py` module to
hold exactly one lane. Its boundary is the one this manifest already admits for the neighbouring
review-surface module: everything runs in-process over state under `tmp_path` — the six cases build
**two real knowledge snapshots** through the public store operations and drive the real `compose_review`
over them, with no network, no Node and no service boundary.

**Measured on this candidate, from the manifest and the modules on disk rather than by adding any
earlier account:**

| | measured on this candidate |
| --- | --- |
| Declared lane entries | **312** |
| `mcp/tests/test_*.py` modules on disk | **312** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| File extent | **330 lines** |
| `unit-regression` | **200**, key `:5`, rows `6-205` |
| `public-contract` | **2**, key `:207`, rows `208-209` |
| `integration` | **76**, key `:211`, rows `212-287` |
| `architecture-fitness` | **20**, key `:289`, rows `290-309` |
| `provider-conformance` | **14**, key `:311`, rows `312-325` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:327` and `:329`) |

**The insertion moves every row below `:107` by one, and that is what this leaf owes the rest of
memory.** `test_knowledge_review_source_endpoints.py` — itself a mid-list insertion by
`260921-ICR-L1` — now reads at `:108`, and the lane keys now stand at `:207` (public-contract), `:211`
(integration), `:289` (architecture-fitness), `:311` (provider-conformance) and `:327`/`:329` for the
two empty lanes. Every citation into this manifest that points below `:107` therefore reads one line
lower than it did, and those held by other cards were left to the citation-reprojection pass rather
than re-pointed by hand. The one population that moves is `unit-regression`, which rises by exactly
one; the other five are unchanged. Older per-candidate accounts above state the numbers *their*
candidate measured and are retained as that record.

- **The registered row itself, in the alphabetical knowledge run immediately after the review-surface module and before the source-endpoint module.** [222]
- The lane key the population is counted from, and the key of the next occupied lane after the insertion. [223]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [224]
- The row this insertion displaced by one line, itself a `260921-ICR-L1` mid-list registration. [225]
- **The catalog consumer row the same registration produced, which is the other half of this leaf's footprint in the evidence registries.** [226]
## 260921-ICR-L45 One Lane Row — The Per-Target Realization Rationale Cases

`ICR-R20@v1` (the per-target realization rationale repair) registers one new ordinary unit module,
`mcp/tests/test_curator_realization_authoring.py` (12 cases), in the **`unit-regression`** lane directly
below its curator-ingest siblings (`test_curator_family_authoring.py`, `test_curator_family_retention.py`,
`test_curator_ingest_write_and_retention.py`). It marks its cases `pytest.mark.evidence_unit`; the
worker found the omission because an unregistered module fails the lane-manifest check. **The insertion
is at `:24`, so every manifest line below it moved by one**; every body row of this card and of the
cards and overviews citing this file below `:24` was re-pointed through the exact base-to-candidate line
map. Measured on the candidate synced onto L44 (`9b2f775f`): `unit-regression` 233, total 348 declared rows
against 348 `mcp/tests/test_*.py` modules on disk. No lane key, ceiling or other module changed.

- The new lane row, directly below the curator-ingest sibling modules. [227]

## 260921-ICR-L8 Three Lane Rows — The Movement, Reach And Authored-Line Case Modules

`260921-ICR-L8` (`ICR-R08@v1`) registers **three** modules, all `unit-regression` and all inserted
mid-list in the alphabetical knowledge run: `mcp/tests/test_knowledge_review_relationship_line.py` at
`:114`, `…_movement.py` at `:115` and `…_reach.py` at `:116` — between
`mcp/tests/test_knowledge_review_revision_selection.py` above them and
`mcp/tests/test_master_net_generation.py` below. Each module carries its own declared lane
(`pytestmark = pytest.mark.evidence_unit`), and the loader requires every `mcp/tests/test_*.py` module to
hold exactly one lane, so a new module that is not registered refuses at collection. Their boundary is
the one this manifest already admits for the neighbouring review case modules: everything runs
in-process over state under `tmp_path` — the cases build two real knowledge snapshots through the public
store operations and drive the real `read_knowledge_review` composition over them, with no network, no
Node and no service boundary.

**Measured on this candidate, from the manifest and the modules on disk rather than by adding any
earlier account:**

| | measured on this candidate |
| --- | --- |
| Declared lane entries | **323** |
| `mcp/tests/test_*.py` modules on disk | **323** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| File extent | **341 lines** |
| `unit-regression` | **211**, key `:5`, rows `6-216` |
| `public-contract` | **2**, key `:218`, rows `219-220` |
| `integration` | **76**, key `:222`, rows `223-298` |
| `architecture-fitness` | **20**, key `:300`, rows `301-320` |
| `provider-conformance` | **14**, key `:322`, rows `323-336` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:338` and `:340`) |

**The three insertions move every row below `:113` by three, and that is what this leaf owes the rest
of memory.** The lane keys now stand at `:218` (public-contract), `:222` (integration), `:300`
(architecture-fitness), `:322` (provider-conformance) and `:338`/`:340` for the two empty lanes; the
`unit-regression` population rises by exactly three and the other five are unchanged. Every citation
into this manifest that points at or below `:113` therefore reads three lines lower than it did, and the
rows this card and its sibling cards carry at or below that point were re-derived from the anchor's real
position in the same pass rather than carried. Older per-candidate accounts above state the numbers
*their* candidate measured and are retained as that record.

- **The three registered rows themselves, in the alphabetical knowledge run, and the neighbours they sit between.** [228]
- The lane key the population is counted from, and the key of the next occupied lane after the insertions. [229]
- The modules' own lane declarations, which make the classification their own rather than a budget convenience. [230]
- The row the insertions displaced, itself a mid-list registration. [231]
- **The catalog consumer rows the same registration produced, which is the other half of this leaf's footprint in the evidence registries.** [232]

## 260921-ICR-L10 One Lane Row, Inserted Mid-List In The Knowledge Run

`260921-ICR-L10` (`ICR-R10@v1`) adds **one** row to this manifest: the new pagination case module
joins `unit-regression` at line 163 of `mcp/tests/test-evidence-lanes.toml`, between
`mcp/tests/test_retry_selection.py` above and `mcp/tests/test_review_state.py` below, so the run still
declares one row per module on disk and neither count changes. The classification is the
behaviour-preserving one rather than a budget convenience: the module marks itself
`pytestmark = pytest.mark.evidence_unit`, builds every fixture under `tmp_path`, and touches no live
coordination tree, no network and no service.

**The insertion moved every entry below it, and that is this manifest's citation fact.** Every lane key
and every row at or below line 163 reads one line lower than the accounts above record it, so the ranges
in those accounts were re-derived against this candidate rather than left to rot.

## 260921-ICR-L26 One Lane Row — The Subject-Isolation Cases

`260921-ICR-L26` (`ICR-R26@v1`) appends **one** row to the `unit-regression` lane:
`mcp/tests/test_knowledge_review_subject_isolation.py`, the thirteen cases that measure one selected
subject's record isolation through the production composition. The lane is the right one rather than
`integration`: every record is produced through its owning operation against a real leaf enclosure, but
the reads are the ordinary production port and no real boundary outside the worktree is exercised.

**This file refuses an unregistered module at collection**, which is why the row is part of the change
set rather than a follow-up: a case module with no lane row cannot run at all. The row is inserted in the
alphabetical position the file keeps (`…test_knowledge_review_relationship_line.py`,
`…test_knowledge_review_subject_isolation.py`, `…test_master_net_generation.py`), and no other lane and
no other row moved.

## 260921-ICR-L12 The Committed-Leaf Case Module Joins The Unit Regression Lane

`260921-ICR-L12` (`ICR-R12@v1`) adds **one** lane row: `mcp/tests/test_historical_committed_leaf_review.py`
joins `unit-regression`, which is where the module's `pytestmark = pytest.mark.evidence_unit` puts it.
The row is one path in a bare TOML list — the lane key itself carries no anchor a citation grammar can
bind, so a row about it names the path as a quoted anchor — and the collection gate refuses an
unregistered module before it may run at all, which is why the row and the module landed together.

Nothing else in the file changed: no lane was renamed, no path was removed, and no lane's meaning
moved. **Every row below the insertion shifted by one line**, which is why the rows on this card were
re-derived rather than left as they were — a stale range here is a card that tells a reader the wrong
line carries the module it names.

## 260921-ICR-L22 Two Lane Rows — The Rebinding And Movement-Read Case Modules

`260921-ICR-L22` (`ICR-R22@v1`, managed Git recovery rebinding) registers **two** modules, both in the
`integration` lane, which is the lane each module's own construction earns:
`mcp/tests/test_review_sync_rebinding.py` (942 lines) drives the production `worktree_sync` tool through
the real transaction, the real binary-stage knowledge merge, the real publication owner and the real
comparison-generation owner, and `mcp/tests/test_review_sync_movement_read.py` (356 lines) drives the
shipped `read_knowledge_review` over the enclosure its sibling owns. Both rows are inserted mid-list at
`:300-301`, immediately after `mcp/tests/test_worktree_sync.py` at `:299` — the module the sync-side cases
were extracted from — so the two rows are `mcp/tests/test-evidence-lanes.toml:301` and
`mcp/tests/test-evidence-lanes.toml:302`.

**The two insertions moved every entry below them, and that is this card's citation fact.** Each row is
one path, so every entry at or below them reads two lines lower than the accounts above record it: the
`integration` list's own last rows `:300-302` → `:302-304` (76 → **78** entries), `architecture-fitness`'s
key `:304` → `:306` (rows `:305-324` → `:307-326`), `provider-conformance`'s key `:326` → `:328` (rows
`:327-340` → `:329-342`), `stress-durability`'s key `:342` → `:344`, `migration`'s key `:344` → `:346`, and
the file's own extent **345 → 347 lines**.

**Measured on this candidate, from the manifest and the modules on disk rather than by adding any earlier
account:**

| | measured on the working candidate |
| --- | --- |
| Declared lane entries | **329** |
| `mcp/tests/test_*.py` modules on disk | **329** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| File extent | **347 lines** |
| `unit-regression` | **215**, key `:5`, rows `6-220` |
| `public-contract` | **2**, key `:222`, rows `223-224` |
| `integration` | **78**, key `:226`, rows `227-304` |
| `architecture-fitness` | **20**, key `:306`, rows `307-326` |
| `provider-conformance` | **14**, key `:328`, rows `329-342` |
| `stress-durability` / `migration` | **0** / **0** (keys `:344` and `:346`) |

The `unit-regression` and `public-contract` lanes are untouched by this leaf — their counts, keys and row
ranges read exactly as the accounts above record them — which is why the census moves by two and only in
the `integration` lane. No lane was renamed, no path was removed, and no lane's meaning moved.

## 260921-ICR-L31 Three Case Modules Join The Unit-Regression Lane

**``ICR-R31@v1`` added three case modules and registered them here, and nothing else in this manifest
moved.** ``mcp/tests/test_review_family_context.py`` (the production-entry cases),
``mcp/tests/test_review_family_context_population.py`` (the revision-population cases fix round 1
added) and ``mcp/tests/test_review_family_context_values.py`` (the value-construction cases) each
gained their row in the ``unit-regression`` lane, which refuses an unregistered module at collection.
The ``integration`` lane is untouched: this leaf adds no real-boundary integration case, because the
three modules drive the production review over the shared endpoint fixture.

**Why three modules rather than one.** The first was headed past the 900-line soft rail as fix round 1's
cases landed, so the population cases and the value cases were split out by seam rather than by line
count — the population module imports the first module's enclosure and helpers instead of duplicating
them, and the values module builds values in memory and imports no fixture at all. All three stay under
the 1,200-line hard rail and the whole-tree census gained no offender.

**Citation accounting:** this card's rows cite individual lane entries as quoted path strings, which
repeat across the file's lane arrays; each repaired row was translated through the measured insertion
delta and then confirmed to hold its anchor **inside the lane array the row names** (``unit-regression``
or ``integration``), never at a matching string in another lane.

## 260921-ICR-L29 One Lane Row, Mid-List

`ICR-R29@v1` registers one new ordinary unit module in this manifest:
`mcp/tests/test_knowledge_bootstrap.py`, inserted in the **`unit-regression`** lane beside its
`test_knowledge_*` siblings. It is a unit lane row rather than an integration one because the module
marks its cases `pytest.mark.evidence_unit` and drives the shipped CLI inside a self-built coordination
world, which is what this repository calls an ordinary unit-boundary journey; all fifteen cases pass in
that lane.

**The insertion is mid-list, so every line below `:91` in this manifest moved by one.** That matters
here more than in most files: this document is cited by lane key and by line from the case cards and
from the route overview, and a range measured against the base commit lands one line short of the row
it names. Cards that cite this file by line were therefore re-derived against this candidate rather
than shifted. Nothing else changed: no lane key was added or removed, no ceiling moved, and no module
left a lane.

## 260921-ICR-L43 One Lane Row — The Attributed Source-Content Cases

`ICR-R03@v1` (under the 2026-09-28 admission ruling) registers one new ordinary unit module,
`mcp/tests/test_knowledge_review_attributed_source_content.py`, in the **`unit-regression`** lane
directly below its sibling `test_knowledge_review_source_content.py`. It marks its cases
`pytest.mark.evidence_unit`; an unregistered module fails the lane-manifest check, which is how the
worker found the omission. **The insertion is at `:126`, so every line below it moved by one**; rows of
this card that cite lines below it were shifted by one after each was verified against both the base
and this candidate. No lane key, ceiling or other module changed.

- The new lane row, directly below the sibling source-content module. [233]

## 260921-ICR-L42 One Lane Row — The Bounded Task-Document Body Read Cases

`ICR-R24@v3` registers one new ordinary unit module, `mcp/tests/test_task_document_body_lookup.py`
(3 functions, 5 cases), in the **`unit-regression`** lane in alphabetical position. It sits directly
above its closest sibling, `test_task_documents_graph_projection.py`, which is also a unit row. The
lane fits the module: it uses only `tmp_path` and `monkeypatch`, composes no application, and imports
`FRESH` from the integration-lane `test_observer_projection.py` the same way that sibling does. The
worker found the omission because an unregistered module collects no tests (event E1). **The insertion
is at `:208`, so every manifest line below it moved by one.** Every onboarding row citing a line
below it was shifted by one after checking that the base line and the candidate line hold the same
text. Two ranges that span the insertion were widened by one line. Measured on the candidate:
`unit-regression` 231 (was 230), total 346 declared rows against 346 `mcp/tests/test_*.py` modules on
disk. No lane key, ceiling or other module changed.

- The new lane row, directly above its graph-projection sibling. [234]

## 260921-ICR-L55 One Lane Row — The Notes-Listing Cases

`ICR-R24@v3` registers one new ordinary unit module, `mcp/tests/test_notes_listing.py` (5 functions,
6 cases), in the **`unit-regression`** lane in alphabetical position, between `test_models.py` and
`test_observer.py`. The lane fits the module: it uses only `tmp_path` and `monkeypatch`, and it drives
the notes routes through an in-process `TestClient` on a bare app that registers nothing else. The
worker found the omission when the first run without the row exited with pytest status 4 (event E5).
**The insertion is at `:162` of the manifest as it stands after L44, L45 and L47 landed, so every line
below it moved by one.** Every onboarding citation-table row citing a line at or below it was shifted
by one against that landed manifest (256 rows in 59 cards), and 4 ranges that span the
insertion were widened by one line. Rows whose anchor was already off at the landed base keep their
relative offset: this leaf re-points, it does not re-derive older debt. Measured on the candidate:
`unit-regression` 235 (was 234), and 350 declared rows against 350 `mcp/tests/test_*.py` modules on
disk, with none declared but absent and none present but undeclared. No lane key, ceiling or other
module changed.

- The new lane row, between its alphabetical neighbours. [235]

## 260921-ICR-L56 One Lane Row — The Anchor-Observation Memo Cases

`ICR-R24@v3` registers one new ordinary unit module, `mcp/tests/test_read_anchor_memo.py` (8 functions,
9 cases), in the **`unit-regression`** lane in alphabetical position, between
`test_quality_subprocess_environment.py` and `test_read_ar_files.py`. The lane fits the module: each case
builds its own temporary Git repositories under `tmp_path` and uses only `monkeypatch` spies that delegate
to the real runner and extractor. **The insertion is at `:173` of the manifest as it stands after L55
landed (code base `ae2fd5c8`), so every line below it moved by one.** Every onboarding citation-table row
whose range reaches `:173` was shifted by one against that landed manifest (220 rows in 57 cards; 3
ranges that span the insertion were widened by one line). Update History entries and earlier accounts'
prose keep the line numbers of their own time, and rows whose anchor was already off at the landed base
keep their relative offset. Measured on the candidate: `unit-regression` 236 (was 235), and 351 declared
rows against 351 `mcp/tests/test_*.py` modules on disk, with none declared but absent and none present but
undeclared. No lane key, ceiling or other module changed.

- The new lane row, between its alphabetical neighbours. [236]

## 260921-ICR-L57 Three Lane Rows — The File-Size Splits, Each Beside Its Sibling

`260921-ICR-L57` split three case modules that had crossed the 1200-line rail. It registers each new
ordinary unit module in the **`unit-regression`** lane **directly below the module it was split from**,
not in alphabetical position:

- `test_knowledge_review_resolution_and_route.py` below `test_knowledge_review_surface.py` (`:123`);
- `test_knowledge_review_attribution_precedence.py` below `test_knowledge_review_source_endpoints.py`
  (`:127`);
- `test_knowledge_diff_attribution.py` below `test_knowledge_diff_scope.py` (`:139`).

The lane fits each module for the same reason it fits its sibling: the moved cases are byte-identical,
so the new modules keep their siblings' in-process `evidence_unit` marker and fixtures. **The three rows
land at `:123`, `:127` and `:139` of the candidate manifest. Against the manifest as landed at
`69883386`, lines after base `:122`, `:125` and `:136` moved by one, two and three.** Every onboarding citation-table row citing this manifest was re-pointed
through the exact base-to-candidate line map. Ranges that span an insertion grew by the rows inserted
inside them. Measured on the candidate: `unit-regression` 239 (was 236), and 354 declared rows against
354 `mcp/tests/test_*.py` modules on disk, with none declared but absent and none present but
undeclared. No lane key, ceiling or other module changed.

- The three new lane rows, each directly below its sibling. [237]
