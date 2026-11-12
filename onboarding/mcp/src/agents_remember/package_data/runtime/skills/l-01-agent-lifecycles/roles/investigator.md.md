# mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/investigator.md

## Message/file transport and return addressing

Messages are short wake-ups naming work and files; report/verdict/evidence content travels in file-only `body` or existing-file `attach`, not pasted text. Within a shared task the files stay in its record and a leaf workspace exposes the folder link. Wake text uses the settings limit without a pinned number. The report-written notice goes with `role_message` on `agents-remember-task` to the parent's role and task references; developer questions go to the parent the same way, or to the Investigator's own chat when it has no parent.


## Governing Overview

[Route overview](../../../../../../../overview.md)

## Purpose

The packaged mirror of the canonical scoped Investigator role.

The Investigator reports what is and what is not, with evidence for each. It states no requirement, ruling or duty of its own; a needed change is an open question for the parent, not a fix to apply.

## Code Commentary

The canonical skills/l-01-agent-lifecycles/roles/investigator.md owns the concern, selection and read/report/mutation boundaries. scripts/sync-skills.py regenerates this packaged copy, the sole generated skill target the tool server serves as MCP resources; this file authors no independent role. The scoped concern may be of any kind, checks remain scratch/sandbox-only, code/memory/task mutations remain with their owners, and provider/system remediation remains report-first and explicitly ordered. Projects, sprint and sprint/master starts preserve the actual parent concern channel and no invented task identity.

## Working folders and reports

Agent-authored temporary files, experiments and working copies live only in the handover's real `workspace.scratchRoot`, outside code, memory and task folders; reports and evidence go in the handover's local report folder, which the product copies to canonical notes before removal.

## Evidence


- The source owns the documented investigation, identity or request boundary.

- The Investigator reports what is and what is not, with evidence for each. It states no requirement, ruling or duty of its own; a needed change is an open question for the parent, not a fix to apply.

- The Investigator starts without a task reference, on a sprint, or on a sprint and master, never on a leaf; its concern arrives in its parent's first role_message, or from the developer's request when it has no parent, and a missing concern or scope is asked for, never invented. [1]

- The Investigator reports what is and what is not, with evidence for each. It states no requirement, ruling or duty of its own; a needed change is an open question for the parent, not a fix to apply. [2]
