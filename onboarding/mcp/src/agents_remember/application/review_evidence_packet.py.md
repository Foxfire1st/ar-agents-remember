# mcp/src/agents_remember/application/review_evidence_packet.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Assembles one explanation’s evidence packet from its exact recorded or planned comparison: copies the owner’s four sides and distinct owner/reference, accounts for every collection preparation did or did not build, and refuses to read a packet as evidence of another comparison.

## Code Commentary

`comparison_binding` copies the record's sides and conversion inputs and keeps the states the owner measured; it invents no side state. `build_evidence_packet` fills every collection the rule names, records the ones preparation skipped as `not-selected` or `not-read` with their reason, adds the matching omissions, and refuses a packet whose supplied populations exceed its own admitted bounds before the model can be built.
`same_comparison` and `require_same_binding` compare the packet's full identity — task, leaf, number, both repositories/trees, both commits/refs and the conversion — so code-only or memory-only movement leaves an earlier packet bound to its own trees. `retained_supplemental` returns the receipts exactly as captured, never refreshed in place.

`intended_source_root` admits requirement packets, the leaf’s exact own JSON/Markdown names and `notes/reference/<leaf>/` as intended sources, excluding the task root as a whole, another leaf and `DEVELOPER-DIRECTION.md`. `intended_receipt_ids` uses only present admitted receipts. Supplemental sources omitted at the read ceiling are explicit `truncated-read` omissions alongside omitted collections.

## Evidence

- Packet assembly copies the comparison owner's sides instead of inventing them, and fills every collection or names why it is missing. [1]
- A packet read as evidence of another comparison is refused on the owner's full identity. [2]
- Supplied populations are bounded before the packet is assembled. [3]
- A skipped collection is carried as not selected or not read, with its reason. [4]

- The current implementation adds intended source admission and receipt-bound omission accounting; no previous valid full-identity or population-bound statement is removed. [5]
