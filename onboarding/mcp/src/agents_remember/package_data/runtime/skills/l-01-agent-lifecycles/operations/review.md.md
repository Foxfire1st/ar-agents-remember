# operations/review.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The requested independent review seam and its exact mode contract — what a baseline seals, what a successor may verify, and how the verdict is recorded and consumed.

Every operation block shares one five-part shape — who carries it, required inputs, normal workflow, authority gates, failure handling, and handoff/exit — which is what makes a long procedure separately loadable instead of padding every role file.

## Code Commentary

### Logic

`## Required inputs` is a two-row mode table: `reviewMode=baseline` takes the complete agreed scope, all
applicable standing criteria from `../criteria/`, the required routes/lenses, and the evidence to inspect
them, and states the simple review rule (no review state means the used-round count is zero and the next
review is a baseline — do not create a pristine marker or refuse because legacy history is absent).
`reviewMode=fix-verification` takes the sealed baseline, the immediately preceding result, the exact
outstanding IDs, and the worker fixes/evidence. `## Who carries it, and their job` assigns the reviewing
seat, the manager's `begin_review`/`record_review` duty, the orchestrator's super-exit dispatch, and the
architect's plan-review ruling; `## Normal workflow` and `## Authority gates` keep the successor rounds
inside the sealed finding set.

`## Handoff / exit` carries the completion-truth boundary for this surface: the verdict artifact is the
durable handoff, and terminal/finalizer truth **then** attests only that **this** turn ended and wakes
the decider, who validates the verdict independently. The reviewer authors no second completion row and
carries no decider runtime identity. The wording matters mechanically as well as semantically — the
detector reads "then attests only that this turn ended", and the clause now states both facts in the
detector's own vocabulary rather than implying them.

### Conventions

Review is never selected by default; closeout and integration neither require nor launch it.

### Invariants And Boundaries

- An operation block holds procedure only; a rule that applies across roles belongs in `core/`.
- A role file names the operation it selects; it does not restate the procedure.
- The operation vocabulary is closed at eight names, so an unknown operation is an explicit error rather than a silent fallback.
- Authority gates and failure handling stay inside this block, not in the role that triggers it.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References

| The operation block's declared purpose, source path, and applicable roles. | `"operations"`; `"purpose"`; `"applies_to_roles"` | skills/l-01-agent-lifecycles/composition-manifest.json:1-1; skills/l-01-agent-lifecycles/composition-manifest.json:45-45; skills/l-01-agent-lifecycles/composition-manifest.json:47-47; skills/l-01-agent-lifecycles/composition-manifest.json:63-63; skills/l-01-agent-lifecycles/composition-manifest.json:73-73; skills/l-01-agent-lifecycles/composition-manifest.json:80-80; skills/l-01-agent-lifecycles/composition-manifest.json:90-90; skills/l-01-agent-lifecycles/composition-manifest.json:98-98; skills/l-01-agent-lifecycles/composition-manifest.json:107-107; skills/l-01-agent-lifecycles/composition-manifest.json:115-115; skills/l-01-agent-lifecycles/composition-manifest.json:128-128; skills/l-01-agent-lifecycles/composition-manifest.json:185-185; skills/l-01-agent-lifecycles/composition-manifest.json:223-223; skills/l-01-agent-lifecycles/composition-manifest.json:261-261; skills/l-01-agent-lifecycles/composition-manifest.json:289-289; skills/l-01-agent-lifecycles/composition-manifest.json:324-324; skills/l-01-agent-lifecycles/composition-manifest.json:366-366; skills/l-01-agent-lifecycles/composition-manifest.json:397-397; skills/l-01-agent-lifecycles/composition-manifest.json:429-429; skills/l-01-agent-lifecycles/composition-manifest.json:463-463; skills/l-01-agent-lifecycles/composition-manifest.json:489-489; skills/l-01-agent-lifecycles/composition-manifest.json:512-512; skills/l-01-agent-lifecycles/composition-manifest.json:539-539; skills/l-01-agent-lifecycles/composition-manifest.json:48-48; skills/l-01-agent-lifecycles/composition-manifest.json:64-64; skills/l-01-agent-lifecycles/composition-manifest.json:74-74; skills/l-01-agent-lifecycles/composition-manifest.json:81-81; skills/l-01-agent-lifecycles/composition-manifest.json:91-91; skills/l-01-agent-lifecycles/composition-manifest.json:99-99; skills/l-01-agent-lifecycles/composition-manifest.json:108-108; skills/l-01-agent-lifecycles/composition-manifest.json:116-116; skills/l-01-agent-lifecycles/composition-manifest.json:129-129; skills/l-01-agent-lifecycles/composition-manifest.json:138-138; skills/l-01-agent-lifecycles/composition-manifest.json:142-142; skills/l-01-agent-lifecycles/composition-manifest.json:146-146; skills/l-01-agent-lifecycles/composition-manifest.json:150-150; skills/l-01-agent-lifecycles/composition-manifest.json:154-154; skills/l-01-agent-lifecycles/composition-manifest.json:158-158; skills/l-01-agent-lifecycles/composition-manifest.json:49-49; skills/l-01-agent-lifecycles/composition-manifest.json:65-65; skills/l-01-agent-lifecycles/composition-manifest.json:75-75; skills/l-01-agent-lifecycles/composition-manifest.json:82-82; skills/l-01-agent-lifecycles/composition-manifest.json:92-92; skills/l-01-agent-lifecycles/composition-manifest.json:100-100; skills/l-01-agent-lifecycles/composition-manifest.json:109-109; skills/l-01-agent-lifecycles/composition-manifest.json:117-117; skills/l-01-agent-lifecycles/composition-manifest.json:130-130 |
| The manifest keeps the operation vocabulary at exactly these eight names. | `OPERATION_KEYS`; `test_manifest_resolves_every_role_and_operation_source` | mcp/tests/test_role_instruction_corpus.py:56-64; mcp/tests/test_role_instruction_corpus.py:199-225; mcp/tests/test_role_instruction_corpus.py:66-66; mcp/tests/test_role_instruction_corpus.py:177-177; mcp/tests/test_role_instruction_corpus.py:180-180; mcp/tests/test_role_instruction_corpus.py:253-253 |
| The canonical source of this block. | `# Operation` | skills/l-01-agent-lifecycles/operations/review.md:1-1 |
| The completion-truth clause this block carries, and the boundary's one home. | `## Handoff / exit` | skills/l-01-agent-lifecycles/operations/review.md:116-120; skills/l-01-agent-lifecycles/core/acceptance.md |

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.
