# mcp/src/agents_remember/worktrees/modules/record_landing.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

The **pull-request landing route**: record a landing the remote already performed.
`worktree_integrate` lands code by moving refs locally and then records what it moved; when the code
landed through a pull request, AR moved nothing, because `gh pr merge` did. Without this route,
the contract's `integration` cell stays `not-started` for a PR landing — and that is not
cosmetic, because the cell is what `worktree_cleanup` requires before it retires a branch and what
the series abandon guard reads before it lets a master's integration branch go. A PR-merged master
would otherwise look like a master whose work had never left it.

Successful PR recording adds emptyLanding=true for a pair equal to recorded bases; it publishes no Git commits. The recorded result also carries `staleDocuments` (MIK-R124 rule 4): the count of documents the landing made stale and the read that lists them — absent when the landing named no document, while a series master's end keeps `count: 0` when naming inherited debt (`alreadyStale`/`namedOnly`) or post-landing parent repairs (`repairedOnParent`) — computed from the recorded landed memory commit with `master_end` set and `document_base` resolved by `master_document_base` when the contract is a series, so a recorded master landing examines every document against the standing base and an ordinary recording only those its change can move. After recording a final PR landing, `record_landing_result` runs an advisory `briefs/` refresh through `refresh_recorded_landing_memory_briefs` for the recorded code/memory commits and attaches any refresh or unpulled-checkout problem as `briefsProblem` without reversing or failing the recorded landing.

## Code Commentary

### Logic

The PR landing path forwards only the supplied landed code and memory-content commits into the shared `LandedIntegration` writer. It requests no ledger commit and cannot turn cache refresh into evidence that a remote landing occurred.

`record_landing_result(args)`, which also asks the mandatory gate on converted memory (section below), cit:([`record_landing_result`], mcp/src/agents_remember/worktrees/modules/record_landing.py:604-710)
refuses unless the call is approved or a dry run
cit:(["recording a landing requires explicit developer approval"], mcp/src/agents_remember/worktrees/modules/record_landing.py:606-606),
loads the contract, refuses disabled contracts first (`is_disabled_contract`), and then calls `abandoned_contract_reason(contract)` (lines 612-619) **before** the `already-recorded` short-circuit: when `contract.cleanup == "abandoned"` or the contract's own task document reads `"abandoned"`, it returns `state_refusal_result(..., state="refused", code=CONTRACT_ABANDONED_CODE, error=abandoned_reason)` (`"contract-abandoned"`) in both dry run and apply without overwriting `cleanup: abandoned`, while leaving missing or unreadable task documents to the existing checks. For non-abandoned contracts, it short-circuits to `already-recorded` when the cell already records a
landed integration — `completed` or `checkpointed`
cit:(["already-recorded"], mcp/src/agents_remember/worktrees/modules/record_landing.py:633-633) —
so a repeat is idempotent rather than a second write.

It then requires the landed commit cit:(["requires landed_code_commit"], mcp/src/agents_remember/worktrees/modules/record_landing.py:514-514)
and resolves the branches that commit may legitimately have landed on. Both shapes occur: a master
integrates into its recorded source branch (the super branch), while a task whose branch was merged
straight to the protected default bypasses super entirely — which is what happened to
`ar/260831_lifecycle-owned-completion-relay`. `_landing_targets` cit:([`_landing_targets`], mcp/src/agents_remember/worktrees/modules/record_landing.py:88-102)
therefore returns the recorded `code_source_branch` plus `main` when it exists locally, keeping only
targets that are actually present.

The anti-fabrication check is an ancestry test against those targets
cit:(["not reachable from any landing target"], mcp/src/agents_remember/worktrees/modules/record_landing.py:544-544):
a commit that landed nowhere cannot set the cell. A `dry_run` reports `would-record` and writes
nothing cit:(["would-record"], mcp/src/agents_remember/worktrees/modules/record_landing.py:658-658).
The real path records `strategy=PR_STRATEGY` (imported from `worktrees/integration/standalone_pr_landing.py:26`, used at line 668)
through the shared writer, so the cell says which route landed the work. The
call bundles its landed facts into the shared `LandedIntegration` record (the same record the local
routes build) and appends no `checkpoint` flag, so this route still records a final landing
cit:([`record_landed_integration`], mcp/src/agents_remember/worktrees/modules/landing_record.py:36-66).

