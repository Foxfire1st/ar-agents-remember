# mcp/tests/test-evidence-lanes.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test-evidence-lanes.toml` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:20:31+00:00 |
| lastVerifiedCommitHash | `58bf4cde0f5271bbe420ad8e045d18b433f11253` |
| lastVerifiedCommitDate | 2026-09-17T12:31:16+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l15-ar` uncommitted source (17 dirty paths); base `15fa0e2c0bb91d5bb1b2abf4ee8eb54916bd5ed4` |
| reviewedWorkingCandidate | `ar/260915-caps-l17-ar` uncommitted source; base `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` (synced onto L14's landing) |
| governingOverview | `overview.md` |

## 260915-CAPS-L9 Row

This leaf adds **one** manifest row — `mcp/tests/test_capsule_experiment_install.py:19` — and its
module is **not** a seventh `D9` module: the fail-closed loader still names exactly the same six
at this tip as at the clean base (`test_eve_adapter`, `test_eve_protocol`,
`test_role_capsule_admission`, `test_role_capsule_compiler`, `test_role_instruction_corpus`,
`test_task_projection`). The `test_install_runtime.py` mention at `:74` is pre-existing context
for the catalog consumer proof, not a row this leaf added.

## Governing Overview

[Tests overview](overview.md)

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

Classifies the retained test-shaped modules into explicit evidence categories. **Current population measured at the `260831-LOCR-L39` hardening tip (code base `a5f5380b`): 224 modules on disk and 224 manifest entries — 130 unit-regression (key `:5`, rows 6-135, next key `:137`), 2 public-contract (key `:137`, rows 138-139), 62 integration (key `:141`, rows 142-203), 17 architecture-fitness (key `:205`, rows 206-222) and 13 provider-conformance (key `:224`, rows 225-237); stress-durability (`:239`) and migration (`:241`) are empty. The unit-regression bracket is `:5-135`, the integration bracket is `:141-203`.** The L05 measurement and its method are in the `## 260831-LOCR-L04 Lane Row (Declared)` and `## 260831-LOCR-L05 Lane Row (Declared)` sections below; the `## 260831-LOCR-L06 Lane Row (Declared)` section carries the immediately preceding 215-module measurement (pair code base `e9678c56`), the `## 260831-LOCR-L17 Lane Row (Declared)` section the 214-module one before that and the `## 260831-LOCR-L18 Lane Row (Declared)` section the 213-module one before that. Every count and bracket in the two paragraphs below is an earlier measurement — L23 measured 208 modules, and sibling unit-lane insertions from L01 (`:97`) and L10 then moved the later file lines down; L27's own integration row at `:183` accounts for the rest; those two declared sections are the as-of records that carry their own evidence. The focused terminal-evidence cursor suite `test_terminal_evidence_cursors.py` and the parked-external-await separation guard `test_parked_external_await_separation.py` are unit-regression members, and 260831-LOCR-L32 added `test_worktree_status_terminal_next_tool.py` to the **integration** lane (row 175; it drives real worktree services and a real repository under `tmp_path`), while 260831-LOCR-L34 added `test_checkpoint_landing_end_to_end.py` to that same lane (row 132; it drives the public checkpoint/closeout operations over real temporary Git repositories), and 260831-LOCR-L36 added `test_cross_master_concurrency.py` to that lane as well (row 143; it drives two sprint-commanded atomic masters and the public land/resume operations over one real temporary Git world), while 260831-LOCR-L37 added `test_pause_stop_only_end_to_end.py` to that same lane (row 159; it drives the public pause over one real temporary Git world holding two atomic masters and measures refs, object databases, coordination tree, worktrees and task documents before and after) **and** `test_pause_is_not_publication.py` to **architecture-fitness** (row 191; it is an AST-only import-closure guard that executes nothing), and the 260831-LOCR seal-removal change set added `test_lifecycle_playthrough_end_to_end.py` to **integration** (row 153; it plays the whole leaf-and-master lifecycle in order over one real temporary Git world and is the regression proof for the deleted child-admission seal). The 260913-LCA-L7 change set added one more integration member,
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
`mcp/tests/test-evidence-lanes.toml:173`, in the **integration** lane, inserted alphabetically between
`test_eve_capsule_runtime.py` (`:172`) and `test_git_command.py` (`:174`). That is its
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

## 260915-CAPS-L5 Lane Row (Declared)

