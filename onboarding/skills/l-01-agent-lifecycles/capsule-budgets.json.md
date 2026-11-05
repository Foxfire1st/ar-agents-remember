# skills/l-01-agent-lifecycles/capsule-budgets.json

## Governing Overview

[lifecycle overview](overview.md)

## Purpose

Past-epoch budget account (retained wording, not current policy): The decision-backed registry of all 38 role, operation and launcher capsule budgets: each current capsule budget equals min(ceil of its compiled instruction-word size times eleven over ten, 3,700), recorded in the same change as the texts it measures.

Current registry policy applies a role-specific capsule ceiling at every stage: Architect 4,631 words; Manager 4,513; Curator, Reviewer and Bootstrap 4,000; other roles 3,700. Budgets remain min(ceil(size_words * 11 / 10), the applicable ceiling). The registry has 38 capsule rows and 28 step-detail rows; step details retain the 2,500-word ceiling. The separately delivered shared digest records size_words 1,000 and budget_words 1,100. These are stored declarations, not a new compilation or test run.

## Code Commentary

Size is whitespace-split words of `render_instructions()`, task data and seals excluded. Growth, a new role and a new operation are each a decision recorded in the same change as the raised or added budget. The budget test fails when a capsule exceeds its budget, lacks one, or the registry names a capsule the manifest no longer yields. The registry also records a `handover` budget for each role a start operation launches: the size is that role's largest legal projection and the budget is the smaller of ceil(size x 11 / 10) and 3,300 tokens.

## Current composition and authoring contract

Past-epoch budget account (retained wording, not current policy): The registry keeps 38 role/operation/launcher rows. Its current rule is `min(ceil(size_words * 11 / 10), ceiling)`, with a 3,700-word capsule ceiling and a 2,500-word step-file ceiling. Capsule counts are declared as whitespace-split `render_instructions()` words excluding task data and seals; step counts cover the complete declared source.

The current role-specific ceilings and 28-detail inventory stated above govern this earlier account.

Past-epoch budget account (retained wording, not current policy): Fifteen admitted step files have separate `step_details` rows. L88 and its repair-round decisions explain the recorded numbers; older L101, L116 and L54 decision objects retain their parsed values despite compact reserialization. Stored size declarations and this static comparison are not freshly executed compiler, budget-test or host evidence. The old unconditional equality-to-ceil promise is false for capped rows; a successful line mapping cannot fix that semantic difference.

The current role-specific ceilings and 28-detail inventory stated above govern this earlier account.


## Measured instruction changes

decisions_L170 records ten changed capsule measurements for the conditional sync, precedent, direct-repair and evidence obligations. decisions_L172 records 22 changed capsule measurements for the rule-1 change that makes the role and operation texts send what is handed over and awaited with `role_message` instead of pointing at the agent's own chat; `curator/curation` replaces text and adds none, standing at 3,698 words, and no capsule exceeds 3,700. decisions_L182 records the six Architect entries re-measured for the change that replaces the Architect's prohibition on running checks himself with a freedom bounded to a copy and to his own seat: orientation 2972 words against 3270, planning 2323 against 2556, review 2582 against 2841, coordination 3576 against 3700, authorized-closeout 2195 against 2415 and recovery 2288 against 2517. The registry still uses capped eleven-tenths budgets with the existing capsule and step ceilings. Stored measurements are declarations and retained compiler provenance; reading them is not a fresh compiler run, test execution or native-host grade.

## The bootstrap measurement decision

`decision_L196_B10` records the three changed Bootstrap capsules in the same change as the texts they measure: `bootstrap/bootstrap` 3,688 words against the 3,700 ceiling (from 3,622), `bootstrap/orientation` 2,628 against 2,891 (from 2,593), and `bootstrap/recovery` 1,944 against 2,139 (from 1,909). Its reason is specific: `operations/bootstrap.md` step 6 no longer scaffolds onboarding through `c-03-repo-bootstrap` or runs the citation fixer — it reads what the baseline will carry and says that optional onboarding and the knowledge foundation are the later Architect task's work — step 7 keeps the preview, the status readback, the developer's drift decision and the unconditional validator refusal, and `roles/bootstrap.md` puts the prohibitions of "What you must not do" above the operation on disagreement. The registry also gains the step-detail row for `reference/bootstrap-failure-states.md` at 724/797 words, and the existing `reference/bootstrap-foundation-d301.md` row is re-measured at 241/266. Every step detail is re-measured and unchanged, and no other capsule, step detail, ceiling or compiler count rule changes. These remain stored declarations, not a fresh compiler run.

## Evidence


> Retained earlier citation wording: - The registry records the instruction-change measurements and reasons under the existing capped budget policy.

Past-epoch source custody: `skills/l-01-agent-lifecycles/capsule-budgets.json`, original Git blob `32588f695124b7d325ef8e5c24ad430a9a85ee81`, lines256–3440. The retained wording above is detached from live citation numbers and belongs only to its named source epoch; the current table supports only its current clauses.






Retained authoring-row wording:

Finding: The test bounds fresh compiled sizes by stored capsule budgets; decision recording is registry policy and is not checked by this test.

