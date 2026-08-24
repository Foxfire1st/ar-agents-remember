# mcp/src/agents_remember/testing/unsafe_effects.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/unsafe_effects.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Defines the closed effect taxonomy and exact safe/unsafe call and import vocabulary used by the
static direct-test classifier.

## Code Commentary

`UNSAFE_EFFECT_RULES` maps import prefixes to eight effect families. Allowed external imports,
safe builtins/value methods, unsafe qualified calls, and dynamic calls are explicit tables queried
by the closure analyzer. Unknown candidate dependencies refuse elsewhere; this file does not infer
purity from names.

## Invariants And Boundaries

- Rules are fail-closed policy data, not a best-effort linter list.
- No marker, directory, or historical pass result bypasses a rule.
- Expansion requires forcing proof for the new construct and all affected transitive closure.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Eight closed unsafe families are mapped to import prefixes. | `UNSAFE_EFFECT_RULES` | mcp/src/agents_remember/testing/unsafe_effects.py:19-89 |
| Dynamic and qualified calls have explicit policies. | `UNSAFE_QUALIFIED_CALLS`; `DYNAMIC_CALLS` | mcp/src/agents_remember/testing/unsafe_effects.py:251-276 |

## Update History

- 2026-08-24T20:55+02:00 — Created for 260824-PDLS.
