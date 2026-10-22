# dashboard/src/panels/lifecycle-list/limited-expiry.test.tsx

## Governing Overview

[panels overview](../overview.md)

## Purpose

The sidebar row is one display instant: when the window ends, the word, its mark and every hover cell say paused together.

## Code Commentary

Expiry happens on the display clock with no new server snapshot, no recomputed counts and no server-side timer, so the row must not show one surface past the reset while another still counts. The case drives the clock past the served end and reads every part of the row.

**L184 — INV-XZYGEB.** The expiry transition is the row's own behaviour, and this case drives it through that row's clock. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.
