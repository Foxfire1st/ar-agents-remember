# mcp/src/agents_remember/kernel/harnesses.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

The built-in agent-ID vocabulary for role settings. `HARNESS_IDS` is the ordered tuple
`claude`, `codex`, `pi`, `eve`; this module defines no `Harness` object, availability probe,
PATH detector, adapter registry or launch implementation. A named ID is not evidence that the
host offers or can run it.

## Code Commentary

The source docstring states that spawn harness validation combines these IDs with IDs declared
under orchestration.harnesses. A role with no named agent chooses the first offered ID in this
order; actual offerings remain the host's answer. Preserve the vocabulary row for `eve` without
restoring its retired runtime/probe machinery.

### Invariants And Boundaries

Settings vocabulary, host availability and launch capability are different owners. No readiness
verdict or execution proof is provided by this constant. The prior registry/probe account is
retired source history, not a compatibility path.

## Evidence

- Ordered built-in role-setting IDs do not establish host availability or restore a probe/adapter registry. [1]
