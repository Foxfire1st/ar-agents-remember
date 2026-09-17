# mcp/src/agents_remember/serving/launch_capsule.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/launch_capsule.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T09:05+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l15-ar` uncommitted source (17 dirty paths); base `15fa0e2c0bb91d5bb1b2abf4ee8eb54916bd5ed4` |
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

**The one place a launch decides what instructions it carries, and the single workspace rule that
follows from that decision.** `260915-CAPS-L15` added it to connect the severed capsule chain: the
compiler (L2), the admission/MCP surface (L4), the Codex instruction seam (L5) and the eve carrier (L7)
were each individually proven, and **no production launch point supplied a capsule to any session** —
a dispatched seat and a free agent both launched with no instructions at all.

The module owns exactly two things:

1. the **decision** — for one launch, one of `capsule` / `legacy` / `refused`, with the reason carried
   in the value rather than implied by an absent field; and
2. the **workspace rule** — a launch whose capsule admits a workspace runs *there*, so the session cwd,
   the settings selection and the child's `AR_WORKSPACE_ROOT` are one value instead of three that have
   to agree.

It is `serving`-rank (17) and therefore **may not import `application`** (21): the compile crosses an
injected port (`LaunchCapsuleResolver`), filled at the composition root. The *decision* stays here, so
every launch point answers "capsule, legacy or refused" identically and only one place decides it.

## Code Commentary

### Logic

**Three modes, and only three.** `LaunchCapsuleMode` is `capsule` | `legacy` | `refused`. `LaunchCapsule`
is the resolved value: the two harness carriers the master already built (`codex_delivery` for Codex's
app-server instruction field, `eve_env` for eve's launch environment — a launch sets whichever belongs
to the harness it is about to start and never both), the admitted `session_workspace`, and a compact
`report` published on the launch's own result so a run's instruction mode is readable afterwards
instead of inferred from an empty field. `explain()` is the one operator-facing line naming what was
selected or why it refused.

**`resolve_launch_capsule(resolver, request)` is the whole decision tree**, in this order:

| Condition | Answer |
| --- | --- |
| no role, or role in `LEGACY_SESSION_ROLES` (`chat`, `terminal`) | `legacy`, reason named — the identity-free launcher, or a seat that is deliberately not an agent |
| role is neither a frozen capsule role nor a declared legacy seat | **`refused`** (`role-not-capsule-addressable`) — never a quiet legacy launch |
| harness blank, or not in `CAPSULE_CARRIER_HARNESSES` (`codex`, `eve`) | `legacy` **by declared decision**, naming the harness and the two channels that exist |
| `resolver is None` (process composed without the port) | **`refused`** (`capsule-resolver-unavailable`) |
| role-configured seat on a carrier-bearing harness | the port compiles it, or the launch takes the compiler's own status and remedy |

`legacy_launch_capsule` **raises on a blank reason**: a legacy declaration must name why, so "no capsule"
is a recorded decision at every launch rather than a default nobody chose. `LAUNCH_OPERATION` is
`orientation` — not a new selection rule, but the default the registered `role_capsule_compile`
operation already declares.

**The workspace rule, stated once.** `session_workspace(capsule, server_workspace=…)` returns the
capsule's admitted workspace when it has one, otherwise the server's workspace. Only an eve carrier
admits a workspace: its runtime re-verifies per request that it runs in the admitted git worktree, so
the value is part of the artifact's validity rather than a detail beside it. The Codex instruction
carrier has no workspace concept at all, so it carries `None` and no Codex launch's cwd moves.
`selection_for_workspace(selection, workspace=…)` then moves **only** `ResolvedLaunch.workspace` (a
`replace` over the frozen dataclass) — the harness, model and effort the settings chose are untouched,
and a selection already naming that workspace is returned unchanged.

