# mcp/tests/test_validator_link_targets.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Describes anchor and record-link validation across ordinary comparisons, sync merges and leaf publication.

## Code Commentary

Existing anchor cases preserve absent-path, reanchoring, locator/content format and unconverted-base behavior. The record-link cases exercise both file anchors and route targets: an exactly carried target can report at a sync merge, but a new target, single-base commit or leaf publication refuses. Supplying repaired code removes that link-target finding; standalone conversion explicitly lacks paired path checks.

## Invariants And Boundaries

Reporting at a multi-parent sync is not a landing waiver. Assertions retain separate refusing/report-only populations and do not imply every route was run in this curation pass.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- Describes anchor and record-link validation across ordinary comparisons, sync merges and leaf publication. Reporting at a multi-parent sync is not a landing waiver. Assertions retain separate refusing/report-only populations and do not imply every route was run in this curation pass. [1]
