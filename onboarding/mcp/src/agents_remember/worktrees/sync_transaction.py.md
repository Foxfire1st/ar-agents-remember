# mcp/src/agents_remember/worktrees/sync_transaction.py

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-20T06:02+02:00 against the uncommitted
CYCLE-02-remainder candidate on `ar/260915-ks-l40-ar`. The commit fields name the candidate's base; they do
not identify a future commit for the working changes.

## Purpose

Drives resumable, contract-addressed mid-task source synchronization. One durable generation can
be observed, continued after resolving retained content conflicts, cancelled, or recovered without
reconstructing lifecycle evidence from task prose.

## Code Commentary

### Logic

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

**The retained-conflict continuation was one route with two endings, and it is now the route an authored
decision takes as well.** `_retained_side` reads the side the retained phase names, so the phase really is
the whole address and the three call sites can no longer disagree about which side is meant.
`_finish_retained_merge` is the single continuation both a hand-staged resolution and an authored
reconciliation end in: it commits the retained merge, clears `conflictFiles`, the journaled
`knowledgeConflict` **and `knowledgeReconciliations`** together (the agent was told what to reconcile, and the
state that carried it goes with the conflict), restores parked work, and rejoins the ordinary automatic run. So a reconciled sync is a normal
sync with one authored input rather than a second route through the transaction.

**Progress or an actionable refusal, never an indefinite cycle.** When a conflict survives an attempt,
`_reconcile_progress_refusal(remaining, side.knowledgeReconciliations)` compares it against the decisions this
side held **before** the attempt, and returns the reason for the `sync-resolution-cycling` result when a row an
already-accepted decision answered has come back anyway: the authored decision was applied and retracted the
arriving change, and retracting it re-exposed another arriving change that needs the same row, so no further
authored decision will make this merge converge. The refusal names the exact row and what to do instead —
resolve it in the worktree and continue, or cancel — and it deliberately does **not** journal the same decision
a second time. A row no accepted decision named is ordinary progress: the merge moved on to a conflict nobody
has answered yet, and that one is journaled and reported exactly as the first was.

**An authored decision is checked against the journal *before* the merge is entered.**
`_reconcile_knowledge_resolution` reads the conflict from the journal, hands it to `_reconcile_problem` (via
`_reconcile_refusal`), and only then calls `reconcile_side_merge`. `_reconcile_problem` names both facts a
caller can get wrong: `_decision_matches` requires the decision to name the exact table and rendered
`record_id` the engine refused (or to be the row-less decision for a conflict with no row), and the decision
must be one `decisions` says that conflict admits. A wrong record, a decision the conflict does not admit,
or a reconcile against the code side (which merges text and carries no knowledge dataset) is refused with
`sync-input-invalid` and `invalidField="knowledge_resolution"` **without entering the merge** — carrying a
decision into a merge that would ignore it and hand back the same conflict is exactly the loop this replaced.
A decision that settles one conflict may reveal the next; that one is journaled through `_knowledge_conflict`
and reported exactly as the first was. **Every decision already accepted persists**, and the reason is the
loop this route exists to close: `_reconcile_knowledge_resolution` builds
`accepted = (*side.knowledgeReconciliations, args.knowledge_resolution)` and hands the whole sequence to
`reconcile_side_merge`, so each attempt starts from the conflict the previous attempt actually reached rather
than from the first one again. With only the newest decision carried, a merge holding two conflicts alternated
between the same two rows forever and re-offered a decision that had already been made and already had its
effect. A decision still answers only the row it named, and every conflict no decision names is still refused.
`sync_input_refusal` pairs the two inputs both ways:
`resolution_action='reconcile'` without `knowledge_resolution`, and `knowledge_resolution` with any other
action, are refused by name. `_reconcile_preview` routes a dry run to the read-only preview and refuses with
`sync-resolution-not-active` when no knowledge conflict is retained.

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

### Conventions

