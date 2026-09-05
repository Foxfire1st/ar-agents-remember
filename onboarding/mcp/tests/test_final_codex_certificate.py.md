# mcp/tests/test_final_codex_certificate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_final_codex_certificate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Standalone CCR-R14 Gate-4 certificate binding tests (leaf 260831-CCR-L14, code commit 54ff803a). The suite covers the one bound Gate-4 certificate: it requires the exact green Gate-1..3 predecessor certificate identities, a complete terminal two-fresh-pass run bound to the exact frozen plan and candidate, shared runtime authority, and green result manifests for both repetitions. Every stale, red, incomplete, mismatched, or retried composition refuses before a certificate can publish. Fully standalone: it imports only the leaf-local builder module and the package under test.

## Code Commentary

### Logic

`predecessor_identities` (lines 35-41) builds the ordered Gate-1..3 certificate identities, and `green_run` (lines 42-59) publishes a complete two-fresh-pass run. `FinalCodexCertificateTests` (lines 60-166) covers: a green two-fresh-pass publishing the bound certificate (61-79); a red manifest refusing publication (80-106); a one-pass/one-fail composition never compensating (107-140); a candidate mismatch refusing (141-154); and diagnostic or partial predecessors refusing (155-166).

### Conventions

Every refusal asserts a typed `CertificationContractError` code from the `final-codex-` certificate family.

### Invariants And Boundaries

- A certificate binds the exact ordered Gate-1..3 predecessor identities.
- Only a complete terminal two-fresh-pass run can publish; one pass never compensates the other.
- Predecessor manifests must bind the exact frozen plan and candidate at certifying altitude.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R14@v3 (approved packet, leaf 14_final-real-codex-certification) requires the bound Gate-4 certificate semantics; task artifact paths are not repo-relative citations, so clauses are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| Only the exact two-fresh-pass run publishes a bound certificate. | `FinalCodexCertificateTests` | mcp/tests/test_final_codex_certificate.py:60-166 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exercises the bound certificate compiler. | `compile_gate_four_certificate` | mcp/src/agents_remember/certification/final_codex/certificate.py:117-204 |
| The shared leaf builders supply the two-fresh run and its manifests. | `green_run`; `gate4_manifest` | mcp/tests/test_final_codex_certificate.py:42-59; mcp/tests/test_final_codex_models.py:289-297 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| Every case is in-process and repository-neutral. | - | - |

## Update History

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new standalone CCR-R14 certificate-binding suite delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
