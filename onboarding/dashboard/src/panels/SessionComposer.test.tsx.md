# dashboard/src/panels/SessionComposer.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/SessionComposer.test.tsx`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T11:22+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels overview](overview.md)

## Purpose

Vitest render + interaction tests for `SessionComposer` (slice 6e-3). The composer is pure +
presentational (React Aria, no backend/xterm), so the tests drive it directly.

## Code Commentary

### Logic

Three cases via `fireEvent` on the `<textarea>`: (1) typing + `Send` reports the **trimmed** draft and
clears the field; (2) ⌘/Ctrl+Enter sends; (3) an empty / whitespace-only draft never sends (the Send
button is disabled and the keystroke no-ops). `fireEvent.change` / `fireEvent.keyDown` is the repo idiom
for driving React Aria interaction.

### Invariants And Boundaries

Render + interaction only; no backend, no WebSocket, no xterm. Asserts the reported value + the cleared
field, not the stdin write (that wiring lives in `Chats`).

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test. | — | [SessionComposer.tsx](SessionComposer.tsx) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
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

- 2026-08-01T11:22+02:00 — 260731-EFA-L4 curator: No content impact: the only change is the answer-mode
  seed swapping `{ id, gate } as unknown as LifecycleProjection` for
  `lifecycleWithGate({ id: "lc-answer-mode" }, { …the same gate… })`, and I checked the thing that could
  have made it consequential — whether the extra fields the builder now supplies can reach an assertion.
  `findInteractionGate` (`data/interactionAnswer.ts` L258-L274) is the only consumer of this seed, and it
  reads `lifecycle.gate.kind`, `gate.state`, `gate.packet.adapterInteraction.{sessionId,interactionId}`
  and `lifecycle.id` — nothing else. The gate override is total for all four fields and
  `lifecycleWithGate` applies `over` last, so `id` still wins; `BASE_LIFECYCLE`'s `state`/`phase`/`tokens`
  are inert here. The suite's described cases, assertions and boundaries are unchanged, so the body
  stands.

- 2026-07-24T13:17:17Z — Curator: recorded the live composer behavior and evidence-gating
  regressions; verification fields remain pre-commit.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — FEUI-L5: replaced obsolete textarea/paste tests with the complete
  reliable composer, pop-back, recovery, ordering, IME, and answer-mode matrix.

- 2026-06-19T05:48 — Created for task 6 slice 6e-3: render + interaction tests for the context composer (trimmed send + clear; ⌘/Ctrl+Enter; empty no-op). Verification metadata pinned until closeout stamps the 6e-3 code commit.
