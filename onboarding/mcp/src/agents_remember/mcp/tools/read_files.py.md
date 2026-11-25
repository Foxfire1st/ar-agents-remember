# mcp/src/agents_remember/mcp/tools/read_files.py

## Governing Overview

[overview.md](overview.md)

## Current source contract evidence




## Purpose

`read_files.py` is the thin payload builder for the `read_ar_files` tool
(slice 07): it forwards to the application entry point and returns the result through the
shared token choke point.

Builds read_ar_files response payload through existing resolution and token owners.

## Code Commentary

`read_ar_files_payload` derives call-local configuration through `task_scoped_mcp_config_for_reader`. Ordinary files are repository-relative strings, up to twenty. The receivable `refresh` sentinel is only a removed-argument refusal boundary: supplied true, false or null refuses `argument-removed`; the ordinary schema omits it. The builder passes the admitted leaf’s worktree group as `working_folder`, delegates naming to `read_ar_files_reply` and supplies the reply's fitter to `complete_tool_response`. The fitter can retain fuller card and count fields, list governing overviews once, and include eligible rule text where space permits. Compact replies retain each path, its available status and any brief pointer with saved freshness. Open a current saved brief when present. Reading leaves the memory folder unchanged. [1] [2] [3]

### Role Runtime and Scope

Optional task_context is admitted to a call-local config, without mutating the shared configuration. `_working_folder` uses the admitted code checkout’s parent for caller-openable locations; absent task context keeps absolute locations. Task/enclosure authority stays with the admission owner.

## Invariants And Boundaries

- The application reader assembles its payload and fitter. The shared completion boundary validates and measures the delivered response.

## Evidence

### Repo-Internal References
















### Runtime Source References




- Alternating/concurrent registered base and leaf calls preserve their source/memory roots; wrong repository, canonical contract and malformed pairs refuse. [5]

- The application reply owns the exact context, tree observation and naming rows. [1]


- The payload gives the reader's fitter to the shared response completion after scope resolution. [2]

- The strict response permits named file rows, an optional overview list, and brief problem and omission fields. [3]

- The payload applies the removed-argument refusal and shares the same completion boundary for admitted requests. [4]



- The mounted adapter delegates row assembly and sends the fitter when completing the response. [6]
