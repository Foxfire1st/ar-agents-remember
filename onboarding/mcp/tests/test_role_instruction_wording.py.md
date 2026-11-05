# mcp/tests/test_role_instruction_wording.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Checks what a role is told: its delegation and seat boundaries, how it reaches its parent, peers and the
developer, which host tool names it may use and which it must not, and what its compiled capsule sends as
a return. The census is the router, the eight launcher role files and their nine operations, delivered in
order and compared with the packaged copy's bytes.

## Code Commentary

### Logic

`InstructionFileWordingTests` reads the canonical skill tree and, through `PACKAGED`, the packaged serving
copy, and it compiles capsules with `role_capsules.compilation` and `skill_resources.capsule`.

- **Scope and authority.** `test_investigator_scope_report_and_authority_are_explicit` and
  `test_retired_investigator_wording_is_detected_when_reinserted` pin the Investigator's scope, report and
  authority and prove the retired wording is caught when reinserted.
- **Coordination and curation.** `test_current_coordination_and_curator_rules` and
  `test_direct_closeout_keeps_the_architect_and_its_existing_gates` keep the current coordination rules and
  the Architect's closeout gates with its kept clause.
- **Positive obligations.** `test_every_role_organises_its_harness_work_with_seat_boundaries`,
  `test_leaf_roles_and_operations_deliver_their_own_positive_obligations` and
  `test_removing_each_affirmative_clause_is_detected_on_its_surface` require each surface to state its own
  obligation and prove deleting a clause fails on that surface; `test_equivalent_preserved_identity_and_no_role_boundaries_are_allowed`
  keeps an equivalent phrasing admissible.
- **The census.** `test_the_surfaces_are_the_router_seven_roles_and_their_eight_operations` fixes the
  delivered set, and `test_no_forbidden_host_string_is_left_and_the_packaged_copy_is_the_same_text` compares
  the packaged copy with the canonical text.
- **Tool names.** `test_every_passage_that_names_an_ar_tool_names_the_task_tool_server`,
  `test_the_router_names_the_host_the_two_tools_and_the_only_tool_server` and
  `test_the_orientation_says_where_the_tools_are_and_what_a_reply_is` keep every mention of an AR tool tied
  to the task tool server.
- **Reach and return.** `test_each_role_is_told_how_to_reach_agents_and_the_developer` and
  `test_the_capsules_send_a_return_and_never_point_at_the_agent_chat` keep `role_message` as the way
  handovers and awaits travel; `test_the_workers_report_names_its_agent_id` keeps the Worker's report naming
  its own agent.
- **Sync and repair.** `test_a_clean_sync_keeps_the_review_and_a_repair_stays_visible` pins the conditional
  sync clause and the visible direct-repair clause at their delivered audiences.

### Conventions

Wording is checked through `capsule_wording` and `leaf_instruction_wording`, which read a facet on its real
role, stage or detail surface and apply a deletion control, so a passing case means the clause is load
bearing on that surface.

### Invariants And Boundaries

- The packaged copy is the same text as the canonical source.
- No surface names a forbidden host string or points a seat at the agent chat instead of `role_message`.

Named-section deletion and relocation controls cover construction-cost escalation, continuation, exact freeze/check identity and design-guideline duties. Coordination assertions preserve staged Manager seat creation, empty-seat recovery and scoped manual repair; message duties are checked at their actual shared delivery step. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence
- Instruction tests check Investigator scope and authority, coordination and positive seat obligations, task-server vocabulary and compiled handover/await returns; the declarations do not establish a fresh test run. [Past-epoch source caption, detached from live reference 1. Recorded citation custody: mcp/tests/test_role_instruction_wording.py blob 02d7feb6be0a2c87f6dbb2b4735879f167688ed6 (available); mcp/tests/test_role_instruction_wording.py blob 73dd5b9660c6d872dc71217bedde72df528fcec0 (available); historical event commit not identified. No historical event or intent inferred.]

Current source: Instruction cases assert Investigator scope/report/mutation boundaries, current coordination, positive leaf-seat obligations, the task-tool-server vocabulary and compiled return/await channels. Their assertions distinguish a stored file from an explicit handover and establish no fresh test run.


- The Investigator wording case checks scoped concern intake, report and remediation authority, and the canonical investigator role plus retained system-specialist alias. [2]


- Compiled parented handovers distinguish fixed starter identity from ordinary return role/task addresses; leaf returns name the current Manager. [3]


- Current protected instruction/compiled/tool-description sentences require the Manager-owned three-seat set and product-held permission/start/turn messages with ordered delivery and no prompt answering or sender resubmission. Description census includes role_start_set beside role_start/role_message. Investigator report-notice substring, actual-parent developer questions and ordinary role/task report return stay distinct; no wording case proves a concrete live recipient or host consumption. [Past-epoch source caption, detached from live reference 4. Recorded citation custody: mcp/tests/test_role_instruction_wording.py blob 02d7feb6be0a2c87f6dbb2b4735879f167688ed6 (available); mcp/tests/test_role_instruction_wording_handover.py blob d26f7a71fe3a996c2c34acccc3af29f5d88d16a3 (available); skills/l-01-agent-lifecycles/operations/orientation.md blob a1874e84f67fee3a09491d5b1e1e560a4526671c (available); historical event commit not identified. No historical event or intent inferred.]