The L5 change set adds `mcp/tests/test_codex_capsule_delivery.py` **and** its row in the same change.
The row is `mcp/tests/test-evidence-lanes.toml:216`, in the **provider-conformance** lane, inserted
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
the dated `## Update History

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

- 2026-09-17T10:45+02:00 — 260915-CAPS-L15 curator: the manifest gained one row for this leaf's own new
  module, `mcp/tests/test_capsule_launch_wiring.py`, at `:19` in the **unit-regression** lane — its
  behaviour-preserving lane, since the module drives the launch points, the real runner preparation and
  the real adapter factory in process with the vendor boundary recorded and no real process started. A
  declared section records the row, its insertion point and the D9 rule it satisfies in the same change
  that adds the module. No row was removed, moved between lanes, or added to a capped population beyond
  the one module's own. Verification metadata moves to this leaf's base `15fa0e2c`; the candidate is
  deliberately uncommitted, so the governed closeout stamps the real code commit and no hash or
  fingerprint was invented here.
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
- Lane membership is additionally bounded by the declared collected-case budgets (`unit_case_budget` 1500, `integration_case_budget` 250 — `pyproject.toml:158-159`; the 150/200/1000 values in earlier entries of this card are stale). **The unit ceiling was raised from 1000 to 1500 by 260915-CAPS-L8, executing the developer's ruling**, because the default selection had outgrown 1000 and so refused collection before any case ran; the raise restored a working default selection and is a ceiling rather than a target. A module that was previously running unmarked already spends unit budget, so registering it as `unit-regression` preserves behaviour; moving it into `integration` can push full-suite collection past the integration cap and fail collection outright. Classification cannot be chosen for semantic tidiness alone.
- Full suites and whole-candidate review occur at master completion, not once for every lane or leaf.
- Lane membership must keep each collected population inside its declared case budget: `unit_case_budget` 1500 and `integration_case_budget` 250 (root `pyproject.toml:158-159`), enforced in `pytest_collection_finish`. A module that a full run previously collected unmarked - and therefore already counted as unit - belongs in `unit-regression`; moving it to `integration` can refuse collection.

## Docs References

No external Domain Documentation source is configured; these are repository-owned implementation facts.

## Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Retained unit-regression membership, including the R28 deferred-work and canonical terminal-evidence mapping proofs. The range moved by +2 when this change set and L4 each inserted one row additively into the same list. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-128 |
| Small actual integration file population | `integration` | mcp/tests/test-evidence-lanes.toml:129-190 |
| Retained structural detector classifications | "architecture-fitness" | mcp/tests/test-evidence-lanes.toml:191-208 |
| Provider contract classifications | "provider-conformance" | mcp/tests/test-evidence-lanes.toml:209-224 |
| Empty former stress/migration populations | "stress-durability"; "migration" | mcp/tests/test-evidence-lanes.toml:225-226; mcp/tests/test-evidence-lanes.toml:227-228 |
| L38 registered public activation/admission and route-review transport ownership | `integration` | mcp/tests/test-evidence-lanes.toml:129-129 |
| The new parked-candidate suite is registered in the unit-regression lane. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-5 |
| The manifest still has no default classification for an unregistered test file. | "stress-durability" | mcp/tests/test-evidence-lanes.toml:224-224 |
| LOCR-L09 boundary-delivery forcing module registered in the unit lane | "mcp/tests/test_state_signal_boundary_delivery.py" | mcp/tests/test-evidence-lanes.toml:101-101 |
| The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. | "mcp/tests/test_checkpoint_landing.py" | mcp/tests/test-evidence-lanes.toml:25-25 |
| The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 184 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_worktree_status_terminal_next_tool.py" | mcp/tests/test-evidence-lanes.toml:186-186 |
| The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 134 now, after the L4, L5, L7, L8 and L3 insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. | "mcp/tests/test_checkpoint_landing_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:136-136 |
| The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 146 now, after the L4, L5, L7, L8 and L3 insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:148-148 |
| The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 163 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_pause_stop_only_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:165-165 |
| The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row 196 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:198-198 |
| The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 157 now, after the L4, L5, L7, L8 and L3 insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:159-159 |
| The L4 producer-census suite is registered in the unit-regression lane by the commit that landed L4, closing the gap the L4 section recorded. | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:70-70 |
| The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 154 now, after the L7, L8 and L3 insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:156-156 |
| The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 138 now, after the L8 and L3 insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. | "mcp/tests/test_closeout_projection_source_classification.py" | mcp/tests/test-evidence-lanes.toml:140-140 |
| The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 178 now, after the L3 insertion) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:180-180 |
| The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 69) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:71-71 |
| The integration lane's collected-case cap that constrains lane choice, cited as the pinned key and value. | "integration_case_budget = 250" | pyproject.toml:159-159 |
| The lane manifest is fail-closed: an unregistered tracked module makes loading refuse rather than classifying it by default. | `load_lane_manifest` | mcp/test_support/agents_remember_test_support/testing/lane_manifest.py:99-142 |
| The L4 capsule-and-skill-serving suite is registered in the unit-regression lane by the same change set that created it (entry row 19) — 19 of its 21 cases are hermetic over a disposable coordination root and a synthetic skills corpus and only its two real-process exchanges carry the integration marker, so that is its behaviour-preserving lane. | "mcp/tests/test_capsule_serving.py" | mcp/tests/test-evidence-lanes.toml:19-19 |
| The unit collected-case ceiling. **Corrected by 260915-CAPS-L8:** it read 1000 and the default selection had outgrown it (1053 collected at the base, so `pytest mcp/tests` refused collection before any case executed); the developer ruled the raise and this leaf executes it, so the declaration now reads 1500 and the default selection runs. Superseded, not deleted — the condition it recorded was real and is what caused the ruling. | "unit_case_budget = 1500" | pyproject.toml:158-158 |
## Cross-Repo References

No separate cross-repository authority is established by this file.

## Update History

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: recorded this leaf's **one** added row
  (`mcp/tests/test_capsule_experiment_install.py:19`) and the unchanged `D9` set — the fail-closed
  loader names the same six modules at this tip as at the clean base, and this leaf's module is not a
  seventh. The `test_install_runtime.py` mention at `:74` is pre-existing catalog-consumer context,
  not a row this leaf added. Verification metadata remains closeout-owned (the candidate is
  uncommitted).
- 2026-09-16T22:19+02:00 — 260915-CAPS-L16 curator: **one row added — `test_citation_source_index_membership.py`
  at `:26`, unit-regression** — and the population re-measured at this leaf's synced base `8997e184` plus
  its change set: **232 declared rows** against **238** modules on disk, leaving exactly the six
  pre-existing D9 modules unregistered (this leaf closed none of that gap and added no case to a capped
  population that was not already there). A new declared section carries the measurement and the
  behaviour-preserving lane rationale; the older "Current population" paragraph is now explicitly marked
  as the L7 candidate's measurement rather than the current one, because the insertion at `:26` moved
  every row below it and a reader must not take its 230/236 pair as current. Verification metadata moves
  to `8997e184` with the reviewed working candidate named; the candidate is deliberately uncommitted, so
  the governed closeout stamps the real code commit and no hash or fingerprint was invented here.

- 2026-09-16T20:42+02:00 — 260915-CAPS-L7 curator: **two rows added and the population re-measured at
  the current base.** Registered this leaf's `mcp/tests/test_eve_capsule_binding.py` in
  **unit-regression** (hermetic focused cases: no process, no Node) and
  `mcp/tests/test_eve_capsule_runtime.py` in **integration** (it executes the shipped TypeScript under a
  real Node). Added a measured `## Current population` section because the card's standing numbers were
  from an older base and no longer described the tree: **236** modules on disk, **230** manifest
  entries, unit-regression 134 (key `:5`), public-contract 2 (`:141`), integration 63 (`:145`),
  architecture-fitness 17 (`:210`), provider-conformance 14 (`:229`), stress-durability and migration
  empty. The loader's **one** finding — six test files with no explicit lane
  (`test_eve_adapter.py`, `test_eve_protocol.py`, `test_role_capsule_admission.py`,
  `test_role_capsule_compiler.py`, `test_role_instruction_corpus.py`, `test_task_projection.py`) — is
  recorded as **pre-existing at the pristine base** and none of it is this leaf's; this leaf adds two
  rows and closes none of that gap. Case budgets are recorded as `pyproject.toml`'s own
  (`unit_case_budget = 1500`, `integration_case_budget = 300`) and explicitly separated from lane
  membership, with the card's older 150/200/250/1000/1100 figures marked stale rather than edited out of
  the history. Verification metadata moves to the leaf's synced base `23cc7a72`; the candidate is
  deliberately uncommitted, so the governed closeout stamps the real code commit and no hash or
  fingerprint was invented here.

