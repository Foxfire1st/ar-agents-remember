# mcp/tests/role_instruction_wording_support.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The skill trees, the forbidden strings and the file readers the two wording case modules share, split out so the instruction-file cases and the handover cases read the same canonical tree and matcher.

## Code Commentary

`CANONICAL` is the checkout's `skills` tree and `PACKAGED` the runtime copy the capsule compiler reads. `FORBIDDEN` lists the host strings a role text may not name, including the removed tools and the earlier seat variables, and `forbidden_in` searches case folded. `REPORT_DIRECTORY` is the report segment a handover states. `LAUNCHER_ROLES` is derived from the launcher role arguments through `canonical_role`, `STARTERS` names the three starting roles, and `_NAMED_TOOL` matches a public tool in code font. `instruction_files` reads the lifecycle composition manifest and returns the router plus each launcher role's file and the operations that apply to those roles; `read` and `role_text` load a file and collapse a role file's whitespace.

## Invariants And Boundaries

The forbidden search covers the report directory segment as part of the whole text, so a rename of that directory cannot leave an unchecked spelling. The packaged tree is read separately because a canonical rewrite is not live until the sync has run.

## Evidence

### Repo-Internal References

- The forbidden strings and the one matcher are defined here, and the role set is derived from the launcher roles. [1]

- The instruction set comes from the lifecycle composition manifest: the router, the role files and their operations. [2]
