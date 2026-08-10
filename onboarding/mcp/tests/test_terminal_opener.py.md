# mcp/tests/test_terminal_opener.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/tests/test_terminal_opener.py`               |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`        |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

`test_terminal_opener.py` covers the shared hosted-session opener (`serving.terminal_opener`) — the
ONE spawn path both the dashboard `POST /api/terminal/{session}` route and the agent-facing
`spawn_agent_session` MCP tool compose over cit:([`open_terminal_session`], mcp/src/agents_remember/serving/terminal_opener.py:680-732) cit:(["def _open_terminal_response("], mcp/src/agents_remember/serving/_app_terminal_routes.py:224-224) cit:([`spawn_agent_session_tool`], mcp/src/agents_remember/application/terminal_tools.py:769-842). It drives `open_terminal_session` against a fake host
(records the `ensure` call, no real tmux) + a real JSON catalog, pinning the leaf-claim / provenance /
env-seed behaviour both call paths inherit — and, since 260703-L16, the per-harness knob→argv
application (`KnobApplicationTests`).

## Code Commentary

### 260714-ACPUI-L2 Opener Carriage Boundary

The opener tests now assert carriage, not static vendor mapping. A Claude or Codex
`ResolvedLaunch` enters the encoded runner payload unchanged while `argv` retains only the base
command plus user-authored launch arguments; adapter preparation owns native flags and Codex
thread configuration. No model/effort value is synthesized into `sessionCommands`. The environment
still records resolved spend provenance, and settings-defined custom harnesses are opened without
guessing a native mapping at this generic boundary.

### 260714-ACPUI-L4 Live Launch Truth

L4 pins reopen behavior to the process that actually exists. An identical selected pair returns the
unchanged durable row and makes no second `ensure` call. A different pair or launch identity against
the same live process returns `launch-conflict`, preserves the original command/pair/endpoint, and
does not mutate the catalog. Once the process is dead, the same catalog id may start a fresh
generation with the newly selected pair, new creation time and endpoint, `starting` control state,
and no stale process-specific raw/session evidence.

The concurrent different-pair case drives two opener calls through the catalog transaction fence.
Exactly one wins `opened`, the other receives `launch-conflict`, the host creates one process, and
both results agree with the one durable catalog row. The role-based worker/reviewer/curator/manager
coverage remains on this same opener, so dashboard and `spawn_agent_session` cannot diverge into
parallel launch paths.

### 260713-PHA-L1 control metadata coverage

The opener tests now prove an unregistered harness is persisted and returned as explicit
`unsupported` control state with protocol metadata, and that a supplied private endpoint is retained
on re-open. This is additive catalog behavior; no pane or log fallback is accepted.

### 260707-HFX2-L16 Multi-Role Pipeline And Replacement Proof

The opener suite now places worker, reviewer, curator, and manager on one canonical leaf, refuses a
live same-role duplicate, replaces a dead worker without ceremony, and opens curator after worker
completion without suffix hacks. It also checks persisted binding role in opener results.

### Logic

The historical L15 env-to-TUI flag expectation was superseded by ACPUI-L2. Current Codex coverage
asserts the selection is structured inside `RunnerConfig`; the opener does not synthesize a TUI
`--model` or effort config override.

`OpenTerminalSessionTests` drives `open_terminal_session` with a `_FakeHost` (records `ensure`'s sid /
cwd / command / env, adds the tmux name to a known set) + a real `TerminalCatalog` over a temp dir + a
`_detected` `which`. The cases:

- **opened** (`test_opened_records_provenance_env_and_leaf`, cit:([`test_opened_records_provenance_env_and_leaf`], mcp/tests/test_terminal_opener.py:174-209)): the result is `opened`, the catalog row
  carries the leaf, the spawned-by session/lifecycle, the harness, and the `spawn_role` read
  from the env's `AR_SPAWN_ROLE`; the knob env was seeded into the
  detached tmux spawn; and the provenance survives the catalog camelCase round-trip
  (`spawnedBySession` / `spawnedByLifecycle` / `spawnRole`).
- **role preservation** (`test_reopen_preserves_spawn_role_and_hand_open_records_none`, cit:([`test_reopen_preserves_spawn_role_and_hand_open_records_none`], mcp/tests/test_terminal_opener.py:295-308)): a
  role-less re-open keeps the recorded `spawn_role` (write-once, like the spawned-by pair), and a
  hand-opened session (no env role) records `None` with `spawnRole` absent from its JSON.

`KnobApplicationTests` now pin opener-side carriage. A typed Claude or Codex selection round-trips
inside `RunnerConfig`; the ensured command remains the base argv plus explicit `launch_args`, and
the resolved env keeps riding as provenance. Normalized effort never becomes a session command.
Free-form provenance (`launch_args`/`prompt_keywords`/`session_commands`) remains on the catalog
row and survives JSON/re-open behavior. An injected effective registry still resolves a
settings-defined harness without guessing native knob mapping, while an unknown-everywhere id
refuses pointing at `orchestration.harnesses` and the harness manual.
- **leaf-taken** (`test_leaf_taken_surfaces_owner_without_spawning`): a running chat already owning the
  leaf makes the opener return `leaf-taken` with the owner and never spawn or upsert the intruder.
