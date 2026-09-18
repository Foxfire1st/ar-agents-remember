# mcp/src/agents_remember/memory/migration/cutover.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/migration/cutover.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `2dcacb27446ecbaba01b69ee32e2ac40a1713b09`|
| lastVerifiedCommitDate |  2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The cutover's three artifacts as data, and the escalation they stay behind: the six criteria that
must hold before the live authority may change, the seven-step plan with its rollback story, archival
step and point of no return, and the one proposal that goes to the owner for a decision. **Nothing in
this module executes anything.** `KS-R21@v1` §8.1 requires the leaf to produce the three artifacts and
execute none of them, and §8.4 requires that nothing here be a gate — so the module has no trigger, no
flag, no scheduled activation and no code path that changes which memory is live, and there is no
function in it that writes anything. Reading the artifacts is the whole operation. The escalation is
likewise a record rather than an approval: the proposal carries the exact quoted boundary
`design/storage-design.md:465` and the item `starts migration/cutover`, and its decision state is
`absent`, which is the state.

## Code Commentary

### Logic

**The absence of activation is the design, not an omission.** The module docstring states the two
properties a reviewer should check — that the criteria are not softened to be met, and that the
escalation is a recorded proposal awaiting a recorded decision — and then states the mechanism that
keeps the first true: §8.4 makes "nothing here is a gate" a requirement, and "the way to keep that true
is for the module to have no side effect at all". Every other module in `memory/migration/` imports
something; this one imports only `Callable`, `Mapping`, `Sequence`, `dataclass` and `Literal` from the
standard library, so it cannot reach the corpus, a store or an operation even by accident.

**Six criteria, each with the evidence that would show it.** `CUTOVER_CRITERIA` is one module-level
tuple of six `CutoverCriterion` values, each carrying an identifier, a statement and an `evidence`
field that names the observable artifact or measurement which would show the condition holds —
"because a criterion whose evidence is not named is a criterion nobody can check". The six cover
distinct ground rather than restating one another: inventory completeness including the surfaces with
no onboarding (`CRIT-1`), a parse outcome and a migration disposition for every artifact (`CRIT-2`),
reference resolution (`CRIT-3`), assessment completion as `(T + F + U) / N` with a non-zero `P` as
the exact shortfall (`CRIT-4`), an independently reviewed reference inventory whose `K` was not
derived from the corpus being measured (`CRIT-5`), and the negative proof that no path revives legacy
prose as authority (`CRIT-6`).

**Seven ordered steps, and reversibility declared per step.** `CUTOVER_PLAN` is a `CutoverPlan` whose
`steps` tuple holds seven `CutoverStep` values, each carrying its own `order`, `action`, `reversible`
flag and `note`. Steps 1 to 4 are the preparation and are `reversible=True`; steps 5, 6 and 7 — archive
the corpus, switch the live authority, verify that nothing falls back — are declared
`reversible=False`. The plan therefore answers "can we go back?" with a number rather than a hope:
`point_of_no_return=5` names the step index after which the rollback no longer restores the previous
authority, and the `rollback_story` explains why — steps 1 to 4 publish no authority change and are
reversible "by doing nothing", while recovering an archived corpus is a second, separately approved
cutover in the other direction rather than a rollback, so the rollback must be decided before step 5
and recorded with the decision. The archival step is requirement 7.3's, and it is stated with the
property that makes it sufficient rather than merely present: archived material is preserved,
referencable by an exact identity, **not** on any reader's resolution path, and never an implicit
fallback — "an implicit fallback to archived prose is a second live authority wearing a different
name". The archival mechanics are named as the owner's to decide, and the plan states the property
they must satisfy rather than inventing a location.

**`evaluate_criteria` re-orders and checks completeness; it does not evaluate.** Its docstring is
explicit that it is "a pure re-ordering and completeness check, not an evaluator: the outcomes are the
caller's". It builds a mapping from the observations it was given, computes the declared criteria that
mapping omits, raises `ValueError` naming those identifiers when any are missing, and otherwise returns
one observation per `CUTOVER_CRITERIA` entry in declared order. The refusal is the point: "an
evaluation that silently skipped one would read as a satisfied criterion set", so a result omitting
`CRIT-5` cannot pass as a complete evaluation. Observations beyond the declared six raise nothing —
they are simply not returned.

