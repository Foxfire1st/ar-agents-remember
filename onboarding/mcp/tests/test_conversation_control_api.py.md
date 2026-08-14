# mcp/tests/test_conversation_control_api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_control_api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Production-route tests for the conversation control API (R7). Every test drives the real composition
on one loop — bridge + IPC server on a real user-private socket, a real catalog row, the L0
`register_conversation_routes` composition, and HTTP over a real uvicorn wire — with the structural
fake adapter as the only double at the harness edge.

## Code Commentary

### Logic

cit:([`ControlApiTests`], mcp/tests/test_conversation_control_api.py:26-378) exercises the seventeen registered routes over the real wire: the O4
typed-error mapping per route family, remote-peer 403, epoch guards, multipart attachment staging,
read-only policy 405s on PATCH/PUT/DELETE, the queue-truth privacy + withdrawal flow end-to-end, and
cit:([`test_no_paste_pty_or_native_queue_substitution_in_control_modules`], mcp/tests/test_conversation_control_api.py:355-378), the source scan proving
no PTY Esc / paste / native-queue substitution anywhere in the control modules. The terminal-wire
arm submits through `submit_control_prompt(entry, body, ControlSubmission(source="terminal",
request_id=…))` — one parameter object, not loose keywords.

### Conventions

This is the only L3 suite that crosses a real HTTP wire; the routes resolve their service through the
unmodified `conversation_control_service` path (the harness seeds the `NOW`-anchored instance into the
memo, so the wire is time-consistent without touching this file). The source scan is a
topology/absence assertion, intentional for a leaf that establishes what does NOT exist.

### Invariants And Boundaries

- Every routine refusal lands on its precise HTTP status over the real wire — no raw 500.
- Non-loopback peers fail 403; every wire verifies the expected bridge epoch.
- Policy/telemetry/queue/pending are GET-only; policy mutation verbs return 405.
- No paste/PTY/native-queue substitution exists in the control modules (source-scanned).

### Todos

None.

## Docs References

No Domain Documentation source is configured; the route contract is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The suite drives the registered routes and their O4 mapping over the real wire and shared topology.

| Finding | Anchor | Source |
| --- | --- | --- |
| The seventeen registered routes and the O4 typed-error mapping under test. | `conversation_telemetry` | mcp/src/agents_remember/serving/conversation/control/api.py:736-759 |
| The shared fake-topology harness (real bridge/IPC/authority/L0 composition). | `ControlHarness` | mcp/tests/_control_plane.py:436-518 |
| The foundation pin that independently asserts the exact seventeen routes. | `control_paths` | mcp/tests/test_conversation_foundation.py:65-69 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 6 citation finding(s); scoped recheck clean.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the `control/api.py` citation. The file
  is now 686 lines and the stamped `L57-L570` both started before the routes (in the import block)
  and stopped four routes short. Counted the `@router` decorators: exactly seventeen, at L131, 160,
  190, 220, 242, 272, 300, 328, 352, 378, 420, 465, 497, 524, 551, 590 and 612 — so the claim's
  count still holds — spanning L131 through the end of `conversation_telemetry` at L631. The O4
  typed-error mapping is `_map_typed_error` at L107-L124 (epoch mismatch 409, authorization 403,
  composition 503, ref/operation/session self-describing status, control 503, re-raise otherwise).
  Split into those two ranges; claim unchanged.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2: corrected the in-file anchor for
  `test_no_paste_pty_or_native_queue_substitution_in_control_modules`, which the leaf moved from
  L354 to L355 — the terminal-wire submission dropped one line by folding `source`/`request_id`
  into `ControlSubmission`, and a `ruff format` reflow of the usage assertion added two. Named the
  new submission object in the Logic paragraph. `ControlApiTests` still opens at L26, and the
  seventeen routes, the O4 typed-error mapping, the remote-peer 403, the epoch guards, the policy
  405s and the source scan are all untouched.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the production-route
  suite — the seventeen routes over a real uvicorn wire, O4 mapping, remote-peer 403, epoch guards,
  multipart staging, policy 405s, the queue-truth privacy/withdrawal flow, and the no-paste/no-
  substitution source scan. Verification is blank because the new source file is uncommitted;
  closeout owns its first source stamp.
