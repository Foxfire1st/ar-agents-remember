# mcp/tests/test_role_instruction_wording_handover.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

What a launched role is told: the handover text the launch builds in code, and the role tool descriptions, neither of which may name a forbidden host string.

## Code Commentary

The fixture compiles a role's capsule and builds the handover for taskless, sprint, master and leaf selections admitted by the production resolver, isolating only the task-reader and enclosure plumbing: no launch, model or lifecycle operation runs. The cases require the developer question channel to match the role and its parent, the owner relation to route developer questions and preserve coordinators, and the first message to name no forbidden host string. The reader context must name the readers of the task tool server, the handover must name that server, its two tools and the host, and a role without a parent must be told it needs none while a started role is told who started it. The description cases hold the three role-tool descriptions to the same forbidden list.

## Invariants And Boundaries

The forbidden search is the shared case-folded literal-substring matcher over the whole text: each entry must appear as one contiguous run of characters, so a spelling broken across a line is not matched. The text checked is the compiled capsule and the built handover, not a template source.

## Evidence

### Repo-Internal References

- The handover names the tool server, its two tools and the host, and tells a parentless role it needs none. [1]

- No first message and none of the three tool descriptions names a forbidden host string. [2]