**The verdict is derived, so it cannot contradict its own measures.** `criteria_verdict` reads the
observations rather than accepting a verdict as an argument: with no unmet observation it returns
`"cutover is justified by the recorded criteria"`, and otherwise it renders
`"cutover is not yet justified: ..."` followed by each unmet criterion's identifier and its observed
value, joined by `"; "`. That is §8.3's conforming output — "cutover is not yet justified" is a
supported result, not a failure — and the derivation is what stops a caller from "report[ing] a
satisfied cutover while carrying an unmet criterion".

**One measure and one predicate are computed together, and an invented criterion is refused.**
`measure_criterion` looks the criterion up in `CUTOVER_CRITERIA` and raises `ValueError` when the
identifier is not declared there — "a criterion invented at evaluation time would not be a condition
anybody reviewed" — then returns a `CriterionObservation` whose `met` is the result of calling the
supplied `holds` predicate once, at that point, and whose `observed` is the caller's measure string.
The `statement` and `required` fields are both filled from the declared criterion, so an observation
cannot carry a statement that disagrees with the condition it is reporting on. The predicate is called
exactly once, so the caller cannot report a met criterion whose own measure says otherwise.

**The escalation is data, quoted verbatim.** `ESCALATION_BOUNDARY` holds the string
`"design/storage-design.md:465"` and `ESCALATION_ITEM` holds `"starts migration/cutover"` as
module-level constants, "stored as data rather than as a comment so the proposal a reader holds names
the same sentence the decision is reserved by"; `CUTOVER_PROPOSAL` copies both into its
`boundary_reference` and `boundary_item` fields and sets
`proposal_id="cutover-proposal/legacy-onboarding-to-substrate"`. Its summary states the change of live
authority it proposes and adds that "the proposal is recorded here and is not acted on by this leaf".

**An approval is not representable.** `ProposalDecision` is
`Literal["absent", "owner-recorded"]` — there is no third state and no value on that vocabulary means
"approved", because an approval is a recorded decision owned elsewhere and this leaf has no way to
represent one it did not receive. The shipped proposal carries `decision_state="absent"` with
`decision_reference=None`, and `CutoverProposal.executes_cutover` is typed
`Literal[False] = False`: the field exists so a reader can see the artifact declare that it does not
perform the cutover, and its type makes the opposite value unconstructible rather than merely
unwritten.

**One accessor, and it is the deliverable.** `cutover_artifacts()` returns a three-key mapping —
`"criteria"`, `"plan"`, `"proposal"` — and its docstring states that the mapping is the deliverable
§8.1 names, that nothing in it is executed, and that the function has no side effect. It is the only
callable here that returns the artifacts together, and it returns them by identity rather than copying
or rendering them.

### Conventions

Every type in this module is a `@dataclass(frozen=True)` — `CriterionObservation`, `CutoverCriterion`,
`CutoverStep`, `CutoverPlan`, `CutoverProposal` — so the artifacts are immutable values and a caller
cannot edit a plan in place before reporting it. The three artifacts are module-level names in
`UPPER_SNAKE_CASE` (`CUTOVER_CRITERIA`, `CUTOVER_PLAN`, `CUTOVER_PROPOSAL`) beside the two escalation
constants, and the plan and proposal are built once at import time from those constants rather than
assembled per call. Closed vocabularies are `Literal` aliases declared once:
`ProposalDecision = Literal["absent", "owner-recorded"]` and the `Literal[False]` on
`executes_cutover`. The four public functions carry docstrings that state what they do *not* do
(`evaluate_criteria` does not evaluate; `cutover_artifacts` has no side effect), and the module
declares no `__all__`. Nothing in this file imports another module of the `memory.migration` package,
so the three artifacts depend on no peer artifact and on no store.

### Invariants And Boundaries

- **Nothing here executes, triggers or activates.** There is no authority flag, no cutover trigger,
  no scheduled activation and no write path in this module; §8.4 requires that no artifact here be a
  gate, and the way the module keeps that true is by having no side effect at all.
