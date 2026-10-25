# mcp/tests/test_knowledge_read_boundary.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds MIK-R74 rule 6 over every read the product registers: a read changes no branch, tag or HEAD, no worktree
file, no Git index, and files nothing — except the cache it is allowed to write. The cases are grouped by the
surface a caller reaches (tool reads, enclosure reads, dashboard GETs, skill reads), and the harness is proved
non-vacuous by a read that is made to mutate.

## Code Commentary

### Logic

`tool_world()` builds a real world and `_read_tool()` calls a registered read; `_context()` supplies the
memory-backed context a read needs. Each case compares the protected Git and filesystem state before and after
the call.

- **The harness has teeth.** `test_a_mutated_read_is_caught` makes a read create a directory and requires the
  comparison to fail.
- **Tool reads.** `test_every_registered_read_leaves_nothing_but_cache` covers knowledge read, diff,
  integrity and the published-intent block.
- **Enclosure reads.** `test_enclosure_reads_record_only_comparisons_and_previews` and
  `test_adopted_seat_status_preview_and_dry_runs` cover review, status, preview, integrate and reopen dry
  runs; `test_remaining_preview_plan_and_queue_reads_write_nothing` adds the carryover plan and queue status.
- **Dashboard GETs.** `test_review_get_routes_read_without_writing` serves the review and its summary for
  real, and `test_remaining_dashboard_gets_read_without_writing` covers files, notes and the changeset diff.
- **Memory-backed reads.** `test_memory_backed_reads_write_nothing` keeps the context packet, internal drift
  and baseline status on the selected memory-backed seat, including `ok=False` and `state="legacy-format"` for
  an unconverted baseline; `test_converted_drift_check_read_writes_nothing` and
  `test_converted_adopt_dry_run_writes_nothing` cover the converted format.
- **Bounded freshness.** `test_context_packet_freshness_fetch_is_bounded` keeps freshness opt-in: without it
  nothing changes, with it only the fetch.
- **Skill reads.** `test_diagnostic_watcher_and_skill_reads_write_nothing` keeps the catalog list, the
  advertised-URI read and a bogus-URI refusal on the untouched fixture.
- **Description-called reads.** `test_miscellaneous_description_called_reads_write_nothing` keeps server info,
  the resolver and file calls preserving the synthetic seat, with `resolve_context` not called.

### Conventions

Every case asserts on the whole protected footprint — refs, index, worktree bytes and the non-`.git` tree —
rather than on a single file, so a read that files something anywhere is caught.

### Invariants And Boundaries

- A read's only permitted write is its cache.
- A refusal is asserted by its exact returned code where the surface returns one, not by a raised exception.

## Evidence


- Selected knowledge reads, refusals, diff, integrity and published intent leave only the allowed footprint. [1]

- A mutated read is caught, so the roster cannot pass vacuously. [2]
- Enclosure reads attribute comparison objects and allow only preview effects. [3]

- Review GET routes read without other protected-state changes. [4]

- Remaining dashboard GETs read without writing. [5]
- Converted drift and registered baseline status use the filing oracle. [6]
- Context-packet, internal drift and baseline-status paths preserve the selected memory-backed seat, including `ok=False` and `state="legacy-format"`. [8]
- Skill catalog list, advertised-URI read and bogus-URI refusal preserve the fixture. [9]
- Baseline adoption dry run preserves the converted fixture. [10]

- Freshness is opt-in: no unrequested fetch, and a requested fetch changes only its bounded Git footprint. [11]

- Adopted-seat status, preview, integrate and reopen dry runs respect the preview allowance. [12]

- Remaining preview, carryover and queue paths answer or name their refusals without landing or protected-state mutation. [13]


- Two formerly raised boundary cases assert their exact returned refusal codes, while unrelated authority and queue errors still raise. [15]

- Server-info, gate and file calls preserve the synthetic seat; `resolve_context` is not called and file inputs do not prove successful naming. [16]
- The summary port accepts `_number`, and all three GETs retain the before-and-after oracle. [17]


- Current source declarations support the qualified naming or fixture account; no executed test or acceptance is inferred — mcp/tests/test_knowledge_read_boundary.py:1-1037. [14]
