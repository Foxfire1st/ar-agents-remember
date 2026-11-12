# mcp/src/agents_remember/worktrees/integration/closeout/curator_judgments_file.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Reads the optional JSON judgment/assessment file for curator publication under the inline models and resource bounds.

## Code Commentary

The file is opened once nonblocking and must be regular; its size is checked before allocation and the descriptor read is capped to budget plus one byte. The budget accounts for the bounded scalar-field maxima and collection-count limits with UTF-8 or ASCII-escaped supplementary-character expansion. Remaining unbounded assessment content is independently subject to the total file-byte cap: model-valid inline content can exceed that cap. Parsing accepts a JSON object whose optional `judgments` and `review_assessments` list keys default to empty; unknown keys and non-list values refuse. Each supplied entry uses the same inline models and collection limits; later exact candidate coverage is a separate publication check. The digest describes the exact bytes read. Shape, special-file, unreadable and over-budget failures name the file; explicit inline lists, including empty ones, cannot also use the file source.

## Evidence

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.

- One descriptor, regular-file and byte-budget checks bound input acquisition. [1]
- File collections use inline entry models and limits. [2]
