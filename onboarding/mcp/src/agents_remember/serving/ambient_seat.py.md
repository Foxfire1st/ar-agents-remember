# mcp/src/agents_remember/serving/ambient_seat.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Resolves BOTH dispatch caller kinds from trusted hosted-process environment and the authoritative
catalog: the plane-hosted structural seat (`resolve_ambient_seat`) and the ambient launcher
(`resolve_ambient_caller`, a process with no plane identity). It is the boundary that keeps agents
from supplying their own session or lifecycle ids.

## Code Commentary

### Logic

`resolve_ambient_seat` reads plane-seeded hosted context, finds its catalog row, and verifies the
current task-document+role binding before returning the occupant. Hosted identity without a
non-empty process role is now incomplete; a role that disagrees with the catalog remains a mismatch.
`resolve_ambient_caller` returns the typed `AmbientCaller` (caller_kind `ambient`, no catalog row, no
lifecycle of its own) only when the process has neither `AR_HOSTED_SESSION_ID` nor `AR_SPAWN_ROLE`.
A role without the plane-injected hosted identity is incomplete rather than ambient. Plane identity present
means the caller must go through `resolve_ambient_seat`. Since 260821-ARSPAWN-L1 fix round 3
`dispatch_agent`'s `_resolve_dispatch_caller` is ambient-first — `resolve_ambient_caller` decides
the branch directly (the earlier both-fail defensive guard was dead code because both functions
read the same environ) — and the function is covered by direct unit tests
(`test_resolve_ambient_caller_returns_none_when_plane_identity_is_present` /
`test_resolve_ambient_caller_returns_ambient_without_plane_identity` in
`test_dispatch_agent_ambient.py`).

### Conventions

All failure cases are typed `AmbientSeatError` statuses so application tools can fail closed.

### Invariants And Boundaries

- Request payloads never participate in caller identity.
- Unknown, stale, retired, or mismatched hosted evidence is refused.
- There is no global current-role fallback.
- No plane identity means an ambient caller, never a fallback: a process WITH plane identity always
  goes through `resolve_ambient_seat` (its failures refuse, never downgrade); `resolve_ambient_caller`
  is the ambient-first branch decider for dispatch (the both-fail path was dead code and is gone).
- An ambient caller has no catalog row and no lifecycle of its own; its spawn provenance records
  caller kind `ambient` with no spawning session.

### Todos

None.

## Evidence

### Docs References


### Repo-Internal References

- Plane caller resolution is a single trusted-context function. [1]
- Ambient caller resolution returns the typed marker only when no plane identity exists. [2]

### Cross-Repo References
