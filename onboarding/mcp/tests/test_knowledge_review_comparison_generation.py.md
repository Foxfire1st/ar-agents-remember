# mcp/tests/test_knowledge_review_comparison_generation.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose
Checks reopening historical comparison source records without reading their retired canonical datasets.

## Code Commentary
The fixture assembles a legacy manifest with exact source identities. One case preserves those source objects and patches dataset access to ensure it is never used; another refuses a tampered historical source record rather than retargeting it. The former live freeze/restart/custody scenario suite is removed. These two retained cases are source assertions, not a newly frozen generation or proof of current retention.

## Evidence

### Repo-Internal References



### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Cross-Repo References

No cross-repository behavior is measured in this file. It creates a local repository, an enclosure and a
task-artifact root under `tmp_path` for each case.

No meaningful cross-repo references found.

- `test_a_legacy_record_preserves_exact_source_and_never_reads_its_dataset` owns the current boundary described above. [25]
- `test_a_tampered_historical_source_record_is_refused_instead_of_retargeted` owns the current boundary described above. [26]
> Retained earlier citation wording: - The lane row this module was registered under, inside the array whose own key declares the classification.  Anchor: `test_knowledge_review_comparison_generation` [27]

- The lane row this module was registered under, inside the array whose own key declares the classification.  Anchor: `test_knowledge_review_comparison_generation` [27]
