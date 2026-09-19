# mcp/src/agents_remember/application/knowledge_curator_ingest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_curator_ingest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T17:08+02:00 |
| lastVerifiedCommitHash | `562cef4ca64de5b11712d5165d24e78c9a035312` |
| lastVerifiedCommitDate | 2026-09-19T17:51:43+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

This is the curator's reachable ingest: the layer above `knowledge_ingest`'s write half. One
orchestrator hand-off list (revision 1's JSON entries) goes in; one admitted candidate batch and one
report come out. It owns every step between the list and the record — admit the destination, complete
each target path, read the identity that path really holds, verify the locator against those bytes,
observe each anchor against the recorded tree, author the governing routes, commit the whole list
through the closed write path, and report every entry's outcome so the run is auditable afterwards.

The module's first distinction is that three cases are never conflated. A ruling that carries no
target (`target: []`) is **skipped**, with the producer's own `disposition` and `disposition_source`
carried into the report, because there is no construct to cite and recording one would invent a claim
the producer never made. A non-empty target that does not resolve is **refused**, with the exact
reason, because the producer named a place the curator cannot verify. An entry is **committed** only
when every one of its targets resolved, verified and observed. Nothing the operation can *read* makes
it raise: unreadable identities, unresolvable paths and unverifiable locators all arrive as typed
refusals, because a traceback would break the promise that every entry's outcome is reported.

Why it matters: this is the only place where an unlanded draft's citations become recordable. A leaf
cites the code its own line is producing, so the tree a target is resolved against is the leaf's own
code work branch tip rather than the enclosure's recorded base commit, while the identities the run
mints stay anchored to that base. The split is what lets a leaf add and modify files and still cite
them, and what keeps an identity stable as the line advances.

It refuses to be a general citation tool: no symbol extractor, no onboarding writer, no export
builder, no widening to a third root, and no publication — that is the curator's later act and is not
reachable from here. Its public surface is one entry point plus the vocabulary its report is read with.

## Code Commentary

### Logic

**The entry point, and what each mode returns.** `ingest_curator_list(contract_path, entries, *,
candidate_directory, authorization_ref, dry_run=False) -> IngestReport` is the whole operation. It
refuses a blank `authorization_ref` by name before anything is read (`_require_authorization`, a
`ValueError` — the operation's own input contract, not a per-entry refusal), loads the enclosure
contract, binds the two roots (`_roots`, which requires the recorded memory worktree), derives the
resolution trees and the coordination root's top-level names once for the run, then reads and plans
the list. `dry_run=True` returns the identical report with the commit withheld; the real path builds
the authorship envelope (`write_authorship` with `actor_ref` and `authorization_ref` both set to the
one required reference, `origin_refs=("curator-handoff:revision-1",)`), admits or creates the
candidate, and calls `_run`. One required authorization reference rather than two optional ones is
deliberate: "who authorized this" and "who authored it" stay the same admitted fact.

**Admission is resume-or-create, and a refusal is the product's own.** `_admitted_candidate` opens an
existing candidate directory (`open_knowledge_candidate`) instead of initializing over it — the bytes
there are unpublished authored work — and creates it (`create_knowledge_candidate`) only when the
directory is absent. The repository namespace is a `uuid5` under the fixed `_INGEST_NAMESPACE` over
the enclosure's recorded base commit (`_repository_identity`), and the `CandidateResolution` is read
from the enclosure's recorded pair rather than asserted: lane `draft-candidate`, the two trees, the
recorded base commits, and `task_ref` = leaf id or task name (`_resolution`). A refused or
identity-less admission returns a report with `batch_state="not_attempted"` carrying the product's
typed refusal.

**Reading the list: the list is data, and a refusal keeps what its entry already established.**
`_read_entries` accepts the parsed list or the path of the JSON file carrying it and parses no prose; a
non-list, a non-object entry, a missing `id` and a duplicate `id` are `ValueError`s raised before
anything is written. Per entry, `_plan_entry` reads the producer-side fields once
(`_EntryFields.read`) and either builds a ruling plan (no target at all) or plans every target; a
target that refuses returns immediately with the places its earlier targets already completed
(`_refused_targets`) carried in the refusal, so the report's entry accounting and its target
accounting describe the same run instead of a refusal erasing its neighbour. Two targets in one entry
that complete to the same path are refused as `duplicate_target_path` (an inline code, not a module
constant).

**Completing a path: three recorded steps, and the identity is measured rather than restated.**
`_complete_target` asks exactly three places, in order: `<code_root>/<path>` against the code
resolution tree, then `<memory_root>/onboarding/<path>`, then `<memory_root>/<path>`. Membership is
the tree's own answer (`Trees.source_candidate.members`) and the answering root travels out with the
path so the blob is read from that same tree — a memory path's blob lives in the memory tree. `_member`
then reads the working bytes' blob id (`git hash-object --no-filters`) and compares it with the blob
the tree records (`_BlobIdentity.exact`); disagreement is the `recorded_blob_mismatch` refusal saying
the bytes about to be cited are not the bytes the resolution tree holds — what an uncommitted edit to a
cited file looks like — which is what keeps the recorded identity a measurement of the file rather
than a restatement of the tree's own answer. Spelling is settled before any tree is asked
(`_spelling_refusal`): an absolute path that points inside an admitted root is refused as
`path_inside_admitted_root_spelled_absolutely`, one that points outside as
`path_outside_admitted_roots`, a `..` segment as `path_not_confined_by_spelling`, and a leading `./`
is normalised and allowed through (`_confined`).

**A path that resolves nowhere is refused under one code, with the reason that is true of it.** The
code is `target_path_unresolved` and the reason opens with one of three names decided from the
recorded trees and the path's own spelling — never from `is_file()` on a live directory, because the
enclosure's cleanup deletes task-tree files and a reason that changed with them could not be
reproduced from the record the citation was written against. `top_level_entry_file_gone` when the
first segment is a real top-level entry of one of the two admitted trees; `third_root_out_of_scope`
when the path names something under the coordination root that neither admitted tree holds; and
`dependency_source_not_ours` when it names neither. `_coordination_top_level` reads the coordination
root's directory names once per run (minus the two admitted roots) and carries them, so one entry's
reason cannot depend on what still existed when that entry happened to be read.

**The locator is verified in the same act as the path.** `_locator` refuses a null locator as
`target_locator_missing` instead of promoting it to a whole-file citation (a path and the construct
inside it are one act, and "the whole file is the place" is a claim a producer must make explicitly),
refuses an unknown kind as `unsupported_locator_kind`, and dispatches `file`, `line_range` and
`symbol`. A range earns the reason true of *this* range, one code each: `line_range_not_integer_bounds`,
`line_range_not_one_based`, `line_range_not_ordered`, and `line_range_past_last_line` measured against
the recorded member's own line count. A symbol is the producer's bare name normalised into the model's
two-part locator: the name comes from `value` or `qualified_name` (`symbol_name_missing` when absent),
the language is derived from the recorded path's extension (`symbol_language_underdetermined` when the
table does not know it), markdown is refused as `symbol_target_is_prose` and a structured data file
under the same code with its own sentence, and the name must be *defined* in the file — a mention
earns `symbol_not_a_definition`, an absence earns `construct_not_in_named_file`.

**"Defined" is decided by the shipped parser, and by exactly one implementation of the rule.**
`_symbol_locator` hands the one file the path resolved to `bound_definitions` from
`memory_quality/style/citations/extents.py`, which asks `grammars.bindings` — the same tree-sitter
machinery the citation fixer, repair and migration paths use. That function checks the last segment of
a qualified name *and* every segment before it, so a genuinely nested construct resolves while an
invented prefix cannot borrow a real method's identity, and a name that occurs only inside a docstring,
a comment or a string is bound nowhere because the parser never binds it. There is no second definition
detector here: the regex tables, the comment/literal blanking and the per-language declaration patterns
that used to live in this module (`_defines`, `_declares`, `_code_only`, `_blank`,
`_PYTHON_DEFINITION`, `_CODE_DEFINITIONS`, `_PYTHON_LITERAL`, `_SCRIPT_LITERAL`, `_CODE_LITERALS`) were
deleted, because two notions of "a definition" in one tree can drift and nothing keeps them equal.
A consequence worth knowing: a language the shipped extractor has no grammar for — `shell`, `sql`,
`.pyi` — is now refused at this boundary as `symbol_language_underdetermined` rather than accepted, so
a symbol the read rail could never re-resolve is not stored in the first place. `_occurs` anchors at
the name's *start* only, so a file holding `resolve_budget_v` does contain the `resolve_budget` a
producer wrote — which is exactly why that case is refused as "not a definition" rather than "does not
occur".

**The anchor is observed against the tree its path resolved in, and a symbol is resolved.** `_observe`
builds the exact `SourceAnchorDraft` the write path will store (a real UUID from `_observation_id`, the
confined path, `GitBlobIdentity(object_id=resolved.blob)`, the locator) and hands it to
`observe_anchor(repository_root=resolved.root, tree_id=resolved.tree_id)`. `SourceIndexError` and
`OSError` raised by the rail stop being exceptions at this point and become
`observation_<ErrorClass>` refusals, and exactly one answer passes for every locator kind, the symbol
kind included: `exact_recorded_blob`, which the rail earned by reading the recorded blob out of the
requested tree and binding the symbol inside it. Every other answer is refused as
`observation_<answer>` with the rail's detail, so a stored symbol citation is one the read path can
re-resolve rather than one it can only refuse.

**The route leg runs through the primitives, not the batch.** The closed command union's only route
member names a *family revision*, and authoring a family per entry would fabricate grouping structure
the producer never declared — the one thing the curator must not do. So `_author_routes` runs first (a
route that cannot be recorded refuses the list by name, `route_not_recorded`, attributed to every entry
that named a route, before anything is committed) inside one transaction under
`store.exclusive_candidate_lock("author_route")`; each distinct scope is asked about first
(`routes.route_for_path`) because `routes.author_route` answers an existing path by returning that
row's id without writing, so the idempotent answer can be classified as authored or reused; and a
partial author rolls back. `_attach_routes` runs *after* the batch, because the governed row is the
anchor the batch wrote and the union carries no command that sets a route on an anchor: one transaction
under `set_governing_route`, one `routes.set_governing_route` per target, with the six states
`authored`, `reused`, `attached`, `authored-not-attached`, `ungoverned` and `refused` — `ungoverned`
being a fact about a target that named no route rather than a default.

**The commit is one batch for the whole list.** `_curator_entry` turns each plan into the write
module's `CuratorEntry` (invariant id, revision id, `display_version` `v1`, the one authored
applicability string, conditions carrying the producer's kind/disposition/disposition_source/evidence,
and one `CuratorCitation` per target via `_TargetPlan.citation()`), and `_commit` calls
`commit_curator_entries`, which is one `curator_batch` through the closed write path. The operation is
all-or-nothing: a refused batch means nothing was committed, every planned entry is reported refused
with the batch's own code (`batch_<code>`, or `batch_refused` when there was no result), and the
batch's typed `KnowledgeRefusal` travels beside the report in `batch_refusal`. `_role_for` states the
role the ingest authored rather than leaving the edge's meaning to a reader: `primary-authority` for a
file or a range, `enforcement` for a symbol.

