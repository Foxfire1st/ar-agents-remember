# mcp/tests/test-evidence-lanes.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test-evidence-lanes.toml` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T03:15+02:00 |
| lastVerifiedCommitHash | `9c12e8b1ec027b8bb07f4c0cc79ef99a655ff890` |
| lastVerifiedCommitDate | 2026-09-18T01:58:08+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l08` uncommitted source; base `1ff1893f44d875073d58af863238501a6be35288` |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## 260915-KS-L8 Lane Rows (Declared) — **the current account**

The KS-L8 change set adds **two** modules and their rows in the same change, and each lane is that
module's behaviour-preserving classification:

| Module | Lane | Row | Why that lane |
| --- | --- | ---: | --- |
| `mcp/tests/test_knowledge_diff_scope.py` | `unit-regression` | `:76` | 13 nodes; hermetic — temporary directories under `tmp_path`, two in-process APSW databases built through the public store operations (the candidate copied from the closed baseline and curated through the store), two local committed Git trees built by the fixture, no integration marker |
| `mcp/tests/test_knowledge_diff_boundaries.py` | `integration` | `:159` | 15 nodes over the same real trees **driving the production Git probe** rather than a substitute, a real curated candidate database, a real write that moves the logical digest, and the serialized response |

Their shared support module `mcp/tests/diff_scope_test_support.py` is **not** a lane row: it is a governed
artifact (`shared-support` / `internal-canonical` / `integration` / `local-composition`, contract
`knowledge-diff-cases`) in `mcp/tests/evidence-lifecycle.toml`, with exactly those two modules as its
declared consumers — and it is also why `mcp/tests/read_scope_test_support.py`'s consumer list gained the
same two paths in this change, because the diff fixture builds on the read fixture.

### The merged measurement, taken on this leaf's frozen candidate

**Measured from the manifest and the module population on disk, not derived by adding any earlier
account:**

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

| Module | Lane | Row | Why that lane |
| --- | --- | ---: | --- |
| `mcp/tests/test_knowledge_read_scope.py` | `unit-regression` | `:75` | 21 nodes; hermetic — temporary directories under `tmp_path`, in-process APSW databases built through the public store operations, no repository working tree, no network, no integration marker |
| `mcp/tests/test_knowledge_read_boundaries.py` | `integration` | `:157` | 20 nodes over a **real committed Git tree**, a real published database and real snapshot/namespace refusals |
| `mcp/tests/test_knowledge_read_paths.py` | `integration` | `:158` | 5 nodes that measure Git's own `ls-tree` behavior with their own subprocess calls; it exists because these cases pushed the boundaries module past the 1 200-line hard limit in fix round 2, and the limit was paid rather than waived |

Their shared support module `mcp/tests/read_scope_test_support.py` is **not** a lane row: it is a governed
artifact (`shared-support` / `internal-canonical` / `unit-regression`, contract `knowledge-read-scope-cases`)
in `mcp/tests/evidence-lifecycle.toml`, with the three modules above as its exactly-declared consumers.

### The merged measurement, taken on this leaf's frozen candidate

**The two labelled accounts this card carried below were measured against different code states and their
merged counts were recorded as pending. They have now been measured, and this is the measured account** —
counted from the manifest and the module population on disk, not derived by adding the two accounts:

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
`mcp/tests/test-evidence-lanes.toml:140-141`. The lane is not a preference here, it is forced: the unit population
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
rows `mcp/tests/test-evidence-lanes.toml:70-74`, all in the **unit-regression** lane. Each is hermetic (temporary
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
`mcp/tests/test-evidence-lanes.toml:153`, in the **integration** lane: it drives the real public
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
`mcp/tests/test-evidence-lanes.toml:138`, in the **integration** lane: the module composes the real
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
`mcp/tests/test-evidence-lanes.toml:178`, in the **integration** lane: the module builds a real landed
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
The row is `mcp/tests/test-evidence-lanes.toml:184`, in the **integration** lane, between
`test_terminal_liveness.py` at `:182` and `test_tools.py` at `:184`.

That is its behaviour-preserving lane even though the module is hermetic (temporary catalogs,
in-process `unittest`, no `worktree_services`): it is registered exactly as its sibling
`test_terminal_liveness.py` is at `:182`, and a new module in this family needs a row or its
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
`mcp/tests/test-evidence-lanes.toml:123`, in the **unit-regression** lane, immediately below
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
the dated `## Update History` entries — as-of records of earlier candidates — were deliberately left as
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

## Code Commentary

### Logic



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
- Lane membership is additionally bounded by the declared collected-case budgets (`unit_case_budget` 1000 at `pyproject.toml:185`, `integration_case_budget` **300** at `pyproject.toml:186`; the 150, 200 and 250 values in earlier entries of this card are stale). A module that was previously running unmarked already spends unit budget, so registering it as `unit-regression` preserves behaviour; moving it into `integration` can push full-suite collection past the integration cap and fail collection outright. Classification cannot be chosen for semantic tidiness alone.
- Full suites and whole-candidate review occur at master completion, not once for every lane or leaf.
- Lane membership must keep each collected population inside its declared case budget: `unit_case_budget` 1000 and `integration_case_budget` **300** (root `pyproject.toml:185-186`), enforced in `pytest_collection_finish`. A module that a full run previously collected unmarked - and therefore already counted as unit - belongs in `unit-regression`; moving it to `integration` can refuse collection.

## Docs References

No external Domain Documentation source is configured; these are repository-owned implementation facts.

## Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Retained unit-regression membership, including the R28 deferred-work and canonical terminal-evidence mapping proofs | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-5 |
| Small actual integration file population | `integration` | mcp/tests/test-evidence-lanes.toml:138-197 |
| Retained structural detector classifications | "architecture-fitness" | mcp/tests/test-evidence-lanes.toml:228-228 |
| Provider contract classifications | "provider-conformance" | mcp/tests/test-evidence-lanes.toml:247-247 |
| Empty former stress/migration populations | "stress-durability"; "migration" | mcp/tests/test-evidence-lanes.toml:262-264 |
| L38 registered public activation/admission and route-review transport ownership | `integration` | mcp/tests/test-evidence-lanes.toml:138-200 |
| The new parked-candidate suite is registered in the unit-regression lane. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-5 |
| The manifest still has no default classification for an unregistered test file. | "stress-durability" | mcp/tests/test-evidence-lanes.toml:262-262 |
| LOCR-L09 boundary-delivery forcing module registered in the unit lane | "mcp/tests/test_state_signal_boundary_delivery.py" | mcp/tests/test-evidence-lanes.toml:124-124 |
| The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. | "mcp/tests/test_checkpoint_landing.py" | mcp/tests/test-evidence-lanes.toml:26-26 |
| The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 184 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_worktree_status_terminal_next_tool.py" | mcp/tests/test-evidence-lanes.toml:223-223 |
| The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 134 now, after the L4, L5, L7, L8 and L3 insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. | "mcp/tests/test_checkpoint_landing_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:171-171 |
| The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 146 now, after the L4, L5, L7, L8 and L3 insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:183-183 |
| The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 163 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_pause_stop_only_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:200-200 |
| The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row 196 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:236-236 |
| The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 157 now, after the L4, L5, L7, L8 and L3 insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:194-194 |
| The L4 producer-census suite is registered in the unit-regression lane by the commit that landed L4, closing the gap the L4 section recorded. | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:89-89 |
| The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 154 now, after the L7, L8 and L3 insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:191-191 |
| The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 138 now, after the L8 and L3 insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. | "mcp/tests/test_closeout_projection_source_classification.py" | mcp/tests/test-evidence-lanes.toml:138-200 |
| The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 178 now, after the L3 insertion) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:216-216 |
| The L2 knowledge graph suite is registered in the unit-regression lane by the same change set that created it (entry rows 69-73) — all four modules are hermetic (temporary directories, in-process APSW databases, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. | "mcp/tests/test_knowledge_family_revision.py"; "mcp/tests/test_knowledge_graph_reads.py"; "mcp/tests/test_knowledge_relation_rules.py"; "mcp/tests/test_knowledge_revision_seals.py" | mcp/tests/test-evidence-lanes.toml:72-81 |
| The L3 candidate-batch pair and the label-operations suite are registered in the unit-regression lane by the same change set that created them (entry rows 18-19, and row 71 now after the L4 insertions) — all three are hermetic (temporary directories, in-process APSW databases driven through the real admitted destination, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. | "mcp/tests/test_candidate_batch_commands.py"; "mcp/tests/test_candidate_batch_transaction.py"; "mcp/tests/test_knowledge_label_operations.py" | mcp/tests/test-evidence-lanes.toml:18-73 |
| The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (row 79 now, after the L4 insertions) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:90-90 |
| **The L4 snapshot pair is registered in the unit-regression lane by the same change set that created them (rows 69 and 75)** — both modules are hermetic: temporary directories under `tmp_path`, in-process APSW databases driven through the real admitted destination and the real publication lock, and a child interpreter used only as a crash probe, with no integration marker, no repository working tree and no network. | "mcp/tests/test_knowledge_candidate_workspace.py"; "mcp/tests/test_knowledge_snapshot_publication.py" | mcp/tests/test-evidence-lanes.toml:70-83 |
| **The knowledge block's current membership across all four KS leaves**, whose insertion order is why the rows are not contiguous by leaf. | "mcp/tests/test_knowledge_store.py" | mcp/tests/test-evidence-lanes.toml:84-84 |
| **The integration lane's collected-case cap that constrains lane choice, cited as the pinned key and value — raised to 340 on this master's owning seat's measurement, not by this leaf's fix round.** | "integration_case_budget = 340" | pyproject.toml:287-287 |
| **The unit ceiling, cited as the pinned key and value — raised to 1250 because the merged line collects both campaigns' populations and `pytest_collection_finish` runs no tests at all over an over-budget population.** | "unit_case_budget = 1250" | pyproject.toml:286-286 |
| **The two lane rows this leaf registered in the same change, both in `integration` because the unit population sits exactly at its declared ceiling.** | "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" | mcp/tests/test-evidence-lanes.toml:160-161 |
| The lane manifest is fail-closed: an unregistered tracked module makes loading refuse rather than classifying it by default. | `load_lane_manifest` | mcp/test_support/agents_remember_test_support/testing/lane_manifest.py:99-144 |
| Retained unit-regression membership, including the R28 deferred-work, canonical terminal-evidence mapping and L23 registration-order proofs | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-128 |
| The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 191 now, after the L4, seal-removal, L5, L7, L8, L3, L01 and L17 insertions). | "mcp/tests/test_worktree_status_terminal_next_tool.py" | mcp/tests/test-evidence-lanes.toml:223-223 |
| The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 135 now, after the L4, L5, L7, L8, L3 and L01 insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. | "mcp/tests/test_checkpoint_landing_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:171-171 |
| The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 147 now, after the L4, L5, L7, L8, L3 and L01 insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:183-183 |
| The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 164 now, after the L4, seal-removal, L5, L7, L8, L3 and L01 insertions). | "mcp/tests/test_pause_stop_only_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:200-200 |
| The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row 197 now, after the L4, seal-removal, L5, L7, L8, L3 and L01 insertions). | "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:236-236 |
| The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 158 now, after the L4, L5, L7, L8, L3 and L01 insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:194-194 |
| The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 155 now, after the L7, L8, L3 and L01 insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:191-191 |
| The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 139 now, after the L8, L3 and L01 insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. | "mcp/tests/test_closeout_projection_source_classification.py" | mcp/tests/test-evidence-lanes.toml:175-175 |
| The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 179 now, after the L3 and L01 insertions) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:216-216 |
| The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 69) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:90-90 |
| The L23 registration-order proof is registered in the unit-regression lane by the same change set that created it (entry row 118) — it drives the real catalog and sweeper over `tempfile` files with in-process registrar/compactor doubles, so it is hermetic and the default unit lane is its behaviour-preserving classification. | "mcp/tests/test_terminal_liveness_registration_order.py" | mcp/tests/test-evidence-lanes.toml:147-147 |
| The L27 pane-authority proof is registered in the integration lane by the same change set that created it — entry ordinal **53** of 61 in that lane; file line `:183` at base `52bee429` **plus** this change set (`:182` at that base alone, and `:181` at this candidate's own build base `b368b661`, which is the figure the leaf's verdict and worker report cite). It is hermetic but takes the lane of its sibling `test_terminal_liveness.py`, and a new module of this family needs a row or its application imports run inside ordinary unit collection. | "mcp/tests/test_terminal_liveness_pane_authority.py" | mcp/tests/test-evidence-lanes.toml:218-218 |
| The unit-regression bracket the L23 row sits inside, whose upper bound has moved with each later unit-lane insertion (L23, then L01, then L10). | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-128 |
| The L01 steady-state observation suite is registered in the unit-regression lane by the same change set that created it (entry row 97) — it drives the real lifespan finalizer, the real sweeper and the real catalog under a virtual event-loop clock and issues no HTTP request, so the default unit lane is its behaviour-preserving classification. | "mcp/tests/test_serving_observation_loop.py" | mcp/tests/test-evidence-lanes.toml:119-119 |
| The L18 startup-prime proof is registered in the unit-regression lane by the same change set that created it (entry row 98), immediately below its sibling and sharing that sibling's fixture — it drives the real lifespan over a temporary catalog under a virtual clock with no HTTP request and no process, so the default unit lane is its behaviour-preserving classification. | "mcp/tests/test_serving_startup_prime.py" | mcp/tests/test-evidence-lanes.toml:121-121 |
| The unit-regression bracket at the L18 candidate measurement, whose upper bound moved with each later unit-lane insertion (L23, L01, L10, then L18). | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-126 |
| The integration bracket at the L18 candidate measurement. | `integration` | mcp/tests/test-evidence-lanes.toml:132-194 |
| The L17 observer-health proof is registered in the unit-regression lane by the same change set that created it (entry row 122, immediately below `test_terminal_liveness_registration_order.py` at `:121`) — it drives the record, the writer, the accumulator and the real `_state_response` handler and `stream_events` generator against stub projectors with no HTTP transport and no server, so the default unit lane is its behaviour-preserving classification. The insertion sits below `test_serving_observation_loop.py` (`:97`) and `test_serving_startup_prime.py` (`:98`), so no earlier row moved. | "mcp/tests/test_terminal_observer_health.py" | mcp/tests/test-evidence-lanes.toml:148-148 |
| The L06 reviewer-relay proof is registered in the unit-regression lane by the same change set that created it (entry row 68, immediately below `test_lifecycle_operation_model_helpers.py` at `:67` and above `test_memory_attribution_producers.py` at `:69`) — it drives the real observer, the production terminal-evidence lift and the real notifier sweep over a temporary coordination root with no HTTP request, no server and no process, so the default unit lane is its behaviour-preserving classification. Unlike the L17/L18 insertions this row lands inside the unit run above the rows this card cites, which is why every affected citation here was re-derived against the candidate. | "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" | mcp/tests/test-evidence-lanes.toml:88-88 |
| The L05 worker turn owner wake module is registered in the unit-regression lane by the same change set that created it (entry row 105, immediately below `test_state_signal_restart_recovery.py` at `:104` and above `test_state_signal_structural_dispatch_recovery.py` at `:106`) — it seeds owned worker and manager seats on a real `TerminalCatalog`, drives the real `run_agent_notifier_sweep` over a temporary coordination root with real task documents and the real durable stores, issues no HTTP request, starts no server and starts no process, and asserts the whole inbox store rather than its state-signal subset, so the default unit lane is its behaviour-preserving classification. The insertion sits inside the unit run above the rows this card cites, which is why every affected citation here was re-derived against the candidate rather than carried. | "mcp/tests/test_state_signal_worker_wake.py" | mcp/tests/test-evidence-lanes.toml:128-128 |
| The L17 observer-health proof is registered in the unit-regression lane by the same change set that created it (entry row 122, immediately below `test_terminal_liveness_registration_order.py` at `:121`) — it drives the record, the writer, the accumulator and the real `_state_response` handler and `stream_events` generator against stub projectors with no HTTP transport and no server, so the default unit lane is its behaviour-preserving classification. The insertion sits below `test_serving_observation_loop.py` (`:97`) and `test_serving_startup_prime.py` (`:98`), so no earlier row moved. | "mcp/tests/test_terminal_observer_health.py" | mcp/tests/test-evidence-lanes.toml:148-148 |
| The L07 curator-wake proof is registered in the unit-regression lane by the same change set that created it (entry row 102), immediately below `test_state_signal_boundary_delivery.py` at `:101` and above `test_state_signal_relay.py` at `:103` — it drives the real liveness sweeper, the real agent-notifier sweep and the real `run_agent_notifier_sweep` over temporary catalogs and an in-process tmux host, with no HTTP request, no server and no process, so the default unit lane is its behaviour-preserving classification. | "mcp/tests/test_state_signal_curator_wake.py" | mcp/tests/test-evidence-lanes.toml:125-125 |

## Cross-Repo References

No separate cross-repository authority is established by this file.

## Update History
- 2026-09-17T22:33:10+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:228-228. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:247-247. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:262-262. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:124-124. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:223-223. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:171-171. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:183-183. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:200-200. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:236-236. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:194-194. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:89-89. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:191-191. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:90-90. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_knowledge_store.py" repointed to mcp/tests/test-evidence-lanes.toml:84-84. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:161-161; mcp/tests/test-evidence-lanes.toml:160-160. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:223-223. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:171-171. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:183-183. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:200-200. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:236-236. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:194-194. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:191-191. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:175-175. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:90-90. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:147-147. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:218-218. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_serving_observation_loop.py" repointed to mcp/tests/test-evidence-lanes.toml:119-119. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:121-121. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:148-148. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:88-88. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:128-128. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:148-148. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_state_signal_curator_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:125-125. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "unit-regression" repointed to mcp/tests/test-evidence-lanes.toml:5-5. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:224-224. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:243-243. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:258-258. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:120-120. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:219-219. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:167-167. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:179-179. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:232-232. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:190-190. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:85-85. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:187-187. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:212-212. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_family_revision.py"; "mcp/tests/test_knowledge_graph_reads.py"; "mcp/tests/test_knowledge_relation_rules.py"; "mcp/tests/test_knowledge_revision_seals.py" repointed to mcp/tests/test-evidence-lanes.toml:71-71; mcp/tests/test-evidence-lanes.toml:73-73; mcp/tests/test-evidence-lanes.toml:77-77; mcp/tests/test-evidence-lanes.toml:78-78. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:86-86. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_store.py" repointed to mcp/tests/test-evidence-lanes.toml:80-80. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:157-157; mcp/tests/test-evidence-lanes.toml:156-156. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:171-171. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:143-143. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:214-214. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_serving_observation_loop.py" repointed to mcp/tests/test-evidence-lanes.toml:115-115. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:117-117. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:144-144. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:84-84. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:124-124. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_state_signal_curator_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:121-121. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `mcp/tests/test_knowledge_candidate_workspace.py` in the row 719 of this card from mcp/tests/test-evidence-lanes.toml:69-69 to mcp/tests/test-evidence-lanes.toml:70, the extent of the construct the claim is about (the checker named line(s) [70] as its live location); re-pointed `mcp/tests/test_knowledge_label_operations.py` in the row 717 of this card from mcp/tests/test-evidence-lanes.toml:18-19 to mcp/tests/test-evidence-lanes.toml:72, the extent of the construct the claim is about (the checker named line(s) [72] as its live location); re-pointed `mcp/tests/test_knowledge_snapshot_publication.py` in the row 719 of this card from mcp/tests/test-evidence-lanes.toml:70 to mcp/tests/test-evidence-lanes.toml:79, the extent of the construct the claim is about (the checker named line(s) [79] as its live location); re-pointed `migration` in the row 700 of this card from mcp/tests/test-evidence-lanes.toml:232-232 to mcp/tests/test-evidence-lanes.toml:260, the extent of the construct the claim is about (the checker named line(s) [260] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): stamped the untimestamped Update History entries with this document's own commit clock
- 2026-09-17T03:31:11+02:00 — **Historical stamp carried from the incoming official line** (merge HEAD `12bd7fd3`; the live stamp for this file is the later synced value in the metadata table above, which closeout re-stamps): `lastUpdated` 2026-09-15T15:02+02:00; `lastVerifiedCommitHash` `806649b91bdce18f7b915bfbbf6727967f4e7a88`; `lastVerifiedCommitDate` 2026-09-16T12:23:53+02:00.
- 2026-09-17T03:15+02:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): **recorded this leaf's two lane rows and re-measured the whole manifest rather than carrying L7's numbers.** The rows are `test_knowledge_diff_scope.py` (unit-regression, `:76`, 13 hermetic nodes) and `test_knowledge_diff_boundaries.py` (integration, `:159`, 15 nodes that drive the **production Git probe** over two real committed trees and a real curated candidate database) — each the module's behaviour-preserving classification, not a budget consequence. **The measured account: 243 declared entries against 243 modules on disk**, closed in both directions, 0 duplicates, with unit-regression 143 (`5-149`), public-contract 2 (`150-153`), integration 68 (`154-223`), architecture-fitness 17 (`224-242`), provider-conformance 13 (`243-257`) and the two empty lanes; against 241/241 after L7 and 238/238 on the merged base, so this leaf's two modules are the whole difference. The shared support module is named as a *governed artifact* (`knowledge-diff-cases`) rather than a lane row, and the card records that **the read-scope artifact's consumer list gained the same two paths** in this change. **The budget pair did not move**: 1250 / 340 with `pyproject.toml` clean, and the sizing question and its merged-line attribution are left exactly where L7 recorded them. The sentence that said the merged counts were pending now points at this leaf's measured account, and the earlier accounts are kept as as-of records. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): **recorded this leaf's three lane rows and, as the closing curator, produced the merged measurement the two labelled accounts were waiting for.** The rows are `test_knowledge_read_scope.py` (unit-regression, `:75`), `test_knowledge_read_boundaries.py` (integration, `:157`) and `test_knowledge_read_paths.py` (integration, `:158`), with the split explained as what it is — the 1 200-line hard limit was paid, not waived — and the shared support module named as a *governed artifact* rather than a lane row. **The merged counts are measured, not derived:** 241 declared entries against 241 modules on disk, with unit-regression 142 (`6-148`), public-contract 2 (`150-152`), integration 67 (`154-221`), architecture-fitness 17 (`223-240`), provider-conformance 13 (`242-255`) and the two empty lanes, and the merged base's own 238/238 recorded beside them so the difference is attributable rather than merged. The sentence that said the merged counts were *pending* now says they were measured and where they are recorded, and the earlier accounts are kept as as-of records under the memory doctrine. The card also carries the raised budget pair **1250 / 340** with the merged-line attribution stated as measured (official 1014/1100 green, KS parent 1003/1100 green, merged 1138/1100 red *before any L7 line*), the note that the raise is headroom rather than a target, and this leaf's own populations (unit 1138 → 1159, integration 279 → 304). Verification metadata remains empty until closeout stamps the code commit.

