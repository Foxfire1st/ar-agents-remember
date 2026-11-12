# mcp/src/agents_remember/application/review_revision_comparison.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Select one invariant/family’s own recorded before/after revisions and forward each side’s display version.

## Code Commentary

SubjectRevisionSelection remains a frozen holder for optional selection and actual source items. Unsupported or absent selectors return no selected identity. `_side_item` takes the first matching kind/id item with a non-None revision on that side; arbitrary duplicate/conflicting caller items are not rejected independently.

Each selected side supplies both its revision id and its own display_version. The output’s head/retained lists are empty or singleton, equal per side. Both ids produce compared, only after added, only before removed and neither unresolved, with a statement naming the actual operands.

revision_heads still sorts a supplied sequence deterministically; this selection path does not call it, open snapshots, traverse lineage or offer intermediate historical revisions. Its names do not revive the removed multi-head policy.

## Invariants And Boundaries

Selection uses subject identity, not a collection-wide default, but stream position can affect arbitrary duplicate inputs because the local lookup chooses first. Display versions are forwarded values, not inferred revision chronology or source-authenticity proof.

## Historical predecessor account

The entire previous account follows as historical provenance. Removed names, old selection/collection semantics and prior execution claims do not describe the current module; prose reference numbers are inert.

### mcp/src/agents_remember/application/review_revision_comparison.py

#### Governing Overview

[application route overview](overview.md)

#### Purpose

The explicit revision comparison's selection policy (MIK-R74 rule 1): which retained revision each
snapshot's side of the primary statement comparison is rendered from. Every retained revision is a
head — text records hold no predecessor edge, so no recorded successor relation narrows the
population. Unique heads compare head-to-head; a known-empty side stays an `ICR-R06@v1`
addition or removal; multiple heads are an explicit ambiguity that still lists every head and every
retained revision. No collection order, no presence on both sides, no timestamp and no text
similarity participates. Under `ICR-R07@v1` heads were recorded-successor selections over authored
predecessor edges; that rule is superseded — the edge readers are deleted and
`select_subject_revisions` takes only items and selector.

**Why this is its own module.** The review adapter is over the repository's soft file-size rail, and
the packet's Scope asks a leaf that touches a responsibility inside it to move that responsibility out
before adding behavior. Head selection is that responsibility here: one implementation, called by
`application/knowledge_review.py`, which stays the adapter that resolves, calls and assembles. The
adapter re-exports nothing from here because no module under `mcp/` imported the rule this replaces —
the both-sides preference was private to the adapter — so there is one implementation and no alias to
keep.

**What it reads.** The selected populations come from the shipped comparison's own union items (one
item per retained revision, each carrying the side payloads that selected it). No snapshot
predecessor table is read; the edge readers are deleted. Both inputs
are recorded facts; this module invents neither.

**What it returns.** One `SubjectRevisionSelection` per reviewed identity: the compared pair when
each nonempty side establishes exactly one head, the one-sided head under `ICR-R06@v1` when a side
is known-empty, and an explicit ambiguous or unresolved selection — with every head and every
retained revision still listed — when multiple heads or an empty population prevent a pair.
Intermediate revisions stay in the union and stay addressable through the comparison's own per-side
explicit revision selector; this module removes none of them.

#### Code Commentary

##### Logic

**`revision_heads` is the whole rule in one pure function: every retained revision is a head.**
Text records hold no predecessor edge (MIK-R74 rule 1), so no recorded successor relation narrows the
population — a side with exactly one retained revision establishes one head, and a side with several
establishes several. The sorted output order is a rendering determinism (the same snapshots always
list the same heads), never a semantic revision rule: no caller may read the first head as the
selected one.

**`select_subject_revisions` is the one entry point, and it decides from the comparison's own union,
never by re-reading a snapshot for populations.** The populations are the shipped comparison's own
union items for the selector's identity — the before payloads' revisions on the before side and the
after payloads' on the after side (`_side_population`, which reads only the two selectable kinds:
a claim and a frontier link hold no selectable revisions, so they never establish heads). A selector that names no identity addresses no identity item (`None`), and
two empty populations are an explicit unresolved selection rather than a decision — exactly as the
adapter's rule this replaces did.

**`_decide` routes one identity's established populations to exactly one recorded selection.** A known-empty side stays an `ICR-R06@v1` addition or
removal (`_one_sided`, which shows the nonempty side's unique head and renders the empty side absent
exactly as the one-sided contract already does — a nonempty side with anything but one head is an
ambiguity, not a one-sided side wearing a chosen revision). Two nonempty sides
combine in `_combine`: anything but exactly one head per side is an explicit ambiguity with no pair; one head per side is the
compared pair.

