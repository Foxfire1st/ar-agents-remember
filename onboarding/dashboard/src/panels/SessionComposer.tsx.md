# dashboard/src/panels/SessionComposer.tsx

## Governing Overview

[panels overview](overview.md)

## 260731-EFA-L8 Change

The composer was split by responsibility: hooks moved to
`panels/sessionComposerHooks.ts`, render parts to `panels/sessionComposerParts.tsx`,
and styles to `panels/sessionComposerStyles.ts`. The editor-creation effect now
reads initial values through refs so `exhaustive-deps` passes without recreating the
editor per keystroke; behavior is unchanged.

## Purpose

The shared FEUI-L5 reliable composer for Chats and the sessions cockpit (the removed contextual `RailChat` also used it before MIK-R95). It is a
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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- `SessionsView` names the focused-live seat condition used by the composer boundary. [1]
- Ordinary composer drafts call `submitSessionDraft`. [2]
- Pending interaction answers call `submitInteractionAnswer`. [3]
- The test suite declares the `SessionComposer` render/interaction block. [4]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

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
