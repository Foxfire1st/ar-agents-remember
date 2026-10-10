# mcp/tests/test-evidence-lanes.toml

## Governing Overview

[tests route overview](overview.md)

## Purpose

The canonical evidence-lane catalog: which test modules belong to which lane, so a leaf's checks can name the population they ran. Membership declares the selected population, never that an invocation ran or passed.

## Code Commentary

The catalog assigns each current test module exactly one evidence lane, one module path per row, kept sorted within the lane. This leaf adds three `unit-regression` rows: the extracted capsule serving-surface suite and the two memory-opt-out refusal suites (start and routes). The file now holds 474 lines with 456 module rows, 315 of them in `unit-regression`; earlier shape counts recorded against smaller trees are superseded by the tree itself.

## Evidence

- Extracted capsule surface suite in unit-regression [835]
- Opt-out refusal suites in unit-regression [836]
- Lane lists with one row per module [837]
