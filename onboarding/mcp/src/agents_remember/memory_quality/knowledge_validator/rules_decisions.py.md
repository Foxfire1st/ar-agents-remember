# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_decisions.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R13's decision content rules in the validator's one registry (MIK-R22 rule 9).** Importing the module
registers five rules; `validator.py` imports it next to the other rule modules, so every place the validator runs
(the writer, `validate_tree`, `require_valid_commit`, the managed sync, `knowledge-validate`) runs them over every
decision record of the candidate tree. The checks themselves are the pure functions of
`models/knowledge_files/decisions.py`.

| Rule | Status | What it checks |
| --- | --- | --- |
| `R13.1-alternatives` | refusing | at least two alternatives, and exactly one `chosen` |
| `R13.1-reconsider-when` | refusing | every `rejected` or `deferred` alternative states `reconsider_when` |
| `R13.2-superseded-derived` | refusing | `superseded` is never stored, as the decision's status or an alternative's |
| `R13.3-reconsider-on` | refusing | a `reconsider_on` link's `alternative` indexes an existing `rejected` or `deferred` alternative |
| `R13.3-governs` | report-only | a decision with no `explains`, `constrains` or `motivated_change_to` link is read from nowhere |

## Code Commentary

### Logic

- `_decisions` walks the parsed records and yields each `DecisionRecord` with its path; `_findings` turns each
  `ContentProblem` into a `Finding` at the problem's field.
- `check_alternatives`, `check_reconsider_when` and `check_reconsider_on` run `alternative_problems`,
  `reconsider_when_problems` and `reconsider_link_problems` per decision.
- `check_superseded_not_stored` reads the **raw** JSON of every file under `knowledge/decisions/`
  (`_DECISION_DIRECTORY`), because a stored `superseded` never parses: the shape rule `R22.1-shape` refuses the same
  file, and this rule says why and names the field (`status` or `alternatives.<i>.status`) with the remedy (keep it
  `active` and name it in the superseding decision's `supersedes`). A file that is not JSON is left to the shape
  rule. A record with `superseded` does not parse, so its other content rules are not evaluated until it is fixed.
- `check_governs` reports a decision with no governs link: "link what it governs, or keep it in the task if it
  governs nothing". It is **report-only by ruling 01:45:56 Q2**: the packet lists the link types but does not
  require one, and whether a lifted decision still governs code is the curator's judgment.

### Conventions

- **The content rules apply to every decision, new or carried** (ruling 01:45:56 Q3): the packet's refusal list has
  no new/existing split, unlike MIK-R27, and the conversion exports no decisions, so no carried tree can be blocked
  at the cutover.
- None of the five rules sets `writer_reports`, so the writer refuses exactly as a commit route does.
- Rule IDs carry the packet rule number (`R13.1`, `R13.2`, `R13.3`) and each `ValidationRule` cites "MIK-R13 rule N".

### Invariants And Boundaries

- **A decision has at least two alternatives and exactly one chosen**, and **every rejected or deferred alternative
  says when to reconsider**: refused by `R13.1-alternatives` and `R13.1-reconsider-when`; proved by the unit cases in
  `test_knowledge_decisions.py`, by the writer refusal `test_a_decision_that_breaks_a_content_rule_is_refused_and_nothing_is_written`,
  and on real data by the worker's and reviewer's hand edits (one alternative only: refused by this build, **passed
  by the base build**).
- **Superseded is derived, never stored**: refused by `R13.2-superseded-derived` (plus the shape rule); proved by
  `test_a_stored_superseded_status_is_refused_naming_the_field` and the real hand-edit runs.
- **`origin` names the task or ruling** without a rule here (ruling 01:45:56 Q1): `origin.task` is required by
  MIK-R21's shape, and the ruling travels in the attached entry's evidence (`origin.handoff.evidence`); the
  `knowledge-bootstrap:<repo>` origin of a bootstrap wave is valid provenance. **Admission** is MIK-R27's
  (`rules_admission`), where a decision is never an export (L13 review F6).
- **An unresolved requirement endpoint is never a violation.** The validator has no task plane (`memory_quality`
  ranks below `memory`), so it only checks the reference's shape; the writer reports each endpoint's resolution.
- **Nothing is refused until decisions are authored on a converted line.** The validator runs only over converted
  memory (MIK-R22 rule 8), and the conversion writes no `knowledge/decisions/` directory; `knowledge-validate` on
  a freshly converted tree gave byte-identical reports from the base and the L13 builds (review R1).

### Todos

- **L14 (ruling 01:45:56 Q5/Q6; review F1, F2): resolved by L14 for index stability, partly for endpoints.** The
  sibling rule `R14.1-linked-alternative-order` (`rules_reconsideration.py`) refuses a reorder that moves a linked
  alternative; the endpoints of `reconsider_on` links are reported, through `resolve_requirement_endpoint`, in the
  worklist's `reconsideration.links` summary. The validator itself still resolves no endpoint (no coordination root
  on commit routes); the reads stay with L29.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R13@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`13_decision-records-with-rejected-alternatives.json`), MIK-R21 rules 4 and 6 for the record and requirement-reference
shapes, and the coordination-root note Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`,
section 4.5); they live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The five rules and their registration.

- The decision files the raw superseded check reads. [1]
- Every parsed decision with its path, and each problem as a finding. [2]
- The three refusing content checks, one per rule. [3]
- A stored superseded is named from the raw JSON, with the remedy. [4]
- A decision with no governs link is reported. [5]
- The five rules, four refusing and one report-only, registered on import. [6]
- The rule table the module docstring states, including why the rules apply to every decision. [7]
- D12 and D18 as records pass every rule. [8]
- A governs-less decision is reported, not refused. [9]

### Cross-Repo References

No meaningful cross-repo references found: the rules read the validation context's candidate tree only.

No cross-repo boundary is crossed by this file.
