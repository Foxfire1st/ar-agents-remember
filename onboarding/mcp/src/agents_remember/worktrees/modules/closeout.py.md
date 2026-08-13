# mcp/src/agents_remember/worktrees/modules/closeout.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/closeout.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-13T12:26+02:00 |
| lastVerifiedCommitHash | `a09b906bbf2855c3479b4d3199607ff8689b7d93` |
| lastVerifiedCommitDate | 2026-08-13T13:51:44+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns worktree closeout preview/apply behavior.

## Code Commentary

Closeout validates source branch positions and explicit commit approval. When a code commit would
be created **in any repository whose checkout carries the wrapper**, it stages the task worktree and
then runs the configured pre-commit hook once, restages any hook edits, and runs the leaf
change-set-scoped quality contract (`--targeted` — changed files +
reverse-import closure + derived test subset, mandatory CRAP over the changed modules) over
exactly that, before any code, memory, ledger, contract, or applied-gate mutation. The full
wrapper is NOT a leaf gate: it runs once per master at the master integration gate with
host-managed RAM/swap by default. After the wrapper's pytest-final subprocess, closeout commits exactly the
certified index with hooks bypassed; it neither reruns the fast hook nor restages the working
tree. Only after that gate passes does it claim the
`closeout-approval` gate (260731-EFA-L5 — the `applied` mutation now sits here, one statement above
the first commit, rather than at the end), commit code, refresh
onboarding metadata, route overview metadata, generated route indexes, and
entity fingerprints to the new code commit, run `memory_quality_check`, commit
memory content, update the external memory ledger, and return the closeout
payload.
The pre-code citation phase is isolated in `_memory_quality_before_refresh`: external-memory
contracts obtain the configured preflight checks and run them against the unstamped base commit,
while other memory modes return an empty result. The actual phase runner, bounded failure
formatting, and two-phase result composition now live in `closeout_memory_quality.py`; this
behavior-preserving extraction keeps the closeout coordinator below the repository's 1,200-line
structural rail without weakening the gate. `closeout_result` still invokes the pre-refresh helper
immediately before deciding and running the strict code-quality gate, and
`_external_closeout_commits` still combines that result with the post-refresh pass before the
memory commit.
Closeout is worktree-only: the former direct-closeout functions
(`validate_direct_external_context`, `direct_closeout_preview_payload`,
`direct_closeout_result`) were removed with the direct tool surface (issue #62).
Worktree closeout uses the code worktree as the source of truth for drift and
fingerprint checks after the worktree code commit exists.

Closeout admission now combines the immediate source-head check with the full task-derived
transitive lineage projection. That source state is checked once at preflight and again after the
memory/code quality work, on the last reversible line before approval claim. A parent branch that
moves during the long gate therefore refuses before the approval is spent or any code, memory,
ledger, or contract commit is created. `_closeout_quality_preflight` owns the reversible memory and
code gates; `_CloseoutResultFacts` and `_closed_result_payload` isolate the completed result shape
without moving any irreversible ordering boundary.

The worklist is no longer dirty-tree-only (issue #83). `closeout_changed_paths`
unions the working tree with `committed_changed_paths(code_worktree,
code_base_commit, code_commit)` — the unverified committed range, excluding
synced-in parallel work and previous closeouts in the same worktree — and both
preview and apply consume that worklist. The onboarding plan receives the
working tier through `working_paths`, so missing sidecars block only for
working-tree paths while committed-range paths without onboarding surface as
the non-blocking `unonboarded` list. Both body gates receive
`contract_memory_verified_commit(contract)` (`ledger_commit` →
`memory_content_commit` → `memory_base_commit`) so sidecar work already
committed in the memory worktree still classifies honestly. When everything is
pre-committed and the tree is clean, `commit_if_dirty` returns the existing
HEAD and metadata stamps to that tip without creating an empty commit.

Payload lists that scale with transported history are bounded (issue #83):
`_bounded_paths` exposes count + sample capped at `PATH_SAMPLE_LIMIT`, applied
to `changed_code_paths`, `changed_code_paths_committed`, the
`onboarding_metadata_refresh` view (`required`/`unonboarded`; the blocking
`missing`/`unsupported` lists stay full), `sidecar_body_gate`,
`sidecars_attested_no_impact`, `refreshed_onboarding`, and
`unonboarded_changed_paths` in the apply payload.

The preview payload exposes the body gates' classifications
(`sidecar_body_gate` from `classify_sidecar_updates` and
`route_overview_body_gate` from `classify_route_overview_updates`), and the
apply path surfaces `sidecars_attested_no_impact`,
`route_overviews_attested_no_impact`, and
`route_overviews_stamped_without_body_review`, so explicit
`No content impact:` / `No route impact:` attestations and happenstance
header stamps are visible at the commit-approval gate instead of only in
memory diffs.

The entry points (`closeout_preview_payload`, `closeout_result`) and the
`_closeout_approval_note` / `_external_closeout_commits` helpers take the typed
`WorktreeArgs` dataclass (imported from `modules.args`) rather than the old
`argparse.Namespace`; `closeout_result` asserts `args.contract_path is not None`
before loading the contract, since `WorktreeArgs.contract_path` is optional.

Since 260731-EFA-L2 `_external_closeout_commits(contract, args, change)` takes a
`VerifiedChange` (from `modules.models`) in place of `changed_paths`, `code_commit`,
`code_commit_date` and `working_paths`. `closeout_result` constructs it once from the values it
already computed, and it is threaded straight into `refresh_onboarding_metadata` and
`refresh_route_overview_metadata_for_context` — so the commit hash, the commit date, the changed
paths and the working subset that all get stamped into onboarding necessarily describe the same
landed change. `refresh_entity_fingerprints_for_context(context, change.changed_paths)` still
takes only the path list, because it stamps no commit.

Server-side gate enforcement (slice 6b, generalized by 260703-L4): when the contract carries a
`lifecycle_id`, closeout reads the lifecycle's gate log via
`GateStore(observer_logs_root(contract.coordination_root))` — the same log the
dashboard writes — and `controlplane.evaluate_closeout_gate(..., policy=args.gate_policy)` refuses the closeout
unless a `closeout-approval` gate is `approved` by the developer or by a
policy-valid delegated orchestration decision (a model self-approval, owner
self-approval, missing required reviewer verdict evidence, or an
`open`/`rejected`/`applied` gate blocks; a gateless lifecycle falls back to the
chat `--approved` gate, unchanged). Both preview and apply payloads carry a `closeout_gate` block
(`enforced` / `permitted` / `gateId` / `reason`) for the commit-approval relay.

**Since 260731-EFA-L5 that enforcement is two functions, not one, and this is the section to read
before changing either — see "The Claim" below.** The old shape —
`_enforce_closeout_gate` checking near the top, `_mark_closeout_gate_applied` appending `applied`
after `write_contract` at the very end — is gone. `_mark_closeout_gate_applied` was **deleted, not
deprecated**.

Task 30 adds the re-closeout reset path for already-integrated leaves. When a
completed integration is legitimately re-closed, source-head validation accepts
the recorded integrated tips in addition to the original base tips. Preview
reports `integration_reopen.would_reopen` when the closeout would create or
transport new unlanded code or memory content. Apply compares the resulting
code and memory-content commits against the contract and recorded source
branches; if either new content commit is not yet on its source branch, closeout
reopens the contract by clearing the integrated commit fields, setting
`integration_status` back to `not-started`, and leaving cleanup pending so
`worktree_integrate` can land the new tip normally. A clean no-op re-closeout
does not reopen integration and avoids duplicating an existing ledger mapping,
so a completed leaf stays completed when no new code or memory content exists.

## 260731-EFA-L17: The Leaf Contract And The Memory-Quality Carve-Out

Both closeout entry points now pass the leaf's targeted plan: `closeout_preview_payload`
(lines 362-434) and `closeout_result` (lines 941-1037) hand
`QualityGatePlan(mode="targeted")` to the preview/run, and `_gate_staged_code`
runs `run_strict_code_quality_gate(QualityGateTarget(code_worktree, worktree_group),
diff_base=..., plan=QualityGatePlan(mode="targeted"))` after the reset+stage. The enclosure
argument routes the complete test/quality transcript to the leaf's stable
`reports/test-results.md`; the successful closeout payload retains its `reportPath`. The preview summary and
the apply flow state the ladder explicitly: the leaf contract is `--targeted` (changed
files + reverse-import closure + derived test subset), the full wrapper is NOT a leaf
gate (once per master at the master integration gate with host-managed memory
by default), and
`memory_quality_check` stays a per-leaf closeout gate (`run_memory_quality_phase` in
`closeout_memory_quality.py`). A leaf closeout cannot skip its required checks: an uncovered changed
production module, a failed targeted run, or a missing wrapper refuses loudly.

## 260731-EFA-L4: The Gate Stages Before It Gates

`_gate_staged_code(code_worktree, *, worktree_group, diff_base)` replaces the bare
`run_strict_code_quality_gate(...)` call in `closeout_result`. It is four steps, and **the order is
the contract**:

1. `_refuse_outside_a_linked_worktree(code_worktree)`
2. `_refuse_conflicted_worktree(code_worktree)`
3. `require_git(code_worktree, ["reset", "--mixed", "--quiet", "HEAD"])`
4. `require_git(code_worktree, ["add", "-A"])`
5. `run_pre_commit_hook_if_configured(code_worktree)` → restage hook edits when configured
6. `run_strict_code_quality_gate(QualityGateTarget(code_worktree, worktree_group), diff_base=diff_base)`

The commit side of the same contract is `commit_verified_staged`: it performs no `add -A` and
uses `git commit --no-verify`, so the configured hook is not restarted after the wrapper's final
pytest subprocess. This is intentionally different from ordinary `commit_if_dirty`, which still
stages and honors hooks for memory and other non-certified commits.

**Why stage at all.** Every rail of the wrapper reads the index: `derive_scope` lists what ruff and
pyright are given with `git ls-files`, and `diff_coverage` diffs the base against the tracked tree.
Closeout commits with `git add -A`, so until it staged first, any file the task **created** — as
opposed to edited — went into the commit without a single rail reading a line of it, and the gate
reported green having never seen it. Leaf 3's `abc7cbcc` shipped four files that way. The index cut
both ways: a path the task deleted stayed in `ls-files` until the deletion was staged, so ruff was
handed a file that no longer existed and took an `E902`. Staging first makes the gate's scope and
the commit's content one set by construction, rather than by a second enumeration that has to be
kept in step. Widening `derive_scope` to `--cached --others --exclude-standard` was the rejected
alternative: it would redefine the pre-commit tier, where staged content is the point, and could not
reach the coverage floor at all, since an untracked file has no diff against any base.

**Why the mixed reset.** `add -A` alone does not make a retry mean the same thing as a first run:
git applies ignore rules only to files it does not already track or have staged, so a path staged by
a refused attempt survives even after the retry adds it to `.gitignore`, and the commit carries it.
That is this leaf's own history — a `.dmypy.json` a type checker dropped in the worktree was staged
by a refused attempt, ignored on the retry, and committed anyway. `--mixed` is index-only, so the
tree the gate certifies is byte-for-byte what the task left on disk; each run recomputes the index
from the working tree under the ignore rules in force *now*.

**Why the reset goes after both refusals.** Ahead of the first it would inflict the exact damage
that refusal prevents — a mixed reset in a checkout somebody works in discards their `git add -p`
selection, and that refusal promises nothing in the checkout was touched. Ahead of the second it
would disarm it silently: `git reset` drops the unmerged index entries and removes `MERGE_HEAD`, so
`diff --diff-filter=U` would report nothing, the conflict refusal would never fire again, and
`add -A` would stage the `<<<<<<<` markers it exists to keep out of a commit. Reset-then-add is one
step wholly downstream of both checks.

**`_refuse_outside_a_linked_worktree`** tests git's own definition of a linked worktree —
`rev-parse --path-format=absolute --git-dir --git-common-dir` returning two different values — and
raises when they are equal. Not the contract's `kind`: `kind` is a label sitting next to the path,
while this constrains the path about to be written. A leaf contract whose `code_worktree` had been
pointed at the primary checkout would pass a `kind` check and still stage in somebody's working
repository, and a series contract genuinely pointing at a disposable worktree would be refused for
no reason. This is not hypothetical — `default_series_contract` sets
`code_worktree=code.repo_path` for a `kind: "series"` contract, i.e. the primary checkout itself,
and nothing else stops such a contract reaching `worktree_closeout_apply`.

**`_refuse_conflicted_worktree`** runs `diff --name-only --diff-filter=U` and refuses on any
unmerged path, reporting the count and up to `PATH_SAMPLE_LIMIT` names. This is a **behaviour
change, not a guard against the impossible**: `git add -A` over an unmerged index does not fail, it
*resolves* every conflict by taking whatever the working tree holds — the file with the markers
still in it — and closeout then committed that.

**No snapshot, no restore.** A refused gate leaves the worktree staged and commits nothing. The
staging is not undone because this is the task's own disposable checkout (which
`_refuse_outside_a_linked_worktree` makes true rather than assumed), nobody holds a partial staging
in it, and the reset means the next attempt does not inherit it anyway. The previous attempt at this
saved the index file aside and copied it back; that machinery is **gone rather than fixed** — it
could not survive `core.splitIndex` (the saved pointer outlives the `sharedindex.<sha>` that
`add -A` expires, leaving `status` exiting 128), it could not survive `SIGTERM`, which is how an MCP
server actually dies, and every guarantee it offered was about a person who is never in this
checkout.

**The preview says all of this.** `closeout_order` replaced its single
`"run-strict-code-quality-if-code-commit"` entry with four:

```
refuse-if-gate-would-run-and-code-checkout-is-not-the-tasks-own-worktree
refuse-if-gate-would-run-and-code-worktree-has-unresolved-merge-conflicts
reset-and-stage-whole-task-worktree-if-gate-would-run
run-configured-pre-commit-hook-once-and-restage-hook-edits
run-strict-code-quality-over-that-staged-content
commit-exactly-certified-code-index-without-rerunning-hooks
```

and the preview `summary` was rewritten to state that the staging step and its two refusals belong
to the gate — so they apply exactly when the preview reports `code_quality_gate.status ==
enforced`. A checkout carrying no wrapper runs no gate, stages nothing early, and commits as it
always has.

### Two smaller contract-integrity changes in the same leaf

- The preview's commit-approval block now calls **`recovery_guidance("request_commit_approval",
  tool="worktree_closeout_apply", ...)`** instead of `next_guidance` (the import changed with it).
  The emitted keys are identical; `request_commit_approval` is a `RecoveryOperation` because this
  payload is a gate rendered as a `FlexibleToolResponse`, not a lifecycle phase reaching
  `WorktreeSummary`.
- The end-of-closeout contract write splits in two: `amend_contract(replace(contract, <free-text
  commits, notes and strategies>), ContractCells(human_review_status="approved",
  closeout_status="completed", integration_status=..., cleanup=...))`. The four vocabulary cells go
  through the typed record so pyright checks them; `replace` carries only the fields that have no
  vocabulary to be checked against. The reopen logic itself is unchanged.

## 260731-EFA-L5: The Claim, And Where It Goes

This leaf found three reproduced ways to spend one human approval twice. Two of them lived in this
file. The framing that explains why the store fix alone was not enough: **durability of a record is
not atomicity of a decision** — the gate log now loses nothing, and this file's defects would have
existed even if it never had.

### The semantic change, stated plainly

**An approval authorises one attempt, not one success.**

A closeout that dies *after* the claim — a crashed process, a failed memory quality gate, a git
error, an ENOSPC — leaves the approval consumed, and the next closeout needs a fresh gate.
`enforcement.evaluate_gate` already words the remedy: *"was already applied; open a fresh gate for a
new mutation"*. This is a deliberate, accepted behaviour change, and the alternative is not a milder
version of it. Marking `applied` at the **end** means the marker is attempted only once the code
commit, the memory commit, the ledger commit and the contract rewrite have all happened — so every
way that write can fail to land leaves a **live approval sitting on top of an unknown amount of
completed, irreversible work**. Both were reproduced. Fail-closed costs a re-approval after a
failure the operator can see; fail-open silently hands the next closeout an approval the human
granted for work that is already done.

A two-phase claim (a `claimed` state finalised to `applied` on success and released back to
`approved` on a clean failure) was considered and **rejected**: the release is exactly the step that
cannot be guaranteed — same write, same late position, same failure modes — so it would need a
reaper to age a stuck `claimed` gate back to spendable, which re-opens this window on a timer and
cannot tell a died-mid-commit closeout from a died-before-commit one.

### Memory-quality phase placement (260731-EFA-L16)

The closeout runs its citation gate — `range_resolution` plus `claim_reopen` — BEFORE the strict
wrapper and the code commit: both checks are working-tree semantics, so they clear without a
commit (the fixer regenerates ranges; a changed construct with a current citation is the
report-only review surface) and a failure rejects in seconds instead of after the 13-minute
suite. The curator clears the same `memory_quality_check` during the leaf, so gate findings are
the exception. The L6 placement ran claim evidence before the code commit with a clearing
condition that required the commit to exist — an unreachable state that deadlocked this leaf's
closeout with 115 unresolvable findings. The post-commit phase keeps drift, document shape, and
history order as the sanity pass over the metadata refresh. The approval-claim ordering is
untouched: `gate_guard` is still claimed before the first irreversible act.

### `_claim_closeout_gate` — the spend

`_claim_closeout_gate(contract, args)` calls
`GateStore.claim_approval(contract.lifecycle_id, kind=CLOSEOUT_GATE_KIND, now=now_iso(), policy=args.gate_policy)`,
which folds the log, applies the policy and appends the `applied` snapshot **inside one held lock**,
and raises the same `closeout blocked by gate enforcement: …` message on a refusal. Two closeouts
racing that line resolve to exactly one spend. The old shape checked in one place and marked applied
about a hundred lines and every commit later, with no lock across the pair; two real processes and a
0.4s body were enough to have both permitted and two `applied` snapshots on disk. A contract with no
`lifecycle_id` returns `None` and the chat `--approved` path governs, unchanged.

### The call site is the design, not a detail

The claim is placed **one statement above the first commit** — after `_gate_staged_code`, immediately
before `commit_if_dirty` — and a source comment at that line says not to move it down past the
commit. Both directions are wrong for a reason:

- **Not earlier.** Everything upstream of that line only *reads*, or only touches the **index of the
  task's own disposable worktree**: source-head validation, the onboarding and route plans, the
  mixed reset and staging, and the strict code-quality gate. A refusal up there changes nothing that
  survives, and a refused code-quality gate is the common case — claiming earlier would burn a
  developer's approval on a refusal that changed nothing.
- **Not later.** Everything below it writes a commit somebody would have to undo, so none of it may
  run on an approval this closeout has not already consumed. That is the fail-open shape the leaf
  removed.

### `_refuse_unsatisfied_closeout_gate` — the early check, renamed because it can only deny

The early check survives, at the same position as before (after the chat approval note, before the
worklist), but it is **renamed** and it **returns nothing**: it can only refuse, never write. It
exists purely so an unapproved closeout is refused *before* it stages the worktree and spends a
minute in the strict code-quality gate.

It is safe to keep precisely because it decides nothing. Its read is unlocked and therefore already
stale by the time it returns, and a stale read there has exactly two outcomes: it refuses a gate
that has since been approved (the operator reruns, and nothing was consumed), or it permits and the
claim re-evaluates the same policy under the lock and refuses there. **It can never be the reason an
approval is spent, because it never writes.** Reading it as the enforcement is the check-then-act
mistake this leaf was called in to remove.

`mcp/tests/test_gate_replay_window.py` pins both halves: the gate is already `applied` by the time
`commit_if_dirty` runs, and a gate failure leaves it `approved`.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Ledger updates use the kernel memory ledger parser and renderer. | `parse_ledger_text`, `ledger_to_text`, `load_ledger` | mcp/src/agents_remember/kernel/memory_ledger.py:52-104; mcp/src/agents_remember/kernel/memory_ledger.py:159-184; mcp/src/agents_remember/kernel/memory_ledger.py:187-190 |
| Closeout refresh helpers provide sidecar metadata, route overview metadata, route index, and entity fingerprint updates before the memory commit. | `refresh_onboarding_metadata`, `refresh_route_overview_metadata_for_context`, `refresh_route_indexes_for_context`, `refresh_entity_fingerprints_for_context` | mcp/src/agents_remember/worktrees/modules/onboarding.py:457-488; mcp/src/agents_remember/worktrees/modules/onboarding.py:491-499; mcp/src/agents_remember/worktrees/modules/onboarding.py:606-652; mcp/src/agents_remember/worktrees/modules/onboarding.py:957-965 |
| The dry-run preview test reports the commit plan. | `test_closeout_dry_run_without_approval_reports_commit_plan` | mcp/tests/test_worktree_support_tests_1.py:957-1010 |
| The approval-note test guards real commits. | `test_closeout_requires_approval_note_for_real_commits` | mcp/tests/test_worktree_support_tests_2.py:39-55 |
| The missing-onboarding test blocks changed-source closeout. | `test_closeout_blocks_missing_onboarding_for_changed_source` | mcp/tests/test_worktree_support_tests_2.py:120-139 |
| The refresh test covers onboarding metadata, route overview/index refresh, and new code commit metadata. | `test_closeout_refreshes_onboarding_metadata_to_new_code_commit` | mcp/tests/test_worktree_support_tests_2.py:77-118 |
| The memory-quality test blocks a memory commit when quality fails. | `test_closeout_blocks_memory_commit_when_memory_quality_fails` | mcp/tests/test_worktree_support_tests_2.py:407-442 |
| The ledger round-trip test covers ledger rendering and prepend behavior. | `test_memory_ledger_roundtrip_and_prepend` | mcp/tests/test_worktree_support_tests_1.py:329-340 |
| Defines the `WorktreeArgs` dataclass that types every closeout entry point and helper. | `WorktreeArgs` | mcp/src/agents_remember/worktrees/modules/args.py:20-82 |
| The pure closeout-gate policy this module enforces (slice 6b). | `GateGuard`, `evaluate_gate`, `evaluate_closeout_gate` | mcp/src/agents_remember/controlplane/enforcement.py:41-53; mcp/src/agents_remember/controlplane/enforcement.py:59-107; mcp/src/agents_remember/controlplane/enforcement.py:110-116 |
| The gate policy threaded through `WorktreeArgs`. | `WorktreeArgs` | mcp/src/agents_remember/worktrees/modules/args.py:20-82 |
| `GateStore.claim_approval` — the compare-and-swap this module now spends an approval through: fold, policy verdict and the `applied` append inside one held `exclusive_access`. It is the only way to spend one; `_mark_closeout_gate_applied` was deleted. | `claim_approval` | mcp/src/agents_remember/controlplane/store.py:190-234 |
| `CONSUMED_APPROVAL_GATE_KINDS` — why the `applied` snapshot this module writes is no longer reclaimed at any age, which is the other half of the replay fix. | `CONSUMED_APPROVAL_GATE_KINDS` | mcp/src/agents_remember/controlplane/interaction_retention.py:52-54 |
| The replay-window regressions: the gate is `applied` before `commit_if_dirty`, and a gate failure leaves it `approved`. | `test_the_applied_record_survives_a_concurrent_gate_log_compaction`, `test_the_approval_is_already_consumed_when_the_first_commit_runs`, `test_a_refusal_before_any_commit_leaves_the_approval_unspent` | mcp/tests/test_gate_replay_window.py:261-290; mcp/tests/test_gate_replay_window.py:582-615; mcp/tests/test_gate_replay_window.py:617-645 |
| The strict source-quality adapter decides applicability, executes the current worktree wrapper under the selected mode/executor, and fails before mutation. | `code_quality_gate_preview`; `requires_strict_code_quality`; `run_strict_code_quality_gate` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:110-171; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:100-107; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:193-266 |
| Focused closeout regressions prove failure preserves code/memory/ledger/contract state and success runs the leaf targeted contract before code commit; `CloseoutGateSeesCreatedFilesTests`, `TaskWorktreePreconditionTests`, `ConflictedIndexTests` and `RetryStagesWhatAFirstRunWouldTests` pin the staging step, both refusals, the reset-after-the-conflict-check ordering, and that a refused gate leaves the worktree staged. | `CloseoutGateSeesCreatedFilesTests`, `TaskWorktreePreconditionTests`, `ConflictedIndexTests`, `RetryStagesWhatAFirstRunWouldTests` | mcp/tests/test_worktree_closeout_quality_gate.py:398-504; mcp/tests/test_worktree_closeout_quality_gate.py:658-781; mcp/tests/test_worktree_closeout_quality_gate.py:784-842; mcp/tests/test_worktree_closeout_quality_gate.py:848-911 |
| `require_git` is the fail-closed facade over the shared Git runner; it preserves raw runner decoding and makes only raised diagnostics transport-safe. | `require_git` | mcp/src/agents_remember/worktrees/modules/git.py:18-29 |
| Closeout routes its staging call sites through `require_git`, supplies both checkout and enclosure in `QualityGateTarget`, and runs the leaf targeted plan. | `_gate_staged_code` | mcp/src/agents_remember/worktrees/modules/closeout.py:774-869 |
| The external-memory citation preflight remains immediately before strict code quality; the extracted helper module owns phase execution and combination without moving this coordinator boundary. | "def _memory_quality_before_refresh("; "def run_memory_quality_phase("; "def combine_memory_quality(" | mcp/src/agents_remember/worktrees/modules/closeout.py:956-965; mcp/src/agents_remember/worktrees/modules/closeout_memory_quality.py:33-80 |
| `recovery_guidance` and the `RecoveryOperation` vocabulary the commit-approval gate belongs to, plus `status_payload`. | `recovery_guidance`, `RecoveryOperation`, `status_payload` | mcp/src/agents_remember/worktrees/modules/guidance.py:37-44; mcp/src/agents_remember/worktrees/modules/guidance.py:137-160; mcp/src/agents_remember/worktrees/modules/guidance.py:441-443 |
| `ContractCells` and `amend_contract` define the contract-cell amendment API. | `ContractCells`, `amend_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:181-196; mcp/src/agents_remember/worktrees/worktree_contract.py:199-227 |
| Closeout uses that amendment API for its contract write and avoids the forbidden `replace` keyword. | `_amended_closeout_contract` | mcp/src/agents_remember/worktrees/modules/closeout.py:917-953 |

## 260731-EFA-L1 Current Commit-Gate Delta

The three quality-gate call sites — `code_quality_gate_preview` in `closeout_preview_payload`, and
`code_quality_gate_preview` plus `requires_strict_code_quality` in `closeout_result` — now pass
`contract.code_worktree` instead of `contract.repo_name`. The gate is no longer hard-coded to this
repository: applicability is decided by whether the target checkout carries
`mcp/src/agents_remember/code_quality/check.py`.

**This call site is type-unsafe by construction.** `contract` is unannotated here, so Pyright does
not object if a `str` repository name is passed where a checkout `Path` is expected — and the
failure is silent, because a relative path built from a name is not a file, so
`requires_strict_code_quality` returns `False` and the mandatory gate never runs.
`test_worktree_closeout_quality_gate.py::test_closeout_hands_the_gate_the_code_worktree_not_the_repository_name`
spies on the actual argument at both entry points for exactly this reason.

The payload's `code_quality_gate.status` now distinguishes `enforced`, `no-code-commit`, and
`wrapper-unavailable`; the last means the commit still happens and the payload states it was not
quality-checked.

## 260718-CHATS-L5I Incremental Commit-Gate Delta

Preview exposes the strict quality requirement and places it first in `closeout_order`. Apply
recomputes whether code would commit, runs the gate before `commit_if_dirty`, and returns the gate
result in the closeout payload. **Since 260731-EFA-L4 the apply path calls `_gate_staged_code`
rather than `run_strict_code_quality_gate` directly, and the single `closeout_order` gate entry
became four** — see the L4 section above. `run_strict_code_quality_gate` remains imported and is
still what actually runs the wrapper, one step inside `_gate_staged_code`.

## Update History
- 2026-08-13T12:26+02:00 — L23 structural-rail repair: documented the behavior-preserving
  extraction of memory-quality phase execution, bounded refusal formatting, and result composition
  into `closeout_memory_quality.py`. The pre-refresh call, post-refresh combination, approval claim,
  and commit ordering remain in their prior fail-closed sequence; verification provenance remains
  closeout-owned.

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: documented transitive lineage plus immediate-head validation at preflight and post-quality before approval claim, and the extracted reversible quality/result-payload helpers. Verification metadata remains closeout-owned.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: corrected the
  closeout preview doctrine to describe host-managed master memory by default;
  leaf targeted behavior is unchanged. Verification metadata remains pinned
  until closeout stamps L24.

- 2026-08-12T03:31+02:00 — 260731-EFA-L22 closeout repair: re-read the `require_git` dependency
  after its diagnostic-boundary change. Closeout still uses the same fail-closed facade and Git
  runner; only malformed failure text is escaped before it crosses MCP serialization.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 citation maintenance: regenerated the staging and retry
  regression ranges after splitting runner policy from closeout mutation; behavior is unchanged.

- 2026-08-11T17:50+02:00 — 260731-EFA-L19 curator: recorded that the closeout quality
  call now carries the owning worktree group in `QualityGateTarget`, so the completed targeted
  transcript is atomically published at the enclosure's stable test-results path and returned in
  the closeout payload. Verification metadata remains pinned until governed closeout.

- 2026-08-10T22:09+02:00 — L21 closeout prerequisite: the hard structural-limit regression in
  the L9 base was repaired without changing behavior by extracting the existing external-memory
  citation preflight into `_memory_quality_before_refresh`; recorded its exact pre-gate call site
  and refreshed the shifted closeout helper citations. Verification metadata stays pinned until
  closeout stamps the L21 code commit.

- 2026-08-10T12:46+02:00 — L9 closeout-order repair: the working-tree memory preflight remains
  first; `_gate_staged_code` now runs the configured fast hook after complete staging, restages
  hook edits, and only then invokes the targeted wrapper. The subsequent code commit uses
  `commit_verified_staged`, which neither restages nor reruns hooks after pytest. Verification
  metadata stays pinned until closeout stamps the repair commit.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the leaf targeted
  contract at both closeout call sites and `_gate_staged_code`, the full-wrapper
  master-gate home, and the `memory_quality_check` per-leaf carve-out; refreshed
  the gate/regression/staging rows to the post-L17 source ranges. Verification
  metadata stays pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-05T22:55+02:00 — 260731-EFA-L16 curator: recorded the citation-gate placement in `closeout_result` — the citation checks (`range_resolution` + `claim_reopen`, working-tree semantics that clear without a commit) run BEFORE the strict wrapper and the code commit as the quick-reject gate, and `_combined_memory_quality` reports the gate and the post-commit sanity phase as one result. Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer semantic correction: split refresh, gate-test, Git-runner, and
  contract-amendment claims so each source owner is independently cited.

- 2026-08-03T03:01:25+02:00 — Curator W3-B02 repaired 11 Repo-Internal citation rows, resolving 22 manifest findings with exact ledger, onboarding, gate-policy, store, retention, quality-gate, focused-regression, guidance, and contract anchors; verification metadata was preserved.
- 2026-08-01T19:45+02:00 — 260731-EFA-L5 (durable store integrity). The card described a gate
  enforcement shape that no longer exists: `_enforce_closeout_gate` returning a guard near the top
  and `_mark_closeout_gate_applied` appending `applied` after `write_contract` at the end.
  Corrections: `_enforce_closeout_gate` is renamed **`_refuse_unsatisfied_closeout_gate`** and now
  returns `None` — it can only deny, never write — and `_mark_closeout_gate_applied` is **deleted,
  not deprecated**. Added the new section for `_claim_closeout_gate`, which spends the approval
  through `GateStore.claim_approval` (fold, policy verdict and `applied` append inside one held
  lock) and is called **one statement above the first commit**, after `_gate_staged_code` and
  immediately before `commit_if_dirty`. Recorded why that position and not another: everything
  upstream only reads or touches the index of the task's own disposable worktree and a refused
  code-quality gate is the common case, so claiming earlier would burn a developer's approval on a
  refusal that changed nothing; everything downstream writes a commit somebody would have to undo.
  Stated the semantic change plainly — **an approval authorises one attempt, not one success** — with
  the fail-closed-versus-fail-open argument and the rejected two-phase `claimed` alternative.
  Recorded that the early check is safe *because* it can only deny, so a stale unlocked read there
  can never be the reason an approval is spent. Updated the Code Commentary opening to place the
  claim in the apply order. Replaced the `controlplane/store.py` reference row and added two.
  Verification metadata pinned until closeout stamps the L5 commit.
- 2026-08-01T09:40+02:00 — 260731-EFA-L4 curator: the card said apply "runs
  `run_strict_code_quality_gate` before `commit_if_dirty`" and that preview "places it first in
  `closeout_order`" — both stale. Apply now calls the new `_gate_staged_code(contract.code_worktree,
  diff_base=contract.code_base_commit)`, and `closeout_order`'s one gate entry became four
  (transcribed verbatim into the new section). Added the "The Gate Stages Before It Gates" section
  for the three new functions — `_refuse_outside_a_linked_worktree` (git's `--git-dir` vs
  `--git-common-dir` test, not the contract's `kind`, because `default_series_contract` sets
  `code_worktree=code.repo_path`), `_refuse_conflicted_worktree` (`diff --name-only
  --diff-filter=U`, a real behaviour change: `add -A` over an unmerged index resolves conflicts to
  the marker-bearing working tree rather than failing), and `_gate_staged_code` itself — with the
  ordering rule that the `reset --mixed` must follow **both** refusals (`git reset` drops unmerged
  entries and `MERGE_HEAD`, which would silently disable the conflict check), why the reset makes
  staging recomputed rather than accumulated, and that there is no snapshot/restore because the
  worktree is disposable. Corrected the preview summary description. Recorded the two smaller
  changes in the same diff: `next_guidance` → `recovery_guidance` for the commit-approval gate, and
  the contract write splitting into `amend_contract(replace(contract, <free text>),
  ContractCells(...))` for the four vocabulary cells. New imports verified: `from pathlib import
  Path`, `require_git` in the `modules.git` block, `recovery_guidance` replacing `next_guidance`,
  and `ContractCells` / `amend_contract` from `worktree_contract`. Re-verified and kept unchanged:
  the L1 three-call-sites section (all still pass `contract.code_worktree`), the L2
  `VerifiedChange` threading, the gate-enforcement and Task 30 reopen sections. Added four
  reference rows. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `_external_closeout_commits` now takes a `VerifiedChange` instead of `changed_paths` /
  `code_commit` / `code_commit_date` / `working_paths`, and threads it into the onboarding and
  route-overview refreshers (which were re-signed to match). No payload or gate behaviour changed.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-31T04:28+02:00 — 260731-EFA-L1: both closeout entry points now hand the quality gate
  `contract.code_worktree` rather than `contract.repo_name`, so the mandatory gate applies to every
  repository whose checkout carries the wrapper. Corrected the previous "no Agents Remember code
  commit means no wrapper run" skip description, which described the removed repository-name
  hard-code. Verification metadata pinned to the pre-leaf source authority until closeout stamps the
  code commit.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental curator: corrected closeout ordering to
  mandatory strict quality before every mutation and documented preview/apply payload evidence plus
  the no-code-commit skip; verification remains pinned until the code commit.

- 2026-07-04T12:32+02:00 — 260703-L4: closeout preview/apply now evaluate
  `closeout-approval` through `args.gate_policy`, so human approvals remain
  binding and delegated orchestration approvals bind only when the trusted
  policy allows them. Verification metadata pinned until closeout stamps the L4
  commit.
- 2026-06-27T21:10+02:00 — Task 30: documented completed-integration
  re-closeout handling. Closeout now reports and applies an integration reopen
  only when a new code or memory-content commit is not yet on the recorded
  source branch, while no-op re-closeout avoids duplicate ledger mapping and
  leaves completed integration state intact. Verification metadata pinned until
  closeout stamps the task-30 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: closeout is now server-side gate-enforcing — `_enforce_closeout_gate` refuses unless the lifecycle's `closeout-approval` gate is developer-approved (gateless lifecycles fall back to the chat `--approved` gate), `_mark_closeout_gate_applied` consumes the approval after the commit, and preview/apply payloads carry a `closeout_gate` block. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-12T19:06+02:00 — Issue #83: worklist = working tree ∪ unverified committed range (`closeout_changed_paths`), two-tier blocking via `working_paths` with the non-blocking `unonboarded` report, body gates baselined at `contract_memory_verified_commit`, and count+sample payload bounding (`_bounded_paths`, `PATH_SAMPLE_LIMIT`).
- 2026-06-11T08:55+02:00 — No content impact: removed the 8 imports orphaned by the issue #62 deletion (`resolve_context`, `current_branch`, and the direct-path `*_for_context` planners/validators/refreshers) after CI's Ruff F401 gate caught them; pure import cleanup, behavior unchanged.
- 2026-06-11T06:47+02:00 — Removed `validate_direct_external_context`, `direct_closeout_preview_payload`, and `direct_closeout_result` plus the now-unused `MemoryLedger` import (issue #62 worktree-only closeout); the module owns only the worktree closeout path.
- 2026-06-10T05:20+02:00 — Issue #56 sub-task 2: previews additionally expose `route_overview_body_gate`; apply payloads surface `route_overviews_attested_no_impact` and `route_overviews_stamped_without_body_review` (worktree + direct).
- 2026-06-10T04:47+02:00 — Issue #56 sub-task 1: previews expose `sidecar_body_gate` (stale/untraced/attested), and both apply paths surface `sidecars_attested_no_impact` so in-band no-impact attestations show up in the tool response at the commit-approval gate.
- 2026-05-31T12:50+02:00 — All closeout entry points and helpers re-typed from `argparse.Namespace` to the new `WorktreeArgs` dataclass (imported from `modules.args`), dropped `import argparse`, and `closeout_result` added an `args.contract_path is not None` assert; corrected Code Commentary to name the typed param and added the args.py reference (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Typed route-index/memory-quality dicts as `dict[str, Any]`, `validate_direct_external_context` -> `MemoryLedger`; extracted `_refresh_plans_have_work` and `_format_memory_quality_finding` to reduce preview/failure-message complexity; behavior-preserving (commits `0549b28`, `e3dab63`).
- 2026-05-28T15:24+02:00: Updated after closeout began enforcing route overview/index refresh plus a clean memory quality gate before memory commits. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