- 2026-09-16T17:45+02:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): registered the change set's two new knowledge modules and re-measured the whole manifest rather than carrying the L5 numbers — **221 declarations and 221 modules on disk**, with the current brackets unit-regression 127 at rows 6-132, public-contract 2 at 135-136, integration **63** at 139-201, architecture-fitness 16 at 204-219 and provider-conformance 13 at 222-234. Both additions are `test_knowledge_portable_roundtrip.py` and `test_knowledge_portable_boundaries.py` in the **integration** lane (rows 140-141), and the lane is forced rather than preferred: the unit population sits exactly at its declared 1000-case ceiling, and both modules are boundary executors (real databases under `tmp_path`, published closed files, destination bytes and directory contents measured). **The declared budget pair is corrected in this card**: `integration_case_budget` is now **300** at `pyproject.toml:186` (raised by this leaf's fix round with the doctrine-required dated tradeoff above the pair) and `unit_case_budget` stays **1000** at `pyproject.toml:185`; every earlier entry's `250` at `pyproject.toml:150` is stale, including the reference row that carried it — which is also the one pre-existing `citation_claim_reopened` finding this card owned, so that finding is cleared by re-pointing the claim at the key's current line and value. The lane-section layout is unchanged but a new leading section carries the current account so a reader does not have to reconstruct it from eight historical as-of records. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l06`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): registered the change set's two new knowledge modules and re-measured the whole manifest rather than carrying the L4 numbers — **219 declarations and 219 modules on disk**, with the current brackets unit-regression 127 at rows 6-133, public-contract 2 at 135-136, integration 61 at 139-200, architecture-fitness 16 at 202-218 and provider-conformance 13 at 220-233. The two additions are `test_knowledge_guarded_merge.py` in **unit-regression** (row 73) and `test_knowledge_guarded_merge_boundaries.py` in **integration** (row 139); the split is a budget decision, because the unit population sits exactly at its declared 1000-case ceiling after this leaf and each boundary scenario needs its own three-commit Git world. Every entry-row citation in this card below the insertions was re-derived against the new bytes. Verification metadata remains closeout-owned.
- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): registered the change set's two new knowledge modules in the **unit-regression** lane — `test_knowledge_candidate_workspace.py` at row 69 and `test_knowledge_snapshot_publication.py` at row 75 — and re-measured the manifest rather than carrying the L3 numbers: **217 modules on disk and 217 declared entries** with no undeclared module and no stale row, 126 unit-regression (6-131), 2 public-contract (134-135), 60 integration (138-197), 16 architecture-fitness (200-215), 13 provider-conformance (218-230), and stress-durability (232) and migration (234) empty. Both modules are hermetic — `tmp_path` directories, in-process APSW databases driven through the real admitted destination and the real publication lock, and a child interpreter used only as a crash probe — so the default unit lane is each one's behaviour-preserving classification. Their insertion inside the alphabetical knowledge block is why the rows are 69 and 75 rather than adjacent, and it is also why every entry-row citation below moved by two: **this pass re-derived all of them against the working manifest** (the `unit-regression`, `integration`, `architecture-fitness`, `provider-conformance`, `stress-durability` and `migration` row citations plus the twelve per-leaf row citations), which clears the pre-existing `citation_anchor_absent_from_range` findings this card carried. Classification only, so lane membership is not execution or acceptance evidence; verification metadata remains closeout-owned.
- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): registered the change set's three new knowledge modules in the **unit-regression** lane — `test_candidate_batch_commands.py` and `test_candidate_batch_transaction.py` at entry rows 18-19, `test_knowledge_label_operations.py` at row 70; all three are hermetic and driven through the real admitted destination, no integration marker, no repository or subprocess — and re-measured the manifest rather than carrying the L2 numbers: 215 modules on disk and 215 declared entries with no undeclared module and no stale row, 124 unit-regression (5-130), 2 public-contract (131-134), 62 integration (135-196), 18 architecture-fitness (197-214), 13 provider-conformance (215-229), stress-durability and migration empty. The five earlier knowledge modules are now at rows 69-74 and were re-cited. Recorded again why the rows are load-bearing rather than bookkeeping: an unregistered module makes `load_lane_manifest` refuse the repository, which raises at collection. Classification only, so lane membership is not execution or acceptance evidence; verification metadata remains closeout-owned.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base
  `60e0820e`): registered the change set's four new knowledge modules in the **unit-regression** lane
  at entry rows 67-70 — `test_knowledge_family_revision.py`, `test_knowledge_graph_reads.py`,
  `test_knowledge_relation_rules.py` and `test_knowledge_revision_seals.py`; all four are hermetic
  (temporary directories, in-process APSW databases, no integration marker, no repository or
  subprocess), so the default unit lane is each one's behaviour-preserving classification — and
  re-measured the manifest rather than carrying the L1 numbers: 212 modules on disk and 212 declared
  entries with no undeclared module and no stale row, 121 unit-regression (entries 6-126), 2
  public-contract (129-130), 60 integration (133-192), 16 architecture-fitness (195-210), 13
  provider-conformance (213-225), stress-durability and migration empty. One of the four arrived in
  the fix-verification round as the evidence repair for sealed finding `260915-KS-L2-RV-1`, and its
  row was added in the same change. Recorded again why the rows are load-bearing rather than
  bookkeeping: an unregistered module makes `load_lane_manifest` refuse the repository, which raises
  `pytest.UsageError` at collection and quietly drops the quality path's retry proof. Classification
  only, so lane membership is not execution or acceptance evidence; verification metadata remains
  closeout-owned.


- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base
  `67b21aeb`): registered the change set's new `mcp/tests/test_knowledge_store.py` in the
  **unit-regression** lane at entry row 67 — the module is hermetic (temporary directories, in-process
  APSW databases, no integration marker, no repository or subprocess), so the default unit lane is its
  behaviour-preserving classification — and re-measured the manifest rather than carrying the L3
  numbers: 208 modules on disk and 208 declared entries with no undeclared module and no stale row,
  117 unit-regression (entries 6-122), 2 public-contract (125-126), 60 integration (129-188),
  16 architecture-fitness (191-206), 13 provider-conformance (209-221), stress-durability and
  migration empty. Recorded why the row is load-bearing rather than bookkeeping: an unregistered
  module makes `load_lane_manifest` refuse the repository, which raises `pytest.UsageError` at
  collection and quietly drops the quality path's retry proof. Classification only, so lane
  membership is not execution or acceptance evidence; verification metadata remains closeout-owned.


---

- 2026-09-15T21:40+02:00 — 260831-LOCR-L05 curator, **re-dispatch** (uncommitted change set on
  `ar/260831-locr-l05`, pair code base `67c91534`, memory base `309110f8`,
  `mcp/tests/test-evidence-lanes.toml` +1/−0): registered the change set's new
  `mcp/tests/test_state_signal_worker_wake.py` in the **unit-regression** lane at file line `:105`,
  immediately below `test_state_signal_restart_recovery.py` at `:104` and above
  `test_structural_dispatch_recovery.py` at `:106` — the module seeds owned worker and manager seats
  on a real `TerminalCatalog`, drives the real `run_agent_notifier_sweep` over a temporary
  coordination root with real task documents and the real durable stores, issues no HTTP request,
  starts no server and starts no process, and asserts the whole inbox store rather than its
  state-signal subset, so the hermetic default unit lane is its behaviour-preserving classification.
  Re-measured the manifest against the candidate rather than carrying the L06 numbers: 216 modules on
  disk and 216 manifest entries, every module listed exactly once and no path duplicated — 123
  unit-regression (key `:5`, rows 6-128), 2 public-contract (key `:130`), 62 integration (key `:134`),
  16 architecture-fitness (key `:198`) and 13 provider-conformance (key `:216`), with
  stress-durability (`:231`) and migration (`:233`) empty; the live test-module derivation and the
  manifest therefore agree module for module and the fail-closed load holds. No existing row changed
  lane and no case budget was raised (the declared case budgets live in `pyproject.toml`, which is
  their authority). **Every citation in this card and in `overview.md` whose anchored row this
  insertion moved was re-derived against the candidate rather than carried** — the insertion sits in
  the unit run above the rows those tables cite, so 20 citations in this card and 8 in the route
  overview moved by one line and were repointed; the 686 `style.citations.range_resolution` findings
  the up-front check reports are pre-existing legacy drift on other files and were left alone. Scope
  note: this is a preservation leaf — `mcp/src` is byte-unchanged (`git status --porcelain` = the
  modified manifest plus the untracked module; `mcp/src` diff = 0 files). Classification only: lane
  membership is not execution, certification or acceptance evidence, and the verification stamps
  remain closeout-owned.


- 2026-09-15T21:25+02:00 — 260831-LOCR-L04 curator (uncommitted change set on `ar/260831-locr-l04`,
  base `e9678c56`, `mcp/tests/test-evidence-lanes.toml` +1/−0): registered the change set's new
  `mcp/tests/test_serving_notifier_handoff.py` in the **unit-regression** lane at file line `:97`,
  between `test_semantic_topology_refusals.py` at `:96` and `test_serving_observation_loop.py` at `:98`.
  The module is the proof half of a preservation leaf: it enters the real `_serving_lifespan` under a
  deadline-correct virtual clock and measures the observer-to-notifier handoff latency against the
  oracle's bound and its decomposition, with no HTTP request, no server and no process, so the hermetic
  default unit lane is its behaviour-preserving classification. The leaf's two support modules
  (`_handoff_clock.py`, `_serving_handoff.py`) take no row, by the same rule that keeps the directory's
  other support modules out of the manifest. Re-measured at base `e9678c56` plus this change set:
  **215** modules on disk and **215** manifest entries — unit-regression **122** (key `:5`, rows 6-127,
  next key `:129`), public-contract 2 (`:129`), integration 62 (`:133`, rows 134-195),
  architecture-fitness 16 (`:197`), provider-conformance 13 (`:215`), stress-durability (`:230`) and
  migration (`:232`) empty. No case budget is quoted here and none was raised; `pyproject.toml` is the
  authority. **Because this insertion at `:97` sits above every previously-latest unit row, it moved
  every later manifest line by one**, so the citations into this file were re-derived against the
  current manifest rather than carried — 59 live citations in this card, the tests route overview and
  fifteen sibling cards; dated `## Update History` entries were left as written as-of records, and one
  citation already stale before this leaf (the L34 boundary suite at `:143-143` → `:140-140`) was
  corrected to the line that carries it. Verification metadata remains closeout-owned; no stamp
  advanced.


