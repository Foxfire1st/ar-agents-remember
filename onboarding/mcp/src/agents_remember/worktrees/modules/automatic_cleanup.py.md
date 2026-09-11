# mcp/src/agents_remember/worktrees/modules/automatic_cleanup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/automatic_cleanup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-11T14:50+02:00|
| lastVerifiedCommitHash | `76ce662ab759e3c1d30726b3116472472c3baab5` |
| lastVerifiedCommitDate | 2026-09-11T13:49:27+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[worktrees/modules/overview.md](overview.md)

## Purpose

Runs the existing cleanup procedure automatically after a completed integration and restates its
outcome in operator language. This module owns only the wiring and the report: a completed leaf is
reclaimed without a further prompt, because the landing that just completed is the authorization
for its own terminal reclamation.

## Code Commentary

### Logic

`run_automatic_cleanup(contract)` is the whole public surface. It calls
`cleanup_result` with a `WorktreeArgs` whose `approved=True`, `dry_run=False`, and
`teardown_providers=True`, so the destructive work stays in the existing terminal procedure —
which already proves terminal evidence, archives it and reads it back, and refuses while
authority is live or ambiguous.

Three outcomes fold into one report shape:

- A terminal cleanup state (`_TERMINAL_CLEANUP_STATES` — `cleanup-completed` or `already-clean`)
  with a zero return code is `_completed`. `already-clean` is reported as exactly that: the
  terminal archive already proves reclamation, so the contract's targets are not restated as
  "still in place".
- Any nonzero return code or non-terminal state is `_refused`, carrying the payload's `summary`
  (or state) as the reason plus any `blockers`.
- A raised refusal or crash is caught and reported through the same `_refused` path as
  `"<ExceptionType>: <message>"`.

`_inventory` derives the report's two lists — `removed` and `notRemoved` — for all four target
kinds: worktrees, local branches, the `reports` directory and the enclosure root. Removed entries
come from the cleanup payload (`removed_worktrees` with a truthy `removed`, `branches` with a
truthy `deleted`, and a truthy `directories` cell for the two paths). Kept entries are derived
from the contract itself (`_contract_worktrees` / `_contract_branches`: the code side always, the
memory side only when `memory_mode == "external"`), so a target cleanup never observed is still
reported with `_reason` — `cleanup-did-not-run` when the payload says nothing about it, otherwise
the payload's own reason or `not-removed`.

`_summary` renders the operator sentence. A refused run that had already removed something names
both what was reclaimed and what is still in place; one that removed nothing says so and lists the
four target kinds. A completed run names what was removed and what was left, or states that
nothing was left in place.

`_refused` is the only outcome that adds a `refusal` block —
`{reason, cleanupState, blockers}`. Every report carries `automatic: True`, `state`, `summary`,
`removed` and `notRemoved`.

### Invariants And Boundaries

- The destructive authority is `cleanup_result`'s, not this module's: nothing here removes,
  archives, or proofs anything itself.
- A refusal is reported, never raised. This procedure runs after a successful landing, and turning
  that landing into a reported failure would hide a real integration; the failure stays loud
  through this payload and through the contract's own `cleanup` cell, which the phase machine
  turns into `cleanup-pending`.
- `already-clean` must stay reported as already reclaimed; restating the contract's targets as
  un-removed would state the opposite of what the terminal proof says.
- The removed/notRemoved inventories stay complete over all four target kinds — a silent
  destructive success is not acceptable.
- `teardown_providers=True` and `approved=True` are the wiring contract: cleanup runs
  unattended, on the integration's approval.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring states the automatic-cleanup ruling and the report-never-raise boundary. | module docstring | mcp/src/agents_remember/worktrees/modules/automatic_cleanup.py:1-14 |
| The two terminal cleanup states, and the public entry point that calls the existing procedure with `approved=True` / `dry_run=False` / `teardown_providers=True`. | `_TERMINAL_CLEANUP_STATES`; `run_automatic_cleanup` | mcp/src/agents_remember/worktrees/modules/automatic_cleanup.py:23-23; mcp/src/agents_remember/worktrees/modules/automatic_cleanup.py:28-53 |
| `already-clean` is reported as already reclaimed, with empty removed/notRemoved inventories. | `_completed` | mcp/src/agents_remember/worktrees/modules/automatic_cleanup.py:64-87 |
| The refusal report carries `{reason, cleanupState, blockers}`. | `_refused` | mcp/src/agents_remember/worktrees/modules/automatic_cleanup.py:94-113 |
| The four target kinds are inventoried into `removed` / `notRemoved`; kept targets fall back to the contract's own worktrees and branches. | `_inventory`; `_contract_worktrees`; `_contract_branches` | mcp/src/agents_remember/worktrees/modules/automatic_cleanup.py:116-134; mcp/src/agents_remember/worktrees/modules/automatic_cleanup.py:212-223 |
| Operator summary wording for refused / completed runs. | `_summary` | mcp/src/agents_remember/worktrees/modules/automatic_cleanup.py:226-248 |
| The destructive procedure it delegates to, including its refusal authority. | `cleanup_result` | mcp/src/agents_remember/worktrees/modules/cleanup.py:632-632 |
| The caller that runs this after `integration_status=completed` and reloads the post-cleanup status payload. | `_integrated_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:372-407 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-09-11T14:50+02:00 — Created for the automatic post-integration cleanup at code commit `76ce662ab759e3c1d30726b3116472472c3baab5`: recorded the wiring to `cleanup_result`, the three outcome mappings (terminal / refused / raised), the already-clean reporting rule, the four-kind removal inventory, and the report-never-raise boundary. Read whole-file at that commit; this records source documentation only and makes no acceptance or certification claim.
