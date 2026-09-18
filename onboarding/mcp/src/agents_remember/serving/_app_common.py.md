# mcp/src/agents_remember/serving/_app_common.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_common.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-17T10:25+02:00 |
| lastVerifiedCommitHash | `0346da9c572e1eb913a8eb4130e9a9e9d37343c8` |
| lastVerifiedCommitDate | 2026-09-17T09:06:38+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[Serving overview](overview.md)

## Purpose

Defines shared serving request/composition models and helper seams used by the split FastAPI route
modules.

## Code Commentary

### Logic

`TerminalAttachTaskRequest` accepts the canonical task-document reference and role used by the
assignment route. Shared runtime/collaborator records keep topology, catalog, host, projection, and
cache dependencies explicit for route handlers. `_ServingRuntime` is the one collaborator bundle the
lifespan and the read routes share, so a fact written by one half and served by the other cannot land
on two different objects: since `LOCR-R17@v1` it carries `observer_health`
(`TerminalObserverHealthPublisher`) on the same observer root and the same serving clock as the
liveness sweeper. `stream_events` takes the observer-health payload as an optional keyword and passes
it into `served_state_tail`, so the SSE `snapshot` carries `terminalObserverHealth` beside the
heartbeat while a `delta` — one projection node, not a state body — carries no tail at all.

Since `260915-CAPS-L15` the collaborator bundle also carries `capsule_launch`
(`LaunchCapsuleResolver | None`), the application-tier capsule compiler injected by the composition
root. `serving` ranks below `application` in `layers.toml`, so the dashboard's launch route cannot
import the compiler; it takes this port exactly as it takes the execution-evidence registrars above, and
a process that omits it **refuses** a role-configured launch by name
(`capsule-resolver-unavailable`) rather than starting a seat with no instructions. The port is
declared on both `ServingCollaborators` and `_ServingRuntime`, and `serving/app.py` copies it from the
first onto the second.

### Conventions

Wire parsing belongs here; structural qualification and mutation delegate to owned services. The
serve-time tail arguments are optional keywords, and absence is a valid served answer rather than an
error: a caller with no build stamp, no heartbeat reader, or no observer-health source still produces
a valid body.

### Invariants And Boundaries

- No leaf-key attach request or compatibility parser remains.
- Request identity is task document plus role.
- Runtime collaborators are server-resolved, not browser-provided authority.
- **The capsule compiler crosses a port, never an import.** `ServingCollaborators.capsule_launch` is
  the only way this rank reaches `application`; it is optional in the record and fail-closed in
  behaviour (an absent resolver refuses a role-configured launch instead of silently running legacy).
- **The served surfaces hold no capsule content.** The port returns the decision and the carriers; the
  route publishes only the compact per-run record, so no instruction prose enters the served state.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Terminal assignment parses canonical document and role. | `TerminalAttachTaskRequest` | mcp/src/agents_remember/serving/_app_common.py:300-304 |
| The one collaborator bundle the lifespan and the routes share, including the observer-health owner added by `LOCR-R17@v1`. | `_ServingRuntime` | mcp/src/agents_remember/serving/_app_common.py:458-479 |
| The SSE event sequence: one additive, omissive tail on the `snapshot` and none on a `delta`. | `stream_events` | mcp/src/agents_remember/serving/_app_common.py:120-157 |
| The application-rank capsule compiler as an injected port, absent means a named refusal rather than a capsule-less launch. | `ServingCollaborators.capsule_launch`; `_ServingRuntime.capsule_launch`; `LaunchCapsuleResolver` | mcp/src/agents_remember/serving/_app_common.py:455-462; mcp/src/agents_remember/serving/_app_common.py:496-496; mcp/src/agents_remember/serving/launch_capsule.py:162-163 |
| The composition root that fills the port with the real compiler. | `serving_collaborators` | mcp/src/agents_remember/cli/dashboard.py:67-83 |
| The refusals the port's presence decides, in the one gate every launch point calls. | `resolve_launch_capsule`; `capsule-resolver-unavailable` | mcp/src/agents_remember/serving/launch_capsule.py:275-314 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## 260821-CLIVE Execution-Evidence Collaborators

`ServingCollaborators` now exposes explicit terminal-catalog and operator-inbox execution-evidence
registrars. `_ServingRuntime` retains the inbox registrar for notifier sweeps. These injected seams
let the serving process register task-bound worker/reviewer/curator first evidence before routine
retention can erase the only execution row; absence of a registrar is fail-closed for deletion.

## Update History

- 2026-09-17T10:25+02:00 — 260915-CAPS-L15 curator: **the shared bundle gained the capsule-compiler
  port.** `ServingCollaborators.capsule_launch` and `_ServingRuntime.capsule_launch` carry the
  application-tier compiler into the serving rank, which may not import it; `serving/app.py` copies the
  collaborator onto the runtime. The body records the boundary and its fail-closed half: an absent
  resolver makes the gate refuse a role-configured launch by name rather than run it capsule-less.
  Two invariants and three reference rows added. Verification metadata moves to this leaf's base
  `15fa0e2c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code
  commit and no hash or fingerprint was invented here.

- 2026-09-15T20:42+02:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`,
  base `99534dc5`, `_app_common.py` +19/−2): the shared runtime bundle and the SSE assembly gained
  the observer-health seam, so the body was corrected in place. `_ServingRuntime` now carries a
  required `observer_health` (`TerminalObserverHealthPublisher`) built on the same observer root and
  serving clock as the liveness sweeper — the lifespan PUBLISHES this serving lifetime's accumulator
  through it and the read routes resolve the persisted row through it, so the two halves of
  `LOCR-R17@v1` cannot drift onto different lifetimes or files. `stream_events` gained the matching
  optional keyword and passes it into `served_state_tail`, so the `snapshot` carries
  `terminalObserverHealth` while a `delta` (one projection node, not a state body) carries no tail.
  Recorded that these tail arguments are optional keywords whose absence is a valid served answer.
  Reference ranges re-derived against the candidate (`TerminalAttachTaskRequest` `286-291` →
  `300-304`) with two new rows. Verification metadata remains closeout-owned; no stamp advanced.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: documented the two task-execution registration collaborators. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `_app_common.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
