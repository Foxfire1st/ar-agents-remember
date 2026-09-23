# mcp/src/agents_remember/models/knowledge/revision_selection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/revision_selection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T10:40:00+02:00 |
| lastVerifiedCommitHash | `870701b43039cd205a8c98e418382729510c3de3` |
| lastVerifiedCommitDate | 2026-09-23T03:12:21+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

The explicit before/after revision selection one subject comparison records (`ICR-R07@v1`): which
retained revision each snapshot's side is compared on, every head the snapshots retain, and the exact
statement that says why that pair — or no pair — was used. It holds no SQL, no Git resolution and no
selection policy: the policy that computes it lives in
`application/review_revision_comparison.py`, and this module makes the result unrepresentable to
misread rather than merely documented. It lives outside `models/knowledge/review.py` so the
vocabulary file stays under the soft rail.

- **A pair or an explicit non-pair, never a silent default.** `state` says which question was
  answered: `compared` names the before head and the after head the two snapshots were compared on;
  `added`/`removed` name the one head a known-empty side is shown against (`ICR-R06@v1`'s one-sided
  contract, reused rather than restated); `ambiguous` names the multiple heads no winner was chosen
  from; `unresolved` names the lineage failure no comparison was fabricated from. The validators
  enforce the pairing, so a state cannot carry the ids of another.
- **Heads are recorded beside the pair.** Even a `compared` selection carries every head each side
  retains, and both sides' full retained revision lists travel as `before_retained` and
  `after_retained`. An intermediate revision is therefore addressable — through the comparison's own
  per-side explicit revision selector — rather than merely counted, which is what "intermediate
  revisions remain selectable history" means as a value.
- **No field a fabrication could occupy.** There is no timestamp, no similarity score, no ordering
  rank and no "latest" flag anywhere in this vocabulary, so a newest-version claim invented from
  recency or text resemblance cannot be recorded here even by a caller that wanted to. The lists are
  stored sorted so two runs over the same snapshots render the same value, and that order is a
  rendering determinism the policy module states — never a semantic revision rule, which this value
  could not express.

## Code Commentary

### Logic

**`RevisionSelectionState` is the closed five-member union of which question one subject comparison
answered.** `compared` is the unique-head pair; `added`/`removed` is a known-empty side shown under
`ICR-R06@v1`; `ambiguous` is multiple legitimate heads with no winner chosen; `unresolved` is a
lineage failure (a cycle that leaves no head, or an authored edge the snapshot does not retain) with
no comparison fabricated from it.

**`ReviewRevisionSelection` is one subject's explicit selection, recorded with its own statement.**
`record_kind` is the closed `invariant`/`family` pair (claims and frontier links are never heads, so
they are not representable here); `record_id` names the reviewed identity; `before_revision_id` /
`after_revision_id` are the selected pair when the two snapshots were compared on one revision each,
and are absent exactly when no pair was selected. `statement` is the human-readable record of the
same fact — the compared heads, the named ambiguity, or the named lineage failure — so a reviewer
never has to reconstruct the rule from the ids.

**The three validators are what make a misreading unconstructible rather than discouraged.**
`_require_the_state_to_match_the_pair` refuses a state carrying another state's ids (a compared
selection missing a side, a one-sided selection carrying the empty side, an ambiguous or unresolved
selection carrying any pair — the arbitrary winner the packet forbids).
`_require_the_pair_to_come_from_the_heads` refuses a selected revision outside the recorded heads —
the exact slot a collection-order or presence-based default would enter wearing the heads' names.
`_require_the_heads_to_come_from_the_retained` refuses a head no retained population contains — a
revision invented beside the snapshots rather than read from them.

### Conventions

Every bound is the shared one: `record_id` and the revision ids use `REFERENCE_MAX_LENGTH`,
`statement` uses `PROSE_MAX_LENGTH`, all from `models/knowledge/base.py`, so a display field is
bounded by the same constants every other knowledge model uses. `__all__` names the model and its
state union and nothing else. Immutable collections are `tuple[...]` with `()` defaults, so no model
carries a mutable default. The pane carries this value as an optional field (`revision_selection`,
absent exactly when no subject was compared), and the pane's own one-direction validator keeps a
recorded selection beside a compared subject.

