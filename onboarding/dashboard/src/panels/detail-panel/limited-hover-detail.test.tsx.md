# dashboard/src/panels/detail-panel/limited-hover-detail.test.tsx

## Governing Overview

[panels overview](../overview.md)

## Purpose

The three clockless surfaces covered here — the order graph, the sprint graph and the constellation — show no countdown and owe the served fact in full detail. Places that carry a display clock do count down, and that is a different surface's account, not a denial here.

## Code Commentary

The order graph, the sprint graph and the constellation each carry the whole detail of every limited seat — its provider account, its exhausted window and that window's own reset — where a place has no display clock to count down. The compact countdown and expiry assertions belong to the page-clock and lifecycle cases; this file exercises only the clockless surfaces, and its commentary claims nothing about the clocked ones.

**INV-7GVWYD.** The hover is the place the full detail is shown, so the case that asserts its contents belongs beside it.
