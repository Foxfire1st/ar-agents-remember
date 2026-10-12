# mcp/tests/test_memory_mode_removal.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

The executable guard for the removal of the `internal` and `disabled` memory modes. `internal` — a repo-sidecar root — and `disabled` — a task running with no memory at all — are both gone (MIK-R50): a task in `disabled` can be neither closed out, synced, integrated nor landed, and where converted knowledge exists invariant work is mandatory (D5), so no task may opt out of memory. The supported set is `external` alone.

## Code Commentary

Three properties are pinned, each naming the failure it prevents. Refused by name: `internal` keeps `memory-mode-unsupported` while `disabled` is refused with `memory-opt-out-refused`, which names the true reason (converted knowledge where it exists, removal elsewhere) and the known action — answering `disabled` with the `internal` text would blame a memory root that was never the problem. Reported, not migrated: existing state recording a removed mode is named by artifact and left byte-identical, except a `disabled` contract stays readable where status, attach and guarded abandon need it. The supported set is untouched: `external` still resolves, writes and reads through the application layer and the CLI. The expected set is written literally (`EXPECTED_MODES = ("external",)`), never imported, so a vocabulary change must be made twice. The 44 function definitions (59 collected node IDs: 42 plain, 13 corrected-surface rows, 4 lookalike rows) cover vocabulary narrowers (unknown tokens stay ordinary invalid-argument errors), entry-point refusals, existing-state reporting, the still-readable `disabled` contract, operator reporting, flag narrowers distinguishing typos from removals, and the instruction-corpus plus onboarding-root-shape guards.

## Task-local direct fixture

The configuration helper emits no direct_execution setting. Direct cases seed the exact canonical leaf grant as isolated fixture data before invoking the route. This low-level seed is not authorized architect proof; the retained assertions concern memory-mode removal outcomes.

## Evidence

- Supported set is external alone; both removals named [20]
- Internal refused by name, disabled refused as an opt-out [21]
- Topology narrowers keep the same split [22]
- Start refuses a disabled mode as an opt-out [23]
- Contract writers refuse disabled as an opt-out [24]
- A disabled contract stays readable and byte-identical [25]
- Removed tokens refused while unknown tokens still degrade [26]
