# mcp/tests/test_final_full_memory_coherence_certification.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

CCR-R08 forcing suite for the `certify_final_full_memory_coherence` library result assembly
(green, red, blocked, and typed refusal routes) over a synthetic exact candidate pair. The
suite supplies check-result dictionaries and modeled authorities; it does not drive real
memory scans, a closeout entrypoint, certificate publication or Git finalization. Per the
repository file-size-split convention (compare `test_author_execution_graph` importing from
`test_task_execution_topology`) this module also owns the shared Gate-5 fixture scaffold
consumed by its sibling `test_final_catalog_plan_attestation` — **the only importer that
exists**, measured at `260915-KS-L23`: `ls mcp/tests/test_final_*.py` lists
`test_final_catalog_plan_attestation.py`, `test_final_codex_certificate.py`,
`test_final_codex_models.py` and this module, and the two names an earlier revision of this
paragraph carried (`test_final_gate_prefix_adapter`,
`test_final_catalog_readiness_projection`) are not in the tree. The scaffold stays here rather
than in a second non-test module under `mcp/tests`, because such a module would be governed
evidence requiring lifecycle metadata.

**Lane, measured rather than remembered.** The suite's single row is
`mcp/tests/test-evidence-lanes.toml:69`, inside **`unit-regression`** — the `integration` list
does not begin until `:201`, and the loader marks only `integration` and `stress-durability`
members with `pytest.mark.integration` (`mcp/tests/conftest.py:89-130`). An earlier revision of
this card stated the `integration` lane; that statement was false against the manifest, and the
correction is recorded in this card's Update History.

## Code Commentary

### Logic

The scaffold builds a complete synthetic R21 chain from production model literals only (no
test-support module, no fixture-repo files): `_inline_profile` (169-249),
`_scenario` (444-483) compiles admission/plan/profile, `_green_prefix` (594-606)
compiles the exact green Gate 1-4 certificates, and the R07 affected-closure fixture builds the
same synthetic scope as the R07 leaf tests (`_r07_candidate` 635-686, `_r07_admission`
742-771, `_affected_plan` 788-794). `_pair` (802-804, the module-level factory), `_coherence` (807-838) and
`_passing_checks` (841-846) supply the remaining authorities, and `_EvidenceSpec`
(856-864) / `_evidence` (867-894) compose any scenario, including failing checks and
missing coherence.

The five module-level tests then pin result assembly:

- `test_final_certification_green_binds_exact_pair_and_gate_five_inputs` (897-913) - a green
  certification is finalization-eligible with a fully passing attestation, reused gates 1-4,
  and Gate-5 inputs bound to the exact memory tree and pair authority.
- `test_final_certification_red_blocks_finalization` (916-926) - a failing executed check or
  missing onboarding yields red, no Gate-5 inputs, and no finalization.
- `test_final_certification_blocked_when_full_only_rerun_not_consumed` (929-936) - the
  affected-closure item is blocked when the supplied full-only rerun flag is false.
- `test_final_certification_refuses_without_current_coherence` (939-944) -
  `gate-five-coherence-blocked`.
- `test_final_certification_refuses_stale_prefix_before_any_catalog_work` (947-954) - a code
  input change invalidates the prefix with `gate-five-prefix-invalidated` before any catalog
  work.

### `260915-KS-L23` Item 9: The Second Split, On Properties

The module reached **1199 of the repository's 1200-line hard limit** at `KS-R24@v1`, so item 9 of
`260915-KS-L23` split it a second time — along the **properties**, never along the line count, and
without deleting, renaming or re-scoping one case:

| Module | Protected property | Lines |
| --- | --- | --- |
| this module (kept) | the Gate-5 `certify_final_full_memory_coherence` orchestration (green / red / blocked / refusal) **and** the shared Gate-5 fixture scaffold its sibling imports | **954** |
| `mcp/tests/test_curator_coherence_publication_discoverability.py` (new) | `KS-R24@v1`: whether a caller can discover the curator-coherence request's publication inputs from the request, the refusal and the `prepare` text | 283 |

The 18 publication-input items this card used to describe — one parametrized case per omitted
publication member, the all-nine case in declaration order, the positive control that also asserts
the declaration is the request model's own field order, the real-`prepare` case, the added-member
case, the three parametrized `status`/`prepare`/`validate` items, the multi-field forbidden refusal
including `judgments`, and the unchanged `freeze_snapshot` message — **all moved to the new module
and are unchanged**; that module's own card carries them, and nothing here restates them.

