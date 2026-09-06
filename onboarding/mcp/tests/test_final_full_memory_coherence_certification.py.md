# mcp/tests/test_final_full_memory_coherence_certification.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_final_full_memory_coherence_certification.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `16d1a4d6d6f8e8572b4bca10b8a4a84485449604` |
| lastVerifiedCommitDate | 2026-09-04T00:55:21+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

CCR-R08 forcing suite for the `certify_final_full_memory_coherence` library result assembly
(green, red, blocked, and typed refusal routes) over a synthetic exact candidate pair. The
suite supplies check-result dictionaries and modeled authorities; it does not drive real
memory scans, a closeout entrypoint, certificate publication or Git finalization. Per the
repository file-size-split convention (compare `test_author_execution_graph` importing from
`test_task_execution_topology`) this module also owns the shared Gate-5 fixture scaffold
consumed by the sibling modules `test_final_gate_prefix_adapter`,
`test_final_catalog_plan_attestation`, and `test_final_catalog_readiness_projection`,
because a second non-test module under `mcp/tests` would be governed evidence requiring
lifecycle metadata. The suite is explicitly registered in the `integration` lane of
`test-evidence-lanes.toml`.

## Code Commentary

### Logic

The scaffold builds a complete synthetic R21 chain from production model literals only (no
test-support module, no fixture-repo files): `_inline_profile` (159-240),
`_scenario` (435-474) compiles admission/plan/profile, `_green_prefix` (585-597)
compiles the exact green Gate 1-4 certificates, and the R07 affected-closure fixture builds the
same synthetic scope as the R07 leaf tests (`_r07_candidate` 626-678, `_r07_admission`
733-762, `_affected_plan` 779-785). `_pair` (793-795), `_coherence` (798-829) and
`_passing_checks` (832-837) supply the remaining authorities, and `_EvidenceSpec`
(848-855) / `_evidence` (858-885) compose any scenario, including failing checks and
missing coherence.

The five module-level tests then pin result assembly:

- `test_final_certification_green_binds_exact_pair_and_gate_five_inputs` (888-904) - a green
  certification is finalization-eligible with a fully passing attestation, reused gates 1-4,
  and Gate-5 inputs bound to the exact memory tree and pair authority.
- `test_final_certification_red_blocks_finalization` (907-917) - a failing executed check or
  missing onboarding yields red, no Gate-5 inputs, and no finalization.
- `test_final_certification_blocked_when_full_only_rerun_not_consumed` (920-927) - the
  affected-closure item is blocked when the supplied full-only rerun flag is false.
- `test_final_certification_refuses_without_current_coherence` (930-935) -
  `gate-five-coherence-blocked`.
- `test_final_certification_refuses_stale_prefix_before_any_catalog_work` (938-945) - a code
  input change invalidates the prefix with `gate-five-prefix-invalidated` before any catalog
  work.

### Conventions

Tests call the production library function with synthetic but byte-deterministic R21/R07
authorities and supplied check outcomes. The module adds `mcp/src` to `sys.path` so it can
run against the candidate package. This verifies library composition; the suite's integration
lane classification does not establish production caller wiring or real checker execution.

### Invariants And Boundaries

- The module is the shared fixture scaffold for its three sibling split modules; it is the only
  Gate-5 test module importing the full certification internals.
- No test-support or fixture-module imports; the evidence-lifecycle catalog therefore records no
  transitive test-support consumer here.
- The evidence manifest assigns the suite to the integration lane. Its fixture chain exercises
  the R21/R07 typed library contracts, with modeled rather than producer-executed memory evidence.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared Gate-5 scenario and green-prefix scaffold. | `_scenario`; `_green_prefix` | mcp/tests/test_final_full_memory_coherence_certification.py:435-474; mcp/tests/test_final_full_memory_coherence_certification.py:585-597 |
| The R07 affected-closure fixture reused by the certification. | `_affected_plan`; `_r07_admission` | mcp/tests/test_final_full_memory_coherence_certification.py:779-785; mcp/tests/test_final_full_memory_coherence_certification.py:733-762 |
| Pair, coherence, and executed-checks authorities. | `_pair`; `_coherence`; `_passing_checks` | mcp/tests/test_final_full_memory_coherence_certification.py:793-795; mcp/tests/test_final_full_memory_coherence_certification.py:798-829; mcp/tests/test_final_full_memory_coherence_certification.py:832-837 |
| The composable evidence builder behind every scenario. | `_EvidenceSpec`; `_evidence` | mcp/tests/test_final_full_memory_coherence_certification.py:848-855; mcp/tests/test_final_full_memory_coherence_certification.py:858-885 |
| The green certification binds the exact memory tree, pair authority, and Gate-5 inputs. | `test_final_certification_green_binds_exact_pair_and_gate_five_inputs` | mcp/tests/test_final_full_memory_coherence_certification.py:888-904 |
| Red, blocked, and typed-refusal routes. | `test_final_certification_red_blocks_finalization`; `test_final_certification_blocked_when_full_only_rerun_not_consumed`; `test_final_certification_refuses_without_current_coherence`; `test_final_certification_refuses_stale_prefix_before_any_catalog_work` | mcp/tests/test_final_full_memory_coherence_certification.py:907-917; mcp/tests/test_final_full_memory_coherence_certification.py:920-927; mcp/tests/test_final_full_memory_coherence_certification.py:930-935; mcp/tests/test_final_full_memory_coherence_certification.py:938-945 |
| The suite is registered in the integration lane of the evidence manifest. | "mcp/tests/test_final_full_memory_coherence_certification.py" | mcp/tests/test-evidence-lanes.toml:404-404 |

## Update History

- 2026-09-06T04:32:25+00:00 — L32 incoming-evidence curation: verified the exact cited lane member or current test-function owner against private C b34f4a59 and corrected only its moved coordinates. Existing own-source verification provenance is retained.

- 2026-09-06T00:42:13+00:00 — Gate-5 citation repair: re-read the cited evidence-lane member and its declared classification and corrected its incoming range. Existing source verification provenance is retained.

- 2026-09-05T07:12:23Z — CCR L31 independent-review correction: reread the passing-check
  dictionary builder, evidence fixture and actual library calls at ea359649. Qualified the
  suite's scope as library composition with synthetic authorities, preserved its registered
  lane and useful behavior checks, and removed the unsupported end-to-end execution claim.

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: created this file-level
  onboarding card for the new CCR-R08 final full memory-coherence certification forcing suite
  delivered in code commit 16d1a4d6; anchors and ranges derived from the current worktree source
  and pinned to that commit. The suite entered the `integration` lane of
  `test-evidence-lanes.toml` in the same change.
