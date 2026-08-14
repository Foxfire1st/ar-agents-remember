# mcp/src/agents_remember/mcp/registration/closeout.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/mcp/registration/closeout.py`       |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-13T12:26+02:00                                       |
| lastVerifiedCommitHash | `aeca9a2839c965218a61a3040e15cb84367ebeca`                   |
| lastVerifiedCommitDate | 2026-08-14T13:35:55+02:00|
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
altitude-routed gate itself before any merge (leaf targeted; master full with
host-managed RAM/swap by default and an optional explicit
`orchestration.qualityGate.memoryCapBytes`). The registered tool surface is
unchanged.

## Purpose

`register_closeout_tools(server, config)` declares the **landing half** of a worktree-backed task:
`worktree_closeout_preview`, `worktree_closeout_apply`, `worktree_integrate`, `worktree_cleanup`,
`worktree_abandon`.

The public registration entry delegates to three cohesive helpers:
`_register_closeout_command_tools` for preview/apply,
`_register_integration_command_tools` for integration/cancellation, and
`_register_reclamation_command_tools` for cleanup/abandonment. The `_tools` suffix is deliberate:
the structural exemption remains attributable only to tool declarations and registrar functions,
not arbitrary helpers. The split changes registration structure only; tool names, signatures, and
payload owners remain unchanged.

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
  runs the altitude-routed quality gate before any merge (leaf targeted, master full and
  host-managed by default), then moves branch refs; protected branches need explicit approval.
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
- Keep internal registrar helper names ending in `_tools`; the suffix is part of the narrow
  structural-rule attribution for this declaration-only route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The payload builders these forward to. | `worktree_closeout_preview_payload` | mcp/src/agents_remember/mcp/tools/worktree.py:78-86 |
| `CloseoutCommitMessages`, `CloseoutApproval`, and the quality-before-commit ordering. | `CloseoutCommitMessages`; `CloseoutApproval` | mcp/src/agents_remember/application/worktree_tools.py:309-316; mcp/src/agents_remember/application/worktree_tools.py:319-328 |
| The two pre-staging refusals and reset-then-stage Dagger gate described by apply live in the extracted staged-quality owner. | `_refuse_outside_a_linked_worktree`; `_refuse_conflicted_worktree`; `gate_staged_code` | mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py:20-51; mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py:77-129 |
| The wrapper condition decides whether the gate — and therefore staging and its refusals — runs; the preview exposes the selected mode, executor, and cap. | `quality_wrapper_path`; `requires_strict_code_quality`; `code_quality_gate_preview` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:63-65; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:97-104; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:107-169 |
| The approval/message split proved through a live server. | `test_closeout_apply_keeps_the_approval_separate_from_the_messages` | mcp/tests/test_mcp_registration_wiring_tests_2.py:99-119 |
| The closeout descriptions are asserted to pin quality-before-commit. | `test_closeout_tool_descriptions_pin_strict_quality_before_mutation` | mcp/tests/test_tools.py:223-237 |
| The staged-gate behaviour the rewritten descriptions promise. | `CloseoutGateSeesCreatedFilesTests` | mcp/tests/test_worktree_closeout_gate_scope.py:130-208 |

## R39 Integration Tool Contract

The public integration description states that leaf integration lands the acceptance already
bound to its closeout commit without rerunning it. Only master integration owns a new acceptance
run: full mode through the pinned Dagger executor.

## Update History

- 2026-08-14T11:25+02:00 — R39 curator: aligned the registered tool description with the
  leaf-no-rerun/master-full boundary. Verification remains closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: re-anchored the closeout tool descriptions to the
  extracted staged-quality owner and retained the same Dagger-before-commit promise. Verification
  remains closeout-owned.

- 2026-08-13T12:26+02:00 — L23 structural-rail repair: recorded the exact three internal registrar
  names and their `_tools` suffix, which keeps the registration exemption constrained to tool
  declarations/registrars. Public tool names, schemas, descriptions, and payload owners are
  unchanged; verification provenance remains closeout-owned.

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: recorded the three cohesive registration groups while preserving the one public registration entry point and tool contracts. Verification metadata remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: aligned the MCP
  closeout/integration tool descriptions with the host-managed full-gate
  default and optional explicit cap. Verification metadata remains pinned
  until closeout stamps L24.

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
