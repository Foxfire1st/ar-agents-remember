# skills/l-01-agent-lifecycles/reference/child-questions.md

## Governing Overview

[governing overview](../overview.md)

## Purpose

Owns the relay of child questions and developer answers across the existing parent route.

## Code Commentary

An answer within the receiver’s authority is labelled as that receiver’s answer. Questions beyond that authority retain the originating role, task and agent identity; the developer’s words and receiving-agent attribution pass unchanged on the return. Instruction changes use their owning task and publication route, and sender/receipt handling belongs to message-handover.md.

## Evidence

- The relay distinguishes the receiver’s answer from a developer ruling and preserves originating identity. [1]
- Instruction changes and permission handling retain their owning route and explicit boundaries. [2]
