# mcp/src/agents_remember/worktrees/modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `mcp/src/agents_remember/worktrees/modules` |
| lastUpdated            | 2026-06-10T04:47+02:00|
| lastVerifiedCommitHash | `7cb9c6bf223818a516c443a72ba976a38f6f06e9` |
| lastVerifiedCommitDate | 2026-06-10T05:20:13+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Purpose

The `worktrees/modules` package contains the extracted implementation modules
behind the `git_worktree_manager.py` facade. It separates Git adapters, lifecycle
status guidance, start preparation, onboarding refresh, closeout, integration,
cleanup, abandon, provider teardown, the typed cross-layer argument DTO, and CLI
argument wiring while preserving the public facade import path.

## Hot Path Summary

- `git.py` owns raw Git subprocess operations and small repository state checks.
- `guidance.py` renders lifecycle phase and typed next-operation payloads.
- `start.py`, `closeout.py`, `integrate.py`, `cleanup.py`, and `abandon.py`
  own the named `c-09-git-worktree-manager` skill lifecycle operations. `integrate.py` performs the code and
  memory fast-forwards atomically: it pre-validates that both fast-forwards are
  possible before mutating either branch and rolls both heads back on any
  memory-side failure, so integration never lands a half-integrated state.
  `abandon.py` is the discard-without-integration sibling: it reclaims the
  isolated provider stack and removes worktrees/branches without requiring a
  prior integration.
- `provider_teardown.py` performs full-reclaim teardown of a worktree's
  isolated provider stack (Docker rm -f containers and networks derived from
  persisted settings, then rmtree the provider-runtime tree, reclaiming
  root-owned data via a docker chown when needed). Used by both `cleanup.py`
  and `abandon.py`.
- `onboarding.py` owns closeout-time onboarding metadata and entity fingerprint
  refresh planning, plus the four-case body/history gates
  (`classify_sidecar_updates` / `require_updated_sidecar_content` for file
  sidecars, `classify_route_overview_updates` /
  `require_updated_route_overview_content` for route overviews): a changed
  source's sidecar — and the route overview that is its **nearest governor** —
  must pair a meaningful body change with a new Update History entry, or carry
  an explicit `No content impact:` / `No route impact:` history entry.
  Ancestor-matched overviews are reported as `stamped_without_body_review`
  rather than gating. Previews and apply payloads surface marker-attested
  documents. Shared metadata/route parsing lives in `kernel/onboarding_doc.py`
  and is re-exported here.
- `args.py` defines the frozen `WorktreeArgs` cross-layer DTO that operation
  modules consume in place of `argparse.Namespace`; `from_namespace` builds it
  from partial CLI/controller namespaces with per-field defaults.
- `cli.py` keeps command-line parsing and JSON print adapters out of operation
  modules and converts each parsed namespace into `WorktreeArgs` at the boundary.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The package is imported through the public worktree manager facade. | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Focused worktree tests exercise the facade and operation payloads. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-06-10T05:20+02:00 — Issue #56 sub-task 2: route overviews get the same body gate scoped to nearest-governing routes (`No route impact:` marker; ancestors report as `stamped_without_body_review`), surfaced in closeout previews and apply payloads.
- 2026-06-10T04:47+02:00 — Issue #56 sub-task 1: `onboarding.py`'s content gate became the four-case body/history classification with in-band `No content impact:` attestation, shared parsing helpers moved to `kernel/onboarding_doc.py` (facade re-exports kept), and closeout payloads surface attested sidecars.
- 2026-06-01T00:00+02:00 — Added `abandon.py` (discard without integration) and `provider_teardown.py` (full-reclaim Docker + rmtree teardown) to the Purpose and Hot Path Summary listings.
- 2026-05-31T12:30+02:00 — Documented the new `args.py` typed `WorktreeArgs` cross-layer DTO replacing `argparse.Namespace` and `integrate.py`'s atomic all-or-nothing fast-forward behavior (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created when `c-09-git-worktree-manager` skill worktree lifecycle logic was split into focused implementation modules.
