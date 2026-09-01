# mcp/tests/evidence-lifecycle.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/evidence-lifecycle.toml` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-09-01T11:33+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This TOML file is the enforced lifecycle registry for durable Python test evidence, shared support,
fixtures, and their stable executable replacement contracts.

## Logic

Contract rows bind an owner to an executable evidence node. Artifact rows state authority,
category, fidelity, cadence, provenance, lifetime, permanence/expiry rationale, replacement
contract, and exact source-observed consumers. The public lifecycle validator rejects missing,
stale, contradictory, unowned, or consumer-incomplete rows.

## Current PDLS Delta

The `repository-ruff-policy-evidence` contract and `_ruff_repository_evidence.py` artifact register
the shared Ruff boundary created by the quality-test split, including every direct importer in the
quality-check, quality-scope, file-size, and tool-signature suites. `_quality_admission.py` now lists
the new tool-signature suite as an exact consumer. `large_fixture_bytes` is an operational discovery
threshold for unknown non-source suffixes, not dormant metadata. The catalog is the policy input to
that discovery and is intentionally excluded from its own artifact population, avoiding a recursive
requirement to catalog itself when it crosses the configured size.

The curator-coherence lifecycle suite imports the shared closeout-input test composition root, so
`test_curator_coherence.py` is an exact consumer of `closeout_input_test_support.py`. Keeping that
edge explicit lets source-derived ownership detect later additions and removals instead of silently
accepting a stale hand-maintained consumer set.

`curator_coherence_test_support.py` is registered as internal canonical shared support with the
complete source-derived transitive consumer set created by `test_worktree_support.py`. Its
replacement node exercises the public single-authority publication and historical-Markdown
non-authority contract. The row makes the helper's local-composition fidelity, affected cadence,
permanent lifetime, and production-publication boundary explicit; exact ownership is not reduced
to the three files that import it directly.

## MCAR-L03 Exact Pair Consumer Delta

`test_memory_candidate_pair.py` exercises closeout admission and canonical curator-coherence
publication through the same shared test composition roots as the existing lifecycle suites. It is
therefore an exact source-derived consumer of both `closeout_input_test_support.py` and
`curator_coherence_test_support.py`. The two catalog rows name that edge explicitly so the
evidence-lifecycle validator can distinguish an intentional shared dependency from an incomplete
ownership declaration.

## ARSPAWN-L4 Public-Surface Consumer Delta

`test_public_surface_conformance.py` imports the shared runtime-settings builders from
`test_config.py`. That module reaches the closeout and curator-coherence fixture roots through
`test_worktree_support.py`, so the source-derived ownership graph classifies the public-surface
suite as an exact transitive consumer of both `closeout_input_test_support.py` and
`curator_coherence_test_support.py`. The two catalog rows now declare those exact edges; no helper
was copied and no direct-import exception was added.

## ARSPAWN-L5 Ambient-Reviewer Consumer Delta

`test_dispatch_agent_ambient_reviewer.py` imports the shared ambient-dispatch topology builder,
whose test composition reaches both the closeout-input and curator-coherence fixture roots. The
source-derived ownership graph therefore classifies the reviewer suite as an exact transitive
consumer of `closeout_input_test_support.py` and `curator_coherence_test_support.py`; both catalog
rows declare that edge explicitly.

## Certification Registry Support Ownership

`certification_registry_test_support.py` is permanent internal-canonical shared support for the
generic certification registry contract. It owns portable registry/result builders and bounded
graph families used by exactly the plan-authority, rail-registry, contract-model edge,
reachability edge, and registry-validation edge suites. The catalog gives it affected cadence,
in-process public-contract fidelity, a concrete replacement node, and an exact five-consumer set;
it does not broaden to the full Python population or smuggle an Agents Remember repository profile
into shared support.

| Finding | Anchor | Source |
| --- | --- | --- |
| The permanent shared-support artifact has exact ownership, replacement, and five-consumer declarations. | "mcp/tests/certification_registry_test_support.py" | mcp/tests/evidence-lifecycle.toml:1113-1133 |

## Update History

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 expanded the certification shared-support row to
  the complete five-consumer set exposed by the source graph. Verification remains closeout-owned.

- 2026-09-01T03:11+02:00 — Registered the portable certification composition owner with its two
  exact focused-suite consumers. Verification remains closeout-owned.

- 2026-08-31T12:39+02:00 — Added `test_dispatch_agent_ambient_reviewer.py` to both exact transitive
  consumer sets after the L5 closeout fast hook identified the previously undeclared ownership
  edges.

- 2026-08-30T16:32+02:00 — Added `test_public_surface_conformance.py` to both exact transitive
  consumer sets after the L4 staged fast hook exposed the source-derived ownership edges; the
  focused lifecycle validator passes with 35 governed artifacts.

- 2026-08-29T23:04+02:00 — Added `test_memory_candidate_pair.py` to the exact source-derived
  consumer sets for the closeout-input and curator-coherence test composition roots after the
  A002 lifecycle fast hook exposed both missing edges.

- 2026-08-29T12:27+02:00 — Reconciled the curator-coherence helper's declared consumers with the
  source-derived transitive ownership graph after generation 7 rejected the direct-import-only
  catalog row. Verification remains closeout-owned.

- 2026-08-29T12:10+02:00 — Registered the shared curator-coherence fixture-input owner and its
  three exact importers after the generation-6 fast hook rejected the uncatalogued helper.
  Verification remains closeout-owned.

- 2026-08-29T09:58+02:00 — Added the curator-coherence suite to the exact source-derived consumer
  set for the shared closeout-input test support after the targeted closeout gate exposed the
  missing edge.
- 2026-08-28T05:10+02:00 — Recorded the operational unknown-suffix threshold and the lifecycle
  catalog's explicit policy-input/non-artifact boundary after Q5 v19 forced the self-reference case.
- 2026-08-27T13:32+02:00 — Registered the split Ruff support and its exact consumers. Verification
  remains closeout-owned.
