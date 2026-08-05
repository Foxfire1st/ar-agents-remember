# dev-skills/README.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dev-skills/README.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-06-23T05:31 |
| lastVerifiedCommitHash | `8e39b62c3550e974486479203d191aac39a0f0f3`|
| lastVerifiedCommitDate | 2026-06-23T06:11:39+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview.md](overview.md)

## Purpose

Declares the contract for the `dev-skills/` tree: developer-only Claude Code skills that are **not
distributed** to AR users, are installed by hand, and live outside the `sync-skills.py` distribution
path while still being in the onboarding include scope.

## Code Commentary

### Logic

Three parts: (1) the non-distribution statement — `sync-skills.py` copies only canonical `skills/`, so
nothing here is synced, shipped, or `--check`-gated, and it carries no... it now *does* carry onboarding
sidecars (in scope) but is still not distributed; (2) the rationale — internal build tooling that would
only bloat harness installs; (3) the hand-install recipe — copy the folder into a harness skills dir
and restart.

### Conventions

Prose-only convention doc. Lists current dev-skills at the bottom so the tree is self-describing.

### Invariants And Boundaries

- The distribution boundary and the onboarding-scope boundary are independent: included for onboarding,
  excluded from distribution.
- Do not register a `dev-skills/` entry with `sync-skills.py` or move it into `skills/` unless it should
  ship to users.

### Todos

No open file-local todos.

## Docs References

No relevant documentation found.

## Repo-Internal References

The non-distribution guarantee is structural: the sync helper only copies the canonical `skills/` tree.

| Finding | Anchor | Source |
| --- | --- | --- |
| `sync-skills.py` copies only `REPO_ROOT/"skills"` into its fixed targets; `dev-skills/` is never a target. | `CANONICAL_SKILLS` | scripts/sync-skills.py:15-15 |

## Cross-Repo References

No relevant cross-repo evidence found.

## Update History

- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 1 repository-reference citation (1/1 anchored and sourced; scoped citation check clean).

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-06-23T05:31 — Created with the `dev-skills/` slice (issue #92).
