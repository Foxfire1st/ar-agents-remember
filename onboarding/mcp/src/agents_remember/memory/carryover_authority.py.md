# mcp/src/agents_remember/memory/carryover_authority.py

| Field                  | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| repository             | agents-remember                                                  |
| path                   | `mcp/src/agents_remember/memory/carryover_authority.py`           |
| doc_type               | `file-level-onboarding`                                          |
| lastUpdated            | 2026-07-31T00:00+02:00                                           |
| lastVerifiedCommitHash |                                                                  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |                                                                  2026-07-31T19:28:50+02:00|
| governingOverview      | `../../../overview.md`                                           |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

`carryover_authority.py` proves that the official memory repository contains explicit, supported,
and semantically effective onboarding storage/path-rule authority before carryover may mutate it.

## Code Commentary

### Logic

`required_official_storage()` prefers the JSON settings sibling when present and otherwise scans
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
parser remains responsible for constructing `StorageSettings`. JSON and Markdown paths are kept
behaviorally equivalent through paired full-apply tests and parser comparisons.

### Invariants And Boundaries

- Missing settings, invalid shapes, unsupported storage labels, empty rule containers, blank rule
  members, and final reset-to-empty lists refuse with `AuthorityError`.
- A parser-created wildcard cannot convert an empty raw member into write authority.
- Repeated Markdown keys use final parser state: retained explicit contributions and later
  repopulation remain valid; final empty resets remain invalid.
- JSON sibling precedence and official-over-source selection are fixed authority rules.
- Validation occurs before any carryover mutation. This guard protects official-memory authority
  and parser equivalence; it is not a permissive fallback or speculative defense layer.

### Todos

None known for the MX-FIX-4 official-settings authority boundary.

## Docs References

No Domain Documentation source is configured for this repository. Current authority semantics are
grounded in the package settings parser, this raw preflight, and paired tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `apply_carryover_for_request` obtains `official_storage` from `required_official_storage` and passes it to `_refresh_official_route_indexes` after carried onboarding. | "official_storage = required_official_storage(official_memory)"; "if carried:"; "route_index_refresh = _refresh_official_route_indexes"; "official_storage," | mcp/src/agents_remember/memory/carryover.py:790-790; mcp/src/agents_remember/memory/carryover.py:825-826; mcp/src/agents_remember/memory/carryover.py:829-829 |
| The raw preflight exposes the required official storage authority. | `required_official_storage` | mcp/src/agents_remember/memory/carryover_authority.py:32-66 |
| Full-apply JSON/Markdown tests cover the missing, invalid, empty/reset, unsupported, retained, repopulated, fallback, and official-over-source cases. | `test_missing_official_settings_refuses_before_any_mutation`; `test_semantically_empty_json_authority_refuses_before_any_mutation`; `test_markdown_reset_lists_remove_final_rule_contribution_before_mutation`; `test_markdown_parser_retained_and_repopulated_contributions_remain_authoritative`; `test_unsupported_json_storage_labels_refuse_before_any_mutation`; `test_unsupported_markdown_storage_labels_refuse_before_any_mutation`; `test_official_settings_override_conflicting_source_settings` | mcp/tests/test_carryover.py:374-387; mcp/tests/test_carryover.py:424-450; mcp/tests/test_carryover.py:692-783; mcp/tests/test_carryover.py:820-936; mcp/tests/test_carryover.py:1100-1139; mcp/tests/test_carryover.py:1173-1207; mcp/tests/test_carryover.py:1209-1234 |

## Cross-Repo References

The module reads official external-memory settings while running from the code package, but no
sibling repository provides implementation authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-04T14:17+02:00 — 260731-EFA-L6 S18-B13 curator: closed D10 caller/call/storage dataflow evidence for the same-reviewer residual delta.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0911` armed with no exemptions):
  extracted `_json_path_rule_list_state` from `_json_path_rule_state`'s list branch. No verdict
  changed. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: created the one-to-one sidecar for fail-closed official
  JSON/Markdown carryover authority, typed-parser equivalence, and pre-mutation refusal semantics.
