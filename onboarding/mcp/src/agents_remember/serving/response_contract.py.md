# mcp/src/agents_remember/serving/response_contract.py

## Governing Overview

[serving overview](overview.md)

## Purpose

Strict immutable camel-aliased response vocabulary for retained file/onboarding, notes, task/requirement, action/refusal and change-set routes. Terminal catalog/open/conflict/task-assignment response models are removed.

## Code Commentary

WireResponse forbids extra fields and is frozen; route declarations describe success and explicit refusal shapes. Returning an already-built Response is not runtime model enforcement, so declarations alone are not an executed conformance claim. ComparisonChangeSet names comparison mode, comparison number and four code/memory trees. LeafChangeSet separates working/committed mode from recorded/unrecorded state and stateDetail; an unrecorded zero must not be read as a measured landed-empty range. MasterChangeSet carries net scope/currentness and optional exact generation endpoints. Existing caller mirrors and per-model fields retain their own supporting references. `CHANGESET_READ_RESPONSES` extends the scoped-read declarations with bodyless 304 metadata. It is wire documentation, not runtime Response validation or executed conformance.

## Evidence boundary

This is current-source interpretation of the A9 candidate, not a new test result, CODE grade or MEMORY acceptance. The retained supporting references below are reauthored through the ordinary fixer; unsupported removed constructs are withdrawn, not rebound to arbitrary neighboring code.

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
