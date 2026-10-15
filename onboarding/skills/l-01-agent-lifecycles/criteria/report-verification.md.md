# skills/l-01-agent-lifecycles/criteria/report-verification.md

## Governing Overview

[Role-lifecycle overview](../overview.md)

## Purpose

Canonical report-verification catalog for an assigned adversarial review and for the loop owner verifying a builder round. It checks reports, owner claims and handover summaries against artifacts. Report verification is standing across the review types in the reviewer binding table; the catalog itself does not make review a routine closeout or integration prerequisite.

## Code Commentary

### Logic And Boundaries

The standing criteria are RV-1, RV-2, RV-4 and RV-5; RV-3 remains a candidate. RV-1 opens the artifact behind each claim and forbids sampling the load-bearing ones. A complete-tree claim checks content and mode rows in the same filesystem view, including executable-bit changes that content-only diffs miss.

The same complete-tree claim covers every nonignored untracked path using NUL-delimited or equivalently path-safe enumeration. Inspection is no-follow: record type, numeric mode, executable significance and intention; regular files get size and bounded escaped text or a binary/sensitive classification with hash; symlinks get link text without dereference; directories and special objects need an explicit disposition. Races or inaccessible objects are disclosed and a consistent view is re-established, never silently skipped. This is semantic evidence work, not another verifier or authority to dump sensitive bytes.

RV-2 enumerates the whole sibling class behind an instance-level finding. RV-4 preserves scope-expanding owner supplements and load-bearing builder disclosures in the task decision log, not only a report. RV-5 proves the exact invocation's resolved source/import path and task/contract are the reviewed artifacts; a green result from a different editable install or a command refused before output is not evidence for the change set.

RV-3 asks whether a partial fix made claims about the changed artifacts false elsewhere. Its exploratory status is separate from the standing list. Baseline review adds the brief's novel lenses (default two) and may propose promotions; fix-verification is confined to sealed outstanding IDs with no new-lens or catalog duty. Promotion requires the stated separate first-review catches and loop-owner acceptance. The catalog's historical catching counts and environment examples are not fresh executions or automatic lifecycle prerequisites.

### Retained Source-Epoch Commentary

The quotations below preserve the earlier packaged card’s account. They are historical commentary, not fresh execution, acceptance, source census, installation evidence or an additional present procedure. The canonical description and source-bound qualifications above distinguish retained intent from changed or retired claims.

> The report-verification criteria catalog — one of the five seed catalogs in the new `criteria/`
> folder (leaf 260703-L12), and the one that is **standing from day one in every review type**:
> report-vs-artifact caught real defects in three separate engagements before the catalog existed.
> It binds for the adversarial reviewer AND for the loop owner verifying a builder round.

> Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
> `skills/l-01-agent-lifecycles/criteria/report-verification.md`. The standing catalog carries
> **RV-1 report-vs-artifact on EVERY claim** (open the artifact behind
> each claim — three L8 catches: the round-3 hand-aligned test, the cycle-6 history-only
> "refreshed" overviews, the review-4 owner's own canvas overclaim), **RV-2 CLASS-completeness**
> (promoted to standing at 260703-L18 — catches: L10's six-of-ten first-action surfaces; L18R-3's
> sibling LedgerError block still advertising an inert recovery choice after the named instance
> was fixed), and **RV-4 decision-log completeness for scope-expanding disclosures** (promoted to
> standing at 260703-L18 — catches: L17R-1's report-only owner supplement; L18R-4's report-only
> environment finding), plus **RV-5 canonical invocation target provenance**. The **Candidate
> Criteria** section carries **RV-3
> partial-fix-creates-falsehoods** (single catch: L10's two install-doc claims made false by the
> partial hook flip). Plus the exploratory mandate (default 2 novel lenses) and the promotion
> ratchet.

> Catalog files live beside the templates under `criteria/` and are bound per review type by
> `roles/reviewer.md` (the binding table); this one binds in EVERY review type, including the plan
> review.

> When a report-verification review is explicitly requested, the standing list runs with no sampling
> of "load-bearing" claims — every claim. The catalog does not create a routine closeout or integration
> gate; amendments land only through the promotion ratchet on the loop owner's acceptance.

> No TODO is recorded for this catalog.

> This criteria catalog supplies evidence only when the corresponding review is explicitly requested. It does not create a closeout or integration prerequisite; routine handoff uses the worker's targeted-check record together with the curator's complete memory-quality result and preserves any failed or not-run state.

> No external domain documentation applies to this repository-local catalog.

> No relevant external documentation found.

> No sibling repository evidence is needed for this catalog.

> No meaningful cross-repo references found.

> RV-1's complete-tree claim now includes every nonignored untracked path, enumerated with a
> NUL-delimited Git inventory or an equivalently path-safe API. Each exact path is inspected with
> no-follow (`lstat`-equivalent) semantics: record type and numeric mode; bounded text bytes or a
> binary/sensitive classification plus hash for regular files; link text without dereference for
> symlinks; and an explicit disposition for directories or special objects. Every object is marked
> intended or unintended. A disappearing or identity-changing path is reported as a race/limitation
> and the view is re-established; it is never silently skipped. This remains semantic review work,
> not a new verifier and not authority to dump unlimited or sensitive bytes.

> RV-1 is extended: the "tree contains only intended changes" claim is refuted against BOTH content
> and mode rows — `git status --short` plus `git diff HEAD --numstat` for content, and `git diff
> HEAD --summary` for mode-only changes (exec-bit drops on hooks/scripts are behaviorally meaningful
> and silent to content diffs). The extension records the 260815-DAG-L12 catch (L12-F1): 10 files
> carried mode-only changes (100755→100644, incl. `.githooks/pre-commit`) absent from the worker's
> file list.

## Evidence

The rows cite canonical source text and narrowly relevant neighbor definitions. A historical example or declared check remains distinct from a check result. The packaged source is a propagation twin, not an independent authority.

- The canonical catalog owns report-verification doctrine rather than the generated bundle. [1]
- The generator retains a target record type; this declaration is not a fresh synchronization check. [2]
- The current generator derives skill targets from the checkout declaration rather than an old TARGETS constant. [3]
- The reviewer binding table includes report-verification in every listed review type. [4]
- RV-1 requires artifacts behind claims and checks both content and mode in the same filesystem view. [5]
- RV-1 adds path-safe untracked enumeration, no-follow inspection, bounded content and explicit race/intent handling. [6]
- RV-2 enumerates sibling classes; RV-4 records load-bearing disclosures in the decision log. [7]
- RV-5 proves the resolved invocation source and contract rather than trusting nominally canonical commands. [8]
- RV-3 remains a candidate; baseline exploration and promotion do not expand sealed fix-verification. [9]
