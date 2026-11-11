# docs/reference/settings-json.md

## Governing Overview

[root repo overview](../../overview.md) — governed by the route-local [docs/reference overview](overview.md).

## Purpose

The public settings reference states five distinct homes and their read cadences: boot infrastructure in the MCP authority file; host runtime (`paseoRuntime`) in that same active MCP authority file selected by the server's absolute `--config`; memory topology under the memory root; global/repository-local agentic settings in the user configuration file and an optional repo-local override; and provider lifecycle settings derived from authority configuration. The user's `settings.json` is neither an MCP authority file nor an implicit provider settings source; the MCP authority file lives beside it as `agents-remember-settings.json` unless `--config` selects another.

The page places `paseoRuntime` in the authority file, not in `~/.config/agents-remember/settings.json`, states that the one Bootstrap call creates an absent block once and preserves an existing block unchanged while maintenance only reports the absent state, warns that concurrent writers of the host authority file are unsupported, and names no `harnessSkillRoot` setting: skills are served as MCP resources, with no installed harness skill root to configure. The agentic interview keeps its global file and repo-local override.

Documents `orchestration.landing.commitCheckTimeoutSeconds`: a positive whole number, 900 where the settings name none, read again at each landing; a run past it is stopped and refuses the landing.

## Current source account

The user file is installed read-only and its folder closed to new/removed entries. Opening them for editing and closing them again are explicit user operations; the product does not relax permissions by itself. The product writes it only through `user_settings_init`, which exclusively creates an absent file with mode 600 and preserves an existing one, and the explicit upgrade-user-settings move; neither opens permissions. server_info reads live modes and reports exact-path edit/close commands without changing any file byte or permission. The reference spells those commands for XDG_CONFIG_HOME and quoted paths, not a grant to a role agent.

Paseo runtime is one shared per-use configuration, with no fallback to old per-harness blocks. Missing runtime and unknown keys have named refusal behavior. Each launcher view and start asks the host for current catalog parts. A failed part may use its timestamped last successful answer from the shared disk store; without either answer the configured choice is sent unchecked. Choice IDs or labels match without case, including host-supplied speed labels. The pending launcher displays saved choices but Start waits for fresh options; creation refreshes metadata and asks only for the chosen model's features. Role and per-level knobs merge at field granularity, with retained source/provider/model provenance; unknown settings and conflicting effective speed aliases are not silently normalized into authority.

Legacy retirement, launchArgs/promptKeywords/sessionCommands, native command/model/effort delivery fields, agentNotifier/supervisor/expectations, and concurrency limits remain accepted only where the reference says so, but are unread or unenforced and reported by server_info. The removed supervisor has no current redelivery budget, cadence, escalation ladder or emergency setting taught by this card. Caller spend overrides, current host role settings and unused compatibility fields are distinct surfaces; no removed spawn tool or adapter command is restored.

`provision` writes exactly the daemon settings the reference lists, each applied at start or live, and leaves every other key of the daemon's `config.json` alone. Among them `daemon.mcp.injectIntoAgents` and `agents.idleRuntimeCleanup` are written `false` and apply live: Paseo's own agent tools are off for every seat, and the host does not close an agent idle for 60 minutes (Paseo 0.14 and later would), because Agents Remember reads a closed seat as ended.

The document is guidance, not parser execution, proof of real permission protection, live host launch, installation or settings mutation. The memory example names memory-repo storage.

## Current scoped contract

The role settings reference documents a single user-owned `stepUp` alternative. Worker tries are failed recorded code rounds; Curator tries are failed recorded memory rounds. Rechecking the same candidate does not add a try. Automatic selection occurs on the next start at the configured positive threshold, while a one-sentence explicit request selects the same alternative. Catalog validation precedes idle-seat retirement; active turns and permission prompts refuse. Neither UI nor call arguments gain mode/permission authority, omitted foreign-scope choices use identified host defaults, and the task decision retains the step-up without resetting review limits or sealed findings. Removing the alternative affects a later start, not the running actor.

## Evidence

No external Domain Documentation source or fresh executed acceptance is inferred.

- `server_info` names a file or folder it finds open to writing under `openUserSettings`, with both commands written out for the exact path, and names nothing while both are closed. [4]

- The reference distinguishes per-use host/role choices and permission authority from retained accepted-but-unread settings. Its correct-input canonical-amendment passage keeps read/check/validation/sync refusals, starts, product guards and commit gates as stops, and when no admitted route works the write is made openly by hand and logged. [5]

- The user-owned nonnested stepUp alternative defaults afterTries to three only for Worker/Curator recorded code/memory rounds; record-only repeats do not count. Next-start validation and idle replacement preserve permission, host-default provenance, task decisions and review limits; removing it affects later starts only. [6]
- The same role-settings family admits review-presenter as a validated non-seat capability; native launch uses its configured choices, but a stepUp-only capability row refuses because it has no seat-replacement ladder. [7]
