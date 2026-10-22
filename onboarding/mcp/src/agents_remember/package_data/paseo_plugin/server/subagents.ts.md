# mcp/src/agents_remember/package_data/paseo_plugin/server/subagents.ts

## Governing Overview

[plugin overview](../overview.md)

## Purpose

The provider subagents the host reports for AR's role agents: one subscription per boot, the running set per agent, and the bounded reconciliation that heals a gap.

## Code Commentary

The plugin subscribes once per boot to `agent.provider_subagents.update` and keeps the subagents whose last `upsert` says `running`, with their `createdAt`. It never polls and holds no timer. Traffic it does not keep is skipped rather than counted — a `timeline` row and an update for a parent outside `role-agents.json` change nothing and cause no write, because the publication emits its ignored events with every write.

Both stores are bounded like the plugin's other stores, and a count beyond a bound is published as the bound, so the publication never grows with the host's traffic.

Reconciliation is explicit and bounded: one integer generation and no history. Beginning one drops every earlier decision, so a connection gap cannot keep an absent child alive, and a reply naming an older reconciliation is refused once a newer one has been consumed. The list step asks only about agents with an open session, because asking a closed agent loads its session from storage; the merge lays that list under the events, and an update seen since the reconciliation began wins.
