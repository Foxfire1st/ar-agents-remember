# tools.md

## Governing Overview

[overview](../../../../../../../../overview.md)

## Current source contract evidence

- Current source declarations support the qualified naming or fixture account; no executed test or acceptance is inferred. [7]

## Purpose

The packaged coordinator tools example separates shared coordinator commands from each
repository memory layer's checks and workflow instructions. It is a template for shared coordinator commands, not execution authority or the advertised MCP roster.

## Code Commentary

Repository-specific commands belong in memory `system/tools.md`; resolve the selected
repository through `context_packet` before choosing its task, worktree, memory or validation paths.


## Current evidence

- The coordinator-level tools example: the Global Commands placeholder and the Notes directing agents to resolve the target repository through context_packet and prefer memory-layer tool instructions for repository-specific commands. [6]

## Evidence

### Docs References

No external documentation is needed.

No relevant external documentation found.

### Repo-Internal References

- The coordinator tools example places repository-specific checks, commands, branch workflow and code quality tools in the selected memory layer's system/tools.md, not here. [1]

- The notes tell agents to resolve the target repository through `context_packet` before choosing task, worktree, memory or validation paths. [8]

### Cross-Repo References

No sibling repository evidence is needed.

No meaningful cross-repo references found.
