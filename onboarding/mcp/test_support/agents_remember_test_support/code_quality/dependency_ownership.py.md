# mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `8f670ceecd75323600c873d40c47c4a1cc946ab3` |
| lastVerifiedCommitDate | 2026-09-05T06:48:24+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Owns the source-derived test-consumer graph shared by targeted selection, retry proof and causal localization. It preserves reason provenance and distinguishes proved global invalidation from unresolved ownership.

## Code Commentary

### Logic

DependencyOwnershipGraph builds repository dependency facts, observed imports/literal consumers and independently checked evidence-catalog declarations. resolve retains every unresolved input and returns complete=false instead of silently expanding an incomplete graph. Parse failures, ambiguous modules and invalid lifecycle catalogs produce explicit unresolved reasons.

Changed tests own themselves; deleted tests leave the population. Shared support must have observed consumers. Repository-owned non-Python inputs, including the certification profile, may declare exact consumers only when the observed set matches exactly. The profile consumer set now includes bridge, record-seam and rail-binding tests. A declaration does not prove itself.

Global inputs and conftest roots deliberately invalidate the full population and are separately recorded. Otherwise observed import/literal relationships are preferred; filename matching remains a labeled heuristic. ownership_configuration_digest binds the versioned global inputs, declarations, irrelevant roots/suffixes and dashboard test patterns, so selection authority changes are visible.

### Conventions

Keep test-consumer ownership separate from product-package/coverage ownership. Use deterministic sorted paths and typed SelectionReasonKind values when reporting why a test was selected or an input remains unresolved.

### Invariants And Boundaries

- Unknown ownership does not become a safe-full success at this layer.
- Catalog declarations must agree with independently observed consumers.
- Intentional pytest-global invalidation is distinct from incomplete ownership.
- Necessary import fan-out remains attributable rather than being pruned for speed.
- The selector configuration digest changes when classification authority changes.

### Todos

The previous card incorrectly described unresolved ownership as a full-population fallback. Current source retains incomplete/unresolved results and the targeted caller refuses them.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Global inputs and versioned repository-owned declarations | `GLOBAL_TEST_INPUTS`; `OWNERSHIP_AUTHORITY_VERSION`; `REPOSITORY_TEST_INPUT_CONSUMERS` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:24-52 |
| Typed reasons and incomplete graph behavior | `SelectionReasonKind`; `SelectionReason`; `TestImpact`; `resolve`; `_resolved_impact` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:227-365 |
| Global invalidation and exact consumer matching | `_repository_consumers`; `_test_tree_consumers` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:368-459 |
| Import closure and evidence-catalog consumer discovery | `transitive_importers`; `reverse_import_closure`; `_declared_consumers` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:527-581 |
| Selection authority configuration digest | `ownership_configuration_digest` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:598-619 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Corrected obsolete safe-full wording to the implemented explicit unresolved-ownership contract and incorporated new profile consumers.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: rewrote the
  Docs References task-artifact rows as prose (absolute ar-coordination paths are not
  repo-relative citations and carry no verifiable provenance).

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for eb05a872780112640359232063168639d20fa87b (root bootstrap repair): documented the added exact literal consumer `mcp/tests/test_gate_certificate_authority.py` for the certification profile; verification metadata rebased from `0506b57a` to the bootstrap repair owning commit.

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 added exact, source-verified ownership for
  `layers.toml`: five declared consumers, no full-population launch, and no scanner fallback.
  Verification remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 added source-verified exact consumer ownership for `.codex/config.toml`, avoiding both global invalidation and an unproved narrow selection. Verification remains closeout-owned.

- 2026-08-27T14:04+02:00 — Removed the misleading graph-local `product_*` projection. Consumer
  ownership remains cross-package; explicit configured package authority now exclusively owns the
  distinct product-versus-verification measurement decision.

- 2026-08-27T11:14+02:00 — Reconciled source-first ownership: recursive plugin/import/reference
  facts are authoritative, catalog consumers are a cross-check, and incomplete truth names a fresh
  rerun instead of silently selecting a narrower population.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