The driver owns phase routing and delegates Git mechanics, journal storage, pinned authority,
result formatting, and terminal recovery. Top-level I/O/proof/value failures return
`sync-operation-refused` with the failure family and retained detail. The cache is an ignored
consumer artifact on the memory side, not a second source of sync truth.

### Invariants And Boundaries

- Canonical contract and pinned Git facts identify one retained transaction generation.
- Cached mappings, byte shape, or absence do not authorize or block source synchronization.
- Only memory-side root memory.md is excluded; a code file with that name remains real content.
- New moving-side admission cannot adopt an unrelated active merge.
- Real content conflicts stay resumable, and exact merge/ref proofs cannot be replaced by a cache match.
- Parked work must be restored or explicitly reported before terminal completion.
- **A validator refusal is recoverable and never committed around.** `sync-knowledge-validation-refused` leaves the phase and the staged merge in place, names every violation and the recovery call; there is no sync input that skips validation.
- **`resolution_action='reconcile'` is admitted only with a knowledge resolution, and the two are refused
  as a pair.** `knowledge_resolution` is read only with `reconcile`, which is what keeps a decided input
  from travelling with an action that would ignore it.
- **A retry carries every accepted decision, and a returning answered row is refused rather than re-offered.**
  Each attempt re-enters the merge with all the decisions this side has already accepted plus the new one, so a
  two-conflict merge advances instead of alternating; and a row an accepted decision already answered that comes
  back anyway earns `sync-resolution-cycling` with the exact row and the two honest next steps, never a second
  copy of the same journaled decision. Neither change softens the merge guard:
  `_independent_insert_refusal` still refuses two independent insertions of one identity.
- **A decision never enters the merge unchecked.** It is validated against the *journaled* diagnosis first,
  so a wrong record or an inexpressible decision is refused before the retention is disturbed rather than
  after a merge that would have ignored it.
- **The journaled diagnosis is cleared with the conflict it explains.** A settled retained merge carries
  neither `conflictFiles` nor `knowledgeConflict`, so a completed sync cannot re-advertise a reconcile call
  for a conflict that no longer exists.
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

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

- The driver validates choices and routes retained or new transactions, including the reconcile/decision pairing. [1]
- Dirty work admission and parking use complete typed side records. [2]
- Currentness and continuation use Git facts and content-only conflicts. [3]
- The validator's refusal is mapped to its own state with a recovery line, on the automatic path and the retained-conflict continuation. [4]
- The side run names the crossing owner (leaf or master, and the task ID) and journals the crossing report path. [5]
- The memory merge is paired with the code side's settled result commit, or with nothing before it settles. [6]
- A resolved memory conflict that breaks validation is refused on `continue` and syncs after the repair. [7]
- **The side the retained phase names is read in one place, so phase and side cannot disagree.** [8]
- **The one continuation both a hand-staged resolution and an authored reconciliation end in, which clears the journaled diagnosis with the conflict.** [9]
- **The authored-decision route: validate against the journal, re-run the adapter with every decision this side has already accepted plus the new one, then finish the retained merge.** [10]
- **The two facts a caller can get wrong, and the refusal that names them without entering the merge.** [11]
- **The bounded refusal that stops the recovery cycling: a row an already-accepted decision answered that came back anyway.** [12]
- **The adapter's explanation projected into the journal and the public response, with the decisions that conflict admits.** [13]
- **The read-only dry run of an authored decision.** [14]
- The delegated Git owner excludes only the memory cache while retaining exact native merge proofs, and now returns the adapter's refusal with the merge outcome. [15]
- Pinned authority and parked-work restoration remain separate owners. [16]
- Terminal finalization/cancellation and damaged-journal recovery are delegated. [17]
- **The integration case that drives the authored decision through this driver and asserts the advertised call is the one that settles it.** [18]

- The cutover lock at sync admission: unconverted on every side and a locked repository. [19]
- The lock is asked before the preflight of the participating sides. [20]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.
