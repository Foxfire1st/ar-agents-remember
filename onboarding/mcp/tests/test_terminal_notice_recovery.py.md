# mcp/tests/test_terminal_notice_recovery.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pins that an interrupted terminal notice is settled only by its own route's native record, across the four
recovery situations the design admits.

## Code Commentary

The ordinary landing matrix covers a crash after the landing cell publishes, an exact retry, a different landed
commit that refutes the intent, a live enclosure that has not landed and stays undecided, an unrelated
coordination root, an enclosure of another repository that refutes it, and an unreadable contract that settles
nothing.

The direct-landing matrix is the largest because the journal decides alone: a completed generation publishes its
own occurrence, an in-flight one is undecided rather than refuted, a cancelled or sibling generation refutes,
and a completed cell on the same enclosure neither overrides a cancelled journal nor an undecided one nor proves
a direct generation by itself. A row written before generations still settles by its operation, and an intent
naming another root or repository is refuted rather than published.

The abandonment matrix shows a rollbackable abandon cell staying undecided and keeping its intent, a rollback
that discards the publication leaving no notice standing, and an authored abandoned task counting as no proof.
The after-cleanup matrix shows a recorded landing or abandonment still publishing after the enclosure was
collected, a landing that was never recorded refuting, and an intent whose subject disappears staying undecided.

## Evidence boundary

Source-level pytest cases at the reviewed freeze with real contracts, journals, crash helpers and a real settle
pass, not a live-page witness and no measurement: MIK-R200 evidence item 6 is unrun and carried to L36, item 7
unrun.
