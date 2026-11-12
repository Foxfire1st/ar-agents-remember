# mcp/tests/test_citation_census_artifact.py

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

`test_citation_census_artifact.py` holds the census route to the delivery MIK-R198 rule 1 names, against carried finding `L191-PRE-03`: a valid corpus with more targets than the bound answered `targets: []`, dropped the per-sidecar totals, and offered neither a full artifact nor a continuation. The cases require the bounded answer to say how many rows it omitted and to name the exact, retrievable, complete artifact those rows are in, with the answer and the artifact reconciling.

## Code Commentary

The delivery cases stub `_memory_scope`, `is_converted_memory` and `measured_census`, so the population is synthetic and the over-bound arithmetic is exact rather than lucky; the storage cases call the real `census_artifacts.write_census_artifact`, including four-way concurrent writes through a thread pool. The artifact store is bounded and reclaims oldest first, name every retired receipt at both a below-and-above-keep population, and keeps a caller-named file alive even when a former default was promoted into that path. Identity cases measure a real Git repository: a pair is named by commit and work-tree tree, an absent memory side is `{"kind": "absent"}`, and a relative root answers exactly what the absolute root answers. The command line refuses a `--census` without a contract by name and exits 1 before `load_config` is reached.

## Evidence

- An over-bound population is written whole and the bounded answer names the omission, the artifact and its digest [1]
- Returned plus omitted rows reconcile with the artifact's denominator and route totals at every boundary [2]
- Two populations measured in one second keep two retrievable addresses instead of replacing each other [3]
- Re-measuring the same population resolves the artifact already written and stores no second file [4]
- A caller-named artifact in the store folder survives every default reclamation, and each retired receipt is named [5]
