# mcp/src/agents_remember/serving/response_contract.py

## Governing Overview

[serving overview](overview.md)

## Purpose

Strict immutable camel-aliased response vocabulary for retained file/onboarding, notes, task/requirement, action/refusal and change-set routes. Terminal catalog/open/conflict/task-assignment response models are removed.

## Code Commentary

WireResponse forbids extra fields and is frozen; route declarations describe success and explicit refusal shapes. Returning an already-built Response is not runtime model enforcement, so declarations alone are not an executed conformance claim. ComparisonChangeSet names comparison mode, comparison number and four code/memory trees. LeafChangeSet separates working/committed mode from recorded/unrecorded state and stateDetail; an unrecorded zero must not be read as a measured landed-empty range. MasterChangeSet carries net scope/currentness and optional exact generation endpoints. Existing caller mirrors and per-model fields retain their own supporting references. `CHANGESET_READ_RESPONSES` extends the scoped-read declarations with bodyless 304 metadata. It is wire documentation, not runtime Response validation or executed conformance.

FileContent and NoteContents carry optional media type and an over-limit flag beside their measured size; their bytes routes supply recognized pictures and videos separately. DiffSide separates text content from binary/media metadata and permits an absent side for an addition or deletion. FileResolution reports whether a repository-relative path exists and whether it is a file or directory, with optional language and media type.

- File and note metadata, repository path resolution and independently classified diff sides are declared wire shapes. [16]

## Evidence boundary

The declarations describe wire shapes. They do not establish that a route validated an already-built response or that conformance was executed.

## Source-bound reference inputs

- [1]
- [5]
- [6]
- [10]
- [11]
- [12]
- [13]
- [14]
- [15]
