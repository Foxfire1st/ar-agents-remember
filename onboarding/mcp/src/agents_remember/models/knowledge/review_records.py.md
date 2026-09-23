# mcp/src/agents_remember/models/knowledge/review_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T21:25:00+02:00 |
| lastVerifiedCommitHash | `972b44cc07b307929535fe7974d6a30d53c9c4f1` |
| lastVerifiedCommitDate | 2026-09-23T07:48:19+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The record-collection availability vocabulary one review's composition reports** (`ICR-R14@v1`):
which collections a review supplies, which states one collection's availability can be in, and the
value that carries one collection's answer. It exists as its own module for two reasons, and only one
of them is size: the vocabulary is a **contract of its own** — the record owner
([`application/review_evidence_records.py`](../../application/review_evidence_records.py.md)) resolves
it, the evidence pane carries it, and neither derives it from a collection's length — and its host
payload module had crossed the 900-line soft rail, so extracting it left
[`models/knowledge/review.py`](review.py.md) at 851 lines with the vocabulary re-exported rather than
duplicated.

**Availability is a fact per collection, and the five states are five different facts rather than one
empty tuple with a label:**

| State | What it means |
| --- | --- |
| `recorded` | the owner answered and supplied records of this class |
| `none_recorded` | the owner answered and holds none — a **measured zero** |
| `unavailable` | expected content that could not be read, carried with its provenance (absent, corrupt, refused, not yet established) |
| `not_measured` | a quantity nobody measured (dependency currentness) |
| `not_selected` | a collection this composition never read because the review selected no operand that would reach it |

The five are separate precisely so an empty tuple never has to stand for all of them — which is the
F09 defect this leaf removes: "the authority published none" and "the authority could not be read"
were the same empty list.

**The model refuses a favourable default structurally.** `ReviewRecordChannel`'s validator makes "a
count nobody measured" unrepresentable: a counted state must carry its count, an uncounted state may
**not** carry one (a `0` there would be read as a measured zero), `recorded` requires at least one
record and `none_recorded` requires exactly zero, and every uncounted state must state the next action
that would produce an answer. There is no state in this vocabulary that could be read as "nothing to
worry about", and no field for one.

## Code Commentary

### Logic

**`ReviewRecordClassName` names the collections by record class, not by pane.** The six members are
`assessments`, `detection_signals`, `verification_observations`, `authored_effects`, `evidence_claims`
and `assessment_currentness`. Naming them by class is deliberate: a collection's availability is a fact
about the **owner that produced the records**, and a reader needs the same fact whichever pane happens
to render them — signals are displayed in the knowledge pane, observations and claims in the evidence
pane, and both are read from the same bundle. The last member is not a collection at all but a
measurement, and it is listed here because a reader of the bundle needs its state beside the rest.

**`ReviewRecordChannelState` is the closed five-member vocabulary described above**, and the module
docstring states why each is a different fact.

**`ReviewRecordChannel` carries one collection's availability.** `records` and `state` are required;
`owner` is a non-blank reference to the operation that answered (so an absent or unreadable collection
names **which authority to look at** rather than which code path happened to run); `record_count` is
the number of records supplied and exists **exactly when** the owner answered — `None` is not a zero,
it is the absence of a count; `detail` is required and non-empty, because a state with nothing to say
is a silent gap; `unreadable` names the exact identities inside an otherwise-answered collection that
the composition could not serve, so one damaged record neither withdraws its siblings nor disappears;
and `next_action` is what would produce an answer, required for every state that is not an answer.

**The validator is the invariant, not a formality.** `_require_an_answer_to_carry_its_count` refuses
four shapes: a counted state without a count; an uncounted state **with** one (`"a count that is not an
answer"` — the shape a reader would mistake for a measured zero); `recorded` with no records (which is
what `none_recorded` is for); and `none_recorded` whose count is not zero. A fifth check requires a
non-blank `next_action` on every non-answered state. `_COUNTED_CHANNEL_STATES` is the one declaration
of which states are answers, so the validator and the projection cannot disagree about it.

### Conventions

`__all__` publishes exactly the three names: `ReviewRecordChannel`, `ReviewRecordChannelState` and
`ReviewRecordClassName`. The model is a `KnowledgeModel` (pydantic) like every wire shape, and it
travels on `ReviewEvidencePane.channels` in
[`models/knowledge/review.py`](review.py.md) — which also re-exports these three names, so existing
importers keep resolving through `models.knowledge.review` while the vocabulary lives in one place.
Bounds come from the shared declaration (`PROSE_MAX_LENGTH` for `detail` and `next_action`,
`REFERENCE_MAX_LENGTH` for `owner`) rather than being restated here. The module holds no state, reads
nothing and writes nothing.

### Invariants And Boundaries

- **Five states, five facts, and no favourable default among them.** An empty collection is never a
  clearance, and there is no member of this vocabulary that means "nothing to worry about".
- **A count exists exactly when an owner answered.** An unreadable authority has no count; a
  collection that was read and holds none reports a real zero.
