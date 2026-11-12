# mcp/src/agents_remember/application/review_explainer_receipts.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The supplemental receipts every explainer packet carries: the leaf's own packets, its task document, the reference folder the developer's picks name, and the agreed revision's manifest — each admitted through the task that owns it and bound by the bytes read.

## Code Commentary

- None of these sources is part of the comparison, so none is citable as though it were: each becomes a receipt whose canonical source is stated relative to the owning task and whose content is captured by `capture_supplemental`.
- A source that cannot be read is an `unavailable` receipt carrying its limitation — a measured loss rather than a refusal, so the build goes on and the page knows what it could not see.
- The leaf's own document is admitted under its name only when `document["id"]` is that leaf; a document that names another leaf admits nothing of its own.
- One packet's ceiling is 48 sources: the task document and the agreed manifest are reserved first, then packets and reference files in order, and anything past the ceiling is receipted as an explicit truncated-read omission rather than silently dropped.
- An agreed revision is the yardstick only when it resolves to a retained revision whose digest matches the agreed sha256; otherwise the receipt says which of those two facts failed.

## Evidence

- Every source one build or Update carries is receipted through the task that owns it [1]
- The required yardsticks are reserved before packets and reference files at the read ceiling
- An agreed revision that does not resolve or verify yields an unavailable receipt with its reason [3]
- The requirement files are taken from the leaf's own document in the order it names them [4]
- A source past the ceiling reads as a truncated-read omission, never as a read file [5]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/review_explainer_receipts.py:164-177 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.
