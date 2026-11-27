# mcp/tests/test_provider_limit_hold.py

## Governing Overview

[mcp overview](../overview.md)

## Purpose

The one send check and a drain that waits for the reset.

## Code Commentary

A message to a limited recipient is held with the reason and the reset time on every send path, and the drain pauses before it reads the host, so waiting costs no bridge process. The one exception is the single host read for a recipient the publication shows ended.

`test_stamped_empty_usage_list_can_remove_the_mapping_during_a_periodic_miss` holds the one clearing case: a successful stamped answer with an empty list removes the mapping even while a periodic refresh for the same report is missing.

The drain-pause fixture (`_batch`) constructs a real `McpRuntimeConfig` scoped to the test's temporary coordination root so `pause_for_provider_limit` exercises durable reset-index scheduling alongside the limit-check and wait rules.
