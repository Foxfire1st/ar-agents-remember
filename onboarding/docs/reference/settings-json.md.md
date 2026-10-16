# docs/reference/settings-json.md

## Governing Overview

[root repo overview](../../overview.md) — governed by the route-local [docs/reference overview](overview.md).

## Purpose

The public settings reference states five distinct homes and their read cadences: boot infrastructure in the MCP authority file; host runtime in the shared user configuration; memory topology under the memory root; global/repository-local agentic settings; and provider lifecycle settings derived from authority configuration. User configuration is neither an MCP authority file nor an implicit provider settings source.

Documents landing.commitCheckTimeoutSeconds: positive integer, default 900, reread per landing; timeout refuses.

## Current source account

The user file is installed read-only and its folder closed to new/removed entries. Opening them for editing and closing them again are explicit user operations; the product does not relax permissions by itself. The one product write is the explicit upgrade-user-settings move. server_info reads live modes and reports exact-path edit/close commands without changing any file byte or permission. The reference spells those commands for XDG_CONFIG_HOME and quoted paths, not a grant to a role agent.

Paseo runtime is one shared per-use configuration, with no fallback to old per-harness blocks. Missing runtime and unknown keys have named refusal behavior. Host catalog data supplies actual agent kinds, models, modes and features. Role and per-level knobs merge at field granularity, with retained source/provider/model provenance; unknown settings and conflicting effective speed aliases are not silently normalized into authority.

Legacy retirement, launchArgs/promptKeywords/sessionCommands, native command/model/effort delivery fields, agentNotifier/supervisor/expectations, and concurrency limits remain accepted only where the reference says so, but are unread or unenforced and reported by server_info. The removed supervisor has no current redelivery budget, cadence, escalation ladder or emergency setting taught by this card. Caller spend overrides, current host role settings and unused compatibility fields are distinct surfaces; no removed spawn tool or adapter command is restored.

The document is guidance, not parser execution, proof of real permission protection, live host launch, installation or settings mutation. The memory example names memory-repo storage; old internal/external-memory examples and supervisor operational advice are withdrawn from this live owner's account.

## Current scoped contract

The role settings reference now documents a single user-owned `stepUp` alternative. Worker tries are failed recorded code rounds; Curator tries are failed recorded memory rounds. Rechecking the same candidate does not add a try. Automatic selection occurs on the next start at the configured positive threshold, while a one-sentence explicit request selects the same alternative. Catalog validation precedes idle-seat retirement; active turns and permission prompts refuse. Neither UI nor call arguments gain mode/permission authority, omitted foreign-scope choices use identified host defaults, and the task decision retains the step-up without resetting review limits or sealed findings. Removing the alternative affects a later start, not the running actor. This describes the new recorded-memory-lane design after landing; underway reviews are not migrated or backfilled.

## Evidence

- Five settings homes/cadences, exact user-owned open/close commands and nonmutating live-mode reporting are declared by the current reference. [4]
- The complete reference separates current host role/features from accepted-but-unused retired settings and product answer authority. [5]

No external Domain Documentation source or fresh executed acceptance is inferred.


- The new roles table/paragraphs document one user-layer, nonnested stepUp alternative, default positive afterTries=3 only for Worker/Curator, code versus memory recorded-round tries, record-only nontries and exact-key refusals. The next start validates catalog choices before normal idle-seat retirement; active turn/prompt refuses. Explicit step_up reason/UI Step up use the same alternative without adding permission authority. Cross-harness/model omissions use identified host defaults, durable decisions retain task choice, and reviewer limits/findings do not reset. Removing the alternative changes the next start, not the running actor. [6]
