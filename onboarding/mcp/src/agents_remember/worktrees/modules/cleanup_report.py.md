# mcp/src/agents_remember/worktrees/modules/cleanup_report.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/worktrees/modules/cleanup_report.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-12T19:50+02:00 |
| lastVerifiedCommitHash | `532aaa786becbb7d9f87bb64235fc804d7074743` |
| lastVerifiedCommitDate | 2026-09-12T22:27:17+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[worktrees/modules/overview.md](overview.md)

## Purpose

Shapes the operator-facing report for a terminal reclamation that **already happened**. This is a
reporter, not a runner: it removes nothing, proves nothing, refuses nothing, and reaches no Git.

Reclamation itself belongs to `lifecycle_finalize_task`. Its
`_run_or_verify_cleanup` calls
`cleanup_result` cit:([`cleanup_result`], mcp/src/agents_remember/worktrees/modules/cleanup.py:632-707),
which archives the terminal evidence and refuses while authority is live or ambiguous, and then hands
the successful payload here:
`cleanup_report(contract, result.payload)`
cit:([`cleanup_report`], mcp/src/agents_remember/worktrees/modules/cleanup_report.py:28-53). The
split exists because the two halves have different lifetimes: the run-and-catch wiring that used to
sit beside this shaping was unreachable once reclamation moved behind finalization, while the report
is exactly what an operator still reads afterwards.

## Code Commentary

### Logic

`cleanup_report(contract, payload)` returns the report dict, and it is the whole public surface.
Every report carries `automatic: True`, `state`, `summary`, `removed` and `notRemoved`
cit:([`cleanup_report`], mcp/src/agents_remember/worktrees/modules/cleanup_report.py:28-53).

The `state == ALREADY_CLEAN` short-circuit is the one special case: the terminal archive already
proves the enclosure was reclaimed, so nothing remained to remove, and reporting the contract's own
targets as "still in place" would state the opposite of what that proof says. Both inventories are
empty and the summary says "already reclaimed"
cit:(["ALREADY_CLEAN = \"already-clean\""], mcp/src/agents_remember/worktrees/modules/cleanup_report.py:23-23).

Otherwise `_inventory` derives the report's two lists for all four target kinds — worktrees, local
branches, the `reports` directory and the enclosure root
cit:([`_inventory`], mcp/src/agents_remember/worktrees/modules/cleanup_report.py:60-79):

- Removed entries come from the cleanup payload: `removed_worktrees` with a truthy `removed`,
  `branches` with a truthy `deleted`, and a truthy `directories` cell for the two paths
  cit:([`_removed_worktrees`, `_removed_branches`], mcp/src/agents_remember/worktrees/modules/cleanup_report.py:81-87; mcp/src/agents_remember/worktrees/modules/cleanup_report.py:102-108).
- Kept entries are derived from the **contract** itself, not the payload
  cit:([`_contract_worktrees`, `_contract_branches`], mcp/src/agents_remember/worktrees/modules/cleanup_report.py:156-169):
  the code side always, the memory side only when `memory_mode == "external"`. A target cleanup never
  observed is therefore still reported, with `_reason` supplying `cleanup-did-not-run` when the payload
  says nothing about it, and otherwise the payload's own reason or `not-removed`
  cit:([`_reason`], mcp/src/agents_remember/worktrees/modules/cleanup_report.py:150-153).

`_summary` renders the one operator sentence: `"Automatic cleanup removed 2 worktrees, 2 local
branches, 1 reports directory, 1 enclosure root; nothing was left in place."` where
`_inventory_phrase`/`_counted` build each counted clause and drop the empty ones
cit:([`_summary`, `_inventory_phrase`, `_counted`], mcp/src/agents_remember/worktrees/modules/cleanup_report.py:170-175; mcp/src/agents_remember/worktrees/modules/cleanup_report.py:178-185; mcp/src/agents_remember/worktrees/modules/cleanup_report.py:188-191).
`_presented`/`_absent` translate a directory's boolean into the removed or not-removed list
cit:([`_presented`, `_absent`], mcp/src/agents_remember/worktrees/modules/cleanup_report.py:132-142).

### Conventions

The shaping is pure by construction: it reads the payload and the contract's declared targets and
returns a new dict. There is no `try`, no mutation of `payload`, no filesystem probe, and no
`__all__`/CLI/MCP surface — this is a reporting helper, not an operation.

### Invariants And Boundaries

- **A reporter, never a runner.** Nothing here removes, archives, proves, or refuses. The destructive
  authority stays with `cleanup_result`; if this module ever needs to *check* something, that check
  belongs in the caller or in cleanup itself.
- **A refused or failed cleanup never reaches this shaper.** `_run_or_verify_cleanup` returns cleanup's
  payload unchanged when `args.dry_run` or `result.returncode != 0`, so a refusal keeps its
  `blockers`, its partial removal inventory and its citation-cache facts instead of being flattened
  into a completed-reclamation sentence. That gate lives in the caller, and this module must not
  grow a fallback that re-shapes those payloads.
