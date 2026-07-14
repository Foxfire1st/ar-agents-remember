# harness_control_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T13:59+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b` |
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose
Process entrypoint that owns one adapter bridge, local control endpoint, vendor subprocess,
transcript rendering, and correlated stdin/session-command submission for a hosted session.

## Code Commentary
### Logic
Runner configuration is encoded as a bounded command payload, decoded before launch, and bound to
the exact catalog identity. The server starts before the adapter, renders state/transcript updates,
and shuts down the endpoint and adapter in a final cleanup path. Codex TUI arguments are translated
to app-server argv while non-TUI passthrough arguments remain intact.
### Invariants And Boundaries
The runner is for built-in hosted harnesses; ordinary shells do not use it. Terminal input is
submitted through the bridge, never treated as an inter-agent mailbox or readiness signal.

## Docs References
No relevant external/domain documentation was configured; runner and adapter tests are authoritative.

## Repo-Internal References
- [terminal_opener.py](terminal_opener.py) composes the runner command.
- [harness_control_bridge.py](harness_control_bridge.py) owns adapter state and receipts.

## Cross-Repo References
No meaningful cross-repo references.

## Update History
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented bridge-owned hosted launch, exact identity,
  correlated commands, transcript rendering, and shutdown.
