# mcp/tests/test_paseo_catalog.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Drives the launcher-options route against a recording fake bridge and proves the choices a launch is
offered come from the host runtime's own catalog: freshly asked per operation, validated against answered parts before anything is
created, and named when the runtime is unconfigured. Last successful answers cover failed parts; wholly unknown parts remain unchecked. It is route and fixture coverage;
no daemon, agent workspace or browser is involved.

## Code Commentary

### Logic

`FakeBridge` stands in for `bridge_call` with a queue of replies per command and a record of every
call it was asked to make. `PaseoCatalogTestCase.bridge()` and `PaseoCatalogTestCase.options()` run one
options request with task resolution and settings stubbed out, so a case observes the route's own
decision. `_requested_launch_values`, `_legacy_options_fields` and `_legacy_options_projection` build
the requested and legacy option shapes, and `HARNESS_ORDER` fixes the order harnesses are offered in.

- **The catalog is the source of options.** `test_options_come_from_the_runtime_catalog` reads the
  harnesses, models and efforts out of the runtime's answer instead of a local default.
- **Questions are fresh.** `test_each_view_and_start_asks_fresh_and_refresh_rescans`
  requires every view and start to ask the runtime, with explicit refresh also requesting a provider rescan.
- **Degradation preserves successful answers.** `test_an_unoffered_default_is_flagged_and_never_replaced`,
  `test_whole_failure_uses_previous_success_without_erasing_it` and
  `test_an_unreadable_catalog_leaves_configured_choices_unchecked` distinguish known unoffered defaults, saved successful answers and wholly unknown offerings.
- **Missing runtime and unoffered choices stay distinct.** `test_not_configured_runtime_still_names_the_missing_authority` identifies absent runtime authority, and `test_a_launch_is_validated_against_the_catalog_before_anything_is_created`
  proves an unservable launch is refused before an agent or workspace exists.
- **Service tiers.** `fast` is offered independently of the host default, a model override revalidates
  capability, and `test_unsupported_tier_and_exact_unavailable_model_are_not_substituted` refuses an
  unsupported tier or an exactly-named unavailable model rather than substituting one.

### Conventions

Each case builds its own runtime settings and `McpRuntimeConfig` under a temporary root and queues
the bridge replies it needs, so no case reads another's saved catalog store.

### Invariants And Boundaries

- The catalog is only ever read through the bridge; nothing here starts a daemon, an agent or a task.
- Saved catalog parts are scoped to their runtime, and live answers are shared only within one operation.

## Evidence

- The options route, fresh per-operation questions, saved and unknown catalog parts, refused defaults, distinct
  route errors, launch validation and service-tier handling are all asserted in this file. [1]



- The scoped current source carries the module/document behavior described above. [1]
