# mcp/tests/test_converted_onboarding_drift_leaf_route.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The converted-drift surfaces, the leaf route and the repair cases (MIK-R44@v2), split from the module that keeps the drift measurement and the baseline adoption.

## Code Commentary

The c10-description checks require both shipped skill copies to contain the stale-anchor-gate wording, `R198.1-reference-anchor` and `blocked-invalid`. These are source assertions about the guidance, not a fresh test run or a bypass of paired validation.

`test_descriptions_say_what_the_check_is` holds every live surface to stating measurement, currentness, duty and repair, with the constants `_MEASUREMENT`, `_CURRENTNESS` and `_ADVISORY` naming the words each must carry. The leaf-route cases bind the leaf contract through `_leaf_contract`, a copy of the real enclosure contract with every root remapped, and `_live_code_base_commit` reads that contract's code base live so a pinned hash cannot go stale. `test_context_packet_leaf_route_binds_the_leaf_base` compares against the leaf base rather than HEAD; the carried-anchor case requires the leaf route and the summary to agree that a carried deleted anchor is stale and to refuse it as carried-stale. Further cases cover the full drift envelope in baseline status, an onboarding root that is a file, empty and malformed sidecars, an unbuildable base that withholds its new and carried refusals, the repair cases that must restore state and keep their name, a hook that rewrites and stages layout bytes (refused, nothing committed, branch unmoved) against a passing hook whose adoption records exactly the validated tree, and unreadable history reported unavailable.

## Invariants And Boundaries

The repair cases are judged on state, not on a message: an interrupted run leaves the entry state untouched because it stages a private index. `_EMPTY_BLOB` names the empty blob the empty-sidecar cases build on. No case here writes into the checkout; every contract is remapped under the scratch coordination root.

## Evidence

### Repo-Internal References




- The leaf route compares against the leaf base and agrees with the summary on a carried stale anchor. [1]






- An interrupted adoption leaves the entry state untouched, and a passing hook records exactly the validated tree. [2]






- A hook that rewrites and stages layout bytes is refused with no commit and the branch where it was. [3]
