# mcp/src/agents_remember/worktrees/modules/code_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/code_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-31T16:10+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees/modules overview](overview.md)

## Purpose

This module is the narrow policy and process adapter that makes the project-owned source-quality
wrapper a mandatory, fail-closed gate before a worktree closeout creates a code commit.

**It is no longer scoped to one repository.** Until 260731-EFA-L1 the decider read
`repo_name == "agents-remember"`, so for every consuming repository — the product's actual audience
— the gate the product documents as mandatory was a no-op. Availability of the wrapper now decides,
not the repository's name.

## Code Commentary

### Logic

`quality_wrapper_path(code_worktree)` is the single place the wrapper's location is spelled:
`<checkout>/mcp/src/agents_remember/code_quality/check.py` (`QUALITY_WRAPPER`).

`requires_strict_code_quality(code_worktree, *, code_would_commit)` returns
`code_would_commit and quality_wrapper_path(code_worktree).is_file()`. Note the first parameter is
a **checkout path**, not a repository name — see the boundary note below.

`code_quality_gate_preview(code_worktree, *, code_would_commit)` reports which of three states this
closeout is in, via the `status` key:

| `status` | Constant | Meaning |
| --- | --- | --- |
| `no-code-commit` | `GATE_NO_CODE_COMMIT` | Nothing would commit, so nothing to gate. |
| `wrapper-unavailable` | `GATE_WRAPPER_UNAVAILABLE` | Code would commit, but this checkout carries no wrapper. The reason string names `QUALITY_WRAPPER` and states the commit **is not quality-checked**. |
| `enforced` | `GATE_ENFORCED` | The wrapper runs before the commit; `command` is `python -m agents_remember.code_quality.check`. |

`wrapper-unavailable` is a *reported* state, not a silent skip: closeout still proceeds, and the
payload says plainly that the code commit was not quality-checked and why. That is the deliberate
replacement for the old behavior, which returned the same `required: False` for a consuming
repository as for "nothing to commit" and explained it with the misleading reason "no Agents
Remember code commit would be created".

`run_strict_code_quality_gate(code_worktree, runner=run_subprocess)` requires the wrapper to exist
(else `RuntimeError`), selects an interpreter, executes the current worktree's
`agents_remember.code_quality.check`, and raises with a bounded output tail
(`FAILURE_OUTPUT_LINES` = last 40 lines) on any non-zero result. Success returns
`{"required": True, "status": GATE_ENFORCED, "passed": True, "command": ...}`.

`quality_python` prefers the worktree virtualenv, then the linked primary clone's shared
virtualenv, then the active server interpreter. `quality_environment` always puts the current
worktree's `mcp/src` first on `PYTHONPATH`, so a shared interpreter cannot measure the primary
clone by mistake.

### Conventions

The interpreter search is necessary linked-worktree support: linked worktrees intentionally may not
carry their own `.venv`. It is an ordered authority chain, not a command fallback or an escape from
the project-owned wrapper.

`status` is the machine-readable field; `reason` is prose for a human reading the closeout payload.
Callers should branch on `status`, not on `required` alone — `required: False` now covers two very
different situations.

### Invariants And Boundaries

- **The deciders take a checkout `Path`, never a repository name.** `contract.repo_name` is a
  `str`, `contract` is unannotated in `closeout.py`, and `Path`-vs-`str` is not caught there by
  Pyright. Handing a name in makes `quality_wrapper_path` build a relative path off the process
  CWD, which is not a file, so the gate silently never runs. `test_worktree_closeout_quality_gate.py`
  spies on the actual argument for exactly this reason.
- The only deliberate skip is a closeout that would not create a code commit. A checkout without
  the wrapper is *reported*, not skipped silently.
- A missing wrapper, missing interpreter, or non-zero wrapper result refuses before closeout
  mutation.
- The default wrapper command is used as-is; no threshold-enforcement flag is required or accepted.
- Failure output is bounded to the last 40 lines while preserving the actionable exit status.
- Gate applicability must stay a property of the checkout, not of any repository identity. Do not
  reintroduce a name-based branch.

### Todos

- `wrapper-unavailable` is currently reported and permitted. If a consuming repository should be
  able to *require* a gate it cannot run, that is a policy decision this module does not make.

## Docs References

No external Domain Documentation source is configured for this memory repo (`system/sources.md`
has no entries).

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is configured for this repository-local gate. | — | — |

## Repo-Internal References

Closeout owns sequencing, while the quality wrapper owns the actual Ruff, Pyright, Radon, pytest,
coverage, and CRAP checks.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Wrapper presence decides applicability, the preview reports one of three states, and execution preserves current-worktree imports with bounded failure output. | L15-L113 | [code_quality_gate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/code_quality_gate.py) |
| Both closeout call sites pass `contract.code_worktree` — the preview path and the apply path — and the gate runs before `commit_if_dirty`. | L283-L285; L583-L589 | [closeout.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout.py) |
| Regressions cover all three statuses, the checkout-not-name argument at both call sites, worktree source precedence, bounded failures, interpreter selection, and mutation ordering. | L38-L284 | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |
| The contributor documentation states the same three-state contract for consuming repositories. | "Closeout" section | [CONTRIBUTING.md](agents-remember/CONTRIBUTING.md) |

## Cross-Repo References

This gate acts on whatever code worktree closeout hands it, which for a consuming repository is
that repository's checkout rather than this one.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Applicability is decided by the presence of the wrapper in the target checkout, so a sibling repository that vendors the wrapper is gated and one that does not is reported as `wrapper-unavailable`. | L22-L35 | [code_quality_gate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/code_quality_gate.py) |

## Update History

- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/src/agents_remember/worktrees/modules/code_quality_gate.py` and moved the lines this card
  cites, so the Citations column no longer pointed at the code its rows name. Corrected the ranges
  (L15-L117 → L15-L113; L24-L37 → L22-L35). The behaviour described is unchanged — the file's AST
  is identical to the base revision — this is a citation repair only. Verification metadata pinned
  until closeout stamps the L2 commit.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-31T04:28+02:00 — 260731-EFA-L1 removed the repository-name hard-code (L1-R10). The
  deciders now take the code worktree `Path` and gate on wrapper availability, so the gate applies
  to every consuming repository that carries the wrapper instead of only to `agents-remember`.
  Added `quality_wrapper_path`, the `GATE_ENFORCED` / `GATE_NO_CODE_COMMIT` /
  `GATE_WRAPPER_UNAVAILABLE` status constants, and a `status` key on both the preview and the
  successful run result; removed `AGENTS_REMEMBER_REPO` and the misleading "no Agents Remember code
  commit would be created" reason. Recorded the `Path`-not-name boundary because Pyright cannot
  catch that mistake at the unannotated closeout call sites. Verification metadata pinned to the
  pre-leaf source authority until closeout stamps the code commit.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental curator: created the sidecar for mandatory
  pre-code-commit quality enforcement, linked-worktree interpreter selection, current-worktree
  import precedence, and fail-closed bounded error reporting. Verification remains blank until the
  new source is committed.
