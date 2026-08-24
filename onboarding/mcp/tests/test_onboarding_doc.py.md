# test_onboarding_doc.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_onboarding_doc.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |

## Purpose

Unit tests for the kernel onboarding-document body/history helpers in
`kernel/onboarding_doc.py`.

## Code Commentary

### Logic

A realistic sidecar literal drives the coverage: `meaningful_body` strips the
three verification metadata rows and the Update History section while keeping
non-metadata table rows and sections after the history; metadata-only and
history-only edits are not body changes while real edits and new documents
(`old_text=None`) are; `update_history_section` / `new_history_lines` extract
history lines and diff them against an old text; `has_no_impact_marker`
accepts `No content impact:` and `no route impact:` (case-insensitive, colon
required) and rejects unmarked entries; route helpers normalize root forms to
`.` and match route containment.

### Invariants And Boundaries

Standard-library `unittest` only; no git fixtures — the gate behavior using
these helpers against a real memory repo is covered in
`test_worktree_support.py`.

## Docs References

No external documentation is needed for this standard-library test.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Module under test. | `meaningful_body` | mcp/src/agents_remember/kernel/onboarding_doc.py:94-108 |
| Git-fixture gate coverage consuming the same helpers. | `RequireUpdatedSidecarContentTests` | mcp/tests/test_worktree_support_benchmark.py:668-823 |

## 260824-PDLS Cohort Extraction

The route-normalization root-form and quoting assertions moved unchanged to the bounded direct
cohort. The remaining onboarding document parsing/body/history/route-containment contracts stay in
this module.

## Update History

- 2026-08-24T20:55+02:00 — Moved two pure route-normalization assertions to the direct cohort.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 4 citation findings (2 rows); scoped recheck clean.

- 2026-06-10T04:47+02:00 — Created with the kernel helper extraction (issue #56 sub-task 1).
