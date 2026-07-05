# l-01-agent-lifecycles/templates/manager-brief.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/manager-brief.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T16:30+02:00                     |
| lastVerifiedCommitHash | `19d76dbd73673ffc72d0ee1b6a868ac2fdf15ad0`                                  |
| lastVerifiedCommitDate | 2026-07-05T16:23:40+02:00|

## Purpose

The manager dispatch packet — the "ninth template" the adversarial review demanded (AR-12): the
orchestrator compiles a manager's entire session start from this shape, ending the
manager-dispatch folklore the same way worker-brief.md ended the worker's. It carries the ONE
load-bearing base fact only the orchestrator's own file used to state: the manager's master
integration branch bases off the **current super branch** (with the super-tip commit written in as
the reconciliation anchor), never off main.

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/templates/manager-brief.md`. Opens with the canonical `ROLE BRIEF —
manager` header line (the router's condition-2 recognizer). Placeholder slots: the master + its
leaf list with dependency notes; orchestrator-compiled trust facts (no checkpoint re-run); the
branch base block (master branch off the CURRENT super @ tip); dispatch defaults (worker-brief
template, `AR_SPAWN_ROLE=worker`, qualified leaf keys, concurrency); the exit block (spawn the
reviewer with `AR_SPAWN_ROLE=reviewer`, RAISE `master-handover-approval` with the verdict attached
— the ORCHESTRATOR decides; escalation to the orchestrator, never the developer; the human-pinned
kinds named); the report obligations (master-handover packet, leaf-review notes, decision-log
entries per delegated gate and reopen). Compiler notes bind the orchestrator: fill every
placeholder, state the super-tip anchor, echo-confirmed paste delivery.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-05T16:30+02:00 - Created file-level onboarding for the new manager-brief template (L8
  seam-ruling remediation, cycle 4 — closes AR-12's dispatch-determinism gap). Verification
  metadata pinned until closeout stamps the L8 commit.