- 2026-09-15T21:21+02:00 — 260831-LOCR-L06 curator, **re-dispatch** (uncommitted change set on
  `ar/260831-locr-l06`, pair code base `e9678c56`, memory base `ee93a0fc`,
  `mcp/tests/test-evidence-lanes.toml` +1/−0): registered the change set's new
  `mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py` in the **unit-regression** lane at
  file line `:68`, immediately below `test_lifecycle_operation_model_helpers.py` at `:67` and above
  `test_memory_attribution_producers.py` at `:69` — the module drives the real terminal observer, the
  production terminal-evidence lift and the real notifier sweep over a temporary coordination root,
  with no HTTP request, no server and no process, so the hermetic default unit lane is its
  behaviour-preserving classification. Re-measured the manifest against the candidate rather than
  carrying the L17 numbers: 215 modules on disk and 215 manifest entries — 122 unit-regression (key
  `:5`, rows 6-127), 2 public-contract (key `:129`), 62 integration (key `:133`), 16
  architecture-fitness (key `:197`), 13 provider-conformance (key `:215`), stress-durability (`:230`)
  and migration (`:232`) empty. Unlike the L17 and L18 insertions this row lands **above** the rows
  this card cites, so every manifest citation in the module table at or below `:68` was re-derived
  against the candidate — the L4/L5/L7/L8/L23/L27/L34/L36/L37/L01/L17 module rows plus the
  `integration` and `stress-durability` key lines — and this card's purpose paragraph was
  re-measured with them. `LOCR-R09@v1`, `LOCR-R11@v1` and `LOCR-R18@v1` classifications are
  untouched: no existing row changed lane and no case budget was raised, the budget authority
  remaining `pyproject.toml`. The leaf is a preservation leaf, so no production byte moved.
  Verification metadata remains closeout-owned; no stamp advanced.


- 2026-09-15T21:19+02:00 — 260831-LOCR-L07 curator (uncommitted change set on `ar/260831-locr-l07`,
  base `e9678c56`, `mcp/tests/test-evidence-lanes.toml` +1/−0): registered the change set's new
  `mcp/tests/test_state_signal_curator_wake.py` in the **unit-regression** lane at file line `:102`,
  between its two alphabetically adjacent state-signal siblings — the module drives the real
  `TerminalCatalogLivenessSweeper`, the real agent-notifier sweep and the real `run_agent_notifier_sweep`
  over temporary catalogs, an in-process tmux host and an accepting paster double, with no HTTP
  request, no server and no process, so the hermetic default unit lane is its behaviour-preserving
  classification, the same lane its three siblings hold for the same reason. Re-measured the manifest
  against the candidate rather than carrying the L17 numbers: **215** modules on disk and 215 manifest
  entries — 122 unit-regression (key `:5`, bracket `:5-127`), 2 public-contract (key `:129`), 62
  integration (key `:133`, bracket `:134-195`), 16 architecture-fitness (key `:197`), 13
  provider-conformance (key `:215`), with stress-durability (`:230`) and migration (`:232`) empty. The
  Purpose paragraph now opens with that measured population instead of the L17 214-module figure it
  previously presented as current, and the L17 measurement is retained below as its own as-of record.
  Every live line reference in the module table that this insertion moved (target line `:102` or
  below) was re-derived against the manifest as it now stands; three of them — the L34, L36 and L37
  rows — were already four to six lines adrift of the source before this leaf and are now cited at
  their measured lines, and the per-row prose "row N now" figures of an earlier era were left as
  found. This is a preservation leaf: `mcp/src` is unchanged by the change set, and no case budget was
  touched — `pyproject.toml` remains the authority for the pinned budgets. Classification only: lane
  membership is not execution, certification or acceptance evidence, and the verification stamps
  remain closeout-owned.


- 2026-09-15T20:42+02:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`,
  base `99534dc5`, `mcp/tests/test-evidence-lanes.toml` +1/−0): registered the change set's new
  `mcp/tests/test_terminal_observer_health.py` in the **unit-regression** lane at file line `:122`,
  immediately below `test_terminal_liveness_registration_order.py` at `:121` — the module drives
  the record, the writer, the serving-lifetime accumulator and the real `_state_response` handler
  and `stream_events` generator against stub projectors, with no HTTP transport, no server and no
  process, so the hermetic default unit lane is its behaviour-preserving classification. Re-measured
  the manifest against the candidate rather than carrying the L18 numbers: 214 modules on disk and
  214 manifest entries — 121 unit-regression (key `:5`, rows 6-126), 2 public-contract (key
  `:128`), 62 integration (key `:132`), 16 architecture-fitness (key `:196`), 13 provider-conformance
  (key `:214`), stress-durability (`:229`) and migration (`:231`) empty. The insertion sits below
  `test_serving_observation_loop.py` (`:97`) and `test_serving_startup_prime.py` (`:98`), so no row
  this card cites from `LOCR-R11@v1` or `LOCR-R18@v1` moved; the L18 measurement is retained below
  as its own as-of record. Every line reference in the module table was re-derived against the
  candidate (the L34/L36/L37/L38 and seal-removal rows had drifted by one to six lines as later
  insertions moved them). Verification metadata remains closeout-owned; no stamp advanced.


- 2026-09-15T15:02+02:00 — 260831-LOCR-L18 curator (uncommitted change set on `ar/260831-locr-l18`,
  base `d868486c`): registered the change set's new `mcp/tests/test_serving_startup_prime.py` in the
  **unit-regression** lane at file line `:98`, immediately below its sibling
  `test_serving_observation_loop.py` at `:97` — the module drives the real `_serving_lifespan` under a
  temporary catalog, a virtual clock, an in-process fake tmux host and parked sibling loops, with no
  HTTP request and no process, so the hermetic default unit lane is its behaviour-preserving
  classification, the same lane and reason as its sibling. Re-measured the manifest against the
  candidate rather than carrying the L27 numbers: 213 modules on disk and 213 manifest entries — 120
  unit-regression (key `:5`, bracket `:5-125`, next key `:127`), 2 public-contract (`:127`), 62
  integration (key `:131`, bracket `:131-193`), 16 architecture-fitness (`:195`), 13
  provider-conformance (`:213`), with stress-durability (`:228`) and migration (`:230`) empty. The
  Purpose paragraph now opens with that measured population instead of the L27 211-module figure it
  previously presented as current, and three reference rows were added (the L18 row, the
  unit-regression bracket, the integration bracket). No existing row changed lane and no case budget
  was raised; the integration ceiling stays 250 (`pyproject.toml:150`). Classification only: lane
  membership is not execution, certification or acceptance evidence, and the verification stamps
  remain closeout-owned.


- 2026-09-15T13:57+02:00 — 260831-LOCR-L02 curator (uncommitted change set on `ar/260831-locr-l02`,
  base `67b21aeb`): registered the change set's new `mcp/tests/test_serving_terminal_catalog_read.py`
  in the **integration** lane (entry row 171) — it drives the real registered route over
  `fastapi.testclient.TestClient` and the real composed `create_app`, so the boundary lane is its
  behaviour-preserving classification — and re-measured the manifest rather than carrying a count:
  208 modules on disk and 208 manifest entries, 116 unit-regression, 2 public-contract, 61
  integration, 16 architecture-fitness, 13 provider-conformance, stress-durability and migration
  empty, with the 250-case integration ceiling (`pyproject.toml:150`) unchanged and no budget raised.
  A `## 260831-LOCR-L02 Lane Row (Declared)` section records the measurement and states explicitly
  that it is this leaf's as-of population over base `67b21aeb`, because concurrent sibling leaves
  landed their own rows on the same source branch. The Purpose paragraph gained the matching clause.
  Verification metadata stays closeout-owned: the candidate is uncommitted, so no stamp advanced.

- 2026-09-15T13:36+02:00 — 260831-LOCR-L27 curator (uncommitted change set on `ar/260831-locr-l27`,
  base `b368b661`): registered the change set's new `mcp/tests/test_terminal_liveness_pane_authority.py`
  in the **integration** lane at file line 181, between `test_terminal_liveness.py` at `:180` and
  `test_tools.py` at `:182`. The module is hermetic, but it takes the lane of its sibling
  `test_terminal_liveness.py`, and a new module of this family needs its own row or its application
  imports run inside ordinary unit collection — that is why the leaf added a lane entry at all. The
  module is the family's first **addition** rather than an extension: extending
  `test_terminal_liveness.py` in place reached 1094 lines, inside the `system/coding-guidelines.md`
  900-1200 band, so the proof was split out and the sibling stayed byte-unchanged. Re-measured the
  manifest rather than carrying the L23 numbers: 209 modules on disk and 209 manifest entries, 117
  unit-regression (file lines 5-123), 2 public-contract (124-127), **61** integration (128-190), 16
  architecture-fitness (191-208), 13 provider-conformance (209-223), stress-durability and migration
  empty. The insertion moved only the integration, architecture-fitness and provider-conformance file
  lines and left every unit-regression and public-contract row untouched; no existing row changed lane
  and no case budget was raised (the integration ceiling stays 250, `pyproject.toml:150`). Three stale
  bracket citations in this card's Repo-Internal References table were repaired in the same pass, and
  the Purpose paragraph now opens with the current population before the L23-measured text it
  previously presented as current. Classification only: lane membership is not execution,
  certification or acceptance evidence, and the verification stamps remain closeout-owned.


