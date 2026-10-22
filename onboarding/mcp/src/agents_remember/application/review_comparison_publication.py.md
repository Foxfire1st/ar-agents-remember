# mcp/src/agents_remember/application/review_comparison_publication.py

## Governing Overview

[Owning route overview](../../../../overview.md)

## Purpose

Publish one comparison record so that the first writer wins and no later writer replaces it.

A comparison record is immutable once it exists. Publishing it used to ask whether the file was there and then write it, so two processes that both found it absent published the same number and the later write replaced the record an earlier reader had already answered with.

## Code Commentary

`publish_comparison_record` writes the record's bytes to a temporary file private to the call (process id and a random suffix) and publishes it by linking that file into place. `os.link` fails with `FileExistsError` when the name is taken, so the create itself is the decision: a call that loses the race returns `False` and publishes nothing, and the temporary file is removed on the two linking paths — a successful link and the lost race; the bytes are written, flushed, fsynced and closed before that cleanup, so a failure there escapes with the temporary file still on disk. `_fsync_directory` flushes the directory entry on platforms that have a directory handle.

`publication_refusal` names the case where a number went to another pair: a retryable `reviewer_busy` refusal with the number as its offending input, never a silent overwrite.

Nothing here numbers, pins or re-reads a record. Numbering, identity, pinning and reuse stay the comparison owner's, which calls this module and answers the winning record when its own publication loses.

## Invariants And Boundaries

Only the first create names a record. A lost race publishes nothing and answers either the winner's bytes or the named refusal. The module holds no numbering, pin or retention authority, and writing a record grants no review or acceptance.

## Evidence

- The record is published by an exclusive link of a private temporary file, so a later writer publishes nothing. [1]
- A directory entry is flushed where the platform has a directory handle. [2]
- A number taken by another pair is a named retryable refusal. [3]
