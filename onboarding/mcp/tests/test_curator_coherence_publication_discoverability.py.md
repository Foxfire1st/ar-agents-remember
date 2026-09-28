# mcp/tests/test_curator_coherence_publication_discoverability.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_curator_coherence_publication_discoverability.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T05:30:43+00:00 |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28`|
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The `KS-R24@v1` lane: **the curator-coherence request states its own publication inputs.** `publish`
requires nine request members, and a caller could previously discover which ones only by reading the
validator — `semantic_requirement_revision` and `delivery_attempt` defaulted to `None` (so they
looked optional), `prepare` never echoed them, and the refusal named none of them. Two leaves
recorded the authority as unpublishable when it in fact publishes fine.

These cases pin **every refusal to the request member it is about** and the `prepare` text to the one
declaration the model, the validator and the text all read, so the input set is discoverable from
the tool's own answers rather than from its source.

**The module is also the second half of the L23 split**, and the split was made on properties rather
than on line count. `mcp/tests/test_final_full_memory_coherence_certification.py` protects the Gate-5
final-certification orchestration *and* owns the shared fixture scaffold its sibling modules import;
these cases protect publication discoverability. The two are different subjects that happened to
share one file at 1199 of the repository's 1200-line hard limit, and each half still asserts exactly
what the whole file asserted before the split — measured by collected node identity, not by line
count.

## Code Commentary

### Logic

**The authority is one declaration.** `PUBLICATION_MEMBERS`
(`mcp/src/agents_remember/models/lifecycles/curator_coherence.py:320-332`) is a tuple of nine
`PublicationMember` records (`:306-317`) in the request model's own field order, carrying the
`caller_supplied` flag on the first two. The validator refuses on it, `publication_refusal`
(`:360-384`) names what is missing from it, and `publication_input_statement` (`:393-418`) is the
text `prepare` renders — so a member added to the declaration needs no second edit anywhere, which
is what one case measures rather than asserts.

**`_PUBLICATION_INPUT_NAMES` (`:55-65`) and `_MEMBER_VALUES` (`:67-80`) are the module's own
mirrors** of the declaration and of a request carrying every member. `_publication_request` (`:92-95`)
composes the full request before overrides, `_refusal_message` (`:98-101`) returns
`errors()[0]["msg"]` from `CuratorCoherenceRequest.model_validate`, and `_missing_detail` (`:104-108`)
strips the shipped opening sentence — asserted present first, so a refusal that dropped it fails here
rather than silently matching. The docstring on the first case records why the assertion reads the
detail rather than whole-message substrings: the shipped opening sentence contains "caller" as prose
and the required callout contains "caller-supplied", so a substring search cannot tell those from a
reported member.

The eight cases (18 collected items, because three are parametrized):

| Case | What it pins |
| --- | --- |
| `test_publish_refusal_names_the_one_missing_publication_member` (`:145-162`, 9 items) | each member omitted **alone** is named, and the two caller-supplied ones carry the extra sentence *"… is a caller-supplied delivery identity prepare does not derive -- supply it in the request."* |
| `test_publish_refusal_without_any_member_names_all_nine_in_declaration_order` (`:165-175`) | all nine omitted: the detail is the declaration order plus the two-member callout — the case that fails if the order drifts |
| `test_publish_with_every_publication_member_validates` (`:178-201`) | the positive control. Asserts the declaration equals the model's own field order (`declared == _PUBLICATION_INPUT_NAMES == model_order`) with the content members named from the module's own constants, so a field added to the model that is neither declared nor named in the exclusion set fails here |
| `test_prepare_states_the_complete_publication_input_set` (`:204-217`) | the real `_prepare` text: the judgments phrase, all nine names in order, the delivery-identity callout, and `semanticRequirementRevision`/`deliveryAttempt` echoed as `None` |
| `test_a_member_added_to_the_declaration_reaches_both_messages` (`:220-240`) | the declaration is extended and a scratch request model declares the matching field; the new member reaches **both** the refusal and the `prepare` text with neither text edited |
| `test_non_publish_actions_name_the_publication_member_they_received` (`:243-256`, 3 items) | `status`/`prepare`/`validate` refuse a publication-only field **by name** |
| `test_non_publish_refusal_names_every_supplied_field_in_model_order` (`:259-273`) | several supplied fields are named in **model order**, `judgments` included |
| `test_freeze_snapshot_keeps_its_own_named_refusal` (`:276-283`) | the freeze branch keeps the message it already had — the fix may not flatten a named refusal into the generic one |

