# operations/review.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/review.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T22:19+02:00 |
| lastVerifiedCommitHash | `15fa0e2c0bb91d5bb1b2abf4ee8eb54916bd5ed4` |
| lastVerifiedCommitDate | 2026-09-16T22:28:15+02:00|
| governingOverview      | `../../../../../../../overview.md` |

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

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| The operation block's declared purpose, source path, and applicable roles. | `"operations"`; `"purpose"`; `"applies_to_roles"` | skills/l-01-agent-lifecycles/composition-manifest.json:1-1 |
| The manifest keeps the operation vocabulary at exactly these eight names. | `OPERATION_KEYS`; `test_manifest_resolves_every_role_and_operation_source` | mcp/tests/test_role_instruction_corpus.py:56-64; mcp/tests/test_role_instruction_corpus.py:199-225 |
| The canonical source of this block. | `# Operation` | skills/l-01-agent-lifecycles/operations/review.md:1-1 |
| The completion-truth clause this block carries, and the boundary's one home. | `## Handoff / exit` | skills/l-01-agent-lifecycles/operations/review.md:116-120; skills/l-01-agent-lifecycles/core/acceptance.md |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T22:19+02:00 — 260915-CAPS-L16 curator: `## Handoff / exit` now states the completion-truth
  boundary in the detector's own vocabulary — terminal/finalizer truth **then** attests only that
  **this** turn ended, wakes the decider, and the reviewer authors no second completion row. The
  sentence already said all of it; what moved was the wording the completion-truth detector reads
  ("the reviewer's turn ended" → "this turn ended"), and the body now records both facts together so a
  later reader does not reword them apart. **Also repaired here (D16):** this card's
  `governingOverview` field and link pointed five levels up, at
  `onboarding/mcp/src/agents_remember/overview.md`, which does not exist — the card's own link text says
  "MCP package overview", which from `operations/` is **seven** levels up. Both now resolve to
  `onboarding/mcp/overview.md`. Verification metadata moves to this leaf's synced base `8997e184`; the
  candidate is deliberately uncommitted, so the governed closeout stamps the real code commit and no
  hash or fingerprint was invented here.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/operations/review.md` — a file added by the role-instruction corpus consolidation. The canonical source is an operation-scoped procedure block extracted from interleaved role prose (review).; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
