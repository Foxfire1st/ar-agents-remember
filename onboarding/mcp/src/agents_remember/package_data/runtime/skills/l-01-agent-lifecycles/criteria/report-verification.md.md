# l-01-agent-lifecycles/criteria/report-verification.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/report-verification.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T17:35+02:00 |
| lastVerifiedCommitHash | `bcaa78070f77c76f1c4db0af93786bb193b92523` |
| lastVerifiedCommitDate | 2026-07-06T07:51:05+02:00|

## Purpose

The report-verification criteria catalog — one of the five seed catalogs in the new `criteria/`
folder (leaf 260703-L12), and the one that is **standing from day one in every review type**:
report-vs-artifact caught real defects in three separate engagements before the catalog existed.
It binds for the adversarial reviewer AND for the loop owner verifying a builder round.

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/criteria/report-verification.md`. One standing criterion with cited
catching evidence: **RV-1 report-vs-artifact on EVERY claim** (open the artifact behind each
claim — three L8 catches: the round-3 hand-aligned test, the cycle-6 history-only "refreshed"
overviews, the review-4 owner's own canvas overclaim; builder reports and owner claims fail the
same way). A **Candidate Criteria** section (round 2, L12R-2) carries **RV-2 CLASS-completeness**
(single catch: L10's six-of-ten first-action surfaces) and **RV-3 partial-fix-creates-falsehoods**
(single catch: L10's two install-doc claims made false by the partial hook flip) at candidate
tier — each promotes at ≥2 catching engagements. Plus the exploratory mandate (default 2 novel
lenses) and the promotion ratchet (RV-1 is the ratchet's own precedent — promoted on three
catches).

### Conventions

Catalog files live beside the templates under `criteria/` and are bound per review type by
`roles/reviewer.md` (the binding table); this one binds in EVERY review type, including the plan
review.

### Invariants And Boundaries

The standing list MUST run every time; no sampling of "load-bearing" claims — every claim.
Amendments land only through the promotion ratchet on the loop owner's acceptance.

### Todos

No TODO is recorded for this catalog.

### Docs References

No external domain documentation applies to this repository-local catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [report-verification.md](agents-remember/skills/l-01-agent-lifecycles/criteria/report-verification.md) |
| The reviewer role that binds this catalog in every review type. | n/a | [reviewer.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md) |

## Cross-Repo References

No sibling repository evidence is needed for this catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-06T17:35+02:00 — 260703-L12 round 2 (L12R-2): RV-2 and RV-3 re-tiered STANDING → CANDIDATE (one catching engagement each, honestly marked; promote at ≥2 per the catalog's own ratchet); content unchanged. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `criteria/report-verification.md` seed catalog (leaf 260703-L12): RV-1 report-vs-artifact on every claim (three L8 catches incl. the owner's own), RV-2 CLASS-completeness (L10 six-surface catch), RV-3 partial-fix-creates-falsehoods (L10 install-docs), standing from day one in every review type. Verification metadata pinned until closeout stamps the L12 commit.
