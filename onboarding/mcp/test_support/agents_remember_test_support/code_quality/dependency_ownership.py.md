# mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Owns the source-derived test-consumer graph shared by targeted selection, retry proof and causal localization. It preserves reason provenance and distinguishes proved global invalidation from unresolved ownership.

## Code Commentary

### Logic

DependencyOwnershipGraph builds repository dependency facts, observed imports/literal consumers and independently checked evidence-catalog declarations. resolve retains every unresolved input and returns complete=false instead of silently expanding an incomplete graph. Parse failures, ambiguous modules and an invalid lifecycle catalog, caught as the shared catalog reader's `EvidenceLifecycleError`, produce explicit unresolved reasons.

Changed tests own themselves; deleted tests leave the population. Repository-owned non-Python
inputs declare exact consumers only when the independently observed set matches. The reduced
suite's declarations enumerate retained consumers rather than old suite counts. An explicitly
declared empty set is distinct from an absent declaration: only observed-empty equality emits
`verified-repository-input-no-consumers`. Unknown inputs still retain unresolved ownership;
empty declarations cannot hide an actual consumer.

The retired ambient-role scenario runner has no current repository-input declaration. Retained declarations are evaluated against independently observed consumers; catalog identity alone never supplies a missing selection edge.

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

## Evidence

### Docs References

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

No configured external domain source.

### Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or certification pass.

- Transitive importer closure [2]
- Digest binds declarations and classification authority [3]



- An invalid lifecycle catalog is caught as the shared catalog reader's error, not as a bare TOML error, and becomes an unresolved selection reason. [5]
- Observed and declared ownership, exact-empty distinction and refusals [6]

### Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

No cross-repository evidence is required.

