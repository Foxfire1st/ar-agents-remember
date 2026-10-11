# Held-queue recovery and bounded-work proofs

[Tests route overview](overview.md)

## Contract

Fault injection covers admission before receipt counting (including a stale zero count), ended text deletion before terminal receipt publication, immutable batch/part recovery, and sender withdrawal racing a live delivery claim. End records are sender-isolated even when a recipient is archived. Waiting text belongs to the workspace and ends when that folder is reclaimed.

The partition tests distinguish accepted-size lower bounds from refused-size upper bounds: equal and variable-length FIFO messages yield minimum admitted partitions under the fixture’s monotone size limit; an exactly admitted batch is one delivery. Crash/replay exactly-once claims use an explicitly deduping fake host keyed by the durable message ID. They are not a real-host deduplication witness.

Bound tests separately count receipt reads and enumerated names across empty, small and large fleets, multiple zero-input cycles, dead recipients and history. The idle-fleet test observes zero `rglob` yields and a per-tick read cap; it does not claim that every enumeration mechanism produces zero names. The native scanner has its own bounded rotating census.

## Evidence

- A stale receipt zero does not lose durable admitted text after restart. [1]
- A terminal end survives the deletion-to-publication crash boundary. [2]
- Replayed split work retains its part ID on a deduping host. [3]
- A larger admissible remainder is not chopped by a smaller earlier accepted size. [4]
- Fleet-scale idle ticks cap reads and observe enumeration independently of read counts. [5]
