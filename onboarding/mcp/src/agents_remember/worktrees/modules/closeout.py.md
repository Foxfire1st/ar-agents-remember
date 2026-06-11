# mcp/src/agents_remember/worktrees/modules/closeout.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/closeout.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:20+02:00|
| lastVerifiedCommitHash | `a69b72e101d09423601916c03d4f59ecdee7dda6` |
| lastVerifiedCommitDate | 2026-06-11T11:08:18+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns worktree closeout preview/apply behavior.

## Code Commentary

Closeout validates source branch positions and explicit commit approval, commits
code first, refreshes onboarding metadata, route overview metadata, generated
route indexes, and entity fingerprints to that new code commit, runs
`memory_quality_check`, commits memory content only after the quality gate is
clean, updates the external memory ledger, and returns the closeout payload.
Closeout is worktree-only: the former direct-closeout functions
(`validate_direct_external_context`, `direct_closeout_preview_payload`,
`direct_closeout_result`) were removed with the direct tool surface (issue #62).
Worktree closeout uses the code worktree as the source of truth for drift and
fingerprint checks after the worktree code commit exists.

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

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Ledger updates use the kernel memory ledger parser and renderer. | [memory_ledger.py](agents-remember-md/mcp/src/agents_remember/kernel/memory_ledger.py) |
| Closeout refresh helpers provide sidecar metadata, route overview metadata, route index, and entity fingerprint updates before the memory commit. | [onboarding.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/onboarding.py) |
| Worktree tests cover dry-run previews, approval notes, missing onboarding blocking, route overview/index refresh, memory quality gating, and ledger updates. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |
| Defines the `WorktreeArgs` dataclass that types every closeout entry point and helper. | [args.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/args.py) |

## Update History

- 2026-06-11T08:55+02:00 — No content impact: removed the 8 imports orphaned by the issue #62 deletion (`resolve_context`, `current_branch`, and the direct-path `*_for_context` planners/validators/refreshers) after CI's Ruff F401 gate caught them; pure import cleanup, behavior unchanged.
- 2026-06-11T06:47+02:00 — Removed `validate_direct_external_context`, `direct_closeout_preview_payload`, and `direct_closeout_result` plus the now-unused `MemoryLedger` import (issue #62 worktree-only closeout); the module owns only the worktree closeout path.
- 2026-06-10T05:20+02:00 — Issue #56 sub-task 2: previews additionally expose `route_overview_body_gate`; apply payloads surface `route_overviews_attested_no_impact` and `route_overviews_stamped_without_body_review` (worktree + direct).
- 2026-06-10T04:47+02:00 — Issue #56 sub-task 1: previews expose `sidecar_body_gate` (stale/untraced/attested), and both apply paths surface `sidecars_attested_no_impact` so in-band no-impact attestations show up in the tool response at the commit-approval gate.
- 2026-05-31T12:50+02:00 — All closeout entry points and helpers re-typed from `argparse.Namespace` to the new `WorktreeArgs` dataclass (imported from `modules.args`), dropped `import argparse`, and `closeout_result` added an `args.contract_path is not None` assert; corrected Code Commentary to name the typed param and added the args.py reference (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Typed route-index/memory-quality dicts as `dict[str, Any]`, `validate_direct_external_context` -> `MemoryLedger`; extracted `_refresh_plans_have_work` and `_format_memory_quality_finding` to reduce preview/failure-message complexity; behavior-preserving (commits `0549b28`, `e3dab63`).
- 2026-05-28T15:24+02:00: Updated after closeout began enforcing route overview/index refresh plus a clean memory quality gate before memory commits. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
