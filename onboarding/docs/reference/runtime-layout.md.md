# docs/reference/runtime-layout.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

Reference inventory of the directories and files Agents Remember creates or manages on disk—under `<coordination-root>/`, in the Paseo host's XDG install and home folders, in per-role and `/var/tmp/agents-remember/` scratch folders, and at external config and handover-locator paths—together with `runtime_install`'s write, remove, and preserve rules.

## Code Commentary

- Maps `<coordination-root>/` scaffold folders and runtime-created paths (`logs/dashboard/`, `logs/observer/`, `runtime/servers/<pid>.json`, `runtime/knowledge-index/`, `controlplane/`, `temp/tool-reports/`).
- Documents `<home>/agents-remember/` host-home files including `role-agents.json`, `host-activity.json`, `provider-limits.json` (active limits, five-minute recheck attempts, and early clear release), and `turn-ends.jsonl`.
- Separates Worker/Reviewer/Curator enclosure scratch and report folders from non-leaf `<workspace-root>/.agents-remember/role-executions/<request-id>/`, `/var/tmp/agents-remember/` outside scratch, and `~/projects/.agents-remember/handover-locators/`.

## Relationships

- Complements `docs/tool-details.md` (`runtime_install` arguments and behavior) and `docs/reference/settings-json.md`.

## Evidence



- Coordination root scaffold and runtime-created dashboard, observer, server-registry, controlplane, and paseo-native-executions paths. [1]



- Host-home files under `<home>/agents-remember/` including `role-agents.json`, `host-activity.json`, and `provider-limits.json`. [2]
- Per-role scratch and report folders, `/var/tmp/agents-remember/` outside scratch, and handover-locator paths. [3]
