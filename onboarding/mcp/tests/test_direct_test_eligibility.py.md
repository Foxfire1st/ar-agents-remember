# mcp/tests/test_direct_test_eligibility.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_direct_test_eligibility.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Provides pure forcing proof for evidence altitude and every structural direct-test eligibility,
refusal, closure, and candidate-binding boundary.

## Code Commentary

Temporary candidate fixtures cover allowed computation/fixture/helper chains, every unsafe family,
transitive helpers and submodules, autouse fixtures, dynamic dependencies, request-shape and
parameterization refusals, collection-time effects, candidate drift, and whole-request atomicity.
An import-time raising expression proves classification does not execute candidate code. Two
same-named class methods prove scan-cache identity does not conflate source definitions.

## Invariants And Boundaries

- Refusal tests assert stable codes and unsafe families, not incidental prose only.
- Any refused selection executes zero nodes.
- The synthetic candidates test the classifier; they are not admitted production cohort members.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-named methods are scanned independently. | `test_same_named_methods_do_not_share_dependency_cache` | mcp/tests/test_direct_test_eligibility.py:224-251 |
| Import-free classification has a real failing-if-imported sentinel. | `test_transitive_unsafe_helper_refuses_before_execution` | mcp/tests/test_direct_test_eligibility.py:195-222 |

## Update History

- 2026-08-24T20:55+02:00 — Created for 260824-PDLS and records the post-review forcing repairs.
