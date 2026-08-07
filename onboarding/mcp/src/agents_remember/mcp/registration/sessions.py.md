# mcp/src/agents_remember/mcp/registration/sessions.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/registration/sessions.py`       |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-07-31T15:31+02:00                                       |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                   |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## Purpose

`register_session_tools(server, config)` declares the hosted agent-session family:
`attach_terminal_session_to_leaf`, `spawn_agent_session`, `hosted_session_readiness`,
`session_retire`, `session_rename`.

## Code Commentary

### Logic

`spawn_agent_session` is the reason this module exists as its own family and the clearest case of
the route's contract. Its sixteen flat parameters are the published schema every dispatching agent
and every `l-01` skill calls with; the body sorts them into the three parameter objects
`spawn_agent_session_payload` takes:

- `SpawnSeat` — what the caller may declare: `kind`, `leaf_key`, `replacement_for_leaf`, `level`,
  `label`, `env` (the seat's `AR_SPAWN_ROLE` rides here).
- `RetiredSpawnInputs` — what the caller may no longer declare: `context`/`submit` (the retired
  one-call brief) plus `harness`, `model`, `effort`, `launch_args`, `prompt_keywords`,
  `session_commands`. These are still **accepted** so a non-`None` value can be refused loudly
  (`brief-delivery-separate`, `spend-override-unsupported`) before any settings, catalog, or
  terminal side effect. Removing them from the signature would turn a named refusal into an
  unknown-argument error.
- `SpawnedBy` — `spawned_by_session` / `spawned_by_lifecycle`, recorded on the catalog row so the
  dashboard can draw the orchestration tree.

The docstring is the full public contract: status `spawned-unbriefed` on success; the pre-spawn
refusals (`brief-delivery-separate`, `spend-override-unsupported`, `harness-unknown`,
`harness-not-detected`, `effort-invalid`, `model-invalid`, `launch-selection-invalid`,
`level-invalid`, `bad-kind`); the settings-only knob chain (`orchestration.rolesPerLevel[level]`
deep-merged over flat `orchestration.roles`, falling through to `orchestration.spawn.harness` and
then the first detected registry harness); and the separation of brief delivery — the caller must
obtain `hosted_session_readiness(...)=ready` and post one exact-agent durable `dispatch-brief`.

The other four forward their arguments as keywords:

- `attach_terminal_session_to_leaf(session_id, leaf_key, role?)` — moves one existing session;
  returns `attached` / `leaf-taken` / `unknown-session`; needs no worktree enclosure.
- `hosted_session_readiness(session_id, wait_seconds=0.0)` — read-only; exact catalog identity plus
  the protocol adapter snapshot. Pane text, copy mode and log timing are explicitly not authority.
  It never sends input, and the wait is finite (60 s maximum, enforced downstream).
- `session_retire(actor_session_id, session_id, reason)` — `actor_session_id` is the retiring seat's
  own id, self-declared; there is no ambient "who am I" resolution anywhere in this codebase. The
  docstring is the model-visible statement of the authority policy (never self-retire; a manager may
  retire only worker/reviewer seats of its OWN master; the orchestrator may retire any seat) and the
  status vocabulary (`retired`, `already-retired`, `unknown-session`, `unknown-actor`,
  `retire-refused`).
- `session_rename(session_id, label)` — identity text only; the spawned role never changes, and the
  FIRST rename freezes the original spawn-time label into provenance.

### Invariants And Boundaries

- Keep the retired spawn inputs in the signature. They exist to be refused; deleting them changes a
  named, guided refusal into a schema error.
- Do not collapse `spawn_agent_session`'s parameters into `SpawnSeat` at the signature. The
  parameter objects belong on the payload-builder side of the boundary, which is exactly where this
  body puts them.
- Authority (retire policy, spend-override refusal, leaf-claim arbitration) is enforced in
  `mcp/tools/terminal.py` and the `serving/` layer, never here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The payload builders and the `SpawnSeat`/`RetiredSpawnInputs`/`SpawnedBy` definitions. | `spawn_agent_session_payload` | mcp/src/agents_remember/mcp/tools/terminal.py:46-63 |
| The readiness builder and its finite-wait bound. | `hosted_session_readiness_payload` | mcp/src/agents_remember/mcp/tools/hosted_readiness.py:13-30 |
| Each argument lands in exactly one of the three spawn groups. | `RegistrationWiringTests` | mcp/tests/test_mcp_registration_wiring.py:61-116 |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the bare-`*` keyword-only signature remediation (PLR0917). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 6 citation findings; scoped check passed.

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The five session
  declarations moved out of `server.py`; `spawn_agent_session` now packs its arguments into
  `SpawnSeat` / `RetiredSpawnInputs` / `SpawnedBy` in the body while the published flat signature is
  unchanged. Verification metadata pinned to the pre-change commit until closeout stamps the L2 code
  commit.
