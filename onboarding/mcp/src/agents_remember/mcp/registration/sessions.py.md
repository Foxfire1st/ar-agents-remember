# mcp/src/agents_remember/mcp/registration/sessions.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/registration/sessions.py`       |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated | 2026-08-30T12:04+02:00 |
| lastVerifiedCommitHash | `f9f92ca793811b6cb738d7e302dfecdf8636e96e`                   |
| lastVerifiedCommitDate | 2026-08-30T14:26:46+02:00|
| governingOverview      | `overview.md`                                                |

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

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Dispatch accepts only structural identity and the brief. | `dispatch_agent` | mcp/src/agents_remember/mcp/registration/sessions.py:27-49 |
| Child retire and rename use document plus role. | `retire_child`; `rename_child` | mcp/src/agents_remember/mcp/registration/sessions.py:51-81 |
| Self rename derives the caller ambiently. | `rename_self` | mcp/src/agents_remember/mcp/registration/sessions.py:91-94 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-30T12:04+02:00 — 260821-ARSPAWN-L3 made the published tool description explicitly
  fail closed for every invalid plane-identity class, with no plane-to-ambient fallback.
  Verification remains closeout-owned.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1: `dispatch_agent`'s published description documents the caller-kind matrix (plane seat → structural path with identity proof + child-scope; ambient launcher → ambient mode with pinned brief + same rollback, no parent seat, role-altitude validation still applies); `spawn_agent_session` stays internal-only. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-11T14:29+02:00 — Re-read dispatch, child retirement/rename, and self-rename and
  widened their citations to include the registered-tool decorators; verification metadata
  remains unchanged for governed closeout.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the bare-`*` keyword-only signature remediation (PLR0917). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 6 citation findings; scoped check passed.

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The five session
  declarations moved out of `server.py`; `spawn_agent_session` now packs its arguments into
  `SpawnSeat` / `RetiredSpawnInputs` / `SpawnedBy` in the body while the published flat signature is
  unchanged. Verification metadata pinned to the pre-change commit until closeout stamps the L2 code
  commit.
