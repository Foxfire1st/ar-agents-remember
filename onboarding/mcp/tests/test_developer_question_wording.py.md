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

The cases read the canonical role and operation skill files rather than compiled capsules, so what is
checked is the source wording a seat's capsule is built from; only the leaf `ownerRelation` case reads a
capsule the launch compiles.

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

## Evidence


- The parentable roles carry the question, recovery, provenance and notice clauses. [1]


- Every starter role carries the upward notice and unchanged downward answer duties. [2]

- Orientation keeps conditional routing and pending recovery; review and curation are checked as composed role-plus-operation pairs. [3]

- The leaf `ownerRelation` keeps peer results and named parent occasions. [4]


- Each exact retired directive is detected as an independent sentence. [5]


- The compiled leaf `ownerRelation` carries the current Manager role and task return address separately from the descriptive starter identity. [6]
