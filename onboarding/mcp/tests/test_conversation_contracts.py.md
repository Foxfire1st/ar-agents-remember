# mcp/tests/test_conversation_contracts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_contracts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The strict production grammar defines all cursor, item, status, capability, operation, recovery, attachment, metric, and fixture products under test. | L25-L1282 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| Foundation tests separately guard ports, route ownership, helper resolution, and installed-fixture topology. | L21-L137 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

## Cross-Repo References

No neighboring repository participates in these contract tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. `models.py`
  is now 1282 lines and the old L25-L1270 stopped inside `operation_fingerprint` (L1265-L1282), the
  canonical-identity hash the operation products are keyed by. The row now reads L25-L1282: from
  `HarnessId` through the final line of the module, so every product the claim enumerates —
  cursor brands, `ConversationItem`, status, capabilities, operations, recovery, attachments,
  the metric block (L1185-L1242) and `RuntimeFixtureEvidence` (L1252-L1262) — is inside it. No
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
