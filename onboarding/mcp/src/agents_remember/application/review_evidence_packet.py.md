# mcp/src/agents_remember/application/review_evidence_packet.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Assembles one explanation’s evidence packet from its exact recorded or planned comparison: copies the owner’s four sides and distinct owner/reference, accounts for every collection preparation did or did not build, and refuses to read a packet as evidence of another comparison.

## Code Commentary

`comparison_binding` copies the record's sides and conversion inputs and keeps the states the owner measured; it invents no side state. `build_evidence_packet` carries supplied populations in full and records skipped collections as `not-selected` or `not-read` with their reason. A supplied collection with fewer records than its declared count must name the bound responsible for the omission.
`same_comparison` and `require_same_binding` compare the packet's full identity — task, leaf, number, both repositories/trees, both commits/refs and the conversion — so code-only or memory-only movement leaves an earlier packet bound to its own trees. `retained_supplemental` returns the receipts exactly as captured, never refreshed in place.

`intended_source_root` admits requirement packets, the leaf’s exact own JSON/Markdown names and `notes/reference/<leaf>/` as intended sources, excluding the task root as a whole, another leaf and `DEVELOPER-DIRECTION.md`. `intended_receipt_ids` uses only present admitted receipts. Supplemental sources omitted at the read ceiling are explicit `truncated-read` omissions alongside omitted collections.

## Evidence

- Packet assembly copies the comparison owner's sides instead of inventing them, and fills every collection or names why it is missing. 
- A packet read as evidence of another comparison is refused on the owner's full identity. [2]
- Supplied populations carry measured counts and explicit omission reasons.
- A skipped collection is carried as not selected or not read, with its reason. [4]


- Intended sources are selected by the exact leaf and admitted receipt identities. The builder accounts for supplied and unread collection populations. [5]


- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/review_evidence_packet.py::build_evidence_packet - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/application/review_evidence_packet.py::_admit_populations - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