- **bad kind** (`test_bad_kind_reports_detail`): an unknown launch kind returns `bad-kind` with a detail
  and no ensure.
- **undetected harness** (`test_undetected_harness_is_bad_kind`): an undetected harness (`which`
  returning `None`) also resolves to `bad-kind` with no ensure.

### Conventions

`unittest` + `tempfile` + the `sys.path` insertion idiom. The `_FakeHost` duck-types `TerminalHost`
(only `has_session` + `ensure`), and `_running_chat` seeds a running harness catalog row with
deterministic timestamps. `open_terminal_session` is called through a `_open` helper that fills the
required kwargs.

### Invariants And Boundaries

- No real tmux — the fake host records the `ensure` call and the catalog is a plain JSON store.
- `leaf-taken` / `bad-kind` must not spawn or upsert; the tests assert `host.ensured == []` and no
  intruder row.
- Provenance must survive the catalog JSON round-trip (migration-safe camelCase keys).
- A live process owns immutable command, model/effort, creation, and endpoint truth. Same-pair
  reopen is idempotent; a changed pair/identity conflicts without mutation or a second process.
- Dead replacement starts a fresh control generation and must not inherit process-specific control
  session or raw evidence.
- The catalog batch spans read, liveness probe, ensure, and upsert so concurrent callers publish one
  process and one catalog truth.
- Role-based spawn and the daemon route both compose this opener; tests must not create or imply a
  second launch path.

### Todos

No known follow-up in this file.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## 260718-CHATS-L5I Current Delta

Opener regressions now assert that a runner inherits the daemon worktree package root, preventing tmux-server environment leakage from selecting stale checkout code.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## 260731-EFA-L2 Delta — reopen conflicts and dead pre-bridge rows

- A live reopen from **another workspace root** conflicts on cwd, and one whose resolved launch
  names **another harness** conflicts too: a row is only reusable when both its location and its
  harness still agree with the request.
- A dead pre-bridge row is replaced by a **controlled spawn** rather than being reattached to.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
2026-08-04T13:47:55+02:00 — 260731-EFA-L6 S18-B11 same-reviewer correction: recorded that two prose citations were converted and seven rangeless internal rows were deleted; no deleted row was retained as anchored evidence. Verification metadata unchanged.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata pinned until closeout stamps the code commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented same-pair idempotent reopen,
  changed-pair/identity conflict without mutation, fresh dead replacement, concurrent one-process /
  one-catalog truth, the batch fence, and preservation of the role-based shared opener path; also
  corrected the superseded Codex TUI-argv statement. Body verified against the uncommitted L4
  candidate; verification metadata remains pinned to the latest committed source revision until
  closeout.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented typed launch carriage, unchanged
  base argv, adapter-owned native application, provenance env, no effort paste, and the custom
  harness boundary; corrected the governing overview backlink. Verification metadata remains
  pinned until closeout stamps the L2 code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 closeout remediation: documented unsupported-adapter,
  protocol, endpoint, and re-open preservation coverage.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added the workaround-museum multi-role, same-role,
  dead-replacement, and no-suffix pipeline regressions.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: replaced env-only Codex expectations with explicit
  argv and covered the new opener provenance fields. Verification metadata remains pinned until
  closeout stamps the eventual L15 code commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): added `KnobApplicationTests` —
  env-knob→argv flag mapping (env still riding), session-vocabulary effort off the flag, the
  pre-spawn refusal naming both value sets, env-only mapping-less builtins, verbatim `launch_args`,
  free-form provenance recording/round-trip/preservation, effective-registry resolution of
  settings-defined harnesses, the unknown-everywhere manual-pointing refusal, and the vocab-less
  settings-harness guidance refusal. Existing opener tests unmodified. Verification metadata pinned
  until closeout stamps the L16 commit.

- 2026-07-06T23:58:54+02:00 — 260703-L14 (visual hierarchy + chat grouping): the opened case now seeds
  `AR_SPAWN_ROLE` and asserts it lands on the row + round-trips as `spawnRole`; added
  `test_reopen_preserves_spawn_role_and_hand_open_records_none` (write-once role across a role-less
  re-open; hand-opened rows record none).
  Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-04T11:10+02:00 — L2: created coverage for the shared `open_terminal_session` opener —
  opened+provenance+env-seed+leaf, leaf-taken-surfaces-owner-without-spawning, bad-kind, and
  undetected-harness — against a fake host + real JSON catalog. Verification metadata pinned until
  closeout stamps the L2 commit.
