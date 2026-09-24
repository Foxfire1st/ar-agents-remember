# mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T09:05:00+02:00 |
| lastVerifiedCommitHash | `06ed70cfcde7e3860ee5b53435727e7512e4335c` |
| lastVerifiedCommitDate | 2026-09-24T10:53:01+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The vocabulary of a final-output receipt: the typed record that binds one comparison generation to the
output a task actually delivered.** `review_comparison_generation` records what a review *read*; normal
closeout and integration produce what the task *delivered*, and the packet's whole point (ICR-R21@v1) is
that the two are different facts. This module is the value alone — its owner, the selection rule, the
durable publication and the read-back are all
`agents_remember.application.review_final_output_receipt` — so a consumer can hold and validate a receipt
without importing the operation that produced it.

The separation is what lets the record be trusted as evidence. **Every field is a fact an owner produced
and none is authored prose**: the generation's identifiers come from its sealed manifest, the delivered
commits and trees are read out of the repositories that hold them, and the published knowledge identity is
what the ordinary read route resolves at the declared location. A reader therefore *compares the record's
own values* instead of trusting a sentence about them, and the one sentence the record publishes,
`statement` (`:261-289`), is derived from those values and cannot outrun them.

Two vocabularies are deliberately not two-valued, and each widening exists because the two-valued version
stated something false:

| Vocabulary | Values | Why the third value exists |
| --- | --- | --- |
| `MatchState` (`:66`) | `matches-reviewed-input`, `differs-from-reviewed-input`, `not-comparable` | `not-comparable` is **not a softer `differs`**: it is a channel with nothing on one side to compare — a generation that selected no knowledge operand, or a location holding no readable dataset. Reporting it as a difference reports a difference between two things that were never both read. |
| `PublishedKnowledgeState` (`:71`) | `published`, `not-recorded`, `unusable` | the route that resolves the location distinguishes "a dataset is there", "nothing is there", and "something is there that is not a dataset this code can read". Collapsing the last two loses the only fact an operator can act on. |
| `FinalOutputVerdict` (`:80`) | `bound`, `unmeasured`, `moved` | `bound` is the value a consumer keys on as *coverage*. A delivery whose selected knowledge channel was never compared has not matched — it is unknown — so it is `unmeasured`. Two values would have to call that `bound`. |

## Code Commentary

### Logic

**One verdict rule, applied by the validator rather than trusted from a writer.**
`final_output_verdict` (`:114-133`) is the single expression of the rule and the writer calls it
(`application/…:416`), so no second copy of it can drift:

- a mismatch on either channel is `moved`;
- otherwise, a generation that **selected** a knowledge operand (`reviewed_knowledge_state == "retained"`)
  with `knowledge_match == "not-comparable"` is `unmeasured`;
- otherwise `bound` — and a generation that selected no knowledge operand at all is legitimately `bound`
  on the code channel alone, because that is the whole of what it selected.

**The validator re-derives every verdict and refuses the record if it does not follow.** In
`_the_receipt_agrees_with_itself` (`:190-259`), each rule compares two values the record already holds,
so an inconsistent record is detectable **without the store** — which is exactly what makes a forged
`bound` impossible to read back as one:

- `code_match` must equal `code_match_state(reviewed_candidate_code_tree_id, delivered_code_tree_id)`
  (`:200-206`);
- `memory_output_state == "recorded"` must agree with *both* a named memory commit and a named memory
  tree, so a memory identity without its tree (or the reverse) is unconstructible (`:207-216`);
- `reviewed_knowledge_logical_digest` is named exactly when the after side is `retained` (`:217-224`);
- `published_knowledge is not None` exactly when `published_knowledge_state == "published"` — the
  message names both failure directions: "an identity beside an unreadable location is an invented
  publication and a published location with no identity is a claim with nothing behind it"
  (`:225-233`);
- `knowledge_match` must equal `knowledge_match_state(...)` over the carried states and digests
  (`:234-245`);
- `state` must equal `final_output_verdict(...)` (`:246-258`).

**The sentence says only what the record measured.** `statement` (`:261-289`) composes one clause per
verdict. `_code_clause` (`:291-299`) names both trees it compared, so a match and a mismatch read
differently without a second sentence. `_knowledge_clause` (`:301-320`) **cannot claim an unmeasured
comparison**: it returns a coverage or mismatch clause only when `published_knowledge is not None`, then
falls through to the generation's own typed absence (`not-recorded` / `not-selected`) or to the declared
location's state, in both cases saying the published dataset "was not compared to the reviewed
candidate". The `unmeasured` clause (`:273-279`) is the delivery-level version of the same honesty: it
says the generation "covers the delivered code and leaves the delivered knowledge unmeasured", and names
the two remedies (publish the reviewed dataset at the declared location, or publish a successor
generation that compares what was delivered).

### Conventions

`__all__` (`:33-44`) publishes the two version/selection literals, the four `Literal` vocabularies, the
three pure functions and the record — the whole module, since there is nothing private in it beyond the
two clause helpers on the model. `KnowledgeModel` (from `models/knowledge/base.py`) supplies the shared
shapes: `GIT_OBJECT_PATTERN`, `SHA256_PATTERN`, `UUID_PATTERN`, the three length bounds. `receipt_version`
and `selection_rule` are **fields with literal defaults** rather than comments, because "which generation
is this, under which rule?" must travel with the record instead of living in whichever reader is asking.
`delivered_memory_*` are absent together exactly when a phase recorded no memory output, and
`memory_output_state` states that rather than leaving it to be inferred from a missing value.

### Invariants And Boundaries

- **`bound` is the only value that claims coverage, and it requires a measured match on every channel the
  generation actually selected.** This is the module's load-bearing invariant; the validator enforces it,
  so no writer can produce a coverage claim the channels do not support.
