# mcp/tests/test_role_single_server.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Model-free launch/receipt/brief regressions for carrying the product's other server once,
while preserving the task server and unrelated user servers. The module distinguishes
native terminal argument construction, supplied-map filtering and host-route metadata.

## Code Commentary

Pure controls pin the other product server name and per-harness exclusions: Pi filters,
Claude denies both tool-name spellings, Codex uses the unquoted dotted disable override
plus a never-spawned command, and Eve is host-owned. Caller filters merge without dropping
or reordering unrelated arguments; task-server names must not match the exclusion patterns.
Unknown or absent harness acceptance supplies no verified exclusion record.

Constructed `RoleLaunch` inputs check task-only server maps, the exclusion record and the
adapter input's identity/workspace fields. A non-circular supplied-map fixture includes task,
other-product and user entries: filtering removes only the other product entry, while the
no-record path preserves the full supplied map. Receipt fields derive from the applied
filtered input, not just the harness label.

The brief control preserves the task-server guidance. The between-copies choice remains
on the unapplied host route and disappears only under the applied, recognized terminal
predicate; missing server/unknown acceptance keeps it. The record at an adapter boundary
must not be confused with which fields the final native-host wire sends.

## Boundaries

These helpers/dictionary assertions do not show a real agent's live tool list or prove
ambient host registration exclusion. Those host/evidence5 concerns remain separately owned
by L132, not a new first-real-agent obligation or implementation proof credited to L112.
No configuration file, user server or harness model setting is changed by reading this card.

## Evidence


- The complete file owns the behavior and limits described above; documentation/tests are not fresh execution evidence. [1]


## External and cross-repository evidence

No Domain Documentation entries are configured in the resolved source registry.
This card claims only the package-local source contract; no external runtime or
cross-repository acceptance evidence is inferred.
