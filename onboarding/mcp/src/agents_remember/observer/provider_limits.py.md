# mcp/src/agents_remember/observer/provider_limits.py

## Governing Overview

[Observer overview](overview.md)

## Purpose

The read side of the product's one provider-limit record, placed at `observer` so the one status function can read a limit without an upward import.

## Code Commentary

The product keeps every limit in `<PASEO_HOME>/agents-remember/provider-limits.json`; the product's runtime, at `serving.paseo.provider_limits`, is its one writer and this module is the only reader model the status function needs. It sits at `observer` deliberately: the limit is read where task state is computed, and reaching up into `serving` or `cli` for it would add the upward edge MIK-R190 rule 19 forbids.

The file holds, per report id, the moment work may resume, the report's source and account labels, the exhausted windows and when the fact was observed; and, per agent, the report ids its last read named. An agent is limited while now is before the `until` of one of its report ids, so one exhausted account stops every seat on it. The models are strict and frozen: an absent or malformed file reads as nothing limited, which is the fallback for a provider with no report.

`limited_until` answers one agent's moment of resumption, and `read_provider_limits` returns the whole record; neither writes, and neither reads the host.
