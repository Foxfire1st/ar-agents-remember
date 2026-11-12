# mcp/src/agents_remember/application/memory_quality/citation_runs.py

## Governing Overview

[../overview.md](../overview.md)

## Purpose

Owns asynchronous citation-preview admission and execution through the existing quality-run registry.

## Code Commentary

`start_citation_preview` validates selection and resolves configured memory scope, or admitted candidate scope when a contract is supplied, before building an immutable identity with operation `citation_fix` and document selectors. It submits the synchronous preview callable to `start_quality_run`; it does not construct a second worker registry. `_execute_preview` revalidates the admitted scope before and after the callable. `poll_citation_preview` delegates repository, operation, scope and freshness checks to the common controller.

### Invariants And Boundaries

Capacity refusal and runtime loss use the shared run contract. Background work is preview-only; the adapter rejects a write request before admission. Completion reports a computed result, not clean memory or lifecycle acceptance.

## Evidence


- Preview admission binds scope, operation and document selectors. [1]


- Polling uses the common scope controller. [2]


- The worker checks scope around the synchronous preview. [3]

