# mcp/src/agents_remember/application/review_committed_leaf.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_committed_leaf.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076` |
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The one owner of a *committed or closed* leaf's review resolution** (`ICR-R12@v1`): the comparison a
leaf's own durable records hold, reopened for a leaf whose worktree cleanup has removed the enclosure.
A live review resolves a candidate *because it has to* — the candidate of a task still being written is
a tree that exists in no commit — and the intake defect this module exists for is that the same route
refused a cleaned leaf with `candidate_not_live` ("the leaf's enclosure has no live worktree, so there
is no candidate to review"), so the ordinary committed diff succeeded while Intent Review could not be
opened at all.

A closed leaf does not need a live candidate, because the comparison it *did* make was published as a
durable generation and its task recorded the commits it landed. Those are the two records this module
resolves from, in this order:

- **a published generation is the authority for the comparison it froze** — the generation's own
  retained snapshots are the two knowledge halves, its two recorded code objects are the bound trees,
  and the root they are read in is the repository the record names. The record is measured against the
  world it names by R11's own reopen owner rather than re-derived here, so a closed leaf's review is the
  comparison it had when it was frozen, byte for byte;
- **a leaf that published no generation still has its recorded source range** — the enclosure contract
  records the base the leaf forked from and the commit its closeout or integration landed, and this
  module exposes that code and reads knowledge.sqlite at the exact recorded memory endpoints. The response explicitly says it was reconstructed rather than previously frozen. A missing, corrupt or undeclared operand retains its own typed state; no current dataset supplies it.

Both resolutions produce the same
[`ReviewCandidateResolution`](review_candidate_resolution.py.md) the live path produces, so **one
composition renders both**, and the surface is told which record answered instead of inferring it.

**The record stays the authority and nothing falls back to today.** A generation whose objects or
snapshots no longer resolve is reported channel by channel with R11's own states; a recorded range the
repository no longer holds is refused by name; and the current branch tip, `HEAD`, a working tree,
another leaf's records and today's knowledge are all unreachable as substitutes. Nothing here writes,
retains, freezes or releases anything: retaining and reopening a generation stay R11's owners, the
source-change inventory stays R02's, and the frozen record bundle stays R14's.

## Code Commentary

### Logic

An explicit `generation_id` selects one named retained comparison through the existing reopen owner. It does not select the newest directory or recreate a worktree. The returned historical resolution keeps `candidate_identity=None`; an explicit successor recovery may consume the manifest's recorded capture only inside the retention owner.

The no-generation branch now reconstructs both exact recorded source and memory endpoints. read_recorded_knowledge owns private knowledge materialization and its lifetime, and the resolution uses the dataset declared namespace. The payload labels reconstructed recorded endpoints explicitly. An existing frozen generation still wins; ambiguous/unreadable frozen history never triggers reconstruction or substitution.

**`resolve_committed_leaf_review` resolves in the packet's own order: the recorded enclosure contract,
then the published generation, then — only when no generation was ever published — the recorded source
range.** The contract is located through `recorded_leaf_contract`, the accessor the *live* resolution
also calls, because two scans of the enclosure directory would be two answers to "which contract is
this leaf's"; a leaf with no readable contract is refused as `candidate_unresolved` naming the
`tasks/<repository>/<master>/enclosures` location the review is addressed from. The generation is then
read by `reopen_comparison_generation` (R11's own owner), and its answer decides the branch: `ambiguous`
or `manifest-unreadable` is refused in the reopen's own words (`_reopen_refusal` carries
`reopened.refusal` when the owner produced one, rather than inventing a sentence about bytes it did not
read), a present manifest takes the generation path, and `manifest is None` takes the recorded-range
path. **No branch reads a worktree**, which is what lets a fresh process reconstruct the same comparison
from the coordination root and the record alone.

**The generation path binds the record's own four endpoints, and deliberately carries no captured
candidate identity.** `_generation_resolution` composes a `ReviewCandidateResolution` whose two
databases are `_half_database`'s answers and whose two code roots are `manifest.source.code_repository_root`
— the repository the record names, which is also the root the live resolution's baseline names, and
therefore the root in which both recorded objects resolve. `candidate_identity` is explicitly `None`:
nothing about a closed enclosure may be re-derived, so the pre-publication recheck
(`require_current_candidate_identity`) has nothing to refuse and leaves the resolution exactly as it was
read. The `closed_leaf` field carries the `ClosedLeafReview` value that names which record answered and
what it measured.

**One half's dataset is read from the generation's own copy, or from the leaf's own disposable
location when the record states the half was never kept.** `_half_database` reads a `retained` binding
out of the generation directory's `COMPARISON_KNOWLEDGE_DIRECTORY` snapshot; for a typed absence it
returns `_disposable_half`, which is the *live* resolution's own expression (the contract's worktree
group, `REVIEW_CANDIDATE_RELATIVE_ROOT`, the half's directory, the dataset name) — so the file is
absent for the reason the record states rather than because this module inferred it from a missing
file. `_retained_namespace` reads the namespace the two halves are opened under from the dataset
identities the generation recorded, falling back to the contract's repository only when the generation
retained no half, which is what the live path reads for a pair with no admission receipt either.

**The recorded-range path reuses R01's committed-range owner and addresses trees rather than
commits.** `_recorded_range_resolution` calls `recorded_committed_range(contract, memory=False)` — the
shipped owner, not a second selection of the two recorded commits — and then `_tree_of` peels the landed
commit to `^{tree}` **in the repository the range names**: the expansion owner refuses a commit, a blob
or a tag by name, so binding the commit itself would publish an inventory whose own entries could not be
opened. A commit that will not peel is `candidate_unresolved` with the restore-or-reopen action, and the
detail names no branch tip and no other leaf's records.

**The refusal a closed leaf's recorded range earns is branched on the endpoint's own kind (the F2 fix
of this leaf's fix round).** `_no_recorded_range_refusal` reads `RecordedEndpointAbsent.kind`:
`not-recorded` — nothing was recorded *and* nothing is live — keeps the packet's original
`candidate_not_live`, which is the one state in which that code is true; `unresolvable` and
`no-repository` are **recorded endpoints that do not resolve**, and they answer `candidate_unresolved`
with a detail naming the kind and the recorded commit. Answering the intake-defect's own code for those
would have applied "there is no candidate to review" to a leaf that recorded exactly the candidate this
surface failed to read, while the sibling "will not peel to a tree" failure already answered
`candidate_unresolved`.

**What the surface declares is three functions over one `ClosedLeafReview`, and the declared-limit
vocabulary is stated once.** `closed_leaf_limitations` publishes the facts a reader acts on as
top-level `kind:value` tokens — which record answered (`history:recorded-comparison` /
`history:recorded-source-range`), which generation it was
(`history:comparison-generation:<id>`), each intent half's state (`history:intent:<side>:<state>`) and a
source channel that is not `available` (`history:source:<state>`). For a resolution with no closed-leaf record it
delegates to `knowledge_unavailable_limitations` (MIK-R25): the tree comparison's facts, the legacy facts, or an
empty tuple for a live dataset candidate, so a live dataset response is byte-identical to the one it always was. `closed_leaf_intent_detail` is
the one sentence a reopened review states about the operand it did not compare, and
`closed_leaf_dataset_refusal` is the refusal the entry route and the subject composition share.

**A state the record itself declares is never rendered as content that was lost (the F1 fix).**
`closed_leaf_dataset_refusal` partitions the half reasons through R11's own `TYPED_ABSENCE_STATES`
(imported, not re-spelled) and words each group separately: `_stated_sentence` states an owner-declared
absence — "no such knowledge content was ever recorded (…), which is a declared absence in the
repository's history and **not** a channel that is unavailable" — and only `_unresolved_sentence` says
the content "does not resolve now … reported unavailable". A generation carrying both kinds is told
both, in that order, because the two answer different questions. `_half_reason` takes the record's own
measured channel state as the first authority and asks the disk only for a half the record retained and
that resolves there, where a missing file is the one genuine surprise and is reported as `missing`
rather than as either absence.

### Conventions

`__all__` publishes the two record names, the three declared-limit prefixes, the closing sentence, the
`ClosedLeafReview` value and the four surface-entry callables (`resolve_committed_leaf_review`,
`closed_leaf_dataset_refusal`, `closed_leaf_intent_detail`, `closed_leaf_limitations`) — the names the
adapter and the task-context composition import, and nothing else. `IntentState` is a `Literal` of the
six states this surface may declare for an intent half: `retained` for a half the generation kept and
that still reads back as the identity that was frozen, the two typed absences that are history
rather than failure — R05's own `not-recorded`, carried as the imported `NOT_RECORDED` when no
generation recorded a half, and R11's `not-selected` channel state — and the three
`_UNAVAILABLE_INTENT_STATES`
(`missing`, `corrupt`, `unavailable-history`) that are deliberately **not** collapsed into either
absence. `_SIDES` fixes the order every report of the two halves uses, and `_HALF_DIRECTORY` /
`_DISPOSABLE_RELATIVE` import the live resolution's own names rather than re-spelling them, so "the half
this leaf would hold" is one path rather than two conventions that agree today. The `TYPE_CHECKING`
import in `review_candidate_resolution.py` is the other side of this module's one local import: the
dependency is one-way at runtime and both modules publish the same resolution value.

### Invariants And Boundaries

- **No worktree is read, and none is created.** Every endpoint is a recorded object id, a retained
  snapshot or the leaf's own recorded range; historical inspection adds no worktree and no checkout.
- **The published record is never re-derived.** The generation is resolved by R11's reopen owner and
  the recorded range by R01's committed-range owner; this module selects and reports, and re-implements
  neither.
- **A closed resolution carries no captured candidate identity, by design.** The recheck belongs to a
  live capture, and ordinary live capture still cannot consume it. Explicit recovery selects an exact generation and asks the existing retention owner to validate its recorded capture without making the resolution live.
- **A declared absence and unavailable content are different facts and are never each other's
  wording.** The partition is R11's own `TYPED_ABSENCE_STATES`, and only the unresolved states are
  called unavailable.
- **The endpoints are trees in the repository the record names.** A recorded commit is peeled to its
  tree in that repository; no branch tip, working tree or current knowledge substitutes for either
  endpoint.
- **`candidate_not_live` survives only where it is true**: a closed leaf that recorded neither a
  comparison nor a landed commit.
- **A converted repository's closed leaf reads no database (MIK-R25 rule 4).** `_converted_repository_resolution`
  reopens a recorded tree comparison from its tree ids, or, for a converted official line with only a dataset
  record, answers `legacy-unavailable` knowledge sides with the code sides kept; an unconverted repository's
  closed leaf takes the dataset path unchanged.
- **The module writes nothing.** It retains, freezes, releases and deletes nothing; every one of those
  decisions remains the owner's it was read from.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: this module's own docstring and
functions, the two owners it resolves through (R11's reopen and R01's committed range), the resolution
value it composes, the adapter and task-context composition that read its declarations, and the case
module that measures the whole chain through the real HTTP route. Three details a reader should carry:
the **resolution** is reached only through `resolve_review_candidate`'s closed-enclosure branch,
so no second entry point composes a historical review — the adapter and the task-context
composition read this module's declaration helpers, never its resolver; the recorded-range path is reached only when **no**
generation exists, so a published record always wins; and the diff of this leaf adds exactly one
suppression (`# noqa: PLC0415 - cycle`, in the resolution module's local import), widening no limit and
silencing no other rule.

| Finding | Anchor | Source |
| --- | --- | --- |
| The historical resolver asks the converted-repository resolution first (MIK-R25: a recorded tree comparison, or a legacy one), then prefers the retained generation and reconstructs exact recorded endpoints only when no generation exists. | `resolve_committed_leaf_review`; "def _generation_resolution("; `_recorded_range_resolution` | mcp/src/agents_remember/application/review_committed_leaf.py:174-216; mcp/src/agents_remember/application/review_committed_leaf.py:364-401; mcp/src/agents_remember/application/review_committed_leaf.py:265-303 |
| **The published surface: the two record names, the three declared-limit prefixes, the closing sentence, the review value and the four entry callables.** | `__all__` | mcp/src/agents_remember/application/review_committed_leaf.py:71-84 |
| **The two records a closed leaf is reopened from, named once because a second spelling would be a second vocabulary.** | `HISTORY_RECORDED_COMPARISON`; `HISTORY_RECORDED_SOURCE_RANGE` | mcp/src/agents_remember/application/review_committed_leaf.py:88-89 |
| **The declared-limit vocabulary every fact is published at the top level of the response under.** | `HISTORY_COMPARISON_PREFIX`; `HISTORY_INTENT_PREFIX`; `HISTORY_SOURCE_PREFIX` | mcp/src/agents_remember/application/review_committed_leaf.py:95-97 |
| **The one sentence the surface publishes when a closed leaf's review is opened, stated here so the entry, the review and the expansion cannot describe the same resolution three ways.** | `CLOSED_LEAF_REVIEW_SENTENCE` | mcp/src/agents_remember/application/review_committed_leaf.py:102-106 |
| **The six intent-half states this surface may declare: its own `retained`, the two typed absences that are history (R05's `not-recorded`, R11's `not-selected`), and the three unresolved states kept apart from them.** | `IntentState`; `_UNAVAILABLE_INTENT_STATES` | mcp/src/agents_remember/application/review_committed_leaf.py:112-119; mcp/src/agents_remember/application/review_committed_leaf.py:122-124 |
| **The record one closed leaf's review was reopened from: the reopen owner's own answer, the two bound trees, and the two properties that name which record answered and which half channel it measured.** | `ClosedLeafReview`; `state`; `intent` | mcp/src/agents_remember/application/review_committed_leaf.py:127-171 |
| **The whole resolution, in the packet's order: the recorded contract, R11's reopen, the reopen's own refusal for an unreadable record, and the generation-or-range branch.** | `resolve_committed_leaf_review`; `recorded_leaf_contract`; `reopen_comparison_generation` | mcp/src/agents_remember/application/review_committed_leaf.py:174-216; mcp/src/agents_remember/application/review_candidate_resolution.py:490-517; mcp/src/agents_remember/application/review_comparison_reopen.py:228-249 |
| **An unreadable or ambiguous generation refused in the reopen's own words rather than in a sentence invented here.** | `_reopen_refusal` | mcp/src/agents_remember/application/review_committed_leaf.py:245-259 |
| **The generation resolution: the two retained snapshots, the record's own two code objects read in the repository the record names, and the deliberately absent captured identity.** | `_generation_resolution` | mcp/src/agents_remember/application/review_committed_leaf.py:265-303 |
| **One half's dataset: the generation's own retained copy, or the leaf's own disposable path when the record states the half was never kept.** | `_half_database`; `_disposable_half` | mcp/src/agents_remember/application/review_committed_leaf.py:306-325; mcp/src/agents_remember/application/review_committed_leaf.py:328-337 |
| **The namespace the retained halves are read under, taken from the dataset identities the generation recorded.** | `_retained_namespace` | mcp/src/agents_remember/application/review_committed_leaf.py:340-358 |
| **The recorded-range resolution: R01's committed-range owner, the two recorded endpoints, and the explicit statement that no generation was published.** | `_recorded_range_resolution`; `recorded_committed_range` | mcp/src/agents_remember/application/review_committed_leaf.py:364-401; mcp/src/agents_remember/serving/changeset_endpoints.py:87-125 |
| **The endpoint is a tree, resolved in the repository the range names, because the expansion owner refuses a commit, a blob or a tag by name.** | `_tree_of` | mcp/src/agents_remember/application/review_committed_leaf.py:404-429 |
| **The F2 fix: the refusal branched on the endpoint's own kind, so a recorded endpoint that does not resolve is `candidate_unresolved` and only "nothing live and nothing recorded" keeps `candidate_not_live`.** | `_no_recorded_range_refusal`; `RecordedEndpointAbsent` | mcp/src/agents_remember/application/review_committed_leaf.py:432-472; mcp/src/agents_remember/serving/changeset_endpoints.py:68-84 |
| **The declared facts one reopened review publishes; without a closed-leaf record it delegates to the tree or legacy facts (MIK-R25), which are the empty tuple for a live dataset candidate, so a live dataset response is unchanged.** | "def closed_leaf_limitations(" | mcp/src/agents_remember/application/review_committed_leaf.py:478-511 |
| **The one sentence a reopened review states about the operand it did not compare, with the record's own state deciding which fact leads.** | `closed_leaf_intent_detail`; `_intent_sentence` | mcp/src/agents_remember/application/review_committed_leaf.py:514-526; mcp/src/agents_remember/application/review_committed_leaf.py:651-704 |
| **The F1 fix: the refusal the entry route and the subject composition share, partitioning the half reasons through R11's own typed-absence set and wording a declared absence apart from a channel that is unavailable.** | `closed_leaf_dataset_refusal`; `_stated_sentence`; `_unresolved_sentence`; `TYPED_ABSENCE_STATES` | mcp/src/agents_remember/application/review_committed_leaf.py:529-593; mcp/src/agents_remember/application/review_committed_leaf.py:604-612; mcp/src/agents_remember/application/review_committed_leaf.py:615-624; mcp/src/agents_remember/application/review_comparison_generation.py:151-151 |
| **Which half cannot be compared and why: the record's own channel state first, the disk asked only for a half the record retained.** | `_half_reason`; `_half_present`; `_intent_state` | mcp/src/agents_remember/application/review_committed_leaf.py:627-641; mcp/src/agents_remember/application/review_committed_leaf.py:644-648; mcp/src/agents_remember/application/review_committed_leaf.py:707-718 |
| **The two halves in the order every report of them uses, and the two directory names imported from the live resolution rather than re-spelled.** | `_SIDES`; `_HALF_DIRECTORY`; `_DISPOSABLE_RELATIVE` | mcp/src/agents_remember/application/review_committed_leaf.py:722-722; mcp/src/agents_remember/application/review_committed_leaf.py:727-727; mcp/src/agents_remember/application/review_committed_leaf.py:731-731 |
| **The value this resolution is composed into, and the field that carries the record rather than a live capture.** | `ReviewCandidateResolution`; `refusal` | mcp/src/agents_remember/application/review_candidate_resolution.py:132-177; mcp/src/agents_remember/application/review_candidate_resolution.py:494-508 |
| **The single entry point: the closed-enclosure branch that delegates here, with the one local import this leaf's diff suppresses and the reason it is local.** | `resolve_review_candidate` | mcp/src/agents_remember/application/review_candidate_resolution.py:180-242 |
| **The reopen owner's answer this module reads rather than restates: the manifest, the per-channel states and the refusal an ambiguous or unreadable record earns.** | `ComparisonReopen`; `ComparisonKnowledgeChannel` | mcp/src/agents_remember/application/review_comparison_reopen.py:136-151; mcp/src/agents_remember/application/review_comparison_reopen.py:164-225 |
| **The two routes that publish these declarations: the entry refusal and the review's declared limits.** | `list_knowledge_review_entries`; `compose_review` | mcp/src/agents_remember/application/knowledge_review.py:257-318; mcp/src/agents_remember/application/knowledge_review.py:335-577 |
| **The case module that measures the whole chain through the real composition and the real HTTP route.** | `test_a_closed_leaf_serves_its_recorded_comparison_byte_for_byte`; `test_a_pre_feature_leaf_exposes_its_recorded_source_range_and_its_absence` | mcp/tests/test_historical_committed_leaf_review.py:257-324; mcp/tests/test_historical_committed_leaf_review.py:387-446 |

| `_recorded_range_resolution` owns the behavior described above. | `_recorded_range_resolution` | mcp/src/agents_remember/application/review_committed_leaf.py:364-366 |
| `_generation_resolution` owns the behavior described above. | `_generation_resolution` | mcp/src/agents_remember/application/review_committed_leaf.py:265-267 |
| `resolve_committed_leaf_review` owns the behavior described above. | `resolve_committed_leaf_review` | mcp/src/agents_remember/application/review_committed_leaf.py:174-176 |

The following declarations carry the changed boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| An explicit generation is resolved through the same committed-leaf owner. | `resolve_committed_leaf_review` | mcp/src/agents_remember/application/review_committed_leaf.py:174-216 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one coordination root's task tree
and the records of one leaf's enclosure, and it carries no identity that ranges beyond the repository
namespace the request names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`knowledge_review.py`) moved with the leaf's inserted lines: 3 passing row(s) normalised by the fixer. The fixer's normalisation also re-measured ranges into files this leaf did not change (`review_candidate_resolution.py`). No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T04:01:40+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): **body updated for MIK-R25.** Added the section "260928-MIK-L25 A Converted Repository's Closed Leaf Reads Trees, Or Reports Legacy-Unavailable": `_converted_repository_resolution` before the generation path, and the three declaration helpers delegating to `review_legacy_comparison` when no closed-leaf record answers; one row. **Two reopened claims re-read, reworded and re-anchored:** the historical-resolver row and the `closed_leaf_limitations` row. Their committed generated-repair bullets (2026-09-26T21:14:45+00:00) are left intact, so both rows are re-anchored on the line-exact quotes "def _generation_resolution(" and "def closed_leaf_limitations("; the two bullets this pass's fixer wrote for them were removed. The Logic paragraph on `closed_leaf_limitations` was updated. **Already-stale rows re-measured:** the `_recorded_range_resolution` and `_generation_resolution` declaration rows (base `315-317` and `216-218`, which no longer held the declarations even at the base) now cite `364-366` and `265-267`. The other rows were projected or normalised by the installed fixer, or re-pointed by exact line shift. No verification stamp was advanced.
- 2026-09-30T01:46:18+00:00: Generated citation repair: `HISTORY_RECORDED_COMPARISON`; `HISTORY_RECORDED_SOURCE_RANGE` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:88-88; mcp/src/agents_remember/application/review_committed_leaf.py:89-89. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:46:18+00:00: Generated citation repair: `HISTORY_COMPARISON_PREFIX`; `HISTORY_INTENT_PREFIX`; `HISTORY_SOURCE_PREFIX` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:95-95; mcp/src/agents_remember/application/review_committed_leaf.py:96-96; mcp/src/agents_remember/application/review_committed_leaf.py:97-97. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:46:18+00:00: Generated citation repair: `CLOSED_LEAF_REVIEW_SENTENCE` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:102-106. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:46:18+00:00: Generated citation repair: `ClosedLeafReview`; `state`; `intent` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:127-171; mcp/src/agents_remember/application/review_committed_leaf.py:151-155; mcp/src/agents_remember/application/review_committed_leaf.py:163-171. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:46:18+00:00: Generated citation repair: `_retained_namespace` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:340-358. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-28T17:15:39+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/src/agents_remember/application/knowledge_review.py`) were re-pointed to where the same anchors now sit; each re-pointed row held its anchors at the base and holds them after the base-to-candidate line mapping. Claim wording unchanged. No stamp advanced.

- 2026-09-27T05:30:43+00:00 — Authored scoped citation maintenance for 11 L41 source-range projection(s) resolved by the frozen source index. Only changed-source ranges were adopted from the preview; unrelated ranges, generated history and verification stamps are preserved.

- 2026-09-27T05:23:46+00:00 — Re-resolved 3 source-linked citation claim(s) against the extracted or shifted L41 owners. Each selected symbol uses its current declaration extent; other source references and prior generated history remain unchanged. Verification stamps remain closeout-owned.

- 2026-09-27T04:56:35+00:00 — Documented exact-generation selection and the strict separation between historical resolution and live capture. Verification hashes/dates remain closeout-owned.
- 2026-09-26T21:14:45+00:00: Generated citation repair: `__all__` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:60-73. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:45+00:00: Generated citation repair: `HISTORY_RECORDED_COMPARISON`; `HISTORY_RECORDED_SOURCE_RANGE` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:77-77; mcp/src/agents_remember/application/review_committed_leaf.py:78-78. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:45+00:00: Generated citation repair: `HISTORY_COMPARISON_PREFIX`; `HISTORY_INTENT_PREFIX`; `HISTORY_SOURCE_PREFIX` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:84-84; mcp/src/agents_remember/application/review_committed_leaf.py:85-85; mcp/src/agents_remember/application/review_committed_leaf.py:86-86. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:45+00:00: Generated citation repair: `CLOSED_LEAF_REVIEW_SENTENCE` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:91-95. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:45+00:00: Generated citation repair: `IntentState`; `_UNAVAILABLE_INTENT_STATES` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:101-108; mcp/src/agents_remember/application/review_committed_leaf.py:111-113. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:45+00:00: Generated citation repair: `ClosedLeafReview`; `state`; `intent` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:116-160; mcp/src/agents_remember/application/review_committed_leaf.py:140-144; mcp/src/agents_remember/application/review_committed_leaf.py:152-160. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:45+00:00: Generated citation repair: `_reopen_refusal` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:196-210. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:45+00:00: Generated citation repair: `_generation_resolution` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:216-254. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:45+00:00: Generated citation repair: `_half_database`; `_disposable_half` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:257-276; mcp/src/agents_remember/application/review_committed_leaf.py:279-288. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:45+00:00: Generated citation repair: `_retained_namespace` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:291-309. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:45+00:00: Generated citation repair: `_tree_of` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:355-380. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:45+00:00: Generated citation repair: `closed_leaf_limitations` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:429-462. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:45+00:00: Generated citation repair: `_SIDES`; `_HALF_DIRECTORY`; `_DISPOSABLE_RELATIVE` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:670-670; mcp/src/agents_remember/application/review_committed_leaf.py:675-675; mcp/src/agents_remember/application/review_committed_leaf.py:679-679. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — Reconciled the changed ownership and current behavior with the source.
- 2026-09-23T05:05:00+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): created this one-to-one card for the module this leaf introduced to reopen a **committed or closed** leaf's code-and-intent comparison from its own durable records (`ICR-R12@v1`). The card records the intake defect it removes (a cleaned leaf's Intent Review answered `candidate_not_live`), the two records it resolves from and their order, why both resolutions produce the value the one composition already renders, the per-kind refusal of the recorded-range path, and the declared-limit vocabulary the response publishes. **The two findings of this leaf's fix round are recorded as current behaviour rather than as history**: the F1 partition of a state the record itself declares away from content that is unavailable, and the F2 branch that keeps `candidate_not_live` for the one state in which it is true. **Stamp accounting:** the verification pair names the production line at this leaf's base — the last real commit the reading was taken against — because every construct this card cites exists only in this leaf's uncommitted candidate; the governed closeout owns the real stamp once the code commit exists.

## 260928-MIK-L25 A Converted Repository's Closed Leaf Reads Trees, Or Reports Legacy-Unavailable

**MIK-R25 rule 4.** `resolve_committed_leaf_review` now calls `_converted_repository_resolution` before R11's
generation reopen:

- a leaf that recorded a tree comparison reopens from its tree ids (`review_tree_comparison.reopen_review_trees`
  and `tree_resolution`); a tree Git can no longer produce is `unavailable-history`, named, never substituted;
- a leaf whose repository's official memory line is converted (`official_line_converted`) but which recorded only a
  dataset comparison, or only a committed range, is answered by `review_legacy_comparison.legacy_comparison_resolution`:
  code sides kept, knowledge sides `legacy-unavailable`, or four committed trees when the recorded memory endpoints
  are converted;
- every other leaf (an unconverted repository's) returns `None` here and keeps the dataset path below unchanged.

`closed_leaf_limitations`, `closed_leaf_intent_detail` and `closed_leaf_dataset_refusal` delegate to
`knowledge_unavailable_limitations`, `knowledge_unavailable_detail` and `knowledge_unavailable_refusal` when no
closed-leaf record answers, so a tree or legacy comparison declares its own facts and refusal. The pre-existing
radon C scores here were accepted (review F8, ruling 23:15:34).

| Finding | Anchor | Source |
| --- | --- | --- |
| A recorded tree comparison reopened, a converted repository's legacy answer, or none for the dataset path. | `_converted_repository_resolution` | mcp/src/agents_remember/application/review_committed_leaf.py:219-242 |
