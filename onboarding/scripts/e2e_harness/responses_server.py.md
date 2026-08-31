# responses_server.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `scripts/e2e_harness/responses_server.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T22:20:19+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `scripts/e2e_harness/overview.md` |

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Provides the deterministic localhost Responses API that scripts model-side tool discovery and calls
while leaving the real Codex app-server and candidate MCP server untouched.

## Code Commentary

### Logic

`ScriptedResponses` correlates prior function outputs, classifies the current user prompt, selects the
next public action, discovers the requested tool from direct or tool-search results, validates the
real `dispatch_agent` name/description/schema through the canonical product validator, records its
digest, delegates controlled missing-brief and missing-ambient-description mutations to
`dispatch_sentinels.py`, and emits one SSE response. The HTTP handler bounds and safely parses
request size and preserves a redacted request summary on error.

### Conventions

Routes are explicit semantic fixture states. Tool-search completion is correlated by call id so an
older retained search cannot satisfy a later query. Namespace and direct function advertisements are
both accepted only when exactly one matching public tool exists.

### Invariants And Boundaries

- This server never supplies MCP tools or bypasses Codex discovery.
- Missing, duplicate, malformed, or stale tool-search evidence fails loudly.
- Dispatch name, caller-boundary description, nested canonical task reference, role vocabulary,
  fields, required inputs, and closed-object behavior must match the documented public surface.
- Both controlled negative variants must fail at the expected canonical boundary.
- Error diagnostics exclude full prompts and complete tool schemas.

### Todos

None.

## Docs References

No Domain Documentation source is configured. The real request payload is the runtime authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| Tool discovery and schema validation operate on the request produced by real Codex. | `ScriptedResponses` | scripts/e2e_harness/responses_server.py:47-127; scripts/e2e_harness/responses_server.py:329-344 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The state script maps ambient, hosted, retirement, vacancy, and replacement prompts to public tools. | `_action` | scripts/e2e_harness/responses_server.py:144-204; scripts/e2e_harness/responses_server.py:277-300 |
| Tool-search output is paired with its exact query call id. | `_has_completed_tool_search` | scripts/e2e_harness/responses_server.py:390-403 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The server is a local test provider with no sibling-repository dependency. | `ResponsesServer` | scripts/e2e_harness/responses_server.py:207-226 |

## Update History

- 2026-08-30T22:20:19+02:00 — 260821-ARSPAWN-L5 converted source references to the
  canonical anchored citation format. Verification metadata remains closeout-owned.

- 2026-08-30T22:11:35+02:00 — 260821-ARSPAWN-L5: delegated controlled negative
  advertisement proof construction to its dedicated module while retaining live-tool validation and
  event ownership here. Verification metadata remains closeout-owned.

- 2026-08-30T21:59:40+02:00 — 260821-ARSPAWN-L5: replaced the local top-level schema
  check with the canonical dispatch-advertisement validator, content digest, and two controlled
  regression sentinels; malformed request diagnostics no longer mask themselves. Verification
  metadata remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 created onboarding for the deterministic real-Codex Responses provider. Verification metadata remains closeout-owned.
