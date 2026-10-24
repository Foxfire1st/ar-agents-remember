# mcp/tests/landing_report_test_support.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Holds the constants, scratch leaf pairs, landing fixtures and loadable contracts of the landing-report cases (MIK-R120@v1), so the report module and the closeout population module judge the same artifact.

## Code Commentary

The module pins `LAYOUT_MARKER` for converted memory and a `SIDECAR` template, plus the curator and Reviewer sentences with the curator sentence's written equivalent. `_leaf_pair` opens a memory and code git repository at one base; `_rename_pair` adds a rename with an edit; `_operation_pair` adds or withholds one cut card and one added file; `_operation_contract` and `_paired_gate_contract` build minimal loadable leaf contracts binding those bases; `_clean_pair` and `_gate_trees` give a validator-clean pair; `_land` performs the cut and the addition without committing; `_checklist`, `_report`, `_landing_counts`, `_reviewer_landing_roots` and `_operation_context` read the populations back; `_commit_all` commits a fixture. `_curator_landing_missing` is the missing-evidence probe.

## Invariants And Boundaries

The landing is left uncommitted on purpose, so the consumers are shown a working-tree population. The forbidden reviewer-sentence probes are harmless text in the fixture, not assertions about the product.

## Evidence

### Repo-Internal References

- A leaf pair is two git repositories at one base, and the landing cuts one card and adds one file without committing. [1]

- The loadable leaf contracts bind the fixture bases so the real gate and closeout phases can run on scratch trees. [2]
