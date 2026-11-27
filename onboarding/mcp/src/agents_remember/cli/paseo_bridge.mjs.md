# mcp/src/agents_remember/cli/paseo_bridge.mjs

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

The native Paseo bridge module the runtime serves.

## Code Commentary

agent-cancel validates agentId/requestId, finds only that id, cancels it and re-reads it. agentState includes provider, lastUserMessageAt and lastStatus; absent activeTurn is null rather than false. `agentCreation` adds no Claude-only fence for a review presenter and injects no tool restriction of its own; tool limits reach a seat only through the provider options its settings name.

The bridge module carries native host integration loaded beside the runtime. A provider catalog row that is still loading retains available `modes`, `defaultModeId` and `fetchedAt` from the discovered provider entry; missing modes are marked by `modeError`, and unanswered models are omitted with a loading error rather than represented as a successful empty list. Pending model listing does not discard mode offerings the host has already supplied. `closingText` concatenates the final trailing assistant messages, trims the assembled text and exposes the whole nonempty reply with `textTruncated: false`; it imposes no role-message character cut. The delivery policy layer owns settings-bound reply text and complete reply-file storage.

`host-activity-snapshot` delegates to `daemon.invokePluginRpc("ar-plugin", "ar.host-activity-snapshot", {})` and returns the configured server identity plus the plugin publication. It is the full-host reconciliation RPC. Its follow-up requests subagents for recorded AR role seats with open, unarchived sessions. That lookup includes background seats when it lists agents. The bounded `agents-live` discovery census has a separate caller contract. A bridge answer is not evidence that role facts were consumed.

`agents-live` reads unarchived agent IDs through `daemon.fetchAgents`, at most ten pages of 200 entries. The request includes background agents. It reports `complete` only when the runtime explicitly says `hasMore: false`; a bound or missing next cursor ends the read without establishing absence. It neither resumes agents nor reads their timelines. Whole-reply transport remains separately owned by `closingText`.

`workspace-open` dispatches to `paseo_workspaces.mjs`, which owns task workspace keys, archive-successor traversal and placement. The bridge imports its text-validation and typed-failure helpers from `paseo_bridge_primitives.mjs`; provider/model resolution, agent creation, live-agent listing and reply transport retain their own owners.

The header documents `presenter-transcript` as a read of up to 200 timeline entries and `presenter-cancel` as cancellation of the named presenter. These commands remain separate from AR role execution.

`agent-send` validates optional image and text-attachment lists through `sendExtras` before reading the recipient or attempting delivery. Nonempty extras accompany the same native send and preserve its existing message ID and steer behavior. Absent, null or empty lists add no options. A malformed entry refuses the whole payload before recipient lookup; the bridge does not send a partial list. The attachment helper owns individual image/text schemas, while recipient state checks and delivery outcomes remain here.


`usage-reports` dispatches to `paseo_usage_reports.mjs`, which owns the read, the sixty-second leaf refresh and the shared forced refresh; the bridge returns that module's answer unchanged. The command surface remains in the bridge, while the request shape and the cached-entry rules belong to the extracted reader.

## Fresh catalog and creation choices

`readCatalog` defaults to metadata, which lists enabled provider and model choices without feature queries and returns a launcher-scoped `daemonConfig` projection (via `catalogConfiguration` and `catalogProviderSettings`, carrying `agentProfiles` and per-provider `options` or `params` with `extraArgs` and `supportsMcpServers` while excluding provider `env` maps) or an explicit `daemonConfigError` (with missing config still producing `'The runtime supplied no configuration'` on both `daemonConfigError` and provider `toolServerError`) from the same `api.config.get()` read. Selected mode reads features for one specified provider and model. Explicit Refresh renews the provider snapshot before querying its current offerings. During saved native Antigravity Retry, the bridge looks up the exact recorded agent. It can deliver the saved first message to that agent. A missing agent produces a typed refusal before creation. `creationFeatureValues` checks configured feature values when an answer is available, matching IDs before labels without case through `namedOption`. A failed, timed-out or malformed feature listing passes configured values through unchecked; a known-empty offering refuses them. `agentCreation` accepts optional booleans `skipToolServerWait` and `allowMissingParent` (refusing non-boolean values with `invalid_bridge_payload`). `sendFirstMessage` skips the 6-second `toolServerStart()` (`TOOL_SERVER_START_MS`) startup wait when `skipToolServerWait` is true because launch confirmation has already verified the bound task server. When `allowMissingParent` is true (used by deferred held-seat opens), `createAgent` checks whether `parentAgentId` is absent or archived before calling `create` and omits `parentAgentId` in that case (also retrying once without `parentAgentId` if `create` fails while `includeParent` was true and the new agent was not created).

`role-registry` dispatches to `readRoleRegistry` for unarchived history or exact canonical UUID reads. The exact result distinguishes a positive archive timestamp and a successful null; the dedicated reader carries completeness and daemon identity.

## Evidence


## Current contract evidence

- The native bridge returns the assembled whole final reply without a character cut; the separate delivery policy owns truncation and filing. [1]


- `agents-live` requests background agents, retains unarchived IDs and reports a complete census only after the host explicitly ends the listing. [2]



- A provider still loading at the discovery deadline keeps its identity and any known modes and fetch time. An unanswered model or mode listing remains unknown. [3]




- The command table delegates workspace-open to the imported workspace owner while retaining the bridge command surface. [4]







- Optional image/text lists are validated before recipient lookup and accompany the same native send without changing steering or plain-message options. [6]

- `agent-cancel` acts on the identified agent and returns its re-read state. The state reports provider, last user-message time and last status. Absent active-turn state is null. [7]

- `agentCreation` uses the selected settings role and supplies its applied options (plus `allowMissingParent` handling in `createAgent`). The bound tool server registers the general tools and four explainer tools, and checks the launched seat on calls to those four. [5]


- The host-activity reconciliation opts into background agents and asks only open, unarchived AR role seats for subagents. [8]

- An ordinary usage read names the agent. A forced refresh for a stale leaf report names its report ID alone. [9]




- The bridge dispatches role-registry to its dedicated history and exact-read helper. [10]


- `agentCreation` validates optional boolean `skipToolServerWait` and `sendFirstMessage` skips the 6 s `toolServerStart()` wait when `skipToolServerWait` is true. \[11] [11]
