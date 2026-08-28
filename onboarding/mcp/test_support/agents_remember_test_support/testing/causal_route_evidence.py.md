# mcp/test_support/agents_remember_test_support/testing/causal_route_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/causal_route_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T10:16:27+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Builds and verifies the real Dagger cascade comparing unlocalized symptoms with exact owner-level
causal suppression and rollback.

## Code Commentary

### Logic

The route prepares one failed contract artifact, runs a five-node baseline containing three
source-proved downstream symptoms plus two independent nodes, reruns the same population with exact
causal input, and compares outcomes and phase timings. The machine artifact records the baseline's
three symptom-level action targets versus the localized route's one corrective owner, the explicit
one-edit-per-presented-target validation protocol, independent-node preservation, and limitations
that separate those protocol counts from observed human behavior.

### Conventions

The failing baseline is expected evidence, not a green acceptance gate.

### Invariants And Boundaries

- Exactly the three source-proved dependent nodes may skip in the localized run.
- Same-file and unrelated nodes must execute in both runs.
- Omitting causal input restores full execution while preserving the report.
- The comparison remains non-accepting and publishes raw phase/outcome evidence rather than a
  timing-only speed claim.

### Todos

None.

## Docs References

No external contract applies.

## Repo-Internal References

The Dagger owner is `AgentsRememberQuality.causal_evidence`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The forcing route binds one real owner failure to exactly three source-derived dependent nodes and rejects either independent node entering the blocked set. | `DEPENDENT_NODES`; `prepare_forced_report` | mcp/test_support/agents_remember_test_support/testing/causal_route_evidence.py:33-78 |
| Verification requires three baseline failures, three localized skips, and two independent passes in both phases before publishing comparison evidence. | `verify_route_evidence` | mcp/test_support/agents_remember_test_support/testing/causal_route_evidence.py:81-161 |
| The comparison records phase timings, presented action targets, edit/rerun protocol counts, avoided amplification, and explicit interpretation limits. | `verify_route_evidence` | mcp/test_support/agents_remember_test_support/testing/causal_route_evidence.py:81-161 |
| The five-node population uses the ordinary certifying pytest composition and is Dagger-admission guarded. | `run_proof_population` | mcp/test_support/agents_remember_test_support/testing/causal_route_evidence.py:164-194 |

## Cross-Repo References

No cross-repository boundary applies.

## Update History

- 2026-08-28T10:03:40+02:00 — Expanded the real Dagger proof to a three-symptom/two-independent
  cascade with before/after phase timings, action-target/rerun counts, and explicit limitations.
- 2026-08-28T04:37+02:00 — Rebound the forcing population to the renamed independent-node
  regression while preserving exact dependent-only suppression.
- 2026-08-27T11:08+02:00 — Created for real-route causal and rollback proof.
