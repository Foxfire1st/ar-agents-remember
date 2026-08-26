# mcp/tests/test_task_doc_graph_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_doc_graph_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T13:43+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation was available after checking the configured source registry. | n/a | n/a |

## Repo-Internal References

The test suite and the application owner are the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite proves supported zero/one shape, pre-publication no-effect refusal, and order independence. | `TaskDocGraphPublicationTests` | mcp/tests/test_task_doc_graph_publication.py:93-160 |
| The owner under test defines the typed cardinality and in-memory title context. | `require_single_graph_document`; `build_publication_batch_graph_titles` | mcp/src/agents_remember/application/task_docs/task_doc_graph_titles.py:17-34; mcp/src/agents_remember/application/task_docs/task_doc_graph_titles.py:37-49 |

## Cross-Repo References

No cross-repository boundary is exercised by this suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository references were found. | n/a | n/a |

## Update History

- 2026-08-24T13:43+02:00 — Created for DAGQC L1: focused zero/one/two graph-publication
  cardinality and no-effect forcing. Verification remains closeout-owned because the test source
  is uncommitted.
