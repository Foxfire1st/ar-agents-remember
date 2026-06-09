# mcp/src/agents_remember/memory/carryover.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory/carryover.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00     |
| lastVerifiedCommitHash | `592274a52cec61d97521771c630272c72240ed01` |
| lastVerifiedCommitDate | 2026-06-10T01:38:42+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`carryover.py` is the package-local `c-11-memory-carryover-from-branch` skill implementation for planning and
applying branch-memory carryover after code has landed.

## Code Commentary

### Logic

The module compares old base, source branch, and official branch source changes,
classifies carryover candidates by evidence, and can copy proven onboarding into
official memory while updating metadata and the ledger. `CarryoverRequest`,
`build_plan_for_request()`, and `apply_carryover_for_request()` are the service
entry points used by MCP controllers; CLI commands remain adapters around those
functions. When apply finds nothing actionable to carry (no auto-carry and no
pending review-required candidate), `_nothing_to_carry_result()` still maps an
**unmapped official code HEAD** — e.g. a PR merge commit that landed on top of the
verified tip — to the current memory content commit and commits the ledger,
returning state `ledger-mapped-head`; this removes the manual post-merge ledger
reconciliation a later worktree would otherwise need.

### Invariants And Boundaries

- Only proven evidence tiers auto-carry.
- `evidence_for_path()` returns the strongest `exact-landed-commit` tier only
  when EVERY source-branch commit touching the path is an ancestor of the
  official ref; a single landed commit is not enough, so a later unlanded commit
  to the same path cannot be silently carried over as landed.
- Review-required paths must be selected explicitly before apply.
- `run_git` must never let children inherit the process stdin: under the stdio
  MCP transport that descriptor is the protocol request pipe, and inheriting it
  hung the carryover tools for minutes while their work completed (GitHub #49;
  proven by `test_mcp_stdio_transport.py`). `stdin=DEVNULL` unless explicit
  `input_text` is given (`git patch-id`).
- The MCP facade constrains memory paths to the configured coordination root.
- MCP controllers should pass `intent_note` to the service API and should not
  route through CLI `--approved` / `--approval-note` parsing.
- The post-merge head-mapping only fires when nothing is actionable
  (`auto-carry == 0` and `review-required == 0`) and the official HEAD is not
  already in the ledger; a pending review-required candidate keeps the result
  `nothing-to-carryover` so a behind-memory state is never falsely marked verified.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `memory_carryover_plan` and `memory_carryover_apply` call this module. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| Ledger updates are delegated to kernel memory ledger helpers. | [memory_ledger.py](agents-remember-md/mcp/src/agents_remember/kernel/memory_ledger.py) |

## Update History

- 2026-06-10T05:30+02:00 — `run_git` now sets `stdin=subprocess.DEVNULL` (or explicit `input`): git children inherited the MCP stdio protocol pipe, the proven root cause of the #49 tool-call hangs (stdio harness A/B: 120s hang pre-fix, 3.4s post-fix).
- 2026-06-02T04:00+02:00: `apply_carryover_for_request()` now maps an unmapped official code HEAD to the current memory content (new state `ledger-mapped-head`) when there is nothing actionable to carry — automating the post-merge merge-commit ledger entry so the next worktree needs no manual reconciliation; gated so a pending review-required candidate still returns `nothing-to-carryover`. Added `_nothing_to_carry_result()` plus `find_mapping`/`MemoryLedger` imports. (`l-01-session-job-lifecycle` skill series, Sub-task C, mcp 1.1.0.)
- 2026-05-31T12:30+02:00 — `evidence_for_path()` now requires ALL source-branch commits touching a path to be ancestors of the official ref for `exact-landed-commit`, not just one (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Narrowed `plan['candidates']` to a `list` before iterating to clear a Pyright not-iterable error; behavior-preserving (commit `0549b28`).
- 2026-05-24T00:35+02:00: Updated after adding carryover request/service entry points for MCP controllers.
- 2026-05-23T13:09+02:00: Copied into the MCP package and patched to package imports.
