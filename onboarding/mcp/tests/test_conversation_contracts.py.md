# mcp/tests/test_conversation_contracts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_contracts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate |  2026-07-21T11:31:07+02:00|
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
| The strict production grammar defines all cursor, item, status, capability, operation, recovery, attachment, metric, and fixture products under test. | L25-L1270 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| Foundation tests separately guard ports, route ownership, helper resolution, and installed-fixture topology. | L21-L137 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

## Cross-Repo References

No neighboring repository participates in these contract tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: corrected the capability-demotion coverage for
  the R4 version-gate removal — `test_capability_has_no_version_demotion_predicate` now pins that
  `FeatureCapability` has no `for_observed_runtime` predicate (the contract probe is the only gate;
  version strings are informational metadata). Reworded the former "runtime/helper demotion" Logic
  bullet and added the no-version-gate invariant. Verification metadata stays pinned (uncommitted);
  closeout re-stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the hostile semantic-product test
  sidecar after same-reviewer PASS closed status, capability, open identity, and rollback gaps.
  Verification is blank until closeout commits and stamps the new source.
