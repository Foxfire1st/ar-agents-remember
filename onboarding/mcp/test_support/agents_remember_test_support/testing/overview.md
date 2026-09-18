# Python Test Evidence Infrastructure Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/test_support/agents_remember_test_support/testing` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-28T10:16:27+02:00 |
| lastVerifiedCommitHash | `a29a20c6eefea424a7e0321a54fcda2ed1b35098`|
| lastVerifiedCommitDate | 2026-09-17T14:23:47+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Python verification infrastructure](../overview.md)

## What This Area Is

Repository-owned pytest isolation and evidence infrastructure. Ordinary pytest bootstrap and
certifying startup are distinct: `pytest_bootstrap.py` owns deterministic ordering, isolated caches
and restoration of owned mutable state, while `certifying_bootstrap.py` requires Dagger admission
before preparing a certifying candidate process. Ordinary bootstrap does not grant certification or
external-service capability.

## Hot Path Summary

`dependency_facts.py` and `consumer_inventory.py` derive import/plugin/consumer ownership from
current source. `lane_manifest.py` and `evidence_lanes.py` validate the explicitly declared evidence
population. `evidence_lifecycle.py` validates catalog ownership, lifetime, real contract nodes and
observed consumers; `evidence_governance.py` owns artifact discovery.

`candidate_snapshot.py` and `evidence_provenance.py` bind generated artifacts to candidate and
machine facts. `retry_selection.py` observes canonical collection and admits only the explicit
affected module population. `causal_dependency.py` and `causal_failures.py` retain the exact-node
causal evidence boundary. `cadence_runner.py` and `pytest_phase_reporter.py` own their retained
execution/reporting adapters. The former route-measurement and causal-route matrix modules are
retired; their old measured populations are historical evidence, not current route obligations.

## Operating Model

Use the ordinary bootstrap for its declared local pytest responsibilities. Certifying entry uses
`prepare_certifying_pytest_bootstrap`, which proves the Dagger capability before candidate setup.
Neither route's mere execution supplies acceptance. The retained lane, lifecycle and dependency
validators describe current source and configured evidence; they do not require reconstruction of
removed test matrices or older source/test censuses.

## Local Invariants And Traps

- Ordinary pytest setup has no certifying or external-service authority. Dagger admission remains
  mandatory at the certifying composition boundary.
- Owned mutable module state is restored after each test; a leak is reported rather than silently
  accepted. Seeded ordering uses a local RNG and does not perturb the process-global RNG.
- Literal plugin/import relationships are source facts. Unknown dynamic ownership cannot be
  promoted to an exact dependency claim.
- Explicit lane membership and discovered evidence catalog coverage remain exact; missing,
  stale or conflicting declarations are findings.
- Retry selection accepts only explicit affected modules whose collection was observed. It never
  expands execution silently to repair missing ownership.
- Causal suppression requires exact independently supported nodes. Reports and candidate/machine
  provenance do not become certification merely because the tool ran in Dagger.
- Coverage is diagnostic and retired matrix populations are not restoration requirements. Full
  suites and aggregate review belong to the master completion route.

## File-Level Onboarding Map

The generated route index inventories the surviving source owners and their paired cards.
It must be rebuilt from current source, never copied from a retired route census.

## Source References

| Finding | Anchor | Source |
| --- | --- | --- |
| Ordinary bootstrap owns local ordering/cache/state isolation without certification. | "Reusable pytest bootstrap with no certifying or external-service capability." | mcp/test_support/agents_remember_test_support/testing/pytest_bootstrap.py:1-1 |
| Certifying setup admits Dagger before candidate preparation. | `prepare_certifying_pytest_bootstrap` | mcp/test_support/agents_remember_test_support/testing/certifying_bootstrap.py:27-39 |
| Retry execution retains exact explicit affected modules. | `pytest_collection_modifyitems` | mcp/test_support/agents_remember_test_support/testing/retry_selection.py:63-79 |

## 260915-CAPS-L18 Complete Curation Reaches This Route

This route gained `curation_doctrine.py`, the retired-sentence registry and required-rule table the
shipped-corpus guard reads. CAPS-R18@v1 inverted the optional/narrow-curation doctrine in the shipped instruction sources. The
sentences that presented the full `memory_quality_check` operation and the `curator_coherence`
certification as developer-request-only diagnostics, "never routine closeout/integration prerequisites",
are gone. The rule is now normative: **curation is complete on every leaf** — the full operation runs at
the leaf's contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every
curator-actionable finding is repaired or escalated as blocked with its exact returned code, and the
operation is re-run after every repair until `curatorActionableCount=0` and the **raw**
`qualityChecklistStatus=ready-for-closeout`. The **combined** `checklistStatus` is rewritten to
`coherence-required` **only when the coherence record is then missing or stale** — that is the coherence
gate, cleared by publishing the `curator_coherence` authority with `prepare` → `publish` → `validate`.
On the success path, where the record is already current, the combined field is **not rewritten** at all
and keeps its incoming `ready-for-closeout` value, with `closeoutReady=true`; `ready-for-closeout` is
therefore observable in the combined field once the whole pipeline is already complete. **Field-name
correction (`D35`, made by 260915-CAPS-L10):** this sentence previously named
`checklistStatus=ready-for-closeout` as the loop's termination condition; read the raw field to end the
loop and the combined field to decide the coherence gate
(`application/memory_quality/controller.py:664`, `:671`, `:678`, `:685-687`).

