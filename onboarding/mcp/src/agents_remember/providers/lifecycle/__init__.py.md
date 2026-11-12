# mcp/src/agents_remember/providers/lifecycle/__init__.py

## Current operative account — MIK-R112

The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.

- Current facade is lazy __getattr__ over _EXPORT_MODULES, with no __all__.
- CLI module is no longer an export owner.

### Superseded inventory

- Pre-repair card claim: Card says facade imports CLI main and generates __all__. This is superseded archival wording, not a current prescription.

### Source and authority bounds

- Source comparison: `mcp/src/agents_remember/providers/lifecycle/__init__.py:9 (_EXPORT_MODULES =)`.
- Source comparison: `mcp/src/agents_remember/providers/lifecycle/__init__.py:26 (def __getattr__)`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

## Governing Overview

[mcp/overview.md](overview.md)

## Purpose

`providers.lifecycle` is the public provider lifecycle package facade. It
re-exports provider-owned CGC and GrepAI lifecycle modules, shared lifecycle
helper modules, CLI functions, and aggregate watcher actions.

## Code Commentary

### Logic

The facade imports `ContextProviderError`, `stable_provider_id`, all CGC and
GrepAI lifecycle exports, shared helper modules by responsibility, watcher
operations, and the CLI `main()` function. `__all__` is generated from the
public global names so tests and service callers can keep using the former
monolithic public surface.

### Invariants And Boundaries

- Keep the facade import-only; provider-specific implementation belongs in
  provider-owned lifecycle packages.
- Keep `main()` sourced from `lifecycle.cli`.
- Callers import this facade directly; there is no `provider_lifecycle.py`
  compatibility module.

## Evidence

### Repo-Internal References


- CGC exports are grouped behind the CGC package facade. [2]
- GrepAI exports are grouped behind the Docker-owned GrepAI package facade. [3]

</details>
