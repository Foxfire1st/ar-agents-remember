# mcp/src/agents_remember/models/knowledge/review_evidence.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The evidence packet's shapes for one bound review comparison: its binding, the collections preparation supplies, its finite limits, supplemental byte receipts, claims with their typed bases, and the evidence map that scopes them.

## Code Commentary

`EvidenceComparisonBinding` carries the comparison owner's own identity — repository, task, leaf, number and reference, both code sides and both memory sides with their measured states, the conversion inputs, and the stored and compared memory-base trees stated apart. It refuses a binding whose compared tree is not the converted tree when a conversion applied.
`EvidenceCollection` names one collection's producer, population and read state: `present` states a positive count, `measured-empty` exactly zero, and any other state may not state a positive count — this validator rejects a positive count there, while a zero is tolerated but measures nothing — so a measured zero is never confused with `absent`, `not-read` or `not-selected`. `EvidencePacket` holds every collection the rule names and refuses a claim that duplicates another's local id.
`EvidenceClaim` and `ClaimBasis` keep the classifications apart: an `intended` claim needs at least one inspected supplemental receipt; code or another basis alone cannot establish what a task is meant to produce. The receipt basis names the same receipt in `reference` and `receipt_id`. For the other classifications, a recorded fact, mechanical signal or authored judgment needs an inspected (`present`) basis, a presenter inference names its author and inputs, and an unresolved question or unavailable evidence states its limit. `EvidenceMap`, `EvidenceOmission` and `CoverageCount` carry scope, omissions and counts with their own denominator, filters and limits; a passed count that plus unassessed exceeds the population is refused.
`EvidencePacket` also rejects duplicate receipt ids or canonical sources, a claim citing an unknown receipt, and a basis state that contradicts whether its receipt contains present examined bytes.
`EvidenceLimits` requires a measurement to turn a declared number into a measured tradeoff, `SupplementalReceipt` binds examined bytes rather than truth or currentness, and `packet_errors` lists what the packet still owes a reader without inventing a value.

## Evidence

- The packet is bound to one existing comparison's full identity, with the stored and compared memory-base trees named separately. [1]
- A collection states its producer, population and read state: `present` carries a positive count, `measured-empty` exactly zero, and no other state a positive count. [2]
- Claim classifications differ in what they require of a basis, and a claim map refuses a duplicate local identity. 
- Coverage counts carry their denominator, and an unassessed remainder cannot be counted as passed. 
- The packet reports what it still owes a reader instead of filling it with a default. 

- An intended claim needs an inspected supplemental receipt whose reference and receipt_id agree. Packet validation rejects duplicate receipt ids or canonical sources, unknown receipt citations and basis states that contradict the examined receipt. 


- An intended claim needs an inspected supplemental receipt whose reference and receipt_id agree. Packet validation rejects duplicate receipt ids or canonical sources, unknown receipt citations and basis states that contradict the examined receipt. [6]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/models/knowledge/review_evidence.py::EvidenceClaim - the bytes it recorded now occur 6 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/models/knowledge/review_evidence.py::CoverageCount - the bytes it recorded now occur 4 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/models/knowledge/review_evidence.py::packet_errors - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/models/knowledge/review_evidence.py::ClaimBasis - the bytes it recorded now occur 5 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
