# l-01-agent-lifecycles/criteria/report-verification.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/report-verification.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T17:35+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|

## Purpose

The report-verification criteria catalog — one of the five seed catalogs in the new `criteria/`
folder (leaf 260703-L12), and the one that is **standing from day one in every review type**:
report-vs-artifact caught real defects in three separate engagements before the catalog existed.
It binds for the adversarial reviewer AND for the loop owner verifying a builder round.

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/criteria/report-verification.md`. THREE standing criteria with
cited catching evidence: **RV-1 report-vs-artifact on EVERY claim** (open the artifact behind
each claim — three L8 catches: the round-3 hand-aligned test, the cycle-6 history-only
"refreshed" overviews, the review-4 owner's own canvas overclaim), **RV-2 CLASS-completeness**
(promoted to standing at 260703-L18 — catches: L10's six-of-ten first-action surfaces; L18R-3's
sibling LedgerError block still advertising an inert recovery choice after the named instance
was fixed), and **RV-4 decision-log completeness for scope-expanding disclosures** (promoted to
standing at 260703-L18 — catches: L17R-1's report-only owner supplement; L18R-4's report-only
environment finding). The **Candidate Criteria** section carries **RV-3
partial-fix-creates-falsehoods** (single catch: L10's two install-doc claims made false by the
partial hook flip) and **RV-5 worktree-shadowed regression pins** (single catch: L18R-1 — a
mutation-tested pin biting only under a hand-set `PYTHONPATH` because the editable install
shadows the worktree; pins must bite under the canonical invocation) — each promotes at ≥2
catching engagements. Plus the exploratory mandate (default 2 novel lenses) and the promotion
ratchet (RV-1 is the ratchet's own precedent — promoted on three catches).

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | `# Criteria Catalog — Report Verification`; `SkillTarget`; `TARGETS`; "mcp package data" | skills/l-01-agent-lifecycles/criteria/report-verification.md:1-99; scripts/sync-skills.py:26-29; scripts/sync-skills.py:43-56 |
| The reviewer role that binds this catalog in every review type. | `## Criteria Catalogs (the review test bench — bound here)`; `report-verification` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:56-75 |

## Cross-Repo References

No sibling repository evidence is needed for this catalog.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: anchored 2 table citations and added the exact canonical-to-package sync evidence; no unresolved Tier-3 claims.

- 2026-07-07T20:55+02:00 — agent-orchestration L18: body de-staled to the current catalog — RV-2 and RV-4 PROMOTED to standing at their second catches (L18R-3, L18R-4); candidates now RV-3 + RV-5 (worktree-shadowed regression pins, catch L18R-1). Covers both the 984a303 direct commit (RV-4 seeding, previously unreflected in this sidecar) and this leaf's promotions. Verification metadata pinned until closeout stamps the L18 commit.
- 2026-07-06T17:35+02:00 — 260703-L12 round 2 (L12R-2): RV-2 and RV-3 re-tiered STANDING → CANDIDATE (one catching engagement each, honestly marked; promote at ≥2 per the catalog's own ratchet); content unchanged. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `criteria/report-verification.md` seed catalog (leaf 260703-L12): RV-1 report-vs-artifact on every claim (three L8 catches incl. the owner's own), RV-2 CLASS-completeness (L10 six-surface catch), RV-3 partial-fix-creates-falsehoods (L10 install-docs), standing from day one in every review type. Verification metadata pinned until closeout stamps the L12 commit.
