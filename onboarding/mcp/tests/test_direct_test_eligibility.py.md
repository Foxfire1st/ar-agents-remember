# mcp/tests/test_direct_test_eligibility.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_direct_test_eligibility.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Provides pure forcing proof for evidence altitude and every sealed direct-cohort admission,
refusal, closure, and candidate-binding boundary.

## Code Commentary

Synthetic cohort manifests declare exact admitted node IDs, audited paths and symbols, local-import
closure, effect dispositions, fixture/closure facts, and the configuration digest. The tests prove
only explicit manifest members can enter; mixed or duplicate selections refuse as one unit. A safe
body is insufficient when its import was omitted from the manifest, an audited path is unreachable,
an external or autouse dependency is unknown, or source/configuration bytes drift after review.

Every closed unsafe-effect family produces a stable refusal, including unsafe transitive helpers.
Dynamic calls, parameterized or ambiguous nodes, unsupported fixtures, oversized requests, and
candidate drift are fail-closed. The suite also proves diagnostic evidence remains at diagnostic
altitude and certifying evidence can only be minted by the verified Dagger factory.

## Invariants And Boundaries

- Refusal tests assert stable codes and unsafe families, not incidental prose only.
- Any refused selection executes zero nodes.
- Admission is manifest membership plus a current content seal; structural inference never adds a
  node or silently rebaselines changed inputs.
- The synthetic candidates test the classifier; they are not admitted production cohort members.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture and helper closure is content-sealed before direct execution. | `test_fixture_and_helper_closure_is_content_sealed` | mcp/tests/test_direct_test_eligibility.py:108-135 |
| Import-free classification has a real failing-if-imported sentinel. | `test_transitive_unsafe_helper_refuses` | mcp/tests/test_direct_test_eligibility.py:182-204 |

## Update History

- 2026-08-26T10:44:52+02:00 — Reconciled the suite with sealed manifest admission, audited dependency closure, explicit membership, and fail-closed candidate/configuration drift.

- 2026-08-24T21:23+02:00 — Created for 260824-PDLS and records the post-review forcing repairs.