Anchor:

Source: mcp/tests/test_role_capsule_budgets.py:111-154; mcp/tests/test_role_capsule_budgets.py:165-175


## Current source qualification

Past-epoch budget account (retained wording, not current policy): The registry has 38 capsule rows with budget min(ceil(size_words * 11 / 10), 3,700), plus 15 step-detail budgets capped at 2,500. Its decisions_L54 section records the authority, method and 21 changed capsule entries; those entries distinguish inherited landed growth from L54 text growth. The other stored decisions and untouched rows remain. These are the registry's measured declarations and provenance, not a newly executed compilation, test, current native launch-size qualification or acceptance.

The current role-specific ceilings and 28-detail inventory stated above govern this earlier account.



## Inherited Source-Epoch Commentary

The following distribution-copy account preserves useful explanations and source-epoch history, not a second current contract. Its currentness, tool, seat, provider, execution and permission claims are inherited scope unless separately qualified above against the current canonical source. Earlier incompatible claims on the explicitly updated seams are historical, not restored authority. Historical labels in this quotation do not allocate this card's reference numbers.

> # mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/capsule-budgets.json
>
> ## Governing Overview
>
> [MCP package overview](../../../../../../overview.md)
>
> ## Purpose
>
> Generated package-data copy of the canonical capsule-budget registry. It carries no contract of its own; the canonical `skills/l-01-agent-lifecycles/capsule-budgets.json` with its card owns the budgets.
>
> ## Code Commentary
>
> `scripts/sync-skills.py` regenerates this copy byte-identical from the canonical source; `sync-skills.py --check` passes 9/9. Never hand-edit a generated copy.
>
> ## Evidence
>
> - This copy is byte-identical to the canonical registry, which owns the contract. (historical reference 1)
> - The canonical registry records all 38 ceil(raw*11/10) budgets. (historical reference 2)

Inherited reference 1 commentary (not a revalidated target):

> This copy is byte-identical to the canonical registry, which owns the contract.

Inherited reference 2 commentary (not a revalidated target):

> The canonical registry records all 38 ceil(raw*11/10) budgets.

## Canonical Source Ownership

The byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. Whole-file source evidence does not certify inherited statements, execution, grading or the whole card.


> Retained earlier citation wording: - The authored source owns this contract; the distribution copy is not a separate authority.




- The earlier L88 decision introduced capped capsule/step budgets and recorded fourteen admitted step files at that change; those fourteen are historical measurements, not the current step-file total. [5]



- The earlier L88 repair-round decision retains its measured capsule changes under the fixed capsule and detail ceilings; its fourteen-file context remains historical, not a fresh measurement or current registry total. [6]



- The retained L88 decisions preserve their authority, measurements and fourteen-step-file provenance from that change; later step additions do not rewrite those historical measurements. [7]



> Retained earlier citation wording: - All 38 capsules carry capped eleven-tenths budgets recorded with the texts they measure.


> Retained earlier citation wording: - The registry retains 38 capped capsule rows and fifteen step-file rows; its decisions retain the provenance of their own measured changes. The publication pointers were measured in their own decision entry — twelve capsules, the 36-word Manager clause, both coordination capsules at the 3,700 ceiling and `manager/coordination` at 3,684 — under the capped budget policy unchanged.

Past-epoch source custody: `skills/l-01-agent-lifecycles/capsule-budgets.json`, original Git blob `32588f695124b7d325ef8e5c24ad430a9a85ee81`, lines40–255. The retained wording above is detached from live citation numbers and belongs only to its named source epoch; the current table supports only its current clauses.

## Outside scratch and merged capsule measurements

The outside-scratch guidance preserves the capped eleven-tenths formulas and the existing ceilings. The registry retains the publication-pointer decision's historical measurements above, the earlier outside-scratch sync measurements in `decision_L198_sync`, and the merged measurements in `decision_L198_post_L194_sync`. They describe their own source trees; the earlier curator values are not the current merged values.

Past-epoch source custody: `skills/l-01-agent-lifecycles/capsule-budgets.json`, original Git blob `32588f695124b7d325ef8e5c24ad430a9a85ee81`, lines3220–3439. The retained wording above is detached from live citation numbers and belongs only to its named source epoch; the current table supports only its current clauses.

Past-epoch merged measurement account (retained wording; the current matrix differs): The current registry records worker orientation at 2,643 words with budget 2,908, implementation at 2,378 with budget 2,616, and recovery at 1,959 with budget 2,155. Curator orientation is 3,121 with budget 3,434, curation is 3,700 with budget 3,700, and recovery is 2,437 with budget 2,681. Reviewer orientation is 3,698 with budget 3,700, review is 3,652 with budget 3,700, and recovery is 3,014 with budget 3,316. Manager coordination is 3,678 with budget 3,700. All 38 capsule rows retain the capped formula; all fifteen step-detail measurements remain unchanged in the merged decision. These are stored declarations, not a fresh compiler run.

