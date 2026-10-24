# mcp/tests/test_paseo_catalog.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Drives the launcher-options route against a recording fake bridge and proves the choices a launch is
offered come from the host runtime's own catalog: cached per runtime, validated before anything is
created, and named when the runtime is unconfigured or unreachable. It is route and fixture coverage;
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
- **Caching is per runtime.** `test_catalog_is_cached_per_runtime_and_only_a_refresh_rediscovers`
  shows a second read answering from cache and only an explicit refresh asking the runtime again.
- **Degradation is named.** `test_an_unoffered_default_is_flagged_and_never_replaced`,
  `test_a_partial_catalog_is_kept_and_a_failed_discovery_caches_nothing` and
  `test_an_unreadable_catalog_is_a_named_failure_and_is_not_cached` keep a flagged default, a partial
  answer and an unreadable answer apart: a failed discovery or unreadable catalog caches nothing, while a
  returned partial catalog is kept, with its listing error, until a refresh replaces it.
- **Refusals stay distinct.** `test_route_errors_name_not_configured_and_unreachable_apart` separates
  the two states, and `test_a_launch_is_validated_against_the_catalog_before_anything_is_created`
  proves an unservable launch is refused before an agent or workspace exists.
- **Service tiers.** `fast` is offered independently of the host default, a model override revalidates
  capability, and `test_unsupported_tier_and_exact_unavailable_model_are_not_substituted` refuses an
  unsupported tier or an exactly-named unavailable model rather than substituting one.

### Conventions

Each case builds its own runtime settings and `McpRuntimeConfig` under a temporary root and queues
the bridge replies it needs, so no case reads another's cache.

### Invariants And Boundaries

- The catalog is only ever read through the bridge; nothing here starts a daemon, an agent or a task.
- Cache entries are keyed by the runtime they came from, so two runtimes never share a catalog.

## Evidence

- The options route, its per-runtime cache, partial and unreadable catalogs, refused defaults, distinct
  route errors, launch validation and service-tier handling are all asserted in this file. [1]
