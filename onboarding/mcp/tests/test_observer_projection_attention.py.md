# mcp/tests/test_observer_projection_attention.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin attention ordering, retained-kind dismissal durability and safe occurrence reclamation.

## Code Commentary

Provider alarms sort ahead of drift warnings, then by wait and ID. Drift acknowledgements survive new timestamps when actionableFingerprint stays equal; changed findings recur. Provider-down, failed-setup and blocked-start clicks work without a session and survive unchanged refresh/restart. Only explicit source recovery or a complete gone/configuration census ends those occurrences. Per-repo recovery is not inferred from a workspace-level healthy row; unknown/malformed/partial/unreadable sources retain dismissals, including failures inspecting another provider. Reconciliation does not rewrite unchanged bytes, keeps its read map on failed cleanup, and never removes a click newer than the observation. Retired stale-session JSON is invalid compaction input, not a supported kind. In-process ASGI routes assert failed dismissal persistence returns 503/dismissal-not-held, then successful clicks survive restart. Task-bound worktrees retain precomputed disabled-action reasons. These fixture assertions do not establish live host delivery.

## Evidence

- Equal findings remain dismissed across clock changes and a changed fingerprint recurs. [6]
- Severity, wait and ID determine stable ranking. [7]
- Explicit recovery ends retained-kind occurrences and later failure returns. [8]
- Partial/broken input retains acknowledgement; complete gone facts reclaim. [9]
- Observation cutoff protects a later click. [10]
- Long histories retain current subjects and compact invalid retired/torn rows without repeat rewrite. [11]
- ASGI persistence failure is 503; accepted dismissals survive refresh and restart. [12]
- Precomputed task-worktree disablement remains authoritative. [13]
- Incomplete provider census cannot clear another provider acknowledgement. [14]
