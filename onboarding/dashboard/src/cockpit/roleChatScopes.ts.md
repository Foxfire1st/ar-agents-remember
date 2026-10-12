# dashboard/src/cockpit/roleChatScopes.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Memoize canonical document and options scopes by their content.

## Code Commentary

Role plus repository/path values of sprint, master and task references determine document scope. Agent choice also keys options scope. Replacing reference objects with equal content preserves both memo identities; feature-value edits change neither.

## Boundaries

No HTTP, session storage or native-frame authority. A scope-key change invalidates consumers but does not choose a different execution UUID.

## Evidence

- useRoleChatScopes is a current owner of the behavior described above. [1]
