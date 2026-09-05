# mcp/tests/test_gate_five_memory_rails.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_gate_five_memory_rails.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `668d710bf2a9898fb706614163462ff346d986b7` |
| lastVerifiedCommitDate | 2026-09-05T02:45:47+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Protects the correspondence between the final memory catalog and its R11 rail population.

## Code Commentary

### Logic

Tests compare each rail with the complete final catalog, require the memory-domain Gate-5 classification and admitted selection id, recompute the expected configuration digest from catalog/registry inputs, and assert unique stable ordering.

### Conventions

These are pure definition-contract tests. They inspect catalog-derived data and do not scan memory, execute checkers or publish certificates.

### Invariants And Boundaries

- Catalog population and rail population agree exactly.
- All rails share the digest of the actual catalog/registry configuration.
- Rail identity and ordering remain deterministic.
- Passing definition checks is not evidence that the Gate-5 executor is called.

### Todos

No additional source defect is asserted by this card.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact catalog population and Gate-5 domain | `test_gate_five_rails_mirror_the_complete_final_catalog` | mcp/tests/test_gate_five_memory_rails.py:19-31 |
| Digest recomputation | `test_gate_five_rails_configuration_digest_is_deterministic_and_bound` | mcp/tests/test_gate_five_memory_rails.py:34-47 |
| Unique canonical ordering | `test_gate_five_rails_are_canonically_ordered_unique` | mcp/tests/test_gate_five_memory_rails.py:50-55 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Created the rail-population test account while preserving the distinction between catalog definitions and actual memory execution.
