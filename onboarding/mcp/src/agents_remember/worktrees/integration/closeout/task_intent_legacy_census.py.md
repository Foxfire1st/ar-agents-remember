# mcp/src/agents_remember/worktrees/integration/closeout/task_intent_legacy_census.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/worktrees/integration/closeout/task_intent_legacy_census.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-03T12:30:00+02:00                  |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00                  |
| governingOverview      | `overview.md`                             |

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Deterministic census for the bounded `task-intent/v1` legacy decoder (CCR-R02@v2). It counts
current live containers per owning record class that still lack canonical task intent, classifies
unreadable/malformed rows as bounded problems, and refuses removal of the compatibility decoder
until every enumerated class is readable with zero legacy rows. Immutable historical generations
are deliberately excluded.

## Code Commentary

### Logic

- `LegacyIntentRecordClass` (line 14) names the four owning classes
  (`route-review`, `curator-coherence`, `closeout-door`, `lifecycle-operation`) and
  `LEGACY_INTENT_RECORD_CLASSES` (line 20) fixes their exact tuple; the census validates that its
  rows enumerate every class exactly once (`_classes_are_exact`, line 45).
- `TaskIntentLegacyCensus` (line 40) carries per-class `scanned`/`missingIntent` counts and a
  bounded `unreadable` list (16 MiB file cap, 10,000 problem cap); `remaining` (line 52) sums
  the legacy rows.
- `task_intent_legacy_census` (line 61) runs the four scanners: route reviews inside live task
  documents (`_scan_route_reviews`, line 101), curator-coherence authorities plus their confined
  record paths (`_scan_curator_coherence`, line 120), closeout doors read from the
  `closeout_door:` front-matter cell of every `series-contract.md` (`_scan_closeout_doors`,
  line 157), and schema-3.0 `closeout`/`direct-landing` operation records under
  `worktrees/` (`_scan_lifecycle_operations`, line 187).
- `_count_intent` (line 213) counts a row as missing when `taskIntent` is absent or exactly
  `{"state": "missing-intent"}`, and records `task-intent-invalid` for any other malformed
  value; `TaskIntentIdentity.model_validate` is the validator.
- `require_task_intent_decoder_removal` (line 88) raises `TaskIntentLegacyCensusError` while any
  row is unreadable or any current row lacks intent, so the compatibility decoder is removed only
  at a proven zero population.

### Conventions

The scan counts only live/current containers; historical generations and archives are not evidence
of remaining legacy state. Path confinement (task-root-relative, non-symlink sub-task refs) keeps
the census from reading outside its own tree.

### Invariants And Boundaries

- The sentinel `missing-intent` remains absence: it can never satisfy currentness or acceptance,
  and no census row can mint a digest for it.
- Unreadable or unclassified records block decoder removal rather than being guessed.
- The decoder is removed when every class reaches zero; it is not an open-ended dual reader.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty; no external documentation claim is made.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact owning record-class enumeration. | `LEGACY_INTENT_RECORD_CLASSES` | mcp/src/agents_remember/worktrees/integration/closeout/task_intent_legacy_census.py:20-25 |
| The census model with bounded unreadable rows and zero-population proof. | `TaskIntentLegacyCensus`; `remaining` | mcp/src/agents_remember/worktrees/integration/closeout/task_intent_legacy_census.py:40-54 |
| The four live-container scanners and the per-row intent classifier. | `task_intent_legacy_census`; `_count_intent` | mcp/src/agents_remember/worktrees/integration/closeout/task_intent_legacy_census.py:61-85; mcp/src/agents_remember/worktrees/integration/closeout/task_intent_legacy_census.py:213-230 |
| The removal refusal until readable zero population. | `require_task_intent_decoder_removal` | mcp/src/agents_remember/worktrees/integration/closeout/task_intent_legacy_census.py:88-98 |
| The validator shared for current rows. | `TaskIntentIdentity` | mcp/src/agents_remember/models/task_intent/__init__.py:55-59 |

## CCR-R02@v2 Legacy Cutover

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, only the legacy persisted-record
decoder/currentness boundary may materialize a typed `missing-intent` sentinel, and the
compatibility decoder is removed when a deterministic census reaches zero across every owning
record class. This module implements that census and removal gate for the landed L25 candidate
(`99dc249b`).

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  created this card for the new legacy task-intent census (`task_intent_legacy_census`,
  `require_task_intent_decoder_removal`, the four scanning owners, bounded-problem handling);
  documented the zero-population decoder-removal gate and the exclusion of historical generations.
  Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.
