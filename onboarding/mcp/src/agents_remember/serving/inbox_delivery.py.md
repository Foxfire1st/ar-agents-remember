# mcp/src/agents_remember/serving/inbox_delivery.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/serving/inbox_delivery.py`    |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-04T12:31+02:00                                 |
| lastVerifiedCommitHash |                                                        `6b940141fc319f1d2d18b2c94fd9e9a213d43141`|
| lastVerifiedCommitDate |                                                        2026-07-04T12:52:03+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[overview.md](overview.md)

## Purpose

Push-delivery helper that takes one durable operator inbox entry and injects it
into a matching hosted terminal session through the server-side echo-confirmed
paste seam.

## Code Commentary

### Logic

`deliver_inbox_entry(...)` resolves a target running `TerminalCatalogEntry` by
exact agent id first and lifecycle id second. It verifies the tmux session still
exists through `TerminalHost.has_session`, formats an inbox block with message
kind, sender, optional artifact path, ask, and response, then calls
`TerminalPaster.paste(..., submit=True)`. The same inbox entry is updated through
`OperatorInboxStore.record_delivery(...)` with `delivered`, `unconfirmed`, or
`no-hosted-session` metadata.

### Conventions

Delivery is a push attempt layered on a durable inbox row. The helper never
deletes the row; polling/consuming remain available when hosted delivery is
missing or unconfirmed.

### Invariants And Boundaries

- A catalog row alone is not enough; the tmux session must also pass
  `TerminalHost.has_session`.
- `delivered` means the terminal paster saw a real composer echo, not merely pane
  output during harness boot.
- The formatted stdin text is simple Markdown-ish text for agents, not a hidden
  protocol.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Delivery state is persisted on the operator inbox record. | [operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |
| Echo-confirmed paste behavior lives in the server-side paster. | [terminal_paste.py](agents-remember/mcp/src/agents_remember/serving/terminal_paste.py) |
| The dashboard serving route and MCP payload builder both pass catalog/host/paster seams for delivery. | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |

## Update History

- 2026-07-04T12:31+02:00 - L3: created the hosted inbox push-delivery helper card. Verification metadata pinned until closeout stamps the L3 commit.
