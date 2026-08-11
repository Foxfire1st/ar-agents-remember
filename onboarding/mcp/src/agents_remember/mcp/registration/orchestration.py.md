# mcp/src/agents_remember/mcp/registration/orchestration.py

| Field                  | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| repository             | agents-remember                                                   |
| path                   | `mcp/src/agents_remember/mcp/registration/orchestration.py`       |
| doc_type               | `file-level-onboarding`                                           |
| lastUpdated | 2026-08-11T14:29+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                        |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                                     |

## Governing Overview

[registration route overview](overview.md)

## Purpose

Registers agent-facing parent and child whole-message tools over structural seat relationships.

## Code Commentary

### Logic

`message_parent` derives the target entirely from the ambient caller. `message_child` accepts only
a canonical child task document, role, and message content. Both delegate persistence, authorization,
current-occupant resolution, and delivery to the structural application boundary.

### Conventions

Runtime, lifecycle, inbox-row, gate, and adapter ids are absent from requests and responses.

### Invariants And Boundaries

- Ordinary traffic is re-resolved after replacement.
- Dispatch briefs and state signals are plane-owned, not model-posted through these tools.
- A child target must be an authorized direct structural relation.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Parent messaging has no caller-supplied target identity. | `message_parent` | mcp/src/agents_remember/mcp/registration/orchestration.py:21-42 |
| Child messaging accepts only structural target and content. | `message_child` | mcp/src/agents_remember/mcp/registration/orchestration.py:44-68 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T14:29+02:00 — Re-read `message_parent` and `message_child` and widened both
  citations to include their registered-tool decorators; verification metadata remains unchanged
  for governed closeout.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the bare-`*` keyword-only signature remediation (PLR0917). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 4 citation rows with
  builder, model-record and wiring-test anchors (operator_inbox.py, orchestration.py,
  operator_inbox_records.py, test_mcp_registration_wiring.py). Zero findings remain.

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The four messaging
  declarations moved out of `server.py`; post now packs `InboxAddress`/`InboxMessage`/`InboxPoster`/
  `HostedDelivery` and the nudge packs `NudgeTarget`/`NudgeSubject`, with model/cli attribution still
  fixed in the declaration. Verification metadata pinned to the pre-change commit until closeout
  stamps the L2 code commit.
