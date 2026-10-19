# mcp/src/agents_remember/application/review_evidence_read.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Bounded investigation reads at a comparison's exact trees: the operand is the comparison's own side (the effective converted tree for a converted memory base), path spellings that could point elsewhere are refused by name, and every read is a measured window of the object it read — an honest remainder, a continuation that never leads past the object's end, and that end named when the requested range runs beyond it.

## Code Commentary

`side_operand` resolves one side through the record and names the stored tree beside the effective one; `_path_problem` refuses `HEAD`, a ref, a URL, an absolute path, a `..` segment and pathspec magic rather than repairing them. Reads stream a `cat-file --batch` child and stop at the declared byte, line, page and scan budgets, so an offset beyond the scan budget refuses before a blob is read.
`_take_window`, `_scan_cut` and `_receipt_from_window` keep empty, absent, truncated and unavailable apart: a line longer than the window is returned as the decoded prefix text this read examined, marked cut, with a byte offset in the receipt that strictly advances, a range past the decoded prefix is truncated rather than absent, and the receipt states the requested and returned ranges, the remainder where the read measured it and the limit that cut it. `_remainder` counts only lines the read measured: a requested end line inside the examined bytes gives the exact remainder, a window that holds the object's end states the count a page bound held back or that the request is complete, and a suffix the read never examined states no count. A read whose requested range runs past the object's end ends at that last line and is `present`, with no continuation and no limit, and its detail names the line; `_located_start` and `_object_end_absence` answer a read started at the object's end with the measured range absence the scan already gives a start line past the end, so no empty line and no byte-less continuation exists. `measured_limits` records the measurement that earns a number; `evidence_address` and `read_claim_basis`, both defined and exported by `review_evidence_claims`, read a claim's `side:path#L1-L2` reference through the same bound. The receipt carries the byte coordinates (`returned_bytes`, `next_byte`) beside the text, so a cut read is text plus an offset rather than a bytes-valued result.

## Evidence

- A read resolves its side through the comparison and names the effective and stored memory-base trees apart. [1]
- A path spelling that could name another operand is refused rather than repaired. [2]
- One bounded read returns a window, an honest remainder and a progressing continuation. [3]
- A line cut by the window is returned as the decoded prefix text it examined, with the next byte offset, never as absence. [4]
- A scan that could not reach the requested line says so instead of certifying an empty range. [5]
- A requested range that runs past the object's end ends at its last line and is complete, with no continuation and no limit. [6]
- A read started at or past the object's end is a measured range absence, never an empty line and never a continuation that reads no byte. [7]
