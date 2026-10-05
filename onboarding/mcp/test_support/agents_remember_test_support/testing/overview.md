# Python Test Evidence Infrastructure Overview

## Merged curation doctrine assertion support

curation_doctrine keeps selected curator/reviewer assertions aligned with native role language and converted writer semantics. Shared test helpers are not execution or knowledge-verdict owners. Canonical instruction/mirror consistency uses its synchronization owner, and test qualification, completed curation, semantic acceptance and Git publication retain separate authority.

- Current imported source owns this scoped route boundary. [4]
- Current imported source owns this scoped route boundary. [5]

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/test_support/agents_remember_test_support/testing` |

## Governing Overview

[Python verification infrastructure](../overview.md)

## What This Area Is

Repository-owned pytest isolation and evidence infrastructure. Ordinary pytest bootstrap and
certifying startup are distinct: `pytest_bootstrap.py` owns deterministic ordering, isolated caches
and restoration of owned mutable state, while `certifying_bootstrap.py` requires Dagger admission
before preparing a certifying candidate process. Ordinary bootstrap does not grant certification or
external-service capability.

## Hot Path Summary

The imported native Paseo role route retains canonical task/workspace identity, exact launch/replay and independent model/effort/tier validation alongside the existing converted MIK memory and publication owners.

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

## Evidence

### Source References

- Ordinary bootstrap owns local ordering/cache/state isolation without certification. [1]
- Certifying setup admits Dagger before candidate preparation. [2]
- Retry execution retains exact explicit affected modules. [3]

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

## 260915-KS-L23 The Byte Pin And The Consumer Oracle Are Two Gates, And This Route Owns One Of Them

`testing/evidence_lifecycle.py` is where the repository's **consumer-completeness oracle** lives, and
the point of the L23 section is that a reader arriving here must be able to tell it apart from the
gate beside it. `D-19` measured the cost of the confusion: four green checks — the byte pin, pytest,
ruff, format and pyright — shipped a red governance gate, because nothing in them derives the
catalog's consumers from the source tree.

| Gate | Where it lives | The question it answers | Its documented repair |
| --- | --- | --- | --- |
| the catalog **byte pin** | `mcp/tests/test_dependency_ownership_ast_helpers.py`'s `LIFECYCLE_CATALOG_SHA256` / `LIFECYCLE_CONTRACT_COUNT` / `LIFECYCLE_ARTIFACT_COUNT` | *is this the exact catalog file that was measured?* — nothing in the source tree can redden it | a re-pin, after the catalog edit was reviewed |
| the **consumer oracle** | this route's `load_evidence_inventory` | *does the catalog agree with the source tree it describes?* — it derives the dependency graph and requires every `consumer_scope = "exact"` artifact's declared `consumers` to equal the test modules that actually reach it | a registry row — which is *why* the pin moves afterwards |

The oracle's module docstring (`evidence_lifecycle.py:1-19`) was rewritten in this leaf to name both
gates and each one's repair, and the case that shows the distinction as a measurement rather than a
claim is `mcp/tests/test_evidence_catalog_gate_boundaries.py` — one catalog edit, in one run, where
the oracle refuses the tree and the pinned catalog's bytes and populations are unchanged.

**The class this route pays for on every landing, stated so the next leaf does not relearn it.** A
test module that starts or stops importing a governed support module changes its artifact's
consumer proof **without touching the catalog**, so the oracle reddens and the repair is a registry
row (after which the closing stamp moves the pin). This leaf obliged **four** such rows — three for
its two governed-support consumers and one that the item-16 case itself created by reading the lane
manifest — while the catalogue's populations stayed at **15 contracts / 65 artifacts** and the
digest moved to `25b00f88...`, because a consumer-only change moves the bytes and not the counts.
