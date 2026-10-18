# mcp/tests/test_writer_correction_history.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Describes paired-tree regression assertions for writer history eligibility, stable refusals and rule15 relocation.

## Code Commentary

A synthetic extended row adds one entry and relocates two carried entries while preserving invariant bytes, old IDs/origins and authored fields; before/after covers and persisted-request rerun bytes are asserted. The same no_impact request retains its exact refusal and no-write boundary. Other cases protect closed changed rows against hiding/reordered items, malformed persisted worklists, family guarantee changes, own-record aliases, and itemless planned/hunk rows, with explicit mutation checks.

### Existing-row recovery and new-row refusal

The added paired-Git case first authors an invariant and its own row through the native writer, records that row in the fixture base, then changes the code and uses a different leaf's native empty operation to carry the moved anchor. The original history remains byte-exact and the actual R09 mismatch is observed. A freshly computed worklist lacks the invariant and membership subject. The original owner then renews the row with the same ID and exact current `CodeSnapshot.resolve` after-cover; R09 clears and an identical rerun preserves all written bytes. This is a synthetic native-writer regression, not a live-leaf apply.

The literal/handoff/bare-alias fresh-row control now first creates only a foreign owner's history row about the same record. Its own history still does not exist. With or without repeating the entry request, each itemless new own-leaf row refuses and preserves all memory bytes; a real recomputed membership item admits the separate positive control. Malformed-worklist, governing changed-row and relocation assertions remain distinct. No fresh execution or expansion of inherited L63 copy custody is claimed here. Malformed-history non-admission is a separately inspected production boundary, not a native malformed-history execution claim from these cases.

## Invariants And Boundaries

Rule15 source tests describe the repaired candidate, not permission to use it for this leaf’s own memory. The thirteen deferred copy pairs remain under L63 custody; test declarations and existing historical passes are not new execution evidence.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- A pre-existing own-leaf row renews a genuinely moved anchor without a worklist subject, retaining its ID, exact current after-cover and byte-idempotent rerun. [2]


- A foreign history row does not authorize a new own-leaf row through literal, handoff or bare aliases; refused requests preserve bytes and genuine recomputed membership admits the positive control. [3]


- Retained paired-Git regression declarations cover relocation, stable no-write refusals and genuine own-row recovery; source declarations do not authorize using leaf code as the live leaf producer. [1]
