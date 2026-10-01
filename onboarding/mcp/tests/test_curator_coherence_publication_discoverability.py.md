# mcp/tests/test_curator_coherence_publication_discoverability.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The module's own statement of the property, and of its place in the split. [1]
- **The one declaration: nine members in the request model's own order, the first two flagged caller-supplied.** [2]
- The member record the declaration is built from. [3]
- **The refusal that names the missing members, and the text `prepare` renders from the same declaration.** [4]
- The request model whose field order the positive control compares against. [5]
- The two content members that are publication inputs but not among the nine. [6]
- The shipped action entry point, and the `prepare` branch whose text the cases read. [7]
- The module's own mirrors of the declaration, of a full request, and the three helpers that turn a request into the refusal's detail. [8]
- **The one stubbed boundary: the real `prepare` over a stubbed observation, so the asserted summary is the one a caller receives.** [9]
- One member omitted alone, and all nine omitted, in declaration order. [10]
- The positive control: the declaration is the model's own field order, with the content members named from the module's constants. [11]
- **The `prepare` case: all nine names in order, the judgments phrase, and the two identities echoed as not derived.** [12]
- **The added-member case: one declaration edit reaches the refusal and the text, with neither text touched.** [13]
- The non-publish refusals, by name and in model order, and the freeze branch's preserved message. [14]
- The module this one was split out of, which keeps the Gate-5 orchestration and the shared scaffold. [15]
- The lane row this module was appended to. [16]

### Cross-Repo References

No cross-repository behavior is implemented or measured in this file. Every case drives this
repository's own model and publication route over a stubbed observation.

No meaningful cross-repo references found.
