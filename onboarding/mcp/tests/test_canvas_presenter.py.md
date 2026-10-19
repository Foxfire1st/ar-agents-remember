# mcp/tests/test_canvas_presenter.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The presenter capability: launch choices with provenance, the design text's resolution and bound, the capability text's budget, explicit activation, the attempt lifecycle and confined publication.

## Code Commentary

- A start requires explicit activation and this page's own comparison.
- The design text is resolved, bounded and named by digest.
- The capability text is shipped inside its word budget.

- Delayed-receipt and publication/cancellation races wait on their actual events. `HANG_GUARD_SECONDS` bounds a stuck wait or join without treating a short scheduling deadline as the tested condition.

## Evidence

- The case `test_a_start_requires_explicit_activation_and_this_pages_comparison` protects this behaviour. [1]
- The case `test_the_design_text_is_resolved_bounded_and_named` protects this behaviour. [2]
- The case `test_the_capability_text_is_shipped_inside_its_budget` protects this behaviour. [3]

- An event-coordinated late receipt cannot revive a cancelled attempt; the shared hang guard only bounds a stuck wait. [4]
