# mcp/tests/test_final_full_memory_coherence_certification.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_final_full_memory_coherence_certification.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T19:12+02:00|
| lastVerifiedCommitHash | `7879f5b22c34a912f939e27868786818463c3b9c` |
| lastVerifiedCommitDate | 2026-09-19T20:18:09+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `overview.md` |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The scenario builds the configured disposable code/memory pair. | "def _scenario(" | mcp/tests/test_final_full_memory_coherence_certification.py:444-483 |
| The affected-plan fixture selects the selected mode for the scenario. | "def _affected_plan(" | mcp/tests/test_final_full_memory_coherence_certification.py:788-794 |
| The coherence fixture binds the exact candidate pair and memory inputs. | "def _coherence(" | mcp/tests/test_final_full_memory_coherence_certification.py:807-838 |
| The evidence builder composes the exact pair, plan, prefix and check authorities. | "def _evidence(" | mcp/tests/test_final_full_memory_coherence_certification.py:867-894 |
| The green certification binds the exact memory tree, pair authority, and Gate-5 inputs. | `test_final_certification_green_binds_exact_pair_and_gate_five_inputs` | mcp/tests/test_final_full_memory_coherence_certification.py:897-913 |
| A red final certification blocks finalization. | "def test_final_certification_red_blocks_finalization(" | mcp/tests/test_final_full_memory_coherence_certification.py:916-926 |
| **The single declaration the moved publication-input cases assert on, and the two members `prepare` does not derive.** Those cases now live in `mcp/tests/test_curator_coherence_publication_discoverability.py`. | `PublicationMember`; `PUBLICATION_MEMBERS` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:298-310; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:316-326 |
| **The refusal every omission case drives, and the statement the prepare case drives — both now asserted from the new module.** | `publication_refusal`; `publication_input_statement` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:353-377; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:386-411 |
| The suite's own row in the evidence manifest, inside `unit-regression`. | "mcp/tests/test_final_full_memory_coherence_certification.py" | mcp/tests/test-evidence-lanes.toml:68-68 |
| The scenario builds the configured disposable code/memory pair. | "def _scenario(" | mcp/tests/test_final_full_memory_coherence_certification.py:433-472 |
| The affected-plan fixture selects the selected mode for the scenario. | "def _affected_plan(" | mcp/tests/test_final_full_memory_coherence_certification.py:788-788 |
| The coherence fixture binds the exact candidate pair and memory inputs. | "def _coherence(" | mcp/tests/test_final_full_memory_coherence_certification.py:796-827 |
| The evidence builder composes the exact pair, plan, prefix and check authorities. | "def _evidence(" | mcp/tests/test_final_full_memory_coherence_certification.py:856-883 |
| The green certification binds the exact memory tree, pair authority, and Gate-5 inputs. | `test_final_certification_green_binds_exact_pair_and_gate_five_inputs` | mcp/tests/test_final_full_memory_coherence_certification.py:886-902 |
| A red final certification blocks finalization. | "def test_final_certification_red_blocks_finalization(" | mcp/tests/test_final_full_memory_coherence_certification.py:916-916 |
| The same manifest row, which is the module's lane registration. | "mcp/tests/test_final_full_memory_coherence_certification.py" | mcp/tests/test-evidence-lanes.toml:68-68 |
| The second half of the L23 split, which now owns the publication-input cases this card used to describe. | "The curator-coherence request states its own publication inputs" | mcp/tests/test_curator_coherence_publication_discoverability.py:1-14 |

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

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: "def _affected_plan(" repointed to mcp/tests/test_final_full_memory_coherence_certification.py:788-788. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "def test_final_certification_red_blocks_finalization(" repointed to mcp/tests/test_final_full_memory_coherence_certification.py:916-916. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:12+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **re-read this card against the module `260915-KS-L23` item 9 split, and corrected three statements the split (and the tree) had falsified.** (1) The Purpose paragraph named `test_final_gate_prefix_adapter` and `test_final_catalog_readiness_projection` as sibling importers; **neither module exists in this tree** — `test_final_catalog_plan_attestation` is the only importer, which is also why the scaffold stayed here. (2) The card stated the suite is registered in the **`integration`** lane; measured, its single row is `mcp/tests/test-evidence-lanes.toml:69`, inside **`unit-regression`** (the `integration` list begins at `:201`, and only `integration`/`stress-durability` members are marked `pytest.mark.integration`, `mcp/tests/conftest.py:89-130`). The two reference rows that carried the false lane claim were corrected in place, not removed. (3) The `KS-R24@v1: The Publication Input Cases` section described 18 items that **moved out** to `mcp/tests/test_curator_coherence_publication_discoverability.py`; it is replaced by the split's own record — the two subjects, the line counts (954 + 283 against 1199 before), the fact that the scaffold stayed so the sibling's import still resolves, the empty `diff` of **23** collected node names across the two halves, and the fact that no `[[contract]]`/`[[artifact]]` row was added because no non-`test_` module was created. The KS-R15 section records that the content-member assertion moved with the cases and now asserts at the new module's `:201`. **No `lastVerifiedCommitHash`/`lastVerifiedCommitDate` was advanced**: the split exists only in this leaf's uncommitted candidate, so no commit carries the bytes a stamp would claim — the `reviewedWorkingCandidate` row states what was actually read and closeout owns the stamp. The pre-existing reference rows whose cited ranges the split and the earlier insertions moved were **left to the citation-repair engine** (its class, and its designated owner) rather than hand-rewritten here.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_final_full_memory_coherence_certification.py" repointed to mcp/tests/test-evidence-lanes.toml:69-69. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_final_full_memory_coherence_certification.py" repointed to mcp/tests/test-evidence-lanes.toml:69-69. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_final_full_memory_coherence_certification.py" repointed to mcp/tests/test-evidence-lanes.toml:68-68. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "def _affected_plan(" repointed to mcp/tests/test_final_full_memory_coherence_certification.py:790-790. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "def test_final_certification_red_blocks_finalization(" repointed to mcp/tests/test_final_full_memory_coherence_certification.py:918-918. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_final_full_memory_coherence_certification.py" repointed to mcp/tests/test-evidence-lanes.toml:68-68. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/src/agents_remember/models/lifecycles/curator_coherence.py:260-288` -> `mcp/src/agents_remember/models/lifecycles/curator_coherence.py:298-310; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:316-326`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-18T03:20+02:00 — 260915-KS-L24 curator (uncommitted change set on `ar/260915-ks-l24`, base `9c12e8b1`): **re-read this card against the module the leaf grew and recorded the 18 publication-input cases.** The leaf inserted three import lines below the top of the module and a 236-line section at its end, so every scaffold coordinate this card carried was nine to eleven lines low — `_inline_profile` is `169-249`, `_scenario` `444-483`, `_r07_candidate` `635-686`, `_r07_admission` `742-771`, `_affected_plan` `788-794`, `_coherence` `807-838`, `_evidence` `867-894`, and the five module-level tests `897-913` / `916-926` / `929-936` / `939-944` / `947-954`; the Logic section and the reference table now carry the measured extents, and the two mechanical generated bullets for `"def _affected_plan("` and `"def test_final_certification_red_blocks_finalization("` are retired here because this pass re-read and re-cited those rows itself. A new subsection states what the 18 cases protect and why a message is the requirement, and records the module's position against the 1200-line rail (**1190**), so the next leaf that adds curator-coherence cases here knows it must split first. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_final_full_memory_coherence_certification.py" repointed to mcp/tests/test-evidence-lanes.toml:66-66. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_final_full_memory_coherence_certification.py" repointed to mcp/tests/test-evidence-lanes.toml:57-57. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T01:06:15+00:00: Generated citation repair: "mcp/tests/test_final_full_memory_coherence_certification.py" repointed to mcp/tests/test-evidence-lanes.toml:54-54. No content impact: mechanical anchor-range projection bound to citation source snapshot 1740540b8733028dd833a3538d739271e8925ea5f51911a0f8dcd8c49e7e1c13; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "mcp/tests/test_final_full_memory_coherence_certification.py" repointed to mcp/tests/test-evidence-lanes.toml:52-52. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T02:43:28+02:00 — CCR-L38 bounded inherited citation repair: repointed the evidence-lane membership citation to the current member line 50; source-sha256=0aff0c8665ee76c3ca934460b5d85f55b0e80d85018a9465b40d43c1746284bc; verification metadata remains unchanged.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=d579fd361edd77aa2bf16f4319ed154ee6fcb5cc9ec5d710e8a960e553f384da; verification metadata remains unchanged because commit-owned realization is pending.

- 2026-09-08T18:14:20+02:00 — CCR-L24 bounded memory-quality repair: re-read the evidence-lane registration and corrected its current line; verification metadata remains pinned.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `test_final_certification_green_binds_exact_pair_and_gate_five_inputs` repointed to mcp/tests/test_final_full_memory_coherence_certification.py:886-902. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-06T22:41:21+00:00: Generated citation repair: "mcp/tests/test_final_full_memory_coherence_certification.py" repointed to mcp/tests/test-evidence-lanes.toml:50-50. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T04:32:25+00:00 — L32 incoming-evidence curation: verified the exact cited lane member or current test-function owner against private C b34f4a59 and corrected only its moved coordinates. Existing own-source verification provenance is retained.

- 2026-09-06T00:42:13+00:00 — Gate-5 citation repair: re-read the cited evidence-lane member and its declared classification and corrected its incoming range. Existing source verification provenance is retained.

- 2026-09-05T07:12:23Z — CCR L31 independent-review correction: reread the passing-check
  dictionary builder, evidence fixture and actual library calls at ea359649. Qualified the
  suite's scope as library composition with synthetic authorities, preserved its registered
  lane and useful behavior checks, and removed the unsupported end-to-end execution claim.

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: created this file-level
  onboarding card for the new CCR-R08 final full memory-coherence certification forcing suite
  delivered in code commit 16d1a4d6; anchors and ranges derived from the current worktree source
  and pinned to that commit. The suite entered the `integration` lane of
  `test-evidence-lanes.toml` in the same change.
