# mcp/src/agents_remember/worktrees/modules/record_landing.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

The **pull-request landing route**: record a landing the remote already performed.
`worktree_integrate` lands code by moving refs locally and then records what it moved; when the code
landed through a pull request, AR moved nothing, because `gh pr merge` did. Until this route existed
the contract's `integration` cell stayed `not-started` for every PR landing — and that was not
cosmetic, because the cell is what `worktree_cleanup` requires before it retires a branch and what
the series abandon guard reads before it lets a master's integration branch go. A PR-merged master
therefore looked exactly like a master whose work had never left it.

It is `worktree_record_landing`'s domain half, reached through the MCP tool of that name.

## Code Commentary

### Logic

The PR landing path forwards only the supplied landed code and memory-content commits into the shared `LandedIntegration` writer. It requests no ledger commit and cannot turn cache refresh into evidence that a remote landing occurred.

`record_landing_result(args)`, which since MIK-R09 also asks the mandatory gate on converted memory (section below), cit:([`record_landing_result`], mcp/src/agents_remember/worktrees/modules/record_landing.py:168-253)
refuses unless the call is approved or a dry run
cit:(["recording a landing requires explicit developer approval"], mcp/src/agents_remember/worktrees/modules/record_landing.py:170-170),
loads the contract, and then short-circuits to `already-recorded` when the cell already records a
landed integration — `completed` or `checkpointed`
cit:(["already-recorded"], mcp/src/agents_remember/worktrees/modules/record_landing.py:186-186) —
so a repeat is idempotent rather than a second write.

It then requires the landed commit cit:(["requires landed_code_commit"], mcp/src/agents_remember/worktrees/modules/record_landing.py:203-203)
and resolves the branches that commit may legitimately have landed on. Both shapes occur: a master
integrates into its recorded source branch (the super branch), while a task whose branch was merged
straight to the protected default bypasses super entirely — which is what happened to
`ar/260831_lifecycle-owned-completion-relay`. `_landing_targets` cit:([`_landing_targets`], mcp/src/agents_remember/worktrees/modules/record_landing.py:57-71)
therefore returns the recorded `code_source_branch` plus `main` when it exists locally, keeping only
targets that are actually present.

The anti-fabrication check is an ancestry test against those targets
cit:(["not reachable from any landing target"], mcp/src/agents_remember/worktrees/modules/record_landing.py:215-215):
a commit that landed nowhere cannot set the cell. A `dry_run` reports `would-record` and writes
nothing cit:(["would-record"], mcp/src/agents_remember/worktrees/modules/record_landing.py:226-226).
The real path records `strategy=PR_STRATEGY` cit:([`PR_STRATEGY`], mcp/src/agents_remember/worktrees/modules/record_landing.py:54-54)
through the shared writer, so the cell says which route landed the work. Since 260831-LOCR-L30 the
call bundles its landed facts into the shared `LandedIntegration` record (the same record the local
routes build) and appends no `checkpoint` flag, so this route still records a final landing
cit:([`record_landed_integration`], mcp/src/agents_remember/worktrees/modules/landing_record.py:36-66).

The result payload is built by `_identity_payload` cit:([`_identity_payload`], mcp/src/agents_remember/worktrees/modules/record_landing.py:159-165)
rather than by `status_payload`. That is deliberate: this operation has no worktree or provider state
to report, and avoiding the status payload keeps the operation callable and unit-testable without
bound worktree services.

### 260928-MIK-L09 The Landed Memory Commit Is Checked (MIK-R09 Rule 3)

Record landing commits no memory, but on converted memory it now checks the landed memory commit before the dry-run
and apply branches (`_require_knowledge_gate(contract, commit, landed_memory_content_commit)`, a `RuntimeError` naming
every finding):

- **Probe first (review R1 F7, ruling 2026-09-30T16:07:55).** `_line_converted` probes the official memory line and
  the task's `memory_base_commit` for the layout marker **before** anything reads the landed commit; a probe Git
  cannot answer refuses by name. On an unconverted line the landed commit is only probed (`_commit_converted`), and
  one Git cannot read refuses by its named probe error. A missing or unconverted candidate
  receives the central legacy-format refusal; a present converted candidate reaches `_judged_landing_refusal`
  and its leaf/master pair judgment even when the official line remains legacy (MIK-R46). The prior tip never
  makes a converted candidate legacy or grants an exemption for an unreadable commit.
