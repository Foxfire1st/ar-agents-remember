# c-09-git-worktree-manager/SKILL.md

## Governing Overview

[MCP package overview](../../../../../../overview.md)

## Purpose

This skill documents `c-09-git-worktree-manager` skill, the Git worktree lifecycle manager for Agents
Remember tasks. `c-09-git-worktree-manager` skill now owns worktree start, attach/status, external-memory
compatibility before worktree start, integration, lifecycle finalization, and cleanup. Since L11 it also documents reopening: `task_reopen` resets a fully landed leaf back
to planning under its exact leaf id, and a normal `worktree_start` then recreates the
worktrees. HFX2-L6 changes the approval wording to applicable authority: standalone/new/final work
still stops for developer approval, while subordinate accepted-series work can record standing
series authority and continue through worktree start, integration, and finalize/cleanup after clean
previews. Closeout
sequencing belongs to `c-12-closeout` skill; `c-09-git-worktree-manager` skill only supplies the worktree-specific
configured leaf `series-contract.md` path and the integration/finalization follow-up rules. Slice 2c adds a
Lifecycle Resume And Promotion section: `worktree_start` promotes the current
fleeting lifecycle to persistent (the contract `lifecycle:` anchor),
`worktree_attach` resumes it, and attaching over an unsaved fleeting lifecycle
hits the save gate (`on_unsaved=save`|`discard`).

The current skill also owns public doctrine for per-contract atomic-series activation and
resumable synchronization. Activation is runtime admission, not planning authority; the
activation record is keyed by the canonical series contract, so two atomic masters commanded by
one sprint and sharing its protected code/memory source branches hold independent records and
neither is a reason for the other to wait; nothing serializes a graph-less sprint, because a sprint
without an `executionGraph` declares no dependencies, so independent atomic masters proceed
concurrently, no master is held because another is selected, and `atomic-sequential` names the
sprint's shape (every commanded master executes atomically) rather than a serialization mechanism —
only an explicit graph's `predecessor-incomplete:` waves gate anything; conflicts are retained for
explicit continue/cancel;
stable journal evidence remains below the enclosure root; and terminal cleanup releases only the
exact selected contract.

## Code Commentary

### Logic

Since L10 the skill's intake no longer offers a chat build: it wraps the light-task or external workflow only, and single-session work rides a THIN w-02 doc (the l-01 'chat is never a build route' invariant swept into the intro and intake step 4). The skill defines the worktree MCP entrypoints for start, attach, status,
mid-task sync, worktree closeout tool handoff, integration, and cleanup. Since
the GitHub #54 series it documents the stale-base preflight (start blocks when
a source branch is behind/diverged from its upstream, with
`stale_base_choice="fast-forward"`/`"proceed-stale"` recoveries), the
auto-created external-memory source branch (official-tip base, code branch
name as template, reported as `memorySourceBranch`), the fetch-free
`worktree_status` freshness block with its `syncHint`, and the **Mid-Task Sync**
section: `worktree_sync` reconciles an exact moved code/memory source pair as a journaled,
resumable transaction. The new code tip must be ledger-mapped at the admitted memory tip; sync
early before memory work; retained code or memory conflicts resume through
`resolution_action=continue`, while explicit `cancel` restores pinned heads and releases an exact
reconciling selection. Its Mid-Task Sync section states that memory resolution is not re-judged
against either parent's row list — the ledger is derived state, its rebuild is its authority, and a
row the rebuild cannot resolve is reported as an exclusion — while repeated code commits stay valid
newest-first state history and no globally unique code key is imposed.

begins after the normal intake and onboarding gate, uses context resolved by the `c-08-ar-coordination-context-resolver` skill
through the MCP worktree tools, refuses external-memory worktree start while
the source memory repo has uncommitted content or ledger changes, and reports
recoverable lifecycle state through typed next-operation hints. 260707-HFX2-L6 broadens the
approval wording from all-human per-junction approval to **applicable authority**: standalone or
new work still uses the developer Worktree Intent Gate, but subordinate leaves/edges inside an
accepted orchestrated series record accepted-series authority and continue without a new developer
stop. The same authority distinction now governs integration and lifecycle finalization/cleanup:
accepted-series leaf→master and master→super edges may proceed after clean dry-runs under standing
series authority, while final super→main cleanup, standalone work, and deliberately raised
human-pinned gates still stop for the developer. It now also
requires agents to identify the branch that `worktree_integrate` would move
before `worktree_start`; when that branch is protected, PR-gated, or otherwise
not directly landable, agents must first create or check out a pushable
integration branch and use that branch as the worktree `source_branch`. Before
calling `worktree_start`, agents must present a Worktree Intent Gate for
developer approval; the packet names the repo, build mode, branch policy,
source branch, work branch/worktree name, memory mode, landing path, and risks.

