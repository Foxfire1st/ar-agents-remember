# docs/reference/harnesses.md

## Governing Overview

[root repo overview](../../overview.md) — governed by the route-local [docs/reference overview](overview.md).

## Purpose

Explains host-owned agent kinds and the settings-owned role and per-level knobs. The manual no longer teaches AR native adapters, provider protocol negotiation or terminal spawning.

## Current source account

- The host catalog determines agent availability, models and efforts; the built-in table supplies ordered IDs, not executables or model enums.
- A role names its agent kind as harness; a start names it as agent. Additional orchestration.harnesses entries add IDs. Legacy command, argv and native model/effort delivery fields remain accepted but unread, and server_info reports held unused keys.
- Role and per-level settings deep-merge at field granularity, with repository level, global level, repository role and global role precedence. Legacy launchArgs, sessionCommands and promptKeywords remain accepted but unread.
- Current settings core retains distinct repository-local and user settings path authorities. This card grants no settings write, restart or provider acceptance.

## Evidence

The registered source inventory supplies no external Domain Documentation authority. These are statically inspected current source facts, not new execution or CODE grades.


- Current settings core deep-merges per-level role knobs over flat defaults and keeps repository-local versus user settings path boundaries. [1]
