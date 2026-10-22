# dashboard/src/tray/TraySent.limitWord.test.tsx

## Governing Overview

[panels overview](../overview.md)

## Purpose

A tray hold for a provider limit names the time left in one compact unit; a hold for any other reason keeps the plain word.

## Code Commentary

The word says `held · rate limited: 3h`, never a clock time, and the full view adds the exact reset with date and zone. The case also holds an unparseable served string to be shown verbatim rather than repaired.

**L184 — INV-4DQMNE.** Both forms of the tray's word are asserted here, which is the place the requirement gives them different jobs. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.
