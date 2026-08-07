# dashboard/src/panels/SessionComposer.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/SessionComposer.test.tsx`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T11:22+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                   |

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
slash commands, answer-mode interaction submission, and the raw-session gate. The tests assert the
current draft/revision and server-confirmed outcomes rather than a direct PTY write.

### Invariants And Boundaries

Render and interaction coverage includes the session draft/client seam but does not open a backend,
WebSocket, or xterm in this unit suite. Controlled prompt delivery uses the reliable draft path;
raw-terminal delivery remains owned by the vendor TUI rather than this composer.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component under test. | "export const SessionComposer" | dashboard/src/panels/SessionComposer.tsx:57-57 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

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

## Update History

- 2026-08-04T15:56:39+02:00 — 260731-EFA-L6 S18-B10 curator: closed same-reviewer residual D12 by narrowing the answer-mode history assertion to the actual `lifecycleWithGate(...)` call use; rechecked this card through the locked exact-document fixer/check.

- 2026-08-01T11:22+02:00 — 260731-EFA-L4 curator: No content impact: the answer-mode lifecycle map
  entry calls `lifecycleWithGate`, cit:(["lifecycleWithGate("], dashboard/src/panels/SessionComposer.test.tsx:712-712).
  Gate resolution is implemented by `findInteractionGate`,
  cit:(["function findInteractionGate"], dashboard/src/data/interactionAnswer.ts:268-268), and the fixture
  builder is `lifecycleWithGate`, cit:(["lifecycleWithGate"], dashboard/src/test/fixtures/wire.ts:256-256).
  These use/declaration facts avoid asserting behavior or argument equivalence that those cited lines
  do not establish.

- 2026-07-24T13:17:17Z — Curator: recorded the live composer behavior and evidence-gating
  regressions; verification fields remain pre-commit.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — FEUI-L5: replaced obsolete textarea/paste tests with the complete
  reliable composer, pop-back, recovery, ordering, IME, and answer-mode matrix.

- 2026-06-19T05:48 — Created for task 6 slice 6e-3: render + interaction tests for the context composer (trimmed send + clear; ⌘/Ctrl+Enter; empty no-op). Verification metadata pinned until closeout stamps the 6e-3 code commit.
