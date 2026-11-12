# mcp/tests/test_providers_remove.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Fixture-based safety regressions for the explicit provider-folder removal CLI, separately
from non-destructive installation and provider retirement.

## Code Commentary

Temporary trusted settings retain legacy provider keys and create owned runner/data folders.
Dry run must keep those folders and load their coordination root. Apply patches the stop
seam, requires one real-mode stop request, and removes the seeded folders. A failed-stop
case returns failure and preserves folders. The busy case starts a real disposable process
with cwd inside a provider folder, waits for the production `/proc` scanner to observe it,
and requires refusal/preservation; `finally` terminates and joins that fixture process.

Foreign-root alias cases protect a user-data sentinel and require refusal before the stop
seam, including dry run. A consistent coordination-root alias is a positive control: it
still resolves the owned folders and can clean them. Thus not every symlink is an escape;
ownership is determined by the physical root/target relationship.

## Boundaries

The tests do not clean the user's providers, grant general deletion authority, or establish
an atomic race-free filesystem lock. Some docstring claims (reported pid/bytes) are supported
by production formatting/control flow rather than every case capturing stdout. Assertions
and fixture structure are described here without claiming a fresh execution or whole-suite PASS.

## Evidence

- The complete file owns the behavior and limits described above; documentation/tests are not fresh execution evidence. [1]

## External and cross-repository evidence

No Domain Documentation entries are configured in the resolved source registry.
This card claims only the package-local source contract; no external runtime or
cross-repository acceptance evidence is inferred.
