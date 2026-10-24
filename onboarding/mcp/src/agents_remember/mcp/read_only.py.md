# mcp/src/agents_remember/mcp/read_only.py

## Governing Overview

[Owning route overview](../../../overview.md)

## Purpose

Own the explicit read-only/mutating partition used to annotate every registered MCP tool.

## Code Commentary

Server creation applies this single partition after registration. A registered name absent from both sets raises UnknownReadOnlyMark rather than shipping an unclassified annotation. The marks describe the complete advertised capability, not whether one particular invocation happened to write.

knowledge_diff is marked mutating because working-tree comparison can capture loose Git objects and the naming handler publishes a comparison report. context_packet is marked mutating because include_freshness can update Git fetch metadata. Report-producing diagnostics and task/host/memory writers are also mutating; an operation’s read-like name is not authority to mark it read-only.

`dispatch_agent` is absent from both mark sets after its registered surface was retired; its old mutating mark is historical, not a retained advertised tool. `retire_child` remains mutating because it changes seats.

Read-only checks exclude only the derived index and logs under their owner rules. The mark does not prove that a harness will suppress its permission prompt, and it grants no write authority.




## Evidence

- The current partition marks retained capabilities, including mutating retire_child, and omits retired dispatch_agent. [1]
- An unknown registered name fails closed instead of receiving a default mark. [2]
- Annotations are applied after registrars from the same partition. [3]

## The settings initializer is a writer

`user_settings_init` is in the mutating set: a call that is not a preview creates the one user settings file, so the mark describes the capability rather than one invocation's choice. The partition, its fail-closed rule and its application after registration are otherwise unchanged.

- The mutating set that now carries the settings initializer. [4]
