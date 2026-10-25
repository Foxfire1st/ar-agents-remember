# mcp/src/agents_remember/providers/recovery.py

## Current operative account — MIK-R112

The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.

- The shared constant no longer instructs provider_watchers restart/status/diagnostics.
- It now says stop the named leftover process and rerun install.
- Only providers-remove deletes leftover runtime folders; old enabled keys are reported unused.

### Source and authority bounds

- Source comparison: `mcp/src/agents_remember/providers/recovery.py:1-8`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`providers/recovery.py` centralizes provider recovery strings that need to be
identical across status projection and runtime-install recovery reporting.

## Code Commentary

### Logic

The module currently exposes `PROVIDER_WATCHER_RESTART_RECOVERY`, the
operator-facing instruction to run `provider_watchers(action='restart')` when a
watcher must rebind to current runner roots without invalidating provider
indexes. Both provider status and runtime install use this text when reporting a
non-destructive recovery action.

### Conventions

- Keep recovery text concrete and operator-actionable.
- Keep destructive index rebuild guidance separate from restart/rebind guidance.

### Invariants And Boundaries

- Restart/rebind guidance must preserve indexes and must not suggest
 `invalidate-indexes`.
- This module holds shared wording only; status classification and watcher
 lifecycle execution live in their respective modules.

### Todos

None.

## Evidence

### Docs References

No external documentation is configured for this repository slice.

No relevant documentation found after checking configured sources.

### Repo-Internal References

The shared recovery text is consumed by both provider status and runtime-install
watcher rebind reporting.

- The shared recovery constant names `provider_watchers(action='restart')`, current runner roots, preserved indexes, and follow-up status/diagnostics checks. [1]
- Runtime-install watcher recovery actions use the shared restart/rebind text when provider watchers remain degraded. [2]
- Provider status carried the same shared recovery text for GrepAI `noWorkspace`; both that status recovery text and `noWorkspace` are gone at C, where the two providers are retired.

### Cross-Repo References

No sibling repository evidence is needed for this shared message module.

No meaningful cross-repo references found.

</details>
