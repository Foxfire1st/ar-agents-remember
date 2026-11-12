# mcp/src/agents_remember/serving/actions.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Pure mapping of enclosure action availability and attention dismissals into attributed HTTP outcomes. There is no gate-decision intent, gate approval/rejection action family or lifecycle resume action in this module.

## Code Commentary

Ordinary actions need a target and matching enabled precomputed enclosure action; missing/unknown target, absent action and disabled action remain distinct. Lookup includes unbound and task-bound worktrees. Acceptance is attributed 202 intent, not mutation. Dismissal needs nonblank itemId, an actually published item and exact matching kind; missing itemId is 400, unknown item is 404 and kind mismatch is 400. There is no dismissibility refusal: every published entry is acknowledged once per occurrence (v2 rule 7), so the backend accepts the dismissal of every published kind and refuses only an item this projection does not publish. Dismissing changes nothing at the cause. The returned DismissalIntent captures the published actionable fingerprint. Lifecycle-target exemption rules are removed; actor and dashboard provenance remain explicit. The router owns persistence and its failure.

### 20261023-L190-v2 No Dismissibility Refusal Remains

`_dismiss_action_outcome` (:96-136) evaluates three outcomes only: 400 `missing-item` for a blank id, 404 `unknown-item` for an id this projection does not publish, and 400 `item-kind-mismatch` for a kind that is not the published row's own. The 409 `not-dismissible` branch is removed with rule 7's first form: the acknowledgement no longer has to be refused at the cause, because it never claims to change the cause.

Everything else in the action path is untouched: acceptance is still an attributed 202 intent rather than a mutation, the intent still carries the published actionable fingerprint, the router still owns persistence and its failure (`dismissal-not-held` 503), and actor/dashboard provenance is still explicit.

## Evidence boundary

This is current-source interpretation of the A9 candidate, not a new test result, CODE grade or MEMORY acceptance. The retained supporting references below are reauthored through the ordinary fixer; unsupported removed constructs are withdrawn, not rebound to arbitrary neighboring code.

## Source-bound reference inputs


- Anchor: Current precomputed enclosure availability and workspace shape. [1]

- [2]
- [3]



- Anchor: Retained compact attention acknowledgements. [5]



- Dismiss actions bypass target lookup but require a nonempty itemId, an item published in the attention queue and an exactly matching kind. Missing itemId yields 400, unknown item yields 404 and kind mismatch yields 400. Every published kind is dismissible; a match returns 202 plus a DismissalIntent carrying the published actionable fingerprint. Non-dismiss actions require a target (400 if absent), a known target (404 otherwise) and a published enabled action (409 if absent or disabled); enabled actions return 202. There is no actionable-drift-only missing-target exemption. [6]
