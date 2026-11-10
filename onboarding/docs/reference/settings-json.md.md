# docs/reference/settings-json.md

## Governing Overview

[root repo overview](../../overview.md) — governed by the route-local [docs/reference overview](overview.md).

## Purpose

The public settings reference states five distinct homes and their read cadences: boot infrastructure in the MCP authority file; host runtime (`paseoRuntime`) in that same active MCP authority file selected by the server's absolute `--config`; memory topology under the memory root; global/repository-local agentic settings in the user configuration file and an optional repo-local override; and provider lifecycle settings derived from authority configuration. The user's `settings.json` is neither an MCP authority file nor an implicit provider settings source; the MCP authority file lives beside it as `agents-remember-settings.json` unless `--config` selects another.

The current page moves `paseoRuntime` out of `~/.config/agents-remember/settings.json` and into the authority file, states that the one Bootstrap call creates an absent block once and preserves an existing block unchanged while maintenance only reports the absent state, warns that concurrent writers of the host authority file are unsupported, and drops the optional `harnessSkillRoot` setting because skills are served as MCP resources with no installed harness skill root to configure. The agentic interview keeps its global file and repo-local override.

Documents landing.commitCheckTimeoutSeconds: positive integer, default 900, reread per landing; timeout refuses.

## Current source account

The user file is installed read-only and its folder closed to new/removed entries. Opening them for editing and closing them again are explicit user operations; the product does not relax permissions by itself. The product writes it only through `user_settings_init`, which exclusively creates an absent file with mode 600 and preserves an existing one, and the explicit upgrade-user-settings move; neither opens permissions. server_info reads live modes and reports exact-path edit/close commands without changing any file byte or permission. The reference spells those commands for XDG_CONFIG_HOME and quoted paths, not a grant to a role agent.

Paseo runtime is one shared per-use configuration, with no fallback to old per-harness blocks. Missing runtime and unknown keys have named refusal behavior. Each launcher view and start asks the host for current catalog parts. A failed part may use its timestamped last successful answer from the shared disk store; without either answer the configured choice is sent unchecked. Choice IDs or labels match without case, including host-supplied speed labels. The pending launcher displays saved choices but Start waits for fresh options; creation refreshes metadata and asks only for the chosen model's features. Role and per-level knobs merge at field granularity, with retained source/provider/model provenance; unknown settings and conflicting effective speed aliases are not silently normalized into authority.

Legacy retirement, launchArgs/promptKeywords/sessionCommands, native command/model/effort delivery fields, agentNotifier/supervisor/expectations, and concurrency limits remain accepted only where the reference says so, but are unread or unenforced and reported by server_info. The removed supervisor has no current redelivery budget, cadence, escalation ladder or emergency setting taught by this card. Caller spend overrides, current host role settings and unused compatibility fields are distinct surfaces; no removed spawn tool or adapter command is restored.

The document is guidance, not parser execution, proof of real permission protection, live host launch, installation or settings mutation. The memory example names memory-repo storage; old internal/external-memory examples and supervisor operational advice are withdrawn from this live owner's account.

## Current scoped contract

The role settings reference now documents a single user-owned `stepUp` alternative. Worker tries are failed recorded code rounds; Curator tries are failed recorded memory rounds. Rechecking the same candidate does not add a try. Automatic selection occurs on the next start at the configured positive threshold, while a one-sentence explicit request selects the same alternative. Catalog validation precedes idle-seat retirement; active turns and permission prompts refuse. Neither UI nor call arguments gain mode/permission authority, omitted foreign-scope choices use identified host defaults, and the task decision retains the step-up without resetting review limits or sealed findings. Removing the alternative affects a later start, not the running actor. This describes the new recorded-memory-lane design after landing; underway reviews are not migrated or backfilled.

## Evidence


Historical source account (detached from live reference 4; docs/reference/settings-json.md blob 6d8cc9b75acea207484aeaf2f87c0e5cafd6640e):

- Five settings homes/cadences, exact user-owned open/close commands and nonmutating live-mode reporting are declared by the current reference.

- The reference states five settings homes/cadences, explicit user-owned open/close commands and nonmutating exact-path mode reporting; role agents do not acquire user-settings write authority.



Historical source account (detached from live reference 5; docs/reference/settings-json.md blob 6d8cc9b75acea207484aeaf2f87c0e5cafd6640e):

- The complete reference separates current host role/features from accepted-but-unused retired settings and product answer authority.

- The reference distinguishes per-use host/role choices and permission authority from retained accepted-but-unread settings. Its new receipt-scope and same-tool correct-input canonical-amendment passages preserve permission, read/check/validation/sync and transaction stops.



No external Domain Documentation source or fresh executed acceptance is inferred.



Historical source account (detached from live reference 6; docs/reference/settings-json.md blob 6d8cc9b75acea207484aeaf2f87c0e5cafd6640e):

- The new roles table/paragraphs document one user-layer, nonnested stepUp alternative, default positive afterTries=3 only for Worker/Curator, code versus memory recorded-round tries, record-only nontries and exact-key refusals. The next start validates catalog choices before normal idle-seat retirement; active turn/prompt refuses. Explicit step_up reason/UI Step up use the same alternative without adding permission authority. Cross-harness/model omissions use identified host defaults, durable decisions retain task choice, and reviewer limits/findings do not reset. Removing the alternative changes the next start, not the running actor.

- The user-owned nonnested stepUp alternative defaults afterTries to three only for Worker/Curator recorded code/memory rounds; record-only repeats do not count. Next-start validation and idle replacement preserve permission, host-default provenance, task decisions and review limits; removing it affects later starts only.




Historical source account (detached from live reference 7; docs/reference/settings-json.md blob 6d8cc9b75acea207484aeaf2f87c0e5cafd6640e):

- The same `orchestration.roles` family admits the non-seat capability id `review-presenter`: every rule above validates its row, it is never dispatchable as a lifecycle seat, and it applies `harness`, `model`, `effort`, `mode`, `serviceTier`, `featureValues` and `notes` through the native launch. A row naming `stepUp` alone refuses that capability's launch by name because it owns no seat replacement ladder.

- The same role-settings family admits review-presenter as a validated non-seat capability; native launch uses its configured choices, but a stepUp-only capability row refuses because it has no seat-replacement ladder.



**L184 — NEW-R192-EXTRA-ARGS.** This is the document that states what the settings file's keys mean, so a new key has to be described here rather than inferred from code. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

- The reference states five settings homes/cadences, explicit user-owned open/close commands and nonmutating exact-path mode reporting; role agents do not acquire user-settings write authority. [4]

- The reference distinguishes per-use host/role choices and permission authority from retained accepted-but-unread settings. Its correct-input canonical-amendment passage keeps read/check/validation/sync refusals, starts, product guards and commit gates as stops, and when no admitted route works the write is made openly by hand and logged. [5]

- The user-owned nonnested stepUp alternative defaults afterTries to three only for Worker/Curator recorded code/memory rounds; record-only repeats do not count. Next-start validation and idle replacement preserve permission, host-default provenance, task decisions and review limits; removing it affects later starts only. [6]
- The same role-settings family admits review-presenter as a validated non-seat capability; native launch uses its configured choices, but a stepUp-only capability row refuses because it has no seat-replacement ladder. [7]
