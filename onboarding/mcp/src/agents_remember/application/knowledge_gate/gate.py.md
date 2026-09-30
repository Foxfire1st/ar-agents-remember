# mcp/src/agents_remember/application/knowledge_gate/gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_gate/gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:09:38+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The mandatory invariant closeout gate over one leaf's exact candidate: recompute, decide, validate
(MIK-R09@v2).** `evaluate_leaf_gate` recomputes the leaf's worklist over the Git trees the route already captured
(C and K_C), decides every item through its kind's predicate, runs the validator (MIK-R22) against the parent line's
memory tip, and returns a `GateResult`: every open item, every unreadable input and every refusing violation is one
`GateFinding`. The curator publication counts them toward `curatorActionableCount`; the closeout validator and
every commit route refuse while any exists. None is report-only, and there is no waiver (rule 5).

## Code Commentary

### Logic

- **Findings.** `GateFinding(code, path, message, item)`; the codes are `knowledge-item-open` (`ITEM_OPEN`, one per
  open item, naming kind, subject, item ID, the reason, the registry's `satisfying_row` as the required action and
  `item_facts`), `knowledge-worklist-incomplete` (`RUN_INCOMPLETE`, one per unreadable input) and
  `knowledge-validator` (`VALIDATOR`, one per refusing violation; `knowledge-validator-unreadable` when the trees
  cannot be read). `to_repair_finding` renders one as the checklist's repair row under check `knowledge-gate`
  (`GATE_CHECK`), with `itemId` for an open item.
- **`GateResult`** carries the owner, the recomputed worklist, where it was persisted, the findings and the
  report-only validator findings. `ok` is "no finding"; `brief()` is the tool response's `knowledgeGate` (state, owner,
  worklist state/digest/path, and the finding, open-item, incomplete, violation and report-only counts); `refusal()`
  joins every finding (40 shown) under "the mandatory invariant gate (MIK-R09) refuses: N finding(s) … (no waiver
  exists)". `memoisable` is false for any result whose worklist is not `complete` or that carries an `incomplete` or
  unreadable-validator finding.
- **`GateTrees`** is the exact candidate: the code tree C and memory tree K_C in their repositories' object stores,
  the validator's comparison bases, B (an unconverted base converts at its own trailer's code commit, or at B) and
  the converted-base cache.
- **`recompute_for_gate`** calls `leaf_worklist(contract, persist=False, candidate=…)` and never raises: a
  `SubprocessError` is the `incomplete` worklist naming `git` (`git_failure`, the L03 carry, ruling 19:15:20); any other
  exception names the run. Nothing persisted earlier is read (the L11 carry: always recompute).
- **`evaluate_leaf_gate(contract, candidate, *, parent_memory_tip=None)`**:
  1. `_applies` probes the marker (`leaf_gate_applies`): a non-leaf contract, one without a memory worktree, or a leaf
     with the marker on neither side returns `None` before anything more is read. A probe Git cannot answer
     (`SubprocessError`, `LayoutProbeError`) is **applicable**, never taken for unconverted memory (review R1 F9).
  2. With no tip given, `_resolved_tip` reads the parent line's memory tip from the contract
     (`worktrees.knowledge_gate.parent_memory_tip`); a failure is one `incomplete` finding (`parent memory line`), and
     that result is not memoised.
  3. The memo (`memo.memo_key`, `memo.remembered`): a hit re-persists the kept worklist beside the contract and returns
     the kept verdict.
  4. On a miss, `_evaluate` runs inside `recorded_reads()`, so every requirement file and settings file the
     evaluation reads is recorded (ruling 15:09:25), and `memo.remember` keeps the verdict with that read set when it
     is memoisable.
- **`_evaluate`** recomputes, persists the worklist (`_persist`; a write failure never changes the verdict) and
  calls `judge` with `validation_bases=(parent tip,)` and the contract's cache.
- **`judge(document, path, trees, owner)`**: an incomplete run is one finding per named input; a complete one goes
  through `_item_findings`; the validator's refusing findings are appended.
  - `_candidate` reads K_C (`git_tree_snapshot`, `KnowledgeSide`) and opens C once for every predicate, or returns the
    finding that names what cannot be read (`K_C`, `git`, `C`).
  - `_decided` decides the invariant kinds first, then gives the family rule the set of open invariants, then decides
    everything else, each through `item_open_reason`. A `GitReadFailed` raised inside a predicate makes the result one
    `incomplete [git]` finding (never memoised).
  - A leaf with no leaf ID gets one open-item finding: it has no history file whose rows could answer its items.
- **`validation_findings(trees)`** reads K_C and each base (`_base` replaces an unconverted base of a converted
  candidate by its conversion, MIK-R24 rule 7), and, when `validation_applies`, runs `validate_tree(…,
  leaf_publication=True)`: every judged candidate publishes a leaf, so the history-row rule reads the leaf's own file
  whatever its `closed` flag (review R1 F1). A `SubprocessError` is `incomplete [git]`, never a validity verdict
  (F9); `OSError`/`ValueError` is `knowledge-validator-unreadable`.

### Conventions