**Why `eve_binding_env()` exists.** It reads the three environment names out of the carrier module the
runtime's loader reads them from, so the writer (`terminal_opener._eve_capsule_env`) and the reader
(`eve_runtime_launch.launch_spec_binding`) cannot drift into two spellings of the same binding.

### Conventions

- **The opener performs; the launch point decides.** No opener derives a capsule. The decision lives
  here and the resolved value is passed onto the launch request.
- Mode/reason vocabulary is lowercase and wire-visible: `report` is published verbatim as
  `instructionMode` on both launch surfaces, so a rename is a transport change.
- Rank comments (`layers.toml` 17 vs 21) are the module's reason to exist; the port is the same shape
  `register_inbox_execution_evidence` already uses.

### Invariants And Boundaries

- **One decision point.** A second place that decides a mode is the severed chain again, one level up.
  Every launch point passes the resolved value; none re-derives it.
- **A refusal a caller can ignore is not a refusal.** All three launch points resolve *before* any host
  side effect, and `terminal_opener.open_terminal_session` refuses a refusal defensively as well, so a
  caller that bypassed the gate still cannot start a role-configured session with no instructions.
- **`legacy` is always a declared decision with a reason.** `legacy_launch_capsule` raises on a blank
  reason, and the one production launch point left on the legacy chain
  (`serving/conversation/library/open_service.py`) carries `LIBRARY_REOPEN_LEGACY_REASON` explicitly.
- **One workspace authority.** The value is read back out of the carrier the consumer re-verifies, so
  the cwd, the selection and `AR_WORKSPACE_ROOT` cannot disagree by construction. The runner itself
  refuses a selection whose workspace differs from the cwd
  (`serving/harness_control_runner.py:175`), which is the product-side second axis of the same rule.
- **This module carries no instruction prose and compiles nothing.** It consumes a value the
  `application` tier produced.
- **A harness with no verified channel is legacy by this master's own declaration**, recorded with its
  reason — not a gap this module papers over. `claude`, `pi` and settings-defined ids are all in that
  class until a cutover leaf gives one a channel.

### Todos

None known for this module. The two open limitations around the paths it wires are recorded, owned and
**not repaired here**:

- **An eve seat still cannot be *dispatched*** through the settings chain, for an inherited reason in a
  downstream gate (`application/terminal_tools.py::_resolve_harness_dispatch` requires model **and**
  effort, while eve's honest capability catalogue advertises no launch-settable effort — defect
  **D22**). The capsule gate passes and the next refusal is that inherited one. Owner: the leaf the
  developer's route-(A) ruling created (**L17**), recorded in `notes/product-defects-observed.md`.
- **The dashboard route cannot start the *shipped* eve row** (it does not set
  `TerminalLaunchRequest.session_backend`, so the harness is checked as a PATH program). Pre-existing,
  measured by this leaf, owner **L17**.

## Docs References

