# mcp/src/agents_remember/mcp/registration/sessions.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/registration/sessions.py`       |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated | 2026-08-11T14:29+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                   |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[registration route overview](overview.md)

## Purpose

Registers agent dispatch and structural child/self seat-management operations whose caller identity
is plane-resolved.

## Code Commentary

### Logic

`dispatch_agent` accepts child document, role, brief, and optional label. Retire/rename child use
the same structural address; rename-self has no identity argument. Application services own
authorization, runtime allocation, exact initial brief delivery, and cleanup.

### Conventions

The public operation family speaks task documents and roles only.

### Invariants And Boundaries

- Models never submit a session/lifecycle/terminal id.
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
| Self rename derives the caller ambiently. | `rename_self` | mcp/src/agents_remember/mcp/registration/sessions.py:83-86 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

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