The result payload is built by `_identity_payload` cit:([`_identity_payload`], mcp/src/agents_remember/worktrees/modules/record_landing.py:438-444)
rather than by `status_payload`. That is deliberate: this operation has no worktree or provider state
to report, and avoiding the status payload keeps the operation callable and unit-testable without
bound worktree services.

### Landed Memory Commit Gate (MIK-R09 Rule 3)

Recording publishes no Git commit. Converted pair judgment precedes new dry-run and apply recording. The public precondition adapter answers recognized legacy-format and knowledge-gate refusals before a record write, retaining the sentence and bounded detail. Only a complete stale-entry-only finding set on a non-leaf may remain as debt after reachability and the independent landed-chain proof pass; mixed or truncated findings and converted-leaf staleness still refuse:

- **Probe first (review R1 F7, ruling 2026-09-30T16:07:55).** `_line_converted` probes the official memory line and
  the task's `memory_base_commit` for the layout marker **before** anything reads the landed commit; a probe Git
  cannot answer refuses by name. On an unconverted line the landed commit is only probed (`_commit_converted`), and
  one Git cannot read refuses by its named probe error. A missing or unconverted candidate
  receives the central legacy-format refusal; a present converted candidate reaches `_judged_landing_refusal`
  and its leaf/master pair judgment even when the official line remains legacy (MIK-R46). The prior tip never
  makes a converted candidate legacy or grants an exemption for an unreadable commit.
- **A converted line must name its memory commit** (`_unnamed_memory_commit_refusal`).
- **The leaf pair.** Converted leaf recording requires the contract's memory base by name; no landed-parent fallback replaces a missing base. The actual landed memory commit is judged by `leaf_pair_refusal` with a recomputed worklist over its exact tree. Code is the recorded closeout code commit when the landed commit contains it, otherwise the landed code commit. An unreadable recorded object/ancestry refuses rather than silently selecting another pair. The latest leaf history file must remain closed.
- **The master pair.** Recorded master landing also runs validator, net staleness from the series code base, newly closed history ownership, and the full admitted code/memory chain up to the supplied landed commits, not today's branch tips. For a series contract, `_landing_request` sets `master_end=True` and `document_base=master_document_base(contract, code_commit=code, memory_commit=memory_commit)` so dependent-document staleness checks only this master's own work against the standing base and exempts documents already repaired on the parent line after landing. A converted route refuses unreadable inputs before either dry-run or apply recording; recording publishes no memory commit or ref.
- **Tests:** `test_record_landing_checks_the_landed_memory_commit_is_closed_and_valid`,
  `test_record_landing_refuses_through_its_route_entry`, and
  `test_a_hand_closed_leaf_file_is_refused_at_closeout_validation_and_record_landing` (F1); real data `closeout.txt`
  step 3.


- The module docstring's gate and probe-first paragraphs.

- Probe the line first; an unconverted line's commit is only probed.


- The gate's request over the landed commit, based on the task's memory base.



- The gate runs before the dry-run and apply branches.


- **Recorded-closeout freezing.** The shared pair judge freezes history files closed in the parents of the contract's recorded closeout memory commit when the judged commit is that commit or descends from it, including a later merge. It freezes nothing for a commit outside that ancestry; newly added rows remain checked.


- The recorded closeout and its descendants use the recorded-closeout parent freezing policy.


- Newly added or hand-closed history is still judged on the actual landed tree.


### Named stale-entry debt

When those preconditions accept debt, `staleEntries` carries its count, full finding sentences, `<path>#<entry id>` record keys and the knowledge-maintenance remedy. Dry run returns the same debt without writing the contract. Apply passes the keys to the shared landing writer, which preserves them in `WorktreeContract.stale_entries`.

`test_the_record_landing_tool_names_the_entries_it_keeps` proves debt transport through the real payload, finalization, log, public projection and contract persistence after actual admission. It carries real gate-produced findings across the precondition boundary after supported synchronization clears the net diff. A public stale-debt recording remains unexercised. No supported sequence preserving that complete case was found because supported synchronization advances the code base to the landed tip; this is the approved nearest-boundary proof limit. `test_stale_entry_debt_does_not_skip_the_recorded_master_chain` separately calls the real public tool in dry and apply modes and asserts a chain refusal with the contract unchanged.

### Conventions

The route label `PR_STRATEGY` and refusal code `CONTRACT_ABANDONED_CODE` are single-sourced constants in `worktrees/integration/standalone_pr_landing.py` imported here (lines 46-50), rather than string literals at call sites.

