# responses_server.py

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

## Evidence

### Docs References

No Domain Documentation source is configured. The real request payload is the runtime authority.

- Tool discovery and schema validation operate on the request produced by real Codex. [1]

### Repo-Internal References

- The state script maps ambient, hosted, retirement, vacancy, and replacement prompts to public tools. [2]
- Tool-search output is paired with its exact query call id. [3]

### Cross-Repo References

No meaningful cross-repository reference applies.

- The server is a local test provider with no sibling-repository dependency. [4]