- **A non-answer must state what would produce an answer.** A state a reader cannot act on is a silent
  gap, and the validator refuses it.
- **A damaged identity is named, not dropped.** `unreadable` is what keeps one damaged record from
  withdrawing its siblings and from vanishing silently.
- **Nothing here selects, measures or judges.** A channel reports what one owner's answer was; the
  owner pointer is a reference, not an authority this module exercises.
- **The vocabulary is declared once.** The record owner, the evidence pane and the served wire payload
  all reach it through these names; no caller re-spells the states.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in this module's own docstring, vocabulary and validator, in the
payload module that re-exports it and carries the resulting list, in the composition that resolves it,
and in the cases that measure both the vocabulary's refusals and the wire payload that carries it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what the vocabulary is, why it is its own module, and the five distinguishable facts. | "The record-collection availability vocabulary" | mcp/src/agents_remember/models/knowledge/review_records.py:1-12 |
| The published surface and the collections named by record class rather than by pane, with the reason spelled out. | `__all__`; `ReviewRecordClassName` | mcp/src/agents_remember/models/knowledge/review_records.py:26-45 |
| **The five-state vocabulary and why each state is a different fact rather than one empty tuple with a label.** | `ReviewRecordChannelState` | mcp/src/agents_remember/models/knowledge/review_records.py:47-63 |
| **The one declaration of which states are an owner's answer.** | `_COUNTED_CHANNEL_STATES` | mcp/src/agents_remember/models/knowledge/review_records.py:65-65 |
| **The channel value: the state, the owner that answered, the count that exists exactly when an answer does, the named unreadable identities and the next action.** | `ReviewRecordChannel` | mcp/src/agents_remember/models/knowledge/review_records.py:68-89 |
| **The validator that makes "a count nobody measured" unrepresentable — four refusals plus the required next action on every non-answer.** | `_require_an_answer_to_carry_its_count` | mcp/src/agents_remember/models/knowledge/review_records.py:91-123 |
| The shared bounds the model takes rather than restating. | `PROSE_MAX_LENGTH`; `REFERENCE_MAX_LENGTH` | mcp/src/agents_remember/models/knowledge/base.py:1-60 |
| **The payload module that re-exports the three names and carries the resulting list on the evidence pane.** | `ReviewRecordChannel`; `ReviewRecordChannelState`; `ReviewRecordClassName`; `ReviewEvidencePane`; `channels` | mcp/src/agents_remember/models/knowledge/review.py:49-49; mcp/src/agents_remember/models/knowledge/review.py:893-893; mcp/src/agents_remember/models/knowledge/review.py:50-50; mcp/src/agents_remember/models/knowledge/review.py:75-75; mcp/src/agents_remember/models/knowledge/review.py:51-51; mcp/src/agents_remember/models/knowledge/review.py:76-76; mcp/src/agents_remember/models/knowledge/review.py:918-958|
| **The composition that resolves every channel through the owner of each collection this vocabulary names.** | `_COLLECTION_OWNERS`; `_channel`; `ReviewRecordChannel` |mcp/src/agents_remember/application/review_evidence_records.py:128-135; mcp/src/agents_remember/application/review_evidence_records.py:808-819; mcp/src/agents_remember/application/review_evidence_records.py:778-778|
| **The cases that measure the vocabulary's own refusals and its presence in the served wire schema.** | `test_the_channel_model_refuses_a_count_no_owner_measured`; `test_the_wire_payload_carries_the_channels` | mcp/tests/test_knowledge_review_evidence_channels.py:761-787; mcp/tests/test_knowledge_review_evidence_channels.py:789-796 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It declares a payload vocabulary and touches
no boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-22T09:20:00+02:00 — 260921-ICR-L4 curator (gate repair pass on the merged line): **one enforced row re-cited.** The re-export row cited `models/knowledge/review.py:643-666` for the pane, which the six-counts and partition growth moved; it now cites `:665-701`. Wording unchanged; no stamp advanced.
- 2026-09-21T21:25:00+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): created this one-to-one card for the module this leaf introduced by **extracting the availability vocabulary out of `models/knowledge/review.py`**. The card records what the vocabulary is rather than only where it moved: the six collection names taken by record class rather than by pane (with the reason — availability is a fact about the owner, and one fact has to serve whichever pane renders the records); the five states and what each one distinguishes; and the validator that makes the defect's shape unrepresentable, since a state that measured no count may not carry one and every non-answer must say what would produce an answer. It also records the extraction's provenance: `models/knowledge/review.py` had crossed the 900-line soft rail (940 → 851), and the three names are **re-exported** from it so no importer had to learn a new home. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the **production line this reading was against** — `d80a0513e928ef29a973527d09597c82c96fde87`, the master line `ar/260921_complete-code-and-intent-review` at its current tip and this leaf's own base — because every construct cited here exists only in this leaf's uncommitted candidate and no commit contains the content a stamp would otherwise claim to have verified. That is a statement of what the reading was against, not a claim that these constructs exist in that commit; the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates, and that remains the real stamp.
