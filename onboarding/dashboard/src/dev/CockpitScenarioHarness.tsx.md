# dashboard/src/dev/CockpitScenarioHarness.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Provides the dev-only authority boundary around one real Chats cockpit scenario. It installs fake
HTTP authority before descendant polling, waits for the keyed prior shell's passive cleanup, resets
all transient state, and only then mounts the successor shell and mock PTY transport.

## Code Commentary

`CockpitScenarioHarness` installs transport in a layout effect and performs reset/readiness in a
passive effect so old descendants cannot race the new fixture. `CockpitScenarioExitBoundary` applies
the same post-unmount reset when returning to ordinary Engine Room scenarios without retaining fake
HTTP authority. Socket behavior can be live or deliberately dropped and omits irrelevant xterm banner
output in cockpit scenarios.

## Invariants And Boundaries

DEV-only; it wraps the real `CockpitShell` rather than a private UI. Readiness must remain false until
the old authority is revoked and all transient/module registries have been cleared.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

No configured Domain Documentation source exists for this file.

### Cross-Repo References

The harness composes repository-local stores, scenario fixtures, and the real CockpitShell; no external fixture framework is an implementation authority.

No applicable cross-repository source was found.

### Repo-Internal References

- Scenario facts, reset, and fake fetch installer. [1]
- Bench mounts `CockpitScenarioHarness` and wraps the shell in `CockpitScenarioExitBoundary`. [2]
