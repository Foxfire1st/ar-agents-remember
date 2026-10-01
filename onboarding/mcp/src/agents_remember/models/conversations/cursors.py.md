# mcp/src/agents_remember/models/conversations/cursors.py

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

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
