# mcp/src/agents_remember/tasks/master_order.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Derive an ordinary master’s state-aware Order from its explicitly indexed task rows and their waitsFor fields; never persist derived waves or authorize execution.

## Code Commentary

Child loading opens only row.file paths and accepts prepared overrides before disk reads. Missing/invalid/non-subTask children are skipped. A view is absent for non-master/sprint input or when no matching listed child carries nonempty waitsFor. Row status is authoritative; a matching child contributes its title and dependencies. Unknown dependency IDs remain synthetic gone/fileless facts.

The iterative ordered SCC calculation identifies legacy cycles, including self-cycles, from the full stored dependency population before excluding Completed tasks from the scheduling graph. Unfinished members retain those full-population component identities. A component containing inProgress, gone or abandoned state anchors at wave zero; other unfinished components follow prerequisite waves with a minimum of one. Every member of a stored cycle, including Completed members, receives the unfinished component’s wave, or -1 when the entire cycle is Completed, and keeps its cycle flag. Other Completed tasks remain outside the unfinished wave graph. Only planning, noncycle tasks whose prerequisites are Completed enter ready_ids; derive_master_order indexes cycle IDs as a set for repeated membership checks. The predecessor’s unfinished-only SCC/cycle scope is historical, not the RF01 rule. This ordinary-master calculation is not the sprint frontier’s terminal-resolution policy and is not a start gate.

## Evidence

- Explicit child loading and authoritative row status determine the read-only population; full stored SCC identity survives Completed filtering, while unfinished scheduling derives waves and cyclic members never become ready. [1]
