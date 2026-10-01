# Citation Document Publication

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/memory_quality/style/citations/documents` |

## Governing Overview

[Memory quality overview](../../../overview.md)

## What This Area Is

The accepted citation-document batch owner. It composes the fixer's accepted source-cell edits and deterministic projection history into exact final bytes, then verifies the original document and frozen source bindings before publishing through the existing atomic writer.

## Hot Path Summary

`transaction.py` defines `Edit` and `DocumentTransaction`. The fixer admits edits before constructing a batch; `render`, `unchanged`, `preview` and `publish` own composition and the final-read boundary. `__init__.py` is a docstring-only package marker. Exact-name resolution remains in the parent citation route.

## Operating Model

One batch holds one original UTF-8 document, one source-index snapshot ID and its accepted edits. Preview and publication use the same full-byte, cell and projection preconditions; only successful publication contributes a completed-write count. The complete rendered digest includes grouped generated history and retains CRLF bytes. A detected conflict refuses that document's accepted batch and preserves the concurrent content; other documents are independent.

## Local Invariants And Traps

The application owns write-scope authorization; the index lease supplies frozen source authority. Neither is a memory-file mutex. Atomic replacement prevents partial files, but final-read comparison cannot exclude a writer after validation. No live source recensus or OS compare-and-swap is claimed. This overview describes prepared private C; Gate 5 and delivery remain pending.

## File-Level Onboarding Map

- [Package marker](__init__.py.md) has no runtime side effects.
- [Transaction owner](transaction.py.md) binds complete accepted document publication.

## Evidence

### Repo-Internal References

- Projection admission precedes staging; declined claims retain their original bytes. [1]
- Accepted batches check complete document bytes and held source/cell bindings before atomic publication. [2]

### Docs And Boundary References

No external Domain Documentation source is configured. This route composes repository-owned citation and atomic-publication owners, without a new cross-repository protocol.
