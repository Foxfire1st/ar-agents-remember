# mcp/src/agents_remember/mcp/read_only.py

## Governing Overview

[Owning route overview](../../../overview.md)

## Purpose

Own the explicit read-only/mutating partition used to annotate every registered MCP tool.

## Code Commentary

Server creation applies this single partition after registration. A registered name absent from both sets raises UnknownReadOnlyMark rather than shipping an unclassified annotation. The marks describe the complete advertised capability, not whether one particular invocation happened to write.

knowledge_diff is marked mutating because working-tree comparison can capture loose Git objects and the naming handler publishes a comparison report. context_packet is marked mutating because include_freshness can update Git fetch metadata. Report-producing diagnostics and task/host/memory writers are also mutating; an operation’s read-like name is not authority to mark it read-only.

Read-only checks exclude only the derived index and logs under their owner rules. The mark does not prove that a harness will suppress its permission prompt, and it grants no write authority.




## Evidence

- The explicit partition covers registered reads and mutating capabilities. [1]
- An unknown registered name fails closed instead of receiving a default mark. [2]
- Annotations are applied after registrars from the same partition. [3]
