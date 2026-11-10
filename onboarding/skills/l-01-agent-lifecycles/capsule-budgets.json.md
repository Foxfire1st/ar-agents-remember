# skills/l-01-agent-lifecycles/capsule-budgets.json

## Governing Overview

[overview](overview.md)

## Purpose

This registry keeps the historical capsule and step-detail budgets with the decisions that set them, and the handover-projection token budgets. It records capsule ceilings of Architect 4,631 words, Manager 4,513, Curator 4,100, Reviewer and Bootstrap 4,000 and other roles 3,700, a 2,700-word step-detail ceiling and a shared-digest budget of 1,474 words against its recorded size of 1,000. One later decision sets only 24 named budgets to their measured sizes and another sets the Architect working-rules detail to 2,200 words; every other budget remains min(ceil(size_words * 11 / 10), the applicable ceiling). It has 38 capsule rows and 27 step-detail rows, keyed by the role and reference names of their measurement, including the removed Designer and Strategist roles and the earlier flat `reference/` file names. These are stored declarations, not a new compilation or test run. The limits and measurements for the texts delivered now are in `capsule-budgets-current.json`; `capsule-budgets-d694.json` is its predecessor layer, and both bind this registry by its SHA-256 as the historical record.

## Code Commentary

Size is whitespace-split words of `render_instructions()`, task data and seals excluded. Growth, a new role and a new operation are each a decision recorded in the same change as the raised or added budget. The budget test fails when a capsule exceeds its current limit, lacks one, or the current record names a capsule the manifest no longer yields; it reads those limits from `capsule-budgets-current.json` and only the handover rows and provisional records from this file. The registry also records a `handover` budget for each role a start operation launches: the size is that role's largest legal projection and the budget is the smaller of ceil(size x 11 / 10) and 3,300 tokens.

## Measured instruction changes

decisions_L170 records ten changed capsule measurements for the conditional sync, precedent, direct-repair and evidence obligations. decisions_L172 records 22 changed capsule measurements for the rule-1 change that makes the role and operation texts send what is handed over and awaited with `role_message` instead of pointing at the agent's own chat; `curator/curation` replaces text and adds none, standing at 3,698 words, and no capsule exceeds 3,700. decisions_L182 records the six Architect entries re-measured for the change that replaces the Architect's prohibition on running checks himself with a freedom bounded to a copy and to his own seat: orientation 2972 words against 3270, planning 2323 against 2556, review 2582 against 2841, coordination 3576 against 3700, authorized-closeout 2195 against 2415 and recovery 2288 against 2517. Stored measurements are declarations and retained compiler provenance; reading them is not a fresh compiler run, test execution or native-host grade.

## The bootstrap measurement decision

`decision_L196_B10` records the three changed Bootstrap capsules in the same change as the texts they measure: `bootstrap/bootstrap` 3,688 words against the 3,700 ceiling (from 3,622), `bootstrap/orientation` 2,628 against 2,891 (from 2,593), and `bootstrap/recovery` 1,944 against 2,139 (from 1,909). The decision records no step-detail change (`step_detail_changes` is empty); the registry's `step_details` hold the row keyed `reference/bootstrap-failure-states.md` (the file is now `reference/bootstrap/failure-states.md`) at 724/797 words and the row keyed `reference/bootstrap-foundation-d301.md` (now `reference/bootstrap/foundation-state.md`) at 241/266. Every step detail is re-measured and unchanged, and no other capsule, step detail, ceiling or compiler count rule changes. These remain stored declarations, not a fresh compiler run.

## Canonical Source Ownership

The byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. Whole-file source evidence does not certify inherited statements, execution, grading or the whole card.

- The earlier L88 decision introduced capped capsule/step budgets and recorded fourteen admitted step files at that change; those fourteen are historical measurements, not the current step-file total. [5]

- The earlier L88 repair-round decision retains its measured capsule changes under the fixed capsule and detail ceilings; its fourteen-file context remains historical, not a fresh measurement or current registry total. [6]

- The retained L88 decisions preserve their authority, measurements and fourteen-step-file provenance from that change; later step additions do not rewrite those historical measurements. [7]

## Outside scratch and merged capsule measurements

The registry retains the publication-pointer decision's historical measurements above, the earlier outside-scratch sync measurements in `decision_L198_sync`, and the merged measurements in `decision_L198_post_L194_sync`. They describe their own source trees; the earlier curator values are not the current merged values.

The retained handover block records worker implementation at 3,038 tokens, reviewer review at 3,064 and curator curation at 3,054, each budgeted at 3,300. The sync changes none of those recorded values; reading the registry does not claim a new handover measurement.

## Merged measurement evidence

- The registry contains 38 capsule rows and 27 step-detail rows; its ceilings are Architect 4,631, Manager 4,513, Curator 4,100, Reviewer and Bootstrap 4,000, other roles 3,700 and step files 2,700. Anchor: `capsule_ceilings_words` [3]

- The registry retains the earlier instruction-change measurement decisions alongside named later ceiling decisions. Each historical measurement describes its own source epoch; the retained decisions are not fresh compiler execution or acceptance. [8]

- The current registry retains decision_L198_post_L194_sync as its historical measurement account. Its recorded values and provenance describe that source epoch, rather than the current matrix or a new execution. [9]

- Budgets are min(ceil(size_words * 11 / 10), the applicable ceiling) except the 24 budgets one decision set to their measured sizes and the one detail budget a later decision superseded; the shared digest budget is 1,474. Anchor: `budget_authority` [11]

- The no-overrun budget test reads current limits and measurements from `capsule-budgets-current.json` and only the handover rows and provisional records from this registry; other budget tests still read this registry's D656_R8 raises and check its recorded budgets against the D681 limits. [12]

- All 38 capsule rows carry recorded budgets: capped eleven-tenths budgets, or the measured size for the 8 capsule rows among the 24 budgets one decision names. Anchor: `decisions_D681` [1]

- The test bounds fresh compiled sizes by the current record's limits; decision recording is registry policy and is not checked by this test. [2]

- The authored source owns this contract; the distribution copy is not a separate authority. [4]

- The registry's capsule, step-detail and handover rows keep their recorded values; the handover rows keep the capped token formula. [10]
