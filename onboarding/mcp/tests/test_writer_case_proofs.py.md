# mcp/tests/test_writer_case_proofs.py

## Governing Overview

[tests route overview](overview.md)

## Current source account — a proof that names a case by its lines

Each case builds a real Git code and memory world, writes a small `pkg/cases.test.tsx`, and submits a proof whose `test` is `{path, locator: {kind: "line_range", start, end}}`. The admitted case proves lines 4-6, the `it.each` case, and reads back a single `proves` entry whose anchor locator is that range and whose `content` is the `sha256:` digest of exactly those three source lines; the evidence naming the case's own title is reported `proof_written` and names the case as `path::title`. A computed title's expanded evidence is not a pairing, so the evidence entry stays `unresolvable` while the proof is written and listed among the entries.

Refusals are texts, not shapes. A span inside a case (`5-5`) is refused as `lines 5-5 of pkg/cases.test.tsx are not a case a line range proves` with the overlapping span `4-6`, a `.skip` case is refused because it does not run, and a `.ts` file that is not a test file is refused by name; each of those leaves the memory tree byte-identical. A name taken by an ordinary `const` beside the case, or resolving to a declaration elsewhere in the file, does not close the range, so the case is still proved by its lines; a literal case under a computed `describe` title pairs by its own title.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- A line-range proof stores a `line_range` anchor with the case's blob content and reports the paired evidence `proof_written` [1]
- A computed title's evidence stays `unresolvable` while its proof is written and listed [2]