**Warrant corrected by `CAPS-R19` (leaf `260915-CAPS-L19`).** The `D35` correction above originally rested
on the sentence *"`ready-for-closeout` is never a value of the combined field."* That absolute claim is
**literally false**, and `CAPS-R19`'s revision note records it as superseded by the three-path model now
stated here. The field-name correction it supported still holds; only its stated warrant was wrong.
**Attribution is complementary and both halves hold:** `260915-CAPS-L10`'s curator corrected the
**onboarding cards** that carried the wrong form, while `CAPS-R19` corrected the **shipped sources** — the
five loop-gate carriers, their nine generated copies, and the guard registry's own docstring — and brought
`docs/reference/mcp-tools.md` into both the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`.

**And on this route the wrong field name was not only in prose — it was pinned by the guard, and that
obstacle has since been repaired.** This route's `curation_doctrine.py` owns
`CURATION_COMPLETENESS_STATEMENTS`, the required-form table the shipped-corpus guard reads, and at the
base its `skills/l-01-agent-lifecycles/roles/curator.md` row **required** the fragments
`"curatorActionableCount=0"` and `"checklistStatus=ready-for-closeout"`.
`missing_completeness_statements` and `test_role_instruction_corpus.py::CurationIsCompleteOnEveryLeafTests::
test_every_canonical_source_states_the_complete_curation_rule` match those fragments on
`normalize_statement`'s reading, which strips emphasis and collapses whitespace but does **not** change
case. So a repair that rewrites the sentence to `qualityChecklistStatus=ready-for-closeout` removes the
lowercase-`c` fragment and turns the guard **red**. `D35`'s repair therefore had to move the declared
fragment with the sentence, in the canonical source and in this table together, or the guard would fail
on the repair itself.

**Repaired by `CAPS-R19` (leaf `260915-CAPS-L19`), verified in the code worktree at this leaf's tip.**
`260915-CAPS-L10` recorded this obstacle but did not repair it, because the table is code and that seat
writes onboarding only. `CAPS-R19` is the leaf that moved the fragment: the retired pairing is no longer
a *required* fragment anywhere in the table — it became the guard's own retired-form constant
`RETIRED_LOOP_GATE_FIELD_PAIRING` (`curation_doctrine.py:222`), paired with the positive
`LOOP_GATE_CORRECTED_FIELDS = ("qualityChecklistStatus", "closeoutReady")` (`:229`) now attached to the
`roles/curator.md`, `operations/curation.md` and `templates/curator-brief.md` rows. `LOOP_GATE_DOCUMENTS` became a **path → required-field-names
mapping** (`:237-240`, covering `docs/reference/drift-c02.md` and `docs/reference/mcp-tools.md`), and the
new reader `missing_loop_gate_statements` (`:382`) asserts the positive half inside the **existing**
census case `test_the_census_ranges_over_the_canonical_tree_and_every_generated_copy`
(`test_role_instruction_corpus.py:685`) — no case was added, so the unit case delta is 0. Re-inserting the
wrong pairing now reds the suite from three axes, measured by seeded experiment rather than asserted.

**What the guard still does not do, stated rather than implied:** it is a **fragment matcher** with a
declared blind spot — a wrong gate restated in fresh vocabulary that never writes the exact pairing is
invisible to it — and it does not read the running tool. Coverage of this leaf's subject is therefore
real but bounded, and no card may claim the guard catches every restatement.

Two corrections the inversion must not collapse, both preserved: closeout still owns only the Git
transaction and **invokes** nothing — it **carries** the completed curation as a prerequisite; and the
rule is about the completeness of curation, not about unscoped runs, so "complete" always means the whole
operation at the leaf's contract scope. The ruling is forward-looking: the already-landed and finalized
leaves are not re-curated, and whole-layer completeness is discharged by L11's full-scope run at the
frozen tip.

## Update History

- 2026-09-17T14:15+02:00 — 260915-CAPS-L19 curator: **Field-name warrant corrected — `ready-for-closeout` read as *never* a value of the combined `checklistStatus`.** That absolute sentence was written by 260915-CAPS-L10's curator as the warrant for this card's `D35` correction, and `CAPS-R19` (`260915-CAPS-L19`) measures it **literally false** (`application/memory_quality/controller.py:685-687` leaves the combined field at its incoming `ready-for-closeout` value on the success path, with `closeoutReady=true`). The card now states the three-path model instead: the raw `qualityChecklistStatus` is the repair loop's gate; the combined `checklistStatus` is rewritten to `coherence-required` **only when the coherence record is then missing or stale**; and `closeoutReady` becomes true only once that validation passes. Corrected under `CAPS-R19`'s revision note (2026-09-17T13:55), which is the authority for this change. The field-name correction itself stands and attribution is complementary — `260915-CAPS-L10` corrected the onboarding cards, `CAPS-R19` corrected the shipped sources (the five loop-gate carriers, their nine generated copies, the guard registry's docstring) and brought `docs/reference/mcp-tools.md` into the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`. The earlier entries below are left exactly as written: they record what L10 did, and this entry is the correction of their warrant. No verification stamp advanced — the candidate is uncommitted and the governed closeout owns the real commits. Also corrected the card's guard-obstacle paragraph, which L10 recorded as "not repaired": `CAPS-R19` **did** repair it — the retired pairing is no longer a required fragment, it is the guard's `RETIRED_LOOP_GATE_FIELD_PAIRING` (`curation_doctrine.py:222`) beside the positive `LOOP_GATE_CORRECTED_FIELDS` (`:229`) and the `LOOP_GATE_DOCUMENTS` mapping (`:237-240`), asserted by `missing_loop_gate_statements` (`:382`) inside the existing census case (`test_role_instruction_corpus.py:685`).
- 2026-09-17T13:45+02:00 — 260915-CAPS-L10 curator: **corrected a landed defect (`D35`) and recorded the obstacle its repair will hit on this route.** The `CAPS-L18` section now names the **raw** `qualityChecklistStatus` as the repair loop's gate and the combined `checklistStatus=coherence-required` as the coherence gate (`application/memory_quality/controller.py:664,671,678,687`). Added the source-backed statement that this route's `curation_doctrine.py::CURATION_COMPLETENESS_STATEMENTS` **requires** the fragment `"checklistStatus=ready-for-closeout"` for `roles/curator.md`, and that `normalize_statement` is case-preserving, so rewriting the sentence to `qualityChecklistStatus=…` would turn `test_every_canonical_source_states_the_complete_curation_rule` red unless the declared fragment moves with it. Recorded, not repaired — the table is code and this seat writes onboarding only.
- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: the complete-curation doctrine reaches this route. The canonical sources on this route now state that the full `memory_quality_check` operation is part of every leaf's curation, that a subset never stands in for it, and that closeout and integration carry the completed result as a prerequisite while invoking nothing. Body updated as above; no verification stamp advanced because the sources are uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-09T02:35:47+02:00 — CCR-L38 inherited route reconciliation: re-read this route's purpose, member inventory, route summary, and invariants against frozen candidate code tree `4c6b7bc2362bc03d50fc7a0643f34b591b805d45`; the candidate's changed paths are outside source route `mcp/test_support/agents_remember_test_support/testing`, so no route/member/prose/invariant change is required. route-member-count=20; source inspection only; verification metadata remains unchanged pending producer-owned realization. No acceptance or certification claim.

