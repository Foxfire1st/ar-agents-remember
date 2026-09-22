# mcp/src/agents_remember/application/review_comparison_generation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_comparison_generation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T22:40:00+02:00 |
| lastVerifiedCommitHash | `2edad477bcd9127a90e4618d345ce34ef7e6a6d9` |
| lastVerifiedCommitDate | 2026-09-23T00:33:19+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

The **durable record of one comparison generation** — what a comparison bound, where that record lives,
and how it is read back — and nothing else. It exists because everything a comparison actually read is
disposable: both datasets live in a leaf's disposable knowledge root, the bound candidate is a tree that
exists in **no commit**, and the worktree holding both is removed by cleanup. Once that has happened, a
reader holding only "a comparison was made" can re-read nothing.

Three responsibilities, and the whole module is those three:

1. **The manifest.** `ComparisonGenerationManifest` is one immutable, canonical-JSON record binding both
   code objects, both knowledge sides (or the typed state saying why a side legitimately has none), the
   selected scope with the exact inventory measured over it, the record collections the composition
   supplied, the cited evidence, every owner-declared policy version in play, and the generation's own
   lineage. It stores **references to owner-produced content and no semantic judgment**: the one digest
   it computes for itself is a *seal* over its own fields.
2. **The layout.** One directory per generation under the durable task-artifact root that
   `memory/knowledge/durable_evidence.durable_reports_root` already fixes — so this module does not
   restate `<task_root>/notes/reports`, it *asks* the one owner that decides it.
3. **The deletion record.** `ComparisonHistoryDeletion` is the unavailable-history record an explicit
   release or discard writes *before* it deletes, which is the only thing that lets a later reader tell
   a deliberate deletion from an accidental loss.

**What this module deliberately is not.** It never touches the code repository, never copies a dataset,
never writes a manifest, and never resolves what the record points at. Producing a generation is
`review_comparison_freeze` (with `review_comparison_retention`), deleting one's content is
`review_comparison_reclamation`, and *resolving* a published record against the world it names is
`review_comparison_reopen` — the separate responsibility next door, "because reading a record and
resolving what it points at are different acts".

**Three states that must never collapse into one** (the distinction the module's docstring states and
the tests measure): `not-recorded` is R05's typed historical absence — a fact about the repository's
history imported as `knowledge_before_half.NOT_RECORDED` rather than re-spelled here; `not-selected` is
*this comparison's* own statement that it selected no knowledge operand at all; and `missing`, `corrupt`
and `unavailable-history` are the three ways an expected input fails to resolve, each measured on the
channel that reports it.

## Code Commentary

### Logic

**The manifest validates itself against itself, in two independent statements of one identity.**
`ComparisonGenerationManifest._the_record_agrees_with_itself` (`:410-438`) requires exactly one
knowledge side per half, ties `generation_index == 1` to "records no predecessor", recomputes
`binding_digest` from the record's own fields and refuses a mismatch, and then **re-derives
`generation_identity(binding_digest)`** and refuses an id the seal does not produce. That second check
is the one that matters: sealing a record and then renaming it would otherwise describe a generation
nobody published. `read_manifest` (`:586-620`) adds the *second* statement of the same identity from
outside the file — the containing directory must be named for the id the record claims — because a
record resealed *around* edited fields would be internally consistent under the old address, and the
address a reader resolved would then describe a comparison nobody published.

