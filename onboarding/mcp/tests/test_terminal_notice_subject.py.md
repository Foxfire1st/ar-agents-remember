# mcp/tests/test_terminal_notice_subject.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pins canonical subjects for terminal notices: leaf enclosures and direct leaf generations name the leaf's own document, while an ordinary series contract names its own master document. An unresolved leaf never borrows that master.

## Code Commentary

The ordinary cases use real authored master and leaf documents with their enclosure bindings: two sibling leaves
publish their own task documents, a leaf's subject comes from its own declared binding, a series contract still
names its master document because that is its own task, and an unresolvable leaf never falls back to the master —
it produces no notice at all.

The direct-landing cases pin the requested leaf rather than the series master, carry the exact generation
identity (commit, `:g3`, repository and root), and write no notice for an unnameable leaf. The retry and cleanup
cases show an exact retry keeping only its own identity while a sibling differs, and occurrences surviving an
enclosure's cleanup unchanged.

## Evidence boundary

Source-level pytest cases at the reviewed freeze over authored file-backed contracts, driving the production record
and finish paths with supplied synthetic commit and journal identities: not actual Git landings, not an OS kill, and
not a live-page witness
and no measurement: MIK-R200 evidence item 6 is unrun and carried to L36, item 7 unrun.
