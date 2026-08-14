# mcp/src/agents_remember/serving/hosted_session_runtime.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/hosted_session_runtime.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-31 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

Holds `HostedSessionRuntime` — the pair of authorities that jointly decide which hosted sessions
exist. New at 260731-EFA-L2.

A hosted session is two things at once: a durable catalog row (identity, provenance, control
metadata) and a live tmux process. Neither answers "does this session exist" on its
own — opening, reopening, retiring, delivering to and reconciling a seat all read the row and probe
the process together, and **a row read against the wrong host is a silent correctness bug**. This
type makes the pairing a single value so the two can only travel bound to each other.

## Code Commentary

### Logic

One frozen dataclass, two fields:

```
HostedSessionRuntime(catalog: TerminalCatalog, host: TerminalHost)
```

`catalog` is the durable hosted-session catalog; `host` is the tmux host that runs its sessions.
`__all__` exports only `HostedSessionRuntime`.

It mirrors the composition-time bundles the serving layer already uses (`ConversationRuntime`,
`AgentNotifierContext`): the authorities are frozen together once and then passed as one thing.

### Invariants And Boundaries

- Catalog and host must be the matching pair. Constructing one with someone else's host is the exact
  bug the type exists to prevent — a test that fakes the host must build the runtime with the
  catalog that agrees with it.
- This module holds no behaviour. If session logic starts accumulating here, it belongs in the
  catalog, the host, or the opener.

## Docs References

No domain documentation source is configured for this repository.

## Repo-Internal References

- [terminal_opener.py](terminal_opener.py.md) — `open_terminal_session(runtime=..., ...)` is the
  primary consumer; it replaced the previous separate `catalog=` / `host=` keywords.
- [terminal_catalog.py](terminal_catalog.py.md) — the durable row store.
- [terminal.py](terminal.py.md) — `TerminalHost`, the tmux side.
- [app.py](app.py.md) — builds one from its `_ServingRuntime` when calling the opener.

## Cross-Repo References

No meaningful cross-repo references.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: created for the new module. Verification metadata stays
  pinned to the pre-commit source history until closeout.

