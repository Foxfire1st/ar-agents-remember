# mcp/src/agents_remember/kernel/coordination_context/serialize.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/serialize.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-06T22:15:27+00:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`serialize.py` owns JSON-safe and text formatting for resolved coordination
contexts.

## Code Commentary

`cross_repo_entry_to_dict` always emits repo, expectedBranch, includeCode and includeMemory. State, reason, code and memory are emitted only when truthy; unset cross-repository optionals are omitted rather than null. This differs from context path fields, whose absent values use empty strings. `path_to_string` resolves filesystem paths before formatting them. cit:([`path_to_string`, `cross_repo_entry_to_dict`], mcp/src/agents_remember/kernel/coordination_context/serialize.py:15-16; mcp/src/agents_remember/kernel/coordination_context/serialize.py:42-57).

### Logic

The module converts `CoordinationContext`, storage rules, and cross-repo
entries into dictionaries with string paths and stable keys. `print_text()`
emits the legacy tab-separated text format used by the CLI.

### Invariants And Boundaries

- Serialization does not mutate the context; path formatting resolves paths through `path_to_string`.
- Empty optional paths serialize as empty strings in JSON output, preserving the
  old resolver contract.

## Docs References

No external documentation is needed for this local formatter.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The CLI delegates JSON/text output to this module. | "context_to_dict("; "print_text(" | mcp/src/agents_remember/cli/coordination_resolver.py:108-108; mcp/src/agents_remember/cli/coordination_resolver.py:110-110 |
| The application context packet builds the packet with `context_to_dict()`. | `build_context_packet`; "context_to_dict(" | mcp/src/agents_remember/application/context_packet.py:59-102 |

## Cross-Repo References

No cross-repository evidence is needed for this formatter.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-06T22:15:27+00:00 — Preserved actual asset/context semantics from retired test onboarding; verification pins unchanged.

- 2026-08-04T11:34:10+02:00 — 260731-EFA-L6 S18-B12 curator: anchored the CLI and application consumers of the formatter, including the packet builder's formatter call.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-05-25T20:57+02:00: Created by extracting `c-08-ar-coordination-context-resolver` skill JSON/text serialization from the monolithic resolver.
