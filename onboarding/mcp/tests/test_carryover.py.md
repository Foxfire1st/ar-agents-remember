# mcp/tests/test_carryover.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_carryover.py`              |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-18T20:03+02:00                     |
| lastVerifiedCommitHash | `7ca29c3b6dd2c0184253e2690f1ebe78c511573b` |
| lastVerifiedCommitDate | 2026-07-18T20:18:51+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

`test_carryover.py` validates branch-memory carryover planning/apply, with MX-FIX-4 focused on
fail-closed official-memory JSON/Markdown write authority and exact zero mutation on refusal.

## Code Commentary

### Logic

The existing real-repository fixtures cover sidecar, route-overview, memory-only-doc, and entity-
catalog candidates; evidence tiers; guarded official route-index regeneration; ledger mapping; and
ff-only memory-main advancement. MX-FIX-4 extends full apply with snapshots of official HEAD, Git
status, every non-Git byte, source bytes, and route-index presence.

Refusal cases include missing/invalid/unrelated settings, `onboarding:null`, invalid non-null
shapes, semantically empty rule containers and members, blank Markdown, final empty/reset lists,
unsupported recognized lists, unsupported storage labels, and truthy invalid fallback. Positive
controls cover root storage fallback, mode/layout selection, falsey fallback, valid global/scoped
rules, retained contributions across repeated keys, later repopulation, supported list names, and
official-over-source authority. Each case compares raw preflight outcome with the typed settings
parser, then runs production `apply_carryover_for_request()`.

### Conventions

Helpers create real code and memory Git repositories and drive the service API, not CLI adapters.
Refusal tests assert the whole observable mutation surface rather than only the raised exception.
JSON and Markdown cases are paired where their parser semantics correspond.

### Invariants And Boundaries

- Parser defaults cannot grant official-memory write authority when raw rules are empty.
- Missing, invalid, unsupported, or final-reset-to-empty authority refuses before all mutation.
- Retained explicit contributions and later repopulation remain valid exactly when the typed parser
  retains them.
- JSON sibling precedence, root fallback, mode/layout selection, and official-over-source settings
  are fixed and independently tested.
- Every refusal preserves official HEAD/status/non-Git bytes, source bytes, ledger, and route-index
  absence; successful apply reuses the validated storage authority for index refresh.

### Todos

Refresh verification metadata only after closeout commits the candidate.

## Docs References

No Domain Documentation source is configured for this repository. The full-apply fixtures and local
typed parser are the authority evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Carryover invokes official settings authority before any content/ledger/index/commit mutation. | apply path | [carryover.py](agents-remember/mcp/src/agents_remember/memory/carryover.py) |
| Raw JSON/Markdown preflight mirrors typed parser semantics while rejecting default-only write authority. | L1-L415 | [carryover_authority.py](agents-remember/mcp/src/agents_remember/memory/carryover_authority.py) |
| Authority matrix spans missing/invalid/empty/reset/unsupported refusals and retention/repopulation/fallback positive controls. | L374-L1268 | [test_carryover.py](agents-remember/mcp/tests/test_carryover.py) |
| Earlier evidence-tier and ledger-mapping coverage remains in worktree tests. | carryover tests | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

Fixtures model separate code and external-memory repositories locally; no sibling repository is a
test dependency.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: added full-apply JSON/Markdown official-settings
  authority matrices, typed-parser equivalence controls, retained/repopulated rule semantics,
  unsupported cases, selector isolation, and exact zero-mutation refusal proof.
- 2026-06-11T15:05+02:00 — Added entity-catalog and memory-only-doc candidate/evidence coverage.
- 2026-06-10T09:45+02:00 — Issue #54 sub-task C added memory-main advancement coverage.
- 2026-06-10T05:50+02:00 — Created for route-overview carryover candidates and guarded index
  regeneration (issue #56 sub-task 3).
