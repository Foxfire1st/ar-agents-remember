# mcp/src/agents_remember/models/read_files.py

## Governing Overview

> FileReadStatus, FileRead, carried source/onboarding/format/references/published_intent and lifecycle-deduplicated overview bodies are not current response fields or owners. Strict validation and token stamping survive under the current NamedRecord/NamedFile naming model.

[overview.md](overview.md)

## Current naming-reader contract — MIK-R109

`NamedRecord` names only action-asking records by ID, kind, state and heading (with disclosed titleFallback). `NamedFile` names source existence, governing card location, card state, per-state counts and action records, plus two one-line counts where they are non-zero: `openWeaknesses` (open weaknesses anchored to that file) and `dependentDocuments` (documents whose dependent record stands on it). A confined-row refusal carries unknown existence and a reason, without dropping valid siblings. `ReadArFilesResponse` is strict, `state` is named/refused, `codeState`/`codeTree` say the observed code and `memoryState` says whether memory can be named. Governing overview locations are once per call, nearest first. `cardStatus` admits `found`, `missing` and `sidecar-only`; an existing JSON half with no Markdown half is named at its JSON path. No source/onboarding/overview text, sidecar/reference document, published_intent block, session dedup or continuation is in this model. Token stamping remains at the shared choke.

## Current source contract evidence


- Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance.


## Purpose

> FileReadStatus, FileRead, carried source/onboarding/format/references/published_intent and lifecycle-deduplicated overview bodies are not current response fields or owners. Strict validation and token stamping survive under the current NamedRecord/NamedFile naming model.

`read_files.py` defines the AR-owned, strict response contract for the
`read_ar_files` tool: one batch of knowledge locations for repository-relative paths.

## Code Commentary

> FileReadStatus, FileRead, carried source/onboarding/format/references/published_intent and lifecycle-deduplicated overview bodies are not current response fields or owners. Strict validation and token stamping survive under the current NamedRecord/NamedFile naming model.





`ReadArFilesResponse` subclasses `ToolResponse` (strict), with `operation` (`"read_ar_files"`), `repoId`, named files, governing overview locations, observed code/memory state and refusal fields. Token fields are stamped by
`finalize_payload_tokens` at the `_tool_payload` choke point — this module never
sets them.



### Role Runtime and Scope

> FileReadStatus, FileRead, carried source/onboarding/format/references/published_intent and lifecycle-deduplicated overview bodies are not current response fields or owners. Strict validation and token stamping survive under the current NamedRecord/NamedFile naming model.



## Invariants And Boundaries

> FileReadStatus, FileRead, carried source/onboarding/format/references/published_intent and lifecycle-deduplicated overview bodies are not current response fields or owners. Strict validation and token stamping survive under the current NamedRecord/NamedFile naming model.

- STRICT AR-owned shape: the models forbid extra fields. `ReadArFilesResponse` is
  registered in `tool_registry.PUBLIC_TOOL_RESPONSE_MODELS` and exercised by the
  conformance suite, which requires a representative payload per registered tool.

- Token fields are part of the contract but populated only at the choke point.


## Evidence

> FileReadStatus, FileRead, carried source/onboarding/format/references/published_intent and lifecycle-deduplicated overview bodies are not current response fields or owners. Strict validation and token stamping survive under the current NamedRecord/NamedFile naming model.

### Repo-Internal References

> FileReadStatus, FileRead, carried source/onboarding/format/references/published_intent and lifecycle-deduplicated overview bodies are not current response fields or owners. Strict validation and token stamping survive under the current NamedRecord/NamedFile naming model.

- The strict response base and `ToolResponse`. [1]



- The registry mapping `read_ar_files` to this response model (L88). [5]

### Runtime Source References

> FileReadStatus, FileRead, carried source/onboarding/format/references/published_intent and lifecycle-deduplicated overview bodies are not current response fields or owners. Strict validation and token stamping survive under the current NamedRecord/NamedFile naming model.




- The strict ReadArFilesResponse names governing files and overviews and observed state; it carries no published-intent body. [6]