- **An unmet criterion is reported, never narrowed.** Each criterion is a predicate over a census
  result, and an unmet one is reported with the exact observed measure; a criterion that cannot be met
  yields a deferred cutover, not a softened statement. "Cutover is not yet justified" is a conforming
  output.
- **An omitted criterion is a `ValueError`, not a shorter result.** `evaluate_criteria` refuses any
  observation set missing a declared `criterion_id`, and `measure_criterion` refuses any
  `criterion_id` this module does not declare, so neither a skipped nor an invented criterion can
  reach a reader as a complete evaluation.
- **An approval is not representable, and the cutover is not performable by this artifact.**
  `ProposalDecision` admits only `absent` and `owner-recorded`, and `executes_cutover` is
  `Literal[False]`, so the value that would claim an approval or a performed cutover cannot be
  constructed here.
- **The escalation quotes the boundary instead of paraphrasing it.** Both the reference and the item
  are stored as data and copied onto the proposal, so the sentence the decision is reserved by is the
  same one the proposal carries.
- **The plan states a property, not a location.** The archival destination, retention and
  referencability are the owner's to decide; the plan names what they must satisfy — preserved,
  referencable, off every reader's resolution path, never an implicit fallback — and invents no path.
- **The point of no return is a step index, and the rollback story is bound to it.** The rollback must
  be decided before step 5 and recorded with the decision, because recovering an archive is a second
  cutover rather than a rollback.
- **No reader is changed by anything in this file.** The artifacts describe a future transition; the
  legacy corpus stays live until an owner records a decision and executes the plan elsewhere.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