**`_prepared_payload` (`:111-142`) is the only stubbed boundary, and it is stubbed at the observation
rather than at the text.** `mock.patch.multiple` replaces `observe_curator_coherence_source`,
`current_curator_coherence_predecessor` and `curator_coherence_paths` in
`curator_coherence_publication`, then calls the shipped `curator_coherence_action(contract,
CuratorCoherenceRequest(action="prepare", …))`. `_prepare` owns the shipped text, so the summary the
case asserts is the one a caller receives — a change to the text is measured, not bypassed.

### Conventions

The module imports the production declaration rather than a copy (`PUBLICATION_MEMBERS`,
`PublicationMember`, `publication_input_statement`, `JUDGMENTS_MEMBER`, `REVIEW_ASSESSMENTS_MEMBER`,
`CuratorCoherenceRequest`), and the two content-member names are used as constants so the exclusion
set and the shape validator that refuses them cannot drift apart. `_CONTRACT_PATH` (`:52`) is a real
enclosure-shaped path, and `_REFUSAL_PREFIX` (`:53`) is asserted before being stripped. The module
carries **no `pytestmark`**; its lane row was **appended** to the end of `unit-regression` in
`mcp/tests/test-evidence-lanes.toml:194`. It imports only `agents_remember` models, `pydantic` and
`pytest`, so it is **not** a consumer of any governed support module and owes no
`evidence-lifecycle.toml` row — measured with the oracle's own derivation, not assumed.

### Invariants And Boundaries

- **One declaration is the authority.** A member added to the request model without a matching
  `PublicationMember` fails the positive control; a member added to the declaration reaches both
  messages without a second edit.
- **A refusal names the member it is about**, never the whole set when one member is missing, and
  never a substring that merely contains the member's name.
- **The two caller-supplied identities are called out** because `prepare` cannot derive them — the
  sentence is part of the contract, asserted with its exact text.
