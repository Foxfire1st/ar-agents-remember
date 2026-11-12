# mcp/src/agents_remember/application/review_comparison_generation.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Decode retained historical comparison JSON and preserve its exact source identities, artifact references and archival ownership. Normal reviews bind code/memory trees; no new canonical dataset generation is published here.

## Code Commentary

### Logic

The manifest validates recorded bindings, the seal and derived identity. `read_manifest` additionally checks agreement with its containing directory. Retained knowledge bindings remain historical metadata and authorize no canonical snapshot read. Discovery lists readable records without guessing damaged fields.

Layout helpers derive deletion-record locations from the supplied task root; reads distinguish a missing record from an unreadable one. Direct read_manifest(path) accepts its caller's path, not a separately enforced task-root sandbox. These archive operations preserve the historical generation identity, not the current availability of its former datasets.

### Invariants And Boundaries

No new dataset freeze/publication route is provided. Tampered source records are refused rather than retargeted. Current memory trees never replace historical unavailable knowledge halves. Source and artifact identities remain independently inspectable.

### Todos

None recorded.

### Logic

`ComparisonRecordBinding.assessment_channel` optionally retains the assessment owner's availability separately from collection counts. It now uses the retained-manifest-only `ComparisonAssessmentAvailability` from `models/lifecycles/comparison_records.py`, not the removed Reviewer record pane. The specialized model permits `assessments` only, distinguishes counted recorded/none_recorded states from unanswered states, and requires a next action for the latter. Its present count must equal the binding's declared assessment count; this parent agreement check already existed at BASE, not a new measurement. Missing availability is omitted from canonical serialization, preserving existing sealed manifest bytes; it means availability was not captured, never that no assessment existed. No assessment object or new semantic judgment is serialized into the manifest.

**The manifest validates itself against itself, in two independent statements of one identity.**
`ComparisonGenerationManifest._the_record_agrees_with_itself` requires exactly one
knowledge side per half, ties `generation_index == 1` to "records no predecessor", recomputes
`binding_digest` from the record's own fields and refuses a mismatch, and then **re-derives
`generation_identity(binding_digest)`** and refuses an id the seal does not produce. That second check
is the one that matters: sealing a record and then renaming it would otherwise describe a generation
nobody published. `read_manifest` adds the *second* statement of the same identity from
outside the file — the containing directory must be named for the id the record claims — because a
record resealed *around* edited fields would be internally consistent under the old address, and the
address a reader resolved would then describe a comparison nobody published.

**Every nested binding carries a validator that makes its own fields one fact.** These are the module's
load-bearing refusals, and each closes a way a record could lie about what it bound:

- `ComparisonKnowledgeBinding._retained_means_identity_and_bytes`: `retained` requires
  **both** the dataset identity and an artifact descriptor, and a non-retained side must carry
  neither and must state a reason. This validates the recorded shape, not the existence or content of
  the file the descriptor names; historical reopen treats these legacy knowledge halves as unavailable
  without reading a canonical dataset.
- `ComparisonSourceBinding._custody_and_the_pin_agree`: the retained-object descriptor is present **exactly when**
  declared custody is `retained`; it names deletion ownership and a cleanup scope, and its recorded
  tree/base fields must equal the two bound identities. This is structural agreement, not a fresh
  observation that a Git ref/object still exists (`retained.tree == candidate_code_tree_id` and
  `retained.base_commit == baseline_code_tree_id`).
- `ComparisonScopeBinding._the_selection_and_its_selectors_agree`: a scope is `subject`
  exactly when it names the selector it selected.
- `ComparisonPublicationLineage._a_predecessor_is_named_by_identity_and_digest`: the
  predecessor's generation id and that generation's manifest digest travel together or not at all.

**Reads answer with values, and a broken record is never a guess.** `read_manifest` raises
`KnowledgeStorageError` for every failure (absent, not canonical JSON, not a valid record, wrong
directory) and says why the last one matters. `read_history_deletion` returns `None` only
when no record is *there*: a record that exists but cannot be read is a storage error, because
answering "no deletion was recorded" for an unreadable record is exactly how a deliberate deletion comes
to be reported as an accidental loss. `write_history_deletion` writes canonical bytes, so
the same deletion always has the same file content and a repeated deletion converges instead of
accumulating records. `generation_directories` is the one list of published-looking
generation directories, hidden entries excluded; `read_generation_refs` **skips** a
directory whose manifest is absent or unreadable rather than inferring fields from a damaged record —
discovery exists to let a caller address an exact generation, and an explicit reopen still reports the
damaged directory as unreadable.

### Invariants And Boundaries

