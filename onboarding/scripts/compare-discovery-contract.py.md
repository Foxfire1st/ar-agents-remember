# scripts/compare-discovery-contract.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Compares the complete MCP discovery answer of two source trees by running the seat command against each and canonicalising both `tools/list` results. It turns "discovery did not change" into a byte-level statement about every tool's name, order, description, schemas and annotations, with the first differences named when they differ.

## Code Commentary

- Each side is a real `tools/list` answer: the script builds a throwaway coordination world, spawns `python -m agents_remember.mcp --config <settings>` from that tree's own `mcp/.venv`, completes `initialize`, and keeps the whole result rather than a count or a name list.
- Both results are re-encoded with sorted keys and compact comma/colon separators and compared as strings; the record carries `identical`, both digests, both tool counts and both name lists, and a difference compares corresponding tool positions using `zip(strict=False)`, lists at most five differing paired positions and counts those paired-position differences. Tool counts and name lists separately disclose any unmatched tail; `difference_count` does not count unmatched tail entries.
- It asks the child process which `agents_remember` file it imported instead of trusting the venv's position, and sets `attribution_qualified` only when both answers name the root being compared; an unattributed digest is marked as such rather than presented as evidence.
- It writes both raw answers beside the record and hashes them, and records each tree's resolved root, git head and dirty-entry count so a digest is readable beside the tree that produced it.
- Its scope is stated in the record: `tools/list` only. Runtime refusals — dispatch refusing a tool outside the surface, a missing or invalid binding refusing service — are separate claims that this comparison does not make.

## Evidence

- Each compared side is the whole `tools/list` answer from a seat command spawned against that source tree. [1]
- The record places each digest beside that tree's resolved root, git head and dirty-entry count. [2]
- Attribution is qualified only when both children report a package under the compared root. [3]
- The process exits non-zero whenever the canonical encodings differ. [5]

- The script saves complete before/after discovery JSON+digests, compares canonical full answers, reports first differing tool schemas/descriptions/annotations and independently probes executed package attribution. It labels tools/list-only scope and excludes runtime refusal claims. [6]

- Differing paired positions are counted and at most five listed; tool counts and name lists disclose unmatched tails separately. [4]
