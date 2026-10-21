# dashboard/src/tray/shownChat.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Stores the chat target published by a visible column, plus its active page/repository, for first-pick targeting.

## Code Commentary

### Logic

Visible page owners publish chat/page context and clear only their own contribution on cleanup; undefined repository updates preserve the existing repository.

### Invariants And Boundaries

This store does not verify native drawing. Each column owns what it publishes and takes back only its own chat on cleanup; null is the published absence of a chat. This module does not read native plural selection. The first-pick policy lives in the store/model.

## Evidence

- Stores published chat, page and repository values without verifying native drawing. [1]
- A column publishes its chat and clears only its own contribution on cleanup. [2]
- Page/repository publication retains an existing repository for undefined input and lets the visible File Viewer name its own repository. [3]
