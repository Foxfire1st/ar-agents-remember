# mcp/src/agents_remember/mcp/registration/gates.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/mcp/registration/gates.py`       |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated | 2026-08-20T09:35+02:00 |
| lastVerifiedCommitHash | `a9d50e08b830c4a34c14e495706c19fe697f47ab` |
| lastVerifiedCommitDate | 2026-08-20T09:26:15+02:00 |
| governingOverview      | `overview.md`                                             |

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

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Gate creation uses ambient structural context. | `lifecycle_gate` | mcp/src/agents_remember/mcp/registration/gates.py:23-49 |
| Decisions select an authorized document and kind, not a gate id. | `gate_decide` | mcp/src/agents_remember/mcp/registration/gates.py:51-74 |
| Listing exposes only caller-scoped structural summaries. | `gate_list` | mcp/src/agents_remember/mcp/registration/gates.py:85-87 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: `lifecycle_gate`/`gate_decide`/`gate_list` accept an
  optional request-carried `caller` (role + task_document_ref) for ambient callers with no plane
  seat; hosted seats win and a contradicting declared caller refuses. Claim re-read and citation
  range regenerated. Verified at code commit a9d50e08.


- 2026-08-11T14:29+02:00 — Re-read the three public gate declarations and widened their
  citations to include the registered-tool decorators; verification metadata remains unchanged
  for governed closeout.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the bare-`*` keyword-only signature remediation (PLR0917). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 4 repository-reference citations (4/4 anchored and sourced; scoped citation check clean).

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The three gate
  declarations moved out of `server.py`; `lifecycle_gate` now packs `GateRaise` + `GateWait` and
  `gate_decide` packs `GateVerdict`, keeping the fixed model/cli vs orchestration attribution in the
  declaration. Verification metadata pinned to the pre-change commit until closeout stamps the L2
  code commit.
