# codex_driver.py

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Owns the real Codex consumer boundary for the clean-room scenario: candidate MCP probing, ambient
app-server execution, bounded notification collection, negotiated-version evidence, and subprocess
diagnostics.

## Code Commentary

### Logic

The public helpers bridge synchronous scenario code into bounded async probes. Candidate MCP
registration is checked independently, then a fresh real Codex app-server session starts against
the deterministic Responses endpoint and normally configured MCP server. Evidence keeps bounded
turn/notification summaries, exact process status, negotiated 0.151.0 identity, and explicit
absence of ambient plane/role environment identity rather than copying entire logs. The caller may
select the initial or same-seat-idempotency fixture prompt; neither path adds model-held retries.

### Conventions

Codex is invoked from the candidate container's selected executable. Environment construction is
explicit and fixture-scoped; no host configuration or production credentials are inherited by
accident.

### Invariants And Boundaries

- This module never fakes Codex or the MCP transport.
- The deterministic model provider controls choices only; real app-server protocol and MCP tool
  discovery remain in force.
- Timeouts are bounded and failure evidence is size-limited.
- The executed client must report the pinned 0.151.0 release in acceptance evidence.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured. Runtime negotiation is the authority for the client
actually exercised by this file.

- The real app-server probe and ambient turn collect negotiated runtime evidence. [1]

### Repo-Internal References

- MCP registration and handshake are inspected before ambient execution. [2]
- Process and notification summaries stay bounded for actionable reports. [3]

### Cross-Repo References

No meaningful cross-repository reference applies.

- All external state is fixture-provided rather than imported from another repository. [4]
