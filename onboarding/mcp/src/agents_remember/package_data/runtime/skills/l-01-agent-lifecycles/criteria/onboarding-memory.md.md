# l-01-agent-lifecycles/criteria/onboarding-memory.md

## Purpose

The onboarding/memory review criteria catalog — one of the five seed catalogs in the new
`criteria/` folder (leaf 260703-L12). Binds over the memory side of every change set: sidecars,
route overviews, route indexes, update histories (the onboarding-vs-code lens at both seams).

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/criteria/onboarding-memory.md`. Two standing criteria with cited
catching evidence: **OM-1 staleness diff vs as-landed code** — as of round 2 (L12R-1) cited to the
verifiable record: two engagements — L8 cycle 6's OWNER follow-up pass (deleted canvas models in
the panels overview's build-job/frame tail; duplicated Layout-table rows in the tools and
controlplane overviews; all durably recorded in those overviews' own 2026-07-05T19:25 Update
History entries) and L10's flowModels-sidecar de-stale (its 2026-07-06T12:05 history entry +
L10R-3) — and **OM-2 history-only-update detection** ("refreshed" must mean a genuine body edit —
the L8 cycle-6 closeout-body-gate catch of overviews claimed refreshed but history-only). A
**Candidate Criteria** section (round 2, L12R-2) carries **OM-3 newest-first with the checker's
own semantics** at candidate tier (single catching engagement: L11's four parallel-wave history
collisions re-sorted with the checker's parse — naive as-is, tz-aware folds to UTC; promotes at
≥2). Plus the exploratory mandate (default 2 novel lenses) and the promotion ratchet, which notes
that the closeout body gate IS this catalog's OM-2 mechanized — the working example of a criterion
graduating into a gate.

**OM-4, admission justifications are plausible** (leaf 260928-MIK-L27, MIK-R27 rule 5, developer
ruling D14) is a third standing criterion. It entered **by requirement, not by the promotion
ratchet** (ruling 22:11:24 Q3), is marked so in its heading, and is demoted only by a developer
ruling. The validator checks only presence, shape, a justification made only of task, leaf,
requirement or ruling references, commit hashes and provenance words, and the two checkable criteria
(`spans_locations`, `guarded_by_test`); the reviewer judges the rest: a `prevents_costly_mistake`
naming no plausible, costly error, a `family_guarantee` the guarantee does not need, a
`joint_guarantee` one member already promises alone, a `real_alternatives` whose rejected option was
never serious, and a record that restates one leaf's acceptance criteria or that a code change alone
motivates. OM-4 binds converted memory only (the text format, MIK-R21), so it asks nothing of reviews
of today's unconverted memory. Its body was rewrapped to 100 columns (ruling 23:04:57 F5); the heading
cannot wrap.

### Conventions

Catalog files live beside the templates under `criteria/` and are bound per review type by
`roles/reviewer.md` (the binding table).

### Invariants And Boundaries

When an onboarding/memory review is explicitly requested, the standing list runs and reports each
criterion; the catalog does not create a routine closeout or integration gate. Amendments land only
through the promotion ratchet on the loop owner's acceptance.

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
- OM-4, the requirement-bound standing criterion for plausible admission justifications. [2]
- The reviewer role that binds this catalog per review type. [3]
- The Update History order checker whose naive/UTC comparison semantics OM-3 pins. [4]

### Cross-Repo References

No sibling repository evidence is needed for this catalog.

No meaningful cross-repo references found.

## CCR-L42 current candidate

The onboarding-memory criteria now apply exploratory and new-catalog duties only to a baseline review. Fix-verification uses the sealed outstanding IDs and cannot recensus the catalog or add findings.