- **The record stores identities and references, never a description and never a judgment.** Its binding digest excludes `_UNSEALED_FIELDS`; its canonical manifest-byte digest is a separate value, not the binding digest.
- **The binding seal excludes `binding_digest`, derived `generation_id` and `recorded_at`.** Other
  recorded fields feed the canonical binding digest. The separate canonical manifest encoding includes
  those fields; equal binding identity is not a claim of equal manifest bytes at another record time.
- **The id is derived, not minted** — from the seal, under a literal namespace — so a different
  comparison can never be published under an id another comparison already holds.
- **The identity is stated twice**, by the seal and by the containing directory name, and
  `read_manifest` requires both.
- **A `retained` binding carries identity and artifact metadata**; a non-retained binding carries
  neither and states its reason. The model does not authenticate physical snapshot bytes.
- **`not-recorded` and `not-selected` are statements, not failures.** `TYPED_ABSENCE_STATES` is built
  from R05's own constant so the spelling this module accepts and the spelling the before-half owner
  records cannot drift.
- **An unreadable deletion record is a storage error, never "no deletion recorded".**
- **Layout is task-relative, not a caller-path sandbox.** Helpers derive task-report paths;
  `read_manifest(path)` reads the provided path and checks its generation-directory name. This module
  does not read code-repository objects, canonical knowledge stores or legacy snapshot bytes.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in this module's own docstring and functions, in the retained-history owners and in the stored regression assertions. No removed assembler,
snapshot_path helper or canonical snapshot publisher is treated as current here. Three details a reader should carry: the durable root is **asked of its owner**
(`durable_evidence.durable_reports_root`) rather than restated; the id is re-derived from the seal *and*
checked against the directory name; and `recorded_at` is outside the seal on purpose, so deterministic binding identity does not depend on the record clock; manifest-byte identity remains
a distinct value.

- The module's own statement of what it owns (the record, the layout, the deletion record) and of the separate responsibility next door. [1]

- The retained decoder exposes its current version, layout, model and archival read/discovery helpers; it exports no new-generation assembler. [2]

- The retained layout names generation, manifest and deletion locations and typed absence; former canonical snapshot-directory/name constants are removed. [3]

- **The fields the seal does not cover, and why each is excluded.** [4]

- A retained snapshot artifact is metadata: relative path, declared digest/length, deletion owner and scope; this model does not read or prove the file exists. [5]

- Knowledge binding validation requires identity plus artifact metadata for retained, neither for non-retained, and a reason for non-retained; physical bytes are a separate question. [6]


- The source binding checks that retained custody and pin presence agree. With a pin, it requires both deletion-owner fields and compares retained tree/base to the bound identities; without a pin it returns after the ownership-field condition. It does not cross-check candidate_capture base/tree against those identities. These are recorded structural constraints, not fresh Git-object availability evidence. [7]


- **The scope binding: the owner-produced inventory's state, digest and population, plus the selection that must name its selector.** [8]

- One cited owner-produced artifact as a task-relative, digest-bearing reference. [9]

- Legacy input collection counts/digest and optional assessment availability remain distinct declared facts. [10]

- Every policy version as a constant its owner declares, never a version derived here. [11]

- **The lineage: one predecessor named by id *and* manifest digest, plus the two optional owner digests.** [12]

- **The record itself, the seal it carries, and the four self-agreement checks including the re-derived generation id.** [13]

- **The unavailable-history record an explicit deletion writes, including the custody measured *before* a pin was released.** [14]

- Current historical layout helpers derive task-report generation, manifest and deletion paths; the snapshot_path helper is removed. [15]

- Generation identity is derived from the binding digest; the manifest exposes its own canonical encoding, not the removed assemble_manifest publisher. [16]

- **The two-statement read: the record's own validation plus the containing directory's agreement with the id it claims.** [17]

- **The deletion reads and the canonical-bytes write, with "present but unreadable is not absence" stated in the code.** [18]

- **Discovery: the one list of published-looking directories, and the pass that skips an unreadable record instead of guessing its fields.** [19]

- **The one durable-root owner this module asks instead of restating `<task_root>/notes/reports`.** [20]

- The R05 constant imported rather than re-spelled, so the accepted spelling and the recorded one cannot drift. [21]

- Referenced source/selection/inventory/identity owners remain inspectable; this decoder no longer assembles new generations from them. [22]

- Historical source is preserved without reading a canonical dataset; tampered source is refused rather than retargeted. [23]

The following declarations carry the changed boundary.

- The optional assessment availability uses its retained-manifest-only owner; absent availability is omitted from canonical serialization and a present count matches the declared assessment total. [24]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The historical layout is under the coordination
task root, outside both the code and memory repository, and the repository it *names* is a
path the source binding records rather than something this module resolves.

No meaningful cross-repo references found.
