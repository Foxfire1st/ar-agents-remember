# mcp/tests/test_curator_realization_authoring.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_curator_realization_authoring.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T17:09:54+02:00 |
| lastVerifiedCommitHash | `eda947325ccbe0791973953265278597e968a34a`|
| lastVerifiedCommitDate | 2026-09-28T18:11:05+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Unit-lane evidence for **per-target realization rationale and role** in the ordinary curator writer
(ICR-R20@v1, leaf `260921-ICR-L45`): every case drives the real `ingest_curator_list` over the sibling
module's real repository pair and reads the result back through the public invariant view or the stored
claim rows. It proves that each target stores its own authored explanation, that the entry-level
default is explicit and inherited only for what a target leaves unstated, that a missing, non-text,
unknown-role, over-long or placeholder-route value refuses only its own entry before anything is
written, that no rationale is generated, and that operations already committed (including ones the
base writer committed with no rationale) still replay and publish unchanged.

## Code Commentary

### Logic

- **Resolution.** `test_each_target_of_one_entry_stores_its_own_authored_rationale_and_role` (two
  targets, two distinct rationales/roles over an entry default) and
  `test_a_target_that_states_nothing_inherits_the_entry_level_default` (halves inherit independently).
- **Absence.** `test_a_target_with_no_rationale_refuses_its_entry_by_name_and_nothing_is_generated`:
  `realization_rationale_absent`, no journal key, no claim row, no generated sentence.
- **Replay.** `test_an_exact_replay_of_per_target_rationale_is_idempotent_and_a_changed_one_is_refused`
  (byte-identical rows and journal; a reworded rationale is `allocation_content_conflict`) and
  `test_a_claim_holding_the_old_generated_sentence_reads_back_exactly_as_stored` (history untouched;
  `GENERATED_BEFORE` is the old sentence as stored rows hold it).
- **Value rules.** `test_a_value_that_is_not_text_an_unknown_role_or_an_over_long_rationale_refuses_its_own_entry`
  (`realization_value_not_text`, `realization_role_unknown` — `"absent"` as a role included —
  `realization_rationale_too_long`; the sibling entry commits),
  `test_the_word_absent_as_a_governing_route_is_refused_and_an_omitted_route_stays_ungoverned`,
  `test_a_governing_route_that_is_not_text_is_refused_where_it_is_written` and
  `test_the_word_absent_is_refused_as_a_governing_route_in_any_case_once_trimmed`.
- **Committed-allocation exemption.** `test_an_operation_the_base_writer_committed_without_rationale_replays_and_publishes`
  runs the **real base writer**: the `base_writer` fixture `git archive`s `BASE_COMMIT`'s `mcp/src`
  and runs it in a child interpreter; it skips with a stated reason when that commit is not in the
  checkout's history. `test_a_committed_operation_without_rationale_replays_with_no_base_history_needed`
  is the history-independent guard: `commit_like_the_base_writer` restores only the base's two
  behaviours (no realization check, the generated sentence) under `monkeypatch` for one run, so the
  recorded digest is the base one. Both assert through `assert_the_committed_legacy_operation_replays`
  (exact retry `replayed` and published, journal and claims byte-identical, changed key conflicts, a
  new rationale-less entry refused). `test_a_recorded_but_uncommitted_allocation_without_rationale_is_still_refused`
  copies a committed operation's journal into an empty candidate: the allocation is recorded but not
  stored, so the entry is refused `realization_rationale_absent` with the journal unchanged.

### Conventions

- Builders (`entry`, `target`, `pair`, `run`, `symbol`) are shared from
  `test_knowledge_curator_ingest_list.py`; `placed` adds a target with optional `rationale` / `role`.
- Registered in the `unit-regression` lane of `test-evidence-lanes.toml` and as a consumer in two
  `evidence-lifecycle.toml` artifact rows (catalog completeness requires both).

### Invariants And Boundaries

- The base-history case needs `BASE_COMMIT` (`a0b2c18d…`) reachable; where it is not (a history-less
  export), the no-history guard carries the protection.
