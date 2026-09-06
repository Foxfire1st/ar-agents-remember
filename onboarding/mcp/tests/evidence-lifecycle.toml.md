# mcp/tests/evidence-lifecycle.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/evidence-lifecycle.toml` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-09-06T21:51:32+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Declares the current 42 shared-support/fixture artifacts and four executable replacement contracts. The catalog preserves authority, fidelity, lifetime and exact source-observed consumers for the reduced suite; deleted artifacts and their old consumer populations are no longer active declarations.

## Code Commentary

### Logic

Contract rows bind a production owner to a retained executable evidence node. Artifact rows state
category, authority, fidelity, cadence, provenance, permanence/expiry rationale, replacement
contract and consumers. The public validator checks observed consumers against declarations;
keeping a stale consumer merely because an older suite used it is not valid ownership.

The store harness now points to retained provider process-race evidence. Generic synthetic evidence
uses the retained dependency-ownership test as its replacement node. Shared profile/certification
support retains exact consumers without claiming that synthetic fixture bytes are installed-executor
proof. `large_fixture_bytes=25000` controls discovery of unknown non-source suffixes; the catalog
is a policy input excluded from its own artifact population.

### Invariants And Boundaries

- Missing, stale, contradictory or consumer-incomplete declarations refuse.
- Fidelity and permanence are independent of evidence-lane labels.
- Exact source-observed ownership includes transitive consumers where declared; no old count is authoritative.
- The catalog remains a global pytest policy input; that is distinct from broadening an individual helper’s ownership.
- Removing unused scaffolding does not authorize unowned new evidence or a second fixture catalog.

## Docs References

No external Domain Documentation source is configured; these are repository-owned implementation facts.

## Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Catalog schema and large-fixture discovery threshold | `schema_version` | mcp/tests/evidence-lifecycle.toml:1-2 |
| Four retained executable replacement contracts | `contract` | mcp/tests/evidence-lifecycle.toml:4-22 |
| Actual process-race support and two consumers | "_store_durability.py" | mcp/tests/evidence-lifecycle.toml:44-61 |
| Retained registry fixture ownership | "certification_registry_test_support.py" | mcp/tests/evidence-lifecycle.toml:488-507 |
| Profile support and current consumer declarations | "repository_profile_test_support.py" | mcp/tests/evidence-lifecycle.toml:508-546 |

## Cross-Repo References

No separate cross-repository authority is established by this file.

## Update History

- 2026-09-06T21:51:32+00:00 — Reconciled the retained IAS implementation and diagnostic testing policy with current source citations; prior verification provenance is retained and no new test or review result is claimed.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Registered the extracted gate fixture and publication-suite consumers in durable memory; reconciled exact-source runner ownership with the distinct pytest closure.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): recorded the L21 registration of
  `test_gate_certificate_authority.py` as an exact consumer of the shared certification and
  closeout-input support rows whose builders its forcing suite imports. Verification is pinned
  to the owning commit.

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
