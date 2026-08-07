# mcp/tests/test_conversation_contracts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_contracts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash |  `b252c42cca200933d5c9c36e26de47a526a569ce`|
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Provides the hostile semantic-product regression matrix for the normalized native-authoritative
conversation grammar. It proves that valid individual fields cannot combine into false cursor,
provenance, status, capability, identity, rollback, recovery, attachment, or metric authority.

## Code Commentary

### Logic

- Builds reusable exact authorization, active identity, capability evidence, and status fixtures.
- Tests purpose-branded cursor separation, authorization/identity/scope binding, SSE resume
  conflicts, stable item identity/revision/global ordinals, and exact input provenance products.
- Tests image accessibility, canonical status evidence, waiting/terminal sibling matrices, and the
  rule that unknown evidence cannot establish ready.
- Tests capability evidence-tier/state matrices and attachment limits. (260718-CHATS-L5F R4)
  `test_capability_has_no_version_demotion_predicate` now asserts the model carries NO version-gate:
  `FeatureCapability` has no `for_observed_runtime` attribute — the contract probe is the only gate,
  and version strings survive as informational metadata only. The former runtime/helper version
  demotion is removed, not asserted.
- Tests canonical operation fingerprints and the full open identity/catalog/rollback grammar.
- Tests interrupt, queue privacy, authoritative withdrawal/pop-back recovery, attachment state,
  gap/repage, metric evidence, and fixture non-promotion products.
- Tests the multiplexed sub-agent wire additions as purely additive products: `ConversationAgentRef`
  pins the six-word status vocabulary (registered/running/completed/interrupted/failed/unknown), the
  agentId-only minimum, absent-not-null identity fields, and extra-forbid rejection;
  `ConversationItem.agent` defaults absent so the pre-multiplex wire decodes byte-identical and the
  agent key changes nothing else on the envelope; `ConversationLibraryAgentRow` is evidence-bound
  and extra-forbid with a required title; and the library row `agents` grouping plus the page
  `agentsNote` both default to absent.

### Conventions

Authority validators are exercised with valid-product tables plus direct counterexamples for each
sibling state. Pydantic `ValidationError` is part of the expected fail-closed boundary.

### Invariants And Boundaries

- Do not replace product-matrix probes with field-presence assertions.
- Keep exact failed/open identity rollback products bidirectional.
- Raw recovery text may appear only in a successful withdrawn response; pending/failure projections
  must stay raw-free.
- Fixtures remain evidence with `enablesCapabilities=false`.
- No version-string comparison gates a capability: the capability model exposes no
  `for_observed_runtime` demotion predicate (260718-CHATS-L5F R4), and the suite asserts its absence.
- This suite verifies contracts, not projector/native-helper/control implementation behavior.

### Todos

Extend the same hostile-product style when later leaves add DTO states; endpoint behavior belongs
in focused service/API suites.

## Docs References

No Domain Documentation source is configured. The repository-owned model contract is direct
evidence for this internal test suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The strict production grammar defines all cursor, item, status, capability, operation, recovery, attachment, metric, and fixture products under test. | "class ActivePageCursor(_OpaqueToken):"; "class ConversationItem(WireModel):"; "class ConversationStatus(WireModel):"; "class OpenConversationOperation(WireModel):"; "class MetricEvidence(WireModel, Generic[T]):"; "class RuntimeFixtureEvidence(WireModel):" | mcp/src/agents_remember/serving/conversation/_models_wire.py:67-67; mcp/src/agents_remember/serving/conversation/_models_blocks.py:158-158; mcp/src/agents_remember/serving/conversation/_models_status.py:145-145; mcp/src/agents_remember/serving/conversation/_models_operations.py:19-19; mcp/src/agents_remember/serving/conversation/_models_telemetry.py:28-28; mcp/src/agents_remember/serving/conversation/_models_telemetry.py:87-87 |
| Foundation tests separately guard ports, route ownership, helper resolution, and installed-fixture topology. | `test_exactly_two_conversation_ports_exist`; `test_root_composes_three_owned_child_routers`; `test_helper_package_and_lock_select_only_the_exact_repository_dependencies`; `test_installed_runtime_fixtures_are_allowlisted_evidence_not_enablement` | mcp/tests/test_conversation_foundation.py:22-29; mcp/tests/test_conversation_foundation.py:32-107; mcp/tests/test_conversation_foundation.py:125-136; mcp/tests/test_conversation_foundation.py:163-188 |

## Cross-Repo References

No neighboring repository participates in these contract tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 5 citation claims; scoped result 0 findings.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. `models.py`
  is now 1282 lines and the old L25-L1270 stopped inside `operation_fingerprint` cit:(["def operation_fingerprint("], mcp/src/agents_remember/serving/conversation/_models_telemetry.py:100-100), the
  canonical-identity hash the operation products are keyed by. The row now reads L25-L1282: from
  `HarnessId` through the final line of the module, so every product the claim enumerates —
  cursor brands, `ConversationItem`, status, capabilities, operations, recovery, attachments,
  the metric block cit:(["class MetricEvidence(WireModel, Generic[T]):"], mcp/src/agents_remember/serving/conversation/_models_telemetry.py:28-28) and `RuntimeFixtureEvidence` cit:(["class RuntimeFixtureEvidence(WireModel):"], mcp/src/agents_remember/serving/conversation/_models_telemetry.py:87-87) — is inside it. No
  claim text changed.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/tests/test_conversation_contracts.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 19 line(s), touching only redundant grouping
  parentheses. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds. Noted while checking: the references table also
  cites line ranges inside `models.py`; those ranges shifted because this task edited those files,
  so treat the cited numbers as approximate and the linked cards as authoritative.

- 2026-07-26T18:30+02:00 — 260718-CHATS-L7 curator: recorded the four wire-contract additions for
  the multiplexed sub-agent surface — the `ConversationAgentRef` status-vocabulary/additive-shape/
  extra-forbid matrix, `ConversationItem.agent` absent-by-default with the pre-multiplex wire held
  byte-identical, the additive evidence-bound `ConversationLibraryAgentRow`, and the library row
  `agents` + page `agentsNote` absent defaults. One Logic bullet added; verification metadata stays
  pinned (uncommitted); closeout re-stamps the candidate commit.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: corrected the capability-demotion coverage for
  the R4 version-gate removal — `test_capability_has_no_version_demotion_predicate` now pins that
  `FeatureCapability` has no `for_observed_runtime` predicate (the contract probe is the only gate;
  version strings are informational metadata). Reworded the former "runtime/helper demotion" Logic
  bullet and added the no-version-gate invariant. Verification metadata stays pinned (uncommitted);
  closeout re-stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the hostile semantic-product test
  sidecar after same-reviewer PASS closed status, capability, open identity, and rollback gaps.
  Verification is blank until closeout commits and stamps the new source.
