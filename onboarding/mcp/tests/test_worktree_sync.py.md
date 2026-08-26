# test_worktree_sync.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_worktree_sync.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-26T08:50+02:00                     |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`                         |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                                 |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Covers the resumable, contract-addressed `worktree_sync` transaction over real code and ledgered
external-memory repositories, for ordinary leaf worktrees and operation-owned atomic-series
temporary worktrees.

## Code Commentary

### Logic

`SyncFixture` builds real code and ledgered memory repos with live work branches and a stable
enclosure-root journal; `SeriesSyncFixture` builds canonical series refs and verifies `.sync/code`
and `.sync/memory` temporary worktrees are used then removed with all operation authority refs.

The matrix proves current-pair no-op, consistent-pair/ledger admission, dry-run byte preservation,
atomic base/log advance, code and chosen-memory merge plans, and explicit memory choice. A genuine
conflict is retained with `MERGE_HEAD`, agent-owned file/worktree guidance, and no held integration
lock; a staged resolution continues the same generation and produces the exact two-parent commit.
Cancel preview is read-only, real cancel restores pinned pre-sync heads, and repeat cancel is
idempotent. Terminal continue preview does not garbage-collect leftover refs.

Failure/recovery tests prove invalid input refuses before journal/ref admission; malformed and
identity-invalid journals with no refs archive exact raw bytes and become quarantined terminal
evidence; a nonregular journal entry is renamed opaquely without following its symlink; partial refs
restore every complete side and return exact manual-repair facts for the incomplete side. Skip-memory
records a completed skip plan while leaving the memory base unchanged; chosen memory merge preserves
one ledger mapping after continuation.

The fixture's `ref_value` helper delegates exact ref observation to production `read_ref`; the test
therefore shares the validated-ref/missing-ref contract instead of reimplementing a looser
`rev-parse` interpretation beside the production API.

### Invariants And Boundaries

Real git subprocess fixtures establish `refs/remotes/origin/main` plus symbolic `origin/HEAD` as
the exact repository-default authority, then exercise `sync_result` via `WorktreeArgs` directly
(the application/payload layers are covered by the conformance suite's representative
`worktree_sync` payload).

- Conflicts remain agent-resolvable; the suite must never reintroduce abort-on-conflict assertions.
- Contract path plus stable journal/refs address recovery; no public operation id or queue row is
  accepted as authority.
- Preview cannot fetch, mutate journals, selectors, temporary worktrees, Git refs, or cleanup
  terminal residue.
- Recovery preserves exact raw/opaque evidence and fails into bounded manual repair when authority
  is incomplete rather than guessing.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public sync facade validates, previews, refreshes, rereads under authority, and delegates by contract kind. | `sync_result` | mcp/src/agents_remember/worktrees/modules/sync.py:27-100 |
| Durable resume/continue/cancel routing is owned by the transaction driver. | `sync_contract_under_authority` | mcp/src/agents_remember/worktrees/sync_transaction.py:38-371 |
| Journal/ref/temp-worktree cancellation and recovery are separated from routing. | `cancel_sync`; `recover_unreadable_journal`; `recover_missing_journal`; `cleanup_terminal_residue` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:156-289 |
| Stable no-follow journal observation and quarantine records live at the enclosure root. | `SyncOperationStore`; `observe_sync_operation` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:158-411 |

## Cross-Repo References

No meaningful cross-repository reference applies beyond the explicit code/external-memory Git
fixtures exercised by this suite.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:50+02:00 — Rebound the recovery/cancellation reference to the frozen focused
  function names and range.

- 2026-08-26T08:45+02:00 — Restored canonical Docs/Cross-Repo reference sections for this changed
  sync integration suite card.

- 2026-08-26T08:30+02:00 — Restored the required governing-overview link for the frozen public
  sync integration suite.

- 2026-08-26T06:20+02:00 — Reconciled the fixture's exact-ref helper with the production
  `read_ref` API, removing a duplicate interpretation of Git absence. No test-execution claim is
  made.

- 2026-08-26T03:37+02:00 — Replaced obsolete abort/block coverage with the full resumable-sync
  contract: retained code/memory conflicts, continue/cancel, series temporary worktrees, pinned-ref
  cleanup, preview purity, invalid-input pre-admission refusal, raw/opaque quarantine, and partial
  authority manual repair. Verification remains post-Dagger/closeout-owned.

- 2026-08-17T12:30+02:00 — No content impact: L5 coverage-pragma alignment only; the documented sync behavior is unchanged.

- 2026-08-16T02:51+02:00 — L4 default-branch authority: the repository fixture now installs an
  exact remote default ref and symbolic `origin/HEAD`, allowing sync cases to reach their intended
  source and memory assertions without weakening fail-closed authority.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: rebased the `sync_log` range; exact
  non-fixing check returns zero findings.

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 2 initial citation findings (1 anchor, 0 prose, 1 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep.
  No content impact: `SyncFixture` now builds its contract through
  `default_contract(ContractTask(...), leaf=LeafIdentity(...), code=RepoBranchPlan(...),
  memory=RepoBranchPlan(...))` instead of the flat keyword list, and everything else is
  `ruff format` reflow of the two `git worktree add` argument lists, two `assertEqual` calls,
  and the `subprocess.run` inside `git()`. This card names no `default_contract` keyword, and
  the same repo paths, source/work branches, and base commits are still paired, so the eight
  documented sync cases and their assertions are unaffected.
- 2026-06-10T09:56+02:00: Created with issue #54 sub-task D (8 tests over live-worktree fixtures).
