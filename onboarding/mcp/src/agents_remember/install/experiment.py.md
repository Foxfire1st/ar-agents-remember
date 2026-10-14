# mcp/src/agents_remember/install/experiment.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

Per-run experimental install selection, delivery decision, capability report and undo/run records. It does not install the removed Eve application or probe native adapter dependencies.

## Code Commentary

Selection remains request before process environment before unselected, never a persisted settings switch. Unselected delivery is legacy; selected-and-available is capsule; selected-and-unavailable is refused, never fallback. The actual capability probe is now only the blocking canonical-corpus-anchor file digest. ExperimentRunRecord reports resolved selection/source, instruction-source digest, mode/reason, corpus anchor and capabilities; removed application/dependency-install fields are absent. Undo rows restore withheld coordinator startup targets via an unselected install and name skill roots only when that separate install populated them. Installation mode and current host role launch are distinct owners.

## Evidence boundary

This account is current source interpretation only. It creates no executed test/host/bootstrap result and supplies no new CODE or MEMORY grade.

## Source-bound reference inputs

- [1]
- [2]
- [3]
- [4]
- [6]
- [7]
- [8]
