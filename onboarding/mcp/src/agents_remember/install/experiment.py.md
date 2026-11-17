# mcp/src/agents_remember/install/experiment.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Per-run experimental install selection, delivery decision, capability report and run record. It does not install an application or probe native adapter dependencies.

## Code Commentary

Selection remains request before process environment before unselected, never a persisted settings switch. Unselected delivery is legacy; selected-and-available is capsule; selected-and-unavailable is refused, never fallback. The delivery mode does not decide what the installer writes: every accepted install removes the three retired coordinator startup files, and no mode installs or restores them. The actual capability probe is only the blocking canonical-corpus-anchor file digest. ExperimentRunRecord reports resolved selection/source, instruction-source digest, mode/reason, corpus anchor and capabilities. The module renders no undo rows; the install payload's `rollback` list is always empty. Installation mode and current host role launch are distinct owners.

## Evidence boundary

This account is current source interpretation only. It creates no executed test/host/bootstrap result and supplies no new CODE or MEMORY grade.

## One delivery of the skill corpus

Every accepted install removes `AGENTS.md`, `system/AGENTS.md` and `tasks/AGENTS.md` from the coordination root; `WITHHELD_STARTUP_TARGETS` is the same tuple, named in the experiment report. No skill tree is installed beside the runtime at all, so the packaged corpus the capsule compiler reaches through `application/skill_resources` → `packaged_source_root()/runtime/skills` is the one delivery, and the coordination root holds nothing that could stand in for it.



## Evidence

### Source-bound reference inputs

- Anchor: Per-run selection and unknown-id refusal. [1]
- Anchor: Explicit unselected install value. [2]
- Anchor: Selected-but-unavailable remains refused, never a legacy fallback. [3]




- Anchor: Actual retained run-record fields and their resolved inputs. [7]

- The experiment payload reports the withheld targets and an empty rollback list. [10]

### Repo-Internal References (continued)



- The three coordinator startup files every accepted install removes; the withheld name is the same tuple, kept for the experiment report. [4]

- The startup targets reported as withheld are the retired targets removed by every accepted install. [9]

### Repo-Internal References (renewed)

- Only the canonical corpus-anchor capability is probed; a missing anchor names `from the source checkout, run mcp/.venv/bin/python scripts/renew-instructions.py` as its remedy. [6]