- 2026-09-15T13:36+02:00 — 260831-LOCR-L27 curator, **post-sync reconciliation** (same change set;
  the memory sync advanced the base from `b368b661` to `163ba8a9` and parked this card's WIP over the
  two incoming memory commits): the sync brought L01's own declared-row section into this card, which
  collided with the L27 section above in the same region, so both sections were kept and reconciled
  rather than one being dropped. The incoming line numbers were re-measured rather than carried: at
  base `163ba8a9` **plus** this change set the manifest holds 209 modules on disk and 209 entries —
  118 unit-regression (key `:5`, next key `:125`), 2 public-contract (`:125`), 61 integration
  (`:129`), 16 architecture-fitness (`:192`), 13 provider-conformance (`:210`), with
  stress-durability (`:225`) and migration (`:227`) empty. L01's unit-lane insertion at `:97` moved
  every row below it down one line, so this module's own row now sits at `:182` (it was `:181` on this
  candidate's build base, which is the figure the leaf's verdict and worker report cite), and the
  Purpose paragraph and the three later lane-bracket citations were recomputed against that base. No
  row changed lane and no case budget moved. The merge is a memory-side reconciliation only: no
  production byte and no entry in the manifest itself was authored by this pass.


- 2026-09-15T13:36+02:00 — 260831-LOCR-L27 curator, **second post-sync reconciliation** (final
  measurement for this leaf; the base advanced once more, `163ba8a9` → `52bee429`, as L10 landed in the
  unit lane): the memory sync fast-forwarded cleanly with all five of this card's change-set files
  restored, and the manifest was re-measured at the new base **plus** this change set: 211 modules on
  disk and 211 manifest entries — 119 unit-regression (key `:5`, next key `:126`), 2 public-contract
  (`:126`), 61 integration (`:130`), 16 architecture-fitness (`:193`), 13 provider-conformance
  (`:211`), with stress-durability (`:226`) and migration (`:228`) empty. This module's row sits at
  file line `:183`, entry ordinal **53 of 61** in the integration lane, between
  `test_terminal_liveness.py` at `:182` and `test_tools.py` at `:184`. **This is the figure the card
  now carries**; `:182` was the `163ba8a9` measurement and `:181` is this candidate's build base,
  which the leaf's verdict and worker report cite. The unit-regression bracket citation was corrected
  from `:5-124` to `:5-125` in the same pass. Every one of these shifts is a sibling unit-lane
  insertion moving the file lines of a row this leaf never touched: this leaf's own manifest delta is
  exactly one inserted integration row and no lane, budget or production change. Verification metadata
  is pinned to `52bee429` (code) — the closeout transaction stamps the final commit.


- 2026-09-15T13:20+02:00 — 260831-LOCR-L23 curator (uncommitted change set on `ar/260831-locr-l23`,
  base `67b21aeb`): registered the change set's new `mcp/tests/test_terminal_liveness_registration_order.py`
  in the **unit-regression** lane at entry row 118 — the module drives the real `TerminalCatalog` over
  `tempfile` catalogs and the real `TerminalCatalogLivenessSweeper.refresh` with in-process
  registrar/compactor doubles and no `worktree_services`, so it is hermetic and the default unit lane
  is its behaviour-preserving classification, the same lane as its sibling at `:117`. Re-measured the
  manifest rather than carrying the L3 numbers: 208 modules on disk and 208 manifest entries, 117
  unit-regression (5-122), 2 public-contract (123-126), 60 integration (127-188), 16
  architecture-fitness (189-206), 13 provider-conformance (207-221), with stress-durability (222-223)
  and migration (224-225) empty. The insertion moved **no** other row: row 118 is bracketed by
  `test_terminal_liveness_deferred_work.py` at `:117` and `test_terminal_paste.py` at `:119`, both
  alphabetically adjacent, so every citation below that does not name the unit bracket is unchanged;
  the Purpose population sentence and the unit bracket citation were the two that moved. No lane
  changed and no case budget was raised. Classification only: lane membership is not execution,
  certification or acceptance evidence, and the verification stamps remain closeout-owned.

- 2026-09-15T13:19+02:00 — 260831-LOCR-L01 curator (uncommitted change set on `ar/260831-locr-l01`,
  base `67b21aeb`): registered the change set's new `mcp/tests/test_serving_observation_loop.py` in
  the **unit-regression** lane at entry row 97 — the module injects fakes, issues no HTTP request,
  starts no process and publishes nothing, so the default unit lane is its behaviour-preserving
  classification — and re-measured the manifest rather than carrying the L3 numbers: 208 modules on
  disk and 208 manifest entries, 117 unit-regression (key `:5`), 2 public-contract (`:124`),
  60 integration (`:128`), 16 architecture-fitness (`:190`), 13 provider-conformance (`:208`), with
  stress-durability (`:223`) and migration (`:225`) empty. The insertion sits at `:97` between
  `test_semantic_topology_refusals.py` and `test_signal_routing.py`, so every later lane key is one
  line higher than the L3 entry recorded; the Purpose paragraph's 207/207 and 116 figures are that L3
  measurement, not this one. Because the insertion moves every later row, this card's own lane
  citations were re-derived against the current manifest rather than carried:
  `test_state_signal_boundary_delivery.py` `:99` → `:100`, `test_checkpoint_landing_end_to_end.py`
  `:134` → `:135`, `test_closeout_projection_source_classification.py` `:138` → `:139`,
  `test_cross_master_concurrency.py` `:146` → `:147`, `test_leaf_doc_master_link_binding.py` `:154` →
  `:155`, the playthrough `:157` → `:158`, `test_pause_stop_only_end_to_end.py` `:163` → `:164`,
  `test_terminal_blocker_reasons.py` `:178` → `:179`,
  `test_worktree_status_terminal_next_tool.py` `:184` → `:185`,
  `test_pause_is_not_publication.py` `:196` → `:197`, the `integration` lane key `:127` → `:128`, and
  the empty-lane keys `:222`/`:224` → `:223`/`:225`; the four lane brackets were re-measured the same
  way (`unit-regression` `5-121` → `5-122`, `integration` `127-188` → `128-189`,
  `architecture-fitness` `189-206` → `190-207`, `provider-conformance` `207-221` → `208-222`).
  Classification only: lane membership is not execution or acceptance
  evidence, and the verification stamps remain closeout-owned.


- 2026-09-15T13:15+02:00 — 260831-LOCR-L10 curator: registered the change set's new `mcp/tests/test_state_signal_restart_recovery.py` in the **unit-regression** lane at entry row `:101` — its seven cases drive one temporary durable world per case through the retained sweep/action entry points with an injected store fault or a structural rebind, so the hermetic default lane is its behaviour-preserving classification — and re-measured the manifest rather than carrying the L3 numbers: 208 modules on disk and 208 manifest entries, 117 unit-regression (5-122), 2 public-contract (124-126), 60 integration (128-188), 16 architecture-fitness (190-206), 13 provider-conformance (208-221), stress-durability and migration empty. The insertion sits near the end of the unit run, so no row this card cites moved. The module's own card owns the case inventory; this row is selection and cost classification only. Verification metadata remains closeout-owned.

- 2026-09-14T17:20+02:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base
  `7317108b`): registered the change set's new `mcp/tests/test_memory_backfill.py` in the
  **unit-regression** lane at entry row 69 — its cases drive the backfill plan and apply paths against
  disposable `tempfile` repositories and the module carries no integration marker, so the default unit
  lane is its behaviour-preserving classification — and re-measured the manifest rather than carrying
  the L8 numbers: 207 modules on disk and 207 manifest entries, 116 unit-regression (5-121), 2
  public-contract (123-126), 60 integration (127-188), 16 architecture-fitness (189-206), 13
  provider-conformance (207-221), with stress-durability (222-223) and migration (224-225) empty. The
  insertion sits at `:69`, so every cited row below it moved one line and was re-cited:
  `test_state_signal_boundary_delivery.py` `:98` → `:99`, `test_checkpoint_landing_end_to_end.py`
  `:133` → `:134`, `test_cross_master_concurrency.py` `:145` → `:146`,
  `test_lifecycle_playthrough_end_to_end.py` `:156` → `:157`, `test_pause_stop_only_end_to_end.py`
  `:162` → `:163`, `test_terminal_blocker_reasons.py` `:177` → `:178`,
  `test_worktree_status_terminal_next_tool.py` `:183` → `:184`, `test_pause_is_not_publication.py`
  `:195` → `:196`, `test_leaf_doc_master_link_binding.py` `:153` → `:154`,
  `test_closeout_projection_source_classification.py` `:137` → `:138`, the L38 `integration` key
  `:126` → `:127`, and the empty-lane keys `:221`/`:223` → `:222`/`:224`.
  `test_checkpoint_landing.py` (`:24`) and `test_memory_attribution_producers.py` (`:68`) sit above the
  insertion and are unchanged, and the Purpose paragraph plus the L5, L7 and L8 bracket notes were
  corrected to the measured L3 population; classification only, so lane membership is not execution
  or acceptance evidence and the verification stamps remain closeout-owned.

- 2026-09-14T15:05+02:00 — 260913-LCA-L8 curator (uncommitted change set on `ar/260913-lca-l8-ar`):
  registered the change set's new `mcp/tests/test_terminal_blocker_reasons.py` in the **integration**
  lane (entry row 177) — it builds a real landed leaf over disposable code and external-memory
  repositories and drives the public landing, integration and `lifecycle_finalize_task` routes, so
  that is its behaviour-preserving lane — and reconciled the population and every lane bracket against
  the current manifest, measured rather than carried: 206 modules on disk and 206 manifest entries,
  115 unit-regression (5-120), 2 public-contract (122-124), 60 integration (126-186), 16
  architecture-fitness (188-204), 13 provider-conformance (206-219), with stress-durability and
  migration empty. The same change set also corrected three out-of-order consumer entries in
  `evidence-lifecycle.toml`, which moves the L5 row up one line (`:316` → `:315`) and the L4 row down
  one (`:319` → `:320`) without changing any lane. Two rows this card cites after the insertion are
  one line higher than the L7 entry recorded: `test_worktree_status_terminal_next_tool.py`
  `:182` → `:183` and `test_pause_is_not_publication.py` `:194` → `:195`; re-derived the bracket rows
  (`126-185` → `126-186`, `187-203` → `188-204`, `205-218` → `206-219`, the empty-lane keys
  `220-220`/`222-222` → `221-221`/`223-223`) and corrected two rows that were already one line short
  of their entries (`test_checkpoint_landing_end_to_end.py` `:132` → `:133` and
  `test_cross_master_concurrency.py` `:143` → `:145`). Classification only: lane membership is not
  execution or acceptance evidence, and the verification stamps remain closeout-owned.