**`_item_with` keys the rendered operands by stored revision identity, never by stream position.**
The head the snapshots replaced is found by its revision id wherever the union placed it — which is
what makes "never use collection order or presence on both sides as a semantic revision rule" a
property of the lookup rather than a convention of its callers.

##### Conventions

The module imports the shipped vocabulary and re-declares nothing: `KnowledgeDiffItem` /
`KnowledgeReadSeed` are the diff and read models, `ReviewRevisionSelection` is the value module's.
`__all__` publishes the three names a caller needs — `SubjectRevisionSelection`,
`revision_heads`, `select_subject_revisions` — and the private helpers
(`_ReviewedPopulations`, whose four tuples travel as one value so a helper cannot be handed one
subject's populations with another's heads) stay private. The dataclasses are frozen, because a
selection's inputs are facts, not accumulators.

##### Invariants And Boundaries

- **Heads are retained revisions, never order, presence, recency or resemblance.** The
  module greps clean for timestamp/similarity/latest/HEAD logic (only docstring prohibitions), and
  the value module it returns into has no field such a fabrication could occupy.
- **A non-pair is explicit, never a silent default.** Ambiguity lists every head and every retained
  revision with no pair; unresolved names the missing selected population with no pair; one-sided
  names the shown head and the empty side. No path fabricates a winner.
- **Known-empty stays one-sided under R06.** The addition/removal rendering is reused, never
  re-implemented; the recorded state is `added`/`removed` with the one head it shows.
- **Intermediate revisions remain selectable history.** The full retained lists travel on the value,
  and the comparison's own per-side explicit revision selector addresses them — this module removes
  none of them.
- **Kind-agnostic.** The policy asks the same question of invariant and family identities with no
  edge readers; claims and frontier links hold no selectable revisions, so they never establish
  heads.
- **Single-revision records.** One text record holds one revision (MIK-R74 rule 3); there is no
  multi-revision ambiguity for a text tree to express. Family-subject multi-revision choice beyond
  this packet stays R08/R09's; browser rendering of the recorded value stays R25's.

##### Todos

None recorded.

#### Evidence

##### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

##### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and
policy, its three published names, the pure head rule, the entry point's population source, the
one-sided versus two-sided decision and the reused explicit ambiguity. No graph reader remains.

- The module's own statement of the one rule, what it reads, what it returns, and why it is its own module. (historical reference 1)
- The published surface: one value, two readers, one entry point. (historical reference 2)
- The reviewed identity's head selection with the union items its statements render from — and the one-sided item the R06 rendering already reads. (historical reference 3)
- The whole rule in one pure function: every retained revision is a head; sorted order as rendering determinism only. (historical reference 4)
- No edge read: no snapshot is opened for edges and no predecessor table is consulted; populations come from the comparison's own union items. (historical reference 5)
- The one entry point: populations from the comparison's own union, edges from nothing; no-identity selector and empty populations as explicit non-pairs. (historical reference 6)
- Established populations route one-sided for a known-empty side and combine for two nonempty sides; no invalid-graph branch remains. (historical reference 7)
- Two nonempty sides: multi-head ambiguity with no pair, unique heads compared. (historical reference 8)
- A known-empty side stays an R06 addition/removal with the nonempty side's unique head — and a crowded nonempty side is ambiguity, not a one-sided side. (historical reference 9)
- Operands keyed by stored revision identity, never by stream position or both-sides presence. (historical reference 10)
- The adapter's one call site: the selection computed once in `compose_review` from the comparison's union items, rendered by the pane. (historical reference 11)
- The recorded value the policy returns into, with the state/pair/heads validators that make a fabrication unrepresentable. (historical reference 12)
- The cases that measure the policy through the real comparison: single-retained-revision pair, heads-are-retained-population, and text-backed snapshots. (historical reference 13)

##### Cross-Repo References

No cross-repository behavior is implemented in this file. The module reads two snapshot files of one
repository's candidate and carries no identity that ranges beyond the repository namespace the
comparison was opened under.

No meaningful cross-repo references found.

## Evidence

- Selected side ids and their own display versions are forwarded together. [20]
- Four selection states describe the actual chosen operands. [21]
- Identity filtering and first matching side lookup remain explicit. [22]
- The exported helper sorts but is not used by the selector. [23]
