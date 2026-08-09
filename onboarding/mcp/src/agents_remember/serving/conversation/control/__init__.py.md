# mcp/src/agents_remember/serving/conversation/control/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-04T03:03+02:00 |
| lastVerifiedCommitHash |  `7af76249ff1aa728d34a6e81c5f09c8bcb797484`|
| lastVerifiedCommitDate |  2026-08-09T02:17:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

Marks the package that owns the implemented structured exact-session control surface (interrupt,
source-aware queue/withdrawal recovery, typed attachments, read-only policy, and evidence-bound
telemetry) landed by 260718-CHATS-L3.

## Code Commentary

### Logic

Contains only the package docstring; the sibling `api.py` owns the seventeen registered control
routes and each capability lives in its own focused module.

### Conventions

Keep the marker behavior-free; no control work executes at import time. The landed submission
authority remains the mutation owner — the control modules compose it, never a second queue.

### Invariants And Boundaries

- The package marker must not execute control work at import time.
- This package is not a third conversation read port or a second operation queue.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The sibling API module owns the registered control routes; the package overview governs the slice.

| Finding | Anchor | Source |
| --- | --- | --- |
| The sibling `api.py` owns the control surface's `APIRouter` instance. | "router = APIRouter" | mcp/src/agents_remember/serving/conversation/control/api.py:77-77 |
| That router uses the `/api/terminal/{ar_session_id}` prefix and registers exactly seventeen decorated routes, from `conversation_interrupt` through `conversation_telemetry`. | `router`; `conversation_interrupt`; `conversation_interrupt_status`; `conversation_interrupt_reconcile`; `conversation_operation_queue`; `conversation_withdraw`; `conversation_withdraw_status`; `conversation_withdraw_reconcile`; `conversation_pending_recoveries`; `conversation_fetch_recovery`; `conversation_ack_recovery`; `conversation_stage_attachments`; `conversation_rebind_attachment`; `conversation_attachment_status`; `conversation_attachment_reconcile`; `conversation_submit`; `conversation_policy`; `conversation_telemetry` | mcp/src/agents_remember/serving/conversation/control/api.py:75-78; mcp/src/agents_remember/serving/conversation/control/api.py:151-181; mcp/src/agents_remember/serving/conversation/control/api.py:184-215; mcp/src/agents_remember/serving/conversation/control/api.py:218-249; mcp/src/agents_remember/serving/conversation/control/api.py:252-275; mcp/src/agents_remember/serving/conversation/control/api.py:280-311; mcp/src/agents_remember/serving/conversation/control/api.py:314-343; mcp/src/agents_remember/serving/conversation/control/api.py:346-375; mcp/src/agents_remember/serving/conversation/control/api.py:378-403; mcp/src/agents_remember/serving/conversation/control/api.py:406-433; mcp/src/agents_remember/serving/conversation/control/api.py:436-464; mcp/src/agents_remember/serving/conversation/control/api.py:482-528; mcp/src/agents_remember/serving/conversation/control/api.py:531-564; mcp/src/agents_remember/serving/conversation/control/api.py:567-595; mcp/src/agents_remember/serving/conversation/control/api.py:598-626; mcp/src/agents_remember/serving/conversation/control/api.py:635-682; mcp/src/agents_remember/serving/conversation/control/api.py:685-708; mcp/src/agents_remember/serving/conversation/control/api.py:711-734 |
| The governing route-local overview for the implemented control slice. | `# Structured Conversation Control Route Overview` | onboarding/mcp/src/agents_remember/serving/conversation/control/overview.md:1-433 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-04T03:26:26+02:00 — 260731-EFA-L6 S18-SR3-B06 curator: generated and source-inspected the router plus seventeen route-owner ranges (1 repair, 0 normalisations, 0 declines); the locked immediate recheck was clean with frozen zero source/tokenize/parse/build telemetry.
- 2026-08-04T03:03:23+02:00 — 260731-EFA-L6 S18-SR3-B06 worker: replaced the
  underbound prefix/first/last record with the router plus all seventeen decorated route-owner
  symbols, so the exact count is itself bound. The changed binding is a provisional `:1-1` input
  for the fresh Luna curator; no citation mechanics ran.
- 2026-08-04T02:20:03+02:00 — 260731-EFA-L6 S18-B06 curator delta: repaired the scoped citations against the frozen source snapshot; generated ranges were inspected and the managed index remained warm/frozen with zero source reads, tokenization, parsing, and build.

- 2026-08-04T01:24:49+02:00 — 260731-EFA-L6 S18-SR2-B06 worker: retained the generated
  `APIRouter`-definition range and source-first split the prefix plus exact seventeen-decorator
  inventory into an honest `:1-1` binding spanning the first and last route owners. No citation
  mechanics ran.
- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired the exact control-router citation and normalized its governing overview path; final exact frozen-snapshot check is clean.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 broken citations. `control/api.py` grew
  to 686 lines and its seventeen `@router` decorations now run from the `APIRouter(prefix=
  "/api/terminal/{ar_session_id}")` at L58 to the end of `conversation_telemetry` at L631 (was
  `L57-L570`); counted the decorators and read both ends back. The overview row pointed at
  `agents-remember/mcp/.../control/overview.md`, which does not exist in the source tree —
  `overview.md` is a memory-repo onboarding doc, not a code file. Repointed it to the sibling
  `[overview.md](overview.md)` this card already names as its `governingOverview`, and replaced the
  invented `L1-L40` with the house-style non-numeric `route overview` citation, since that doc lives
  in this repo and is not line-stable.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: updated the package-marker description from the
  reserved shell to the implemented control surface and repointed the governing overview to the new
  `control/overview.md` pillar. Verification stays pinned at the L3E base until L3 closeout stamps the
  candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the package-marker sidecar.
  Verification is blank until closeout commits and stamps the new source.
