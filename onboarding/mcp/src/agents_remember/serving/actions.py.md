# mcp/src/agents_remember/serving/actions.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Pure mapping of enclosure action availability and attention dismissals into attributed HTTP outcomes. There is no gate-decision intent, gate approval/rejection action family or lifecycle resume action in this module.

## Code Commentary

Ordinary actions need a target and matching enabled precomputed enclosure action; missing/unknown target, absent action and disabled action remain distinct. Lookup includes unbound and task-bound worktrees. Acceptance is attributed 202 intent, not mutation. Dismissal needs nonblank itemId, an actually published item and exact matching kind; unknown item is 404 and kind mismatch 400, and a published row that is not dismissible is refused 409 `not-dismissible` before the kind comparison, because a live native cause clears only when its cause ends and cannot be acknowledged away. The returned DismissalIntent captures the published actionable fingerprint. Lifecycle-target exemption rules are removed; actor and dashboard provenance remain explicit. The router owns persistence and its failure.

## Evidence boundary

This is current-source interpretation of the A9 candidate, not a new test result, CODE grade or MEMORY acceptance. The retained supporting references below are reauthored through the ordinary fixer; unsupported removed constructs are withdrawn, not rebound to arbitrary neighboring code.

## Source-bound reference inputs

- [1]
- [2]
- [3]
- [5]
- Dismiss actions bypass target lookup but require a nonempty itemId, a published dismissible row and exactly matching kind. Missing itemId yields 400, unknown item yields 404, and a published non-dismissible row yields 409 not-dismissible before kind comparison; kind mismatch yields 400. A matching dismissible row returns 202 plus a DismissalIntent carrying the published actionable fingerprint. Non-dismiss actions require a target (400 if absent), a known target (404 otherwise) and a published enabled action (409 if absent or disabled); enabled actions return 202. There is no actionable-drift-only missing-target exemption. [6]
