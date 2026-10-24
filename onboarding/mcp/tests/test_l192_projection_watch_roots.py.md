# mcp/tests/test_l192_projection_watch_roots.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Bind the projection watch plan to the state the projection actually reads, and show that the
retired provider display roots no longer enter it.

## Code Commentary

`logs/providers/status` and `logs/providers/setup` used to enter `projection_input_roots` with no
entry in `projection_domains_for_paths`, so an admitted event beneath them fell open to every
domain and rebuilt projections from state nothing reads. The first case stages both directories on
disk and asserts that no path in the plan is the provider display root or lives beneath it, then
that each surviving root — task, observer workspace, drift, start progress and tool report —
resolves an event beneath it to exactly its own domain. The last case keeps the independent
provider-safety sampler: it retains its loop and needs no watch root. The roots and the domain map
are asserted together because either half alone leaves a path unbound.

## Evidence

- The retired provider display roots are staged on disk and still absent from the plan, while each
  live root maps to one domain. `test_retired_provider_display_roots_are_not_projection_inputs`,
  `test_genuine_projection_roots_keep_their_own_domain`
- The safety sampler survives the plan change without a watch root.
  `test_the_independent_safety_sampler_survives_the_watch_plan_change`