- **`already-clean` must stay reported as already reclaimed.** Restating the contract's targets as
  un-removed would contradict the terminal proof.
- **The `removed`/`notRemoved` inventories stay complete over all four target kinds** — a silent
  destructive success is not acceptable.
- **Absence of a key is reported, not invented.** `_entries` tolerates a missing or non-dict payload
  cell by treating it as empty, and `_reason` names `cleanup-did-not-run` rather than guessing.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo, and the claims here are
repository-internal report semantics, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public entry point and the `already-clean` short-circuit that reports a proven prior reclamation. | `cleanup_report`; "ALREADY_CLEAN = \"already-clean\"" | mcp/src/agents_remember/worktrees/modules/cleanup_report.py:23-53 |
| The four target kinds are inventoried into `removed` / `notRemoved`; kept targets fall back to the contract's own worktrees and branches. | `_inventory`; `_contract_worktrees`; `_contract_branches`; `_reason` | mcp/src/agents_remember/worktrees/modules/cleanup_report.py:60-79; mcp/src/agents_remember/worktrees/modules/cleanup_report.py:150-169 |
| The counted operator sentence naming what was removed and what was left in place. | `_summary`; `_inventory_phrase`; `_counted` | mcp/src/agents_remember/worktrees/modules/cleanup_report.py:170-175; mcp/src/agents_remember/worktrees/modules/cleanup_report.py:178-185; mcp/src/agents_remember/worktrees/modules/cleanup_report.py:188-191 |
| Removed entries come from the cleanup payload's own observation of each target. | `_removed_worktrees`; `_removed_branches`; `_presented` | mcp/src/agents_remember/worktrees/modules/cleanup_report.py:81-87; mcp/src/agents_remember/worktrees/modules/cleanup_report.py:102-108; mcp/src/agents_remember/worktrees/modules/cleanup_report.py:132-136 |
| **The caller.** It runs `cleanup_result`, short-circuits an already-completed cell, and shapes a real successful reclamation through this module — deliberately not when `dry_run` or the return code is nonzero, so a preview or refusal is reported in cleanup's own words. | `_run_or_verify_cleanup`; "cleanup_report(contract, result.payload)" | mcp/src/agents_remember/worktrees/modules/finalize.py:277-311; mcp/src/agents_remember/worktrees/modules/finalize.py:310-310 |
| The destructive procedure and its refusal authority, which this module deliberately does not duplicate. | `cleanup_result` | mcp/src/agents_remember/worktrees/modules/cleanup.py:632-707 |
| The contract fields the kept-inventory fallback reads: the memory side exists only for external memory, and the two directory targets are derived from the worktree group. | `WorktreeContract`; `memory_mode`; `worktree_group` | mcp/src/agents_remember/worktrees/worktree_contract.py:229-239; mcp/src/agents_remember/worktrees/worktree_contract.py:234-234; mcp/src/agents_remember/worktrees/worktree_contract.py:239-239 |

## Cross-Repo References

This is an in-process report shape with no separate repository or external-system boundary, so there
is no cross-repository protocol to cite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-12T17:57:35+00:00: Generated citation repair: `_summary`; `_inventory_phrase`; `_counted` repointed to mcp/src/agents_remember/worktrees/modules/cleanup_report.py:170-175; mcp/src/agents_remember/worktrees/modules/cleanup_report.py:178-185; mcp/src/agents_remember/worktrees/modules/cleanup_report.py:188-191. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T17:57:35+00:00: Generated citation repair: `_summary`; `_inventory_phrase`; `_counted` repointed to mcp/src/agents_remember/worktrees/modules/cleanup_report.py:170-175; mcp/src/agents_remember/worktrees/modules/cleanup_report.py:178-185; mcp/src/agents_remember/worktrees/modules/cleanup_report.py:188-191. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T19:50+02:00 — Created by the 260831-LOCR-L31 curator pass for the new module at the leaf
  base commit `5410fb07`. Records it plainly as a **reporter, not a runner**: the extraction preserved
  only the pure report-shaping half of the deleted `automatic_cleanup.py` (`cleanup_report` plus its
  `_inventory`/`_summary`/`_presented`/`_absent`/`_reason` helpers), while the run-and-catch half
  (`run_automatic_cleanup`, `_refused`, `_TERMINAL_CLEANUP_STATES`, `_refusal_reason`) was dropped as
  unreachable — a non-zero-returncode cleanup is now passed through raw so its `blockers` and partial
  inventory survive. Names `finalize::_run_or_verify_cleanup` as the caller, including its
  `dry_run`/nonzero-returncode gate, and records the removed/notRemoved completeness and
  `already-clean` invariants. Verification metadata is pinned to the leaf base commit and remains
  closeout-owned; this is source documentation only and makes no acceptance claim.
