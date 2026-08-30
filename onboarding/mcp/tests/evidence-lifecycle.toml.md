# mcp/tests/evidence-lifecycle.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/evidence-lifecycle.toml` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-29T23:04+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5`|
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
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

## Update History

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
