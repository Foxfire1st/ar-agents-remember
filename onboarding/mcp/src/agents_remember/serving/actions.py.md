# mcp/src/agents_remember/serving/actions.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Pure mapping of enclosure action availability and attention dismissals into attributed HTTP outcomes. There is no gate-decision intent, gate approval/rejection action family or lifecycle resume action in this module.

## Code Commentary

An ordinary action needs a target and a matching enabled precomputed enclosure action: missing target, unknown target, absent action and disabled action stay distinct. Acceptance returns 202 with attributed intent but no product mutation. Dismissal requires a nonblank itemId and a lifecycle target except for the repo-level actionable-drift signal. The evaluator returns a DismissalIntent; the router owns its durable write. Actor provenance is typed and dashboard source attribution is set server-side. These remaining boundaries do not revive the removed gate UI.

## Evidence boundary

This is current-source interpretation of the A9 candidate, not a new test result, CODE grade or MEMORY acceptance. The retained supporting references below are reauthored through the ordinary fixer; unsupported removed constructs are withdrawn, not rebound to arbitrary neighboring code.

## Source-bound reference inputs

- [1]
- [2]
- [3]
- [5]
- [6]

