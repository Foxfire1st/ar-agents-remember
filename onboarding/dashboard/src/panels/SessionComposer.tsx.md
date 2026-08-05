# dashboard/src/panels/SessionComposer.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/SessionComposer.tsx`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`       |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
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

The component owns a CodeMirror editor backed by the per-session draft/revision store. `submit()`
ignores composition and empty drafts, routes pending interaction answers through
`submitInteractionAnswer`, and routes ordinary drafts through `submitSessionDraft`; blocked outcomes
become the component's status notice. The editor also owns the Enter/Ctrl+Enter, slash-command, escape,
and withdrawal interactions described by the session cockpit.

### Conventions

React Aria primitives (coding-guidelines: don't hand-roll interactive widgets); Panda `css()` keyed on
`_focusVisible` / `_disabled`. The Send button reuses ＋ Terminal's golden look; the textarea
`color: inherit`s the cockpit fg (form controls don't inherit colour by default).

### Invariants And Boundaries

Controlled editor and client seam: the component does not own a raw terminal or PTY paste path, and it
is unit-tested directly (`SessionComposer.test.tsx`). `SessionsView` mounts it only for a focused live
non-terminal seat; ordinary drafts use the reliable submission client, while the vendor TUI owns raw
terminal input.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `SessionsView` names the focused-live seat condition used by the composer boundary. | `focusedLive` | dashboard/src/panels/session-cockpit/SessionsView.tsx:324-325 |
| Ordinary composer drafts call `submitSessionDraft`. | "void submitSessionDraft" | dashboard/src/panels/SessionComposer.tsx:305-305 |
| Pending interaction answers call `submitInteractionAnswer`. | "submitInteractionAnswer(" | dashboard/src/panels/SessionComposer.tsx:297-297 |
| The test suite declares the `SessionComposer` render/interaction block. | "describe(\"SessionComposer" | dashboard/src/panels/SessionComposer.test.tsx:57-57 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
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

## 260718-CHATS-L5P Delta (well identity + focus + capability-derived hints)

- **FB7.1 — the composer joins the terminal well** (`editorFrame`): `background: bg → well` (the
  `#070b0f` token), matching the conversation feed + the pty pane inset. Pty-pane parity (composer bg ===
  `--well`) is the numeric FB7.1 acceptance test.
- **V4 — visible focus on the page's primary input** (`editorFrame`): the inner CodeMirror
  `.cm-focused` outline is clipped by the frame's `overflow:hidden`, so the FRAME now carries the house
  amber ring via `&:focus-within { borderColor: amber }` — keyboard focus is no longer discoverable only
  by the caret.
- **V9 — capability-derived hints** (`footerHint`): on a legacy-raw TERMINAL seat (`session.kind ===
  "terminal"`) native submission is unsupported (typing bypasses the /submit queue), so the hint is
  `<profile> keys · raw terminal keys pass through` and the `reliable submit · text only` tail is NOT
  rendered — the prior static `markdown · … · reliable submit · text only` set contradicted the pane.
  Controlled chats keep the full markdown/reliable-submit set. This supersedes the always-static hint the
  F7 delta below described.
- **V14 — draft chip is an exception cue**: `draft saved` shows only when a non-empty draft actually
  exists (`draft.draft.length > 0`), not permanently on an empty composer.
- **V3 — send never hides under the inspector** (`sendButton`): `flexShrink:0` + `whiteSpace:nowrap` so
  `ctrl+↵ send` keeps its full width + single line; the hint (`footerLeft`, `flex:1 minWidth:0`) is the
  only part that yields when the inspector opens and the stage column reflows.

## 260718-CHATS-L4 Reviewed Candidate Delta (composer hint restructure, F7)

Presentation-only blank-fill (no authority change): the composer hint line was restructured to close
developer visual-finding A3 (finding F7). It now groups by concern with ONE interpunct separator
(`markdown · emacs keys · draft saved · reliable submit · text only`) and moves the honest-boundary
transport wall (`receipts + reconcile; terminal lines join the same queue without receipts …`) into a
`reliable submit` tooltip (progressive disclosure) instead of a mixed-separator wall. The reliable
submit / receipt / reconcile / withdrawal authorities are unchanged. The reviewed L4 candidate is
uncommitted; verification stays pinned to the FEUI-L8 base until closeout.

## Current L5I Maintenance

The live composer now sends on plain Enter while Shift+Enter explicitly inserts an indented newline.
It renders queue preview/counts only after server-confirmed pre-dispatch queue evidence, describes a
boot-time send deferral as `connecting… · composer draft unchanged`, and keeps static capabilities
in a tooltip rather than standing footer chrome. The exact-turn stop action belongs beside Send for
working controlled seats; raw terminal seats mount no dashboard composer.

## Update History

- 2026-08-04T11:35:04+02:00 — 260731-EFA-L6 S18-B10 curator: source-first semantic citation curation; repaired this card's scoped citation findings with frozen-source evidence and corrected stale or pooled claims where needed.

- 2026-07-24T13:17:17Z — Curator: corrected composer input, queue-honesty, declutter, boot-deferral,
  and stop-control ownership semantics; verification fields remain pre-commit.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the composer polish — `editorFrame`
  `background: well` (FB7.1) + `:focus-within` amber ring (V4); capability-derived footer hint (V9 —
  terminal seats show `raw terminal keys pass through`, not the markdown/reliable-submit claims); `draft
  saved` only with a non-empty draft (V14); `sendButton` `flexShrink:0`+`nowrap` so it never hides under
  the inspector (V3). Reliable-submit/receipt/withdrawal authorities unchanged. Verification pinned to
  the leaf base (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 (structured Chats renderer, reviewer FINAL PASS): recorded
  the presentation-only composer-hint restructure (F7/A3) — grouped by concern with one interpunct
  separator, the honest-boundary wall moved into a `reliable submit` tooltip; no submit/authority
  change. Verification metadata remains pinned to the leaf base until closeout.
- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — FEUI-L5: rewrote the sidecar from the obsolete textarea/paste model to
  the shared CodeMirror reliable-submit, queue, pop-back, recovery, and answer-mode contract.

- 2026-06-19T05:48 — Created for task 6 slice 6e-3: the context composer (React Aria `TextField`/`TextArea` + `Button`) that reports a draft for `Chats` to inject into the active session's stdin as a bracketed paste (no auto-submit). Verification metadata pinned until closeout stamps the 6e-3 code commit.
