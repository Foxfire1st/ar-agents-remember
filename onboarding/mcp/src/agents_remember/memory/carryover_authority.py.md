# mcp/src/agents_remember/memory/carryover_authority.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

`carryover_authority.py` proves that the target recovery-leaf memory repository contains explicit, supported,
and semantically effective onboarding storage/path-rule authority before carryover may mutate it.

## Code Commentary

### Logic

`required_target_storage()` prefers the JSON settings sibling when present and otherwise scans
Markdown. It validates the raw authority surface before accepting typed `StorageSettings`, because
the general parser's wildcard/default behavior is suitable for read/topology discovery but cannot
grant write permission. JSON preflight mirrors parser selection rules, including `onboarding:null`,
root storage fallback, `mode`/`layout`, falsey versus truthy storage selection, supported labels,
and raw path-rule members before defaults are materialized. Since 260731-EFA-L2 the list arm of
`_json_path_rule_state` is its own function, `_json_path_rule_list_state(raw_rules)`: an empty list
is `absent`, and otherwise **the weakest member decides** — `invalid` beats `empty-member` beats the
rest. Same verdicts as the inlined chain; the fold rule now has a name.

The Markdown scanner follows the parser's onboarding/storage/pathRules scopes, global and per-rule
include/exclude lists, recognized list names, repeated-key reset semantics, retained explicit paths
and storage labels, and later repopulation. `_ScopedRuleAuthority` records each contribution so a
blank/reset final state is rejected while a retained or repopulated effective contribution is
accepted. Invalid non-null structures still flow through the typed parser so error classification
does not fork into a second settings language.

### Conventions

Raw scanning answers one narrow question: whether explicit effective authority exists. The typed
parser remains responsible for constructing `StorageSettings`. JSON and Markdown raw preflights follow the same typed parser authority rules; retired full-apply
tests are historical evidence rather than current coverage.

### Invariants And Boundaries

- Missing settings, invalid shapes, unsupported storage labels, empty rule containers, blank rule
  members, and final reset-to-empty lists refuse with `AuthorityError`.
- A parser-created wildcard cannot convert an empty raw member into write authority.
- Repeated Markdown keys use final parser state: retained explicit contributions and later
  repopulation remain valid; final empty resets remain invalid.
- JSON sibling precedence and target-over-source selection are fixed authority rules.
- Validation occurs before any carryover mutation. This guard protects target-memory authority
  and parser equivalence; it is not a permissive fallback or speculative defense layer.

### Todos

None known for the MX-FIX-4 official-settings authority boundary.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. Current authority semantics are
grounded in the package settings parser, this raw preflight, and its current apply consumer.

No configured domain documentation could be checked.

### Repo-Internal References

- The internal apply owner obtains target storage authority and passes it to route-index refresh only after configured contract and protected-checkout authority. [1]
- The raw preflight exposes the required target storage authority. [2]

### Cross-Repo References

The module reads target recovery-leaf external-memory settings while running from the code package, but no
sibling repository provides implementation authority.

No meaningful cross-repo references found.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.
