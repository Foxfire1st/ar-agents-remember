# mcp/src/agents_remember/models/knowledge/revision_selection.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The value describing an invariant or family's selected revision on each compared memory tree.
The application owner is `application/review_revision_comparison.py`; this module performs no
SQL, Git resolution, lineage traversal or selection policy. The current projected-record policy
constructs empty or singleton head/retained lists, not a history of selectable dataset revisions.
The former `ambiguous` state and intermediate-revision-selection account are retired below.

## Code Commentary

### Logic

- `RevisionSelectionState` admits `compared`, `unresolved`, `added` and `removed`.
- `ReviewRevisionSelection` carries the `invariant`/`family` kind, record identity, optional
  before/after revision IDs, each side's head/retained tuples, and a bounded explanatory statement.
  The field names remain; they do not themselves establish database lineage or read authenticity.
- `_require_the_state_to_match_the_pair` checks presence, not recency: compared requires both
  IDs; added only after; removed only before; unresolved neither.
- `_require_the_pair_to_come_from_the_heads` requires a non-None selection to belong to its
  declared side's heads. `_require_the_heads_to_come_from_the_retained` requires each head to
  belong to its declared retained set. These are consistency constraints over supplied values,
  not independent proof that those values came from a memory tree.
- The producer filters by the selected subject's kind and identity and obtains its first matching
  non-None revision item on each side. It builds empty/singleton lists from those items and names
  the pair/addition/removal/no-selection explicitly. It does not walk predecessor edges, diagnose
  multiple lineage heads, pick a newest revision, or offer intermediate revisions as selectors.
  The DTO's tuple annotations do not enforce a maximum length or reject duplicate list members.
- `revision_heads` is deterministic sorting of its supplied population, not graph-head discovery.
- The knowledge pane carries an optional selection. Its actual implication is selection present
  implies `subject_selected`; the converse is not required. In particular a path seed may name no
  invariant/family identity and carry no revision selection. A task-context pane cannot carry one.

### Conventions

The model and state union are the public exports. Reference/prose fields use the shared bounds,
immutable collections have tuple defaults, and `KnowledgeModel` supplies the frozen/extra-forbidden
base behavior. No new record kind, writer or dedicated verdict field is declared here. The free
`statement` string is not a semantic filter against arbitrary prose or conclusions.

### Invariants And Boundaries

The selected-pair presence pattern and declared-set membership are constructor checks. Empty or
singleton lists are what the examined producer constructs, not a separately enforced DTO size
limit. None of these checks authenticates source reads, proves uniqueness of arbitrary caller
items, certifies a comparison, or reinterprets an old review on a replacement tree. The old
multi-head ambiguity and selectable retained-history claims are not current product behavior.

### Todos

No additional implementation work is asserted by this card.

## Evidence

### Docs References

No configured Domain Documentation source was available for this pass. Current implementation
facts below are grounded in the repository's model, producer and direct pane boundary.

### Repo-Internal References

- The current module and value describe a projected record pair, not multi-head lineage or unforgeable input provenance. [1]

- The public exports remain the model and its state union. [2]

- The closed state vocabulary is compared, unresolved, added and removed; ambiguous is no longer admitted. [3]

- The value records subject kind/identity, optional pair, side lists and bounded statement; tuples have no singleton-size validator. [4]

- The declared state requires the exact presence pattern of the before/after pair, with unresolved carrying neither. [5]

- A non-None selection must belong to its declared side heads; this is membership consistency, not source authentication. [6]

- Every declared head must belong to the declared retained set; no lineage traversal or provenance check is performed. [7]

- The value reuses reference/prose bounds and the frozen extra-forbidden base model, not new per-item tuple bounds. [8]

- The pane field and one-direction guard allow selection only for subject_selected, without requiring every compared path seed to carry one. [9]

- The current subject-specific producer constructs empty/singleton lists and explicit state/statement from projected side items; sorting is not multi-head lineage selection. [10]

### Cross-Repo References

No external-system boundary is implemented by this value model or its cited same-repository owners.

## Historical BASE Account

The following preserved account described the former multi-head/retained-history policy. Its
ambiguous-state, intermediate-selector and anti-fabrication claims are superseded, not current
assertions. Historical citation labels are inert; the active evidence above belongs to the
examined freeze07 source. Useful original prose is retained for custody, not execution or approval.

<details>
<summary>Superseded BASE account, preserved for history</summary>