- **A converted line must name its memory commit** (`_unnamed_memory_commit_refusal`).
- **The leaf pair.** Converted leaf recording requires the contract's memory base by name; no landed-parent fallback replaces a missing base. The actual landed memory commit is judged by `leaf_pair_refusal` with a recomputed worklist over its exact tree. Code is the recorded closeout code commit when the landed commit contains it, otherwise the landed code commit. An unreadable recorded object/ancestry refuses rather than silently selecting another pair. The latest leaf history file must remain closed.
- **The master pair.** Recorded master landing also runs validator, net staleness from the series code base, newly closed history ownership, and the full admitted code/memory chain up to the supplied landed commits, not today's branch tips. A converted route refuses unreadable inputs before either dry-run or apply recording; recording publishes no memory commit or ref.
- **Tests:** `test_record_landing_checks_the_landed_memory_commit_is_closed_and_valid`,
  `test_record_landing_refuses_through_its_route_entry`, and
  `test_a_hand_closed_leaf_file_is_refused_at_closeout_validation_and_record_landing` (F1); real data `closeout.txt`
  step 3.


- The module docstring's gate and probe-first paragraphs. [1]

- Probe the line first; an unconverted line's commit is only probed. [2]


- The gate's request over the landed commit, based on the task's memory base. [3]



- The gate runs before the dry-run and apply branches. [4]


- **Recorded-closeout freezing.** The shared pair judge freezes history files closed in the parents of the contract's recorded closeout memory commit when the judged commit is that commit or descends from it, including a later merge. It freezes nothing for a commit outside that ancestry; newly added rows remain checked. This deliberately supersedes the former exact-recorded-commit-only limit.


- The recorded closeout and its descendants use the recorded-closeout parent freezing policy. [16]


- Newly added or hand-closed history is still judged on the actual landed tree. [17]


### Conventions

The route label is a module constant, not a string literal at the call site, so the cell's value is
greppable and single-sourced.

Refusals raise `RuntimeError` with the corrective action in the message (pull the protected branch
locally, then record the commit it landed) instead of a bare failure.

### Boundaries Of The Recorded State (260831-LOCR-L30)

The `already-recorded` short-circuit covers **both** landing states:
`contract.integration_status in {"completed", "checkpointed"}`
cit:(["contract.integration_status in {\"completed\", \"checkpointed\"}"], mcp/src/agents_remember/worktrees/modules/record_landing.py:180-180),
and the summary branches on which one it found
cit:(["This contract already records a checkpointed integration"], mcp/src/agents_remember/worktrees/modules/record_landing.py:190-190).

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
- **`unknown` must never mean "never landed".** The dashboard projection at
  `worktrees/modules/landing.py` returns `None` when `gh` is absent, unauthed, or errored; that
  polarity is correct for a dashboard and would be dangerous as a deletion gate.
- **It must not become a second writer.** All cell writes go through `landing_record`.
- **It does not move refs, carry memory, or push.** Carryover is C-11's, separately guarded by
  cleanup.

### Todos

None. A standalone PR-tail recording step is required operator doctrine, and it is named as step 8
of the landing flow in the repo's `system/git-workflow.md`.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.


- `record_landing_result` validates the recorded code landing, since MIK-R09 checks the landed memory commit on converted memory (before the dry-run and apply branches), and forwards the actual code/memory facts. [5]


- The shared writer this route calls, and the cell it publishes. (`record_landed_integration`) [6]
- The local route that already recorded its own landing. (`_integrated_result`) [7]

- The `already-recorded` guard covers both landing states, so a checkpointed series is never upgraded into a reclaimable integration. (`contract.integration_status in {"completed", "checkpointed"}`) [8]


- The checkpointed summary preserves its still-open state and names worktree_integrate as its completion route. [9]

- Cleanup refuses until the cell this route sets reads completed. (`integration_status`) [10]
- The dashboard PR probe whose `None`/`missing` polarity must not be read as "never landed". (`_pr_for`) [11]

- The MCP tool and payload that expose this operation. (`worktree_record_landing`) [12]


- The application-layer entry point that confines the contract and builds the arguments. (`worktree_record_landing_tool`) [13]

- The PR landing-tail recording step in operator doctrine. (`worktree_record_landing`) [14]


- Unconverted memory: the lock decides, before a memory commit is required. [15]


### Cross-Repo References

The operation shells out to nothing. Its only external participant is the pull-request itself, which
is recorded rather than queried at decision time, so no live external boundary is cited here.

No additional cross-repository evidence applies.
