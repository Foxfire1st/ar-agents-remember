# mcp/src/agents_remember/application/review_comparison_generation.py

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

`ComparisonRecordBinding.assessment_channel` optionally retains the assessment owner's availability separately from collection counts. Its kind and any measured count must agree with the assessment collection. Missing availability is omitted from canonical serialization, preserving existing sealed manifest bytes; it means availability was not captured, never that no assessment existed. No assessment object or new semantic judgment is serialized into the manifest.

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in this module's own docstring and functions, in the four sibling
modules that produce, retain, reclaim and resolve a generation, and in the cases that measure the whole
journey. Three details a reader should carry: the durable root is **asked of its owner**
(`durable_evidence.durable_reports_root`) rather than restated; the id is re-derived from the seal *and*
checked against the directory name; and `recorded_at` is outside the seal on purpose, which is what
makes an exact retry converge.

- The module's own statement of what it owns (the record, the layout, the deletion record) and of the separate responsibility next door. [1]
- The published surface: version, layout literals, the eleven models, the path helpers, the reads and the discovery functions. [2]
- **The layout, named once**, and the two typed-absence spellings with their reason for being distinct from a failure. [3]
- **The fields the seal does not cover, and why each is excluded.** [4]
- **One retained snapshot: a generation-relative path, the digest of the bytes written, and the deletion owner plus bounded scope that may delete it.** [5]
- **The validator that makes the packet's non-conforming example unconstructible: identity and bytes travel together, and a non-retained side states its reason.** [6]
- **The source binding: the capture owner's own identity carried verbatim, the custody measurement, the names it was measured against, and the pin's agreement with the custody.** [7]
- **The scope binding: the owner-produced inventory's state, digest and population, plus the selection that must name its selector.** [8]
- One cited owner-produced artifact as a task-relative, digest-bearing reference. [9]
- **The records binding, which asserts what the composition supplied and deliberately not whether an owner published none or could not be read (R14's fact).** [10]
- Every policy version as a constant its owner declares, never a version derived here. [11]
- **The lineage: one predecessor named by id *and* manifest digest, plus the two optional owner digests.** [12]
- **The record itself, the seal it carries, and the four self-agreement checks including the re-derived generation id.** [13]
- **The unavailable-history record an explicit deletion writes, including the custody measured *before* a pin was released.** [14]
- **The whole layout, derived from the one durable root owner.** [15]
- **The derived generation id, and the one function that seals and validates a field set together.** [16]
- **The two-statement read: the record's own validation plus the containing directory's agreement with the id it claims.** [17]
- **The deletion reads and the canonical-bytes write, with "present but unreadable is not absence" stated in the code.** [18]
- **Discovery: the one list of published-looking directories, and the pass that skips an unreadable record instead of guessing its fields.** [19]
- **The one durable-root owner this module asks instead of restating `<task_root>/notes/reports`.** [20]
- The R05 constant imported rather than re-spelled, so the accepted spelling and the recorded one cannot drift. [21]
- The owners whose values the manifest carries rather than re-derives: the capture identity, the resolved pair, the inventory and the comparison identity. [22]
- **The four cases that measure this record's own contract: what it binds, what it refuses to read, what converges, and what a damaged record is reported as.** [23]

The following declarations carry the changed boundary.

- Counts and optional assessment availability remain separate recorded facts. [24]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The record is published under the coordination
task root, which is outside both the code and the memory repository, and the repository it *names* is a
path the source binding records rather than something this module resolves.

No meaningful cross-repo references found.
