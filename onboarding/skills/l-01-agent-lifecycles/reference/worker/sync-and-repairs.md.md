# skills/l-01-agent-lifecycles/reference/worker/sync-and-repairs.md

## Governing Overview

[overview](../../overview.md)

## Purpose

Tier-2 worker and coordination detail governing `worktree_sync` clean, overlapping, and memory-conflict paths, focused test selection and freeze-report details, worker stops, repair limits, post-PASS final-check failures, measurement and refused handovers, and out-of-scope weakness and dependent-document recording.

## Code Commentary

Covers eight sections: `#synchronize-the-leaf` distinguishing clean sync (focused tests plus Manager report plus Curator refreshed dependent read, no Reviewer round), overlapping or failing sync (one Reviewer look at the repair), and native memory-file conflicts (`sync-resolution-required`, `memory-sync-choice-required`, `sync-active`: Curator repairs content only, Manager stages, Worker calls `worktree_sync(..., resolution_action="continue")`); focused test search, whole-tree collection before removals or renames, and freeze-report fields (`senderLine` ID, evidence-item mapping); worker stops, unfinished-turn notices, and step marking; three-repair stop, generalizing persistent failures, costly small repairs (~1h, second round, or second freeze), and record-only repairs; post-PASS final-check failures sealed via post-seal route 3; measurement handovers (no review freeze); refused handovers (direct send on Manager occasion, pending-retry for failed Manager notices); and recording out-of-scope weaknesses and dependent documents via `templates/curator-handoff-list.md`.

## Relationships

Target of all three Family-3 `refusal_references.py` pointers (`#synchronize-the-leaf`). Absorbs retired `coord-topic-worker-map-evidence-to-report-files.md` (verified by `test_l84_unique_detail_pointers_rules.py`) and checked by `test_lifecycle_turn_truth_handovers.py` and `test_role_instruction_corpus_policies.py`. Registered in `composition-manifest.json` (`step_detail: true`), mirrored under `package_data/runtime/skills/`, and links `../review/rounds-and-late-findings.md` and `../../templates/curator-handoff-list.md`.

## Evidence

- `#synchronize-the-leaf` splits clean sync, overlapping/failing sync, and native memory-file conflicts across Worker, Curator (content-only), and Manager (staging/transaction). [1]
- Focused test selection, freeze-report evidence mapping, stop rules, three-repair stop, persistent-failure generalization, costly-repair reporting, and post-PASS final-check handling define Worker execution bounds. [2]
- Measurement handovers, refused-handover reporting/retries, and out-of-scope weakness/dependent-document recording bind handoff routes to `curator-handoff-list.md`. [3]
