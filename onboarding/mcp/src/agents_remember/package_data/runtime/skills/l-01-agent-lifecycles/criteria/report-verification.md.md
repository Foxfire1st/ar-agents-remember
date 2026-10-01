# l-01-agent-lifecycles/criteria/report-verification.md

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

No relevant external documentation found.

## Evidence

### Repo-Internal References

- Canonical source this bundle copy is sync-propagated from. [1]
- The reviewer role that binds this catalog in every review type. [2]

### Cross-Repo References

No sibling repository evidence is needed for this catalog.

No meaningful cross-repo references found.

### 260821-DAGQC-L4 Untracked Candidate Evidence

RV-1's complete-tree claim now includes every nonignored untracked path, enumerated with a
NUL-delimited Git inventory or an equivalently path-safe API. Each exact path is inspected with
no-follow (`lstat`-equivalent) semantics: record type and numeric mode; bounded text bytes or a
binary/sensitive classification plus hash for regular files; link text without dereference for
symlinks; and an explicit disposition for directories or special objects. Every object is marked
intended or unintended. A disappearing or identity-changing path is reported as a race/limitation
and the view is re-established; it is never silently skipped. This remains semantic review work,
not a new verifier and not authority to dump unlimited or sensitive bytes.

## 260815-DAG-L15 Review-Doctrine

RV-1 is extended: the "tree contains only intended changes" claim is refuted against BOTH content
and mode rows — `git status --short` plus `git diff HEAD --numstat` for content, and `git diff
HEAD --summary` for mode-only changes (exec-bit drops on hooks/scripts are behaviorally meaningful
and silent to content diffs). The extension records the 260815-DAG-L12 catch (L12-F1): 10 files
carried mode-only changes (100755→100644, incl. `.githooks/pre-commit`) absent from the worker's
file list.
