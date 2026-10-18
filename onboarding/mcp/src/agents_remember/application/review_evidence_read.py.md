# mcp/src/agents_remember/application/review_evidence_read.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Bounded investigation reads at a comparison's exact trees: the operand is the comparison's own side (the effective converted tree for a converted memory base), path spellings that could point elsewhere are refused by name, and every read is a measured window with an honest remainder and continuation.

## Code Commentary

`side_operand` resolves one side through the record and names the stored tree beside the effective one; `_path_problem` refuses `HEAD`, a ref, a URL, an absolute path, a `..` segment and pathspec magic rather than repairing them. Reads stream a `cat-file --batch` child and stop at the declared byte, line, page and scan budgets, so an offset beyond the scan budget refuses before a blob is read.
`_take_window`, `_scan_cut` and `_receipt_from_window` keep empty, absent, truncated and unavailable apart: a line longer than the window is returned as the decoded prefix text this read examined, marked cut, with a byte offset in the receipt that strictly advances, a range past the decoded prefix is truncated rather than absent, and the receipt states the requested and returned ranges, the remainder and the limit that cut it. `measured_limits` records the measurement that earns a number; `evidence_address` and `read_claim_basis`, both defined and exported by `review_evidence_claims`, read a claim's `side:path#L1-L2` reference through the same bound. The receipt carries the byte coordinates (`returned_bytes`, `next_byte`) beside the text, so a cut read is text plus an offset rather than a bytes-valued result.

## Evidence

- A read resolves its side through the comparison and names the effective and stored memory-base trees apart. [1]
- A path spelling that could name another operand is refused rather than repaired. [2]
- One bounded read returns a window, an honest remainder and a progressing continuation. [3]
- A line cut by the window is returned as the decoded prefix text it examined, with the next byte offset, never as absence. [4]
- A scan that could not reach the requested line says so instead of certifying an empty range. [5]