> # mcp/src/agents_remember/models/knowledge/revision_selection.py
>
> ## Governing Overview
>
> [models route overview](../overview.md)
>
> ## Purpose
>
> The explicit before/after revision selection one subject comparison records (`ICR-R07@v1`): which
> retained revision each snapshot's side is compared on, every head the snapshots retain, and the exact
> statement that says why that pair — or no pair — was used. It holds no SQL, no Git resolution and no
> selection policy: the policy that computes it lives in
> `application/review_revision_comparison.py`, and this module makes the result unrepresentable to
> misread rather than merely documented. It lives outside `models/knowledge/review.py` so the
> vocabulary file stays under the soft rail.
>
> - **A pair or an explicit non-pair, never a silent default.** `state` says which question was
>   answered: `compared` names the before head and the after head the two snapshots were compared on;
>   `added`/`removed` name the one head a known-empty side is shown against (`ICR-R06@v1`'s one-sided
>   contract, reused rather than restated); `ambiguous` names the multiple heads no winner was chosen
>   from; `unresolved` names the lineage failure no comparison was fabricated from. The validators
>   enforce the pairing, so a state cannot carry the ids of another.
> - **Heads are recorded beside the pair.** Even a `compared` selection carries every head each side
>   retains, and both sides' full retained revision lists travel as `before_retained` and
>   `after_retained`. An intermediate revision is therefore addressable — through the comparison's own
>   per-side explicit revision selector — rather than merely counted, which is what "intermediate
>   revisions remain selectable history" means as a value.
> - **No field a fabrication could occupy.** There is no timestamp, no similarity score, no ordering
>   rank and no "latest" flag anywhere in this vocabulary, so a newest-version claim invented from
>   recency or text resemblance cannot be recorded here even by a caller that wanted to. The lists are
>   stored sorted so two runs over the same snapshots render the same value, and that order is a
>   rendering determinism the policy module states — never a semantic revision rule, which this value
>   could not express.
>
> ## Code Commentary
>
> ### Logic
>
> **`RevisionSelectionState` is the closed five-member union of which question one subject comparison
> answered.** `compared` is the unique-head pair; `added`/`removed` is a known-empty side shown under
> `ICR-R06@v1`; `ambiguous` is multiple legitimate heads with no winner chosen; `unresolved` is a
> lineage failure (a cycle that leaves no head, or an authored edge the snapshot does not retain) with
> no comparison fabricated from it.
>
> **`ReviewRevisionSelection` is one subject's explicit selection, recorded with its own statement.**
> `record_kind` is the closed `invariant`/`family` pair (claims and frontier links are never heads, so
> they are not representable here); `record_id` names the reviewed identity; `before_revision_id` /
> `after_revision_id` are the selected pair when the two snapshots were compared on one revision each,
> and are absent exactly when no pair was selected. `statement` is the human-readable record of the
> same fact — the compared heads, the named ambiguity, or the named lineage failure — so a reviewer
> never has to reconstruct the rule from the ids.
>
> **The three validators are what make a misreading unconstructible rather than discouraged.**
> `_require_the_state_to_match_the_pair` refuses a state carrying another state's ids (a compared
> selection missing a side, a one-sided selection carrying the empty side, an ambiguous or unresolved
> selection carrying any pair — the arbitrary winner the packet forbids).
> `_require_the_pair_to_come_from_the_heads` refuses a selected revision outside the recorded heads —
> the exact slot a collection-order or presence-based default would enter wearing the heads' names.
> `_require_the_heads_to_come_from_the_retained` refuses a head no retained population contains — a
> revision invented beside the snapshots rather than read from them.
>
> ### Conventions
>
> Every bound is the shared one: `record_id` and the revision ids use `REFERENCE_MAX_LENGTH`,
> `statement` uses `PROSE_MAX_LENGTH`, all from `models/knowledge/base.py`, so a display field is
> bounded by the same constants every other knowledge model uses. `__all__` names the model and its
> state union and nothing else. Immutable collections are `tuple[...]` with `()` defaults, so no model
> carries a mutable default. The pane carries this value as an optional field (`revision_selection`,
> absent exactly when no subject was compared), and the pane's own one-direction validator keeps a
> recorded selection beside a compared subject.
>
> ### Invariants And Boundaries
>
> - **No record kind is defined here.** The module declares no table, no status, no stored entity and
>   no writer; every field renders a selection the policy computed, or states its absence.
> - **No field can hold a conclusion.** There is no summary, severity, score, verdict, causal
>   explanation or approval anywhere in the value — the same prohibition the surface vocabulary
>   enforces, applied to the selection it now carries.
> - **A selected pair is drawn from the recorded heads, and the heads from the retained.** Both
>   directions are constructor checks, so neither a presence-based default nor an invented revision can
>   be recorded here.
> - **The value decides nothing.** It carries no policy, no read and no comparison; the application
>   module computes it and the pane renders it.
>
> ### Todos
>
> None recorded.
>
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured for this repository (`system/sources.md` carries no
> `Domain Documentation` entries). The statements below are grounded in repository source only.
>
> No configured domain documentation could be checked.
>
> ### Repo-Internal References
>
> Every claim on this card is checkable in the shipped candidate: the module's own docstring and
> three bullets, the state union, the model and its three validators, the shared bounds it imports,
> and the pane field that carries it.
>
> - The module's own statement of what it owns: the value the comparison is made with, the pair-or-explicit-non-pair rule, the heads beside the pair, and the vocabulary no fabrication can occupy. (historical reference 1)
> - The published surface: the model and its state union. (historical reference 2)
> - The closed five-member union of which question one subject comparison answered. (historical reference 3)
> - One subject's explicit selection with its own statement: the pair present exactly when the snapshots were compared on one revision each. (historical reference 4)
> - The state/pair agreement: a compared selection names both heads, a one-sided selection names its one head, an ambiguous or unresolved selection names none. (historical reference 5)
> - The pair drawn from the heads: a selected revision outside the recorded heads is not a head selection. (historical reference 6)
> - The heads drawn from the retained: a head outside its side's retained list is invented beside the snapshots. (historical reference 7)
> - The shared bounds every field reads rather than restating. (historical reference 8)
> - The pane field that carries this value, absent exactly when no subject was compared, with its one-direction validator. (historical reference 9)
> - The policy that computes this value from authored heads. (historical reference 10)
>
> ### Cross-Repo References
>
> No cross-repository behavior is implemented in this file. Every model is a display shape over one
> repository's records, and no field carries an identity that ranges beyond the repository namespace
> the request names.
>
> No meaningful cross-repo references found.

</details>
