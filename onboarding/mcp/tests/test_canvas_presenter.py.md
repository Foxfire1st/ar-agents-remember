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


A presenter constructed without an injected runner uses `UnconfiguredPresenterRunner`: its start fails with `no-confined-harness` and creates no `host/prepared-start.json`. The retired native presenter is no longer a production default; explicit fixture runners retain their own tested behavior.

## Evidence

- The case `test_a_start_requires_explicit_activation_and_this_pages_comparison` protects this behaviour. 
- The case `test_the_design_text_is_resolved_bounded_and_named` protects this behaviour. 
- The case `test_the_capability_text_is_shipped_inside_its_budget` protects this behaviour. 

- An event-coordinated late receipt cannot revive a cancelled attempt; the shared hang guard only bounds a stuck wait. [4]

- A presenter constructed without an injected runner uses `UnconfiguredPresenterRunner`: its start fails with `no-confined-harness` and creates no `host/prepared-start.json`. The retired native presenter is no longer a production default; explicit fixture runners retain their own tested behavior. [5]

- Retired at the fifth freeze d59c3493: mcp/tests/test_canvas_presenter.py::test_a_start_requires_explicit_activation_and_this_pages_comparison - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976; mcp/tests/test_canvas_presenter.py::test_the_design_text_is_resolved_bounded_and_named - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976; mcp/tests/test_canvas_presenter.py::test_the_capability_text_is_shipped_inside_its_budget - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976. Retired means the anchor no longer stands, not that the cited subject was deleted.
