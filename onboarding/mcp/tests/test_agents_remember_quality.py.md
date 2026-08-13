# mcp/tests/test_agents_remember_quality.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_agents_remember_quality.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-13T14:32+02:00 |
| lastVerifiedCommitHash |  `b2de030c1b52f02a4543619d23ccd8e44ecac6df`|
| lastVerifiedCommitDate |  2026-08-13T14:51:34+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite proves the Dagger module itself is pinned, parseable, fail-closed, and builds the intended clean quality graph before live Docker execution is considered trustworthy.

## Code Commentary

### Logic

In-process fake Dagger objects record container graph construction. The tests cover pinned
manifest/image inputs, targeted and full argument selection, real/fake Codex probe wiring,
export-before-verdict behavior, invalid public inputs, and green/red verification. The public
`quality` and `verify` functions must receive a nonblank explicit diff base, always forward it to
the wrapper, and publish `Annotated`/`Doc` help for source, bundle, base, mode, and cap.

### Conventions

The suite tests graph semantics without a daemon; live field proof remains a separate Dagger run.

### Invariants And Boundaries

- Unit doubles may replace Dagger transport but not command/graph selection.
- Reports must export at the exact completed boundary even for a red run.
- Invalid mode, omitted/blank diff base, or memory inputs refuse.
- Generated Dagger help is tested as part of the public quality-function contract.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this test contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The test contract is defined by the pinned repository module. | `DAGGER_MANIFEST`; `DAGGER_MODULE` | mcp/tests/test_agents_remember_quality.py:14-17 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Tests cover pinning, refusal, graph construction, export ordering, and verdicts. | `test_agents_remember_quality_module_is_pinned_and_parseable`; `test_dagger_verify_returns_green_and_refuses_red_quality_results` | mcp/tests/test_agents_remember_quality.py:82-216 |

## Cross-Repo References

No sibling-repository boundary is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fake Dagger objects isolate graph verification from external transport. | `FakeContainer`; `FakeDag` | mcp/tests/test_agents_remember_quality.py:29-80 |

## Update History

- 2026-08-13T14:32+02:00 — L23 final curator pass: recorded the required explicit diff base and
  generated argument-help contract for both Dagger functions. Focused clean proof covered all 26
  tests with 20 workers; Ruff, formatting, layering, Pyright, CRAP, and all 7 changed coverage lines
  passed. Final commit provenance remains closeout-owned.
- 2026-08-12T15:19+02:00 — Created with L23's Dagger graph contract tests; verification provenance remains closeout-owned.