- 2026-09-14T14:20+02:00 — 260913-LCA-L7 curator (uncommitted change set on `ar/260913-lca-l7`):
  registered the change set's new `mcp/tests/test_closeout_projection_source_classification.py` in the
  **integration** lane (entry row 137) — it composes the real `QueueFixture` over temporary Git
  repositories and drives the production graph admission and projection path, so that is its
  behaviour-preserving lane — and reconciled the population and every lane bracket against the current
  manifest, measured rather than carried: 205 modules on disk and 205 manifest entries, 115
  unit-regression (5-120), 2 public-contract (122-124), 59 integration (126-185), 16 architecture-fitness
  (187-203), 13 provider-conformance (205-218), with stress-durability and migration empty. The single
  insertion sits before rows this card cites, so each of them is one line higher than the L5 entry
  recorded: `test_leaf_doc_master_link_binding.py` `:152` → `:153`, the playthrough `:155` → `:156`, the
  pause suite `:161` → `:162`, the L32 suite `:181` → `:182` and the pause architecture guard `:193` →
  `:194`, with the integration bracket `126-184` → `126-185`; added the L7 registration row and the
  reference row for it, and left every per-leaf section above as its own as-of record. Classification
  only: lane membership is not execution or acceptance evidence, and the verification stamps remain
  closeout-owned.

- 2026-09-14T07:05+02:00 — 260913-LCA-L5 curator (uncommitted change set on `ar/260913-lca-l5-ar`, base
  `52875e7a`): registered the change set's new `mcp/tests/test_leaf_doc_master_link_binding.py` in the
  **integration** lane (entry row 152) — it drives the real public `worktree_start` over one disposable
  code repository and one external-memory repository per case, so that is its behaviour-preserving lane —
  and reconciled the population and every lane bracket against the current manifest, measured rather than
  carried from the previous entry: 204 modules on disk and 204 manifest entries, 115 unit-regression
  (entry rows 6-120), 2 public-contract (123-124), 58 integration (127-184), 16 architecture-fitness
  (187-202), 13 provider-conformance (205-217), with stress-durability and migration empty. **Also
  corrected the L4 section, which recorded an open gap that no longer exists**: measured at base
  `52875e7a`, `test_memory_attribution_producers.py` holds its lane row at `:68` in `unit-regression`, so
  the 203-modules/203-entries population held at this leaf's base and the fail-closed load failure the L4
  entry predicted was already repaired by the commit that landed L4. Re-derived every position this card
  cites against the current manifest by line number (integration `126-184`, architecture-fitness
  `186-202`, provider-conformance `204-217`, stress-durability `:219`, migration `:221`, the L38 row
  `:126`, `test_state_signal_boundary_delivery.py` `:98`, `test_worktree_status_terminal_next_tool.py`
  `:181`, the pause suite `:161`, the pause architecture guard `:193`, the playthrough `:155`) and added
  the L4 and L5 registration rows. The Purpose paragraph above carries pre-L4 counts and is superseded by
  the measured ones; classification only, lane membership is not execution or acceptance evidence, and
  the verification stamps remain closeout-owned.

- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`, base
  `5bb124d4`): **flagged an open gap rather than repairing it, because the file itself is unchanged and
  the repair is code work.** The change set added `mcp/tests/test_memory_attribution_producers.py` and
  declared no lane row for it, so the manifest's closed population no longer holds: measured by diffing
  the disk file list against the manifest, 203 `test_*.py` modules exist and 202 are declared, the one
  undeclared path being the new module, with no stale row pointing at a missing file. Because
  `load_lane_manifest` refuses a manifest that omits a module, this is the same hard load failure the
  card already records from 260831-LOCR-L30, and `code_quality/check.py:677` is a consumer. Recorded in
  a new section with the measurement method, the derivation path (`testpaths` in the repository-root
  `pyproject.toml:155`), the consumer that fails, and the explicit statement that the lane choice is the
  builder's and is not asserted here. The manifest file itself is **not** modified by this curator pass.
  Verification metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-09-13T20:42+02:00 — Child-admission seal removal (uncommitted change set on
  `ar/260831_lifecycle-owned-completion-relay`): registered the change set's new
  `mcp/tests/test_lifecycle_playthrough_end_to_end.py` in the **integration** lane (entry row 153) —
  it plays the whole leaf-and-master lifecycle in order over one real temporary Git world through the
  public master-level operations, so that is its behaviour-preserving lane — and reconciled the
  population and every lane bracket against the current manifest, measured rather than carried from the
  previous entry: 202 modules on disk and 202 manifest entries, 114 unit-regression (entry rows 6-119),
  2 public-contract (122-123), 57 integration (126-182), 16 architecture-fitness (185-200), 13
  provider-conformance (203-215), with stress-durability and migration empty. The insertion shifted the
  three later rows this card cites (`test_worktree_status_terminal_next_tool.py` 178 → 179, the pause
  boundary suite 158 → 159, the pause architecture guard 190 → 191) and every lane bracket after
  integration. Also corrected two stale invariant bullets that still declared
  `integration_case_budget` as 200 at `pyproject.toml:134-135`; the measured source reads 250 at
  `pyproject.toml:150`, which the L37 entry had already recorded for the reference row. Classification
  only: lane membership is not execution or acceptance evidence, and the verification stamps remain
  closeout-owned.

- 2026-09-13T17:20:55+00:00: Generated citation repair: "stress-durability"; "migration" repointed to mcp/tests/test-evidence-lanes.toml:216-216; mcp/tests/test-evidence-lanes.toml:218-218. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:188-188. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "integration_case_budget" repointed to pyproject.toml:150-150. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37 citation review (curator-authored, not a mechanical
  projection): re-read the `integration_case_budget` claim against the current `pyproject.toml` and
  re-cited it to the key's own line, `pyproject.toml:150-150`, where the declared integration ceiling of
  250 now lives. The wording ("the integration lane's collected-case cap that constrains lane choice")
  holds: the cap is the reason the L37 additions and the L30/L34 restorations were classified as they
  were. The previous range arrived from a generated projection and is superseded by this curator
  confirmation.

- 2026-09-13T19:02+02:00 — 260831-LOCR-L37 curator: registered the leaf's two new modules —
  `mcp/tests/test_pause_stop_only_end_to_end.py` in the **integration** lane (entry row 158) because
  it drives the public pause over a real temporary Git world holding two atomic masters, and
  `mcp/tests/test_pause_is_not_publication.py` in **architecture-fitness** (entry row 190) because it
  is an AST-only import-closure guard that executes nothing. Reconciled the population and every lane
  bracket against the current manifest, measured rather than carried from the previous entry: 201
  modules on disk and 201 manifest entries, 114 unit-regression (entry rows 6-119), 2 public-contract
  (122-123), 56 integration (126-181), 16 architecture-fitness (184-199), 13 provider-conformance
  (202-214), with stress-durability and migration empty. Also corrected the stale cap sentence: the
  integration lane is capped at 250 collected cases (`pyproject.toml:150`), not 200. Classification
  only: lane membership is not execution or acceptance evidence, and the verification stamps remain
  closeout-owned.

- 2026-09-13T14:20:09+02:00 — 260831-LOCR-L36 curator: registered the leaf's new `mcp/tests/test_cross_master_concurrency.py` in the **integration** lane (row 143) — it drives two sprint-commanded atomic masters and the public land/resume operations over one real temporary Git world, so that is its behaviour-preserving lane — and reconciled the population and every lane bracket against the current manifest: 199 modules, 114 unit-regression (5-120), 2 public-contract (121-124), 55 integration (125-181), 15 architecture-fitness (182-198), 13 provider-conformance (199-213), with stress-durability (214-215) and migration (216-217) empty. The insertion shifted the L32 row (176 → 177) and every bracket after the integration block, all re-cited here. Classification only: lane membership is not execution or acceptance evidence, and the verification stamps remain closeout-owned.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:12+00:00 — 260831-LOCR-L34 curator: registered the leaf's new
  `mcp/tests/test_checkpoint_landing_end_to_end.py` in the **integration** lane (row 132) — it drives
  the public checkpoint and closeout operations over real temporary Git repositories under
  `tmp_path`, so that is its behaviour-preserving lane — and re-derived the population and every lane
  bracket against the current manifest: 198 modules, 114 unit-regression (5-120), 2 public-contract
  (121-124), 54 integration (125-180), 15 architecture-fitness (181-197), 13 provider-conformance
  (198-212), with stress-durability (213-214) and migration (215-215) empty. The insertion shifted the
  L32 row (175 → 176) and every later lane bracket, all re-cited here; also replaced the last stale
  "150 collected cases" bound in the L30 paragraph with the measured 200. Classification only: lane
  membership is not execution, certification or acceptance evidence, and verification metadata remains
  closeout-owned.

- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: registered the leaf's new
  `mcp/tests/test_worktree_status_terminal_next_tool.py` in the **integration** lane (row 175) — it
  drives real worktree services and a real repository under `tmp_path`, so that is its
  behaviour-preserving lane — and re-derived the population and every lane bracket against the
  current manifest: 197 modules, 114 unit-regression (5-120), 2 public-contract (121-124), 53
  integration (125-179), 15 architecture-fitness (180-196), 13 provider-conformance (197-211), with
  stress-durability (212-213) and migration (214-215) empty. Also corrected a stale bound rather than
  propagating it: `pyproject.toml:135` declares `integration_case_budget = 200`, not the 150 recorded
  in this card's earlier entries, so the two invariants and the purpose paragraph now cite the
  measured value. Classification only: lane membership is not execution, certification or acceptance
  evidence, and verification metadata remains closeout-owned.

- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: registered eight members
  (`test_checkpoint_landing.py`, `test_closeout_kept_rules_pins.py`,
  `test_memory_scope_task_derivation.py`, `test_post_integration_cleanup_guidance.py`,
  `test_record_landing.py`, `test_retired_door_publication_fields.py`,
  `test_automatic_post_integration_cleanup.py`, and
  `test_memory_quality_is_independent_of_the_closeout_plane.py`) and repaired a manifest that could
  not load: seven tracked modules — one of them shipped by the preceding leaf — declared no lane, and
  `load_lane_manifest` refuses an incomplete population. Re-derived the population to 196 (114
  unit-regression, 2 public-contract, 52 integration, 15 architecture-fitness, 13 provider-
  conformance) and every lane bracket citation. Classification only: lane membership is not
  execution, certification or acceptance evidence, and verification metadata remains closeout-owned.

- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `integration` repointed to mcp/tests/test-evidence-lanes.toml:119-119. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "unit-regression" repointed to mcp/tests/test-evidence-lanes.toml:6-6. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T15:06+02:00 — Parked-candidate lane registration: recorded the new `mcp/tests/test_sync_parked_candidate.py` row in the existing `unit-regression` lane and re-derived every lane-block citation shifted by it; reconciled the current population to 183 files (99 unit-regression, 55 integration). No case budget was raised. Verification metadata remains closeout-owned.
- 2026-09-10T12:23+02:00 — 260831-LOCR-L20 curator post-sync refresh: the leaf was synced forward to
  code `bb38d04e`, and the manifest union now holds 187 rows: 103 unit-regression, 2 public-contract,
  55 integration, 14 architecture-fitness and 13 provider-conformance (L28's landed
  `test_terminal_liveness_deferred_work.py` is the extra unit-regression row, inserted at line 104).
  This card's population prose and all six lane bracket citations were re-derived against the new tree,
  and the two synced conflicts were resolved hunk-by-hunk with the synced side authoritative for ranges
  and structure. One synced claim was **corrected rather than preserved**: that row described the
  integration population as "including the R28 deferred-work proof", but
  `test_terminal_liveness_deferred_work.py` registers in `unit-regression` at line 104, so the clause
  was dropped as contradicted by the current tree. Lane classification only; focused execution and any
  later acceptance remain separately owned.


- 2026-09-10T11:55:00+02:00 — Post-sync union curation for 260831-LOCR-L03: the landed LOCR master tip `bb38d04e` carried the sibling R28 registration and its own re-derivation of the authorized three-row CCR landing-debt repair, while this branch carried the L03 `test_terminal_evidence_mapping.py` row. Both rows are kept, sorted, and this card's population statement and all six lane citations were re-derived against the union to 187 declared modules (103 unit-regression, 2 public-contract, 55 integration, 14 architecture-fitness, 13 provider-conformance). The sibling's two-range empty-population citation for stress-durability/migration and its R28 attribution were retained, with the R28 attribution moved to the unit-regression row it actually belongs to. Supersedes the 186-module figures recorded below. Classification only; no execution, certification or acceptance claim.

- 2026-09-10T11:53+02:00 — 260831-LOCR-L09 curator: resolved this card's sync merge and re-derived the whole lane account against the merged manifest — 187 modules, 103 unit-regression / 2 public-contract / 55 integration / 14 architecture-fitness / 13 provider-conformance, with stress-durability and migration empty. Corrected every lane bracket range to current line numbers, replaced the ambiguous `integration` anchor (three resolutions at the verified commit) with the unique `"integration = ["` literal, split the former combined L38 row into its two module paths, and recorded this leaf's boundary-delivery module plus the three pre-existing omitted-row repairs already carried by LOCR-L28. Verification metadata is the merged base `bb38d04e`; the real commit stamp remains closeout-owned.

- 2026-09-10T11:52:46+02:00 — 260831-LOCR-L25 curator: resolved the merge with landed LOCR-L28 (`e26b55db`) and re-derived every lane bracket and the population against the synced manifest: 187 modules — 103 unit-regression (`5-109`), 2 public-contract (`110-113`), 55 integration (`114-170`), 14 architecture-fitness (`171-186`), 13 provider-conformance (`187-201`), with stress-durability (`202-203`) and migration (`204-205`) empty; every row unique and present on disk. Supersedes the 186 / 102 figures recorded above by both leaves. Classification only: lane membership is not execution or acceptance evidence, and verification metadata remains closeout-owned.

- 2026-09-10T11:25:00+02:00 — Authorized repair of a pre-existing manifest omission: `8885939e` created `test_review_state.py`, `test_task_doc_review_public.py` and `test_transaction_only_worktree_delivery.py` in the same change that edited this manifest, but their required rows were omitted, so `load_lane_manifest` could not resolve them. The three rows were restored as `unit-regression` - their behaviour-preserving lane, since a full run had already collected them unmarked - and this card's population statement and all six lane citations were re-derived to 186 declared modules (102 unit-regression, 2 public-contract, 55 integration, 14 architecture-fitness, 13 provider-conformance). Registering them as `integration` was rejected because that lane sits at its 150-case cap and collection fails. Classification only; no execution, certification or acceptance claim.

- 2026-09-10T11:24+02:00 — 260831-LOCR-L28 curator: re-derived the manifest population and every lane range against the current tree after the authorized repair of three missing CCR landing-debt registrations, all three created by code commit 8885939e but omitted from this manifest. All three take the `unit-regression` lane because the integration lane is capped at 150 collected cases and registering them as integration raised a full-suite collection above that cap; in unit-regression the collection succeeds and the previously unmarked modules keep their existing behaviour. This leaf's own `test_terminal_liveness_deferred_work.py` row was corrected the same way, from integration to `unit-regression`: the module is hermetic and registering it as integration took that lane to 155 against the same 150 cap. Current population is 186 modules: 102 unit-regression, 2 public-contract, 55 integration, 14 architecture-fitness, 13 provider-conformance; stress-durability and migration empty. Supersedes the 183-module account in this leaf's first entry. Classification metadata only; focused results and certification remain closeout-owned.

- 2026-09-10T11:22:48+02:00 — 260831-LOCR-L25 curator: corrected the lane split for the three restored CCR landing-debt rows. The first registration put `test_task_doc_review_public.py` and `test_transaction_only_worktree_delivery.py` in `integration`, which pushed full-suite collection to 157 against the 150-case integration cap and raised `UsageError` at collection finish; because both modules previously ran unmarked (unit), the behaviour-preserving lane is `unit-regression`. All three restored rows (`test_review_state.py`, `test_task_doc_review_public.py`, `test_transaction_only_worktree_delivery.py`) are now `unit-regression`. Re-derived population: 102 unit-regression / 2 public-contract / **55** integration / 14 architecture-fitness / 13 provider-conformance = 186 files, superseding the 100 / 2 / 57 figures recorded at 11:04 on the same tree. Integration collects 150 (cap 150), unit collects 712 (cap 1000). The bracket ranges were re-measured (`integration` is again 113-169, `unit-regression` 5-108) and the cap consequence is recorded as a current invariant. Classification only: no execution or acceptance claim, and verification metadata remains closeout-owned.

- 2026-09-10T11:04:12+02:00 — 260831-LOCR-L25 curator: re-derived this card against the developer-authorized manifest repair that restored the three CCR landing-debt rows `8885939e` omitted (recorded here as `test_review_state.py` unit-regression; `test_task_doc_review_public.py` and `test_transaction_only_worktree_delivery.py` integration; the three modules already had cards). All five lane bracket ranges and the L38 row were re-measured and the population was recorded as 100 unit-regression / 2 public-contract / 57 integration / 14 architecture-fitness / 13 provider-conformance = 186 files, replacing 99 / 2 / 55 / 14 / 13 = 183. **The 57-integration split in this entry was superseded by the 11:22 correction above; the total of 186 and the restored-row set remain correct.** Classification only: lane membership is not execution or acceptance evidence, and verification metadata remains closeout-owned.

- 2026-09-10T10:55+02:00 — 260831-LOCR-L20 curator manifest refresh: the developer authorized
  repairing the pre-existing registration omission, and three modules created by the CCR
  transaction-only closeout reform were restored to the closed population —
  `test_review_state.py`, `test_task_doc_review_public.py` and
  `test_transaction_only_worktree_delivery.py`, all in `unit-regression`. They had been running
  unmarked (counted as unit), and the integration lane already sat at its hard cap of 150 collected
  cases, so `integration` would have overflowed the cap; the unit lane is the behaviour-preserving
  classification. The manifest then held 186 rows: 102 unit-regression, 2 public-contract,
  55 integration, 14 architecture-fitness and 13 provider-conformance. `load_lane_manifest` refused
  the incomplete manifest before the repair and loads it now. This card's population prose and all
  six lane bracket citations were re-derived against the file as it stood; the preceding L20 entry's
  183 rows was the count before that restoration. This records lane classification only; focused
  execution and any later acceptance remain separately owned.


- 2026-09-10T10:06:31+02:00 — 260831-LOCR-L25 curator: registered the new separation-guard module `mcp/tests/test_parked_external_await_separation.py` in the `unit-regression` lane and re-derived every lane bracket and membership range against the current manifest on the leaf candidate base `6096941f41204c9a7d6ccb2b29f6b2e862ed56b4`. The recorded population (96 unit / 54 integration / 179 files) had already drifted from the manifest, which held 98 / 55 / 182 before this leaf's row; it is now recorded as 99 / 55 / 183. Classification only: lane membership is not execution or acceptance evidence, and verification metadata remains closeout-owned.

- 2026-09-09T12:22:46+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:203-203. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: recorded the two registered public integration modules and reconciled the manifest population to 179 files (54 integration). Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.

- 2026-09-08T14:39+02:00 — 260831-LOCR-L20 curator reconciliation: registered the new
  `test_terminal_evidence_cursors.py` unit-regression member and reconciled the manifest
  population to its then-current 183 rows (99 unit-regression, 55 integration), adding the focused
  deque-envelope, unsupported-harness, bounded-Pi, and liveness-containment checks to this route's
  account, and re-anchored every lane citation in this card to the tree as it stood. This records lane
  classification only; focused execution and any later acceptance remain separately owned.


- 2026-09-08T14:35+02:00 — 260831-LOCR-L28 curator: registered the new `test_terminal_liveness_deferred_work.py` integration proof and re-derived the manifest population and every lane range against the current tree (183 modules: 98 unit-regression, 2 public-contract, 56 integration, 14 architecture-fitness, 13 provider-conformance; stress-durability and migration empty). The lane remains classification metadata; focused results and certification remain closeout-owned.

- 2026-09-08T14:30:38+02:00 — Added the canonical terminal-evidence mapping regression to the `unit-regression` inventory and reconciled the retained population to 183 modules (99 unit-regression, 55 integration) on the current base, re-deriving this card's lane citations after the new row shifted them. Lane membership controls selection/classification only; this candidate entry does not claim execution, certification or acceptance.

- 2026-09-06T21:51:32+00:00 — Reconciled the retained IAS implementation and diagnostic testing policy with current source citations; prior verification provenance is retained and no new test or review result is claimed.

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Recorded the real transaction suite integration membership and shifted only exact affected lane citations; classification remains distinct from acceptance. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Added current retained-evidence, producer-publication and registry-lock lane assignments with explicit distinctions between classification and execution fidelity.

- 2026-09-05T06:14:14+00:00 — Reconciled all accumulated CCR lane additions and clarified that lane membership does not itself prove real production integration.

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: recorded the five CCR-R14 final-codex contract suites (rows 64-68, `unit-regression`) and the executor plus diff-coverage closure suites (rows 291-292, `integration`) and re-anchored the manifest citations shifted by the new rows (fence 102, gate-certificate 77, doctrine 526-528, retry 157/427/529, kernel 150, future-code 303, pair 385, ARSPAWN 301/396/426/515, CCR-R01 nine suites 29-30/73/158-161/180-181). Verification stamp is the full leaf code commit `54ff803a05209e06f732f2de1f90e2a71a069e08`.

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: recorded the six CCR-R17 measured-replay suites (rows 148-153, `unit-regression`) and re-anchored the manifest citations shifted by the new rows plus prior registrations (doctrine 525-527, retry 158/426/528, kernel 145, future-code 302, pair 384, ARSPAWN 300/395/425/514, fence 97, CCR-R01 nine suites 29-30/68/159-162/181-182, gate-certificate 72). Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185`.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded the three status-wait test modules added to the integration evidence lane.

