# l-01-agent-lifecycles/criteria/report-verification.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/report-verification.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-24T13:51:26+02:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The report-verification criteria catalog — one of the five seed catalogs in the new `criteria/`
folder (leaf 260703-L12), and the one that is **standing from day one in every review type**:
report-vs-artifact caught real defects in three separate engagements before the catalog existed.
It binds for the adversarial reviewer AND for the loop owner verifying a builder round.

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/criteria/report-verification.md`. The standing catalog carries
**RV-1 report-vs-artifact on EVERY claim** (open the artifact behind
each claim — three L8 catches: the round-3 hand-aligned test, the cycle-6 history-only
"refreshed" overviews, the review-4 owner's own canvas overclaim), **RV-2 CLASS-completeness**
(promoted to standing at 260703-L18 — catches: L10's six-of-ten first-action surfaces; L18R-3's
sibling LedgerError block still advertising an inert recovery choice after the named instance
was fixed), and **RV-4 decision-log completeness for scope-expanding disclosures** (promoted to
standing at 260703-L18 — catches: L17R-1's report-only owner supplement; L18R-4's report-only
environment finding), plus **RV-5 canonical invocation target provenance**. The **Candidate
Criteria** section carries **RV-3
partial-fix-creates-falsehoods** (single catch: L10's two install-doc claims made false by the
partial hook flip). Plus the exploratory mandate (default 2 novel lenses) and the promotion
ratchet.

### Conventions

Catalog files live beside the templates under `criteria/` and are bound per review type by
`roles/reviewer.md` (the binding table); this one binds in EVERY review type, including the plan
review.

### Invariants And Boundaries

When a report-verification review is explicitly requested, the standing list runs with no sampling
of "load-bearing" claims — every claim. The catalog does not create a routine closeout or integration
gate; amendments land only through the promotion ratchet on the loop owner's acceptance.

### Todos

No TODO is recorded for this catalog.


## CCR-R12@v5 Review Scope

This criteria catalog supplies evidence only when the corresponding review is explicitly requested. It does not create a closeout or integration prerequisite; routine handoff uses the worker's targeted-check record together with the curator's complete memory-quality result and preserves any failed or not-run state.

### Docs References

No external domain documentation applies to this repository-local catalog.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | `# Criteria Catalog — Report Verification`; `SkillTarget`; `TARGETS`; "mcp package data" | skills/l-01-agent-lifecycles/criteria/report-verification.md:1-130; scripts/sync-skills.py:26-29; scripts/sync-skills.py:43-56 |
| The reviewer role that binds this catalog in every review type. | `# Reviewer`; `report-verification` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:6-6; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:35-42 |

## Cross-Repo References

No sibling repository evidence is needed for this catalog.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260815-DAG-L15 Review-Doctrine

RV-1 is extended: the "tree contains only intended changes" claim is refuted against BOTH content
and mode rows — `git status --short` plus `git diff HEAD --numstat` for content, and `git diff
HEAD --summary` for mode-only changes (exec-bit drops on hooks/scripts are behaviorally meaningful
and silent to content diffs). The extension records the 260815-DAG-L12 catch (L12-F1): 10 files
carried mode-only changes (100755→100644, incl. `.githooks/pre-commit`) absent from the worker's
file list.

## 260821-DAGQC-L4 Untracked Candidate Evidence

RV-1's complete-tree claim now includes every nonignored untracked path, enumerated with a
NUL-delimited Git inventory or an equivalently path-safe API. Each exact path is inspected with
no-follow (`lstat`-equivalent) semantics: record type and numeric mode; bounded text bytes or a
binary/sensitive classification plus hash for regular files; link text without dereference for
symlinks; and an explicit disposition for directories or special objects. Every object is marked
intended or unintended. A disappearing or identity-changing path is reported as a race/limitation
and the view is re-established; it is never silently skipped. This remains semantic review work,
not a new verifier and not authority to dump unlimited or sensitive bytes.

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: **complete curation inverts the doctrine this card recorded.** CAPS-R18@v1 removes the optional/narrow-curation sentences from the shipped instruction corpus and states the rule normatively — the full `memory_quality_check` operation runs as part of every leaf's curation at its contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every curator-actionable finding is repaired or escalated as blocked with its exact returned code, and closeout and integration **carry** the completed curation as a prerequisite while invoking nothing. SOURCE UNCHANGED BY THIS LEAF; card prose falsified by CAPS-R18@v1. Updated the catalog-evidence sentence so routine handoff reads the worker's targeted-check record together with the curator's complete memory-quality result.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `## Criteria Catalogs (the review test bench — bound here)` repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:106-128. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: added NUL-safe, no-follow untracked candidate
  evidence covering type, mode, bounded content, disposition, and race limitations. Canonical and
  generated copies are synchronized; Dagger acceptance remains closeout-owned and pending.

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: RV-1 extended — "the tree contains only intended
  changes" is also refuted against `git diff HEAD --summary` mode rows (mode-only changes; the
  L12-F1 catch). Verified at code commit de3a0fd9.

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: anchored 2 table citations and added the exact canonical-to-package sync evidence; no unresolved Tier-3 claims.

- 2026-07-07T20:55+02:00 — agent-orchestration L18: body de-staled to the current catalog — RV-2 and RV-4 PROMOTED to standing at their second catches (L18R-3, L18R-4); candidates now RV-3 + RV-5 (worktree-shadowed regression pins, catch L18R-1). Covers both the 984a303 direct commit (RV-4 seeding, previously unreflected in this sidecar) and this leaf's promotions. Verification metadata pinned until closeout stamps the L18 commit.
- 2026-07-06T17:35+02:00 — 260703-L12 round 2 (L12R-2): RV-2 and RV-3 re-tiered STANDING → CANDIDATE (one catching engagement each, honestly marked; promote at ≥2 per the catalog's own ratchet); content unchanged. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `criteria/report-verification.md` seed catalog (leaf 260703-L12): RV-1 report-vs-artifact on every claim (three L8 catches incl. the owner's own), RV-2 CLASS-completeness (L10 six-surface catch), RV-3 partial-fix-creates-falsehoods (L10 install-docs), standing from day one in every review type. Verification metadata pinned until closeout stamps the L12 commit.
