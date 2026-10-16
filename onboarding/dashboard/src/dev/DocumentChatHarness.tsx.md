# dashboard/src/dev/DocumentChatHarness.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

DEV-only harness for the MIK-R121/R122 browser rigs (`/dev/document-chat-host`).
It renders the real Operations right rail (`RightRail`: the rail toggle plus EventRiver /
`DocumentChat`) against stubbed role-launch answers and a document switcher, so a spec can
walk the rail toggle and the document selection — master, task, agentless ghost — and watch
the single shared frame follow.
Never shipped: `App` loads `DevApp` only under `import.meta.env.DEV`.

## Code Commentary

`DocumentChatHarness` installs the fetch stub once and renders the real right rail for the
switched document: Projects (no ref), Master, Task and the agentless ghost refs feed `RightRail`
with native TaskEntry `sprint/master/leaf` fixtures and exact references, and rail-toggle buttons walk river and chat.
`installFetchStub` answers the frame-descriptor and document-chats
HTTP calls with a fixed two-workspace agent table and passes everything else to native fetch, so
the chat under test resolves agents exactly as the stubbed backend states them.

## Invariants And Boundaries

DEV-only test rig for the MIK-R121 repair and the MIK-R122 walk; it carries no product contract. The stubbed agents
are fixed literals (`agent-architect`/`agent-manager` in `wks_projects`, `agent-worker`/
`agent-curator` in `wks_leaf`).

## Evidence

- The harness renders the real right rail for the switched Projects/Master/Task/ghost document with river/chat toggle buttons. [1]

- The fetch stub answers frame and document-chats calls with the fixed agent table. [2]