Current registry policy applies a role-specific capsule ceiling at every stage: Architect 4,631 words; Manager 4,513; Curator, Reviewer and Bootstrap 4,000; other roles 3,700. Budgets remain min(ceil(size_words * 11 / 10), the applicable ceiling). The registry has 38 capsule rows and 28 step-detail rows; step details retain the 2,500-word ceiling. The separately delivered shared digest records size_words 1,000 and budget_words 1,100. These are stored declarations, not a new compilation or test run.

Past-epoch source custody: `skills/l-01-agent-lifecycles/capsule-budgets.json`, original Git blob `32588f695124b7d325ef8e5c24ad430a9a85ee81`, lines3220–3439. The retained wording above is detached from live citation numbers and belongs only to its named source epoch; the current table supports only its current clauses.

The retained handover block records worker implementation at 3,038 tokens, reviewer review at 3,064 and curator curation at 3,054, each budgeted at 3,300. The sync changes none of those recorded values; reading the registry does not claim a new handover measurement.

## Merged measurement evidence

- The registry records the instruction-change measurements and reasons under the existing capped budget policy.

Past-epoch source custody: `skills/l-01-agent-lifecycles/capsule-budgets.json`, original Git blob `32588f695124b7d325ef8e5c24ad430a9a85ee81`, lines3220–3439. The retained wording above is detached from live citation numbers and belongs only to its named source epoch; the current table supports only its current clauses.

Retained authoring-row wording:

Finding: The registry's current capsule, step-detail and handover rows retain their capped formulas and recorded values.

Anchor:

Source: skills/l-01-agent-lifecycles/capsule-budgets.json:2-38; skills/l-01-agent-lifecycles/capsule-budgets.json:40-307; skills/l-01-agent-lifecycles/capsule-budgets.json:3513-3525

Retained authoring-row wording:

Finding: All 38 capsules carry capped eleven-tenths budgets recorded with the texts they measure.

Anchor:

Source: skills/l-01-agent-lifecycles/capsule-budgets.json:2-4; skills/l-01-agent-lifecycles/capsule-budgets.json:40-193; skills/l-01-agent-lifecycles/capsule-budgets.json:3513-3525


- The registry retains 38 capped capsule rows and fifteen step-file rows; its decisions retain the provenance of their own measured changes.  Anchor: current definitions

Past-epoch source custody: `skills/l-01-agent-lifecycles/capsule-budgets.json`, original Git blob `32588f695124b7d325ef8e5c24ad430a9a85ee81`, lines40–255. The retained wording above is detached from live citation numbers and belongs only to its named source epoch; the current table supports only its current clauses.


Retained authoring-row wording:

Finding: The authored source owns this contract; the distribution copy is not a separate authority.

Anchor:

Source: skills/l-01-agent-lifecycles/capsule-budgets.json


- The registry records the instruction-change measurements and reasons under the existing capped budget policy.

Past-epoch source custody: `skills/l-01-agent-lifecycles/capsule-budgets.json`, original Git blob `32588f695124b7d325ef8e5c24ad430a9a85ee81`, lines256–3440. The retained wording above is detached from live citation numbers and belongs only to its named source epoch; the current table supports only its current clauses.

- The current registry contains 38 capsule rows and 28 step-detail rows under capped eleven-tenths formulas and the recorded developer-owned ceilings. Current literals include the named later Architect 4,631 and Manager 4,513 raises; the other high roles remain 4,000, other roles 3,700 and step files 2,500. [3]


- The registry retains the earlier instruction-change measurement decisions alongside named later D656 ceiling decisions. Each historical measurement describes its own source epoch; the retained decisions are not fresh compiler execution or acceptance. [8]


- The current registry retains decision_L198_post_L194_sync as its historical measurement account. Its recorded values and provenance describe that source epoch, rather than the current matrix or a new execution. [9]


- Current registry policy applies a role-specific capsule ceiling at every stage: Architect 4,631 words; Manager 4,513; Curator, Reviewer and Bootstrap 4,000; other roles 3,700. Budgets remain min(ceil(size_words * 11 / 10), the applicable ceiling). The registry has 38 capsule rows and 28 step-detail rows; step details retain the 2,500-word ceiling. The separately delivered shared digest records size_words 1,000 and budget_words 1,100. These are stored declarations, not a new compilation or test run. [11]


- Current registry policy applies a role-specific capsule ceiling at every stage: Architect 4,631 words; Manager 4,513; Curator, Reviewer and Bootstrap 4,000; other roles 3,700. Budgets remain min(ceil(size_words * 11 / 10), the applicable ceiling). The registry has 38 capsule rows and 28 step-detail rows; step details retain the 2,500-word ceiling. The separately delivered shared digest records size_words 1,000 and budget_words 1,100. These are stored declarations, not a new compilation or test run. [12]

- All 38 capsules carry capped eleven-tenths budgets recorded with the texts they measure. [1]
- The test bounds fresh compiled sizes by stored capsule budgets; decision recording is registry policy and is not checked by this test. [2]
- The authored source owns this contract; the distribution copy is not a separate authority. [4]
- The registry's current capsule, step-detail and handover rows retain their capped formulas and recorded values. [10]
