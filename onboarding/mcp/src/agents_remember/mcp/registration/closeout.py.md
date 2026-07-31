# mcp/src/agents_remember/mcp/registration/closeout.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/registration/closeout.py`       |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-07-31T15:31+02:00                                       |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                   |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[registration route overview](overview.md)

## Purpose

`register_closeout_tools(server, config)` declares the **landing half** of a worktree-backed task:
`worktree_closeout_preview`, `worktree_closeout_apply`, `worktree_integrate`, `worktree_cleanup`,
`worktree_abandon`.

## Code Commentary

### Logic

The preview/apply pair share `CloseoutCommitMessages(code, memory, ledger)`, built in each body from
the three flat message arguments. Apply keeps a **second** object, `CloseoutApproval(intent_note,
dry_run)`, precisely so the approval-bearing half cannot be confused with the commit text: folding
`dry_run` in with the messages would let a preview read as an approved apply.

Both docstrings state the real order, and it is not commit-first: preview reports whether strict
project-owned quality **including mandatory CRAP enforcement** will run before the code commit;
apply runs that quality before any code, memory, ledger, contract, or applied-gate mutation, and
only then commits code, memory and ledger in that order. Preview and approval precede apply.

The three destructive tools forward flat:

- `worktree_integrate(contract_path, strategy='ff-only'|'replay', ledger_commit_message, dry_run)` —
  moves branch refs; protected branches need explicit approval.
- `worktree_cleanup(contract_path, dry_run, teardown_providers=True)` — removes worktrees and merged
  task branches **after** integration, and by default reclaims the worktree's isolated provider stack.
- `worktree_abandon(contract_path, dry_run, force)` — discards a task without integrating it. Unlike
  cleanup it needs no completed integration; without `force` it refuses dirty worktrees and unmerged
  branches and reports the commits, with `force=true` it discards them
  (`git worktree remove --force`, `git branch -D`).

### Invariants And Boundaries

- Keep `CloseoutApproval` separate from `CloseoutCommitMessages`.
- Apply registers `dry_run=False` and is paired with the explicit preview tool — that pairing is the
  gate, so do not add an apply path that skips preview.
- Closeout is worktree-only; the retired `direct_closeout_*` tools are not registered anywhere.
- All ordering, quality-gate execution and git mechanics live in `controllers/worktree_tools.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The payload builders these forward to. | [tools/worktree.py](agents-remember/mcp/src/agents_remember/mcp/tools/worktree.py) |
| `CloseoutCommitMessages`, `CloseoutApproval`, and the quality-before-mutation ordering. | [controllers/worktree_tools.py](agents-remember/mcp/src/agents_remember/controllers/worktree_tools.py) |
| The approval/message split proved through a live server. | [test_mcp_registration_wiring.py](agents-remember/mcp/tests/test_mcp_registration_wiring.py) |
| The closeout descriptions are asserted to pin quality-before-mutation. | [test_tools.py](agents-remember/mcp/tests/test_tools.py) |

## Update History

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The five landing-half
  declarations moved out of `server.py`; preview/apply now pack `CloseoutCommitMessages` and apply
  additionally packs `CloseoutApproval`. Verification metadata pinned to the pre-change commit until
  closeout stamps the L2 code commit.
