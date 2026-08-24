# mcp/src/agents_remember/testing/eligibility.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/eligibility.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Owns the one total, structural admission decision for an explicit bounded direct pytest request.

## Code Commentary

`classify_direct_selection` validates one to eight unique exact selectors under `mcp/tests`,
resolves each AST node, rejects parameterized expansion, asks `DependencyClosureAnalyzer` for the
complete closure, and binds policy version, exact nodes, closure bytes, and root `pyproject.toml`
into a SHA-256 candidate identity. `direct_selection_is_current` repeats that binding before a
result may be retained.

## Invariants And Boundaries

- No test module is imported during classification.
- Only exact function/class-method selectors are accepted; files, globs, flags, and duplicates
  refuse.
- One refused member makes a multi-node request `mixed-selection`; no member executes.
- Policy is `python-direct-eligibility/v1`; changing it is a policy migration.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact total classifier owns validation through binding. | `classify_direct_selection` | mcp/src/agents_remember/testing/eligibility.py:29-59 |
| Candidate currency is recomputed from closure/configuration bytes. | `direct_selection_is_current`; `_candidate_binding` | mcp/src/agents_remember/testing/eligibility.py:118-126; mcp/src/agents_remember/testing/eligibility.py:267-299 |

## Update History

- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
