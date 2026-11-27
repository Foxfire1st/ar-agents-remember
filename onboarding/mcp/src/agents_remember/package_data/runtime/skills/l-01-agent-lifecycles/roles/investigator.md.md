# mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/investigator.md

## Message/file transport and return addressing

Message-file payload details are routed via the Reference index (`reference/message-handover.md`). The report-written notice goes via `role_message` (server binding in `core/every-role.md`) to the parent's role and task references; developer questions go to the parent the same way, or to the Investigator's own chat when it has no parent.


## Governing Overview

[Route overview](../../../../../../../overview.md)

## Purpose

The packaged mirror of the canonical scoped Investigator role.

The Investigator reports what is and what is not, with evidence for each. It states no requirement, ruling or duty of its own; a needed change is an open question for the parent, not a fix to apply.

## Code Commentary

Before inspecting code, the Investigator calls `read_ar_files` (opening relevant saved briefs when present) and `knowledge_read`.

The canonical skills/l-01-agent-lifecycles/roles/investigator.md owns the concern, selection and read/report/mutation boundaries. scripts/sync-skills.py regenerates this packaged copy, the sole generated skill target the tool server serves as MCP resources; this file authors no independent role. The scoped concern may be of any kind, checks remain scratch/sandbox-only, code/memory/task mutations remain with their owners, and provider/system remediation remains report-first and explicitly ordered. Projects, sprint and sprint/master starts preserve the actual parent concern channel and no invented task identity.

## Working folders and reports

Agent-authored temporary files, experiments and working copies live only in the handover's real `workspace.scratchRoot`, outside code, memory and task folders; reports and evidence go in the handover's local report folder, which the product copies to canonical notes before removal.

## Evidence


- The source owns the documented investigation, identity or request boundary.

- The Investigator reports what is and what is not, with evidence for each. It states no requirement, ruling or duty of its own; a needed change is an open question for the parent, not a fix to apply.

- The Investigator starts taskless in Projects, on a sprint, on a standalone master, or on both, never on a leaf; its concern arrives in its parent's first `role_message` (or from the developer in own chat when parentless), and missing concern, IDs or repos are asked for, never invented. [1]




- The Investigator reports what is and what is not, with evidence for each. It states no requirement, ruling or duty of its own; a needed change is an open question for the parent, not a fix to apply. [2]




- The role directs opening available saved briefs before its source work. Compact rows can give applicable card status and a brief pointer with saved freshness. Fuller replies can include rule text. `knowledge_read` retrieves text-bearing views (`impact`, `search`, `records`, and `dependent`) paired with the code tree. [3]
