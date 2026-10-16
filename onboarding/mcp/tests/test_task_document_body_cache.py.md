# mcp/tests/test_task_document_body_cache.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin conditional on-demand task-body preparation, exact native generation invalidation and cache bounds.

## Code Commentary

Task bodies omit duplicated task summary identity/stage/progress/subtask fields. Repeated ETag reads return 304 before native parsing; edits with restored mtime, replacement, symlink/retarget/deletion, graph inputs and grant additions/edits/removal invalidate. Unreadable metadata and inputs changing during native composition retain nothing. Count/byte LRU limits affect retention, not native read semantics. The ASGI route checks no-cache and bodyRevision; symlink escape remains a native 404 boundary. These are disposable file/HTTP fixtures, not browser or installed performance evidence.

## Evidence

- Unchanged conditional response precedes parse and body excludes duplicated task summary fields. [1]
- Restored-mtime, replace, symlink and deletion mutations revoke the prior response. [2]
- Changed and newly authored graph-master inputs affect the body. [3]
- Live grant additions/edits/removal invalidate bodies. [4]
- Unavailable generation metadata uses the native uncached response. [5]
- A file changed during composition is not retained under the old generation. [6]
- Count and byte limits bound retained bodies and eviction preserves native semantics. [7]
- Actual in-process HTTP route revalidates without reparse and returns new text after edit. [8]
- Symlink retarget updates the body and an outside target remains 404. [9]
