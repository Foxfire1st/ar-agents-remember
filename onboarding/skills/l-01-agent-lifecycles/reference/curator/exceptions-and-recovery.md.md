# skills/l-01-agent-lifecycles/reference/curator/exceptions-and-recovery.md

## Governing Overview

[overview](../../overview.md)

## Purpose

Tier-2 curation detail for Curators, Reviewers, and Managers covering report-only and foundation assignments, quality-check card cuts and external citations, dependent-document closeout checks, and memory-tool, code-concern, and sync-conflict recovery.

## Code Commentary

Covers four areas: report-only assignments (write only the report and upstream message, running no onboarding, index, quality, or coherence writes) and foundation-report contents; proving removed text untrue on every card cut (never cutting merely to clear a finding; linking `../review/rounds-and-late-findings.md` for `cutCards`/`addedFiles`) and citing external documents as `external` sidecar references named in `origin`; Manager closeout stale-dependent `knowledge_read(..., codeTreeId="working-tree", view="dependent", staleOnly=true)` verification and required curation report fields; and bounded encountered-memory repairs, continuing via other admitted memory tools when one fails, stops/unfinished turns/step marking, reporting rejected requirements as contradictions, sending evidenced code concerns to both Worker and Reviewer without editing code, and routing leaf memory-sync conflicts per `../worker/sync-and-repairs.md#synchronize-the-leaf`.

## Relationships

Linked from `roles/curator.md`, `operations/curation.md`, `operations/coordination.md`, and `reference/review/rounds-and-late-findings.md`. Registered in `composition-manifest.json` (`step_detail: true`), mirrored under `package_data/runtime/skills/`, and verified by `test_curator_instruction_wording_delivery.py` and `test_l84_unique_detail_pointers_rules.py`.

## Evidence

- Report-only assignments write only their report and upstream message without running onboarding, quality, or coherence writes; foundation reports enumerate examined/unexamined areas and outcomes. [1]
- Card cuts require source evidence proving removed text untrue, and external documents must be cited as `external` sidecar references named in `origin`. [2]
- Closeout dependent-document checks specify the exact `knowledge_read` working-tree stale-dependent call and recorded receipt fields; recovery rules bound tool failures, stops, code concerns, and sync conflicts. [3]
