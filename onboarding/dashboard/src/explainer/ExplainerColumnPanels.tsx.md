# dashboard/src/explainer/ExplainerColumnPanels.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The column's sub-blocks: the header with the task's chats, the placeholder, the build's step list and Retire's confirmation.

## Code Commentary

- Each block draws what the column's state already holds and calls back for the one act it offers; none of them reads the server or posts.
- The header names the explainer and its task, shows the phase's own status word, offers ✦ Explain always and Retire chat only while a seat exists.
- The agent menu lists the explainer first, marks the row being shown, and says no chat of the task is live when it has no rows.
- The build panel marks each step done, running or waiting, gives a step that counts files or bytes its own percentage, and keeps the request visible as waiting to go out.
- A failed build names its step and reason and says the request stays for a new Send; Retire's confirmation names what ends and what stays before a danger-coloured confirm.

## Evidence

- The header's status word, ✦ Explain and the Retire offer follow the phase and the seat [1]
- The placeholder fixes the role, names the settings role and offers no Start control [2]
- The build panel states the whole percentage, each step's own mark and count, and a failure's reason and step [3]


