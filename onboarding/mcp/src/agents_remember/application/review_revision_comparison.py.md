# mcp/src/agents_remember/application/review_revision_comparison.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_revision_comparison.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T11:39:00+02:00 |
| lastVerifiedCommitHash | `c422dc00273d4ae7a5d8c9c8db97365b8c85d640` |
| lastVerifiedCommitDate | 2026-09-23T05:16:40+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

The explicit revision comparison's selection policy (`ICR-R07@v1`): which retained revision each
snapshot's side of the primary statement comparison is rendered from. The rule the packet's Required
Behavior states is one sentence — **a revision head is a retained revision with no recorded successor
for that identity in the selected snapshot revision population** — where "recorded successor" means
an authored predecessor edge (the successor's own declaration of which revision it replaced) and
nothing else. No collection order, no presence on both sides, no timestamp and no text similarity
participates, because none of them is a statement an author made about which revision replaced which.

**Why this is its own module.** The review adapter is over the repository's soft file-size rail, and
the packet's Scope asks a leaf that touches a responsibility inside it to move that responsibility out
before adding behavior. Head selection is that responsibility here: one implementation, called by
`application/knowledge_review.py`, which stays the adapter that resolves, calls and assembles. The
adapter re-exports nothing from here because no module under `mcp/` imported the rule this replaces —
the both-sides preference was private to the adapter — so there is one implementation and no alias to
keep.

**What it reads.** The selected populations come from the shipped comparison's own union items (one
item per retained revision, each carrying the side payloads that selected it), and the authored edges
come from the two snapshots' own predecessor tables, read through read-only connections. Both inputs
are recorded facts; this module invents neither.

**What it returns.** One `ReviewRevisionSelection` per reviewed identity: the unique-head pair when
each nonempty side establishes exactly one head (before `r1` and after `r1 → r2 → r3` therefore
defaults to `r1` versus `r3`; before `r1 → r2` and after `r1 → r2 → r3` defaults to `r2` versus `r3`),
the one-sided head under `ICR-R06@v1` when a side is known-empty, and an explicit ambiguous or
unresolved selection — with every head and every retained revision still listed — when multiple heads,
a successor cycle, or an authored edge the snapshot does not retain prevents a unique head.
Intermediate revisions stay in the union and stay addressable through the comparison's own per-side
explicit revision selector; this module removes none of them.

## Code Commentary

### Logic

**`revision_heads` is the whole rule in one pure function: a head is a population member no other
member names as its predecessor.** Edges are `(successor, predecessor)` pairs, and only pairs with
*both* endpoints in the population establish a successor relation — an edge to a revision outside the
population is not a successor *in the selected population* the packet scopes the rule to. The sorted
output order is a rendering determinism (the same snapshots always list the same heads), never a
semantic revision rule: no caller may read the first head as the selected one.

**`select_subject_revisions` is the one entry point, and it decides from the comparison's own union,
never by re-reading a snapshot for populations.** The populations are the shipped comparison's own
union items for the selector's identity — the before payloads' revisions on the before side and the
after payloads' on the after side (`_side_population`, which reads only the two supersedable kinds:
a claim and a frontier link record no authored edge, so they are never heads). The edges are each
snapshot's own authored predecessor relations (`read_snapshot_edges`, one read-only open per snapshot,
closed before returning). A selector that names no identity addresses no identity item (`None`), and
two empty populations are an explicit unresolved selection rather than a decision — exactly as the
adapter's rule this replaces did.

**`_decide` routes one identity's established populations to exactly one recorded selection.** An
authored edge touching the reviewed population whose other endpoint the snapshot does not retain is
an invalid graph first (`_invalid_graph_detail` / `_unretained_endpoint`, which names the missing
revision rather than repairing it; recorded-but-unselected endpoints are ignored because the packet
scopes heads to the selected population). A known-empty side then stays an `ICR-R06@v1` addition or
removal (`_one_sided`, which shows the nonempty side's unique head and renders the empty side absent
exactly as the one-sided contract already does — a nonempty side with anything but one head is an
ambiguity or a lineage failure, not a one-sided side wearing a chosen revision). Two nonempty sides
combine in `_combine`: no head on a side is a successor cycle with no newest version fabricated;
anything but exactly one head per side is an explicit ambiguity with no pair; one head per side is the
compared pair.

