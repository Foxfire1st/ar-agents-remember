# mcp/src/agents_remember/memory/carryover_authority.py

| Field                  | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| repository             | agents-remember                                                  |
| path                   | `mcp/src/agents_remember/memory/carryover_authority.py`           |
| doc_type               | `file-level-onboarding`                                          |
| lastUpdated            | 2026-07-18T20:03+02:00                                           |
| lastVerifiedCommitHash |                                                                  `7ca29c3b6dd2c0184253e2690f1ebe78c511573b`|
| lastVerifiedCommitDate |                                                                  2026-07-18T20:18:51+02:00|
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
and raw path-rule members before defaults are materialized.

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Carryover invokes this preflight once after cleanliness proof and reuses the returned storage settings for route-index refresh. | apply path | [carryover.py](agents-remember/mcp/src/agents_remember/memory/carryover.py) |
| The coordination settings parser remains the typed semantic authority that the raw preflight mirrors. | parser API | [settings.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/settings.py) |
| Full-apply JSON/Markdown tests cover missing, invalid, empty/reset, unsupported, retained, repopulated, fallback, and official-over-source cases. | L374-L1268 | [test_carryover.py](agents-remember/mcp/tests/test_carryover.py) |

## Cross-Repo References

The module reads official external-memory settings while running from the code package, but no
sibling repository provides implementation authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: created the one-to-one sidecar for fail-closed official
  JSON/Markdown carryover authority, typed-parser equivalence, and pre-mutation refusal semantics.
