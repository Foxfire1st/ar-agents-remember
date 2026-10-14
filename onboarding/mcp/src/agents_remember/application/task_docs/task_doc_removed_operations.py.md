# mcp/src/agents_remember/application/task_docs/task_doc_removed_operations.py

## Governing Overview

[Task-document application overview](overview.md)

## Purpose

Refuse the removed get/read_steps operations with file-reading guidance, without making absent or corrupt content a prerequisite for that refusal.

## Code Commentary

The caller retains legitimate target and address validation. This helper then attempts a best-effort `read_task_doc`; `OSError`/`ValueError` produce a nonfatal fallback naming the canonical JSON and rendered filenames. A successful identity read uses the document's rendered path and ordinary result identity, but still answers `ok:false`/`operation-removed`.

The module's never-parsing prose is not the implemented contract and the accepted fixed disposition is not a no-parsing policy. The caught fallback does not promise no read, no raise from every earlier validation, or immunity to arbitrary exceptions. It creates no document and authorizes no native canonical-document writes.

## Evidence

- The helper uses best-effort identity with caught fallback and refuses removed operations in both branches. [1]
