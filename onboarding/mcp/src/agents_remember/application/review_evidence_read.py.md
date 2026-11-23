# mcp/src/agents_remember/application/review_evidence_read.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Reads bound source from a recorded comparison. A converted memory base uses the effective tree and names the original tree in the receipt. Path validation confines the read to the selected operand.

## Code Commentary

Both read forms examine the complete located object. The range form returns the requested lines and byte coordinates beside the object's actual line and byte counts. An end line beyond the object returns through its last line. A start line beyond the object returns measured range absence. The whole-source form returns exact UTF-8 text, including a trailing newline when present.

The Git subprocess directs its batch frame to a private spool. The reader checks the blob header type and reported size, then reads one complete body. Missing or malformed frames, non-blob objects and short bodies retain their distinct diagnostics.

## Evidence

- A read resolves its side through the comparison and names the effective and stored memory-base trees apart. [1]
- A path spelling that could name another operand is refused rather than repaired. [2]


- A requested start line beyond the last line returns measured range absence with the object's actual line count and examined byte count. [5]


- A requested range that runs past the object's end ends at its last line and is complete, with no continuation and no limit. 


- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/review_evidence_read.py::read_bound_source - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/application/review_evidence_read.py::_take_window - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 6df6b68c1b9714d360296e4cdeb978f5c22f7eea; mcp/src/agents_remember/application/review_evidence_read.py::_measured_object_end - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 4ce96ad77b243a4d55e28535e23d7557997b2d87; mcp/src/agents_remember/application/review_evidence_read.py::_remainder - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 6df6b68c1b9714d360296e4cdeb978f5c22f7eea; mcp/src/agents_remember/application/review_evidence_read.py::_scan_to_line - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 6df6b68c1b9714d360296e4cdeb978f5c22f7eea; mcp/src/agents_remember/application/review_evidence_read.py::_object_end_absence - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 4ce96ad77b243a4d55e28535e23d7557997b2d87; mcp/src/agents_remember/application/review_evidence_read.py::_located_start - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 4ce96ad77b243a4d55e28535e23d7557997b2d87. Retired means the anchor no longer stands, not that the cited subject was deleted.
