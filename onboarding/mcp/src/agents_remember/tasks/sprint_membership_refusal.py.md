# mcp/src/agents_remember/tasks/sprint_membership_refusal.py

## Governing Overview

[tasks overview](overview.md)

## Purpose

The shared diagnostic for a commanded alias that fails exact master resolution. Reader admission determines
whether that resolution is reached; readers reaching it use the same diagnostic.

## Code Commentary

### Logic

`missing_master_detail(coordination_root, sprint_ref, entry)` looks for the missing master under
`tasks/<repository>/0_archive/`: first a folder named like the entry, then any archived `task.json` whose folder name,
id or title equals the entry (an unreadable archived document is skipped). It returns one text that names the sprint
and the commanded master, says either where the master was found under `0_archive` or that its live task folder is
missing, and names the action: restore the master's folder to its canonical live location, then use
`task_doc.retire_master` on the sprint with `masterRef`, `reason` and the affirmed `removeEdges` to remove its
membership and graph before archival.

### Conventions

- The function reads the filesystem only and never raises for an unreadable archived document.

### Invariants And Boundaries

- Exact commanded-master resolution uses this message. Linkage validation without typed rows returns earlier;
  execution-topology validation can refuse a missing graph before resolving active commanded membership.

## Evidence

- The message names the sprint, the master, where it was found under the archive, and the retire operation with its fields. [1]
- The three topology readers raise the identical message for an archived master. [2]
