# harness_capabilities.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines the normalized own-adapter capability vocabulary shared by Claude stream-json, Codex
app-server, and Pi RPC. It carries live model catalogs with model-local effort choices, projects the
ACP Sense 1 category-keyed select shape without ACP transport, and establishes launch/set result
types for later leaves.

## Code Commentary

### Logic

`ModelCapability` nests `EffortOption` rows under one model and retains optional resolved identity,
description, default, visibility, selectability, and provider facts. `CapabilitySnapshot` carries the
catalog and current selection. Its config projection emits a `model` select only when the current
model is known and a `thought_level` select only when current effort is known. The selected model is
always retained in model options—even if hidden or no longer selectable—so `currentValue` remains
honest and belongs to the option set. `LaunchKnobs` carries additive native argv/env/session config
plus the argv options and config keys exclusively owned by that adapter. The launch boundary uses
those ownership declarations to reject a competing free-form selector instead of silently choosing
one. `SetResult` carries explicit mutation acceptance evidence. `SET_ACCEPTANCE_VALUES` is the
runtime authority for the same five tokens expressed by the static literal, and serialization
rejects any out-of-vocabulary value before exposing a serving shape. Serializer helpers expose
stable camel-case objects without inferring effective values. L4's strict inverse parsers rebuild
snapshots and `SetResult` values from exact-session IPC. They validate required text and boolean
fields, the five acceptance tokens, nested model-local effort lists, and any supplied
`configOptions`; that projection must exactly equal what the catalog itself derives.

### Conventions

Normalized keys preserve vendor tokens rather than inventing aliases. ACP-inspired config ids and
categories use `model` and `thought_level`; this is shape adoption only. Config `currentValue` is
always a string when a select is emitted.

### Invariants And Boundaries

- Effort is model-gated; there is no global effort list or hardcoded default catalog path.
- The only set acceptance values are `echo-verified`, `immediate`, `queued`, `unknown`, and
  `unsupported`; runtime validation and serialization fail closed outside that set.
- `echo-verified` is the only result category that may carry a proven effective value; the queue
  additionally enforces the `ok`/effective-value relationships for every category.
- Unknown current model/effort values are omitted from the ACP-style projection rather than guessed.
- IPC parsing rejects a config projection that disagrees with the model-gated catalog instead of
  trusting two competing representations of the same state.
- Adapter-owned launch selectors are explicit data; callers must conflict-check them before native
  discovery or startup rather than relying on argument order.
- This module has no vendor subprocess, session lifecycle, ACP transport, composer-paste, daemon, or
  settings ownership.

### Todos

None known for the normalized L4 serialization/parsing boundary.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

No configured domain documentation could be checked.

### Repo-Internal References

The adapter boundary consumes these data types, and each native adapter exposes cached advertise
plus transient discovery through that boundary.

- The protocol, discovery, and launchable adapter ports consume `CapabilitySnapshot`, `LaunchKnobs`, and `SetResult`. [1]
- The submission authority validates the exact `SET_ACCEPTANCE_VALUES` vocabulary and the ok/effective-value relationship before releasing a setter result to its waiter. [2]
- The launch boundary consumes owned selectors before token-free discovery and runtime construction. [3]
- The exact-session client uses the strict inverse parsers for live advertise and set responses. [4]
- The normalized capability and setter payloads have strict inverse parsers. [5]
- The daemon emits this unchanged normalized shape for both pre-session and live capability reads. [6]
- Claude produces native model/effort flags. [7]
- Codex declares session config plus owned CLI/config selectors. [8]
- Pi declares provider-qualified model and thinking flags. [9]

### Cross-Repo References

No external repository or ACP transport dependency is implemented by the normalized type layer.

No meaningful cross-repo references found.
