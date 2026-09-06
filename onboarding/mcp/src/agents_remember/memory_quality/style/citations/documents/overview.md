# Citation Document Publication

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/memory_quality/style/citations/documents` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `b34f4a59562b76a3e2413027468e0f699117b36f` |
| lastVerifiedCommitDate | 2026-09-06T06:31:12+02:00 |
| governingOverview | `../../../overview.md` |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Projection admission precedes staging; declined claims retain their original bytes. | `_decide` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:336-381 |
| Accepted batches check complete document bytes and held source/cell bindings before atomic publication. | `DocumentTransaction` | mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py:30-99 |

## Docs And Boundary References

No external Domain Documentation source is configured. This route composes repository-owned citation and atomic-publication owners, without a new cross-repository protocol.

## Update History

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation: Created the focused route for the new transaction package at actual private C b34f4a59; no delivery or aggregate acceptance is asserted.

