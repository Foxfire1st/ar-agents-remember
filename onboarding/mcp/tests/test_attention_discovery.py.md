# mcp/tests/test_attention_discovery.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pins the per-refresh enumeration allowances and the warm-resume behaviour that keeps a held-message discovery
bounded without losing the population it has not reached yet.

## Code Commentary

Each case runs a real coordination root with real receipt trees and activation records under a patched budget and
a `scandir` spy, and expands over two input sizes so a bound is shown to hold rather than merely to exist.

The pause and held-folder cases show heartbeats finishing a population at forty and at ninety entries within
seven looks per read and at eighty under one shared allowance of 256, and finishing an unchanged folder walk
with noise entries. The shedding cases show a deep receipt branch abandoned past the walk depth rather than
retained without limit, an unreadable receipt keeping later chunks incomplete, and receipt-root cursors capped
and shed at both sizes.

The crowded-directory cases pin the per-call budget: a population is walked within one budget per call,
resuming where it stopped, and an incomplete walk keeps the listing it last published rather than an empty one.

## Evidence boundary

Source-level pytest cases at the reviewed freeze — real roots, activation records, a patched budget and a
scandir spy — not a live-page witness and no measurement: MIK-R200 evidence item 6 is unrun and carried to L36,
item 7 unrun.
