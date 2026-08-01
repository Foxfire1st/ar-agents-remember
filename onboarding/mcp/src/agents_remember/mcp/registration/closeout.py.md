# mcp/src/agents_remember/mcp/registration/closeout.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/registration/closeout.py`       |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-01T01:28+02:00                                       |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`                   |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[registration route overview](overview.md)

## Purpose

`register_closeout_tools(server, config)` declares the **landing half** of a worktree-backed task:
`worktree_closeout_preview`, `worktree_closeout_apply`, `worktree_integrate`, `worktree_cleanup`,
`worktree_abandon`.

## Code Commentary

### Logic

The preview/apply pair (`worktree_closeout_preview` L24-L42, `worktree_closeout_apply` L45-L76)
share `CloseoutCommitMessages(code, memory, ledger)`, built in each body from
the three flat message arguments. Apply keeps a **second** object, `CloseoutApproval(intent_note,
dry_run)`, precisely so the approval-bearing half cannot be confused with the commit text: folding
`dry_run` in with the messages would let a preview read as an approved apply.

Both docstrings state the real order, and it is not commit-first. Preview reports whether strict
project-owned quality **including mandatory CRAP enforcement** will run — since 260731-EFA-L4 the
description is specific about *what it runs over*: "over the staged task worktree before the code
commit", not merely "before the code commit".

Apply's docstring was rewritten in the same leaf, and it is now a conditional statement rather
than an unconditional one. It reads: when code would commit **AND the checkout carries the
project-owned quality wrapper**, apply resets the index, stages the whole task worktree, and runs
strict quality with mandatory CRAP enforcement **over exactly that staged content**, before any
code, memory, ledger, contract, or applied-gate **commit**; then commits code, memory and ledger
in order. It states four things the previous text did not:

- **Staging is what lets the gate see files the task created**, not only the ones it edited; the
  **reset** is what makes a retry stage what a first run would, instead of inheriting a refused
  attempt's index.
- **Staging is not undone when the gate refuses** — the checkout staged is the task's own
  disposable worktree.
- The **two refusals guard that staging step**, so they run only where the gate runs: apply
  refuses before staging when the code checkout is not a task worktree (a series/master contract
  records the repository path itself) or has unresolved merge conflicts.
- A checkout carrying **no wrapper** runs neither the gate nor those refusals and reaches the
  ordinary commit step's own `git add -A` exactly as it always has.

The barrier wording also narrowed from "before any … mutation" to "before any … commit", which is
the accurate claim now that staging is itself a mutation the gate performs. MUTATING and
commit-gated: preview and approval precede apply; apply requires `intent_note`.

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
- **These docstrings are the published MCP tool descriptions**, so they are contract, not comment:
  a client sees only what they say. Apply's is deliberately conditional ("when code would commit
  AND the checkout carries the project-owned quality wrapper") because an unconditional promise
  would over-claim for a wrapper-less checkout, which runs neither the gate nor its two refusals.
  Keep the wrapper condition, the staging/reset explanation and the two refusals in the text
  whenever the behaviour behind them changes.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The payload builders these forward to. | — | [tools/worktree.py](agents-remember/mcp/src/agents_remember/mcp/tools/worktree.py) |
| `CloseoutCommitMessages`, `CloseoutApproval`, and the quality-before-commit ordering. | — | [controllers/worktree_tools.py](agents-remember/mcp/src/agents_remember/controllers/worktree_tools.py) |
| The two pre-staging refusals and the reset-then-stage step apply's docstring describes. | `_refuse_outside_a_linked_worktree` L557-L596; `_refuse_conflicted_worktree` L599-L622; `_gate_staged_code` L625-L681 | [worktrees/modules/closeout.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout.py) |
| The wrapper condition that decides whether the gate — and therefore the staging step and its refusals — runs at all. | `quality_wrapper_path` L24-L26; `requires_strict_code_quality` L35-L42; `code_quality_gate_preview` L45-L82 | [worktrees/modules/code_quality_gate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/code_quality_gate.py) |
| The approval/message split proved through a live server. | — | [test_mcp_registration_wiring.py](agents-remember/mcp/tests/test_mcp_registration_wiring.py) |
| The closeout descriptions are asserted to pin quality-before-commit. | — | [test_tools.py](agents-remember/mcp/tests/test_tools.py) |
| The staged-gate behaviour the rewritten descriptions promise. | — | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |

## Update History

- 2026-08-01T01:28+02:00 — 260731-EFA-L4 curator: the card summarised both docstrings as
  "apply runs that quality before any code, memory, ledger, contract, or applied-gate mutation",
  which is now both under- and over-stated. Verified against the diff and the current source and
  corrected it. Preview (L24-L42) now says quality runs "over the staged task worktree" before the
  code commit. Apply (L45-L76) became conditional — the gate runs only when code would commit
  **and** the checkout carries the project-owned quality wrapper — and now states the four facts
  the card was missing: the reset-then-stage-the-whole-worktree step (so the gate sees files the
  task created, not only those it edited, and a retry stages what a first run would rather than
  inheriting a refused attempt's index), that staging is *not* undone when the gate refuses
  (the checkout is the task's own disposable worktree), that the two refusals — code checkout is
  not a task worktree, or has unresolved merge conflicts — guard the staging step and so fire only
  where the gate runs, and that a wrapper-less checkout runs neither and reaches the ordinary
  commit step's `git add -A` unchanged. The barrier wording also narrowed from "before any …
  mutation" to "before any … commit", which is the accurate claim now that staging is itself a
  mutation the gate performs; the two reference rows that echoed "quality-before-mutation" were
  reworded to match. Added the docstrings-are-published-contract invariant, line ranges for the
  preview/apply pair, and two reference rows (the modules implementing the staging/refusals, and
  the gate's test file). The Repo-Internal References header gained the `Citations` column.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The five landing-half
  declarations moved out of `server.py`; preview/apply now pack `CloseoutCommitMessages` and apply
  additionally packs `CloseoutApproval`. Verification metadata pinned to the pre-change commit until
  closeout stamps the L2 code commit.