**`_item_with` keys the rendered operands by stored revision identity, never by stream position.**
The head the snapshots replaced is found by its revision id wherever the union placed it — which is
what makes "never use collection order or presence on both sides as a semantic revision rule" a
property of the lookup rather than a convention of its callers.

### Conventions

The module imports the shipped vocabulary and re-declares nothing: `KnowledgeDiffItem` /
`KnowledgeReadSeed` are the diff and read models, `ReviewRevisionSelection` is the value module's,
and the edge reads go through the shipped `fetch_predecessor_edges` plus the kind-specific recorded
checks. `__all__` publishes the four names a caller needs — `SubjectRevisionSelection`,
`read_snapshot_edges`, `revision_heads`, `select_subject_revisions` — and the private helpers
(`_ReviewedPopulations` / `_EdgeSources`, which travel as one value so a helper cannot be handed one
subject's populations with another's heads) stay private. The two dataclasses are frozen, because a
selection's inputs are facts, not accumulators. No SQL beyond the shipped readers, no Git resolution,
no store, no writer: the module opens the two snapshot files read-only and closes them before
returning.

### Invariants And Boundaries

- **Heads come from authored successors, never from order, presence, recency or resemblance.** The
  module greps clean for timestamp/similarity/latest/HEAD logic (only docstring prohibitions), and
  the value module it returns into has no field such a fabrication could occupy.
- **A non-pair is explicit, never a silent default.** Ambiguity lists every head and every retained
  revision with no pair; unresolved names the missing revision or the cycle with no pair; one-sided
  names the shown head and the empty side. No path fabricates a winner.
- **Known-empty stays one-sided under R06.** The addition/removal rendering is reused, never
  re-implemented; the recorded state is `added`/`removed` with the one head it shows.
- **Intermediate revisions remain selectable history.** The full retained lists travel on the value,
  and the comparison's own per-side explicit revision selector addresses them — this module removes
  none of them.
- **Kind-agnostic.** The policy asks the same question of invariant and family identities through the
  same edge readers; claims and frontier links are never heads.
- **Family-subject multi-revision choice beyond this packet stays R08/R09's; browser rendering of the
  recorded value stays R25's.** This module records the selection and renders its statement text; it
  decides no movement display and draws no UI.

### Todos

