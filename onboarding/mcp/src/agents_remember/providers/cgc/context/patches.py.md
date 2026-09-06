# mcp/src/agents_remember/providers/cgc/context/patches.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/context/patches.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-03T01:55+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`cgc/patches.py` owns marker-based CodeGraphContext patch application helpers
used to keep the Docker runner image patched consistently. L12 adds the watcher
timer-pop patch: fired debounce timers pop their own `self.timers` entry (identity
guarded against replacement-timer races) so the per-path dict stays bounded.

## Code Commentary

### Logic

It applies idempotent patches for `.cgcignore` handling, Windows delete-prefix
cleanup, C++/TableGen discovery, and visualizer routing/query behavior. The
module no longer discovers installed CGC modules from host venv layouts; the
managed patch application path belongs to the Docker runner image build.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Patch helpers operate on explicit files supplied by the Docker runner build
  or unit tests. They must not search a coordination-root host venv.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The marker-based timer cleanup patch is owned here; no removed patch-helper test coverage is asserted. | `apply_cgc_timer_pop_patch` | mcp/src/agents_remember/providers/cgc/context/patches.py:44-65 |

## Update History

- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 1 citation row with exact anchors and current source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-07-03T01:55+02:00 — L12 adds cgc_timer_pop_patch_applied/apply_cgc_timer_pop_patch for core/watcher.py, mirroring the cgcignore patch pattern (marker check, exact-snippet replace, idempotent).
- 2026-06-10T07:30+02:00 — No content impact: import path updated to `providers/context_common.py` (shared helpers moved out of the facade package, GitHub #58); documented behavior unchanged.
- 2026-05-28T13:40+02:00: Updated after host-venv module discovery helpers were removed; patch helpers now describe explicit-file Docker runner patch use only.
- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
