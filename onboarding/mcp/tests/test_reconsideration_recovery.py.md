# mcp/tests/test_reconsideration_recovery.py

## Governing Overview

[tests route overview](overview.md)

## Current source account — recovered refusals and the D430 sequence

The file reuses the surfacing fixture (`pytest_plugins = ("test_reconsideration_surfacing",)`) and its re-point rows, so each case runs over real Git code and converted memory. The D430 case removes the symbol a `reconsider_on` link names, computes the worklist, and finds the item as a `reconsideration_candidate` that `reconsideration_item_open` reports open. An empty hand-off is written without refusal and changes neither the decision's links nor its bytes, and the item stays open; a Curator-authored `still_rejected` carrying `items` and a `repoint` is written, and the gate's own predicate then finds the item answered by that stored row.

The other cases follow a refusal's advice rather than asserting the refusal alone. Restoring the base target in `records` byte for byte, after the refusal asked for exactly that or a raise, admits the same row. Where the fired target still maps, dropping the `repoint` lets the row stand on its refresh and be written. The refresh refusal names both the recompute and the raise, and leaves the decision bytes unchanged. A row with empty prose goes through the writer, and the gate still reports that no satisfying row or change answers the item, with the decision and history files untouched.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence


- A removed symbol opens the item, an empty hand-off answers nothing, and a judged row with `repoint` closes it [1]

- The re-authored refusal's advice — restoring the base target byte for byte — admits the row it refused [2]
