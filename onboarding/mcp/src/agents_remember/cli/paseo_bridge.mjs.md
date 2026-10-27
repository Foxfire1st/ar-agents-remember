# mcp/src/agents_remember/cli/paseo_bridge.mjs

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

The native Paseo bridge module the runtime serves.

## Code Commentary

agent-cancel validates agentId/requestId, finds only that id, cancels it and re-reads it. agentState includes provider, lastUserMessageAt and lastStatus; absent activeTurn is null rather than false. The removed review-presenter Claude-only fence is replaced by server-surface enforcement, not a new native harness fence.

The bridge module carries native host integration loaded beside the runtime. A provider catalog row that is still loading retains available `modes`, `defaultModeId` and `fetchedAt` from the discovered provider entry; missing modes are marked by `modeError`, and unanswered models are omitted with a loading error rather than represented as a successful empty list. Pending model listing does not discard mode offerings the host has already supplied. `closingText` concatenates the final trailing assistant messages, trims the assembled text and exposes the whole nonempty reply with `textTruncated: false`; it imposes no role-message character cut. The delivery policy layer owns settings-bound reply text and complete reply-file storage. The earlier retirement changed no bridge part; that historical observation is not a claim that this later reply transport changed nothing.

`host-activity-snapshot` delegates to `daemon.invokePluginRpc("ar-plugin", "ar.host-activity-snapshot", {})` and returns the configured server identity plus the plugin publication. It is the full-host reconciliation RPC, not the bounded `agents-live` discovery census; a bridge answer is not evidence that role facts were consumed.

`agents-live` reads unarchived agent IDs through `daemon.fetchAgents`, at most ten pages of 200 entries. It reports `complete` only when the runtime explicitly says `hasMore: false`; a bound or missing next cursor ends the read without establishing absence. It neither resumes agents nor reads their timelines. Whole-reply transport remains separately owned by `closingText`.

`workspace-open` dispatches to `paseo_workspaces.mjs`, which owns task workspace keys, archive-successor traversal and placement. The bridge imports its unchanged text-validation and typed-failure helpers from `paseo_bridge_primitives.mjs`; provider/model resolution, agent creation, live-agent listing and reply transport retain their own owners. Extraction does not move actors or change launch permission policy.

The header documents `presenter-transcript` as a read of up to 200 timeline entries and `presenter-cancel` as cancellation of the named presenter. These commands remain separate from AR role execution; this header change adds no command implementation.

`agent-send` validates optional image and text-attachment lists through `sendExtras` before reading the recipient or attempting delivery. Nonempty extras accompany the same native send and preserve its existing message ID and steer behavior. Absent, null or empty lists add no options. A malformed entry refuses the whole payload before recipient lookup; the bridge does not send a partial list. The attachment helper owns individual image/text schemas, while recipient state checks and delivery outcomes remain here.


**L184 — NEW-LIMIT-FROM-REPORT-ONLY.** This bridge is the one process that takes the plugin's answer and then asks it for the list, so the number has to be carried here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Fresh catalog and creation choices

`readCatalog` supports full, metadata and selected-feature questions. Only explicit refresh rescans providers; ordinary questions still read their current offerings. `creationFeatureValues` checks configured feature values when an answer is available, matching IDs before labels without case through `namedOption`. A failed, timed-out or malformed feature listing passes configured values through unchecked; a known-empty offering refuses them.

## Evidence


## Current contract evidence

- The native bridge returns the assembled whole final reply without a character cut; the separate delivery policy owns truncation and filing. [1]

- `agents-live` reads unarchived agent IDs through `daemon.fetchAgents`, at most ten pages of 200 entries. It reports `complete` only when the runtime explicitly says `hasMore: false`; a bound or missing next cursor ends the read without establishing absence. It neither resumes agents nor reads their timelines. Whole-reply transport remains separately owned by `closingText`. [2]

- A still-loading provider retains discovered modes/default mode/fetched time; missing modes and unanswered models remain unknown rather than successful empty lists. Catalog discovery keeps enabled provider identities at the deadline instead of treating still-loading models as a whole-catalog timeout. [3]

- The command table delegates workspace-open to the imported workspace owner while retaining the bridge command surface. [4]


- `agentCreation` no longer imposes the old Claude-only review-presenter fence or injects `tools: ''` / `strict-mcp-config`. The settings role uses the normal harness launch; the product confines its own bound tool server at registration and dispatch. Retained `presenter-transcript` and `presenter-cancel` remain legacy presenter operations, while `agent-cancel` targets the exact explainer seat and request. [5]


- Optional image/text lists are validated before recipient lookup and accompany the same native send without changing steering or plain-message options. [6]


- agent-cancel validates agentId/requestId, finds only that id, cancels it and re-reads it. agentState includes provider, lastUserMessageAt and lastStatus; absent activeTurn is null rather than false. The removed review-presenter Claude-only fence is replaced by server-surface enforcement, not a new native harness fence. The native state response includes provider and last-message/status fields, and distinguishes absent activeTurn from false by reporting null. [7]