### Invariants And Boundaries

- **No record kind is defined here.** The module declares no table, no status, no stored entity and
  no writer; every field renders a selection the policy computed, or states its absence.
- **No field can hold a conclusion.** There is no summary, severity, score, verdict, causal
  explanation or approval anywhere in the value — the same prohibition the surface vocabulary
  enforces, applied to the selection it now carries.
- **A selected pair is drawn from the recorded heads, and the heads from the retained.** Both
  directions are constructor checks, so neither a presence-based default nor an invented revision can
  be recorded here.
- **The value decides nothing.** It carries no policy, no read and no comparison; the application
  module computes it and the pane renders it.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and
three bullets, the state union, the model and its three validators, the shared bounds it imports,
and the pane field that carries it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what it owns: the value the comparison is made with, the pair-or-explicit-non-pair rule, the heads beside the pair, and the vocabulary no fabrication can occupy. | `ReviewRevisionSelection` | mcp/src/agents_remember/models/knowledge/revision_selection.py:1-27; mcp/src/agents_remember/models/knowledge/revision_selection.py:54-74 |
| The published surface: the model and its state union. | `__all__` | mcp/src/agents_remember/models/knowledge/revision_selection.py:41-44 |
| The closed five-member union of which question one subject comparison answered. | `RevisionSelectionState` | mcp/src/agents_remember/models/knowledge/revision_selection.py:51-51 |
| One subject's explicit selection with its own statement: the pair present exactly when the snapshots were compared on one revision each. | `ReviewRevisionSelection` | mcp/src/agents_remember/models/knowledge/revision_selection.py:54-74 |
| The state/pair agreement: a compared selection names both heads, a one-sided selection names its one head, an ambiguous or unresolved selection names none. | `_require_the_state_to_match_the_pair` | mcp/src/agents_remember/models/knowledge/revision_selection.py:76-106 |
| The pair drawn from the heads: a selected revision outside the recorded heads is not a head selection. | `_require_the_pair_to_come_from_the_heads` | mcp/src/agents_remember/models/knowledge/revision_selection.py:108-129 |
| The heads drawn from the retained: a head outside its side's retained list is invented beside the snapshots. | `_require_the_heads_to_come_from_the_retained` | mcp/src/agents_remember/models/knowledge/revision_selection.py:131-150 |
| The shared bounds every field reads rather than restating. | `PROSE_MAX_LENGTH`; `REFERENCE_MAX_LENGTH`; `KnowledgeModel` | mcp/src/agents_remember/models/knowledge/base.py:1-80 |
| The pane field that carries this value, absent exactly when no subject was compared, with its one-direction validator. | `revision_selection`; `_require_a_compared_subject_to_record_its_selection` | mcp/src/agents_remember/models/knowledge/review.py:707-756; mcp/src/agents_remember/models/knowledge/review.py:714-714 |
| The policy that computes this value from authored heads. | `select_subject_revisions` | mcp/src/agents_remember/application/review_revision_comparison.py:144-187 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every model is a display shape over one
repository's records, and no field carries an identity that ranges beyond the repository namespace
the request names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-22T10:40:00+02:00 — 260921-ICR-L7 curator (uncommitted change set on `ar/260921-icr-l7`, base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **created.** The module is new in this leaf and this is its one-to-one card. It records the selection value `ICR-R07@v1` compares on (pair or explicit non-pair with every head and retained revision listed; no timestamp/similarity/rank/latest field), the three validators that make a misreading unconstructible, and the reason the value lives outside `models/knowledge/review.py` (the vocabulary file stays under the soft rail). Every range was measured against the 150-line candidate module. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the leaf's base — the last real commit the reading was taken against — because every construct this card cites exists only in this leaf's uncommitted candidate and no commit contains the bytes a stamp would claim to have verified. The recorded working candidate states what was actually read; closeout owns the stamp once the code commit exists.
