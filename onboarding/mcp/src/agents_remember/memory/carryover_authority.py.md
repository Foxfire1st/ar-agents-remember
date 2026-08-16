# mcp/src/agents_remember/memory/carryover_authority.py

| Field                  | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| repository             | agents-remember                                                  |
| path                   | `mcp/src/agents_remember/memory/carryover_authority.py`           |
| doc_type               | `file-level-onboarding`                                          |
| lastUpdated            | 2026-07-31T00:00+02:00                                           |
| lastVerifiedCommitHash |                                                                  `8bf6edad7e7e65e27cf735be0822f604531d0c8a`|
| lastVerifiedCommitDate |                                                                  2026-08-16T10:54:02+02:00|
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
| The internal apply owner obtains target storage authority and passes it to route-index refresh only after configured contract and protected-checkout authority. | `_apply_carryover_for_request`, `_refresh_target_route_indexes` | mcp/src/agents_remember/memory/carryover.py:636-670; mcp/src/agents_remember/memory/carryover.py:759-852 |
| The raw preflight exposes the required target storage authority. | `required_target_storage` | mcp/src/agents_remember/memory/carryover_authority.py:32-66 |
| Full-apply JSON/Markdown tests cover missing, invalid, empty/reset, unsupported, retained, repopulated, fallback, and target-over-source cases. | `test_missing_official_settings_refuses_before_any_mutation`; `test_semantically_empty_json_authority_refuses_before_any_mutation`; `test_markdown_reset_lists_remove_final_rule_contribution_before_mutation`; `test_markdown_parser_retained_and_repopulated_contributions_remain_authoritative`; `test_unsupported_json_storage_labels_refuse_before_any_mutation`; `test_unsupported_markdown_storage_labels_refuse_before_any_mutation`; `test_target_settings_override_conflicting_source_settings` | mcp/tests/test_carryover_apply_1.py:98-175; mcp/tests/test_carryover_apply_2.py:88-179; mcp/tests/test_carryover_apply_2.py:216-332; mcp/tests/test_carryover_apply_2.py:496-535; mcp/tests/test_carryover_apply_2.py:569-630 |

## Cross-Repo References

The module reads official external-memory settings while running from the code package, but no
sibling repository provides implementation authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## Update History

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-04T14:17+02:00 — 260731-EFA-L6 S18-B13 curator: closed D10 caller/call/storage dataflow evidence for the same-reviewer residual delta.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0911` armed with no exemptions):
  extracted `_json_path_rule_list_state` from `_json_path_rule_state`'s list branch. No verdict
  changed. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: created the one-to-one sidecar for fail-closed official
  JSON/Markdown carryover authority, typed-parser equivalence, and pre-mutation refusal semantics.
