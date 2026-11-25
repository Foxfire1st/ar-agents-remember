# mcp/src/agents_remember/mcp/registration/__init__.py

## Governing Overview

[Registration](overview.md)

## Purpose

Declare the shared registrar signature and ordered tuple of ordinary tool-family registrars.

## Code Commentary

`ToolRegistrar` is a callable receiving a FastMCP server and runtime configuration. `TOOL_REGISTRARS` contains ten family registrars in advertised order: core, seat retirement, memory, worktrees, closeout, tasks, capsule/skill resources, role agents, knowledge and explainer control. The module exports both names.

Family modules own tool declarations. The package imports the registrars; the server factory invokes them. Registration order remains part of advertisement and must agree with the model-owned public roster. The capsule/skill registrar serves resources and extension methods rather than tools.

## Relationships

`create_server` owns compact serialization, application services and server construction. Every launch invokes the ordinary tuple; a valid explainer binding additionally registers the explainer's four tools. Their per-call seat binding is separate from ordinary registration. The live tool-list comparison checks the ordinary advertised set rather than trusting a payload that repeats it.

## Evidence


- `create_server` iterates the ordinary registrar tuple. [1]


- The public tool-name list has one model-owned definition re-exported by the adapter. [2]
- The live tool-list comparison checks the advertised registration against the roster. [7]
- `TOOL_REGISTRARS` declares the ten family registrars in order. [8]
- The registration module leaves compact serialization, application services and process composition to `create_server`. [9]
- Every launch registers the ordinary families; a valid explainer launch adds its four tools. [10]
