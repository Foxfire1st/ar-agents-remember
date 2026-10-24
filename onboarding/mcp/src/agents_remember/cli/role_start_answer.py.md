# mcp/src/agents_remember/cli/role_start_answer.py

## Purpose

Build the role-start tool’s internal answer from its exact durable receipt. The start answer names the complete hand-over's path beside the text artifact's.

## Governing Overview

[MCP package overview](../../../overview.md)

## Current Contract

started_answer reads the receipt for the request’s canonical address and checks requestId. It maps saved execution status to running/held/rejected/unknown, retains report/assignment/preparation/choice fields and checks a stopped agent before treating it as running.

The answer appends step_up_note using the receipt’s observed model/source and carries stepUp metadata. A rejected receipt whose public projection says canRetry advises the same request, selection, reason and overrides; nonretryable rejection still advises a new request. Held seats need a first addressed message, not a second start.

This answer builder does not publish role facts: the obsolete post-answer plugin-publication call is gone. The receipt execution owner publishes receipt-bound identity through `role_activity` before launch/replay; that best-effort boundary is distinct from host execution and does not prove plugin consumption. This is the internal detailed answer consumed by downstream response shaping, not a promise that every field appears in compact delivered success. It does not compile instructions or decide task acceptance.

## Evidence

- Receipt identity, status, disclosure and conditional remedy all derive from saved state. [1]
- Public facade delegates to this extracted owner. [2]
- Registered tool test source requires same-request recovery text. [3]
- Ordinary rejection retains new-request advice. [4]


- On valid saved receipt context, role-facts publication belongs to pre-launch/replay and receipt-aware resume, not to the post-answer projection; filesystem/runtime publication is best effort, not host execution or plugin-consumption evidence. [5]

## The continuation a bootstrap answer names

For Bootstrap the answer independently adds the dashboard address result and the host chat route. `dashboardAddress` is published only when its origin answers and the dashboard owner's action is not `failed` (including a `lock-held`/skipped ensure result when the origin answers); running `nextAction` uses that dashboard address or names its failure. `chatAddress` is derived from the configured embed frame base URL, the bridge-reported server id and the receipt agent id; this path does not HTTP-probe the chat page and is not gated by the dashboard result. Identity and status still come from the saved receipt. This is the Architect-admitted distinction, not a rendered-page or native execution witness.

- The receipt-derived answer that adds the continuation for the free agent. [6]
- A bootstrap start answers with its seat and the place it is continued, and a dashboard that does not answer is reported instead of published. [7]

- Dashboard publication requires the owner/origin result; host chat independently derives its route from embed, reported server id and receipt agent id without an HTTP chat-page probe. [8]
