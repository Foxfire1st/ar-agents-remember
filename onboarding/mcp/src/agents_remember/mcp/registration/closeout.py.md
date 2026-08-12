# mcp/src/agents_remember/mcp/registration/closeout.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/registration/closeout.py`       |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-08T02:00+02:00                                       |
| lastVerifiedCommitHash | `65cb81f7de4db13c0627264fec1eb46f444e0ee3`                   |
| lastVerifiedCommitDate | 2026-08-12T04:57:26+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## 260731-EFA-L17 Change

The five tool declarations are all keyword-only (bare `*` — the L8 remediation completed
here for `worktree_cleanup`/`worktree_abandon`, which still had positional parameters),
and the published docstrings now state the quality altitude ladder: preview/apply
describe the leaf change-set-scoped contract (`--targeted`: changed files +
reverse-import closure + derived test subset, mandatory CRAP over the changed modules)
and say the full wrapper is NOT a leaf gate; `worktree_integrate` states that it runs the
altitude-routed gate itself before any merge (leaf targeted; master full, memory-capped
via `orchestration.qualityGate.memoryCapBytes`). The registered tool surface is
unchanged.

## Purpose

`register_closeout_tools(server, config)` declares the **landing half** of a worktree-backed task:
`worktree_closeout_preview`, `worktree_closeout_apply`, `worktree_integrate`, `worktree_cleanup`,
`worktree_abandon`.

## Code Commentary

### Logic

The preview/apply pair (`worktree_closeout_preview` L24-L46, `worktree_closeout_apply` L47-L76)
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
  runs the altitude-routed quality gate before any merge (leaf targeted, master full +
  memory-capped), then moves branch refs; protected branches need explicit approval.
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
- All ordering, quality-gate execution and git mechanics live in `application/worktree_tools.py`.
- **These docstrings are the published MCP tool descriptions**, so they are contract, not comment:
  a client sees only what they say. Apply's is deliberately conditional ("when code would commit
  AND the checkout carries the project-owned quality wrapper") because an unconditional promise
  would over-claim for a wrapper-less checkout, which runs neither the gate nor its two refusals.
  Keep the wrapper condition, the staging/reset explanation and the two refusals in the text
  whenever the behaviour behind them changes.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The payload builders these forward to. | `worktree_closeout_preview_payload` | mcp/src/agents_remember/mcp/tools/worktree.py:78-86 |
| `CloseoutCommitMessages`, `CloseoutApproval`, and the quality-before-commit ordering. | `CloseoutCommitMessages`; `CloseoutApproval` | mcp/src/agents_remember/application/worktree_tools.py:269-292 |
| The two pre-staging refusals and the reset-then-stage step apply's docstring describes, now running the leaf targeted plan. | `_refuse_outside_a_linked_worktree`; `_refuse_conflicted_worktree`; `_gate_staged_code` | mcp/src/agents_remember/worktrees/modules/closeout.py:728-769; mcp/src/agents_remember/worktrees/modules/closeout.py:770-795; mcp/src/agents_remember/worktrees/modules/closeout.py:796-857 |
| The wrapper condition that decides whether the gate — and therefore the staging step and its refusals — runs at all, plus the mode/cap plan. | `quality_wrapper_path`; `requires_strict_code_quality`; `code_quality_gate_preview`; `QualityGatePlan` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:37-41; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:100-107; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:110-177; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:34-40 |
| The approval/message split proved through a live server. | `test_closeout_apply_keeps_the_approval_separate_from_the_messages` | mcp/tests/test_mcp_registration_wiring_tests_2.py:77-97 |
| The closeout descriptions are asserted to pin quality-before-commit. | `test_closeout_tool_descriptions_pin_strict_quality_before_mutation` | mcp/tests/test_tools.py:223-237 |
| The staged-gate behaviour the rewritten descriptions promise. | `CloseoutGateSeesCreatedFilesTests` | mcp/tests/test_worktree_closeout_quality_gate.py:350-456 |

## Update History

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 citation maintenance: regenerated closeout staging
  ranges after the quality-runner responsibility split; registered behavior is unchanged.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the completed
  keyword-only signatures (cleanup/abandon), the altitude-ladder tool docstrings
  (leaf `--targeted`; full wrapper at the master integration gate, memory-capped;
  `memory_quality_check` per leaf), and refreshed the preview/apply ranges plus the
  closeout/gate reference rows to the post-L17 source. Verification metadata stays
  pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the bare-`*` keyword-only signature remediation (PLR0917). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 5 citation rows (payload builders, CloseoutCommitMessages/CloseoutApproval, wiring/description/staged-gate tests) and converted 2 history prose line citations to cit: forms; the preview/apply ranges L24-L42/L45-L76 verified still exact against the frozen source. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T01:28+02:00 — 260731-EFA-L4 curator: the card summarised both docstrings as
  "apply runs that quality before any code",
  which is now both under- and over-stated. Verified against the diff and the current source and
  corrected it. Preview cit:([`worktree_closeout_preview`], mcp/src/agents_remember/mcp/registration/closeout.py:23-42) now says quality runs "over the staged task worktree" before the
  code commit. Apply cit:([`worktree_closeout_apply`], mcp/src/agents_remember/mcp/registration/closeout.py:44-76) became conditional — the gate runs only when code would commit
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
