# mcp/tests/test_task_doc_graph_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_doc_graph_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T13:43+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Force the current zero/one graph-bearing publication-batch contract and prove that unsupported
two-graph input refuses before task bytes, the supplied publisher, or projection publication can
change.

## Code Commentary

### Logic

`TaskDocGraphPublicationTests` builds graph-bearing task documents with real edges and colliding
local leaf numbers. It accepts plain/one-graph batches, checks the qualified title result, then
forces both input orders through the central owner and ordinary task publication. Sentinel JSON and
Markdown bytes remain identical; the injected publisher and `publish_task_fact_mutation` are not
called.

### Conventions

The suite targets the compact application owner directly and crosses the ordinary publication seam
only for the validate-before-mutate proof.

### Invariants And Boundaries

- Two or more graph documents always produce the same typed cardinality refusal regardless of
  input order.
- The fixture uses real edges; it does not add an unrelated zero-edge proof obligation.
- The tests do not establish multi-graph compatibility or split-retry behavior.

### Todos

None.

## Docs References

No Domain Documentation sources are configured for this repository-internal forcing suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation was available after checking the configured source registry. | _None._ | _No external source._ |

## Repo-Internal References

The test suite and the application owner are the direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The suite proves supported zero/one shape, pre-publication no-effect refusal, and order independence. | L93-L160 | [test_task_doc_graph_publication.py](mcp/tests/test_task_doc_graph_publication.py) |
| The owner under test defines the typed cardinality and in-memory title context. | L17-L51 | [task_doc_graph_titles.py](mcp/src/agents_remember/application/task_docs/task_doc_graph_titles.py) |

## Cross-Repo References

No cross-repository boundary is exercised by this suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repository references were found. | _None._ | _No cross-repository source._ |

## Update History

- 2026-08-24T13:43+02:00 — Created for DAGQC L1: focused zero/one/two graph-publication
  cardinality and no-effect forcing. Verification remains closeout-owned because the test source
  is uncommitted.
