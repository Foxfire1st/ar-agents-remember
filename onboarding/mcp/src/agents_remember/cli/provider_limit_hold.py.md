# mcp/src/agents_remember/cli/provider_limit_hold.py

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

The one check every send path to a role seat reaches: a message to a limited recipient is held with the reason and the reset instead of being sent.

## Code Commentary

The fact comes from the product's one limit file and never from chat text, an error message or a turn's failure kind. The check sits in its own module so `role_message`, the developer's tray send and a report to an architect all reach one place: a send path that skips it is a defect, not a variant.

A held answer carries `provider-limit` as its reason and the moment work may resume, and it is held even when the recipient is idle, because a provider limit does not depend on the seat being busy. The module reads the role record to map an agent to its report ids and asks the serving writer only when a fresh read is due, so a send that finds no limit costs no host call.

Delivery is not this module's: a held message waits for the reset and is released by the drain's own policy.
