# mcp/src/agents_remember/models/conversations/cursors.py

| Field                  | Value                                                         |
| ---------------------- | ------------------------------------------------------------- |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/models/conversations/cursors.py`      |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-08-08T14:38+02:00                                        |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                    |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                                 |

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/cursors.py` (260731-EFA-L9) owns the non-interchangeable cursor, key, and
resume-target families of the conversation wire grammar.

## Code Commentary

### Logic

`ActivePageCursor`/`ActiveEventCursor` (cit:(["class ActivePageCursor"], mcp/src/agents_remember/models/conversations/cursors.py:20-20)) are the active-stream
cursors; `LibraryListCursor`/`LibraryReadCursor`/`LibraryConversationKey` and `NativeResumeTarget`
(cit:(["class NativeResumeTarget"], mcp/src/agents_remember/models/conversations/cursors.py:40-40)) the dormant-history families;
`ActiveCursorBinding`/`LibraryCursorBinding`/`LibraryKeyBinding`/`ActiveEventResume`
(cit:(["class ActiveEventResume"], mcp/src/agents_remember/models/conversations/cursors.py:68-68)) bind purpose/authorization/identity/scope to each
family.

### Invariants And Boundaries

- Active and library cursor families are non-interchangeable and must remain bound to purpose,
  authorization, identity/scope, and generation.

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the cursors layer moved from
  `serving/conversation/_models_wire.py`. Verification metadata pinned until closeout stamps the
  L9 code commit.
