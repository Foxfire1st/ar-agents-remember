# mcp/src/agents_remember/serving/inbox_delivery.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/serving/inbox_delivery.py`    |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-07T22:15+02:00                                 |
| lastVerifiedCommitHash |                                                        `551695279f403ab19c0eba4ce6f6cfde6a8bb1f5`|
| lastVerifiedCommitDate |                                                        2026-07-07T20:09:01+02:00|
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
`no-hosted-session` metadata. Since 260707-HFX-L3 the unconfirmed
`deliveryDetail` is the loud-failure forensic record: `_unconfirmed_detail`
embeds the paster's final pane capture, TAIL-bounded to
`_CAPTURE_EVIDENCE_LIMIT` (2000 chars — the freshest pane output), so the
re-briefing operator reads what the pane actually showed rather than a bare
"not echoed"; an empty capture (vanished session) records
"paste was not capture-verified (empty pane capture)". The SUCCESS detail
string stays exactly `"echo-confirmed"` — dashboard copy references it.

### Conventions

Delivery is a push attempt layered on a durable inbox row. The helper never
deletes the row; polling/consuming remain available when hosted delivery is
missing or unconfirmed.

### Invariants And Boundaries

- A catalog row alone is not enough; the tmux session must also pass
  `TerminalHost.has_session`.
- `delivered` means the terminal paster capture-verified the paste on the pane,
  not merely pane output during harness boot.
- An unconfirmed push must carry its evidence: the durable `deliveryDetail`
  embeds the bounded pane-capture tail (260707-HFX-L3), and the success detail
  stays the exact string `"echo-confirmed"` (dashboard copy depends on it).
- The formatted stdin text is simple Markdown-ish text for agents, not a hidden
  protocol.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Delivery state is persisted on the operator inbox record. | [operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |
| Echo-confirmed paste behavior lives in the server-side paster. | [terminal_paste.py](agents-remember/mcp/src/agents_remember/serving/terminal_paste.py) |
| The dashboard serving route and MCP payload builder both pass catalog/host/paster seams for delivery. | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |

## Update History

- 2026-07-07T22:15+02:00 — 260707-HFX-L3 (capture-verified delivery): the unconfirmed
  `deliveryDetail` now embeds the paster's pane capture, tail-bounded to 2000 chars
  (`_unconfirmed_detail` + `_CAPTURE_EVIDENCE_LIMIT`; empty capture gets its own loud wording);
  the success detail string `"echo-confirmed"` is unchanged. Verification metadata pinned until
  closeout stamps the HFX-L3 commit.
- 2026-07-04T12:31+02:00 - L3: created the hosted inbox push-delivery helper card. Verification metadata pinned until closeout stamps the L3 commit.
