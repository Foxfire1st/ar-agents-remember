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
  orientation, and reviews and curation by joining each role's text to its operation text.
- **Manager wait recording.** `test_manager_records_an_already_sent_developer_question_wait_locally` reads the Manager's delivered `reference/message-handover.md` (`## Ask for a developer decision`) and requires that when no independent work remains, the Manager records the wait in its end line and status file rather than sending a wait message, while other roles send what they await with `role_message`, rejecting the retired wording `"record your state in your report and send what you await"`.
- **Owner relation.** `test_leaf_owner_relation_keeps_peer_results_and_named_parent_occasions` keeps the
  leaf's peer results and the named parent occasions, with the compiled `ownerRelation` carrying the current
  Manager's role and task return address separately from the descriptive starter identity.
- **Retired directives.** `test_exact_retired_directives_are_detected_as_independent_sentences` proves each
  exact retired directive is detected as an independent sentence, so a surviving fragment is caught.

### Conventions

Transport and child-question details are checked from the emitted orientation capsule and its shared paragraph. The review and curation pointer checks join role text with operation text; they do not compile those operation pairs.

### Invariants And Boundaries

- Questions requiring the developer's decision follow the named parent route. Results and questions about another leaf seat's work go directly to that seat.
- A pending question is recovered rather than re-asked from scratch.

`question_step` uses the declared source, the role's audience and that role's own pre-action pointer. For message transport it joins the emitted busy-refusal detail with the role's held-delivery paragraph, which must stand exactly once, audience-labelled, in the compiled orientation shared block (deleted clauses, a relabelled or extended paragraph and a duplicate fail); for child questions it follows the delivered return action's single link to the orientation section that owns answer attribution. Its clause-deletion controls read those actual details for busy/held recovery and unchanged developer-answer provenance; the other cases continue to read canonical source or compiled ownerRelation as appropriate. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

`answer_provenance` follows the emitted child-return pointer to the shipped orientation attribution section and requires those orientation bytes to equal the canonical checkout copy. Its mismatch assertion says `Run mcp/.venv/bin/python scripts/renew-instructions.py`. [8]

## Evidence




- The parentable-role test checks question recovery and answer provenance in the shared orientation home, requires Worker/Reviewer/Curator to carry an orientation referral and Orchestrator/Manager/Investigator to carry their role question route without copying the orientation text, and checks transport clauses through each role's delivered message step and shared held paragraph. [1]



- Starter-role checks require `operations/coordination.md` to link the shared upward permission notice in `closeout-recovery.md` without copying it into starter roles, and check declared transport recovery and the child-question step; the answer clauses retain an own-authority answer, otherwise an unchanged upward question and unchanged quoted developer-answer provenance on the return path. [2]


- `question_step` uses the declared source, the role's audience and that role's own pre-action pointer. For message transport it joins the emitted busy-refusal detail with the role's held-delivery paragraph, which must stand exactly once, audience-labelled, in the compiled orientation shared block (deleted clauses, a relabelled or extended paragraph and a duplicate fail); for child questions it follows the delivered return action's single link to the orientation section that owns answer attribution. Its clause-deletion controls read those actual details for busy/held recovery and unchanged developer-answer provenance; the other cases continue to read canonical source or compiled ownerRelation as appropriate. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [7]

- The compiled leaf ownerRelation test keeps Worker, Reviewer and Curator peer results direct, reserves named authority/developer occasions to the parent, and requires sibling role/task arguments instead of routine parent result notices. [4]

- The retired-directive control reads the current Manager, Orchestrator and router surfaces, appends each exact retired sentence separately and requires detection; the Architect own-chat sentence is retained as an allowed contrast. [5]

- The compiled leaf ownerRelation test records the descriptive starter identity separately from host.parent.returnAddress: returns use the Manager role and canonical sprint/master task references, while peer results keep sibling leaf addresses. [6]

- Orientation keeps conditional routing and pending recovery; review and curation pointers are checked over joined role and operation source text. [3]

### Repo-Internal References (renewed)

- answer_provenance requires the shipped orientation attribution owner to match canonical checkout bytes; a mismatch names `Run mcp/.venv/bin/python scripts/renew-instructions.py`. [8]
