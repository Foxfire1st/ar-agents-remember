# mcp/src/agents_remember/application/knowledge_writer/weakness_authoring.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

`author_weakness` fills a weakness record's anchored place and checks its authored closure against the writer's admitted code repository. `Authoring._write_record` calls it before placing a weakness record. This helper edits the operation's in-memory document and collects problems through `Authoring`; it does not publish files itself.

## Code Commentary

### Anchored place

The curator supplies an anchor path and locator. `_weakness_anchor` refuses a missing path or malformed locator and otherwise resolves the place at candidate C, filling its blob and content identity. If resolution fails and the earlier record has an anchor at the same path, the complete earlier anchor is retained; without that same-path recorded place, the failure is reported. This allows a record to retain where its cause occurred after a file or symbol disappears, without inventing a replacement location or rewriting `seen`. [2]

### Closure

`_closure` acts when the record's state is closed and its `closed` value is a mapping. A supplied string commit must equal the full identity of a commit in the admitted code repository. A newly authored closure without a commit must name the running leaf, or the task of a non-leaf owner. An earlier closed record whose closure mapping is unchanged is left alone during an unrelated metadata edit, including when a later task owns that edit. [3]

The record model separately requires a task and a reason when no commit is supplied, and checks agreement between the closed block and the record's state. Read-time commit attribution is owned by `knowledge_reader/weakness_closure.py`. [4]

## Evidence

### Repo-Internal References

- Anchor authoring resolves at C or retains the complete stored anchor only for the same recorded path. [2]
- Closure checks admit the running task's deferred attribution and validate an explicitly supplied commit. [3]
- The closure and weakness models own the stored shape and state agreement. [4]

- Record authoring delegates weakness anchoring and closure checks before placing the record. [1]