Current source: Current instruction cases require staged individual Manager starts: Worker at build, Reviewer at freeze and Curator after code PASS. Handover tests keep actual-parent developer questions distinct from ordinary role/task returns and pin held-message ordering and permission boundaries. The tool-description census still covers role_start_set beside role_start and role_message; those source-text checks prove no live recipient or host consumption.


- The current source declares positive instruction-clause deletion controls and task-tool-server/host naming assertions; source presence supplies no executed test result or acceptance. [5]


- The module checks the launched instruction surfaces, named task-server boundary, role-return channel and current coordination wording. [Past-epoch source caption, detached from live reference 6. Recorded citation custody: mcp/tests/test_role_instruction_wording.py blob 02d7feb6be0a2c87f6dbb2b4735879f167688ed6 (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The module checks the manifest-derived router/role/operation surface set, forbidden-host and package-copy equality, named task-server usage, parent/developer routing and compiled role returns, together with current coordination wording.


- Uses capsule_wording to read relocated facets on their real role, stage or detail surface and apply nonvacuous deletion controls. Curator short forms retain writer/admission/foundation/worklist/output boundaries; the Git code-and-two-memory-tree comparison is checked in the delivered handoff. Reviewer parentless wording is role-specific. Writer syntax is checked in declared writer/intake details; admission tests preserve no-bypass, selected-root, report/refusal and coherence duties, while the curation operation retains admitted-record readback. [Past-epoch source caption, detached from live reference 8. Recorded citation custody: mcp/tests/test_role_instruction_wording.py blob 73dd5b9660c6d872dc71217bedde72df528fcec0 (available); mcp/tests/test_role_instruction_wording.py blob 02d7feb6be0a2c87f6dbb2b4735879f167688ed6 (available); mcp/test_support/agents_remember_test_support/testing/capsule_wording.py blob 09f2c74edf8eddefa3aabd30414a40628d75575b (available); mcp/tests/test_curator_instruction_wording.py blob 4cec94249db175d2ad18bef512477765ff722e18 (available); skills/l-01-agent-lifecycles/operations/curation.md blob 145be631612f52c363b97b82d253839028ebc907 (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The wording support resolves Curator facets through the real addressed role, stage or declared detail and generates nonvacuous deletion controls. The delivered handoff checks the Git code-and-two-memory-tree comparison. Current Curator tests retain task/foundation/producer/output admission, serving-build writer syntax, selected-root/refusal reporting and full quality/coherence duties; the curation operation still requires admitted-record readback.

- The conditional sync and visible direct-repair clauses are pinned at their delivered audiences. [9]

- The Architect's flat-mode closeout gates and its kept clause stay pinned here after the coordination clauses moved out. Anchor: `test_direct_closeout_keeps_the_architect_and_its_existing_gates` [10]



- The census pins the router, the eight launcher role files and their nine operations in delivered order. [11]




- Protected Manager text separates automatic stage publication, explicit correction and organizational completion — mcp/tests/test_curator_instruction_wording.py:135-144. [Past-epoch source caption, detached from live reference 12. Recorded citation custody: mcp/tests/test_curator_instruction_wording.py blob 4afbf89956084f554e5cb21d5190d2bad1b5f051 (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The protected Manager clause separates automatic stage publication and master-row mirroring at start/finalize/abandon from task_doc set_status for an explicit correction or organizational-master completion.

- Instruction cases assert Investigator scope/report/mutation boundaries, current coordination, positive leaf-seat obligations, the task-tool-server vocabulary and compiled return/await channels. Their assertions distinguish a stored file from an explicit handover and establish no fresh test run. [1]
- Current instruction cases require staged individual Manager starts: Worker at build, Reviewer at freeze and Curator after code PASS. Handover tests keep actual-parent developer questions distinct from ordinary role/task returns and pin held-message ordering and permission boundaries. The tool-description census still covers role_start_set beside role_start and role_message; those source-text checks prove no live recipient or host consumption. [4]
- The module checks the manifest-derived router/role/operation surface set, forbidden-host and package-copy equality, named task-server usage, parent/developer routing and compiled role returns, together with current coordination wording. [6]
- The wording support resolves Curator facets through the real addressed role, stage or declared detail and generates nonvacuous deletion controls. The delivered handoff checks the Git code-and-two-memory-tree comparison. Current Curator tests retain task/foundation/producer/output admission, serving-build writer syntax, selected-root/refusal reporting and full quality/coherence duties; the curation operation still requires admitted-record readback. [8]
- The protected Manager clause separates automatic stage publication and master-row mirroring at start/finalize/abandon from task_doc set_status for an explicit correction or organizational-master completion. [12]

- Named-section deletion and relocation controls cover construction-cost escalation, continuation, exact freeze/check identity and design-guideline duties. Coordination assertions preserve staged Manager seat creation, empty-seat recovery and scoped manual repair; message duties are checked at their actual shared delivery step. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [13]