- 2026-09-16T14:15+02:00 — 260915-CAPS-L5 curator: registered the leaf's new
  `mcp/tests/test_codex_capsule_delivery.py` in the **provider-conformance** lane (entry row 216,
  between `test_codex_app_server_adapter_turns.py` and `test_harness_control_claude.py`) — its subject
  is the vendor app-server instruction channel, the same lane as its sibling `test_codex_app_server_*`
  modules, and its 28 cases carry no `integration` marker. Additive proof by the loader itself: 7
  findings including this module before the row, 6 after, and the module absent from them. Reconciled
  the brackets this insertion moved (provider-conformance 209-224, stress-durability 225-226,
  migration 227-228). Measured population at this candidate: 216 modules on disk, 210 rows (118
  unit-regression, 2 public-contract, 60 integration, 16 architecture-fitness, 14 provider-conformance),
  so the **six D9 modules remain unregistered** — named in the new section and left to L11.
  Classification only; verification metadata stays at the current committed base `c1dbebf8`.
- 2026-09-16T11:43:27+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:129-129. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:224-224. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:101-101. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing.py" repointed to mcp/tests/test-evidence-lanes.toml:25-25. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:186-186. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:136-136. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:148-148. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:165-165. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:198-198. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:159-159. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:70-70. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:156-156. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:140-140. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:180-180. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:71-71. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "integration_case_budget = 250" repointed to pyproject.toml:159-159. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: **a second leaf's row, and the two merged
  additively.** This change set registers `mcp/tests/test_eve_product_integration.py` under
  `unit-regression` (line 52), inserted in the alphabetically-kept list between
  `test_environment_reconstruction.py` and `test_final_catalog_plan_attestation.py`. L4's row for
  `mcp/tests/test_capsule_serving.py` (line 19) arrived in the same file when the leaf's source branch
  advanced, and the two insertions merged without conflict — the loader now names exactly the six
  historical D9 modules and neither leaf's module is among them. The invariant the row exists for: the
  lane loader is fail-closed and raises `LaneManifestError` for any module under `testpaths` without
  an explicit row, which ordinary pytest never detects. Verification metadata moves to the leaf's
  synced base `ff97072c`; the candidate is deliberately uncommitted, so the governed closeout stamps
  the real code commit and no hash or fingerprint was invented here.
- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator (uncommitted change set on `ar/260915-caps-l4`, base
  `b00a4ac2`): registered the change set's new `mcp/tests/test_capsule_serving.py` in the
  **unit-regression** lane at entry row 19 — 19 of its 21 cases are hermetic and only its two
  real-process exchanges are marked `integration`, so the default unit lane is its
  behaviour-preserving classification — and re-measured rather than carried: 208 declared rows, 117
  unit-regression (5-121), 2 public-contract (124-126), 60 integration (128-189), 16
  architecture-fitness (190-207), 13 provider-conformance (208-222), stress-durability and migration
  empty. **Recorded the collection refusal as current state, not as a repair**: the default unit
  selection collects 1083 against `unit_case_budget = 1000` (`pyproject.toml:149`) and already
  collected 1064 against that ceiling at this leaf's base, so 64 of the 83-case overage predates it;
  `conftest.pytest_collection_finish` therefore raises `pytest.UsageError` before any case runs. The
  ceiling was not edited and the module was not moved into another lane to dodge the check — raising a
  declared budget needs an explicit tradeoff and is the owner's decision (`F-L4-01`, L11 owns the
  ceiling). Also recorded that the manifest declares 208 rows while **214** `test_*.py` modules exist
  on disk, the six undeclared modules being the pre-existing `D9` master-tip gaps owned by L11
  (`test_capsule_serving.py` is not among them). Corrected the Repo-Internal References table to add
  the L4 row and the unit-budget row; the one insertion at `:19` moves every cited row below it one
  line higher than this card's earlier entries record. Classification only: lane membership is not
  execution, certification or acceptance evidence, and the verification stamps remain closeout-owned.

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
- 2026-09-13T17:20:55+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:178-178. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
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
- 2026-09-11T22:39:01+00:00: Generated citation repair: "unit-regression" repointed to mcp/tests/test-evidence-lanes.toml:5-5. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
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