This module is the preparation half of the leaf's cutover story: the artifacts describe a transition
that some other seat, with a recorded owner decision, would perform. The rows below cite the module's
statement of its own boundary, the six criteria and their evidence requirement, the seven-step plan
with its reversibility markers and point of no return, the pure re-ordering and the derived verdict
with the two refusals that keep an evaluation honest, the escalation constants the proposal quotes,
and the shipped proposal whose decision state is `absent`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of its boundary: three artifacts, none executed, no trigger, no flag, no scheduled activation, and no function that writes anything. | `CUTOVER_CRITERIA`; `CUTOVER_PLAN`; `CUTOVER_PROPOSAL` | mcp/src/agents_remember/memory/migration/cutover.py:1-19; mcp/src/agents_remember/memory/migration/cutover.py:111-111; mcp/src/agents_remember/memory/migration/cutover.py:175-175; mcp/src/agents_remember/memory/migration/cutover.py:240-240 |
| One criterion's outcome as a value, carrying the exact observed measure beside what the criterion requires, so an unmet criterion reports what fell short. | `CriterionObservation` | mcp/src/agents_remember/memory/migration/cutover.py:38-52 |
| The criterion shape, with the evidence field that names what would show the condition holds. | `CutoverCriterion` | mcp/src/agents_remember/memory/migration/cutover.py:55-65 |
| The step shape, each step stating its own reversibility rather than leaving it to the plan's prose. | `CutoverStep` | mcp/src/agents_remember/memory/migration/cutover.py:68-75 |
| The plan value: the ordered steps, the rollback story, the archival step stated as a property to satisfy, and the point of no return as a step index. | `CutoverPlan` | mcp/src/agents_remember/memory/migration/cutover.py:78-92; mcp/src/agents_remember/memory/migration/cutover.py:220-237 |
| The six criteria, each a predicate over a census result with its own evidence, covering inventory completeness, parse-outcome disposition, reference resolution and assessment completion with `P` as the exact shortfall. | `CRIT-1-inventory-complete`; `CRIT-2-parse-outcomes-dispositioned`; `CRIT-3-references-resolved`; `CRIT-4-assessment-completion`; "CRIT-1-inventory-complete"; "CRIT-2-parse-outcomes-dispositioned"; "CRIT-3-references-resolved"; "CRIT-4-assessment-completion" | mcp/src/agents_remember/memory/migration/cutover.py:111-151 |
| The two criteria that gate on another seat's work rather than on a count: the independently reviewed denominator that was not derived from the corpus, and the negative proof that no path revives legacy prose as authority. | `CRIT-5-denominator-reviewed`; `CRIT-6-no-authority-fallback`; "CRIT-5-denominator-reviewed"; "CRIT-6-no-authority-fallback" | mcp/src/agents_remember/memory/migration/cutover.py:152-171 |
| The seven-step plan: steps 1 to 4 reversible preparation, steps 5 to 7 irreversible, with the archive preserved and referencable and never read as authority again. | `CutoverStep`; `point_of_no_return` | mcp/src/agents_remember/memory/migration/cutover.py:175-238 |
| The escalation boundary and its item, stored as data so the proposal quotes the same sentence the decision is reserved by. | `ESCALATION_BOUNDARY`; `ESCALATION_ITEM` | mcp/src/agents_remember/memory/migration/cutover.py:27-30; mcp/src/agents_remember/memory/migration/cutover.py:240-251 |
| The decision vocabulary with no value that means approved, because an approval is a recorded decision owned elsewhere. | `ProposalDecision` | mcp/src/agents_remember/memory/migration/cutover.py:32-35 |
| The proposal shape: the exact boundary, the decision state and the field declaring that this artifact does not execute the cutover. | `CutoverProposal` | mcp/src/agents_remember/memory/migration/cutover.py:95-105; mcp/src/agents_remember/memory/migration/cutover.py:249-250 |
| The pure re-ordering and completeness check, which refuses an evaluation that omits a declared criterion because an omitted criterion reads as a satisfied one. | `evaluate_criteria` | mcp/src/agents_remember/memory/migration/cutover.py:254-275 |
| The verdict derived from the observations rather than passed in, rendering "cutover is not yet justified" with each unmet criterion's exact measure. | `criteria_verdict` | mcp/src/agents_remember/memory/migration/cutover.py:278-291 |
| The one measurement function: it refuses a criterion this module does not declare, and calls the predicate once so a met criterion cannot contradict its own measure. | `measure_criterion` | mcp/src/agents_remember/memory/migration/cutover.py:294-322 |
| The single accessor that returns the three artifacts together, executing none of them. | `cutover_artifacts` | mcp/src/agents_remember/memory/migration/cutover.py:325-336 |
| The case that exercises the artifact set and its execution claim, so the "three artifacts, none executed" boundary is checked rather than asserted. | `cutover` | mcp/tests/test_migration_census.py:795-804 |
| The case that pins the escalation to the governing boundary and its exact item, and the case that refuses to soften an unmet criterion. | `cutover` | mcp/tests/test_migration_census.py:806-812; mcp/tests/test_migration_census.py:814-838 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The criteria, the plan and the proposal are
module-level values describing a transition of this repository's own onboarding corpus, and every
identity they carry is a criterion identifier, a step index or a quoted boundary string; nothing here
reaches another repository, another dataset or a remote.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): created this one-to-one card for the cutover preparation module, whose centre is what it does **not** do — it produces the three artifacts §8.1 names and executes none of them, with no trigger, no flag, no scheduled activation and no write path of any kind. It records the six `CUTOVER_CRITERIA` with their requirement that each name the evidence that would show it, the seven-step `CUTOVER_PLAN` with its per-step reversibility markers, the `point_of_no_return=5` index and the archival step stated as a property (preserved, referencable, off every reader's resolution path, never an implicit fallback) rather than as a location. It records the two refusals that keep an evaluation honest: `evaluate_criteria` raises `ValueError` for an observation set that omits a declared criterion, and `measure_criterion` raises `ValueError` for a criterion identifier this module does not declare, calling its predicate exactly once so a met criterion cannot contradict its own measure. It records the derived verdict of `criteria_verdict`, which renders "cutover is not yet justified" with each unmet criterion's observed value as a conforming output rather than a failure. It records the escalation as data — `ESCALATION_BOUNDARY` and `ESCALATION_ITEM` copied onto a proposal whose `decision_state` is `absent` on a two-value vocabulary that admits no approval, and whose `executes_cutover` is typed `Literal[False]`. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
