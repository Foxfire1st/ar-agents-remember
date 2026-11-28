# mcp/src/agents_remember/mcp/read_only.py

## Governing Overview

[Owning route overview](../../../overview.md)

## Purpose

Own the explicit read-only/mutating partition used to annotate every registered MCP tool.

## Code Commentary

The central vocabulary marks `render` read-only and `define_category`, `remove_category`, `grade` and `explainer_control` mutating. Unknown marks raise instead of receiving a default.

Server creation enforces this single partition at registration time: `AgentsRememberMCP.add_tool` (when `enforce_read_only_marks=True` in `create_server`) calls `read_only_annotations(tool_name, annotations)` and passes the resulting `ToolAnnotations` to public `MCPServer.add_tool`. When registration supplies `ToolAnnotations`, `read_only_annotations` merges those site-declared hints (`title`, `destructive_hint`, `idempotent_hint`, `open_world_hint`) via `annotations.model_copy(update={"read_only_hint": read_only_hint(tool_name)})` so the central `read_only_hint` partition always wins (`context_packet` and `knowledge_diff` stay `False`); when no site annotations are passed, it constructs `ToolAnnotations(read_only_hint=...)`. A registered name absent from both sets raises `UnknownReadOnlyMark` during `create_server` before role narrowing rather than shipping an unclassified annotation. The marks describe the complete advertised capability, not whether one particular invocation happened to write.

knowledge_diff is marked mutating because working-tree comparison can capture loose Git objects and the naming handler publishes a comparison report. context_packet is marked mutating because include_freshness can update Git fetch metadata. Report-producing diagnostics and task/host/memory writers are also mutating; an operation’s read-like name is not authority to mark it read-only.

`dispatch_agent` is absent from both mark sets after its registered surface was retired; its old mutating mark is historical, not a retained advertised tool. `retire_child` remains mutating because it changes seats. `citation_note_revision` is also in the mutating set because its admitted capability writes one reference note; a preview invocation does not make the capability read-only.

Read-only checks exclude only the derived index and logs under their owner rules. The mark does not prove that a harness will suppress its permission prompt, and it grants no write authority.




## Evidence

- The current partition marks retained capabilities, including mutating `retire_child`, and omits retired `dispatch_agent`. [1]
- An unknown registered name fails closed instead of receiving a default mark. [2]

- Registration-time `ToolAnnotations` merge registration-site hints while forcing `read_only_hint` from the central partition. [3]

## The settings initializer is a writer

`user_settings_init` is in the mutating set: a call that is not a preview creates the one user settings file, so the mark describes the capability rather than one invocation's choice. The partition, its fail-closed rule and its registration-time application are otherwise unchanged.

- The mutating set that carries the settings initializer. [4]
- The central vocabulary marks `render` read-only and `define_category`, `remove_category`, `grade` and `explainer_control` mutating. Unknown marks raise instead of receiving a default. [5]