None recorded. The end-to-end family-kind chain has no dedicated case (all chain fixtures use
invariant identities, though the code reads the same `fetch_predecessor_edges` union for both kinds);
the before-empty + multi-head-after corner routes to ambiguity by construction with no dedicated
case; dashboard rendering of `revision_selection` is out of packet scope (R25's assembly).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and
policy, the four published names, the pure head rule, the entry point's population source, the
three-way decision, the invalid-graph read, the one-sided reuse, and the ten cases that measure it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the one rule, what it reads, what it returns, and why it is its own module. | `select_subject_revisions`; `revision_heads` | mcp/src/agents_remember/application/review_revision_comparison.py:1-31; mcp/src/agents_remember/application/review_revision_comparison.py:144-187; mcp/src/agents_remember/application/review_revision_comparison.py:81-94 |
| The published surface: one value, two readers, one entry point. | `__all__` | mcp/src/agents_remember/application/review_revision_comparison.py:51-56 |
| The reviewed identity's head selection with the union items its statements render from — and the one-sided item the R06 rendering already reads. | `SubjectRevisionSelection` | mcp/src/agents_remember/application/review_revision_comparison.py:63-78 |
| The whole rule in one pure function: heads are members no other member names as predecessor; both-endpoints-in-population filter; sorted order as rendering determinism only. | `revision_heads`; `_touching` | mcp/src/agents_remember/application/review_revision_comparison.py:81-94; mcp/src/agents_remember/application/review_revision_comparison.py:291-303 |
| The read-only edge read: one snapshot opened read-only, both predecessor tables, closed before returning. | `read_snapshot_edges` | mcp/src/agents_remember/application/review_revision_comparison.py:97-110 |
| The one entry point: populations from the comparison's own union, edges from each snapshot's own authored relations; no-identity selector and empty populations as explicit non-pairs. | `select_subject_revisions`; `_populations`; `_side_population`; `_selector_identity` | mcp/src/agents_remember/application/review_revision_comparison.py:144-187; mcp/src/agents_remember/application/review_revision_comparison.py:190-213; mcp/src/agents_remember/application/review_revision_comparison.py:267-288; mcp/src/agents_remember/application/review_revision_comparison.py:256-264 |
| The three-way routing: invalid graph first, one-sided for a known-empty side, combine for two nonempty sides. | `_decide`; `_invalid_graph_detail`; `_unretained_endpoint` | mcp/src/agents_remember/application/review_revision_comparison.py:216-234; mcp/src/agents_remember/application/review_revision_comparison.py:306-331; mcp/src/agents_remember/application/review_revision_comparison.py:334-365 |
| Two nonempty sides: cycle with no head fabricated, multi-head ambiguity with no pair, unique heads compared. | `_combine`; `_compared`; `_ambiguous`; `_unresolved` | mcp/src/agents_remember/application/review_revision_comparison.py:237-253; mcp/src/agents_remember/application/review_revision_comparison.py:378-407; mcp/src/agents_remember/application/review_revision_comparison.py:470-506; mcp/src/agents_remember/application/review_revision_comparison.py:509-526 |
| A known-empty side stays an R06 addition/removal with the nonempty side's unique head — and a crowded nonempty side is ambiguity, not a one-sided side. | `_one_sided` | mcp/src/agents_remember/application/review_revision_comparison.py:410-467 |
| Operands keyed by stored revision identity, never by stream position or both-sides presence. | `_item_with` | mcp/src/agents_remember/application/review_revision_comparison.py:529-552 |
| The adapter's one call site: the selection computed once in `compose_review` from the comparison's union items and the two snapshots' own authored edges, rendered by the pane. | `select_subject_revisions`; `_knowledge_pane` |mcp/src/agents_remember/application/knowledge_review.py:121-121; mcp/src/agents_remember/application/knowledge_review.py:967-1019|
| The recorded value the policy returns into, with the state/pair/heads validators that make a fabrication unrepresentable. | `ReviewRevisionSelection` | mcp/src/agents_remember/models/knowledge/revision_selection.py:54-150 |
| The ten cases that measure the policy through the real comparison: two chain defaults, selectable history, two forks, one-sided removal, cycle, dangling edge, order-independence, and the pane's own statements. | `test_a_unique_chain_defaults_to_the_first_before_head_versus_the_last_after_head`; `test_a_fork_on_the_after_side_is_an_explicit_ambiguity`; `test_a_successor_cycle_is_unresolved_and_names_no_pair`; `test_heads_come_from_successors_not_from_sorted_order`; `test_the_review_pane_renders_the_selected_head_pairs_own_statements` | mcp/tests/test_knowledge_review_revision_selection.py:259-280; mcp/tests/test_knowledge_review_revision_selection.py:333-345; mcp/tests/test_knowledge_review_revision_selection.py:416-467; mcp/tests/test_knowledge_review_revision_selection.py:524-536; mcp/tests/test_knowledge_review_revision_selection.py:571-615 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The module reads two snapshot files of one
repository's candidate and carries no identity that ranges beyond the repository namespace the
comparison was opened under.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-22T11:39:00+02:00 — 260921-ICR-L13 curator, **L7-aftershock citation repair: the adapter call-site row re-cited to the landed declarations** (`select_subject_revisions` import `:90-93`, `_knowledge_pane` `:712-759`). Wording retained; no stamp advanced.
- 2026-09-22T10:40:00+02:00 — 260921-ICR-L7 curator (uncommitted change set on `ar/260921-icr-l7`, base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **created.** The module is new in this leaf and this is its one-to-one card. It records the head-selection policy `ICR-R07@v1` owns (heads from authored predecessor edges only; unique heads compare head-to-head; known-empty sides stay R06 additions/removals; multi-heads, cycles and dangling edges yield explicit ambiguous/unresolved selections that still list every head and retained revision; intermediate revisions selectable on demand through the comparison's own per-side selector), the seam (the adapter resolves, calls and assembles; this module owns the rule; no alias because the replaced both-sides preference was private), and the boundaries the packet states (no order/presence/timestamp/similarity participation; kind-agnostic; R08/R09 movement display and R25 browser rendering out of scope). Every range was measured against the 552-line candidate module. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the leaf's base — the last real commit the reading was taken against — because every construct this card cites exists only in this leaf's uncommitted candidate and no commit contains the bytes a stamp would claim to have verified. The recorded working candidate states what was actually read; closeout owns the stamp once the code commit exists.
