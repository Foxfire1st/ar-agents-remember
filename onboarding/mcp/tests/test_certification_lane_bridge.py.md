# mcp/tests/test_certification_lane_bridge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_certification_lane_bridge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `668d710bf2a9898fb706614163462ff346d986b7` |
| lastVerifiedCommitDate | 2026-09-05T02:45:47+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Tests the canonical R11/R22 bridge against the actual repository profile, including the memory rail contribution, deterministic identity and currentness refusal.

## Code Commentary

### Logic

Fixtures admit the checked-in profile and compile a repository plan, then supply catalog-derived Gate-5 rails. The main test checks one five-gate authority with matching registry/admission/profile identities. Other cases change provenance, remove or corrupt memory rails, select a non-applicable gate population, or change registry identity and currentness inputs.

The tests confirm that changing memory rails changes authority and that unchanged semantic inputs stay deterministic. They do not run the profile's commands or prove that declared result files have production writers.

### Conventions

Use the real profile vocabulary while keeping candidate/provenance fixtures synthetic. Negative tests should preserve typed finding identity rather than accept a generic exception.

### Invariants And Boundaries

- No bridge admission without the memory contribution.
- Invalid gate/domain memory rails and non-applicable repository gates refuse.
- Provenance timestamps must not change semantic digests.
- Contract consistency is distinct from production gate execution.

### Todos

Keep real executor-to-record integration tests separate from these compiler fixtures.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Five-gate authority and provenance-independent determinism | `test_bridge_derives_one_canonical_five_gate_authority_from_the_real_profile`; `test_bridge_is_deterministic_and_ignores_creation_provenance` | mcp/tests/test_certification_lane_bridge.py:74-122 |
| Missing/non-applicable/moved memory contribution | `test_bridge_rejects_a_missing_gate_five_population`; `test_bridge_refuses_a_not_applicable_repository_selection`; `test_bridge_memory_rails_are_part_of_the_registry_digest` | mcp/tests/test_certification_lane_bridge.py:125-178 |
| Currentness, explicit registry identity and malformed memory rails | `test_bridge_admit_currentness_reread_accepts_and_refuses_movement`; `test_bridge_registry_id_is_bound_when_supplied`; `test_bridge_refuses_an_invalid_gate_five_memory_rail` | mcp/tests/test_certification_lane_bridge.py:218-281 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Created the bridge test contract with an explicit boundary between profile/compiler coverage and real execution proof.
