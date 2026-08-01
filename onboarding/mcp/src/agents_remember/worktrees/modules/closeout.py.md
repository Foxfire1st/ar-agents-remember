# mcp/src/agents_remember/worktrees/modules/closeout.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/closeout.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T09:40+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns worktree closeout preview/apply behavior.

## Code Commentary

Closeout validates source branch positions and explicit commit approval. When a code commit would
be created **in any repository whose checkout carries the wrapper**, it stages the task worktree and
then runs the strict project-owned quality wrapper over exactly that, before any code, memory,
ledger, contract, or applied-gate mutation. Only after that gate passes does it commit code, refresh
onboarding metadata, route overview metadata, generated route indexes, and
entity fingerprints to the new code commit, run `memory_quality_check`, commit
memory content, update the external memory ledger, and return the closeout
payload.
Closeout is worktree-only: the former direct-closeout functions
(`validate_direct_external_context`, `direct_closeout_preview_payload`,
`direct_closeout_result`) were removed with the direct tool surface (issue #62).
Worktree closeout uses the code worktree as the source of truth for drift and
fingerprint checks after the worktree code commit exists.

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
`lifecycle_id`, `_enforce_closeout_gate` reads the lifecycle's gate log via
`GateStore(observer_logs_root(contract.coordination_root))` — the same log the
dashboard writes — and `controlplane.evaluate_closeout_gate(..., policy=args.gate_policy)` refuses the closeout
unless a `closeout-approval` gate is `approved` by the developer or by a
policy-valid delegated orchestration decision (a model self-approval, owner
self-approval, missing required reviewer verdict evidence, or an
`open`/`rejected`/`applied` gate blocks; a gateless lifecycle falls back to the
chat `--approved` gate, unchanged). The check runs
after the chat approval note and before the code commit; on success
`_mark_closeout_gate_applied` appends an `applied` snapshot so one approval cannot
be replayed. Both preview and apply payloads carry a `closeout_gate` block
(`enforced` / `permitted` / `gateId` / `reason`) for the commit-approval relay.

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

## 260731-EFA-L4: The Gate Stages Before It Gates

`_gate_staged_code(code_worktree, *, diff_base)` replaces the bare
`run_strict_code_quality_gate(...)` call in `closeout_result`. It is four steps, and **the order is
the contract**:

1. `_refuse_outside_a_linked_worktree(code_worktree)`
2. `_refuse_conflicted_worktree(code_worktree)`
3. `require_git(code_worktree, ["reset", "--mixed", "--quiet", "HEAD"])`
4. `require_git(code_worktree, ["add", "-A"])` → `run_strict_code_quality_gate(code_worktree, diff_base=diff_base)`

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
run-strict-code-quality-over-that-staged-content
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

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Ledger updates use the kernel memory ledger parser and renderer. | [memory_ledger.py](agents-remember/mcp/src/agents_remember/kernel/memory_ledger.py) |
| Closeout refresh helpers provide sidecar metadata, route overview metadata, route index, and entity fingerprint updates before the memory commit. | [onboarding.py](agents-remember/mcp/src/agents_remember/worktrees/modules/onboarding.py) |
| Worktree tests cover dry-run previews, approval notes, missing onboarding blocking, route overview/index refresh, memory quality gating, and ledger updates. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| Defines the `WorktreeArgs` dataclass that types every closeout entry point and helper. | [args.py](agents-remember/mcp/src/agents_remember/worktrees/modules/args.py) |
| The pure closeout-gate policy this module enforces (slice 6b). | [controlplane/enforcement.py](agents-remember/mcp/src/agents_remember/controlplane/enforcement.py) |
| The gate policy threaded through `WorktreeArgs`. | [args.py](agents-remember/mcp/src/agents_remember/worktrees/modules/args.py) |
| The gate log read during enforcement and appended to when marking `applied`. | [controlplane/store.py](agents-remember/mcp/src/agents_remember/controlplane/store.py) |
| The strict source-quality adapter decides applicability, executes the current worktree wrapper, and fails before mutation. | [code_quality_gate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/code_quality_gate.py) |
| Focused closeout regressions prove failure preserves code/memory/ledger/contract state and success runs quality before code commit; `CloseoutGateSeesCreatedFilesTests`, `TaskWorktreePreconditionTests`, `ConflictedIndexTests` and `RetryStagesWhatAFirstRunWouldTests` pin the staging step, both refusals, the reset-after-the-conflict-check ordering, and that a refused gate leaves the worktree staged. | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |
| `require_git` — the runner all three staging commands go through. | [git.py](agents-remember/mcp/src/agents_remember/worktrees/modules/git.py) |
| `recovery_guidance` and the `RecoveryOperation` vocabulary the commit-approval gate belongs to, plus `status_payload`. | [guidance.py](agents-remember/mcp/src/agents_remember/worktrees/modules/guidance.py) |
| `ContractCells` and `amend_contract`, plus the no-`replace`-keyword rule the closeout write follows. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |

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