- **Known fixture limit (review R4 observation, not a finding):** the recorded-but-uncommitted case
  reaches its red result under the weakened exemption (`if held is None`) through an unrelated guard
  (`candidate_candidate_binding_changed`, because the journal came from another candidate), not through
  the real crash window. Reviewer R4 probed the real window separately; rebasing the fixture on it is
  optional and the Architect's call.

### Todos

- Optional (Architect): rebase the recorded-but-uncommitted case on the real crash window (same
  candidate, `_run` raising once after the journal write), per review R4.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the cases it proves.** | "Per-target realization rationale and role, through the real curator writer." | mcp/tests/test_curator_realization_authoring.py:1-19 |
| The shared builders it reuses and the old generated sentence as stored rows hold it. | `GENERATED_BEFORE`; `placed` | mcp/tests/test_curator_realization_authoring.py:47-68; mcp/tests/test_curator_realization_authoring.py:71-79 |
| **Per-target values and the entry default.** | `test_each_target_of_one_entry_stores_its_own_authored_rationale_and_role`; `test_a_target_that_states_nothing_inherits_the_entry_level_default` | mcp/tests/test_curator_realization_authoring.py:121-150; mcp/tests/test_curator_realization_authoring.py:153-179 |
| **No rationale refuses by name and nothing is generated.** | `test_a_target_with_no_rationale_refuses_its_entry_by_name_and_nothing_is_generated` | mcp/tests/test_curator_realization_authoring.py:182-215 |
| Exact replay versus changed rationale, and old generated claims readable as stored. | `test_an_exact_replay_of_per_target_rationale_is_idempotent_and_a_changed_one_is_refused`; `test_a_claim_holding_the_old_generated_sentence_reads_back_exactly_as_stored` | mcp/tests/test_curator_realization_authoring.py:218-251; mcp/tests/test_curator_realization_authoring.py:254-269 |
| Not-text, unknown-role and over-long refusals leave the sibling entry committed. | `test_a_value_that_is_not_text_an_unknown_role_or_an_over_long_rationale_refuses_its_own_entry` | mcp/tests/test_curator_realization_authoring.py:272-314 |
| **The real base writer, and the committed-legacy replay with and without history.** | `BASE_COMMIT`; `base_writer`; `test_an_operation_the_base_writer_committed_without_rationale_replays_and_publishes`; `test_a_committed_operation_without_rationale_replays_with_no_base_history_needed` | mcp/tests/test_curator_realization_authoring.py:317-350; mcp/tests/test_curator_realization_authoring.py:353-384; mcp/tests/test_curator_realization_authoring.py:387-397 |
| **Recorded-but-uncommitted is not exempt.** | `test_a_recorded_but_uncommitted_allocation_without_rationale_is_still_refused` | mcp/tests/test_curator_realization_authoring.py:400-432 |
| The base-shaped commit helper and the shared replay assertion. | `commit_like_the_base_writer`; `assert_the_committed_legacy_operation_replays` | mcp/tests/test_curator_realization_authoring.py:435-456; mcp/tests/test_curator_realization_authoring.py:459-511 |
| Governing-route placeholder and non-text route refusals. | `test_the_word_absent_as_a_governing_route_is_refused_and_an_omitted_route_stays_ungoverned`; `test_a_governing_route_that_is_not_text_is_refused_where_it_is_written`; `test_the_word_absent_is_refused_as_a_governing_route_in_any_case_once_trimmed` | mcp/tests/test_curator_realization_authoring.py:514-560; mcp/tests/test_curator_realization_authoring.py:573-603; mcp/tests/test_curator_realization_authoring.py:606-630 |
| The owner under test. | `realization_refusal`; `EntryRealization` | mcp/src/agents_remember/application/curator_realization_authoring.py:249-280; mcp/src/agents_remember/application/curator_realization_authoring.py:134-174 |
| Lane registration. | "mcp/tests/test_curator_realization_authoring.py" | mcp/tests/test-evidence-lanes.toml:24-24 |

## Cross-Repo References

No cross-repository behavior is exercised by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-28T17:09:54+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`; primary ICR-R20@v1, review R4 PASS): created this card for the new evidence module (12 cases after A5). Verification stamp names the code base; closeout owns the real stamp.