- 2026-09-04T17:50+02:00 — 260831-CCR-L13 Gate-5 memory pass: recorded the four CCR-R13 diagnostic contract suites (rows 60-63, unit-regression) and the executor plus diff-coverage closure suites (rows 284-285, integration) and re-anchored the manifest citations shifted by the new rows (fence 97, doctrine 518-520, retry 152/420/521, kernel 145, future-code 296, pair 378, ARSPAWN 294/389/419/507, CCR-R01 29-30/68/153-156/175-176, gate-certificate 72). Verification stamp is the full leaf code commit `4ba18bb23ba90e201bb37341d61c0efc64161fcf`.

- 2026-09-04T17:15+02:00 - 260831-CCR-L20 Gate-5 memory pass (code commit `ce7f10b5`):
  registered the standalone CCR-R20 terminal rail-failure suite as explicit `integration`
  evidence (row 465) and re-anchored every manifest lane citation in this card to the committed
  tree positions (doctrine 513-515, retry 148/414/516, kernel 141, future-code 290, pair 372,
  ARSPAWN 288/383/413/502, fence 93, CCR-R01 nine suites 29-30/64/149-152/171-172) after
  intermediate registrations and the new row shifted the manifest. Verification stamp is the full
  leaf code commit `ce7f10b565f82bc41421d60ba914ee1d0abf61c4`.


- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5 memory pass: recorded the six new
  durable gate-and-rail telemetry suites (unit-regression lanes file rows 178-183) and re-anchored
  every manifest citation shifted by their rows (doctrine 512-514, retry 148/414/515, kernel 141,
  future-code 290, pair 372, ARSPAWN 288/383/413/501, fence 93, CCR-R01 nine suites
  29-30/64/149-152/171-172). Verification stamp advanced to the certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`.


- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the explicit `integration` lane registration for the new host-authority suite `test_dagger_runtime_authority.py`.

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the `test_generation_coherent_lifecycle_projection.py` unit-regression lane registration and the manifest line shift it causes. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: recorded the CCR-R08
  integration-lane registration of the five final full memory-coherence certification suites
  (rows 365-369) so each forcing suite enters the closed population exactly once. Verification
  metadata pinned to the owning commit 16d1a4d6.


- 2026-09-04T01:15+02:00 - 260831-CCR-L10 Gate-5 memory pass: recorded the CCR-R10 lane registration of
  `mcp/tests/test_citation_deterministic_projection.py` as explicit `integration` evidence (toml row 223)
  and re-anchored every manifest citation shifted by that row (retry 147/401/501, ARSPAWN
  280/370/400/487, future-code 282, pair 364, doctrine 498-500). Verification pinned to the
  leaf code commit 709dd076.


- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: recorded the `test_serving_requirements.py` integration-lane registration and re-anchored the manifest citations shifted by the new row (doctrine 498-500, ARSPAWN e2e 487, retry-coverage 501).

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored all 21 manifest lane citations to the exact current line numbers after the L21 gate-certificate registration and prior registrations shifted rows (doctrine 497-499, retry 147/400/500, kernel 140, future-code 281, pair 363, ARSPAWN 279/369/399/486, fence 92, CCR-R01 nine suites 29-30/64/148-151/170-171). Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored all
  21 manifest lane citations to the exact current line numbers after the L21 gate-certificate
  registration and prior registrations shifted rows (doctrine 497-499, retry 147/400/500,
  kernel 140, future-code 281, pair 363, ARSPAWN 279/369/399/486, fence 92, CCR-R01 nine
  suites 29-30/64/148-151/170-171). Verification remains pinned to the pre-commit source
  history until closeout.


- 2026-09-03T12:30+02:00 - 260831-CCR memory curation pass for 6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): recorded the L21 lane registration of `mcp/tests/test_gate_certificate_authority.py` as explicit `unit-regression` evidence so the new forcing suite enters the closed population exactly once. Verification is pinned to the owning commit.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): recorded the L21 lane registration of
  `mcp/tests/test_gate_certificate_authority.py` as explicit `unit-regression` evidence so the
  new forcing suite enters the closed population exactly once. Verification is pinned to the
  owning commit.


- 2026-09-01T11:33+02:00 - CCR-L11 Attempt 10 added explicit `unit-regression` ownership for the three focused certification edge suites and re-anchored every manifest citation shifted by those rows. Verification remains closeout-owned.

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 added explicit `unit-regression` ownership for the
  three focused certification edge suites and re-anchored every manifest citation shifted by
  those rows. Verification remains closeout-owned.


- 2026-09-01T08:13+02:00 - Final CCR-R01 reconciliation: expanded the current lane account from six to all nine focused unit-regression suites, including the three coverage-edge companions, and regenerated every manifest citation shifted by their rows. The manifest supplies selection and cost classification only; verification remains closeout-owned.

- 2026-09-01T08:13+02:00 — Final CCR-R01 reconciliation: expanded the current lane account from
  six to all nine focused unit-regression suites, including the three coverage-edge companions, and
  regenerated every manifest citation shifted by their rows. The manifest supplies selection and
  cost classification only; verification remains closeout-owned.


- 2026-09-01T05:22+02:00 - 260831-CCR-L01 Attempt 9: added explicit `unit-regression` ownership for the six focused CCR-R01 suites and re-anchored every manifest citation shifted by those rows. The lane declaration governs selection/cost only; accepted task evidence remains reviewer-owned. Verification remains closeout-owned.

- 2026-09-01T05:22+02:00 — 260831-CCR-L01 Attempt 9: added explicit `unit-regression`
  ownership for the six focused CCR-R01 suites and re-anchored every manifest citation shifted by
  those rows. The lane declaration governs selection/cost only; accepted task evidence remains
  reviewer-owned. Verification remains closeout-owned.


- 2026-09-01T04:34+02:00 - Added explicit `unit-regression` ownership for the two certification contract suites and repaired every manifest citation shifted by those rows. The manifest remains fail-closed; no default, fallback, or alternate classification authority was introduced.

- 2026-09-01T04:34+02:00 — Added explicit `unit-regression` ownership for the two certification
  contract suites and repaired every manifest citation shifted by those rows. The manifest remains
  fail-closed; no default, fallback, or alternate classification authority was introduced.


- 2026-08-31T20:30+02:00 - 260831-DER: explicitly classified `mcp/tests/test_integration_publication_fence.py` in the `unit-regression` lane.

- 2026-08-31T20:30+02:00 — 260831-DER: explicitly classified
  `mcp/tests/test_integration_publication_fence.py` in the `unit-regression` lane.


- 2026-08-31T08:05+02:00 - Classified the four A003-unregistered ARSPAWN proof modules exactly once: three integration routes and one architecture-fitness selector-closure route.

- 2026-08-31T08:05+02:00 — Classified the four A003-unregistered ARSPAWN proof modules exactly
  once: three integration routes and one architecture-fitness selector-closure route.


- 2026-08-30T15:15:36+02:00 - Classified `test_public_surface_conformance.py` explicitly as integration evidence. Verification remains closeout-owned.

- 2026-08-30T15:15:36+02:00 — Classified `test_public_surface_conformance.py` explicitly as
  integration evidence. Verification remains closeout-owned.


- 2026-08-30T04:54+02:00 - Added explicit integration-lane ownership for the exact code-memory candidate-pair suite after the lifecycle Dagger census rejected an unclassified test file. No product or requirement semantics changed.

- 2026-08-30T04:54+02:00 — Added explicit integration-lane ownership for the exact
  code-memory candidate-pair suite after the lifecycle Dagger census rejected an unclassified
  test file. No product or requirement semantics changed.


- 2026-08-29T08:52+02:00 - Added explicit integration classification for the structured curator-coherence forcing suite. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Added explicit integration classification for the structured
  curator-coherence forcing suite. Verification remains closeout-owned.


- 2026-08-29T07:35+02:00 - Added explicit integration-lane ownership for the future-code candidate real-Git matrix and repaired exact manifest citations shifted by that row.

- 2026-08-29T07:35+02:00 — Added explicit integration-lane ownership for the future-code
  candidate real-Git matrix and repaired exact manifest citations shifted by that row.


- 2026-08-28T14:18+02:00 - Reconciled manifest citations against the committed PDLS candidate; the explicit-lane contract is unchanged.

- 2026-08-28T14:18+02:00 — Reconciled manifest citations against the committed PDLS candidate;
  the explicit-lane contract is unchanged.


- 2026-08-28T05:10+02:00 - Removed the two stale Candidate A test rows and retained the renamed kernel regression module in its explicit unit lane after Q5 v19 forced the stale-row refusal.

- 2026-08-28T05:10+02:00 — Removed the two stale Candidate A test rows and retained the renamed
  kernel regression module in its explicit unit lane after Q5 v19 forced the stale-row refusal.


- 2026-08-27T18:33+02:00 - Recorded explicit unit-regression membership for the retry coverage composition and quality child-environment suites.

- 2026-08-27T18:33+02:00 — Recorded explicit unit-regression membership for the retry coverage
  composition and quality child-environment suites.


- 2026-08-27T18:06+02:00 - Added explicit architecture-fitness membership for the M40-M45 Requirement Attempt Journal structural proof.

- 2026-08-27T18:06+02:00 — Added explicit architecture-fitness membership for the M40-M45
  Requirement Attempt Journal structural proof.


- 2026-08-27T17:19+02:00 - Added explicit unit-regression membership for the retry-selection forcing suite in the same change that introduced it.

- 2026-08-27T17:19+02:00 — Added explicit unit-regression membership for the retry-selection
  forcing suite in the same change that introduced it.


- 2026-08-27T13:32+02:00 - Added explicit architecture-fitness membership for M39 compilation doctrine and the split tool-signature exemption suite. Verification remains closeout-owned.

- 2026-08-27T13:32+02:00 — Added explicit architecture-fitness membership for M39 compilation
  doctrine and the split tool-signature exemption suite. Verification remains closeout-owned.


- 2026-08-27T12:43+02:00 - M38: created the manifest sidecar and recorded explicit registration of the acceptance-envelope structural test. Verification metadata remains empty until governed closeout stamps the PDLS code commit.

- 2026-08-27T12:43+02:00 — M38: created the manifest sidecar and recorded explicit registration
  of the acceptance-envelope structural test. Verification metadata remains empty until governed
  closeout stamps the PDLS code commit.

