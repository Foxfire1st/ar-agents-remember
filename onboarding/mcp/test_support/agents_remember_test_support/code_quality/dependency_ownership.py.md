# mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T11:33+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Python quality overview](overview.md)

## Purpose

Provides the canonical test-consumer graph used by targeted selection, retry proof, and causal localization.

## Code Commentary

### Logic

It builds one immutable graph from tracked Python imports, recursive literal `pytest_plugins`
declarations, exact source references, and the complete test population. Lifecycle-catalog
consumers are only an independently checked assertion: they must agree with observed source facts
and cannot make an otherwise incomplete graph complete. Every selected consumer retains its reason
provenance. Parse failures, dynamic plugin declarations, ambiguous modules, unowned changes, or
catalog disagreement return an explicit `fresh_rerun_reason` over the full population.

Repository-owned non-Python product inputs that cannot enter the import graph may declare an exact
consumer set here. That declaration is admitted only when source-observed literal reads match it
exactly. `.codex/config.toml` names its two public-surface/starter consumers. `layers.toml` names its
five architecture and structural-policy consumers through one composed `Path` identity; the
source-observed literal scanner independently proves the same set. Any mismatch widens safely
instead of trusting stale metadata.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Selection, retry, and causal localization share one owner; necessary import fan-out is preserved
  and attributed; unknown or ambiguous dependency truth fails closed to a named fresh rerun.
- Source-derived facts are authoritative. Lifecycle declarations are validated against them and
  never self-prove their own consumer completeness.
- The graph answers dependency/test-consumer questions across product and verification packages;
  it deliberately does not infer which importable package is operational product. Targeted and
  full measurement consume the explicit package-authority reader for that separate decision.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- An explicit non-Python consumer declaration never self-proves: the graph compares it with observed
  consumers before targeted selection may use it.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `DependencyOwnershipGraph` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:81-301 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| Graph construction refuses source parse and module ambiguity before consulting declarations. | `DependencyOwnershipGraph`; `__init__`; `resolve` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:81-153 |
| Catalog consumers are cross-checked against independently observed consumers. | `_repository_consumers`; `_test_tree_consumers` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:167-226 |
| Incomplete ownership returns the full population with one stable fresh-rerun reason. | `_safe_full` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:316-325 |
| The root layer contract has one exact repository-owned declaration and five independently observed consumers. | `LAYERS_CONTRACT_PATH`; `REPOSITORY_TEST_INPUT_CONSUMERS` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:29-50 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `DependencyOwnershipGraph` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:81-301 |

## Update History

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
