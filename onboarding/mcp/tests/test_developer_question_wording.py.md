# mcp/tests/test_developer_question_wording.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Keeps the developer-question contract in each capsule: which role may route a question to its parent, how a
question is recovered when it is pending, and where the answer's provenance is stated. It also holds the
upward-notice and downward-answer duties and the leaf `ownerRelation` that names peer results and the
occasions a question goes to the parent.

## Code Commentary

### Logic

**Historical source account, superseded by the current clause below:** The cases read the canonical role and operation skill files rather than compiled capsules, so what is
checked is the source wording a seat's capsule is built from; only the leaf `ownerRelation` case reads a
capsule the launch compiles. [Historical source custody: `mcp/tests/test_developer_question_wording.py` blob `ddc4e0152814a7b8e396988f3bdb89c35da6ff1d` at code base `59b01fb8f72a38d2d27f9c37b8b9ca2513fd3fa0`; this is no current implementation claim.]

- **Question, recovery and provenance.** `test_each_parentable_role_has_question_recovery_and_answer_provenance`
  covers every parentable role.
- **Notice and answer.** `test_each_parent_has_upward_notice_and_unchanged_downward_answer_duties` keeps a
  parent's upward notice and its unchanged downward answer duty.
- **Operations.** `test_question_operations_keep_conditional_routing_and_pending_recovery` checks
  orientation, and reviews and curation as composed role-plus-operation pairs.
- **Owner relation.** `test_leaf_owner_relation_keeps_peer_results_and_named_parent_occasions` keeps the
  leaf's peer results and the named parent occasions, with the compiled `ownerRelation` carrying the current
  Manager's role and task return address separately from the descriptive starter identity.
- **Retired directives.** `test_exact_retired_directives_are_detected_as_independent_sentences` proves each
  exact retired directive is detected as an independent sentence, so a surviving fragment is caught.

### Conventions

A role is checked as it is delivered — role plus operation — so a clause that only holds in the source but
not in the composed capsule is a failure.

### Invariants And Boundaries

- A question goes to the named parent on the named occasions; peers see results, not questions.
- A pending question is recovered rather than re-asked from scratch.

`question_step` uses the declared source, role audience, pointer and exact delivery step. Its clause-deletion controls read actual message-handover and child-question details for busy/held recovery and unchanged developer-answer provenance; the other cases continue to read canonical source or compiled ownerRelation as appropriate. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence
- The parentable roles carry the question, recovery, provenance and notice clauses. [Past-epoch source caption, detached from live reference 1. Recorded citation custody: mcp/tests/test_developer_question_wording.py blob ddc4e0152814a7b8e396988f3bdb89c35da6ff1d (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The parentable-role test checks question recovery and answer provenance in the shared orientation home, requires each selected role to refer to that home without copying it, and checks transport clauses through the declared delivered message step.


- Every starter role carries the upward notice and unchanged downward answer duties. [Past-epoch source caption, detached from live reference 2. Recorded citation custody: mcp/tests/test_developer_question_wording.py blob ddc4e0152814a7b8e396988f3bdb89c35da6ff1d (available); historical event commit not identified. No historical event or intent inferred.]

Current source: Starter-role checks require the shared upward permission notice, declared transport recovery and child-question step; the answer clauses retain an own-authority answer, otherwise an unchanged upward question and unchanged quoted developer-answer provenance on the return path.

- Orientation keeps conditional routing and pending recovery; review and curation are checked as composed role-plus-operation pairs. [3]

- The leaf `ownerRelation` keeps peer results and named parent occasions. [Past-epoch source caption, detached from live reference 4. Recorded citation custody: mcp/tests/test_developer_question_wording.py blob ddc4e0152814a7b8e396988f3bdb89c35da6ff1d (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The compiled leaf ownerRelation test keeps Worker, Reviewer and Curator peer results direct, reserves named authority/developer occasions to the parent, and requires sibling role/task arguments instead of routine parent result notices.


- Each exact retired directive is detected as an independent sentence. [Past-epoch source caption, detached from live reference 5. Recorded citation custody: mcp/tests/test_developer_question_wording.py blob ddc4e0152814a7b8e396988f3bdb89c35da6ff1d (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The retired-directive control reads the current Manager, Orchestrator and router surfaces, appends each exact retired sentence separately and requires detection; the Architect own-chat sentence is retained as an allowed contrast.


- The compiled leaf `ownerRelation` carries the current Manager role and task return address separately from the descriptive starter identity. [Past-epoch source caption, detached from live reference 6. Recorded citation custody: mcp/tests/test_developer_question_wording.py blob ddc4e0152814a7b8e396988f3bdb89c35da6ff1d (available); historical event commit not identified. No historical event or intent inferred.]

[Past-epoch source caption, detached from live reference 6. Recorded citation custody: mcp/tests/test_developer_question_wording.py blob ddc4e0152814a7b8e396988f3bdb89c35da6ff1d (available); historical event commit not identified. No historical event or intent inferred.]

Anchor: `test_leaf_owner_relation_keeps_peer_results_and_named_parent_occasions`

Current source: The compiled leaf ownerRelation test records the descriptive starter identity separately from host.parent.returnAddress: returns use the Manager role and canonical sprint/master task references, while peer results keep sibling leaf addresses.

- The parentable-role test checks question recovery and answer provenance in the shared orientation home, requires each selected role to refer to that home without copying it, and checks transport clauses through the declared delivered message step. [1]
- Starter-role checks require the shared upward permission notice, declared transport recovery and child-question step; the answer clauses retain an own-authority answer, otherwise an unchanged upward question and unchanged quoted developer-answer provenance on the return path. [2]
- The compiled leaf ownerRelation test keeps Worker, Reviewer and Curator peer results direct, reserves named authority/developer occasions to the parent, and requires sibling role/task arguments instead of routine parent result notices. [4]
- The retired-directive control reads the current Manager, Orchestrator and router surfaces, appends each exact retired sentence separately and requires detection; the Architect own-chat sentence is retained as an allowed contrast. [5]
- The compiled leaf ownerRelation test records the descriptive starter identity separately from host.parent.returnAddress: returns use the Manager role and canonical sprint/master task references, while peer results keep sibling leaf addresses. [6]

- `question_step` uses the declared source, role audience, pointer and exact delivery step. Its clause-deletion controls read actual message-handover and child-question details for busy/held recovery and unchanged developer-answer provenance; the other cases continue to read canonical source or compiled ownerRelation as appropriate. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [7]
