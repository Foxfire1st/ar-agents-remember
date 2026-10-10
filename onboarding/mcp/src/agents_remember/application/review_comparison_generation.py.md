# mcp/src/agents_remember/application/review_comparison_generation.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Decode retained historical comparison JSON and preserve its exact source identities, artifact references and archival ownership. Normal reviews bind code/memory trees; no new canonical dataset generation is published here.

## Code Commentary

### Logic

The manifest validates recorded bindings, the seal and derived identity. `read_manifest` additionally checks agreement with its containing directory. Retained knowledge bindings remain historical metadata and authorize no canonical snapshot read. Discovery lists readable records without guessing damaged fields.

Deletion-record reads/writes stay bounded to the task root and distinguish a missing record from an unreadable one. These archive operations preserve the historical generation identity, not the current availability of its former datasets.

### Invariants And Boundaries

No new dataset freeze/publication route is provided. Tampered source records are refused rather than retargeted. Current memory trees never replace historical unavailable knowledge halves. Source and artifact identities remain independently inspectable.

### Todos

None recorded.

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
- **It reads and writes only under the task root.** No code repository, no knowledge store, no ref, no
  snapshot byte is touched here.

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

- Historical source is preserved without reading a canonical dataset; tampered source is refused rather than retargeted. [23]


The following declarations carry the changed boundary.

- Counts and optional assessment availability remain separate recorded facts. [24]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The record is published under the coordination
task root, which is outside both the code and the memory repository, and the repository it *names* is a
path the source binding records rather than something this module resolves.

No meaningful cross-repo references found.
