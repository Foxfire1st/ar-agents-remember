# mcp/src/agents_remember/canvas/explainer_access.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The seat's whole read authority — list, search and read over the admitted surfaces, six read-only Git subcommands, and the knowledge views at the bound memory tree — with the binding-claim and seat checks every answer passes through.

## Code Commentary

- `ExplainerReads` admits a surface only from a closed set (`code`, `memory`, `snapshot-<n>/code`, `snapshot-<n>/memory`, `pages`, `reference`) and refuses any other name as `surface-unknown` before a path is joined, so no caller can widen the read root by asking for a name.
- A relative path is refused when it carries `..`, an empty segment, a backslash or a drive letter; an object name is refused when it is a range, an option or a worktree path. Both refusals are typed values answered as data, never a crash.
- `ExplainerGit` composes the argv itself, so an external diff program, a textconv or filters override, a `-c` override, a pager, `--output` and `diff --no-index` have no spelling that reaches Git; an answer from history is marked as history and explicitly not as evidence.
- `ExplainerReads.reading` answers one bounded chunk with the whole file's digest and a continuation offset, and an oversized file is refused by name instead of being silently truncated.
- `require_claim` refuses a call made at a comparison the environment has left (`binding-moved`) and a claim that names no binding of this environment at all (`binding-unknown`), instead of resolving the nearest one.

## Evidence

- One comparison identity token names the owner, the number and all four trees, and a planned binding names its two tips instead [1]
- A surface this reader does not serve is refused by name before any path is resolved [2]
- Traversal, an absolute path, an empty segment and a drive letter are refused as `path-refused` [3]
- A Git option that would run another program, read a worktree path or write an output is refused, and every Git answer is marked history and not evidence [4]
- A read is one bounded chunk of a size-capped file, with the whole-file digest and the next offset [5]
- The knowledge views are a closed set, and any other view name is refused [6]
