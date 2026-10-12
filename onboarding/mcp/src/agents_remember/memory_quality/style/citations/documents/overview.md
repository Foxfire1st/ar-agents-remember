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

## How It Is Built

One batch holds one original UTF-8 document, one source-index snapshot ID and its accepted edits. Preview and publication use the same full-byte, cell and projection preconditions; only successful publication contributes a completed-write count. The complete rendered digest includes grouped generated history when the document has the canonical history section, and retains CRLF bytes. A detected conflict refuses that document's accepted batch and preserves the concurrent content; other documents are independent.

### File-Level Onboarding Map

- [Package marker](__init__.py.md) has no runtime side effects.
- [Transaction owner](transaction.py.md) binds complete accepted document publication.


## Invariants And Boundaries

The application owns write-scope authorization; the index lease supplies frozen source authority. Neither is a memory-file mutex. Atomic replacement prevents partial files, but final-read comparison cannot exclude a writer after validation. No live source recensus or OS compare-and-swap is claimed.

This route composes repository-owned citation and atomic-publication owners, without a new cross-repository protocol.


## Lifecycle And Provider Metadata

The following retained metadata is outside the operative promises above. The lifecycle statement has no current authority supplied; it is retained under the packet’s status-line exclusion, not a verified pending gate. The configured Domain Documentation registry was independently read and has no entries.

This overview describes prepared private C; Gate 5 and delivery remain pending.

No external Domain Documentation source is configured.

## Evidence

- Projection admission precedes staging; declined claims retain their original bytes. [1]
- Accepted batches check complete document bytes and held source/cell bindings before atomic publication. [2]
