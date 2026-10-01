# mcp/src/agents_remember/mcp/registration/sessions.py

## Governing Overview

[registration route overview](overview.md)

## Purpose

Registers agent dispatch and structural child/self seat-management operations. `dispatch_agent`
accepts BOTH caller kinds: plane-hosted seats (identity proven from plane-injected process context)
and ambient launchers (no `AR_HOSTED_SESSION_ID`, caller kind resolved from the process environment);
the published description documents the caller-kind matrix so agents never guess which mode applies.

## Code Commentary

### Logic

`dispatch_agent` accepts child document, role, brief, and optional label. Retire/rename child use
the same structural address; rename-self has no identity argument. Application services own
authorization, runtime allocation, exact initial brief delivery, and cleanup. The `dispatch_agent`
description documents the caller-kind matrix: a plane-hosted seat (this process carries
`AR_HOSTED_SESSION_ID`) uses the structural path — caller proven from plane-injected identity,
direct-child scope authorized; an ambient caller (no `AR_HOSTED_SESSION_ID` — a launcher chat) spawns
in ambient mode with the pinned dispatch brief and the same rollback, with no parent seat (so
seat-authority and child-scope checks do not apply) but role-altitude validation still enforced.

### Conventions

The public operation family speaks task documents and roles only.

### Invariants And Boundaries

- Models never submit a session/lifecycle/terminal id.
- Ambient dispatch callers have no parent seat; seat-authority and child-scope checks do not apply,
  but the role is still validated against the document's altitude.
- A present but stale, invalid, mismatched, unbound, or unauthorized plane identity is a plane
  refusal. It never changes caller kind or retries through ambient authority.
- The initial brief is internally exact-pinned and persisted before delivery.
- Failed initial briefing retires the unbriefed child.
- Replacement does not change the public child address.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Dispatch accepts only structural identity and the brief. [1]
- Child retire and rename use document plus role. [2]
- Self rename derives the caller ambiently. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
