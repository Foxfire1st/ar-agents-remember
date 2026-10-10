# dashboard/src/dev/DocumentChatHarness.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

DEV-only harness for the MIK-R121 cross-workspace chat repair rig (`/dev/document-chat-host`).
It renders the real `DocumentChat` against stubbed role-launch answers and a document switcher,
so the R1 browser spec can select the master and the task and watch the shared frame follow.
Never shipped: `App` loads `DevApp` only under `import.meta.env.DEV`.

## Code Commentary

`DocumentChatHarness` installs the fetch stub once and renders the real document chat for the
switched document: Projects (no ref), Master and Task refs feed `DocumentChat` with the shared
`sprint/master/leaf` fixtures. `installFetchStub` answers the frame-descriptor and document-chats
HTTP calls with a fixed two-workspace agent table and passes everything else to native fetch, so
the chat under test resolves agents exactly as the stubbed backend states them.

## Invariants And Boundaries

DEV-only test rig for the MIK-R121 repair; it carries no product contract. The stubbed agents
are fixed literals (`agent-architect`/`agent-manager` in `wks_projects`, `agent-worker`/
`agent-curator` in `wks_leaf`).

## Evidence

- The harness renders the real document chat for the switched Projects/Master/Task document. [1]
- The fetch stub answers frame and document-chats calls with the fixed agent table. [2]
