# skills/l-01-agent-lifecycles/reference/bootstrap-failure-states.md

## Governing Overview

[governing lifecycle overview](../overview.md)

## Purpose

The states a new user's setup actually hits, and the move for each — read at Bootstrap only when a step answers with a state the seat cannot name.

## Code Commentary

The file is a step detail of the Bootstrap role, not capsule intake: the composition manifest registers it as non-injected named-step reading when a step answers with a state the seat cannot name. Each row pairs the state, the surface it is observed from and what it means, so a seat that cannot name what it met is guessing rather than reporting.

The rows keep the product's own distinctions rather than collapsing them: no memory root; unsupported topology, where a repo-local `ar-memory/` root is reported with its exact path and never migrated, rewritten or deleted; a dirty memory repo before adoption, because adoption commits the content it finds; missing providers as a separate recovery action; an unresolvable coordination root, which belongs to `c-13-install-and-onboard` and `runtime_install` rather than a hand-built root; a memory root that is not a Git repository; an already-adopted baseline as the ordinary-use transition. On the foundation side it keeps `not-recorded`, `recorded` at an identity, `unusable` with its refusal codes and a refused admission (`context-not-admitted`) as different facts, tells the seat to report the identity or the state and name the Architect, and forbids deleting, overwriting or migrating an unusable destination. Its last two rows belong to the settings step: `already-configured` or `already-initialized` is reported with its path and never overwritten, merged, completed or re-moded, and `settings-not-writable` or `destination-is-symlink` is a developer decision reported with the exact path rather than a mode change by the seat.

## Evidence

- The failure-state table is a separate step detail read only when a step answers with a state the seat cannot name, and its rows stay distinct rather than merged. [1]
- Foundation states, a refused admission and an unusable destination are reported with their own codes and identity, and the move names the Architect rather than an authoring attempt. [2]
- Settings states are reported with their path: an existing file is never overwritten, merged or re-moded, and a refused write is the developer's decision. [3]