**The report is the operation's other half, and a dry run is the same report with the commit
withheld.** `IngestReport` names the contract and candidate directory, the receipt path, the lane,
both trees and where the code tree came from, the repository id, the identity-derivation sentence,
every entry id it read, the three outcome tuples, the counts, the batch state and its digests before
and after, and the batch refusal. `IngestCounts` carries fourteen counts, of which `targets_completed`
(every place whose path completed, in a committed entry *and* in a refused one) and `locators_resolved`
(the places that reached the batch with a locator verified into the model's union) are deliberately two
different measurements. `EntryOutcome`, `TargetOutcome` and `RouteOutcome` are the per-entry,
per-target and per-route renderings. A dry run returns the identical shape from `_projected`, which is
arithmetic over the plans the run already built rather than a second construction of the batch, and its
route states are projected as `authored` because a dry run never read the candidate, so claiming
`reused` would be a fact it did not measure.

**The written-row count is corrected arithmetic, not a receipt length.** `_Run.written` returns zero
for a run with no committed batch, however much its route leg did, and otherwise adds the batch's
distinct `(table, record_id)` rows — the write path reports the anchor a claim cites a second time when
the same batch wrote it (D-42), so the raw receipt length overstates rows by one per citation — to the
route leg's own rows: one `route` row per scope **this run authored** (not per scope it answered) plus
one association per governed anchor the candidate accepted. `_counts` reads every count from the
outcome it counts rather than recomputing it; the mismatch, absent and unavailable observation counters
can only be counted from committed targets, which by construction carry `exact_recorded_blob` or
`unsupported_locator`.

### Conventions

- **One spelling per fact.** The three outcome words (`COMMITTED`, `REFUSED`, `SKIPPED`), the refusal
  codes, the route states, the observation answers and the three path-completion step names are module
  constants, so a reader of the report and a caller branching on it name the same words. Codes used
  once are inline strings at their use site (`duplicate_target_path`, `target_path_unresolved`,
  `route_not_recorded`, `batch_refused`).
- **Everything internal is a frozen dataclass with a leading underscore and a docstring stating the
  distinction it exists to keep.** The public surface is `__all__`'s nine names: `ingest_curator_list`
  is the operation, and the other eight are the outcome words and the report vocabulary a caller reads
  it with.
- **Refusals are values; exceptions are the operation's own input contract.** `_Refusal` before the
  batch and `EntryOutcome.refusal` strings in the report are the failure vocabulary; the raises are a
  blank authorization, a contract recording no memory worktree, a malformed or duplicated hand-off
  list, and a tree the recorded commit cannot name. Anything else that is not one of the citation
  machinery's named conditions propagates deliberately: a defect in this module is not a refusal, and
  dressing one as a refusal would be the same failure pointed the other way.
- **Identities are derived, never random.** `uuid5` under one fixed namespace over the enclosure's
  recorded base commit, which identity it is (invariant, revision, anchor, claim, route) and the
  entry's own id — plus the written path for a target, because a target carries no identity of its own
  in revision 1. Two runs of one list mint the same ids, and a second run is diagnosable rather than
  duplicated.
- **The producer's vocabulary is carried, not re-derived.** `kind`, `disposition` and
  `disposition_source` travel into the report and into the revision's conditions unchanged; the ingest
  authors only the fields the list does not carry (version `v1`, applicability, the realization role)
  and says so in the report.

### Invariants And Boundaries

- **Three outcomes, never merged.** An entry appears in exactly one of `committed`, `rulings` or
  `refused`. A ruling is reported skipped with the producer's verdict carried, never committed as an
  obligation with no realization; an entry is committed only when every one of its targets resolved,
  verified and observed.
- **No readable input makes the operation raise.** Unreadable identities, unresolvable paths,
  unverifiable locators and the rail's raised boundary conditions all arrive as typed refusals in the
  report; only the operation's own input contract (and a genuine defect) raises.
- **The resolution tree and the identity anchor are two different commits on purpose.** Citations
  resolve against the leaf's own code line — the work branch by name, else the worktree's `HEAD`, else
  the recorded base with `code_tree_source` naming the fallback — while the memory side stays the
  recorded memory base and every derived identity stays anchored to the recorded code base commit,
  because identity is a fact about which leaf this is and must not move when the line advances. Every
  report names both trees.
- **A reason is reproducible from the record.** Unresolved-path reasons are decided from the recorded
  trees and the path's own spelling, and the coordination root's top-level names are read once per run
  — never from the live filesystem per entry, so the same citation earns the same reason after the
  enclosure's cleanup has deleted the files it described.
- **The recorded blob identity is a measurement.** Membership is the tree's answer and the working
  bytes are hashed and compared with it; a disagreement is refused rather than recorded, so an
  uncommitted edit cannot be cited as the tree's content.
- **The route does not travel through the batch, and the report says so.** No family is invented per
  entry; the two legs are separate transactions over the candidate, and
  `routes.author_route`'s idempotence plus `routes.set_governing_route`'s one-route-per-governed-row
  constraint are what make repetition safe rather than assumed.
- **Boundary.** No symbol extractor (a symbol locator is carried and observed, and the rail answers
  `unsupported_locator` for it), no onboarding write, no export, no third root, no publication, no lane
  parameter (the `draft-candidate` lane is the only one it admits), and no candidate-directory
  convention (the caller names it and the report echoes it). In this revision no MCP tool imports the
  operation: a repository-wide search finds `ingest_curator_list` imported only by the module's own
  test population, so the caller is the curator seat rather than a tool surface.

### Todos

Two module constants are declared with their rationale and never referenced: `_RULING_SHAPE`
(`"empty_target_ruling"`, described as the one shape an empty target is reported under) and
`_NO_REFUSAL` (how a blank per-target refusal reads). Nothing in the report carries either name today —
a ruling is reported through `EntryOutcome.state` being `SKIPPED`, and a committed target's refusal is
the empty-string default on `TargetOutcome.refusal` — so the two comments document an intent the code
does not yet exercise. Everything else this module states about its own limits is a deliberate boundary
recorded above (no symbol extractor, no onboarding write, no third root, no export, publication out of
reach), not an outstanding task.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped revision: the module's own docstring and
functions, the write module whose entries it builds, the route and observation primitives it calls,
the model vocabulary it constructs, the hand-off list contract it reads, and the cases that measure
each behaviour. Two details a reader should carry: the resolution tree is the leaf's own code line
while every derived identity is anchored to the recorded base commit, and the route leg is two
transactions outside the batch because the closed command union has no command that sets a route on an
anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the job and of the three cases that are never conflated, beside its statement of what it refuses to be (no symbol extractor, no onboarding, no export, no third root, no publication). | "Three cases, never conflated."; "What this module does not do." | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1-64; mcp/src/agents_remember/application/knowledge_curator_ingest.py:59-63 |
| The no-exception promise, and the one boundary where the citation machinery's raised conditions become refusals instead of a traceback. | "No failure is an exception."; `_plan_target` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:41-46; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1149-1177 |
| The published surface (`ingest_curator_list` plus eight report-vocabulary names), the operation itself with its required authorization and dry-run mode, and the run that authors routes, commits one batch, attaches routes and reports. | `__all__`; `ingest_curator_list`; `_run` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:117-127; mcp/src/agents_remember/application/knowledge_curator_ingest.py:700-794; mcp/src/agents_remember/application/knowledge_curator_ingest.py:797-830 |
| Admission as resume-or-create, the enclosure-derived repository namespace, the resolution read from the recorded pair, the enclosure string identity derives from, and the contract and loader those facts come from. | `_admitted_candidate`; `_repository_identity`; `_resolution`; `_enclosure`; `WorktreeContract`; `load_contract` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:877-895; mcp/src/agents_remember/application/knowledge_curator_ingest.py:898-909; mcp/src/agents_remember/application/knowledge_curator_ingest.py:912-925; mcp/src/agents_remember/application/knowledge_curator_ingest.py:928-935; mcp/src/agents_remember/worktrees/worktree_contract.py:234-286; mcp/src/agents_remember/worktrees/worktree_contract.py:437-468 |
| The three outcome words, and the ruling path that reports an empty-target entry as skipped with the producer's verdict carried rather than committing it. | `COMMITTED`; `REFUSED`; `SKIPPED`; `_ruling_plan` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:131-131; mcp/src/agents_remember/application/knowledge_curator_ingest.py:132-132; mcp/src/agents_remember/application/knowledge_curator_ingest.py:133-133; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1126-1146 |
| The report and count shapes a caller reads, the two measurements kept apart, and the written-row arithmetic (distinct batch rows plus authored route rows) that a dry run projects from the same plans. | `IngestReport`; `IngestCounts`; `EntryOutcome`; `TargetOutcome`; `RouteOutcome`; `_counts`; `written`; `_projected` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:363-397; mcp/src/agents_remember/application/knowledge_curator_ingest.py:343-360; mcp/src/agents_remember/application/knowledge_curator_ingest.py:329-340; mcp/src/agents_remember/application/knowledge_curator_ingest.py:303-316; mcp/src/agents_remember/application/knowledge_curator_ingest.py:319-326; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2403-2446; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2306-2331; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2206-2231 |
| The resolution tree versus the identity anchor, the work-branch-then-HEAD-then-base line lookup, and the observation rail the anchor is handed to, with the error type whose raise that boundary converts. | `_TreeIds`; `_tree_ids`; `_code_line`; `observe_anchor`; `SourceIndexError` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:454-468; mcp/src/agents_remember/application/knowledge_curator_ingest.py:949-974; mcp/src/agents_remember/application/knowledge_curator_ingest.py:977-991; mcp/src/agents_remember/memory/knowledge/read_anchors.py:101-174; mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:64-65 |
| The three-step path completion, the tree-membership check, the measured working-blob identity compared with the recorded blob, and the normalisation of a leading `./`. | `_complete_target`; `_member`; `_working_identity`; `_BlobIdentity`; `_confined` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1288-1325; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1328-1365; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1368-1398; mcp/src/agents_remember/application/knowledge_curator_ingest.py:490-505; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1238-1244 |
| The three reasons a confined path earns, the first-segment ownership test read from the trees, the third-root test against the coordination root, its once-per-run top-level read, and the lexical containment helper. | `_unresolved_reason`; `_first_segment_admitted`; `_outside_the_roots`; `_coordination_top_level`; `_within` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1408-1448; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1451-1467; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1470-1490; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1493-1511; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1514-1528 |
| The locator gate that refuses a missing locator rather than promoting it, the four range refusals with one code each, the symbol path from bare name to two-part locator, the language and prose/structured refusals, and the extension table lookup. | `_locator`; `_range_locator`; `_symbol_locator`; `_symbol_language`; `_language_of` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1531-1566; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1569-1613; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1616-1656; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1659-1689; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1692-1701 |
| The extension table a symbol's language name is derived from, and the extractor that decides whether a name is a *definition* — now the shipped tree-sitter one, called through `bound_definitions` rather than reimplemented here. | `_LANGUAGES`; `bound_definitions`; `grammars.parsed` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:230-241; mcp/src/agents_remember/memory_quality/style/citations/extents.py:107-134; mcp/src/agents_remember/memory_quality/style/citations/grammars.py |
| The symbol boundary and its refusal codes: the qualified-name resolution through the shipped extractor, the locator's language derivation, and the mention-versus-absence distinction — with no second definition implementation beside it. | `_symbol_locator`; `_symbol_language`; `_occurs` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1583-1667; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1668-1712 |
| The route leg: the distinct scopes, the pre-batch authoring transaction that classifies authored versus reused, the post-batch attachment transaction, each target's route outcome, and the two primitives whose idempotence the leg depends on. | `_author_routes`; `_author_route_rows`; `_attach_routes`; `_attached_outcome`; `_distinct_routes`; `author_route`; `set_governing_route` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1835-1863; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1877-1904; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1931-1956; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1976-2001; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1866-1874; mcp/src/agents_remember/memory/knowledge/routes.py:276-332; mcp/src/agents_remember/memory/knowledge/routes.py:436-520 |
| The write half of this module: one target plan's stored anchor and citation, the authored realization role, the entry assembly with its conditions, the single batch commit, and the per-entry rendering of a refused batch. | `_TargetPlan`; `_role_for`; `_curator_entry`; `_commit`; `_batch_refused` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:416-451; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2111-2119; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2034-2046; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2060-2071; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2074-2097 |
| The write module this ingest commits through: the citation and entry drafts it builds, the per-entry command list whose order is the batch's own contract, and the all-or-nothing batch commit. | `CuratorCitation`; `CuratorEntry`; `curator_entry_commands`; `commit_curator_entries` | mcp/src/agents_remember/application/knowledge_ingest.py:67-79; mcp/src/agents_remember/application/knowledge_ingest.py:82-101; mcp/src/agents_remember/application/knowledge_ingest.py:104-130; mcp/src/agents_remember/application/knowledge_ingest.py:164-175 |
| The model vocabulary the ingest constructs: the three locator kinds it resolves into, and the stored anchor draft it hands to both the rail and the write path. | `FileLocator`; `LineRangeLocator`; `SymbolLocator`; `SourceAnchorDraft` | mcp/src/agents_remember/models/knowledge/source.py:38-41; mcp/src/agents_remember/models/knowledge/source.py:44-58; mcp/src/agents_remember/models/knowledge/source.py:60-66; mcp/src/agents_remember/models/knowledge/source.py:82-97 |
| The cases that measure the behaviours a reader is most likely to doubt: the three outcomes in one run, the ruling that is never committed, a leaf citing a file its own line created, the measured blob identity refusing a working edit, and the route recorded once per scope and attached per anchor. | "test_one_run_reports_committed_skipped_and_each_refusal_reason"; "test_a_ruling_is_never_committed_as_an_obligation_with_no_realization"; "test_a_producer_citing_a_file_its_own_leaf_created_commits_and_reads_back"; "test_the_recorded_blob_identity_is_measured_and_a_working_edit_is_a_typed_refusal"; "test_the_governing_route_is_recorded_once_per_scope_and_attached_to_each_anchor" | mcp/tests/test_knowledge_curator_ingest_list.py:385-442; mcp/tests/test_knowledge_curator_ingest_list.py:443-489; mcp/tests/test_knowledge_curator_ingest_list.py:490-545; mcp/tests/test_knowledge_curator_ingest_list.py:826-896; mcp/tests/test_knowledge_curator_ingest_list.py:1197-1255 |
| The hand-off list contract this ingest reads: the nine producer-owned fields, the rule that every entry carries all thirteen keys with curator fields null, and the required locator that makes an omission a refusal rather than a whole-file citation. | "The nine the producer supplies are"; "Every entry carries all thirteen keys"; "a target that names a path and no construct" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:27-27; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:50-50; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:85-85 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The operation resolves every path inside the
one enclosure's two admitted roots, refuses a path under the coordination root as a third root it
cannot reach, and carries no identity beyond that enclosure; the hand-off list it reads is handed to it
as data, not fetched.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-19T17:08+02:00 — 260915-KS-L28 curator (uncommitted change set on `ar/260915-ks-l28`): created this one-to-one card for L25's curator ingest. It records the one entry point `ingest_curator_list` with its required `authorization_ref` and dry-run mode, the three never-conflated outcomes (committed, skipped ruling, refused) with the promise that nothing readable raises, the split between the leaf's own code line used for resolution and the recorded base commit the identities stay anchored to, the three-step path completion with the working-byte blob identity measured against the recorded tree, the symbol boundary that now resolves "defined" through the shipped tree-sitter extractor instead of a second regex implementation, the four unresolved-path reasons read from the recorded trees rather than the live filesystem, the route leg run as two transactions through `author_route`/`set_governing_route` because the closed command union carries no route-on-anchor command, the report and count shapes with the corrected written-row arithmetic, and the two declared-but-unreferenced constants `_RULING_SHAPE` and `_NO_REFUSAL`. Verification metadata is the code worktree revision `7e6936c0d3b87f2fa0f462c5c63d6d86441ef10b` that contains the source this card was read against.
- 2026-09-19T18:40+02:00 — 260915-KS-L28 repair (uncommitted change set on `ar/260915-ks-l28`): re-verified this card against the repaired source, which this leaf changed for findings M1-2, INC-2, INC-3, INC-4, INC-5, INC-8 and INC-9. The symbol rows and the two prose blocks above were rewritten: this module no longer implements definition detection at all (the regex tables, the blanking pass and `_defines`/`_declares`/`_code_only`/`_blank` were deleted and both this boundary and the knowledge read rail now call `memory_quality.style.citations.extents.bound_definitions`), a non-mapping target or locator is refused rather than raising `AttributeError`, the admission and destination refusals now attribute every planned entry instead of leaving it in no outcome list, the third-root classifier resolves a name the coordination root owns at its top level as the third root, `records_written` counts route rows the leg really wrote even when the batch then refused, a dry run's route states are `projected` rather than a false `authored`, and the dead `_ROUTE_ATTACHED` constant is gone. Still verified against code revision `7e6936c0d3b87f2fa0f462c5c63d6d86441ef10b` for everything that revision already contained; the changed rows describe the working tree and must be re-stamped when this leaf lands.
