# mcp/src/agents_remember/install/experiment.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

Per-run experimental install selection, delivery decision, capability report and undo/run records. It does not install the removed Eve application or probe native adapter dependencies.

## Code Commentary

Selection remains request before process environment before unselected, never a persisted settings switch. Unselected delivery is legacy; selected-and-available is capsule; selected-and-unavailable is refused, never fallback. The actual capability probe is now only the blocking canonical-corpus-anchor file digest. ExperimentRunRecord reports resolved selection/source, instruction-source digest, mode/reason, corpus anchor and capabilities; removed application/dependency-install fields are absent. Normal runtime-install undo rows restore withheld coordinator startup targets via an unselected install and name no skill root, because that installer supplies no skill roots. The rollback formatter still accepts explicit `install_roots` and can render separately attributed old `skills_install` rows; this retained formatting branch does not expose or run the retired install operation. Installation mode and current host role launch are distinct owners.

## Evidence boundary

This account is current source interpretation only. It creates no executed test/host/bootstrap result and supplies no new CODE or MEMORY grade.

## Source-bound reference inputs

- [1]
- [2]
- [3]
- [4]
- [6]
- [7]
- Normal runtime undo restores startup targets; explicit install_roots can still produce separately attributed legacy formatting rows. [8]

## One delivery of the skill corpus

`WITHHELD_STARTUP_TARGETS` no longer names `skills/AGENTS.md`: the coordinator startup chain withheld in capsule mode is `AGENTS.md`, `system/AGENTS.md` and `tasks/AGENTS.md`. No skill tree is installed beside the runtime at all, so the packaged corpus the capsule compiler reaches through `application/skill_resources` → `packaged_source_root()/runtime/skills` is the one delivery, and the coordination root holds nothing that could stand in for it.

- The startup targets capsule mode withholds, which no longer include a skills instruction file. [9]