The worktree closeout section is deliberately a routing section, not a parallel
closeout doctrine. It sends the applicable authority and concrete code, memory-content,
and ledger transaction inputs to `c-12-closeout` skill. Quality, test, memory-quality,
evidence may be attached, and the curator's complete memory-quality result is part of that evidence, but no such
operation is an automatic closeout or integration prerequisite. For worktree-backed tasks, `c-09-git-worktree-manager` skill
contributes the task `contract.md` used by `worktree_closeout_preview` and
`worktree_closeout_apply`; after closeout, `c-09-git-worktree-manager` skill resumes ownership for
integration and cleanup. Since L8 cycle 6 the Integration section also names the
seam consumer: on an orchestrated master's exit (master → super), an undecided
or policy-invalid `master-handover-approval` gate addressed to the master (by
`enclosure` = master task name) makes `worktree_integrate` return
`handover-gate-blocked` instead of landing — decide the gate per the
`l-01-agent-lifecycles` seam doctrine, then rerun. Since cycle 7 the same
section also names the spelling-check warning: when no gate addresses the
integrating master but open `master-handover-approval` gates exist elsewhere,
integrate proceeds and its result carries a `handover_gate_warning` naming
them — a check on the raised gate's `enclosure` spelling.
Before previewing integration, agents must also check out the recorded code and
memory `source_branch` in the source repositories because `worktree_integrate`
requires those active checkouts even for `dry_run=true`.

Task 25 consolidates the worktree-manager junctions onto `lifecycle_gate` with
the lifecycle-wide dry-run -> report -> raise order. At the **Worktree Intent
Gate** the skill runs the applicable dry-run/preflight first, reports the intent
packet in chat, then raises one durable lifecycle gate carrying the
`worktree-intent` junction kind, developer-facing ask, and intent packet; the
single call also blocks the lifecycle and waits for the developer decision or
matching inbox response. Integration runs
`worktree_integrate(..., dry_run=true)` before reporting the preview in chat and
then uses `lifecycle_gate(kind="integration-approval", ask=..., packet=...)`.
Cleanup/finalization runs `lifecycle_finalize_task(..., dry_run=true)` before
reporting the cleanup plan in chat and then uses
`lifecycle_gate(kind="cleanup-approval", ask=..., packet=...)`. After a
developer response reaches the agent it clears the ambient block with
`lifecycle_resume` before running the gated mutation.

The developer resolves every one of these — an agent's own model-attributed
`gate_decide` never counts as approval, and a chat "approved" does not propagate
itself, so the agent always owns the `lifecycle_resume` clear.

Task 28 reframes these three worktree hand-offs (worktree-intent,
integration-approval, cleanup-approval) from the block-and-wait `lifecycle_gate`
to **notify-and-continue**, in the order **dry-run → notify (last tool call) →
report (last prose) → stop**: the agent runs the applicable dry-run/preflight,
then calls `lifecycle_turn_end_notification(summary={…the intent / integration /
cleanup packet + the developer ask…})` as the **last tool call of the turn**, then
delivers that packet as its **final prose** and **STOPs / ends the turn**. That tool
sets the new `awaiting-developer` lifecycle state, surfaces a dashboard attention
item, and returns immediately — no wait, no operator inbox, and because it does not
render a prompt over the prose the report stays the last thing the developer reads;
the developer
responds and the **first AR tool call of the next turn** auto-resumes
(`running`) and auto-dismisses the item, so the agent issues no explicit
`lifecycle_resume`. The block-and-wait `lifecycle_gate` (+ `lifecycle_resume`)
and the operator inbox are parked as the fallback for a deliberate durable,
developer-attributed, mutation-blocking approval record (on that parked path the
report still precedes the gate raise, since the durable gate renders a prompt over
the prose); the Task 25 /
`gate_decide` / `lifecycle_resume` descriptions above are superseded historical
context. This packaged file is a sync-propagated (`scripts/sync-skills.py`)
bundle copy of the canonical `skills/c-09-git-worktree-manager/SKILL.md`.

