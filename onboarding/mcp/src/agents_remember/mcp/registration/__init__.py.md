# mcp/src/agents_remember/mcp/registration/__init__.py

## Governing Overview

[Registration](overview.md)

## Purpose

Declare the shared registrar signature and ordered tuple of ordinary tool-family registrars.

## Code Commentary

`ToolRegistrar` is a callable receiving an `MCPServer[Any]` and runtime configuration. `TOOL_REGISTRARS` contains nine ordinary tool-family registrars in advertised order: core, seat retirement, memory, worktrees, closeout, tasks, role agents, knowledge, and explainer control. The module exports both names.

Family modules own tool declarations. The package imports the registrars; `create_server` constructs the server with `SkillsExtension` (from `capsule_serving.build_skills_extension`) and then invokes `TOOL_REGISTRARS`. Registration order remains part of advertisement and must agree with the model-owned public roster.

## Relationships

`create_server` owns application services, `SkillsExtension` construction, `MCPServer` creation, direct compact `CallToolResult` conversion (via `mcp/tool_results.py`), and role scoping. Every launch invokes the nine ordinary registrars; a valid explainer binding additionally registers the explainer's four tools. Their per-call seat binding is separate from ordinary registration. The live tool-list comparison checks the ordinary advertised set rather than trusting a payload that repeats it.

## Evidence

- `create_server` iterates the ordinary registrar tuple. [1]



- The public tool-name list has one model-owned definition re-exported by the adapter. [2]

- The live tool-list comparison checks the advertised registration against the roster. [7]


- `TOOL_REGISTRARS` declares the nine ordinary tool-family registrars in order. [8]
- The registration module leaves `SkillsExtension` assembly, application services, and process composition to `create_server`. [9]

- Every launch registers the ordinary families; a valid explainer launch adds its four tools. [10]