**The scaffold stayed in the module whose name the sibling imports**, so
`from test_final_full_memory_coherence_certification import _CODE_TREE, _MEMORY_TREE,
_affected_plan, _coherence, _pair, _passing_checks` still resolves and no sibling import moved. **No
non-`test_` module was created**: a second support module under `mcp/tests` would be governed
evidence requiring lifecycle metadata, so the split adds no `[[contract]]` and no `[[artifact]]` row
and the catalogue's populations stay **15 / 65**.

**Both halves still assert what the whole did — measured by collected node identity, not by line
count.** The pre-split module was written to a scratch path from `git show HEAD:…`, both halves were
collected with `--collect-only -q -p no:randomly`, the node names after `::` were sorted on each
side, and `diff` of the two lists is **empty** over **23** case names. Two factual corrections were
made to this module's own docstring while splitting it: it named
`test_final_gate_prefix_adapter` and `test_final_catalog_readiness_projection` as importers, and
neither module exists in this tree.

### Conventions

Tests call the production library function with synthetic but byte-deterministic R21/R07
authorities and supplied check outcomes. The module adds `mcp/src` to `sys.path` so it can
run against the candidate package. This verifies library composition; the suite's
`unit-regression` lane classification does not establish production caller wiring or real checker
execution.

### Invariants And Boundaries

- The module is the shared fixture scaffold for its one existing sibling split module; it is the only
  Gate-5 test module importing the full certification internals.
- No test-support or fixture-module imports; the evidence-lifecycle catalog therefore records no
  transitive test-support consumer here.
- The evidence manifest assigns the suite to the integration lane. Its fixture chain exercises
  the R21/R07 typed library contracts, with modeled rather than producer-executed memory evidence.

### Todos

None.

## Evidence

### Repo-Internal References

- The scenario builds the configured disposable code/memory pair. [1]
- The affected-plan fixture selects the selected mode for the scenario. [2]
- The coherence fixture binds the exact candidate pair and memory inputs. [3]
- The evidence builder composes the exact pair, plan, prefix and check authorities. [4]
- The green certification binds the exact memory tree, pair authority, and Gate-5 inputs. [5]
- A red final certification blocks finalization. [6]
- **The single declaration the moved publication-input cases assert on, and the two members `prepare` does not derive.** Those cases now live in `mcp/tests/test_curator_coherence_publication_discoverability.py`. [7]
- **The refusal every omission case drives, and the statement the prepare case drives — both now asserted from the new module.** [8]
- The suite's own row in the evidence manifest, inside `unit-regression`. [9]
- The scenario builds the configured disposable code/memory pair. [10]
- The affected-plan fixture selects the selected mode for the scenario. [11]
- The coherence fixture binds the exact candidate pair and memory inputs. [12]
- The evidence builder composes the exact pair, plan, prefix and check authorities. [13]
- The green certification binds the exact memory tree, pair authority, and Gate-5 inputs. [14]
- A red final certification blocks finalization. [15]
- The same manifest row, which is the module's lane registration. [16]
- The second half of the L23 split, which now owns the publication-input cases this card used to describe. [17]

## KS-R15@v1 Content-Member Assertion Re-Scope

The shipped assertion that the declaration is the request model's own field order used to exclude an
inline literal set; this leaf's new content member `review_assessments` was neither declared nor
named, and the assertion failed. **That failure was correct** — it is designed to catch exactly an
unannounced field — and the repair strengthens rather than weakens it: the exclusion now names the two
content members from the module's own constants (`JUDGMENTS_MEMBER`, `REVIEW_ASSESSMENTS_MEMBER`) and
adds a disjointness assertion, so the case also fails if a content member is ever declared as one of
the nine required publication members.

**Capacity fact, now discharged rather than carried.** The file stood at **1199 of its 1200-line hard
limit** after the re-scope (1190 before; the change added 9 lines and recovered 1), with no headroom
left in it for this leaf or any leaf after it. `260915-KS-L23` item 9 is exactly the split that fact
called for: the publication-input cases moved to
`mcp/tests/test_curator_coherence_publication_discoverability.py` and this module now stands at
**954** lines. The assertion the paragraph above describes — that the declaration equals the request
model's own field order and is disjoint from the two content members — **moved with the cases** and is
asserted at `mcp/tests/test_curator_coherence_publication_discoverability.py:201`; it is recorded here
because the re-scope's history is this card's, and the case's current home is that one's.
