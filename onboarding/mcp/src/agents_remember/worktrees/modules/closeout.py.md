# mcp/src/agents_remember/worktrees/modules/closeout.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/closeout.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T04:28+02:00|
| lastVerifiedCommitHash | `c1dc5056ffa45cc7fe1af66a6d5c38497fbfa5f6` |
| lastVerifiedCommitDate | 2026-07-31T04:58:22+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns worktree closeout preview/apply behavior.

## Code Commentary

Closeout validates source branch positions and explicit commit approval. When a code commit would
be created **in any repository whose checkout carries the wrapper**, it runs the strict
project-owned quality wrapper before any code, memory, ledger, contract, or
applied-gate mutation. Only after that gate passes does it commit code, refresh
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
| Focused closeout regressions prove failure preserves code/memory/ledger/contract state and success runs quality before code commit. | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |

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
recomputes whether code would commit, runs `run_strict_code_quality_gate` before
`commit_if_dirty`, and returns the gate result in the closeout payload.

## Update History

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
