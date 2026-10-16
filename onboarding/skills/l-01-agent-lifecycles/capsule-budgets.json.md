# skills/l-01-agent-lifecycles/capsule-budgets.json

## Governing Overview

[lifecycle overview](overview.md)

## Purpose

The decision-backed registry of all 38 role, operation and launcher capsule budgets: each current capsule budget equals min(ceil of its compiled instruction-word size times eleven over ten, 3,700), recorded in the same change as the texts it measures.

## Code Commentary

Size is whitespace-split words of `render_instructions()`, task data and seals excluded. Growth, a new role and a new operation are each a decision recorded in the same change as the raised or added budget. The budget test fails when a capsule exceeds its budget, lacks one, or the registry names a capsule the manifest no longer yields.

## Current composition and authoring contract

The registry keeps 38 role/operation/launcher rows. Its current rule is `min(ceil(size_words * 11 / 10), ceiling)`, with a 3,700-word capsule ceiling and a 2,500-word step-file ceiling. Capsule counts are declared as whitespace-split `render_instructions()` words excluding task data and seals; step counts cover the complete declared source.

Fourteen admitted step files have separate `step_details` rows. L88 and its repair-round decisions explain the recorded numbers; older L101, L116 and L54 decision objects retain their parsed values despite compact reserialization. Stored size declarations and this static comparison are not freshly executed compiler, budget-test or host evidence. The old unconditional equality-to-ceil promise is false for capped rows; a successful line mapping cannot fix that semantic difference.


## Evidence



- The test bounds fresh compiled sizes by stored capsule budgets; decision recording is registry policy and is not checked by this test. [2]

## Current source qualification

The registry has 38 capsule rows with budget min(ceil(size_words * 11 / 10), 3,700), plus 14 step-detail budgets capped at 2,500. Its decisions_L54 section records the authority, method and 21 changed capsule entries; those entries distinguish inherited landed growth from L54 text growth. The other stored decisions and untouched rows remain. These are the registry's measured declarations and provenance, not a newly executed compilation, test, current native launch-size qualification or acceptance.



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

- The authored source owns this contract; the distribution copy is not a separate authority. [4]


- Replaces uncapped eleven-tenths budgets with capped capsule/step budgets; adds fourteen step sources and L88 provenance while retaining parsed older decision payloads. [5]

- Replaces uncapped eleven-tenths budgets with capped capsule/step budgets; adds fourteen step sources and L88 provenance while retaining parsed older decision payloads. [6]

- Replaces uncapped eleven-tenths budgets with capped capsule/step budgets; adds fourteen step sources and L88 provenance while retaining parsed older decision payloads. [7]

- All 38 capsules carry capped eleven-tenths budgets recorded with the texts they measure. [1]

- The registry retains 38 capped capsule rows, fourteen step-file rows and the earlier L54 decision account; L88 decisions state the new ceiling and growth provenance. [3]
