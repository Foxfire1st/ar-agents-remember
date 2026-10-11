# mcp/src/agents_remember/application/review_recorded_relationships.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The relationships one snapshot's union items record, read from that snapshot.** The traversal reads the union both snapshots record, so its inputs are two facts per side and this module owns both: the shipped comparison's own union items (each carrying the side payloads that selected it) and the identity each association revision belongs to — read from the snapshot's own revision rows. Authored predecessor edges and the authored-line reach are deleted with the tables they read (MIK-R74 rule 1).

## Code Commentary

`recorded_snapshot` holds one snapshot's file and connection beside its side name. `read_snapshot_relationships` reads every relationship the union items record, in the union's own order, through the three relationship kinds (`realization`, `membership`, `advertised_family link`) with the identity index resolved first. A relationship is read exactly as the two records state it: a claim whose anchor row could not be read keeps that fact, a membership carries its member revision as well as its family revision, and a revision item is reported as no relationship rather than an empty one. `recorded_change_state` carries the comparison's own statement verbatim. Nothing here selects, pairs or concludes.

## Evidence

- The module owns the union items and the per-snapshot identity index \[14] [14]
- One snapshot as the traversal reads it \[15] [15]
- Three relationship kinds with the identity each sits under \[16] [16]
- One union item's payload for one side \[17] [17]
- The comparison's own change statement, carried verbatim \[18] [18]
