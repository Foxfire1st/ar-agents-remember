# dashboard/src/panels/SessionComposer.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/SessionComposer.tsx`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-20T22:30+02:00                           |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd`       |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels overview](overview.md)

## Purpose

The shared FEUI-L5 reliable composer for Chats, RailChat, and the sessions cockpit. It is a
CodeMirror 6 Markdown editor backed by the per-session draft/revision store, not a PTY paste box.
Ctrl+Enter submits one epoch-bound whole message through `submitClient`; Enter remains a newline,
IME composition is respected, slash commands open the command palette, and Alt+Up performs the
authoritative server-side withdrawal/pop-back flow. The same editor can enter the gate-only answer
mode used by `InteractionBar` without turning a terminal line into an interaction answer.

## Code Commentary

### Logic

A React Aria `TextField` (`value`/`onChange`) wrapping a `TextArea` + a `Button`. `submit()` trims the
draft, no-ops when empty, calls `onSend(value)`, and clears. Send fires on the `Button` `onPress` **or**
⌘/Ctrl+Enter (a `TextArea` `onKeyDown`; plain Enter stays a newline). The `Button` is `isDisabled` while
the trimmed draft is empty.

### Conventions

React Aria primitives (coding-guidelines: don't hand-roll interactive widgets); Panda `css()` keyed on
`_focusVisible` / `_disabled`. The Send button reuses ＋ Terminal's golden look; the textarea
`color: inherit`s the cockpit fg (form controls don't inherit colour by default).

### Invariants And Boundaries

Presentational + controlled: no backend, no WebSocket, no xterm — so it is unit-tested directly
(`SessionComposer.test.tsx`). It only *reports* the draft; `Chats` owns the bracketed-paste wrap, the
write to the active session's stdin, and the **no-auto-submit** decision (injected text lands as a
paste; the operator submits in the terminal).

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The canonical Chats view mounts this over the reliable-submit client for the focused live seat. | — | [SessionsView.tsx](session-cockpit/SessionsView.tsx) |
| The connection whose `sendInput` receives the bracketed-paste injection (+ the `bracketedPaste` helper). | — | [data/terminal.ts](../data/terminal.ts) |
| The render + interaction tests for this composer. | — | [SessionComposer.test.tsx](SessionComposer.test.tsx) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

The component now owns CodeMirror synchronization against the session draft revision, Ctrl+Enter
whole-message submit, IME-safe newline behavior, slash palette handoff, and authoritative Alt+Up.
It renders `QueuePreview`, five-value receipt/reconcile progress, bounded retry/endgame choices, and
the exact withdrawal recovery slot. In answer mode it delegates only to the gate-backed answer
callback. No path writes prompt text into the PTY.

## FEUI-L8 Reviewed Candidate Delta

CodeMirror now consumes the effective keymap through compartments and reconfigures profile/bindings without recreating the editor. House commands retain highest precedence; Vim owns Escape while immutable F6 exits, and the send hint reflects the active binding.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## 260718-CHATS-L4 Reviewed Candidate Delta (composer hint restructure, F7)

Presentation-only blank-fill (no authority change): the composer hint line was restructured to close
developer visual-finding A3 (finding F7). It now groups by concern with ONE interpunct separator
(`markdown · emacs keys · draft saved · reliable submit · text only`) and moves the honest-boundary
transport wall (`receipts + reconcile; terminal lines join the same queue without receipts …`) into a
`reliable submit` tooltip (progressive disclosure) instead of a mixed-separator wall. The reliable
submit / receipt / reconcile / withdrawal authorities are unchanged. The reviewed L4 candidate is
uncommitted; verification stays pinned to the FEUI-L8 base until closeout.

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 (structured Chats renderer, reviewer FINAL PASS): recorded
  the presentation-only composer-hint restructure (F7/A3) — grouped by concern with one interpunct
  separator, the honest-boundary wall moved into a `reliable submit` tooltip; no submit/authority
  change. Verification metadata remains pinned to the leaf base until closeout.
- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — FEUI-L5: rewrote the sidecar from the obsolete textarea/paste model to
  the shared CodeMirror reliable-submit, queue, pop-back, recovery, and answer-mode contract.

- 2026-06-19T05:48 — Created for task 6 slice 6e-3: the context composer (React Aria `TextField`/`TextArea` + `Button`) that reports a draft for `Chats` to inject into the active session's stdin as a bracketed paste (no auto-submit). Verification metadata pinned until closeout stamps the 6e-3 code commit.