- 2026-08-28T10:03:40+02:00 — Added the complete observed failure-family ownership split and the
  measured three-symptom causal repair protocol to the route hot path.
- 2026-08-28T04:37+02:00 — Retired Candidate-A host diagnostics, added threshold-aware evidence
  governance and shared provenance, and replaced pure-only route comparison with repeated
  pure/integration/durability serial/default-xdist measurement.
- 2026-08-27T22:09+02:00 — Recorded explicit `pytest SKIPPED` as the plan-only retry proof after
  the live matrix exposed a validator that incorrectly expected no result line.
- 2026-08-27T21:10+02:00 — Split observed zero-body module collection from genuinely
  missing/uncollected retry paths without adding a fallback.
- 2026-08-27T20:45+02:00 — Bound the product retry scenario to the low-fan-out seed owner after a
  central atomic-write mutation selected 486 test modules.
- 2026-08-27T20:12+02:00 — Recorded formatter-valid controlled retry mutations after the real
  product matrix exposed a pre-pytest harness defect.
- 2026-08-27T17:19+02:00 — Added the dependency-owned retry execution boundary: canonical
  collection restores current import evidence while only explicit affected modules execute.
- 2026-08-27T11:08+02:00 — Moved test infrastructure under verification ownership and reconciled
  explicit lanes, source-derived consumers, complete candidate binding, persistent retry, and
  exact-node causal evidence. Verification remains closeout-owned.
