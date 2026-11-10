# mcp/test_support/agents_remember_test_support/testing/curator_contracts.py

## Governing Overview

[overview](overview.md)

## Purpose

The module supplies the shared Curator and coordination instruction contracts: required clause sets, an action-local link follower, a compile of every declared role/operation pair through the real capsule compiler, and pattern checks for forbidden healing and writer wording.

## Code Commentary

Clause tuples (for example the card-authoring, history disposition, writer identity, publication and fact-check sets) are matched after normalization that drops `*` and backticks and collapses whitespace. `linked_section` requires exactly one paragraph holding both the action and the labelled link, the action before the link, a relative link resolving to the named owner file with the GitHub anchor of the heading, and returns that section. `compile_matrix` reads `composition-manifest.json`, requires the role and operation lists to agree, and compiles each pair with fixture admitted facts and the full public tool roster; any refused compile fails. `healing_findings` flags own-fault-only healing and blanket debt routing; `writer_findings` flags a bare PATH `agents-remember knowledge-ingest|bootstrap` command and leaf self-production wording.

`require_permission_delivery` follows the refused-write detail's pointer to `## Honor harness permission decisions` in the shipped `operations/orientation.md` (whose bytes must equal the corpus copy), requires the permission clauses there, and proves that deleting any clause or breaking the link label, anchor or paragraph fails. `require_coordination_routes` requires the held-delivery clause in `core/authority.md`, exactly once in the Orchestrator's delivered shared block, the Orchestrator's held-delivery action exactly once, and the `operations/coordination.md` links to the full-store refusal section of `reference/message-handover.md` and the failure-handling section of `operations/curation.md`, each with mutants that must fail. `expected_bound_detail` keeps a detail's text and rewrites only its relative inline links to the given resolved targets.

Its readers are the Curator wording, delivery, healing and correction-guidance tests, the developer-question, role-message, link-integrity and wording-pin tests, the converted-onboarding bootstrap test, `mcp/tests/role_instruction_wording_support.py` and `curator_instruction_delivery.py`.

## Evidence

- One action-local link is followed to its exact owner file and heading. [1]
- Every declared role/operation pair is compiled through real admission and the capsule compiler. [2]
- Card authoring requires per-sentence decisions and removal of past accounts. [3]
- Healing wording is rejected when it limits repair to own faults or routes all debt away. [4]
