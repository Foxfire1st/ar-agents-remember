# mcp/src/agents_remember/memory/knowledge/evidence_read.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The evidence-specific selection: one seed selects one complete aggregate, served whole or refused, with
the artifact resolution reported as a read-time fact and never written back.

## Code Commentary

### Logic

The recorded-scope selection and the facet selection are unchanged by this leaf, and this module is why:
the evidence selection is a **third** selection with its own declared policy name, its own seeds and its
own item stream, reachable from neither of the others. Nothing here calls into a shipped selection and no
shipped selection calls into anything here, so a shipped seed's serialized page stays byte-identical to
what it was before this leaf because no code path is shared.

`select_evidence_scope` is the entry point. A claim seed selects that claim's envelope, every retained
revision of it, its subject edge and every claimed-coverage edge — so a caller reading a claim sees what it
asserts and what it says it covers, together. A candidate seed selects every observation whose recorded
tested candidate is the exact candidate named, each with its own retained revisions.

**Complete or refused.** The whole aggregate is selected and the whole aggregate is served. A selection
that reaches `ITEM_LIMIT` raises `EvidenceSelectionIncomplete` rather than emitting a partial page with a
total that was never computed, and the caller converts that into the shipped `selection_incomplete`
refusal. There is no cursor, so there is no continuation contract to bind and no position that could be
read as a different selection.

**Nothing is derived and nothing is judged.** An item's order is fixed by its kind and by stable
identifiers, never by an authored label, an insertion order or a timestamp. Every retained revision is
served as its own item. The execution result is served as the member that was recorded, and no field on a
page is a verdict, a grade, a score or an aggregate status: `_counts` is the selected set's own arithmetic.

`_artifact_resolution` and `_resolution` are the read-time statement about an artifact, with four
distinguishable states. A caller may declare an artifact root so a recorded repository-relative path can be
resolved against real bytes; the resolution is reported as its own state and the stored record is served
exactly as it was written, whatever the resolution says. Nothing here re-pins a digest, drops a reference,
or converts a missing artifact into a statement about the record. `_assessment_state` reports the absence
of an assessment as absence.

The two absences a caller can tell apart are the shipped ones: a seed naming nothing recorded is
`selector_absent`, while a recorded claim with an empty claimed-coverage list is impossible by construction
and a claim with an empty assessment-reference list is a real page reporting the unassessed state.

### Conventions

Selection items are built by `_claim_items` and `_observation_items` from decoded rows and the shipped
revision readers; `_one` and `_many` are the two row helpers, so a missing row is an absent selection rather
than a widened one.

### Invariants And Boundaries

- **The selection never writes.** Every query in this module is a read, and the resolution facts it computes
  are returned rather than stored.
- **A stored reference is served as written in every state.** A digest mismatch is never repaired by
  re-pinning; the record still carries the digest it was written with.
- **The whole aggregate or a typed refusal.** A partial page is not a state this selection can produce.
- **No shipped selection is touched.** The evidence selection declares its own policy name and appears in
  neither the recorded-scope nor the facet response.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The selection entry point and the seed it takes. [1]
- The claim aggregate's items, including the subject edge and every coverage edge. [2]
- The observation items a candidate seed selects, keyed by the recorded candidate rather than a re-derivation. [3]
- The four artifact-resolution states computed at read time and never written back. [4]
- The unassessed state reported as the absence of an assessment rather than a defaulted value. [5]
- The bound whose breach raises rather than serving a partial page, and the exception the caller converts into a shipped refusal. [6]
- The counts, which are the selected set's own arithmetic and nothing more. [7]
- The case that asserts an artifact absent at write time is recorded rather than refused. [8]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
