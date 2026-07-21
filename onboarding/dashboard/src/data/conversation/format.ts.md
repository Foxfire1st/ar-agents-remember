# dashboard/src/data/conversation/format.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation/format.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T05:30+02:00 |
| lastVerifiedCommitHash | `1119b64ff1564c5fc76fd518f88e529535c04b34` |
| lastVerifiedCommitDate | 2026-07-21T08:14:40+02:00|
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

- **`ABSENT = "—"`** (L12) — the em-dash for a genuinely absent value (A1). Callers must never chain
  these; empty states explain or collapse instead.
- **`SEP = " · "`** (L14) — the one separator convention: a spaced interpunct between chips on one
  line (A1/A8).
- **`joinChips(parts)`** (L17-L19) — filters out `null`/`undefined`/empty strings and joins the
  survivors with `SEP`; all-empty input collapses to `""` (no dash-chain, no reassurance-zero cluster
  — A2).
- **`humanizeDuration(ms)`** (L25-L37) — the two most significant units with fixed precision
  (`800 ms`, `45 s`, `3 m 12 s`, `2 h 5 m`, `6 d 0 h`). Never raw minutes or six-decimal seconds
  (the exact developer eyesores `8638.1m` / `518288.173569s`). Negative/non-finite → `ABSENT`. **This is
  the SINGLE duration authority (R5, 260718-CHATS-L5P):** it now formats the supervisor-heartbeat age and
  uptime (`cockpit/Cockpit.tsx`) and the rail-footer heartbeat/cutoff (`SessionRail.tsx`) in addition to
  the telemetry/library surfaces — every duration/age in the composed app routes through here rather than
  a local `/60` or `.toFixed`.
- **`shortId(id, tail = 6)`** (L78-L83, NEW — R6/B10, 260718-CHATS-L5P) — a long ULID/UUID (`> 12` chars)
  collapses to its distinguishing suffix (`…ZKCZEP`) so the rail/chrome never leaks a 26-char raw id;
  short ids pass through unchanged. Display-only — the caller MUST attach the full value as a
  `title`/tooltip (so it stays reachable + copyable), exactly like `truncateMiddle`. Consumers:
  `ChatContextBar` task badges, the `SessionsView` focus-handoff banner fallback.
- **`humanizeAge(iso, now)`** (L40-L47) — an ISO timestamp rendered as `<humanized> ago`; absent /
  unparseable input → `ABSENT`; a future timestamp → `just now`.
- **`freshnessTone(state, ageMs)`** (L55-L64) — maps a freshness state to a QUIET-distinct tone:
  `fresh`, `aging` (a brief <60 s lag), `stale` (long-stale, calm — NOT an alarm; six-day staleness is
  expected for dormant sessions, A4), or `unknown`.
- **`truncateMiddle(value, max)`** (L71-L76) — boundary truncation keeping a 60/40 head/tail so the
  distinguishing suffix (e.g. a native id) survives; the caller MUST attach the full value as a
  `title`/tooltip — this returns display text only (A5).
- **`harnessLabel(id)`** (L79-L90) — a terse lowercase harness label for chips (A8).

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The A1/A4/A5 convention proofs (+ the R6 `shortId` cases). | L1-L44 | [format.test.ts](format.test.ts) |
| The rail footer + supervisor badge consuming `humanizeDuration` as the single duration authority (R5). | — | [../../panels/session-cockpit/SessionRail.tsx](../../panels/session-cockpit/SessionRail.tsx) · [../../cockpit/Cockpit.tsx](../../cockpit/Cockpit.tsx) |
| The rail/context-bar/handoff consumers of `shortId` (R6). | — | [../../panels/session-cockpit/ChatContextBar.tsx](../../panels/session-cockpit/ChatContextBar.tsx) · [../../panels/session-cockpit/SessionsView.tsx](../../panels/session-cockpit/SessionsView.tsx) |
| The ambient-telemetry surface that consumes `joinChips`/`freshnessTone`/`humanizeAge` (F3/F19). | — | [../../panels/session-cockpit/conversation/AmbientTelemetry.tsx](../../panels/session-cockpit/conversation/AmbientTelemetry.tsx) |
| The library rows consuming `truncateMiddle`/`humanizeAge`. | — | [../../panels/session-cockpit/conversation-library/ConversationLibraryList.tsx](../../panels/session-cockpit/conversation-library/ConversationLibraryList.tsx) |
| The developer visual-findings §A rules this module encodes. | — | (task notes) `260720-developer-dashboard-visual-findings.md` |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: added the new `shortId(id, tail)` helper (R6/B10 —
  long ULID/UUID → `…SUFFIX`, full value the caller's `title`) and recorded `humanizeDuration` as the
  SINGLE duration authority now applied to the supervisor badge, rail-footer heartbeat/cutoff, and uptime
  (R5). Verification pinned to the leaf base (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the shared presentation
  conventions — em-dash absent / interpunct separator (A1), humanized fixed-precision durations and
  quiet long-stale tone (A4), and boundary truncation with a mandatory full-value affordance (A5).
  Verification is pinned to the leaf base (`0be0099`) because the new source file is uncommitted;
  closeout owns its first source stamp.
