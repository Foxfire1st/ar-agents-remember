# dashboard/src/cockpit/paseoFrameModel.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The pure model validates configured frame descriptors, native execution targets and normalized plugin messages.

## Code Commentary

Available descriptors require an http(s) serving origin and server ID. Only native paseo-agent host fields provide targets, and rejected receipts provide none. URLs encode agent/workspace identities. The descriptor carries the backend's provisioning command, with an explicit command-template notice when an older backend supplies none.

Source-tagged messages keep ready/pong capability lists, navigated, on-chat, shown, load-failed, native selection and source-scoped Parent errors distinct. Capability absence means an older plugin, not inability to open agents: only an explicit list without open-agent requests URL navigation. The notice names missing abilities and provisioning, and warns when an older plugin ends the waiting line before drawing. Request wait text distinguishes host lookup, application drawing and the legacy undifferentiated chat wait; a late answer says it is slow, not gone.

## Invariants And Boundaries

Native web route spellings are version-sensitive. Parsing cannot establish channel origin/window trust or task acceptance. The dashboard no longer reads a hierarchy snapshot; whether the plugin still posts one is settled by MIK-R95.

## Evidence

These pure-model contracts do not establish channel trust, native runtime success or task acceptance.

- Only a non-rejected native hosted execution supplies the agent target. [1]
- Only source-tagged supported control message shapes are normalized. [2]
- Missing capability declarations retain message opening; only an explicit lack of open-agent disables it. [3]
- A deficient plugin is named with the provision command and any early-drawing boundary. [4]
- Late requests remain waiting rather than being described as a dead channel. [5]
