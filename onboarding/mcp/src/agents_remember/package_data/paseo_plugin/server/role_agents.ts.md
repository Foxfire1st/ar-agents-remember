# Published role-agent facts reader

## Governing Overview

[Plugin overview](../overview.md)

## Purpose

Read the product's per-role-agent facts for event-driven silent-turn notifications. Role start publishes `{role, task, reportPath}` keyed by native agent id; this reader never infers those facts from agent titles or source directories.

## Contract And Boundaries

`PASEO_HOME` locates `agents-remember/role-agents.json`. Missing/empty home or ENOENT returns an empty record set; malformed present JSON, malformed agents and non-string facts fail visibly. The accepted result copies only role, task and reportPath. The plugin reads it fresh for each turn end, while other event state stays in the in-memory tracker. This module starts no polling, publishes no facts and does not identify or replace a parent.

## Evidence

- Absent configuration/file yields no records, while malformed present facts throw; each read reconstructs the typed fact set. [1]