No Domain Documentation source is configured in the resolved source registry for this pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The operation a launch compiles, and the two role sets that decide the first branch of the gate. | `LAUNCH_OPERATION`; `LEGACY_SESSION_ROLES` | mcp/src/agents_remember/serving/launch_capsule.py:43-43; mcp/src/agents_remember/serving/launch_capsule.py:52-58 |
| The two harnesses with a verified channel, and why every other harness is legacy by declaration. | `CAPSULE_CARRIER_HARNESSES` | mcp/src/agents_remember/serving/launch_capsule.py:60-70 |
| The three modes, the resolved value's carriers and its admitted workspace, and the operator-facing explanation. | `LaunchCapsuleMode`; `LaunchCapsule`; `LaunchCapsule.explain` | mcp/src/agents_remember/serving/launch_capsule.py:73-80; mcp/src/agents_remember/serving/launch_capsule.py:108-159 |
| The request the launch point fills from values it already holds; `is_role_configured` is the frozen-vocabulary membership test. | `LaunchCapsuleRequest`; `LaunchCapsuleRequest.is_role_configured` | mcp/src/agents_remember/serving/launch_capsule.py:82-106; mcp/src/agents_remember/serving/launch_capsule.py:97-100 |
| The one workspace rule and the selection rule that follows it. | `session_workspace`; `selection_for_workspace` | mcp/src/agents_remember/serving/launch_capsule.py:166-176; mcp/src/agents_remember/serving/launch_capsule.py:179-192 |
| The declared-legacy constructor refuses a blank reason, so "no capsule" always names why. | `legacy_launch_capsule` | mcp/src/agents_remember/serving/launch_capsule.py:195-208 |
| The fail-closed answer for a role-configured seat whose capsule cannot be supplied. | `refused_launch_capsule` | mcp/src/agents_remember/serving/launch_capsule.py:216-231 |
| The two reason functions: which role is a declared legacy seat, and which harness has no channel. | `legacy_seat_reason`; `capsule_channel_reason` | mcp/src/agents_remember/serving/launch_capsule.py:233-249; mcp/src/agents_remember/serving/launch_capsule.py:251-273 |
| The whole decision tree in one function, including the no-resolver refusal. | `resolve_launch_capsule` | mcp/src/agents_remember/serving/launch_capsule.py:275-314 |
| The port the serving launch points resolve through; the composition root fills it. | `LaunchCapsuleResolver` | mcp/src/agents_remember/serving/launch_capsule.py:162-163 |
| The application-tier implementation the port is bound to. | `compile_launch_capsule` | mcp/src/agents_remember/application/role_capsules/launch.py:273-295 |
| Both launch points resolve through this module before any host side effect. | `_spawn_launch_request`; `_open_terminal_response` | mcp/src/agents_remember/application/terminal_tools.py:740-787; mcp/src/agents_remember/serving/_app_terminal_routes.py:239-334 |
| The runner's own agreement check, which is the product-side second axis of the one-workspace rule. | `parse_runner_config` | mcp/src/agents_remember/serving/harness_control_runner.py:144-171 |
| The one launch point left on the legacy chain, with its named reason. | `LIBRARY_REOPEN_LEGACY_REASON` | mcp/src/agents_remember/serving/conversation/library/open_service.py:113-124 |
| The cases pinning the gate for every seat class, and the production-chain workspace agreement. | `test_the_mode_gate_names_capsule_legacy_and_refused_for_every_seat_class`; `test_the_spawn_launch_agrees_with_its_capsule_about_the_workspace` | mcp/tests/test_capsule_launch_wiring.py:615-657; mcp/tests/test_capsule_launch_wiring.py:874-918 |

## Cross-Repo References

No cross-repository implementation dependency governs this file. The eve carrier's environment names
are read from `models/eve_capsule_carrier.py`, which is in this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| The reader's own environment-name constants, which `eve_binding_env()` returns so writer and reader cannot drift. | `BINDING_REF_ENV`; `CAPSULE_PATH_ENV`; `CAPSULE_DIGEST_ENV` | mcp/src/agents_remember/models/eve_capsule_carrier.py:34-36 |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `parse_runner_config` repointed to mcp/src/agents_remember/serving/harness_control_runner.py:144-171. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T09:05+02:00 — 260915-CAPS-L15 curator: **created this card** (the census reported it
  missing, `integrity.missing_onboarding`). Records the module as the one place a launch decides its
  instruction mode and the one workspace rule that follows; the three-mode gate with its exact branch
  order; the blank-reason refusal that makes "no capsule" a recorded decision; the admitted-workspace
  read-back that makes cwd, settings selection and `AR_WORKSPACE_ROOT` one value by construction; the
  rank discipline that keeps the decision in `serving` and the compile behind a port; and the two
  limitations around the paths it wires that this leaf **reported rather than repaired** (D22, owner
  L17; the dashboard route's `session_backend` gap, owner L17). Verification metadata pins the leaf's
  base `15fa0e2c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real
  code commit and no hash or fingerprint was invented here.
