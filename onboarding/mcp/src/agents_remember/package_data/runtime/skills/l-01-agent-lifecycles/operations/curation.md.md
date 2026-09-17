# operations/curation.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/curation.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T22:19+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The leaf coherence pass — reconciling intended, current, and implemented meaning and writing the affected onboarding.

Every operation block shares one five-part shape — who carries it, required inputs, normal workflow, authority gates, failure handling, and handoff/exit — which is what makes a long procedure separately loadable instead of padding every role file.

## Code Commentary

### Logic

`## Who carries it, and their job` separates two disjoint jobs in one table: the curator reconciles and
writes memory, the manager compiles the brief and owns the transaction. `## Normal workflow` step 5 is the complete curation check set rather than a named scoped check: the
curator runs the full `memory_quality_check` operation for the leaf, repairs or escalates every
curator-actionable finding with its exact returned code, and re-runs it after every repair until
`curatorActionableCount=0` and the **raw** `qualityChecklistStatus=ready-for-closeout`, publishing the `curator_coherence`
authority when the **combined** `checklistStatus` is rewritten to `coherence-required` — which happens
**only when the coherence record is then missing or stale**, the coherence gate. On the success path,
where the record is already current, the combined field is **not rewritten** and keeps its incoming
`ready-for-closeout` value with `closeoutReady=true`. **Field-name
correction (`D35`, made by 260915-CAPS-L10):** the sentence above previously named
`checklistStatus=ready-for-closeout` as the loop's termination condition; read
the raw field to end the loop and the combined field to decide the coherence gate
(`application/memory_quality/controller.py:664`, `:671`, `:678`, `:685-687`).

**Warrant corrected by `CAPS-R19` (leaf `260915-CAPS-L19`).** The `D35` correction above originally rested
on the sentence *"`ready-for-closeout` is never a value of the combined field."* That absolute claim is
**literally false**, and `CAPS-R19`'s revision note records it as superseded by the three-path model now
stated here. The field-name correction it supported still holds; only its stated warrant was wrong.
**Attribution is complementary and both halves hold:** `260915-CAPS-L10`'s curator corrected the
**onboarding cards** that carried the wrong form, while `CAPS-R19` corrected the **shipped sources** — the
five loop-gate carriers, their nine generated copies, and the guard registry's own docstring — and brought
`docs/reference/mcp-tools.md` into both the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`.
`## Authority gates` states the same rule
from the other side: the completed curation is the prerequisite the transaction carries, and a subset
result never stands in for the full operation.

`## Required inputs` states the
three fed inputs (the landed change set with counters and paths pulled from the leaf contract's recorded
range; the leaf task doc with its approved requirement-corpus ruling and version-addressed packets; and
`notes/` with the builder turn report plus the candidate-bound route-review verdict only when review was
requested) and records the rule that none of them is inferred from transcript memory. The block also
carries the curator's own prohibitions — never runs the closeout preview, never repairs transaction
conflicts, never decides whether a leaf lands — and the routing rule that rejects overview-dumping and
task-log-dumping alike.

### Conventions

The strict 1-to-1 source mapping, governing-overview links, and metadata rules live in the `c-05-create-or-update-onboarding-files` skill, not here.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| The operation block's declared purpose, source path, and applicable roles. | `"operations"`; `"purpose"`; `"applies_to_roles"` | skills/l-01-agent-lifecycles/composition-manifest.json:1-1 |
| The manifest keeps the operation vocabulary at exactly these eight names. | `OPERATION_KEYS`; `test_manifest_resolves_every_role_and_operation_source` | mcp/tests/test_role_instruction_corpus.py:56-64; mcp/tests/test_role_instruction_corpus.py:199-225 |
| The canonical source of this block. | `# Operation` | skills/l-01-agent-lifecycles/operations/curation.md:1-1 |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T14:15+02:00 — 260915-CAPS-L19 curator: **Field-name warrant corrected — `ready-for-closeout` read as *never* a value of the combined `checklistStatus`.** That absolute sentence was written by 260915-CAPS-L10's curator as the warrant for this card's `D35` correction, and `CAPS-R19` (`260915-CAPS-L19`) measures it **literally false** (`application/memory_quality/controller.py:685-687` leaves the combined field at its incoming `ready-for-closeout` value on the success path, with `closeoutReady=true`). The card now states the three-path model instead: the raw `qualityChecklistStatus` is the repair loop's gate; the combined `checklistStatus` is rewritten to `coherence-required` **only when the coherence record is then missing or stale**; and `closeoutReady` becomes true only once that validation passes. Corrected under `CAPS-R19`'s revision note (2026-09-17T13:55), which is the authority for this change. The field-name correction itself stands and attribution is complementary — `260915-CAPS-L10` corrected the onboarding cards, `CAPS-R19` corrected the shipped sources (the five loop-gate carriers, their nine generated copies, the guard registry's docstring) and brought `docs/reference/mcp-tools.md` into the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`. The earlier entries below are left exactly as written: they record what L10 did, and this entry is the correction of their warrant. No verification stamp advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-17T13:45+02:00 — 260915-CAPS-L10 curator: **corrected a landed defect (`D35`) in the Logic section.** The complete-curation sentence named `checklistStatus=ready-for-closeout` as the loop's termination condition; `ready-for-closeout` is never a value of the combined field. It now names the **raw** `qualityChecklistStatus` as the loop's gate and the **combined** `checklistStatus=coherence-required` as the point at which the `curator_coherence` authority is published, matching `application/memory_quality/controller.py:664,671,678,687`. The 2026-09-17T12:28+02:00 entry below is left as written: it records what CAPS-L18 did, and this entry is the correction of that wording. No verification stamp advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: **complete curation inverts the doctrine this card recorded.** CAPS-R18@v1 removes the optional/narrow-curation sentences from the shipped instruction corpus and states the rule normatively — the full `memory_quality_check` operation runs as part of every leaf's curation at its contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every curator-actionable finding is repaired or escalated as blocked with its exact returned code, and closeout and integration **carry** the completed curation as a prerequisite while invoking nothing. Added the changed `## Normal workflow` step 5 and `## Authority gates` rule to Logic: the complete curation check set, its `curatorActionableCount=0` / `checklistStatus=ready-for-closeout` termination condition, and the coherence authority published when the checklist requires it.
- 2026-09-16T22:19+02:00 — **No content impact:** 260915-CAPS-L16 curator. The canonical source gained
  one pronoun — the curator's exit says terminal/finalizer evidence attests only that **this** turn
  ended — and this card's Logic describes the curator/manager job split and the three fed inputs, not
  the completion-truth wording, so nothing in the body asserts the sentence that moved. Reviewed
  against the change set and deliberately left as written rather than reworded to match a one-word
  diff. **Repaired in the same pass (D16):** this card's `governingOverview` field and link pointed five
  levels up, at `onboarding/mcp/src/agents_remember/overview.md`, which does not exist — the card's own
  link text says "MCP package overview", which from `operations/` is **seven** levels up. Both now
  resolve to `onboarding/mcp/overview.md`. Verification metadata moves to this leaf's synced base
  `8997e184`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code
  commit and no hash or fingerprint was invented here.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/operations/curation.md` — a file added by the role-instruction corpus consolidation. The canonical source is an operation-scoped procedure block extracted from interleaved role prose (curation).; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
