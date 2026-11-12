# mcp/src/agents_remember/mcp/tools/read_files.py

## Governing Overview

[overview.md](overview.md)

## Current source contract evidence


- Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance. [6]


## Purpose

`read_files.py` is the thin payload builder for the `read_ar_files` tool
(slice 07): it forwards to the application entry point and returns the result through the
shared token choke point.

Builds read_ar_files response payload through existing resolution and token owners.

## Code Commentary

`read_ar_files_payload` derives call-local configuration through `task_scoped_mcp_config_for_reader`. Ordinary files are repository-relative strings, up to twenty. The receivable `refresh` sentinel is only a removed-argument refusal boundary: supplied true, false or null refuses `argument-removed`; the ordinary schema omits it. The builder passes the admitted leaf’s worktree group as `working_folder`, delegates naming to `read_ar_files_tool`, and validates/stamps through `_tool_payload`. The reader names existence, card state/counts and overview locations once per call; it carries no source, card or overview text and has no continuation. [1] [2] [3]

### Role Runtime and Scope

Optional task_context is admitted to a call-local config, without mutating the shared configuration. `_working_folder` uses the admitted code checkout’s parent for caller-openable locations; absent task context keeps absolute locations. Task/enclosure authority stays with the admission owner.

## Invariants And Boundaries

- The payload module stays a thin facade: validation and token stamping happen in
  `_tool_payload`; domain behavior belongs to the application entry point.
- Token fields are stamped by `_tool_payload`, never set here.

## Evidence

### Repo-Internal References


- The application entry point that does the actual resolution. [1]


- The shared choke point every tool's payload passes through: an adapter that hands the tool's whole result, and its compact answer when one is projected, to the application's response completion, where the response is validated and the answer's token count stamped. [2]


- The strict response model `read_ar_files` validates against. [3]


### Runtime Source References


- Frozen implementation of read_ar_files_payload supporting the stated file behavior. [4]


- Alternating/concurrent registered base and leaf calls preserve their source/memory roots; wrong repository, canonical contract and malformed pairs refuse. [5]
