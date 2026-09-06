# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00|
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../../../../../overview.md`               |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Metadata parsing, path mirroring, and `rel` come from `discovery`. | `parse_table_metadata`; `mirror_onboarding_path`; `rel` | mcp/src/agents_remember/kernel/coordination_context/paths.py:42-52; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py:17-32; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py:58-64 |
| Entity-catalog sidecars import `classify_entity_catalog` from `entities`. | "from agents_remember.memory_quality.integrity.onboarding_drift_check.entities import ( classify_entity_catalog" | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py:21-23 |
| For `repo-entity-catalog` sidecars, `classify_sidecar_onboarding_units` delegates to `classify_entity_catalog`. | "if doc_type == \"repo-entity-catalog\": return classify_entity_catalog" | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py:299-300 |
| Local staged/unstaged change notes come from `git_ops`. | `local_change_note`; `local_route_change_note` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py:22-38; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py:48-51 |
| The `cat-file -e` and `diff --quiet` calls run on the single kernel git runner. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:85-151 |

## Update History

- 2026-08-03T02:45:41+02:00 — W3-B01 curator: the correction delta split the entity-catalog finding into separate import and delegation claims, and the fixer generated the actual sidecar extents `21-23` and `299-300` rather than retaining a transient `1-1` pointer. The preserved discovery wording is semantically broader than the current split implementation because `mirror_onboarding_path` lives in coordination-context paths; that developer-owned Tier-3 wording mismatch remains inventoried rather than silently rewritten. Verification metadata remains unchanged for closeout.
- 2026-07-31T20:57+02:00 — 260731-EFA-L3 curator: `run_git` is now imported from
  `kernel.git_command` instead of `git_ops`, so the reference row "Source diff and change notes come
  from `git_ops`" was half false. Split the row, documented the two git calls each classifier makes
  and the return-code-to-verdict mapping, and added the no-local-runner invariant. Verdicts,
  ordering and notes are unchanged.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0911` armed with no
  exemptions): `classify_external_onboarding` was rewritten around a `row(...)` verdict closure
  plus an `_early_classification()` closure, collapsing six hand-repeated `DriftRow(...)`
  constructions into four-field verdicts. Same verdicts, same order. Verification metadata pinned
  until closeout stamps the L2 commit.
- 2026-05-31T12:50+02:00 — `classify_sidecar_onboarding_units` now gates non-sidecar storage via the boolean `is_sidecar_storage` predicate instead of the removed `sidecar_storage_label` helper (both imported from `coordination_context_resolver`); corrected the Invariants note to name `is_sidecar_storage` (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Extracted an `_early_classification` closure in `classify_overview_onboarding` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; the unused `classify_sidecar_onboarding` aggregator was dropped during the split. Metadata pending closeout refresh to the split commit.
