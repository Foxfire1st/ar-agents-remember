# skills/l-01-agent-lifecycles/reference/bootstrap/failure-states.md

## Governing Overview

[overview](../../overview.md)

## Purpose

The states a new user's setup actually hits, and the response for each. Bootstrap reads it only when a setup step returns a state the seat cannot name.

## Code Commentary

The file is a step detail of the Bootstrap role, not capsule intake: the composition manifest registers it for Bootstrap alone, read when a step returns a state the seat cannot name, and the Bootstrap operation points to it at that moment. Each section pairs an observation (the tool answer or check that shows the state) with the response, and the role's stop rules stay in force.

The sections keep the product's own distinctions rather than collapsing them: a missing memory root; unsupported topology (`memory-mode-unsupported`), where the existing memory root is reported with its exact path and never migrated, rewritten or deleted; a dirty memory repository before adoption, because adoption commits the content it finds; a coordination root that cannot resolve, which belongs to `c-13-install-and-onboard` and `runtime_install` rather than a hand-built root; a memory root that is not a Git repository; and an already-adopted baseline. On the foundation side it keeps `not-recorded`, `recorded` with its identity, `unusable` with its refusal code and a refused admission (`context-not-admitted`) as different facts. `not-recorded` and `recorded` hand on to the foundation-state detail; an unusable object is reported and never deleted, overwritten, migrated or reported as `not-recorded`; a refused admission is reported by its own route and not worked around with a self-supplied path or revision. Its last two sections belong to the settings step: an existing settings file hands on to the Bootstrap operation's settings step, and `settings-not-writable` or `destination-is-symlink` is a developer decision reported with the exact path rather than a mode change by the seat.

## Evidence

- The detail is read only when a step returns a state the seat cannot name, and the role's stop rules stay in force. [1]
- The Bootstrap operation points to the failure states at that moment. [2]
- Setup states stay distinct: unsupported topology preserves the memory root, a dirty repository is read before adoption, and a coordination root is never built by hand. [3]
- Foundation states, a refused admission and an unusable object are reported with their own codes, and none is worked around. [4]
- Settings states are reported with their path; a refused write is the developer's decision. [5]