- **No authored prose.** Every field is an owner-produced fact; the one sentence is derived. A reader
  comparing two receipts compares identities, not wording.
- **A carried identity is never a recomputed one.** `binding_digest` and `manifest_digest` are copied from
  the published record; a digest this vocabulary derived from a field set of its own would be a second
  identity to trust.
- **A typed absence is a value, not a gap.** `not-comparable`, `not-recorded`, `not-selected` and
  `unusable` all mean something specific and are never left to be inferred from `None`.
- **Boundary: this module is the vocabulary only.** It reads nothing, writes nothing and resolves nothing;
  a consumer that wants a receipt from the store calls the application owner. That boundary is why the
  validator can be a pure function of the record's own fields.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The claims on this card are checkable in the module's own docstrings, in the two pure functions, in the
validator, and in the cases that measure each state. The detail a reader should carry: **`not-comparable`
is not a soft `differs`, and `unmeasured` is not a soft `bound`** — both exist because the two-valued
version stated something false, and both are enforced by the validator rather than by writer discipline.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what it owns (the vocabulary alone) and of why every field is an owner-produced fact. | `FinalOutputReceipt` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:1-14; mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:136-320 |
| The published surface: two literals, four vocabularies, three functions, one record. | `__all__` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:33-44 |
| The version and selection-rule literals, carried as fields so the answer travels with the record. | `FINAL_OUTPUT_RECEIPT_VERSION`; `FINAL_OUTPUT_SELECTION_RULE` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:46-54 |
| **The two phases are separate records because each is a measurement taken at its own moment, and the published dataset can move between them.** | `FinalOutputPhase` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:56-60 |
| **`not-comparable` is a channel with nothing on one side to compare, and it never makes the receipt `moved`.** | `MatchState` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:62-66 |
| The three states of the declared publication location, in the resolving route's own vocabulary. | `PublishedKnowledgeState` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:68-71 |
| **The one verdict rule and why it has three values: `unmeasured` is not a mismatch, and `bound` is reserved for a measured match on every selected channel.** | `FinalOutputVerdict` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:73-80 |
| The code channel's comparison: delivered tree against reviewed candidate tree. | `code_match_state` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:83-88 |
| **The knowledge channel: `not-comparable` whenever one side is not a dataset at all, and never `matches` when nothing was compared.** | `knowledge_match_state` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:91-111 |
| **The single verdict expression both the writer and the validator call, so they cannot disagree.** | `final_output_verdict` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:114-133 |
| The record itself: the generation's identities, the delivered commits and trees, the published identity, the two match verdicts and the one state. | `FinalOutputReceipt` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:136-188 |
| **The validator that refuses a record whose verdicts do not follow from the identities it carries — detectable without the store, which is what stops a forged `bound`.** | `_the_receipt_agrees_with_itself` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:190-259 |
| **The one sentence the record publishes, derived from its own fields, one clause per verdict.** | `statement` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:261-289 |
| The code clause, which names both trees it compared. | `_code_clause` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:291-299 |
| **The knowledge clause, which cannot claim an unmeasured comparison: coverage and mismatch are reachable only with a published identity in hand.** | `_knowledge_clause` | mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py:301-320 |
| The shared shapes this vocabulary reuses rather than re-declaring. | `KnowledgeModel`; `GIT_OBJECT_PATTERN`; `SHA256_PATTERN`; `UUID_PATTERN` | mcp/src/agents_remember/models/knowledge/base.py:1-60 |
| The identity the published channel carries when a dataset really was read. | `SnapshotIdentity` | mcp/src/agents_remember/models/knowledge/candidate.py:1-111 |
| **The cases that measure each verdict: full match `bound`, a published dataset the review never compared `moved`, a selected knowledge operand with nothing published `unmeasured` and never `bound`, and a forged `bound` refused at read-back.** | `test_review_receipt_binds_the_delivered_pair_to_the_selected_generation`; `test_review_receipt_reports_a_published_dataset_the_review_never_compared`; `test_a_selected_knowledge_operand_with_nothing_published_is_never_bound`; `test_a_forged_coverage_verdict_is_refused_when_read_back` | mcp/tests/test_review_final_output_receipt.py:451-508; mcp/tests/test_review_final_output_receipt.py:544-570; mcp/tests/test_review_final_output_receipt.py:755-788; mcp/tests/test_review_final_output_receipt.py:790-823 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It declares a wire shape whose path fields
(`task_root`, `contract_path`, `published_knowledge_path`) are recorded as the owner produced them; the
relocation boundary that follows from a recorded absolute path is stated on
`application/review_final_output_receipt.py` and is the same one ICR-R12/R13 own for the generation
record.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-23T09:05:00+02:00 — 260921-ICR-L21 curator (uncommitted change set on `ar/260921-icr-l21`, base `972b44cc07b307929535fe7974d6a30d53c9c4f1`): created this one-to-one card for the module this leaf introduced as **the vocabulary half of ICR-R21@v1** — the typed record that identifies the exact source and knowledge outputs a normal closeout/integration selected. It records what a consumer keys on: `bound` is the only value that claims coverage and it requires a measured match on every channel the generation actually selected; `unmeasured` exists because a selected knowledge operand that was never compared is **unknown, not matched**; `not-comparable` is not a softer `differs`; and a carried identity is never recomputed. The validator re-derives every verdict from the record's own fields, which is what makes a forged `bound` unreadable as one. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the **production line this reading was against** — `972b44cc07b307929535fe7974d6a30d53c9c4f1`, this leaf's recorded base, whose date is the worker report's own timestamp — because every construct cited here exists only in this leaf's uncommitted working tree; what was actually read is that working tree, and the governed closeout owns the real stamp once the code commit exists.
