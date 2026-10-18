# mcp/src/agents_remember/application/knowledge_gate/gate.py

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
  1. `_applies` returns false for a non-leaf contract or one without a memory worktree; otherwise it
     delegates applicability to `leaf_gate_applies(contract, candidate)`. A false result returns `None`
     before tip resolution or evaluation. A probe Git cannot answer (`SubprocessError`, `LayoutProbeError`)
     is **applicable**, never an exemption: evaluation continues so its unreadable input can be reported.
  2. With no tip given, `_resolved_tip` reads the parent line's memory tip from the contract
     (`worktrees.knowledge_gate.parent_memory_tip`); a failure is one `incomplete` finding (`parent memory line`), and
     that result is not memoised.
  3. The memo (`memo.memo_key`, `memo.remembered`): a hit re-persists the kept worklist only when `persist_worklist` is true and returns
     the kept verdict.
  4. On a miss, `_evaluate` runs inside `recorded_reads()`, so its recorded requirement and settings
     observations are collected. After that scope exits, `replay_reads(reads)` propagates the collected
     observations to an enclosing recorder, including when the result cannot be memoised. With both a key
     and a result, `memo.remember` then considers the verdict and read set under its existing admission rules.
- **`_evaluate`** recomputes, optionally persists the worklist (`_persist`; a write failure never changes the verdict) and
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
  leaf_publication=LeafCommit(frozen))`: every judged candidate publishes a leaf, so the history-row rule reads the leaf's own file
  whatever its `closed` flag (review R1 F1), except a file closed in a base or in a frozen commit. `frozen` holds the
  history files (`history_tree_from_git`) of `GateTrees.frozen`: the memory commit of the leaf's completed closeout,
  from `closed_out_memory(contract)`. A `SubprocessError` is `incomplete [git]`, never a validity verdict
  (F9); `OSError`/`ValueError` is `knowledge-validator-unreadable`.
- **Findings name the history file the writer writes (L37 reopen ruling, review R1 F10a).** `_item_findings` takes
  the file from `_writable_history(context, owner, trees)`, not from the plain `history_path(owner)`. For every
  history file of the owner in the candidate (`owner_history_attempt`), an attempt counts as frozen when it is
  closed in a comparison base or in the leaf's memory `HEAD` commit (`_closing_commits`, then `_closed_in`: `git
  cat-file blob <commit>:<path>`), which is the writer's own rule: a leaf that closed out and continues before it is
  integrated writes its next attempt; `writable_attempt` then names the latest open attempt, or the next one. An
  attempt that only the candidate closes (this closeout's own) is still the one named. Without any commit to
  read, the candidate's own `closed` flags stand in. The read is for the message only: a failed read counts as not
  closed.
- **The two memory commits beside the candidate (L37, decision record DEC-0AEQ28; INV-MS9BMJ).** `evaluate_leaf_gate`
  reads the leaf's memory `HEAD` (`_leaf_memory_head`; `None` when it cannot be read) beside the parent line's tip
  and carries both as `_MemoryLines`. `HEAD` is part of the memo key, and `GateTrees.leaf_memory_head` is read only
  to name the file a row goes to. `GateTrees.frozen` is what the validator freezes.

### Conventions

- The admission base is the parent line's memory tip (the L27 carry, ruling 2026-09-29T22:11:24): every record first
  created in the leaf, in however many commits, is judged new by `R27.2-new-record`.
- Ordinary quality/closeout runs persist the recomputed worklist beside the contract; landing refusal callers explicitly disable that persistence, including memo hits, so judgment changes no worklist file.

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
- **A false applicability probe returns `None`; an unreadable probe does not.** Applicability is delegated
  to `leaf_gate_applies`, rather than inferred here from a blanket statement about unconverted memory.
  The earlier `unconverted.sh` comparison is historical evidence, not this module's current applicability
  contract. The separately described cutover lock remains a route concern, not an exemption implemented here.

### Historical L09 carry notes — not current open work

These notes retain the earlier L09 handoff. Current reopened-attempt selection, applicability and
publication contracts are described above; they do not defer the current gate or its read provenance.

- **Carried to L37 (ruling 2026-09-30T16:08:08):** after the cutover, `task_reopen` on a leaf that closed out leaves
  its history file closed in K_B, so MIK-R22's freeze rule refuses any row the reopened leaf adds; L37 decides how a
  reopened leaf records answers and tests reopen after a converted closeout.
- **Carried to L37 (gap 1):** the refusal of unconverted trees at every route, which is the cutover lock (G4 remains
  the developer's).

### Read provenance across evaluation scopes

Cold evaluation replays its collected observations after leaving its local recording scope and before
attempting to keep the result. An outer caller can therefore retain the same recorded dependencies
without depending on whether this evaluation produced a memo entry. Warm evaluation obtains its verdict
through `memo.remembered`; that helper owns replay of the kept observations. The existing
`persist_worklist` switch remains independent: a memo hit persists only when requested, and a cold
read-provenance replay is not a worklist write.

Applicability remains a contract-and-candidate probe. This module rejects non-leaf and memory-less
contracts locally, delegates the remaining choice, and continues on the named probe failures instead of
silently exempting unreadable inputs.


### Public gate verdicts for the reviewer

`item_verdicts` is the public per-item projection of the gate’s registered predicates, not a second satisfaction rule. It builds one candidate context, returns `undecided` for every item if that context is unreadable, judges invariant kinds first, and then gives family predicates the subjects of invariants not answered. Optional held K_C/C inputs must both be present and match the memory tree key, code tree and code repository; a partial or mismatched binding is unreadable. This projection does not run validator admission or authorize a write.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R09@v2` and `09_mandatory-invariant-closeout-gate.json`,
outside the repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The public gate projection decides invariants before the remaining items and returns typed unreadability. [22]
- Held reuse admits only both exact candidate sides and the code repository. [23]


- The module docstring: the rule, always recomputed, applicability and what is not wired. [1]
- The finding codes and the repair row. [2]

- The exact candidate the gate judges. [3]

- The verdict: memoisable, brief and refusal. [4]
- The recompute that never raises. [5]


- Probe, tip, memo, then the recorded evaluation. [6]


- The evaluation and the judgment. [7]


- K_C and C read once; the invariant kinds first; a failed read is incomplete. [8]

- The validator at the gate, as a leaf publication. [9]

- The packet's examples: ready only once current rows answer every item, and its case asserts that a new edit reopens four items. [10]
- A failed Git read inside a predicate or the validator is never a verdict. [11]

- The file a row answering the leaf's items goes to: the latest attempt not closed in a base or in the leaf's memory HEAD. [12]

- Whether a comparison base or the leaf's memory HEAD commit holds the path as a closed history file. [13]

- The gate names the attempt the writer writes. [14]


- The gate reads the leaf's memory HEAD beside the parent tip, and keys its memo on both. [15]

- The leaf's memory HEAD, or nothing when it cannot be read. [16]
- The commits whose closed history files are frozen for the writer: the bases and HEAD. [17]
- The validator inside the gate is handed the frozen commit's history files. [18]
- A leaf that continues after its closeout is refused while an item is open, and the refusal names attempt 2. [19]

- Cold evaluation replays its collected reads before memo admission; memo-hit worklist persistence remains optional. [20]
- Applicability delegates to leaf_gate_applies and treats unreadable layout probes as applicable. [21]

### Cross-Repo References

No meaningful cross-repo references found: the gate reads the leaf's own code and memory repositories.

No cross-repo boundary is crossed by this file.