Reachable task-state preconditions return `ok:false`, their existing code and unchanged sentence before any landing record is written; caller bugs, I/O failures and unrecognized internal failures retain their named exception behavior. Legacy-format recovery is selected from the central refusal’s existing case value, not its text: converted-source case offers `worktree_sync` with the exact contract and merge-memory arguments; never-converted case offers the first-conversion program/subcommand and actual memory/code roots as separate values with a `shlex.join` display; unknown case offers no next step. The presentation changes neither conversion admission nor sync behavior.

### Boundaries Of The Recorded State

The `already-recorded` short-circuit covers **both** landing states:
`contract.integration_status in {"completed", "checkpointed"}`
cit:(["contract.integration_status in {\"completed\", \"checkpointed\"}"], mcp/src/agents_remember/worktrees/modules/record_landing.py:627-627),
and the summary branches on which one it found
cit:(["This contract already records a checkpointed integration"], mcp/src/agents_remember/worktrees/modules/record_landing.py:637-637).

The `checkpointed` half is not cosmetic. The full-record path below writes `completed` plus
`cleanup="pending"`, and that pending cleanup is exactly what `worktree_cleanup` requires before it
retires a branch; letting the pull-request route take it would have revoked the checkpoint's
guarantee that a series which landed while still open never becomes reclaimable. Completion stays
with `worktree_integrate`, which reaches it only once the series is genuinely terminal, so this route
still adds no `checkpoint` flag and offers no way to record a non-final landing — it simply declines
to overwrite one that is already recorded.

#### Invariants And Boundaries

- **Never probe `gh`.** Inferring the PR route after the fact would put the network in front of a
  guard that authorizes branch deletion. Recording happens where `gh` necessarily exists — the PR
  tail — and the decision stays offline.
- **`unknown` must never mean "never landed".** `_pr_for` returns `None` when `gh` is absent, unauthed or errored; `_pr_ref` renders that as `unknown` with `factState: missing`. That observation is not a deletion gate.
- **It must not become a second writer.** All cell writes go through `landing_record`.
- **It does not move refs, carry memory, or push.** Carryover is C-11's, separately guarded by
  cleanup.

### Todos

None. `worktree_record_landing` is named as item 4 of the ordinary development landing in this
repository's `system/task-publication.md` - the `local` workflow, where the merge that carries the
branch is the landing and the record is written against it. A repository that lands by pull
request publishes an already-integrated `H` through its own numbered steps and does not invoke
this standalone recording step; the operation's semantics are unchanged either way.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.


- The handler consults the landing preconditions before dry/apply publication and retains the actual code and memory facts. [5]


- The `already-recorded` guard covers both `completed` and `checkpointed` states so a checkpointed series is never upgraded into a reclaimable integration. [8]


- The checkpointed summary preserves its still-open state and names `worktree_integrate` as its completion route. [9]


- `record_landing_result` refuses abandoned contracts and abandoned task documents with `CONTRACT_ABANDONED_CODE` (`contract-abandoned`) before the `already-recorded` short-circuit without overwriting `cleanup: abandoned`. [20]


- `_landing_request` sets `master_end=True` and `document_base=master_document_base(contract, code_commit=code, memory_commit=memory_commit)` for series contracts (and `None` for leaves). [19]

- Conversion guidance follows the central case value, with exact sync arguments or separately carried first-conversion argv; unknown supplies no step. [18]

- The shared writer this route calls, and the cell it publishes. (`record_landed_integration`) Anchor: `record_landed_integration` [6]

- The local route that already recorded its own landing. (`_integrated_result`) [7]

- Cleanup refuses until the cell this route sets reads completed. (`integration_status`) [10]


- The dashboard PR probe whose `None`/`missing` polarity must not be read as "never landed". (`_pr_for`) [11]


- The MCP tool and payload that expose this operation. (`worktree_record_landing`) [12]



- The application-layer entry point that confines the contract and builds the arguments. (`worktree_record_landing_tool`) [13]


- The PR landing-tail recording step in operator doctrine, a verified local memory document rather than a code-source anchor.





- Recording probes the source line and recorded base first; a converted supplied memory output reaches its leaf/master judgment even when those prior inputs are unconverted. Anchor: `_knowledge_gate_refusal` [15]





- Advisory post-recording `briefs/` refresh attaches `briefsProblem` on recorded PR landings. [21]

### Cross-Repo References

Recording performs local Git reads to verify candidate objects and target reachability. It makes no network pull-request lookup and publishes no Git commit or ref; the external pull request has already landed.

No additional cross-repository evidence applies.
