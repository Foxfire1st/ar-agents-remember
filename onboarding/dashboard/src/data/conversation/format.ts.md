# dashboard/src/data/conversation/format.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation/format.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T05:30+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

The shared presentation-convention module for every structured Chats surface. It encodes the
developer visual-findings rules (`260720-developer-dashboard-visual-findings.md` §A) once, as a small
tested vocabulary, so every component reads as one product — no per-component reinvention of empty
states, durations, or truncation. It is pure and side-effect-free; the reducer/store never call it
(they hold structure, not display), and only the view layer (AmbientTelemetry, the library rows,
timeline chips) consumes it.

## Code Commentary

### Logic

- **`ABSENT = "—"`** — the em-dash for a genuinely absent value (A1). Callers must never chain
  these; empty states explain or collapse instead.
- **`SEP = " · "`** — the one separator convention: a spaced interpunct between chips on one
  line (A1/A8).
- **`joinChips(parts)`** — filters out `null`/`undefined`/empty strings and joins the
  survivors with `SEP`; all-empty input collapses to `""` (no dash-chain, no reassurance-zero cluster
  — A2). cit:([`joinChips`], dashboard/src/data/conversation/format.ts:17-19)
- **`humanizeDuration(ms)`** — the two most significant units with fixed precision
  (`800 ms`, `45 s`, `3 m 12 s`, `2 h 5 m`, `6 d 0 h`). Never raw minutes or six-decimal seconds
  (the exact developer eyesores `8638.1m` / `518288.173569s`). Negative/non-finite → `ABSENT`.
  The live `ServingBuildStamp` and `AgentNotifierHeartbeatBadge` use it for uptime and heartbeat age;
  the former rail bus footer is removed. cit:([`humanizeDuration`], dashboard/src/data/conversation/format.ts:25-37)
- **`shortId(id, tail = 6)`** (NEW — R6/B10, 260718-CHATS-L5P) — a long ULID/UUID (`> 12` chars)
  collapses to its distinguishing suffix (`…ZKCZEP`) so the rail/chrome never leaks a 26-char raw id;
  short ids pass through unchanged. Display-only — the caller MUST attach the full value as a
  `title`/tooltip (so it stays reachable + copyable), exactly like `truncateMiddle`. Consumers:
  `ChatContextBar` task badges, the `SessionsView` focus-handoff banner fallback.
- **`humanizeAge(iso, now)`** — an ISO timestamp rendered as `<humanized> ago`; absent /
  unparseable input → `ABSENT`; a future timestamp → `just now`. cit:([`humanizeAge`], dashboard/src/data/conversation/format.ts:40-47)
- **`freshnessTone(state, ageMs)`** — maps a freshness state to a QUIET-distinct tone:
  `fresh`, `aging` (a brief <60 s lag), `stale` (long-stale, calm — NOT an alarm; six-day staleness is
  expected for dormant sessions, A4), or `unknown`. cit:([`freshnessTone`], dashboard/src/data/conversation/format.ts:55-64)
- **`truncateMiddle(value, max)`** — boundary truncation keeping a 60/40 head/tail so the
  distinguishing suffix (e.g. a native id) survives; the caller MUST attach the full value as a
  `title`/tooltip — this returns display text only (A5). cit:([`truncateMiddle`], dashboard/src/data/conversation/format.ts:71-76)
- **`harnessLabel(id)`** — a terse lowercase harness label for chips (A8). cit:([`harnessLabel`], dashboard/src/data/conversation/format.ts:89-100)

### Invariants And Boundaries

- Display-only: every function returns a string for rendering and holds no state. The full value
  behind a truncation is the caller's responsibility (a `title` affordance is mandatory — A5).
- The absent glyph and separator are distinct roles and never mixed (A1); a chip line uses exactly
  one interpunct separator.
- `shortId` returns display text only; the full id is the caller's responsibility via a `title`
  affordance (R6) — the same mandatory-full-value contract as `truncateMiddle`.
- Long-stale is a calm tone, never alarm-red (A4) — the module cannot emit an alarm class.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The A1/A4/A5 convention proofs. | "conversation format conventions (developer findings A1/A4/A5)" | dashboard/src/data/conversation/format.test.ts:5-44 |
| The R6 `shortId` implementation, including the short-value and suffix branches. | `shortId` | dashboard/src/data/conversation/format.ts:83-86 |
| The live `ServingBuildStamp` and `AgentNotifierHeartbeatBadge` consumers. | `ServingBuildStamp`; `AgentNotifierHeartbeatBadge` | dashboard/src/cockpit/Cockpit.tsx:923-953; dashboard/src/cockpit/Cockpit.tsx:959-986 |
| The focus-handoff fallback that uses `shortId` when no seat label exists (R6). | "shortId(" | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:863-863 |
| The ambient-telemetry surface that consumes `joinChips`/`freshnessTone`/`humanizeAge` (F3/F19). | `AmbientTelemetry` | dashboard/src/panels/session-cockpit/conversation/AmbientTelemetry.tsx:54-106 |
| The library rows consuming `truncateMiddle`/`humanizeAge`. | `ConversationLibraryList` | dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx:104-205 |
| The developer visual-findings §A rules this module encodes (task-note pointer: `260720-developer-dashboard-visual-findings.md`). | — | — |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.


- 2026-08-04T16:40:00+02:00 — 260731-EFA-L6 S18-B12 curator correction (reviewer-BLOCK repair): split the pooled row — the A1/A4/A5 convention proofs are bound to the `format.test.ts` body (which does not import or test `shortId`), and `shortId:83-86` is described as implementation branches only; live-consumer ownership retained; the scoped fixer confirmed the final ranges with no writes.
- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 8 direct citations (six function prose citations plus the ambient-telemetry and library references), moved the task-note pointer into Finding prose, and preserved two current-source-mismatched consumer claims unresolved.
- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: added the new `shortId(id, tail)` helper (R6/B10 —
  long ULID/UUID → `…SUFFIX`, full value the caller's `title`) and recorded `humanizeDuration` as the
  SINGLE duration authority now applied to the supervisor badge, rail-footer heartbeat/cutoff, and uptime
  (R5). Verification pinned to the leaf base (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the shared presentation
  conventions — em-dash absent / interpunct separator (A1), humanized fixed-precision durations and
  quiet long-stale tone (A4), and boundary truncation with a mandatory full-value affordance (A5).
  Verification is pinned to the leaf base (`0be0099`) because the new source file is uncommitted;
  closeout owns its first source stamp.
