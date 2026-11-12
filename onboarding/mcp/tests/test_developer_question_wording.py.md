# mcp/tests/test_developer_question_wording.py

## Governing Overview

[overview](overview.md)

## Purpose

Keeps the developer-question contract in each capsule: which role may route a question to its parent, how a
question is recovered when it is pending, and where the answer's provenance is stated. It also holds the
upward-notice and downward-answer duties and the leaf `ownerRelation` that names peer results and the
occasions a question goes to the parent.

## Code Commentary

### Logic

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

`question_step` uses the declared source, the role's audience and that role's own pre-action pointer. For message transport it joins the emitted busy-refusal detail with the role's held-delivery paragraph, which must stand exactly once, audience-labelled, in the compiled orientation shared block (deleted clauses, a relabelled or extended paragraph and a duplicate fail); for child questions it follows the delivered return action's single link to the orientation section that owns answer attribution. Its clause-deletion controls read those actual details for busy/held recovery and unchanged developer-answer provenance; the other cases continue to read canonical source or compiled ownerRelation as appropriate. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence

- Orientation keeps conditional routing and pending recovery; review and curation are checked as composed role-plus-operation pairs. [3]


- The parentable-role test checks question recovery and answer provenance in the shared orientation home, requires each selected role to carry its own pointer to that home without copying it, and checks transport clauses through each role's delivered message step and shared held paragraph. [1]


- Starter-role checks require the shared upward permission notice and each role's referral to it, declared transport recovery and the child-question step; the answer clauses retain an own-authority answer, otherwise an unchanged upward question and unchanged quoted developer-answer provenance on the return path. [2]

- The compiled leaf ownerRelation test keeps Worker, Reviewer and Curator peer results direct, reserves named authority/developer occasions to the parent, and requires sibling role/task arguments instead of routine parent result notices. [4]
- The retired-directive control reads the current Manager, Orchestrator and router surfaces, appends each exact retired sentence separately and requires detection; the Architect own-chat sentence is retained as an allowed contrast. [5]
- The compiled leaf ownerRelation test records the descriptive starter identity separately from host.parent.returnAddress: returns use the Manager role and canonical sprint/master task references, while peer results keep sibling leaf addresses. [6]


- `question_step` uses the declared source, the role's audience and that role's own pre-action pointer. For message transport it joins the emitted busy-refusal detail with the role's held-delivery paragraph, which must stand exactly once, audience-labelled, in the compiled orientation shared block (deleted clauses, a relabelled or extended paragraph and a duplicate fail); for child questions it follows the delivered return action's single link to the orientation section that owns answer attribution. Its clause-deletion controls read those actual details for busy/held recovery and unchanged developer-answer provenance; the other cases continue to read canonical source or compiled ownerRelation as appropriate. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [7]
