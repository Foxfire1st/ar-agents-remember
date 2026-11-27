# mcp/src/agents_remember/cli/provider_limit_hold.py

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

The one check every send path to a role seat reaches — holding a message to a limited recipient with the reason and reset — plus the thin `agents-remember provider-limits` operator CLI adapter (`status`, `suppress`, `unsuppress`).

## Code Commentary

The fact comes from the product's one limit file and never from chat text, an error message or a turn's failure kind. The check sits in its own module so `role_message`, the developer's tray send and a report to an architect all reach one place: a send path that skips it is a defect, not a variant.

`read_usage_for_agents` performs that read for one tick: one bridge call carries the stamped agents and each due report's ordered candidate seats. A refresh the bridge marks failed is recorded so the writer keeps that report's prior fact and mapping, and a due report with no eligible seat is logged once per period rather than read.

A held answer carries `provider-limit` as its reason and the moment work may resume, and it is held even when the recipient is idle, because a provider limit does not depend on the seat being busy. The module reads the role record to map an agent to its report ids and asks the serving writer only when a fresh read is due, so a send that finds no limit costs no host call.

Delivery is not this module's: a held message waits for the reset and is released by the drain's own policy.

`add_arguments`, `_resolve_cli_limits_path`, and `run` implement the `agents-remember provider-limits <status|suppress|unsuppress>` runtime CLI command (accepting `--config` before or after the subcommand). It parses `--report`, `--window`, and `--agent` into a `SuppressionSelector`, delegates every read and mutation exclusively to `serving/paseo/provider_limits.py` (`provider_limits_status`, `suppress_provider_limit_windows`, `unsuppress_provider_limit_windows`), prints JSON, and returns exit code `0` on success, `2` on config/selector/non-live refusals, or `1` on filesystem/unexpected errors.

## Evidence

- Registers `provider-limits status|suppress|unsuppress` arguments and delegates all mutations to `serving.paseo.provider_limits`, printing JSON with exit codes 0/1/2. [1]
