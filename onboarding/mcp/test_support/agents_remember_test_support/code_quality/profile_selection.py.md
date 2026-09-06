# mcp/test_support/agents_remember_test_support/code_quality/profile_selection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/profile_selection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | db57101a9001ede8c681ff9de4eb0147d8b636bc |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python quality verification overview](overview.md)

## Purpose

Publishes the exact repository-owned scope consumed by the certification profile rails: the
Agents Remember test-selection provider. L19 rebuilt it as a content-addressed selector emitting
the canonical `repository-selector-result/v2` contract with typed unresolved inputs, exact
candidate binding, and no safe-full expansion.

## Code Commentary

### Logic

`selection_result` derives either the declared full population or the diff-owned targeted scope
from the canonical quality-scope plus targeted ownership owners. Full mode publishes
`declared-full-mode` as its global invalidator; targeted mode resolves the affected tests,
dashboard suite, coverage roots, and every input decision as typed `RepositorySelectionReason`
rows. All outputs are wrapped by `build_repository_selection_result` into one digest-bound
result. `selection_payload` returns the canonical JSON shape for rail comparison.
`_verify_admitted_identity` refuses a selector invocation whose
id/version/configuration-digest or candidate (kind/value) does not match the versioned ownership
authority and the live Git index; `_confined_output` confines the published result to the
candidate or the admitted sandbox scratch root. `main` requires Dagger admission and prints
either a complete population with digest or the typed
`test-selection-ownership-incomplete` outcome with unresolved-input count and digest.

### Conventions

- Selector identity constants (`SELECTOR_ID`, version from the ownership authority) are the
  admission truth for rail invocations.
- Every output value carries an exact dependency reason; there is no selection without a reason.

### Invariants And Boundaries

- Empty, targeted, and full are explicit modes; full is declared, never inferred.
- An incomplete targeted impact publishes every unresolved input and zero selected tests; it never
  expands to safe-full or a language-specific fallback.
- The candidate tree is derived from the Git index (`git write-tree`) and must match the
  admitted invocation.
- The selector never executes tests; it only publishes the exact population contract.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; CCR-R19@v2 is the governing packet. The
R19 packet requires complete repository-owned selection with typed ownership failure; the packet
path is a task artifact and is recorded as prose here (not a repo-relative citation).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The selector derives and publishes one content-addressed result for full or targeted mode. | `selection_result`; `selection_payload` | mcp/test_support/agents_remember_test_support/code_quality/profile_selection.py:63-128; mcp/test_support/agents_remember_test_support/code_quality/profile_selection.py:150-164 |
| Candidate identity is derived from the Git index and verified against the admitted invocation. | `_candidate_identity`; `_verify_admitted_identity` | mcp/test_support/agents_remember_test_support/code_quality/profile_selection.py:167-177; mcp/test_support/agents_remember_test_support/code_quality/profile_selection.py:396-409 |
| Input decisions map to typed select/global-invalidate/irrelevant/unresolved reason rows. | `_scope_reasons`; `_unresolved_reason`; `_dashboard_invalidators` | mcp/test_support/agents_remember_test_support/code_quality/profile_selection.py:218-254; mcp/test_support/agents_remember_test_support/code_quality/profile_selection.py:305-311; mcp/test_support/agents_remember_test_support/code_quality/profile_selection.py:328-340 |
| Output confinement keeps published results inside the candidate or admitted scratch root. | `_confined_output` | mcp/test_support/agents_remember_test_support/code_quality/profile_selection.py:351-377 |
| The provider serializes the canonical v2 selector result through the shared constructor. | "def build_repository_selection_result(" | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:199-237 |

## Cross-Repo References

None; this is the Agents Remember selector provider instance.

## Update History

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: rewrote the
  Docs References task-artifact row as prose (absolute ar-coordination paths are not
  repo-relative citations and carry no verifiable provenance).

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card and recorded the
  L19 rebuild — content-addressed v2 selector result, declared full/empty modes, typed unresolved
  inputs, dashboard suite invalidators, and admitted identity/candidate verification with no
  safe-full fallback. Verification is pinned to the owning commit.
