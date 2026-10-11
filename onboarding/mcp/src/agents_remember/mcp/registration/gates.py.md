# mcp/src/agents_remember/mcp/registration/gates.py

## Current operative account — MIK-R112

The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.

- HEAD diff deletes the entire named source file.

### Superseded inventory

- Pre-repair card claim: Card presents lifecycle_gate/gate_decide/gate_list registration as current. This is superseded archival wording, not a current prescription.

### Source and authority bounds

- Source comparison: `mcp/src/agents_remember/mcp/registration/gates.py (absent; git diff HEAD -- this path: deleted file mode 100644)`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

## Governing Overview

[registration route overview](overview.md)

## Purpose

Registers public lifecycle-gate creation, decision, and listing without exposing lifecycle or gate
identifiers to agents.

## Code Commentary

### Logic

Gate creation derives the caller's canonical task document from ambient state — a hosted seat, or a
request-carried declared caller when the process has no plane seat (L16-R3). Decision accepts an
authorized child document, kind, and decision; the application finds exactly one open gate. Listing
is scoped to the caller's structural document.

### Conventions

Public gate results contain task document, role, kind, and state. Internal correlation models remain
behind the application seam.

### Invariants And Boundaries

- Gate/lifecycle ids are never agent inputs or outputs.
- Zero or multiple matches fail closed.
- Ambient caller role supplies attribution and policy authority; an ambient caller with no plane
  seat declares `caller` (role + task_document_ref) instead, and the same authorization validates
  it exactly like a seat.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Gate creation uses ambient structural context. [1]
- Decisions select an authorized document and kind, not a gate id. [2]
- Listing exposes only caller-scoped structural summaries. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.

</details>
