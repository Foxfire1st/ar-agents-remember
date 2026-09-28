# mcp/src/agents_remember/application/curator_ingest_planes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/curator_ingest_planes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T07:54+02:00 |
| lastVerifiedCommitHash | `eda947325ccbe0791973953265278597e968a34a` |
| lastVerifiedCommitDate | 2026-09-28T18:11:05+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The curator's two awarded planes, read once, and the coverage one report carries for them
(ICR-R28@v2).** A curator run reads two things from the same hand-off list before it plans a single
entry: the **family plane** (the guarantees, memberships and deliberate no-family outcomes the list
authors) and the **external-source plane** (the sources the curator inspected, retained in a bounded
manifest whose digest every authored record's origin reference names). This module owns reading them
**together** and reporting what became of them, so
`knowledge_curator_ingest.py` stays the operation — resolve, verify, commit, report — and neither
plane's vocabulary is restated there.

**Three properties are load-bearing (`:10-21`):**

| Property | What it means |
| --- | --- |
| Reading is not writing | Identities are allocated in memory and the manifest is computed as bytes; the journal and the manifest file are written by the operation only **after** admission has produced the candidate they belong to |
| Each plane keeps its own state | `recorded` means the rows or the manifest exist and every count was read back from the candidate; `projected` means a planning run wrote nothing; `not-recorded` means nothing was written, with the sentence naming why. A plane that did not record reports **null counts, never zeroes that would read as measured** |
| Every entry is accounted for, once | A plane's refusal is reported through the entry's own refusal; the entries whose outcome the run could not establish are named as unresolved, and the committed entries the curator examined nothing for are named as unexamined |

## Code Commentary

### 260921-ICR-L32 The Family Read Learns The Fork Point

`read_curator_planes` gains a keyword-only `fork_point: Path | None`, and its docstring now states why the read is not simply "the candidate's own bytes yet": an **absent** candidate that selected a baseline does not start empty, because admission clones that baseline — so the family revisions the candidate holds on its first write are the baseline's. Reading only the candidate answered `None` ("there is no dataset here") for exactly that run, and a membership naming a revision the **baseline** stores was refused `family_revision_not_stored` while sitting one step away from a candidate that would hold it. The fallback sits here rather than after admission because the CLI's **planning run is the default** and asks the same question, so a fix covering only the committing run would leave the ordinary dry run refusing the same stored revision. `read_stored_family_facts` answering `None` for a candidate that does not exist yet is what keeps a first run's "records no family" distinguishable from "there is no dataset here".

### Logic

**The two planes travel as one value because the report needs them together.**
`CuratorPlanes` (`:94-141`) carries the list digest, the family read, the resolved declaration plan, the
stored facts, the source read and the manifest. `stored` is `None` when the candidate does not exist
yet, which the docstring states is a different fact from a candidate that records no family.

**`manifest_written` is a separate field on purpose** (`:111-115`). Its comment says exactly why: it is a
different fact from `manifest is not None`, which only says the *list* declared something — a run whose
batch refused still wrote the file it had already named, and a report that said otherwise would be false
about the store. The `refs` property (`:117-121`) is the one place the origin references every written
row carries are composed.

**`CuratorPlanes.refusal_of` answers one entry's question across both planes** (`:123-141`). The two
planes refuse different things — a family decision that cannot be resolved to exact revisions, and an
external source that cannot be found again — and both are facts about one entry, so they are reported
through the entry's own refusal rather than only in the plane's coverage. The order is fixed and stated:
the family read, then the declaration plan, then the source read.

**`read_curator_planes` reads and resolves everything before a single entry is planned** (`:144-178`):
the list digest, the family read, the stored facts, the declaration plan and the source read, in that
order. Nothing is written — the identities are allocated in memory and journalled only after admission
has produced their candidate. `retry_scope` is passed in rather than derived here, with the reason
stated: the operation owns that derivation and this module must not hold a second spelling of it.

**`PlaneCoverageInputs` carries the run's outcome as facts rather than as the operation's private
objects** (`:70-91`): the candidate path, the entry ids, the placed entries, the authoring map, the
planes, whether this was a dry run, and the post-batch read that exists only when the batch committed.
Its `unresolved` property (`:87-91`) is the one definition of "every entry this run carried whose
outcome the two planes did not establish" — every entry id that is not in `placed`.

**`plane_coverage` returns both planes' coverage, each with the state this run actually reached**
(`:181-227`). The states come from `_plane_states`, the entry sets come from the inputs, and the source
coverage's `path` is claimed **only** when the source state is `recorded` — a set of bytes no reader can
find is not reported as a recorded artifact.

**The source plane's state follows the write, not the commit** (`_source_state` `:230-254`), and the
docstring states the reason: the manifest is written *before* the batch it belongs to, because the
origin references that batch stamps name its digest — so "the manifest is not there" and "the batch
refused" are two different facts, and a run whose batch refused still has a written manifest to report.
Three sentences are possible and none is parameterised from another: nothing declared, the manifest
written, and the run stopping before the write.

**The family plane's state comes from the post-batch read.** `_plane_states` (`:257-285`) returns four
values — each plane's state and its own sentence — and the comment says why there are separate sentence
pairs rather than one sentence parameterised by a word: a sentence that claimed more than the run
established would be the defect this whole report exists to prevent. A dry run is `projected` for the
family plane and `not-recorded` for the source plane; otherwise the family state is `recorded` when
`after` is present (the committed candidate holds these rows and every count was read back from it) and
`not-recorded` with `"the batch did not commit, so no family row was written here"` when it is absent.
The two pairs are bound to typed locals and returned as an explicit 4-tuple, so each plane's answer
keeps its own type.

### Conventions

This module composes owners rather than re-implementing them: the family read, the declaration plan,
the stored-facts read and the source plane all come from the two modules that own them, and the two
coverage assemblers are called rather than copied. It holds the **state-and-sentence** vocabulary for
both planes so a report cannot grow a second spelling of "was it recorded?".

### Invariants And Boundaries

- Reading allocates in memory and computes bytes; nothing is written before admission.
- `manifest_written` tracks the write; the batch's own commit is a separate fact reported separately.
- A plane that did not record reports null counts and claims no path and no digest.
- A dry run projects the family plane and records nothing for the source plane.
- Every entry the run carried appears in exactly one of `placed` / `unresolved`.
- `retry_scope` is passed in; this module derives no second spelling of the enclosure's scope.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this is the composition of the repository's own
curator-run planes.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for reading the two planes together. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the three load-bearing properties, including that a plane which did not record reports null counts rather than zeroes.** | "Three properties are load-bearing"; "plane that did not record reports null counts, never zeroes that would read as measured" | mcp/src/agents_remember/application/curator_ingest_planes.py:1-22 |
| The published surface: the two values, the reader and the coverage assembler. | `__all__` | mcp/src/agents_remember/application/curator_ingest_planes.py:62-67 |
| **One run's outcome as facts rather than as the operation's private objects, with the one definition of `unresolved`.** | `PlaneCoverageInputs`; "return tuple(one for one in self.entry_ids if one not in set(self.placed))" | mcp/src/agents_remember/application/curator_ingest_planes.py:70-91 |
| **The two planes in one value, because the report needs the family declarations and the source manifest's digest together.** | `CuratorPlanes` | mcp/src/agents_remember/application/curator_ingest_planes.py:94-110 |
| **`manifest_written` as a fact separate from "the list declared something", because a refused batch still wrote the file it named.** | "manifest_written"; "a report that said otherwise would be" | mcp/src/agents_remember/application/curator_ingest_planes.py:111-115 |
| The one place the origin references every written row carries are composed. | `refs`; `origin_refs` | mcp/src/agents_remember/application/curator_ingest_planes.py:117-121 |
| **One entry's refusal answered across both planes, in a fixed order, because both are facts about that one entry.** | `refusal_of` | mcp/src/agents_remember/application/curator_ingest_planes.py:123-141 |
| **The read-before-you-plan entry point: everything resolved against the destination this run will write into, and nothing written.** | `read_curator_planes`; "Everything here is read and resolved against the destination this run will write into, and nothing is written" | mcp/src/agents_remember/application/curator_ingest_planes.py:144-178 |
| **Both planes' coverage for one report, with the source path claimed only when its state is recorded.** | `plane_coverage`; "SOURCE_MANIFEST_NAME if source_state ==" | mcp/src/agents_remember/application/curator_ingest_planes.py:200-246 |
| **The source plane's state follows the write rather than the commit, because the manifest precedes the batch that names its digest.** | `_source_state`; "manifest is written *before* the batch it belongs to" | mcp/src/agents_remember/application/curator_ingest_planes.py:230-254 |
| **Each plane's state and its own sentence, as separate pairs rather than one sentence parameterised by a word, with the family state read from the post-batch read.** | `_plane_states`; "the batch did not commit, so no family row was written here" | mcp/src/agents_remember/application/curator_ingest_planes.py:276-304 |
| The owners this module composes rather than restates: the family read, the declaration plan, the stored facts and the source plane. | `read_family_plane`; `plan_declarations`; `read_stored_family_facts`; `read_family_allocations`; `read_source_plane` | mcp/src/agents_remember/application/curator_family_authoring.py:174-205; mcp/src/agents_remember/application/curator_family_planning.py:341-373; mcp/src/agents_remember/application/curator_family_planning.py:252-299; mcp/src/agents_remember/application/curator_family_planning.py:138-158; mcp/src/agents_remember/application/curator_source_manifest.py:160-175 |
| The two coverage assemblers this module calls rather than copies. | `family_coverage`; `source_coverage` | mcp/src/agents_remember/application/curator_family_coverage.py:116-156; mcp/src/agents_remember/application/curator_source_manifest.py:410-443 |
| The digest of the list itself, which the origin references name. | `sha256_digest` | mcp/src/agents_remember/kernel/canonical_json.py:34-37 |
| The candidate path the stored facts and the manifest are read and named under. | `candidate_database_path`; `SOURCE_MANIFEST_NAME` | mcp/src/agents_remember/models/knowledge/snapshot.py:58-61; mcp/src/agents_remember/application/curator_source_manifest.py:70-73 |
| The ingest operation owns the batch decision and records the exact planned writes before committing. | `ingest_curator_list`; `_record_what_the_batch_will_write` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1116-1243; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1331-1367 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Both planes are properties of one hand-off
list and one candidate dataset under one coordination root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/src/agents_remember/application/knowledge_curator_ingest.py`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-26T21:37:21Z — Reconciled the reference with the current source owner while retaining its scope and history.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `plane_coverage`; "SOURCE_MANIFEST_NAME if source_state ==" repointed to mcp/src/agents_remember/application/curator_ingest_planes.py:200-246; mcp/src/agents_remember/application/curator_ingest_planes.py:242-242. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_plane_states`; "the batch did not commit, so no family row was written here" repointed to mcp/src/agents_remember/application/curator_ingest_planes.py:276-304; mcp/src/agents_remember/application/curator_ingest_planes.py:295-295. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **body update — the D57 fork-point read.** A new subsection records the keyword-only `fork_point`, why an absent baseline-forked candidate must be read through it, why the fallback belongs before admission (the planning run is the default and asks the same question), and the two distinct answers `read_stored_family_facts` keeps apart. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.

- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base
  `63b476297708f779de8ed5c0bf3555b9d1de70c2`): created this one-to-one card for the module
  `ICR-R28@v2` introduced as **the seam that reads the curator's two planes together**. The stamp basis
  is the leaf's base commit, because the module is untracked there. Two facts a reader must carry: the
  family plane's state is read from the **post-batch read** (`after`), so a run whose batch did not
  commit says `not-recorded` with its reason instead of reporting rows it never wrote; and the source
  plane's state follows the **write**, not the commit, because the manifest is written before the batch
  whose origin references name its digest — which is why `manifest_written` is a field separate from
  "the list declared something". A plane that did not record reports null counts, never zeroes. No
  verification stamp beyond the leaf's base is advanced: the candidate is uncommitted and the governed
  closeout owns the real commit.
