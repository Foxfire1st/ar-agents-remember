# dev-skills/README.md

## Governing Overview

[overview](overview.md)

## Purpose

Declares the contract for the `dev-skills/` tree: developer-only Claude Code skills that are **not
distributed** to AR users, are installed by hand, and live outside the `sync-skills.py` distribution
path.

## Code Commentary

### Logic

Three parts: (1) the non-distribution statement — `sync-skills.py` copies only canonical `skills/`, so
nothing here is synced, shipped, or `--check`-gated; the README also says the tree is outside the
memory include scope and therefore carries no onboarding sidecars, although onboarding cards for it exist; (2) the rationale — internal build tooling that would
only bloat harness installs; (3) the hand-install recipe — copy the folder into a harness skills dir
and restart.

### Conventions

Prose-only convention doc. Lists current dev-skills at the bottom so the tree is self-describing.

### Invariants And Boundaries

- The distribution boundary and the onboarding-scope boundary are independent: `dev-skills/**` is not
  among the memory include paths, yet existing cards cover it; it is excluded from distribution either way.
- Do not register a `dev-skills/` entry with `sync-skills.py` or move it into `skills/` unless it should
  ship to users.

### Todos

No open file-local todos.

## Evidence

### Docs References

No relevant documentation found.

### Repo-Internal References

The non-distribution guarantee is structural: the sync helper only copies the canonical `skills/` tree.

- `sync-skills.py` copies only `REPO_ROOT/"skills"` into its fixed targets; `dev-skills/` is never a target. [1]

### Cross-Repo References

No relevant cross-repo evidence found.
