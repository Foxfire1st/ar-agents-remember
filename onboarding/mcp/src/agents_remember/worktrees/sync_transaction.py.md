# mcp/src/agents_remember/worktrees/sync_transaction.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Contract-addressed driver for resumable source synchronization.

## Code Commentary

### Logic

Input validation and stable journal routing precede mutation. Only merge-memory/skip-memory and continue/cancel are admitted. Dirty moving candidates are parked/restored under their own recorded stash.

Code settles before memory; _paired_code supplies its result for structural memory merge and validation. _continue_resolution selects the retained side and finishes staged merge or parked reapply before automatic progress resumes. Validator refusal leaves phase/staged merge intact and names repair.

Structural report paths survive retained conflicts/conversion. No canonical row conflict, accepted decision list or reconcile-cycling state is authored.


`sync_contract_under_authority` validates input choices and reads the enclosure-root journal. It
routes damaged/missing journal recovery, quarantine, identity validation, active resumption,
terminal replay, or new admission. The operation returns typed results; no lock remains held while
an agent resolves conflicts between calls.

Admission resolves actual code/memory source tips and builds typed `SyncSideRecord` plans for
already-current, fast-forward, merge, or skip behavior. It no longer performs a ledger mapping
preflight. `_already_current_result` uses the recorded bases and participating branch ancestry,
independently of cached rows. A divergent memory plan still requires its explicit merge/skip choice,
and that admitted choice cannot change during continuation.

Before a moving non-temporary side is parked, preflight proves its checkout and rejects real
content conflicts or an active `MERGE_HEAD` outside the sync admission. A merely dirty candidate is
parked rather than refused. `_park_participating_wip` passes the complete side record to dirty-path
and stash helpers, so the memory side excludes only its root `memory.md` cache. It records the stash,
up to 128 sampled paths, and the exact total path count. Failed partial parking attempts restore
already parked work where possible and report any stranded stash identities.

The admitted record pins source/base/pre-sync authority before automatic code-then-memory progress.
Native merge behavior and exact parent/source proofs belong to `sync_transaction_git`. Genuine
content conflicts remain in the retained worktree. The driver reads `content_conflicts(side)` when
refreshing both merge-resolution and parked-WIP-resolution failures, so a memory-cache conflict is
not presented as content requiring agent judgment.

Completed paths, resume, and cancellation restore parked work through the focused authority/recovery
owners. `_reconcile_completed_sides` can recognize an already committed operation-owned merge;
finalization waits for the participating sides and parked work to be settled. Exact checkout,
source, parent/ref, journal, and admitted-choice checks remain in force.

**The memory merge is validated against the code side's result (MIK-R22 rule 8).** `_run_side` and
`_finish_retained_merge` pass `paired_code=_paired_code(record)` into `start_side_merge` and
`continue_side_merge`. `_paired_code` returns the code side's `resultHead` (as a `PairedCode` with the
code repository) once the code side is `completed`, and `None` otherwise; `sync_transaction_git` then
refuses a *converted* memory merge with no paired code commit. When the validator refuses,
`SyncKnowledgeValidationError` is caught before the generic `SyncGitProofError` in both `_run_automatic`
and `_finish_retained_merge`, and `_knowledge_validation_refused` returns the manual-repair result
`sync-knowledge-validation-refused`. Its summary is every violation followed by a recovery line: repair
the files in the memory worktree, stage them, then rerun `worktree_sync` (with
`resolution_action='continue'` when the phase is `memory-resolution-required`), or cancel with
`resolution_action='cancel'`. The phase is not changed and the merge stays staged, so the same call
resumes and re-validates.

**The crossing sync's owner and report (MIK-R24 rule 8).** `_run_side` also passes
`crossing_owner=("leaf" if record.contractKind == "leaf" else "master", record.taskId)` into
`start_side_merge`, so a crossing sync knows whose history file takes the moved no-impact markers (a leaf),
or which task's `<task-id>-crossing-<n>.json` takes a record conflict's row (a master line). The
`SideMergeOutcome.crossing_report` path is journaled on the side record as `crossingReport`, both when
the side needs resolution and when it completes. For an ordinary sync it is empty, and the journal then
omits the key (`sync_transaction_state`).

Retained output is attributed at the mutation boundary. `_run_side` passes the same settled paired code and crossing owner into the merge and `recapture_resumed_merge`. A resumed converted-memory merge earns retained fingerprints only after reproducing both Git and its structural crossing; the mere presence of an active merge does not establish byte ownership. `_persist_fresh_validator_stop` records fresh same-call staged memory output without changing the validator refusal. It does not bless an owner-resolved or unproved crash-window tree.

### Conventions

The driver owns phase routing and delegates Git mechanics, journal storage, pinned authority,
result formatting, and terminal recovery. Top-level I/O/proof/value failures return
`sync-operation-refused` with the failure family and retained detail. The cache is an ignored
consumer artifact on the memory side, not a second source of sync truth.


### Invariants And Boundaries

- Pinned journal/Git facts identify one transaction.
- Parked work must be restored or explicitly reported.
- Validator refusal is never committed around.

- New moving-side admission cannot adopt an unrelated active merge.
- **A memory sync between unconverted sides waits for the crossing sync (L37, MIK-R09 rule 6).**
  `_admit_participating_sides` asks `_cutover_locked(memory, fetch)` before the preflight, so before any preview or
  Git move. It refuses with `sync-unconverted-memory-locked` (exit 2) only when no side holds the layout marker
  (the own head, the incoming commit and, for a merge, their merge base, asked of the repository because a series
  side has no worktree yet) and the repository holds converted memory elsewhere. A crossing sync (some side
  converted), a code-only sync (`skip-memory`) and an already-current side are never refused. A marker probe Git
  cannot answer refuses by name; it is never read as unconverted memory. A sync already in flight is not
  re-admitted, so it can still be continued or cancelled.


### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Evidence

### Docs References

No external Domain Documentation entries are configured. Source and test assertions are distinguished from execution and acceptance evidence.

### Repo-Internal References

- Current input and journal routing. [1]

- Real content conflict continuation scenario. [18]

- Moving candidate park. [2]

- Dirty work admission and parking use complete typed side records. [33]

- Currentness and continuation use Git facts and content-only conflicts. [34]

- The validator's refusal is mapped to its own state with a recovery line, on the automatic path and the retained-conflict continuation. [35]

- The side run names the crossing owner (leaf or master, and the task ID) and journals the crossing report path. [36]

- The memory merge is paired with the code side's settled result commit, or with nothing before it settles. [37]

- A resolved memory conflict that breaks validation is refused on `continue` and syncs after the repair. [38]

- **The side the retained phase names is read in one place, so phase and side cannot disagree.** [39]

- Validator refusal retains repair state. [4]

- Pinned authority and parked-work restoration remain separate owners. [41]

- Terminal finalization/cancellation and damaged-journal recovery are delegated. [42]

- The cutover lock at sync admission: unconverted on every side and a locked repository. [43]

- The lock is asked before the preflight of the participating sides. [44]

- The driver validates choices and routes retained or new transactions: continue or cancel only. [45]

- The one continuation a hand-staged resolution ends in; no authored decision is stored. [46]

- The driver uses one paired-code/owner context for merge and resumed capture. [47]

- Fresh validator-stop output is captured without blessing an owner window. [48]

- Structural report journaling. [5]

- Settled code pairing. [6]

- Current continuation. [9]

### Cross-Repo References

No additional configured cross-repository contract is asserted.
