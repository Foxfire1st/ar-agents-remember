# l-01-agent-lifecycles/criteria/onboarding-memory.md

## Purpose

The onboarding/memory review criteria catalog — one of the five seed catalogs in the new
`criteria/` folder (leaf 260703-L12). Binds over the memory side of every change set: sidecars,
route overviews, route indexes, update histories (the onboarding-vs-code lens at both seams).

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/criteria/onboarding-memory.md`.

**OM-1** compares onboarding with the as-landed source. Its retained catching examples
include deleted canvas models, duplicated route-overview rows and a stale model census.
**OM-2** is the requirement-bound independent second reader on converted memory, not the
former Update History/body-only detector: a seat that authored none of the leaf's cards
or records checks every changed card, sidecar and record statement against final code,
every history row's disposition, effect and reason against the diff, and important omissions.
Blocking findings are repaired before closeout. The lifecycle requires this check; closeout
itself does not mechanically enforce it. A counted card edit alone cannot close a trace.
OM-2 entered by the requirement, not the promotion ratchet, and only a developer ruling
can demote it.

**OM-3** remains the candidate criterion for newest-first Update History under the
checker's naive/UTC comparison semantics. Its historical ordering examples do not require
Update History on converted cards. Baseline review retains the exploratory mandate and
promotion ratchet; fix-verification retains the sealed outstanding scope.

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

On converted memory the independent OM-2 second-reader check is required by the lifecycle
before closeout, whether or not a separate review was otherwise requested. It does not
create a check mechanically performed by closeout or integration. The other criteria
run within the admitted review scope; ordinary promotions use the ratchet, while the
requirement-bound OM-2 and OM-4 criteria are demoted only by a developer ruling.

### Todos

No TODO is recorded for this catalog.


## CCR-R12@v5 Review Scope

Converted-memory OM-2 supplies a required independent fact-check before closeout;
only the other catalog criteria remain conditional on the corresponding requested review.
OM-2 is a lifecycle prerequisite, not a check mechanically enforced by closeout or
integration. Routine handoff still carries the worker's targeted-check record, the
Curator's complete memory-quality result, and every failed, blocked or not-run state.

### Docs References

No external domain documentation applies to this repository-local catalog.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The synchronized criteria source requires the independent converted-memory OM-2 check, binds its scope, and preserves the other review criteria's admission rules. [1]
- OM-4, the requirement-bound standing criterion for plausible admission justifications. [2]
- The reviewer role that binds this catalog per review type. [3]
- The Update History order checker whose naive/UTC comparison semantics OM-3 pins. [4]

### Cross-Repo References

No sibling repository evidence is needed for this catalog.

No meaningful cross-repo references found.

## CCR-L42 current candidate

The onboarding-memory criteria now apply exploratory and new-catalog duties only to a baseline review. Fix-verification uses the sealed outstanding IDs and cannot recensus the catalog or add findings.