- The admission base is the parent line's memory tip (the L27 carry, ruling 2026-09-29T22:11:24): every record first
  created in the leaf, in however many commits, is judged new by `R27.2-new-record`.
- The worklist the gate computed is the one persisted beside the contract and rendered in the checklist.

### Invariants And Boundaries

- **No memory reaches a leaf-publication route without the recomputed worklist fully answered and the validator
  passing; no waiver, override or report-only mode exists.** Candidate invariant (not ingested). Realized here by
  `judge` (open items, incomplete inputs and violations are all findings) and at the routes by the refusals that
  consume `GateResult.refusal()`; proved by the gate and route tests (below) and the real converted scratch
  (`gate-1-refused`: 5 findings; `gate-2-answered`: pass; `gate-3-edited-again`: 2; `gate-4-restored`: pass).
- **The gate always recomputes from the exact trees; a kept verdict is reused only for identical inputs, and an
  incomplete run or a Git failure is never kept.** Candidate invariant; realized by `recompute_for_gate`,
  `GateResult.memoisable` and [`memo`](memo.py.md); proved by the memo, approval-state and Git-failure tests.
- **An unreadable input makes the run incomplete with a named reason; it is never read as unchanged, answered or
  absent.** Candidate invariant; realized by `recompute_for_gate`, `_applies`, `_resolved_tip`, `_candidate`,
  `_item_findings` (`GitReadFailed`) and `validation_findings`; proved by
  `test_an_incomplete_run_is_one_finding_naming_its_input_never_an_unhandled_error`,
  `test_a_git_read_that_fails_inside_a_predicate_or_the_validator_is_never_a_verdict` and
  `test_a_marker_probe_git_cannot_answer_is_never_unconverted_memory`.
- **On unconverted memory the gate is `None`** (inert until the cutover; `unconverted.sh`: identical to base apart
  from the build label).
- **Not built here:** MIK-R09 rule 6's second bullet (refuse unconverted trees and name the crossing sync), carried to
  L37 by ruling 14:38:47 gap 1; the docstring says so.

### Todos

- **Carried to L37 (ruling 2026-09-30T16:08:08):** after the cutover, `task_reopen` on a leaf that closed out leaves
  its history file closed in K_B, so MIK-R22's freeze rule refuses any row the reopened leaf adds; L37 decides how a
  reopened leaf records answers and tests reopen after a converted closeout.
- **Carried to L37 (gap 1):** the refusal of unconverted trees at every route, which is the cutover lock (G4 remains
  the developer's).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R09@v2` and `09_mandatory-invariant-closeout-gate.json`,
outside the repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring: the rule, always recomputed, applicability and what is not wired. | "The gate never reads a persisted worklist or trusts its digest" | mcp/src/agents_remember/application/knowledge_gate/gate.py:1-28 |
| The finding codes and the repair row. | `GATE_CHECK`; `GateFinding` | mcp/src/agents_remember/application/knowledge_gate/gate.py:99-127 |
| The exact candidate the gate judges. | `GateTrees` | mcp/src/agents_remember/application/knowledge_gate/gate.py:130-147 |
| The verdict: memoisable, brief and refusal. | `GateResult`; "def memoisable(self)"; "def brief(self)"; "def refusal(self)" | mcp/src/agents_remember/application/knowledge_gate/gate.py:150-211 |
| The recompute that never raises. | `recompute_for_gate` | mcp/src/agents_remember/application/knowledge_gate/gate.py:214-233 |
| Probe, tip, memo, then the recorded evaluation. | `evaluate_leaf_gate`; `_applies`; `_resolved_tip` | mcp/src/agents_remember/application/knowledge_gate/gate.py:236-279 |
| The evaluation and the judgment. | `_evaluate`; `judge` | mcp/src/agents_remember/application/knowledge_gate/gate.py:293-342 |
| K_C and C read once; the invariant kinds first; a failed read is incomplete. | `_candidate`; `_item_findings`; `_decided` | mcp/src/agents_remember/application/knowledge_gate/gate.py:345-415 |
| The validator at the gate, as a leaf publication. | `validation_findings`; `_base` | mcp/src/agents_remember/application/knowledge_gate/gate.py:436-495 |
| The packet's examples: ready only once current rows answer every item; a new edit reopens two. | `test_a_leaf_is_ready_only_once_current_rows_answer_every_item_and_a_new_edit_reopens_two` | mcp/tests/test_knowledge_closeout_gate.py:404-443 |
| A failed Git read inside a predicate or the validator is never a verdict. | `test_a_git_read_that_fails_inside_a_predicate_or_the_validator_is_never_a_verdict` | mcp/tests/test_knowledge_gate_routes.py:802-825 |

## Cross-Repo References

No meaningful cross-repo references found: the gate reads the leaf's own code and memory repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:09:38+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): created this card for the new file MIK-R09 adds, recording the carried obligations (L22 validator wiring, L03 `SubprocessError` → incomplete, L27 admission base at the parent tip, L11 fail-closed reads and always recompute; start decision 13:15:47), gap 1 carried to L37 (14:38:47), the memo's read set (15:09:25), review R1 F1 and F9 (16:07:55), R2-3 (17:59:48), and the 16:08:08 reopen-after-cutover carry to L37. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