Dashboard task 14 adds `lifecycle_finalize_task` as the terminal worktree
lifecycle tool. The skill now instructs agents to preview it, relay the landed
commit proof, cleanup plan, and task-document updates, raise the
`cleanup-approval` gate, then run the real finalizer after developer approval.
The tool proves exactly one parent-child branch edge by checking that the landed
commit is reachable from the recorded local source branch, runs or verifies
cleanup, and updates the leaf task plus immediate parent row to `Completed` when
task-doc paths are supplied. PR-gated edges are structurally identical after the
PR merge has been pulled locally. Squash-merge equivalence is intentionally out
of the default path because it erases commit lineage and can invalidate memory
lookup history.

**MIK-R38 (260928-MIK-L38): the folder master's row, and the sub-task refusal.** The `## Lifecycle Finalization
And Cleanup` paragraph now says the finalizer derives and reconciles the exact row when the bound leaf declares an
existing immediate parent "or names none and its folder's `task.json` master lists it" (ruling 2026-09-30T12:33:07
Q3), and that "a sub-task naming none whose folder `task.json` is not a master is refused" (review R1 note 5, ruling
13:11:32; "sub-task" rather than "leaf" by ruling 14:12:52, so a `light` task that is its own `task.json`, which
finalizes standalone, is not covered). The authored `skills/` source changed, and `scripts/sync-skills.py` rewrote
this copy and the eight harness starter copies byte-identically (`--check` ok for all nine). The same clauses are in
the `lifecycle_finalize_task` tool description and `docs/reference/mcp-tools.md`.

The closeout paragraph says since L37 that the preview, which runs no quality, test, memory, certification or
review tool, does ask the mandatory invariant gate on converted memory: a leaf the apply would refuse is answered
`knowledge-gate-refused` with the open findings, never `would-closeout`. It points to `c-12-closeout` for the
detail.

### Conventions

`c-09-git-worktree-manager` skill is a wrapper, not a replacement workflow. Task identity should be settled
before worktree creation: a master owns root `series-contract.md` plus its integration branch, and
each build leaf owns `enclosures/<leaf-id>/series-contract.md`. External memory incompatibility is
interactive and offers reconciliation, disabled memory, or custom handling; its
common trigger is starting off a freshly-merged gated branch whose PR merge
commit the ledger has not mapped, which `c-11-memory-carryover-from-branch` skill carryover (run after the merge) now
maps automatically so `reconciliation` is not needed. Dirty source memory blocks
start until memory content and ledger updates are committed or the developer
chooses another path.

Integration follows applicable authority: dependency-ordered leaf→master and
master→super integrations ride the series' standing approval (the developer's
portfolio-gate approval recorded in the planner master), concentrating the
developer hand-off at the super PR/carry-over gate; a raised durable
`integration-approval` gate still awaits the developer. `ff-only` lands closed
task branches when source branches did not move; `replay` handles parallel non-overlapping work by
replaying code and memory content, then regenerating the final memory ledger
row. The recorded `source_branch` is the integration target, not just a base
branch: `worktree_integrate` will move it and will not open a PR or discover
protected-branch policy on its own. For PR-gated repositories, the approved
intent packet must make clear that the protected target is not the recorded
`source_branch`; the source branch is the pushable branch that will later be
pushed for PR. Integration preview also expects the recorded code and memory
source branches to be the active checkouts in the source repositories, so agents
should switch clean source checkouts before calling `worktree_integrate` with
`dry_run=true`. Lifecycle finalization follows the same applicable-authority boundary and removes
worktrees plus merged local task branches only after integration, carryover, and
landed-commit proof.

### Invariants And Boundaries

`c-09-git-worktree-manager` skill must not use divergent memory as trusted context, must not bypass `c-12-closeout` skill's
applicable closeout authority gate, and must not create closeout commits outside
`c-12-closeout` skill's code-memory-ledger sequence. Worktree status reports lifecycle phase,
dirty flags, summary, and typed next hints instead of shell commands.
Integration must not move source branches until code and memory commits are
fast-forwardable or replay has produced mediated commits. The skill must not
call `worktree_start` until either the developer has approved a new-plan Worktree Intent Gate or
accepted-series authority has been recorded for subordinate work.
For protected, PR-gated, or otherwise not-directly-landable target branches, the
selected `source_branch` must be a developer-approved pushable integration
branch created from that target, not the protected target itself. Lifecycle
finalization requires completed closeout, completed integration, completed
memory carryover, landed-commit ancestry on the recorded source branch, and
applicable cleanup/finalization authority.

Atomic-series activation is scoped to the exact canonical series contract and never reads task
prose or queue ownership. Task-document authoring is always upstream. The queue owns no activation,
operation, commit, certification, or integration evidence. There is no tolerant selector reader or
contract-presence election. Terminal cleanup may release only the exact still-selected contract and
must preserve a newer selection.
Memory-merge validation proves the pinned Git history only; older same-code rows remain audit history
and a row the projection cannot resolve is reported there rather than refused by the sync.


### Todos

Source claims are reconciled to the frozen synchronized copy. Verification remains closeout-owned
until the real code commit exists.


## CCR-R12@v5 Transaction Boundary

Current contract: closeout and integration are Git transactions over the authorized code, memory-content, and ledger legs, with preview, conflict, and ref safeguards. Their transaction-owned commit legs suppress automatic quality and test hooks; ordinary explicit Git hook policy outside closeout/integration remains unchanged. Targeted checks, certification, full code quality, full tests, and independent review are contextual evidence or explicit operations rather than automatic c-09 prerequisites; curation is the exception — the curator's complete memory-quality operation travels with the handoff as a prerequisite, and the transaction carries it without invoking it.

### Docs References

No external documentation is needed for this repository-local skill.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- `c-09-git-worktree-manager` skill owns worktree lifecycle and routes closeout to `c-12-closeout` skill. [1]
- `c-12-closeout` skill owns the shared closeout approval and code-memory-ledger sequence for direct and worktree closeout. [2]

- The source-branch contract says protected, PR-gated, or otherwise not-directly-landable targets need a pushable integration branch before `worktree_start`, because integration lands into the recorded `source_branch`. [3]
- The Worktree Intent Gate must be explicitly approved before start and must name branch policy, source/work branches, memory mode, landing path, and risks. [4]
- Developer-gated starts run preflight, notify-and-stop, then auto-resume on the next AR call; accepted-series subordinate starts continue under recorded authority. [5]
- Integration and finalization run dry-runs first; developer-gated edges notify-and-stop while accepted-series subordinate edges continue under standing authority. [6]
- Integration preview requires the recorded code and memory `source_branch` to be checked out in the source repositories, even for `dry_run=true`. [7]
- Integration remains owned by the `c-09-git-worktree-manager` skill and covers fast-forward and replay strategies after closeout. [8]
- Lifecycle finalization remains owned by the `c-09-git-worktree-manager` skill and requires completed integration, carryover, landed-commit proof, and cleanup/finalization approval. [9]
- The finalizer paragraph names the folder master's row and refuses a sub-task naming none whose folder `task.json` is not a master (MIK-R38). [10]
- The shipped text is corrected: admission is contract-scoped, each canonical series contract owns its own activation record, and masters sharing one exact code/memory source pair never share that state. [11]
- The shipped closeout-queue paragraph now projects only active, reconciling, or vacant waiting candidates and owns none of those lifecycle facts. [12]
- The shipped sync-scope "source pair" is current: sync derives one contract's code/memory branch pair from the contract, so the phrase describes a two-branch reconciliation, not a serialization claim. [13]

- The preview asks the mandatory gate on converted memory. [14]

### Cross-Repo References

No sibling repository evidence is needed for the skill itself.

No meaningful cross-repo references found.

## Series-Contract Notes

The packaged worktree-manager skill defines the new operating model: master tasks own an integration branch via root `series-contract.md`, and each active leaf owns a distinct enclosure contract/worktree under `enclosures/<leaf-id>/`.

## L23 Task Topology And Lineage Gate

The packaged worktree skill now requires every build to live in a leaf beneath
a thematic master; single-owner work changes orchestration depth, not topology.
Before structural exposure it requires task-derived super-to-master-to-leaf
code/external-memory lineage and distinguishes that gate from overridable remote
stale-base policy. Recovery synchronizes the existing thematic master/leaf
contracts rather than creating artificial follow-up masters.

## 260821-CLIVE Stable Lifecycle And Terminal Doctrine

The installed skill now distinguishes the configured contract address from the live enclosure root.
Start reserves an exact independent locator and immutable root manifest; live status follows that
address to root-local journal/history, while terminal status follows a state-disjoint locator to
the exact external archive/receipt plus surviving contract truth. Normal readers never scan or
adopt legacy state implicitly. `closeout_door` owns waiting intent, `closeout_queue` owns only
status/rebuild, and `worktree_operation_control` owns advertised journal recovery. Cleanup/abandon
archive before deletion and replay only their exact accepted typed arguments. Queue invalidation,
task edits, or enclosure deletion cannot erase a claimed journal or authorize guessed recovery.

## IAS Per-Contract Activation And Resumable Sync

The packaged skill now matches the canonical runtime doctrine. The activation record is keyed per
series contract, not per protected source pair. Manager/worker dispatch and atomic start/attach
activate the requested canonical contract; reviewer/curator inspection does not. Activation
publishes `reconciling`, syncs that contract's exact code/memory bases, and publishes `active` only
when current. Two atomic masters commanded by one sprint share a protected source pair but own
separate records, so activating one never replaces, pauses, or blocks the other; the only
activation waiting reason is `atomic-series-reconciling` for that contract's own in-flight
reconciliation, and a foreign master is never a reason to wait. Multiple nonterminal contracts are
valid, and task authoring never consults activation or queue state. Nothing serializes a graph-less
sprint: with no `executionGraph` there is no declared dependency to honour, so
`atomic-sequential` describes the sprint's shape — every commanded master executes atomically —
not a scheduling mechanism, and independent masters proceed concurrently. The closeout queue only
projects each contract's own active/reconciling/vacant waiting candidates; it owns none of those
lifecycle facts and cannot hold one master behind another.

Sync pins source and pre-sync refs in the enclosure-root journal. Conflicts remain in operation-owned
`.sync` worktrees for agent resolution and contract-addressed continuation, or explicit cancellation
restores exact pinned heads and publishes `vacant`. Cleanup releases the exact selected terminal
contract before deleting its naming authority. No compatibility reader, direct-Git recovery, or
contract-presence fallback is admitted.

**Shipped text corrected (260831-LOCR-L36 round 2).** The mirrored runtime document this card
describes — `mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md` —
now carries the contract-scoped doctrine in its own text at `:237-247`: implementation admission is
"a separate, contract-scoped authority"; each canonical series contract owns its own activation
record, so masters that share one exact code/memory source pair "never share this state and one
master's selection never pauses or excludes another"; selection first publishes `reconciling` for
that contract, which "suspends nothing"; the selected contract is source-synced and becomes `active`
only when both protected source tips are current; and multiple nonterminal contracts remain valid.
Its task-authoring paragraph at `:249-254` now says the closeout queue "merely projects active,
reconciling, or vacant waiting candidates" and "owns none of those lifecycle facts". The earlier
shipped-source debt note is therefore removed: a repo-wide grep for `source-pair-scoped`,
`source-pair-selected`, the "logically pauses the former master" admission, one-selected-master-at-a-time
and source-pair activation wording returns 0 hits in the code worktree. The file's source-sync
paragraph at `:258-260` was re-checked: its "moved code/memory source pair" phrase describes
`worktree_sync` reconciling one contract's two protected branches, which is still true
(`source_pair(contract)` derives that pair from the contract), so it is not a serialization claim.

Memory resolution proves the admitted Git history and requires no row list of the `memory.md` it
commits: the ledger is derived state and its rebuild reports the rows it cannot resolve. Repeated code
commits stay valid ordered history, the newest row is current authority, and no global ledger-key
uniqueness rule is admitted. The packaged source text at `:293-299` was corrected together with the
canonical skill, so it no longer asserts that continuation validates every exact parent ledger row
survives.

## Direct-Execution Boundary

The packaged skill now distinguishes ordinary series integration from the narrow direct-landing
route. A fresh series integration aggregates already closed leaves and therefore has no closeout
door of its own; its door authority is explicitly `not-applicable`, independent of
`directExecutionEnabled`. Direct landing is reserved for an explicitly selected leaf delivery
without a leaf enclosure. A fresh leaf still requires its exact claimed closeout/direct-landing
source, and an already-journaled no-door operation remains recoverable only as that exact retained
generation.
