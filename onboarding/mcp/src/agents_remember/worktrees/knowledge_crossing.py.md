# mcp/src/agents_remember/worktrees/knowledge_crossing.py

## Governing Overview

[worktrees route overview](overview.md)

## Purpose

**The crossing sync in the managed sync transaction, and the unconverted-line refusal (MIK-R24 rules 8
and 9).** A memory merge is a crossing sync when one of its merge base, its own side and its incoming side
lacks `knowledge/layout.json` and another has it. This module plans the structural merge through the bound
port before Git merges, and applies it to the started merge. It writes the durable crossing report and
closes a master line's crossing history file at commit. It also holds the rule 9 refusal that writes,
memory-quality runs and (later) closeouts call.

## Code Commentary

### Logic

- `crossing_applies(repository, base, own, incoming)` probes the three layout markers
  (`knowledge_validation.has_layout_marker`). A probe failure is refused at step `markers`.
  `merge_base` resolves the base.
- `crossing_plan(worktree, sides, *, paired_code, owner)` refuses at step `convert` when the paired code
  commit is unknown (the fallback cards would have no code tree), or when no `knowledge_crossing` is bound
  (a crossing sync is never merged as plain Git). Otherwise it calls the port with a `CrossingRequest`. A
  `CrossingStepFailed` becomes `CrossingSyncError`, and the worktree is untouched.
- `apply_crossing(worktree, plan)` runs after `git merge --no-commit`:
  1. removes every `knowledge/` and `onboarding/` path from the index;
  2. writes the plan (`_write_plan_files`: tracked paths the plan drops are deleted, and every kept path
     is written);
  3. stages it with `git add -A`;
  4. leaves each conflicted path unmerged, with its converted base, own and incoming bytes as index
     stages 1-3 (`_unmerge`, through `hash-object -w` and `update-index --index-info`).

  The ordinary resolution route (`continue`) then finishes the sync. It returns the conflicted paths.
- `write_crossing_report(worktree, own, incoming, plan)` writes
  `crossing-sync-report-<own12>-<incoming12>.json` into the worktree group's `reports/`, beside the sync
  journal and outside every repository. It holds the plan's report (every conflict with its base, own and
  incoming values, cards per side, marker rows) plus `howToResolve`. `crossing_summary(path)` is the
  resolution payload's bounded view: counts, the first 100 conflicts with a truncation flag, cards, marker
  rows, the record-conflict history owner and the how-to.
- `HOW_TO_RESOLVE` tells the curator three things: a conflicted JSON item stands as a `crossing-conflict`
  marker; Markdown conflicts carry Git markers; and a card's Markdown and its sidecar must be resolved
  together, or R22.3-markers refuses the card (the reviewer's round 3 note).
- `close_crossing_history(worktree, parents)` runs in the commit step. It sets `closed: true` on, and
  stages, each `knowledge/history/<task>-crossing-<n>.json` that the merge adds and that neither parent
  holds, so the file is frozen from that commit on (MIK-R07 rule 7).
- `unconverted_line_refusal(*, memory_worktree, memory_repository, official_branch, operation)` returns
  `None` when the leaf tree is converted or there is no repository directory. When the leaf tree is
  unconverted **and** the official tip holds the layout marker (`_official_line_converted`), it returns
  the rule 9 refusal, which names the crossing sync (`worktree_sync`) and MIK-R24 rules 8 and 9. In
  every other case (no branch, a tip that cannot be read, an unconverted tip) the cutover lock decides
  (`cutover_lock.cutover_lock_refusal`, L37): the unconverted tree is refused as well once its memory
  repository holds converted memory anywhere, and gets `None` in a repository that holds none.

### Conventions

- `KNOWLEDGE_ROOTS = ("knowledge", "onboarding")` are the only paths the crossing replaces. Code-side
  paths and the rest of the memory tree keep ordinary Git merge semantics.
- Wired callers: `sync_transaction_git` (the crossing branch and the commit step),
  `sync_transaction_results` (the summary), `cli/knowledge_write_route` and
  `application/memory_quality/controller` (the refusal).

### Invariants And Boundaries

- **A crossing conflict is never committed silently.** Conflicted paths stay unmerged, and conflicted JSON
  items hold markers the validator refuses. Rule 8 step 5 is enforced at the merge commit, through the
  validator with the converted base.
- **A crossing sync that cannot complete leaves the line unchanged and names the failing step.** The plan
  is computed before Git touches the worktree.
- **Rule 9 refusals are inert until the repository holds converted memory (architect ruling, 2026-09-29; L37).**
  A repository that holds no converted memory is not locked, so no route changes behaviour there. From the
  cutover (MIK-R37 rule 6) other masters' unconverted lines are only read until they cross. **Conversion and crossing
  are separate routes:** the crossing sync is only for lines that descend from a converted official line.
  An unconverted official line, or a repository without one, converts by running `agents-remember
  knowledge-convert` and committing through its normal route.
- The crossing sync's own commit converts the line. There is no separate conversion commit.

### Todos

None recorded. The closeout refusal of rule 9 is wired (L09's gate plus L37's cutover lock in `knowledge_gate.py`).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The crossing helpers and the rule 9 refusal.

- A crossing sync: one tree unconverted and one converted. [1]
- The plan through the bound port, refused without a paired code commit or a bound crossing. [2]
- The merge's knowledge and onboarding paths become the plan; conflicted paths are unmerged with three stages. [3]
- The rule 9 refusal when the official line is converted; every other unconverted tree is left to the cutover lock. [4]
- A master-line crossing history file is closed in the merge commit. [5]
- The durable report and its bounded summary, with the how-to. [6]
- The managed sync crosses an unconverted leaf into a converted line. [7]
- Overlapping edits go to the curator with markers; a failed step changes nothing. [8]
- The refusal fires only once the official line is converted. [9]

- Rule 9, then the cutover lock for every other unconverted tree. [10]
- Whether the official line's tip holds the marker; no line or an unreadable one reads as no. [11]

### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
