# mcp/src/agents_remember/application/review_evidence_adapter.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The prepared-evidence seam: takes the landed comparison owner's opened trees with their measured side/index states, reads the landed schemas at that exact tree, and produces the packet plus exact addresses its consumers can open.

## Code Commentary

`prepare_evidence` consumes the comparison owner's measured states rather than caller-supplied completeness, so a partial index stays partial and a lost history keeps its owner's reason. It builds the source, family, judgment, proof and sidecar collections at the memory candidate, records limitations beside the packet, and prepares addresses in the landed owners' own identifiers.
`consume_address` resolves one prepared address only for the comparison that prepared it; `_carried` checks the owner path, side, revision, row/attempt/proof identity together, so an address pointing at another owner or comparison is unresolved rather than merely missing.

On a planned comparison, `require_intended_authority` refuses `recorded-fact` or `mechanical-signal` when every present claim basis is an admitted receipt of the leaf’s packet, own task document or reference folder. Such a claim is accepted as `intended`; a claim also grounded in present code or memory at the tip keeps its actual authority. Preparation carries the bound owner/reference and supplemental receipts. A truly absent measured code-side input or an exceeded packet scope is a named `evidence-source-unavailable` precondition, while measured unavailable history stays a stated loss.

## Evidence

- Preparation preserves the comparison owner's measured index and side states. 
- An address resolves only inside the comparison and owner path that prepared it. 
- A carried item is matched on its whole identity, not on a single field. 

- The current implementation adds the binding-aware intended-claim rule and typed preparation preconditions; the existing comparison-address and measured-state account remains valid. [4]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/review_evidence_adapter.py::prepare_evidence - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/application/review_evidence_adapter.py::consume_address - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/application/review_evidence_adapter.py::_carried - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