- **The freeze branch's own refusal is preserved.** `only publish may freeze an immutable attempt
  snapshot` is asserted verbatim, so a future consolidation cannot absorb it.
- **Boundary.** This is a test module. It owns no production contract, adds no support module (a
  second non-`test_` module under `mcp/tests` would be governed evidence requiring lifecycle
  metadata), and therefore moves no catalogue count.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the property, and of its place in the split. | "The curator-coherence request states its own publication inputs" | mcp/tests/test_curator_coherence_publication_discoverability.py:1-14 |
| **The one declaration: nine members in the request model's own order, the first two flagged caller-supplied.** | `PUBLICATION_MEMBERS` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:351-361 |
| The member record the declaration is built from. | `PublicationMember` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:333-345 |
| **The refusal that names the missing members, and the text `prepare` renders from the same declaration.** | `publication_refusal`; `publication_input_statement` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:388-412; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:421-446 |
| The request model whose field order the positive control compares against. | `CuratorCoherenceRequest` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:449-529 |
| The two content members that are publication inputs but not among the nine. | `JUDGMENTS_MEMBER`; `REVIEW_ASSESSMENTS_MEMBER` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:365-365; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:371-371 |
| The shipped action entry point, and the `prepare` branch whose text the cases read. | `curator_coherence_action`; `_prepare` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:93-103; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:150-165 |
| The module's own mirrors of the declaration, of a full request, and the three helpers that turn a request into the refusal's detail. | `_PUBLICATION_INPUT_NAMES`; `_MEMBER_VALUES`; `_publication_request`; `_refusal_message`; `_missing_detail` | mcp/tests/test_curator_coherence_publication_discoverability.py:55-65; mcp/tests/test_curator_coherence_publication_discoverability.py:67-80; mcp/tests/test_curator_coherence_publication_discoverability.py:92-95; mcp/tests/test_curator_coherence_publication_discoverability.py:98-108 |
| **The one stubbed boundary: the real `prepare` over a stubbed observation, so the asserted summary is the one a caller receives.** | `_prepared_payload` | mcp/tests/test_curator_coherence_publication_discoverability.py:111-142 |
| One member omitted alone, and all nine omitted, in declaration order. | `test_publish_refusal_names_the_one_missing_publication_member`; `test_publish_refusal_without_any_member_names_all_nine_in_declaration_order` | mcp/tests/test_curator_coherence_publication_discoverability.py:145-162; mcp/tests/test_curator_coherence_publication_discoverability.py:165-175 |
| The positive control: the declaration is the model's own field order, with the content members named from the module's constants. | `test_publish_with_every_publication_member_validates` | mcp/tests/test_curator_coherence_publication_discoverability.py:178-201 |
| **The `prepare` case: all nine names in order, the judgments phrase, and the two identities echoed as not derived.** | `test_prepare_states_the_complete_publication_input_set` | mcp/tests/test_curator_coherence_publication_discoverability.py:204-217 |
| **The added-member case: one declaration edit reaches the refusal and the text, with neither text touched.** | `test_a_member_added_to_the_declaration_reaches_both_messages` | mcp/tests/test_curator_coherence_publication_discoverability.py:220-240 |
| The non-publish refusals, by name and in model order, and the freeze branch's preserved message. | `test_non_publish_actions_name_the_publication_member_they_received`; `test_non_publish_refusal_names_every_supplied_field_in_model_order`; `test_freeze_snapshot_keeps_its_own_named_refusal` | mcp/tests/test_curator_coherence_publication_discoverability.py:243-256; mcp/tests/test_curator_coherence_publication_discoverability.py:259-273; mcp/tests/test_curator_coherence_publication_discoverability.py:276-283 |
| The module this one was split out of, which keeps the Gate-5 orchestration and the shared scaffold. | "Split from ``test_final_full_memory_coherence_certification.py``" | mcp/tests/test_final_full_memory_coherence_certification.py:1-19 |
| The lane row this module was appended to. | "mcp/tests/test_curator_coherence_publication_discoverability.py" | mcp/tests/test-evidence-lanes.toml:238-238 |

## Cross-Repo References

No cross-repository behavior is implemented or measured in this file. Every case drives this
repository's own model and publication route over a stubbed observation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-28T17:15:39+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`) were re-pointed to where the same anchors now sit; each re-pointed row held its anchors at the base and holds them after the base-to-candidate line mapping. Claim wording unchanged. No stamp advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T16:25:39+02:00 — 260921-ICR-L42 curator: No content impact: re-pointed this card's citations into `test-evidence-lanes.toml` after this leaf's line insertions (candidate tree `27409ea9f3320689c28c6a810c9a88afa288bbba` over code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`). Each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): No content impact: citation ranges into files this leaf changed (`dashboard/src/data/review.ts`, `dashboard/src/panels/review/SourceContent.test.tsx`, `mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_knowledge_review_source_content.py`) were re-pointed to where the same anchors now sit, each row checked valid at the base, invalid at the candidate, and valid after the base-to-candidate line mapping; claim wording unchanged. No stamp advanced.

- 2026-09-27T05:30:43+00:00 — Authored scoped citation maintenance for 3 L41 source-range projection(s) resolved by the frozen source index. Only changed-source ranges were adopted from the preview; unrelated ranges, generated history and verification stamps are preserved.

- 2026-09-27T05:23:46+00:00 — Re-resolved 5 source-linked citation claim(s) against the extracted or shifted L41 owners. Each selected symbol uses its current declaration extent; other source references and prior generated history remain unchanged. Verification stamps remain closeout-owned.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "mcp/tests/test_curator_coherence_publication_discoverability.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T19:16:12+00:00: Generated citation repair: "mcp/tests/test_curator_coherence_publication_discoverability.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: "mcp/tests/test_curator_coherence_publication_discoverability.py" repointed to mcp/tests/test-evidence-lanes.toml:200-200. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_curator_coherence_publication_discoverability.py" repointed to mcp/tests/test-evidence-lanes.toml:195-195. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:11+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): created this one-to-one card for the second half of the L23 module split. It records the property the cases protect (publication discoverability, `KS-R24@v1`), the single declaration the validator, the refusal and the `prepare` text all read, the eight cases with what each pins, and the one stubbed boundary — the observation behind the real `prepare`, so the asserted summary is the caller's — plus the fact that the split was made on properties rather than line count and that nothing was deleted or renamed in the move. It also records that the module is not a governed-support consumer and so owes no catalogue row. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate. What was read is this leaf's uncommitted working tree, and closeout owns the stamp.
