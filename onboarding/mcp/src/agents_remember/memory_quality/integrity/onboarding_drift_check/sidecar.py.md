# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`sidecar.py` classifies file-level sidecar onboarding and repo/route overview
onboarding against the current source tree, routing entity-catalog sidecars to
`entities.py`.

## Code Commentary

### Logic

`classify_external_onboarding` compares a source file against its recorded
`lastVerifiedCommitHash` (handling missing source, missing commit, clean, and
drifted cases). Since 260731-EFA-L2 it builds its six verdicts through a local `row(*,
classification, trust, affected_sections, note)` closure that fixes the identity and verification
stamp (`onboarding_file`, `source_file`, `repository`, `storage_mode="external"`,
`last_verified_hash`, `last_verified_date`) once, so the four varying fields are the only thing a
verdict states — the same shape `classify_overview_onboarding` already used. A local
`_early_classification()` closure returns the missing-metadata, orphaned-source and
commit-not-in-history verdicts before the diff runs; `None` means proceed to the diff. Every
classification, trust level, affected-sections string and note is unchanged.
`classify_overview_onboarding` does the same for repo/route
overviews by `sourceRoute`; `classify_external_source` maps a source to its
mirrored sidecar; `classify_sidecar_onboarding_units` dispatches by `doc_type`
(overview / entity-catalog / file-level) and storage mode.

Both classifiers reach git twice: `run_git(repo_root, ["cat-file", "-e", f"{last_hash}^{{commit}}"])`
inside `_early_classification`, and then `run_git(repo_root, ["diff", "--quiet", last_hash, "HEAD",
"--", source_file])` (`source_route` for overviews), whose return code is the verdict — `0` is up to
date, `1` is drifted, and anything else is drifted with the git error in the note. Since
260731-EFA-L3 `run_git` is imported from `agents_remember.kernel.git_command`, not from the sibling
`git_ops`, which no longer defines it; `local_change_note` and `local_route_change_note` still come
from `git_ops`.

The early verdicts are intentionally distinct: missing source-path or verification metadata is
`missing verification` with medium trust; a deleted source is `orphaned` with low trust; an
unavailable recorded commit is `drifted` with medium trust and a Git-history explanation. Every row
retains its classification, trust, affected sections, and specific note so the next repair can
distinguish absent metadata from deleted source and unavailable history.

cit:([`classify_external_onboarding`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py:33-112)

### Invariants And Boundaries

- Reports drift only; it must not rewrite onboarding.
- `disabled` (path-rule excluded) and non-sidecar storage modes are reported
  explicitly rather than treated as drift; the sidecar test uses the boolean
  `is_sidecar_storage` predicate from `coordination_context_resolver`.
- Entity-catalog classification is delegated to `entities.classify_entity_catalog`.
- No local git runner: the commit-existence and source-diff calls are `kernel.git_command.run_git`.
  Its `env=git_environment()` guard is what keeps these verdicts about the caller's repository — an
  inherited `GIT_DIR` would resolve `lastVerifiedCommitHash` in a different repository, where
  `cat-file -e` fails, and every sidecar would be reported "drifted: recorded verification commit is
  not available in git history".

## Evidence

### Repo-Internal References

- Metadata parsing, path mirroring, and `rel` come from `discovery`. [1]
- Entity-catalog sidecars import `classify_entity_catalog` from `entities`. [2]
- For `repo-entity-catalog` sidecars, `classify_sidecar_onboarding_units` delegates to `classify_entity_catalog`. [3]
- Local staged/unstaged change notes come from `git_ops`. [4]
- The `cat-file -e` and `diff --quiet` calls run on the single kernel git runner. [5]
