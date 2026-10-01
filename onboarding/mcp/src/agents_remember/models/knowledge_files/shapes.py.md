# mcp/src/agents_remember/models/knowledge_files/shapes.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The building blocks every knowledge record and sidecar is written in (MIK-R21 rules 3, 4, 6, 7):**
the `FileModel` base, anchors and their three locators, requirement references and external
documents, numbered references with typed targets, links with their relation vocabulary, and the
admission and origin blocks. They check shape only — presence, closed vocabularies, spellings.

## Code Commentary

### Logic

- **`FileModel`** is frozen, `extra="forbid"`, validates by name or alias, serializes by alias, and
  refuses an explicit `null` in a `mode="before"` validator. `to_document()` dumps JSON-mode by alias
  with absent fields omitted — the exact inverse of parsing, which is what lets the canonical
  formatter round-trip every file byte for byte.
- `Text` (non-blank prose), `Label` (non-blank, no surrounding whitespace) and `RepositoryPath` (plain
  repository-relative POSIX path, no `.`/`..`/empty segments, no drive letter, then the shipped
  `require_plain_git_path`) refuse rather than clean.
- **Anchor** `{path?, locator, blob, content}`: locator is a discriminated union of
  `SymbolLocator{name}`, `LineRangeLocator{start,end}` (end ≥ start) and `WholeFileLocator`; `blob` is a
  Git object id; `content` is `sha256:<64 hex>` of the resolved range. Whether `path` must be present
  is decided by the owning model (sidecar entries omit it; route sidecars and link targets need it).
- **References**: `Reference{targets[≥1], note?}` keyed by `^[1-9][0-9]*$`. Targets are a union on
  `kind`: `code`/`test` (anchor), `invariant`/`family`/`decision`/`incident`/`record` (ID; the four
  named kinds require their own prefix), `requirement` (`RequirementReference{task{repository,path},
  packet, id, version}`), `external` (`DocumentIdentity{document, version?}`) and `unresolved` (legacy
  citation text, written only by the conversion). `anchors_of` lists every anchor of a table.
- **Link** `{target, relation, alternative?}`: target is a record ID, `route:<path>`, an anchor that
  names its path, or a requirement reference; `alternative` is required for `reconsider_on` and
  refused for every other relation. Which relations a kind may use is `records.RELATIONS_BY_KIND`.
- **Admission** per kind (`InvariantAdmission`, `FamilyAdmission`, `DecisionAdmission`) is
  `{criteria[≥1, unique], justification}`; `LEGACY_UNASSESSED` is the alternative string.
  **Origin** `{task, leaf? | wave?, handoff?, handoffEntry?, legacyId?}` refuses leaf and wave
  together; `HandoffOrigin` needs a list path, evidence text, or both. `EntryOrigin{leaf,
  handoffEntry?}` is the per-entry form.
- **The criteria's meanings are in the admission docstrings** (since MIK-R27, leaf 260928-MIK-L27;
  a docstring-only change, no model change). Invariant: `spans_locations`, realized in more than one
  file; `guarded_by_test`, at least one proof entry; `family_guarantee`, needed to state a family's
  guarantee; `prevents_costly_mistake`, guards a plausible, costly error the justification names.
  Family: `joint_guarantee`, the members together promise something none promises alone. Decision:
  `real_alternatives`, at least one alternative was seriously considered, and
  `constrains_future_work`. The `InvariantAdmission` docstring says the validator checks the first
  two for a new record (`memory_quality/knowledge_validator/rules_admission.py`) and the reviewer
  judges the rest.

### Conventions

- JSON keys follow the packet: `snake_case` for content, camelCase `handoffEntry` and `legacyId` in
  origin; Python names that differ carry an alias.
- Reuses the shipped `models/knowledge/base.py` limits and `GIT_OBJECT_PATTERN`, and the requirement
  packet version pattern, rather than the shipped knowledge models themselves (those are UUID- and
  digest-shaped).

### Invariants And Boundaries

- **Absent is absent; nothing is stripped.** One spelling per value is what makes the canonical
  formatter a pure formatting step.
- Resolution (does the symbol exist, does the ID resolve, is the criterion justified) is MIK-R22's
  and MIK-R13/MIK-R27's, never this module's.
- `TaskIdentity.path` is relative to `tasks/<repository>/` under the coordination root, the
  `TaskDocumentRef` convention, so the reference survives a relocated coordination tree.

### Todos

The template role `incidental` has no spelling in the format (review R1 finding 6); MIK-R12 owns the mapping.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The base, the three locators and the relation vocabulary are what `records.py` and `sidecars.py` compose.

- The base: frozen, extra-forbidden, alias-serialized, explicit null refused. [1]
- Repository paths are refused, never cleaned. [2]
- The anchor shape. [3]
- The task identity's resolution base. [4]
- ID targets must carry their own kind's prefix. [5]
- A reference has at least one target. [6]
- `alternative` exactly for `reconsider_on`; anchor targets name their path. [7]
- The invariant criteria's meanings, and which two the validator checks. [8]
- The family and decision criteria's meanings. [9]
- Origin names a leaf or a wave, not both. [10]

### Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

No cross-repo boundary is crossed by this file.