**The seal is computed once, in one function, over the stored encoding.** `assemble_manifest`
(`:557-580`) takes an already-JSON-ready payload (every nested value is the `model_dump(mode="json")`
of its owner's model), stamps `recorded_at`, digests everything except `_UNSEALED_FIELDS`
(`("binding_digest", "generation_id", "recorded_at")`, `:155`), and derives the id from that digest.
`recorded_at` is excluded so an exact retry of one freeze — same comparison, same bytes, a later clock —
converges on the same digest, the same id and the same published record instead of refusing against
itself; `generation_id` is excluded because it *is* the digest's derived value. `generation_identity`
(`:546-554`) is `uuid5` under a module literal namespace, so an id is a function of the bindings rather
than of a clock or a counter.

**Every nested binding carries a validator that makes its own fields one fact.** These are the module's
load-bearing refusals, and each closes a way a record could lie about what it bound:

- `ComparisonKnowledgeBinding._retained_means_identity_and_bytes` (`:190-209`): `retained` requires
  **both** the dataset identity and the retained copy of its bytes, and a non-retained side must carry
  neither plus a stated reason. This is the packet's non-conforming example made structurally
  impossible — "a manifest that stores only a digest of already-deleted SQLite bytes".
- `ComparisonSourceBinding._custody_and_the_pin_agree` (`:240-264`): the pin exists **exactly when**
  custody is `retained`; a pin names its deletion owner and a bounded cleanup scope; and the pin must
  keep exactly the two bound objects (`retained.tree == candidate_code_tree_id` and
  `retained.base_commit == baseline_code_tree_id`).
- `ComparisonScopeBinding._the_selection_and_its_selectors_agree` (`:286-295`): a scope is `subject`
  exactly when it names the selector it selected.
- `ComparisonPublicationLineage._a_predecessor_is_named_by_identity_and_digest` (`:366-373`): the
  predecessor's generation id and that generation's manifest digest travel together or not at all.

**The layout is named once and derived from the task root.** `COMPARISON_GENERATIONS_DIRECTORY`
(`comparison-generations`), `COMPARISON_MANIFEST_NAME` (`manifest.json`),
`COMPARISON_KNOWLEDGE_DIRECTORY` (`knowledge`), `COMPARISON_SNAPSHOT_NAME` (`snapshot.sqlite`) and
`COMPARISON_DELETIONS_DIRECTORY` (`deletions`) are literals at `:125-129`; everything below derives its
path from those plus the task root (`:495-532`), so the freeze and the reopen cannot come to disagree
about where a generation lives. `task_root_for_review` (`:535-543`) derives the task root from the
coordination root exactly as the review's own resolution does. One generation is therefore
`<task_root>/notes/reports/comparison-generations/<leaf-slug>/<generation-id>/` holding `manifest.json`,
`knowledge/{before,after}/snapshot.sqlite` and `deletions/<target>.json`.

**Reads answer with values, and a broken record is never a guess.** `read_manifest` raises
`KnowledgeStorageError` for every failure (absent, not canonical JSON, not a valid record, wrong
directory) and says why the last one matters. `read_history_deletion` (`:623-647`) returns `None` only
when no record is *there*: a record that exists but cannot be read is a storage error, because
answering "no deletion was recorded" for an unreadable record is exactly how a deliberate deletion comes
to be reported as an accidental loss. `write_history_deletion` (`:650-665`) writes canonical bytes, so
the same deletion always has the same file content and a repeated deletion converges instead of
accumulating records. `generation_directories` (`:668-682`) is the one list of published-looking
generation directories, hidden entries excluded; `read_generation_refs` (`:696-724`) **skips** a
directory whose manifest is absent or unreadable rather than inferring fields from a damaged record —
discovery exists to let a caller address an exact generation, and an explicit reopen still reports the
damaged directory as unreadable.

**The record's own boundaries on failure and history.** A generation's directory is published by one
rename (`atomic_replace`, in the freeze), so it exists or it does not; `retained.relative_path` is
relative to the generation directory and never absolute, and `ComparisonArtifactReference.relative_path`
is relative to the task root and confined there, so a generation stays addressable after the
coordination root is mounted elsewhere. `ComparisonRecordBinding` (`:313-335`) is deliberately a binding
of **inputs**: `supplied`/`not-supplied` says what the composition handed over, and the docstring records
that telling "the authority published no records" from "the loader could not read the authority" is
R14's obligation and is not asserted here.

### Conventions

`__all__` publishes thirty-four names: the version and layout literals, the two typed-absence
spellings and their frozenset, the eleven models, the path helpers, the three reads/writes and the two
discovery functions. All models are `KnowledgeModel` (pydantic), because every one of them is a wire shape that is
stored and validated on read; `ComparisonGenerationRef` (`:685-693`) is a **frozen dataclass** instead,
because it is a reader's address rather than a stored record. `KnowledgeSide` is
`Literal["before", "after"]` and `KnowledgeSideState` is
`Literal["retained", "not-recorded", "not-selected"]` — the closed vocabularies a reader branches on.
There is no state and no I/O beyond `read_manifest`/`read_history_deletion`/`write_history_deletion`: the
layout helpers are pure path arithmetic.

### Invariants And Boundaries

- **The record stores identities and references, never a description and never a judgment.** The only
  digest it computes for itself is the seal over its own fields.
- **The seal covers everything but itself and the record time**, so an edited-in-place manifest fails
  its own validation and an exact retry still converges.
- **The id is derived, not minted** — from the seal, under a literal namespace — so a different
  comparison can never be published under an id another comparison already holds.
- **The identity is stated twice**, by the seal and by the containing directory name, and
  `read_manifest` requires both.
- **A `retained` side carries identity *and* bytes**; a non-retained side carries neither and states its
  reason. There is no third shape.
- **`not-recorded` and `not-selected` are statements, not failures.** `TYPED_ABSENCE_STATES` is built
  from R05's own constant so the spelling this module accepts and the spelling the before-half owner
  records cannot drift.
- **An unreadable deletion record is a storage error, never "no deletion recorded".**
- **Hidden directories are never generations.** A freeze stages under a hidden sibling, so a crash
  between writing the record and renaming the stage cannot leave a complete-looking generation that no
  publication made.
- **It reads and writes only under the task root.** No code repository, no knowledge store, no ref, no
  snapshot byte is touched here.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in this module's own docstring and functions, in the four sibling
modules that produce, retain, reclaim and resolve a generation, and in the cases that measure the whole
journey. Three details a reader should carry: the durable root is **asked of its owner**
(`durable_evidence.durable_reports_root`) rather than restated; the id is re-derived from the seal *and*
checked against the directory name; and `recorded_at` is outside the seal on purpose, which is what
makes an exact retry converge.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what it owns (the record, the layout, the deletion record) and of the separate responsibility next door. | `ComparisonGenerationManifest`; `ComparisonHistoryDeletion` | mcp/src/agents_remember/application/review_comparison_generation.py:1-42 |
| The published surface: version, layout literals, the eleven models, the path helpers, the reads and the discovery functions. | `__all__`; `COMPARISON_GENERATION_VERSION` | mcp/src/agents_remember/application/review_comparison_generation.py:79-121 |
| **The layout, named once**, and the two typed-absence spellings with their reason for being distinct from a failure. | `COMPARISON_GENERATIONS_DIRECTORY`; `COMPARISON_MANIFEST_NAME`; `COMPARISON_KNOWLEDGE_DIRECTORY`; `COMPARISON_SNAPSHOT_NAME`; `COMPARISON_DELETIONS_DIRECTORY`; `KNOWLEDGE_NOT_SELECTED`; `TYPED_ABSENCE_STATES` | mcp/src/agents_remember/application/review_comparison_generation.py:125-144 |
| **The fields the seal does not cover, and why each is excluded.** | `_UNSEALED_FIELDS`; `_GENERATION_NAMESPACE` | mcp/src/agents_remember/application/review_comparison_generation.py:146-155 |
| **One retained snapshot: a generation-relative path, the digest of the bytes written, and the deletion owner plus bounded scope that may delete it.** | `ComparisonSnapshotArtifact` | mcp/src/agents_remember/application/review_comparison_generation.py:158-172 |
| **The validator that makes the packet's non-conforming example unconstructible: identity and bytes travel together, and a non-retained side states its reason.** | `ComparisonKnowledgeBinding`; `_retained_means_identity_and_bytes` | mcp/src/agents_remember/application/review_comparison_generation.py:175-209 |
| **The source binding: the capture owner's own identity carried verbatim, the custody measurement, the names it was measured against, and the pin's agreement with the custody.** | `ComparisonSourceBinding`; `_custody_and_the_pin_agree` | mcp/src/agents_remember/application/review_comparison_generation.py:212-264 |
| **The scope binding: the owner-produced inventory's state, digest and population, plus the selection that must name its selector.** | `ComparisonScopeBinding`; `_the_selection_and_its_selectors_agree` | mcp/src/agents_remember/application/review_comparison_generation.py:267-295 |
| One cited owner-produced artifact as a task-relative, digest-bearing reference. | `ComparisonArtifactReference` | mcp/src/agents_remember/application/review_comparison_generation.py:298-310 |
| **The records binding, which asserts what the composition supplied and deliberately not whether an owner published none or could not be read (R14's fact).** | `ComparisonRecordBinding`; `record_total` | mcp/src/agents_remember/application/review_comparison_generation.py:313-335 |
| Every policy version as a constant its owner declares, never a version derived here. | `ComparisonPolicyStamp` | mcp/src/agents_remember/application/review_comparison_generation.py:338-348 |
| **The lineage: one predecessor named by id *and* manifest digest, plus the two optional owner digests.** | `ComparisonPublicationLineage`; `_a_predecessor_is_named_by_identity_and_digest` | mcp/src/agents_remember/application/review_comparison_generation.py:351-373 |
| **The record itself, the seal it carries, and the four self-agreement checks including the re-derived generation id.** | `ComparisonGenerationManifest`; `_the_record_agrees_with_itself`; `binding_payload`; `compute_binding_digest`; `manifest_digest`; `knowledge_side` | mcp/src/agents_remember/application/review_comparison_generation.py:376-469 |
| **The unavailable-history record an explicit deletion writes, including the custody measured *before* a pin was released.** | `ComparisonHistoryDeletion` | mcp/src/agents_remember/application/review_comparison_generation.py:472-489 |
| **The whole layout, derived from the one durable root owner.** | `comparison_generations_root`; `leaf_generation_root`; `generation_directory`; `manifest_path`; `snapshot_path`; `deletion_record_path`; `task_root_for_review` | mcp/src/agents_remember/application/review_comparison_generation.py:495-543 |
| **The derived generation id, and the one function that seals and validates a field set together.** | `generation_identity`; `assemble_manifest` | mcp/src/agents_remember/application/review_comparison_generation.py:546-580 |
| **The two-statement read: the record's own validation plus the containing directory's agreement with the id it claims.** | `read_manifest` | mcp/src/agents_remember/application/review_comparison_generation.py:586-620 |
| **The deletion reads and the canonical-bytes write, with "present but unreadable is not absence" stated in the code.** | `read_history_deletion`; `write_history_deletion` | mcp/src/agents_remember/application/review_comparison_generation.py:623-665 |
| **Discovery: the one list of published-looking directories, and the pass that skips an unreadable record instead of guessing its fields.** | `generation_directories`; `ComparisonGenerationRef`; `read_generation_refs` | mcp/src/agents_remember/application/review_comparison_generation.py:668-724 |
| **The one durable-root owner this module asks instead of restating `<task_root>/notes/reports`.** | `durable_reports_root` | mcp/src/agents_remember/memory/knowledge/durable_evidence.py:58-68 |
| The R05 constant imported rather than re-spelled, so the accepted spelling and the recorded one cannot drift. | `NOT_RECORDED` | mcp/src/agents_remember/application/knowledge_before_half.py:84-84 |
| The owners whose values the manifest carries rather than re-derives: the capture identity, the resolved pair, the inventory and the comparison identity. | `FutureCodeCandidateIdentity`; `ReviewCandidateResolution`; `ReviewSourceInventory`; `ComparisonIdentity` | mcp/src/agents_remember/worktrees/modules/future_code_candidate.py:15-22; mcp/src/agents_remember/application/review_candidate_resolution.py:106-135; mcp/src/agents_remember/models/knowledge/review.py:94-94; mcp/src/agents_remember/models/knowledge/review.py:63-63 |
| **The four cases that measure this record's own contract: what it binds, what it refuses to read, what converges, and what a damaged record is reported as.** | `test_the_manifest_binds_the_owners_identities_versions_and_its_own_fields`; `test_a_record_that_cannot_be_read_is_not_a_readable_generation`; `test_an_exact_retry_converges_and_a_superseding_generation_names_its_predecessor`; `test_a_half_with_no_recorded_generation_freezes_as_typed_absence_never_as_inference` | mcp/tests/test_knowledge_review_comparison_generation.py:393-477; mcp/tests/test_knowledge_review_comparison_generation.py:601-669; mcp/tests/test_knowledge_review_comparison_generation.py:711-762; mcp/tests/test_knowledge_review_comparison_generation.py:768-836 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The record is published under the coordination
task root, which is outside both the code and the memory repository, and the repository it *names* is a
path the source binding records rather than something this module resolves.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **one inherited citation defect repaired — it is not this leaf's own.** The row carrying the module's own statement of what it owns cited `review_comparison_generation.py:1-42` with an Anchor cell reading `*(module docstring)*`, which is italic prose rather than an anchor: nothing in the row said what those lines were supposed to contain, so the range could not be checked at all. The defect predates this leaf (the row was written by 260921-ICR-L11) and is repaired here only because this leaf's curation pass owns the gate finding. The Anchor cell now names two real identifiers that occur **literally inside the cited range** — `ComparisonGenerationManifest` at line 11 and `ComparisonHistoryDeletion` at line 22, the record and the deletion record the docstring says this module owns — which is what makes the claim checkable. The Finding wording, the cited range and every other row are unchanged; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are deliberately **not** advanced, because nothing in this leaf is committed and the governed closeout owns the real stamp.
- 2026-09-21T19:26:00+02:00 — 260921-ICR-L11 curator (uncommitted change set on `ar/260921-icr-l11`, base `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`): created this one-to-one card for the module this leaf introduced as the **keystone of ICR-R11@v1** — the durable record a comparison survives cleanup and restart *as*. It records what the record is rather than only where the code lives: the manifest binds owner-produced identities and **stores no semantic judgment of its own** (its one self-computed digest is a seal over its own fields); a `retained` knowledge side must carry identity **and** bytes by construction, which makes the packet's non-conforming example — a manifest holding only a digest of already-deleted SQLite bytes — unconstructible rather than merely discouraged; the generation id is **re-derived from the seal** and then checked a second time against the directory the record was found in, so a record resealed around edited fields is refused instead of being read as the generation a caller resolved; and `recorded_at` is outside the seal on purpose so an exact retry converges on the same record instead of refusing against itself. It also records the boundaries: the durable root is asked of `durable_evidence.durable_reports_root` rather than restated, `not-recorded` / `not-selected` are R05's typed absences and not failures, an unreadable deletion record is a storage error rather than "no deletion recorded", and hidden stage directories are never generations. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the **production line this reading was against** — `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`, this leaf's recorded base — because every construct cited here exists only in this leaf's uncommitted candidate and no real commit contains the content a stamp would otherwise claim to have verified. The recorded working candidate states what was actually read, and closeout owns the real stamp once the code commit exists.
