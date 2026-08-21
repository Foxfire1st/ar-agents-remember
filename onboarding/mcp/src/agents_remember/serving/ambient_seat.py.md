# mcp/src/agents_remember/serving/ambient_seat.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/ambient_seat.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T06:47+02:00 |
| lastVerifiedCommitHash |  `3eafc555c848ac45a07a07720641f1735f8df0eb`|
| lastVerifiedCommitDate |  2026-08-21T05:15:52+02:00|
| governingOverview | `overview.md` |

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
current task-document+role binding before returning the occupant — unchanged since 260731-EFA-L19.
`resolve_ambient_caller` returns the typed `AmbientCaller` (caller_kind `ambient`, no catalog row, no
lifecycle of its own) only when the process has no `AR_HOSTED_SESSION_ID`; plane identity present
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

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Plane caller resolution is a single trusted-context function. | `resolve_ambient_seat` | mcp/src/agents_remember/serving/ambient_seat.py:55-101 |
| Ambient caller resolution returns the typed marker only when no plane identity exists. | `resolve_ambient_caller`; `AmbientCaller` | mcp/src/agents_remember/serving/ambient_seat.py:25-52 |

## Cross-Repo References


## Update History

- 2026-08-21T03:45+02:00 — 260821-ARSPAWN-L1 fix round 3: `resolve_ambient_caller` is now the ambient-first branch decider for dispatch (the both-fail path was dead code and is gone) and its plane-present→`None` branch is unit-tested in `test_dispatch_agent_ambient.py`. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1: the file now owns BOTH dispatch caller resolutions — `resolve_ambient_seat` (plane) unchanged and the new `AmbientCaller`/`resolve_ambient_caller` (no plane identity means ambient, never a fallback; the dispatch path refuses when neither resolution yields a caller). Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for trusted ambient caller resolution.
