# mcp/tests/test_converted_onboarding_drift_leaf_route.py

## Governing Overview

[overview](overview.md)

## Purpose

The converted-drift surfaces, the leaf route and the repair cases, split from the module that keeps the drift measurement and the baseline adoption.

## Code Commentary

`test_descriptions_say_what_the_check_is` holds the `context_packet` registration and `docs/tool-details.md` to stating measurement, currentness, duty and repair, with the constants `_MEASUREMENT`, `_CURRENTNESS`, `_ADVISORY` and `_DUTY_IDENTIFIER` naming the words each must carry; the duty's identifier is required in the served description, which may show it, and not in a public page, where it would be a finding. It requires the drift section of `docs/tool-details.md` to say the read reports and never blocks while publication still refuses the anchor debt, and reads the drift, curation, stale-memory, change-routing, trace and handoff-ingestion wording from the lifecycle skill's reference, operation and template files in both shipped copies. The leaf-route cases write a fixture-owned `WorktreeContract` through `_leaf_contract`. It uses the fixture code and memory roots and their actual base commits at a canonical enclosure path inside the fixture coordination root. `test_context_packet_leaf_route_binds_the_leaf_base` compares against the leaf base rather than HEAD; the carried-anchor case requires the leaf route and the summary to agree that a carried deleted anchor is stale and to refuse it as carried-stale. Further cases cover the full drift envelope in baseline status, an onboarding root that is a file, empty and malformed sidecars, an unbuildable base that withholds its new and carried refusals, the repair cases that must restore state and keep their name, a hook that rewrites and stages layout bytes (refused, nothing committed, branch unmoved) against a passing hook whose adoption records exactly the validated tree, and unreadable history reported unavailable.

## Invariants And Boundaries

The repair cases are judged on state, not on a message: an interrupted run leaves the entry state untouched because it stages a private index. `_EMPTY_BLOB` names the empty blob the empty-sidecar cases build on. The leaf-route cases write their own contracts under the scratch coordination root.

## Evidence

### Repo-Internal References




- The leaf route compares against its fixture base when HEAD differs and shares the carried-stale disposition with the summary. [1]






- An interrupted adoption leaves the entry state untouched, and a passing hook records exactly the validated tree. [2]






- A hook that rewrites and stages layout bytes is refused with no commit and the branch where it was. [3]

- The static description case checks the scoped registration and the current drift guide words in paired in-repository sources. [4]
