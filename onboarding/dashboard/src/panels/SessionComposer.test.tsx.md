# dashboard/src/panels/SessionComposer.test.tsx

## Governing Overview

[panels overview](overview.md)

## Purpose

Vitest render + interaction tests for `SessionComposer` (slice 6e-3). The suite covers the
CodeMirror-backed draft/editor surface, reliable submission and queue/withdrawal behavior, race and
IME handling, answer mode, and the raw-terminal gate.

## Code Commentary

### Logic

The suite drives the editor and session cockpit stores directly. It covers reliable draft submission,
queue and withdrawal state, response/poll ordering, delivered-vs-withdraw races, IME composition,
slash commands, answer-mode interaction submission, and the raw-session gate. The answer-mode case
is explicitly lifecycle-free: it proves one submission-authority read followed by one exact-session
`interaction-response` POST carrying the interaction id, bridge epoch, and response, while duplicate
clicks remain locked. The tests assert current draft/revision and server-confirmed outcomes rather
than a direct PTY write.

### Invariants And Boundaries

Render and interaction coverage includes the session draft/client seam but does not open a backend,
WebSocket, or xterm in this unit suite. Controlled prompt delivery uses the reliable draft path;
raw-terminal delivery remains owned by the vendor TUI rather than this composer.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The component under test. [1]
- Lifecycle-free answer mode uses the exact session response route and locks duplicate sends. [2]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## 260715-FEUI-L5 Reliable Submit Delta

The suite now covers exact submit/revision behavior, draft persistence, slash commands, authoritative
withdrawal, recovery and dismissal, not-found/generation loss, response/poll partial-order races,
queue provenance, delivered-vs-withdraw races, IME behavior, answer mode, and the raw-session gate.
It asserts zero PTY paste for controlled prompt delivery.

## FEUI-L8 Reviewed Candidate Delta

Adds same-tab effective-keymap/profile reconfiguration coverage and proves a live Emacs/Vim or chord change preserves the exact CodeMirror node, draft text, and draft revision.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Current L5I Maintenance

The composer suite now pins Enter-send versus Shift+Enter newline precedence, server-confirmed queue
honesty, deferred-send copy, decluttered exception cues, and the evidence-gated stop control beside
Send.
