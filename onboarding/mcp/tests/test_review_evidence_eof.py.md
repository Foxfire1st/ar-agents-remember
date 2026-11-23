# mcp/tests/test_review_evidence_eof.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Checks measured end-of-object behavior and exact whole-blob transport in the comparison evidence reader.

## Code Commentary

The range cases check exact terminal lines in one reply, including a 450-line body and a line longer than the old window. A start line beyond EOF returns measured absence. Whole-blob transport cases verify exact bytes and decoded text, source length, bounded traced peak and the typed failure details for a malformed, missing, non-blob or short frame.

## Evidence

- The six-line object read at lines 1–100 is present at its last line, with no remaining line, continuation or limit. [1]

- A start line one past the object's end is also a measured range absence. [5]

- Retired at the fifth freeze d59c3493: mcp/tests/test_review_evidence_eof.py::test_f03_r182_a_page_past_the_object_end_stops_at_its_last_line - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 4ce96ad77b243a4d55e28535e23d7557997b2d87; mcp/tests/test_review_evidence_eof.py::test_f03_r182_an_unmeasured_remainder_is_unknown_not_the_requested_difference - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 4ce96ad77b243a4d55e28535e23d7557997b2d87; mcp/tests/test_review_evidence_eof.py::test_f03_r182_a_read_started_at_the_object_end_is_a_measured_absence - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 4ce96ad77b243a4d55e28535e23d7557997b2d87. Retired means the anchor no longer stands, not that the cited subject was deleted.
