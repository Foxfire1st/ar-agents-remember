# mcp/src/agents_remember/cli/paseo_usage_reports.mjs

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

Carry the bridge's usage-report read out of `paseo_bridge.mjs`, so one module owns the request shape, the report-id-only refresh and the periodic verdicts the serving tick passes in.

## Code Commentary

The bridge dispatches `usage-reports` here. A stamped read names the agents the tick saw end; a forced refresh names a report id alone and never both selectors, which the real client refuses. A leaf seat's entry older than sixty seconds is refreshed once, and a shared report is refreshed at most once per batch. The module keeps the report rows and the `periodic` outcomes separate: a periodic verdict is shared by every seat that names the same report, a stamped-only cached entry survives a mixed batch, and a failed refresh is reported so the writer keeps the prior fact.

`fetchedAt` comes from the client's own answer; the module invents no freshness. A reply that lacks a report for a requested periodic candidate is returned as a failed outcome rather than as an empty list, so a missing target never reads as zero usage.

## Evidence

- The extracted module keeps the request shape, the report-id-only refresh and each periodic outcome. [1]
