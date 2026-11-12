# mcp/tests/test_provider_setup_retired.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Negative regressions for the two retired provider identities, including legacy settings
that still mark them enabled. Retirement is id-specific, not a blanket ban on every future
provider identity: the control keeps another enabled id enabled.

## Code Commentary

The first case checks both `provider_enabled` and selection with enabled legacy settings.
The second replaces the three shared/CGC/GrepAI lifecycle-command seams with raising spies.
Shared and provider-specific install/prepare helpers plus watcher-result selection must
return empty results, issue no lifecycle commands, and leave the settings dictionary equal
to its deep copy.

The stop case checks that `stop_provider_watchers_before_refresh` is callable. That is
only presence evidence: it does not exercise a real stop, stop failure or installer cleanup.
Old-watcher stop is deliberately outside the retired install/start/watch gating.

## Boundaries

These are local negative controls on named helper paths, not a real-host provider run or
proof that every direct legacy backend import is impossible. No configuration-file rewrite
or deletion is tested, and reading the cases does not rerun them.

## Evidence

- The complete file owns the behavior and limits described above; documentation/tests are not fresh execution evidence. [1]

## External and cross-repository evidence

No Domain Documentation entries are configured in the resolved source registry.
This card claims only the package-local source contract; no external runtime or
cross-repository acceptance evidence is inferred.
