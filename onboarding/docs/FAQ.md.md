# docs/FAQ.md

## Governing Overview

[Repository overview](../overview.md)

## Purpose

Answers common questions and objections about Agents Remember across its design principles, memory layer, workflow layer, separate Git memory repository, tool comparisons, and non-goals, using the terminology defined in `docs/concepts.md`.

## Code Commentary

- Explains deterministic mirrored-path card lookup (`src/foo/bar.ts` -> `<memory-root>/onboarding/src/foo/bar.ts.md`), bounded `read_ar_files` brief/compact reply shapes, 11-view `knowledge_read` (text-bearing `impact`/`search`, verbatim `records` up to 25 IDs, and structured locations/reports in the other views), and text/keyword search via `knowledge_read(view="search")` or native search.
- Distinguishes drift reporting (`context_packet` with `include_drift`, `knowledge_read`, and `citation_fix`) from closeout publication blocking at the exact-tree knowledge gate.
- Keeps task documents (plans and in-progress notes) separate from approved current-state cards and records, and explains `memory.md` as a Git-ignored computed attribution cache derived from `Code-Commit` trailers.

## Relationships

- Uses definitions from `docs/concepts.md` and aligns with the `read_ar_files` and `knowledge_read` contracts documented in `docs/reference/mcp-tools.md`.

## Evidence

- Deterministic mirrored-path card lookup, bounded `read_ar_files` brief/compact row degradation, and 11-view text-bearing `knowledge_read` (`impact`, `search`, `records`, and compact `dependent` triage). [1]

- Anchor staleness reporting (`context_packet` `include_drift`, `knowledge_read`, `citation_fix`) versus exact-tree closeout knowledge-gate blocking. [2]
- Separate Git memory repository and Git-ignored `memory.md` computed from `Code-Commit` trailers. [3]
