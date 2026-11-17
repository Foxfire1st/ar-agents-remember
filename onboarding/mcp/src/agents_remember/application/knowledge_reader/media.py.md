# mcp/src/agents_remember/application/knowledge_reader/media.py

## Governing Overview

[overview](../overview.md)

## Purpose

Resolves knowledge-code media against the selected memory and code trees.

## Code Commentary

The reader resolves its selected pair and code blob before constructing a media source. Historical media uses that selected blob rather than the current checkout's file or symlink state. Fixed served types and byte bounds remain the shared media reader's responsibility.

## Relationships

The knowledge route accepts the knowledge reader's selected commit under its separate selection contract. Other file and change-set bytes routes keep their server-resolved selector rules.

## Evidence

- Resolves knowledge-code media against the selected memory and code trees. [1]
