# mcp/tests/test_static.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_static.py`                 |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Serves controlled built-bundle and missing-bundle worlds. Entry HTML revalidates while assets retain their own cache policy; missing output returns 503 with the actual build command and no-store, while the API remains usable. A source checkout without a built bundle is an explicit supported state, not evidence of an installed UI.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Built bundle is served with revalidated html | `test_built_bundle_is_served_with_revalidated_html` | mcp/tests/test_static.py:50-59 |
| Missing bundle answers 503 with the build command | `test_missing_bundle_answers_503_with_the_build_command` | mcp/tests/test_static.py:61-68 |
| Missing bundle leaves the api alone | `test_missing_bundle_leaves_the_api_alone` | mcp/tests/test_static.py:70-72 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 4 citation rows to the static resolver, missing-bundle surface, app tests, and release sync; scoped citation fixing regenerated the source ranges.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: made the `test_serving.py` citation the previous
  entry flagged as approximate exact again. The app-level counterpart is `AppTests` L526-L558:
  `test_root_serves_dashboard_bundle` (a stand-in bundle patched over `dashboard_static_dir`, 200 +
  `cache-control: no-cache`) and `test_root_diagnoses_a_missing_bundle_instead_of_a_bare_404`
  (resolver patched to `None`, 503 + remedy text + `no-store`, with `/api/state` still 200) — both
  built through `create_app`, which is what the claim asserts. Read back verbatim. Note for
  accuracy: the skip described in Conventions belongs to `StaticTests` at L1549-L1559, a different
  class that only exercises `dashboard_static_dir()` directly; the two `create_app` cases above do
  not skip.

- 2026-07-31T16:35+02:00 — No content impact: the only change to `mcp/tests/test_static.py` since
  the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 4
  line(s), touching only magic trailing commas and redundant grouping parentheses. Checked by
  parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds. Noted while checking: the references table also cites line ranges inside
  `test_serving.py`; those ranges shifted because this task edited those files, so treat the cited
  numbers as approximate and the linked cards as authoritative.

- 2026-07-31T04:28+02:00 — Created for 260731-EFA-L1: deterministic coverage of the static surface
  after the cockpit bundle left version control — resolver `None` vs. directory, served-HTML
  revalidation without weakening hashed-asset caching, the 503 diagnostic (location, reason,
  remedy, `no-store`), no fabricated cockpit, an unaffected API, greedy deep-route coverage, and
  the method-parity regression against the real `StaticFiles` mount. Verification metadata pinned
  to the pre-leaf source authority until closeout stamps the code commit.
