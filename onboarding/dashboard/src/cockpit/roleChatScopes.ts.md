# dashboard/src/cockpit/roleChatScopes.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Memoize canonical document and options scopes by their content.

## Code Commentary

Role plus repository/path values of sprint, master and task references determine both document scope and options scope (`optionsScope` aliases the memoized `documentScope`, omitting `agentId`). Replacing reference objects with equal content or changing agent/model/effort/mode/feature overrides preserves both memo identities so metadata options reads do not refire.

## Boundaries

No HTTP, session storage or native-frame authority. A scope-key change invalidates consumers but does not choose a different execution UUID.

## Evidence

- useRoleChatScopes is a current owner of the behavior described above. [1]
