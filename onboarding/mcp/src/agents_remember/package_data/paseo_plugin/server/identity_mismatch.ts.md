# mcp/src/agents_remember/package_data/paseo_plugin/server/identity_mismatch.ts

## Governing Overview

[Native Paseo plugin](../overview.md)

## Purpose

Provides pure, host-free recognition and parent-line composition for `IDENTITY MISMATCH:` turn-end lines so a seat that detects a wrong tool-server binding bypasses silent-end waiting and self-wakes and reports its line verbatim to its parent.

## Code Commentary

- **Constants:** `IDENTITY_MISMATCH_PREFIX = "IDENTITY MISMATCH:"` (case-sensitive), `IDENTITY_MISMATCH_LOG_KIND = "identity-mismatch"`, `DEFAULT_LAST_TEXT_LIMIT = 300`, `DEFAULT_LINE_LIMIT = 1000`, `LEADING_MARKERS = /^[ \t*_>#`"-]*/`, and `SYMMETRIC_OPENERS = /[`*_"]+$/`.
- **Extraction:** `extractIdentityMismatchLine(lastText, maxLength = 300)` returns `null` unless `lastText.kind === "text"` and the trimmed text starts with `IDENTITY_MISMATCH_PREFIX` after optional leading whitespace or Markdown markers. `stripMatchingClosingWrappers(lead, text)` reverses any symmetric opener suffix and strips only a matching closing sequence at the end of the body, preserving interior or trailing backticks in unwrapped payloads, then slices to `maxLength`.
- **Parent-line composition:** `composeIdentityMismatchParentLine(agentId, facts, mismatchLine, lineLimit = 1000)` formats `turn ended: <role> <agentId> · <task>; last line: <mismatchLine>; newest report: <reportPath>` without any `marked: silent end` tag and slices to `lineLimit`.
- **Boundary:** Pure string helpers only; performs no host calls, tracker mutations, or delivery.

## Relationships

- **Callers:** `mcp/src/agents_remember/package_data/paseo_plugin/server/turn_ended.ts` (`noteTurnEnded` invokes `extractIdentityMismatchLine` and `composeIdentityMismatchParentLine` before declared-wait and silent-end scheduling, cancels pending wakes/waits, logs `identity-mismatch` without incrementing `silentEnds`, and routes delivery through `noteParentLine`).
- **Type imports:** Type-only imports `TurnEndedFacts` and `TurnLastText` from `./turn_ended.ts`.
- **Tests:** `mcp/src/agents_remember/package_data/paseo_plugin/server/identity_mismatch.test.ts`.

## Evidence

- Case-sensitive prefix, log-row kind, default 300/1000 character limits, and Markdown leading/wrapper regexes define mismatch matching. [1]
- Symmetric closing-wrapper stripping removes only matching openers while preserving interior and unwrapped backticks. [2]
- Extractor requires `kind === "text"`, strips leading markers and matching wrappers, and truncates to `maxLength`. [3]
- Parent-line composer emits seat role, id, task, verbatim mismatch line, and newest report path without silent-end marking, capped at `lineLimit`. [4]
