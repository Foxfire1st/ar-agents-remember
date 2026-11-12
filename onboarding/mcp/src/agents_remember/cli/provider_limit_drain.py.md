# mcp/src/agents_remember/cli/provider_limit_drain.py

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

What a held-message drain owes a recipient whose provider limit is running: wait for the reset, and pay at most one host read per `ended` stamp.

## Code Commentary

Waiting out a limit must cost no host read. For a limited recipient the drain therefore pauses with outcome `provider-limit` before any read, and the first sweep after the reset delivers what waits, in order, within that sweep.

The one read a drain still owes is for a recipient the publication shows `ended`: an archive ends its waiting messages, a closed session keeps them waiting, and that reading is paid once per `ended` stamp rather than on every sweep. The order is part of the rule — the limit comes first and costs no host read; only then, and only for a stamped `ended` recipient, is one reading taken.

Both decisions are policy, so they live here rather than in the held-message store's own module: that module owns the store and the drain, this one decides when they wait.
