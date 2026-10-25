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

- `merge_structure(repository, base, own, incoming)` classifies the actual three marker-bearing trees and selects structural merge or the crossing plan. `merge_base` resolves the base; a failed marker read remains a refusal rather than a guessed format.
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
  incoming values, cards per side, marker rows, and since MIK-R66 the alignment counts: aligned cards,
  renumbered references, kept evidence lines, skipped cards with reasons) plus `howToResolve`.
  `crossing_summary(path)` is the resolution payload's bounded view: counts, the first 100 conflicts with a
  truncation flag, cards, marker rows, the alignment counts, the record-conflict history owner and the how-to.
- `HOW_TO_RESOLVE` tells the curator three things: a conflicted JSON item stands as a `crossing-conflict`
  marker; Markdown conflicts carry Git markers; and a card's Markdown and its sidecar must be resolved
  together, or R22.3-markers refuses the card (the reviewer's round 3 note). Reference numbers are aligned by
  the merge itself, so a curator never renumbers a reference by hand to clear a conflict.
- `close_crossing_history(worktree, parents)` runs in the commit step. It sets `closed: true` on, and
  stages, each `knowledge/history/<task>-crossing-<n>.json` that the merge adds and that neither parent
  holds, so the file is frozen from that commit on (MIK-R07 rule 7).
- `unconverted_line_refusal(*, memory_worktree, memory_repository, official_branch, operation)` returns
  `None` when the leaf tree is converted or there is no repository directory. Every unconverted leaf in an actual repository is refused through the central legacy-format message.
  A converted official line names crossing sync with `merge-memory`; otherwise the cutover helper names first
  conversion. An unreadable official marker object keeps its named probe error, not a guessed legacy state.

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
- **Legacy operational inputs are unconditionally refused (MIK-R46).** The older cutover-window exemption no longer grants permission to a never-converted repository. **Conversion and crossing
  are separate routes:** the crossing sync is only for lines that descend from a converted official line.
  An unconverted official line converts inside a new leaf, as that leaf's first memory change, and lands through normal validation/gates. A root without an attributed baseline converts in place and is then adopted.
- The crossing sync's own commit converts the line. There is no separate conversion commit.
### Todos

None recorded. The closeout refusal of rule 9 is wired (L09's gate plus L37's cutover lock in `knowledge_gate.py`).
## Evidence

### Repo-Internal References

- `merge_structure` implements the retained boundary described above. [12]
- `crossing_plan` implements the retained boundary described above. [13]

- `apply_crossing` implements the retained boundary described above. [14]


- The curator text forbids hand renumbering: the merge aligns numbers itself. [15]
- The summary carries the alignment counts with zero defaults. [16]
### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.
The crossing helpers and the rule 9 refusal.
### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
- A crossing sync: one tree unconverted and one converted. [17]
- The plan through the bound port, refused without a paired code commit or a bound crossing. [18]

- The merge's knowledge and onboarding paths become the plan; conflicted paths are unmerged with three stages. [19]


- The shared legacy refusal names crossing sync for a converted official line and first conversion otherwise. [20]

- A master-line crossing history file is closed in the merge commit. [21]
- The durable report and its bounded summary, with the how-to. [22]

- Legacy refusal is unconditional; converted candidates retain their gate route. [23]


- No branch or unresolved tip returns False; a resolved tip whose marker object is unreadable returns its named LayoutProbeError [24]

- The managed sync crosses an unconverted leaf into a converted line. [25]
- Overlapping edits go to the curator with markers; a failed step changes nothing. [26]


- The refusal fires on legacy leaf memory independent of converted memory elsewhere. [27]
