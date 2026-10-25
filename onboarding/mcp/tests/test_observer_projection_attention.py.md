# mcp/tests/test_observer_projection_attention.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin attention ordering, retained-kind dismissal durability and safe occurrence reclamation.

## Code Commentary

The queue lists the newest entry first — age ascending, ID breaking the tie, and an entry without an age counting as zero — so a drift row that names no age sorts with the newest rather than sinking below one that can date itself. Drift acknowledgements survive new timestamps when actionableFingerprint stays equal; changed findings recur. Blocked-start clicks work without a session and survive unchanged refresh/restart. Only explicit source recovery or a complete gone-source census ends that occurrence; nothing publishes a provider or setup item to acknowledge. Per-repo recovery is not inferred from a workspace-level healthy row; unknown/malformed/partial/unreadable sources retain dismissals, including failures inspecting an unreadable source. Reconciliation does not rewrite unchanged bytes, keeps its read map on failed cleanup, and never removes a click newer than the observation. Retired stale-session JSON is invalid compaction input, not a supported kind. In-process ASGI routes assert failed dismissal persistence returns 503/dismissal-not-held, then successful clicks survive restart. Task-bound worktrees retain precomputed disabled-action reasons. These fixture assertions do not establish live host delivery.

## Evidence


- Equal findings remain dismissed across clock changes and a changed fingerprint recurs. [6]

- Severity leaves the ranking: the queue lists the newest entry first and breaks ties by id, and a drift entry that names no age counts as zero rather than sinking. [7]

### 20261023-L190-v2 Newest First Replaces Severity-First

The ranking case was renamed and its expectation reversed: `actionable-drift:repo:main` (no age, so zero) now
leads, `provider-down:z` (10s) follows, and the equal-age pair `a`/`b` (20s) keeps id order
(`test_observer_projection_attention.py:143-176`). The case still proves a stable total order; it no longer proves
a severity order, because the queue has none.

- Explicit recovery ends retained-kind occurrences and later failure returns. [8]


- Partial/broken input retains acknowledgement; complete gone facts reclaim. [9]


- Observation cutoff protects a later click. [10]


- Long histories retain current subjects and compact invalid retired/torn rows without repeat rewrite. [11]


- ASGI persistence failure is 503; accepted dismissals survive refresh and restart. [12]

- Precomputed task-worktree disablement remains authoritative. [13]

- The retained directory-read-failure case uses blocked-start and keeps its acknowledgement when native source listing fails; no current provider census or provider acknowledgement is asserted. [14]
