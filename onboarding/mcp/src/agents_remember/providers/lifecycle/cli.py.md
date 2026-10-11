# mcp/src/agents_remember/providers/lifecycle/cli.py

## Current operative account — MIK-R112

The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.

- Current source CLI file is deleted.
- Removal of this operator CLI does not prove all lifecycle services are absent.

### Superseded inventory

- Pre-repair card claim: Card advertises provider lifecycle CLI parser/main and cgc/grepai/watchers dispatch. This is superseded archival wording, not a current prescription.

### Source and authority bounds

- Source comparison: `mcp/src/agents_remember/providers/lifecycle/cli.py (absent; git diff HEAD -- this path: deleted file mode 100644)`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`cli.py` owns the provider lifecycle command-line surface: parser construction,
argument normalization, action dispatch, result rendering, and `main()`.

## Code Commentary

### Logic

The parser exposes `cgc`, `grepai`, and `watchers` subcommands with provider
action-specific arguments, including a `no_cache` flag (default `False`) on the
image-build paths that forces a from-scratch Docker rebuild. The
`--from-settings` help text (both providers) names the server-generated
provider lifecycle settings JSON and states there is no coordinator
`system/settings.json` fallback (260703-L13 — the implicit fallback was deleted
in `provider_settings.py`; settings-driven commands without the flag now refuse
with a `ContextProviderError`). Normalizers resolve
paths and stable provider IDs after parsing. Dispatch maps provider names to CGC, GrepAI, or watcher
implementation functions and renders either JSON, native bounded command
output, or a compact text summary. The CGC `patch` subcommand has been
removed: it is no longer parsed, no longer imported (`cgc_patch` is gone from
the `cgc.lifecycle` import), and no longer present in `cgc_cli_handlers()`.

### Invariants And Boundaries

- CLI dispatch is an operator interface; MCP service callers should use
`lifecycle_service.py` and implementation functions directly.
- Argument normalization should stay shallow and avoid provider behavior.
- CGC arguments do not carry a Python executable; Docker runner construction
  owns provider execution.
- Captured native command output should remain streamable for bounded `run`
  actions.

## Evidence

### Repo-Internal References

- Public facade imports `main()` from this module. [1]
- CGC and GrepAI implementations are dispatched from this CLI layer. [2]

</details>
