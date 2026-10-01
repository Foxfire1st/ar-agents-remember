# mcp/src/agents_remember/application/knowledge_export.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The fourth composition seam of the knowledge substrate**: the portable export/import boundary, beside
the single candidate write in `application/knowledge.py`, the candidate-lifecycle/publication seam in
`application/knowledge_snapshot.py` and the guarded merge in `application/knowledge_merge.py`.

It exists for the same reason as the three before it: exporting and importing a whole dataset is a
different composed operation from a candidate write, a snapshot publication or a merge, and keeping them
apart leaves each entry point readable as one intent. Nothing here decides authority and nothing here
holds durable state: it hands the typed request to `memory.knowledge` and returns the typed result
unchanged, so a lower owner — the worktree or lifecycle package that wants to carry a dataset between
candidates — receives `agents_remember.models.knowledge` values and never an import of the store.

**Two boundaries this seam does not cross, stated where a reader of the artifact will look for them:** an
export is **not** a filtered read response and **not** a Markdown projection, and an import creates **no
Git commit** and restores **no Git ancestry**. Capturing an exported artifact into a memory tree, or
committing a restored database, is the existing candidate-tree and closeout owner's operation.

## Code Commentary

### Logic

Five entry points, and the two that are pure delegation are named for what the caller asked:

- `export_knowledge_artifact(request)` delegates to `export_knowledge_dataset` and returns the
  `ExportResult` unchanged. The encoder has no filesystem side effect: a caller that wants the artifact on
  disk writes `ExportResult.artifact` through the repository's own atomic write.
- `import_knowledge_artifact(request)` delegates to `import_knowledge_dataset` and returns the
  `ImportResult` unchanged. Importing a row whose stored `state_at_origin` says `accepted` imports that
  *value*; it grants the receiving context no authority, and nothing on this path promotes a record.
- `validate_knowledge_artifact(text, *, expected_repository_id=None)` is the **read-only half** of the
  import: it answers whether the artifact is a complete export of a supported generation and what logical
  dataset it holds, and it produces **no database at all**. It returns the validator's own
  `PortableValidation` — a refused verdict under `state="refused"` with the refusal inside, never a raised
  exception.
- `read_knowledge_artifact(path)` reads one artifact file as text, or returns the typed refusal that says
  why it is not one. A file that cannot be read at all is `selected_input_unavailable`; bytes that are not
  UTF-8 are `invalid_export`. Nothing on this path is persisted and nothing raises — an `OSError` or a
  `UnicodeDecodeError` handed to a caller to catch would be a failure with no code to branch on.
- `canonical_body_of_artifact(text)` returns the canonical logical body one **validated** artifact carries,
  or the refusal. **Validation comes first on purpose**: a body is what a comparison is made of, and an
  artifact the validator refuses — a filtered projection, a document that dropped a collection, one whose
  declared seal does not cover its records — has no dataset identity to compare against, so returning a
  body for it would hand a caller the shape of a comparison it must not make. It is the read-only half of
  the recovery recipe, so it produces no database and no artifact, and the refusal it returns is the
  validator's own.

`KnowledgeArtifactSeamDefect` is the one internal state the layer below makes unreachable — a validation
that returned neither a report nor a refusal — and it is a defect rather than a caller-facing refusal for
exactly that reason.

### Conventions

- Every function is a delegation or a bounded composition with a docstring that states the boundary it does
  not cross; the module keeps no state, opens nothing itself and closes nothing.
- The seam returns storage's typed values unchanged, so a caller can branch on `state`/`refusal` without
  an application-level wrapper type — the same shape the three sibling seams use.
- The value-or-refusal contract is applied consistently on **both** halves: `read_knowledge_artifact`
  returns `str | KnowledgeRefusal`, `canonical_body_of_artifact` returns `dict | KnowledgeRefusal`, and a
  caller branches rather than catching.
- `__all__` names the seam's surface, including the two re-exported constants (`EXPORT_FORMAT`,
  `PORTABLE_NOTES`, `PortableValidation`) a consumer needs without importing storage.

### Invariants And Boundaries

- **No authority is conferred here.** The request models carry the identities a caller admitted; approval,
  acceptance and task status are not representable in anything this module returns.
- **No durable state and no Git.** The module creates no commit, moves no ref and writes no ledger row.
- **Storage ranks below application.** No lower-ranked package may import this module; a lower owner
  receives `models.knowledge` values.
- **A filtered read response is not a backup.** `validate_knowledge_artifact` is what refuses one, and the
  seam never exposes a path that could accept a partial projection as a complete export.
- **The seam is not yet wired.** Like the three sibling seams, this module has **no non-test importer in
  `mcp/src`** as of this leaf: the supported-MCP-name wiring is an explicit later extension, and this
  leaf's requirement claims the operation, not a tool.

### Todos

None recorded for this slice. The unwired status is a carried limitation of the increment, not a defect
this leaf left open.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The two boundaries this seam does not cross: an export is not a read response or a projection, and an import creates no commit and restores no ancestry.** [1]
- The seam's public surface, including the two constants and the validation report re-exported for a consumer that must not import storage. [2]
- The export entry point. [3]
- The import entry point and the carried no-promotion statement. [4]
- **The read-only validation that produces no database at all.** [5]
- **The value-or-refusal file reader: `selected_input_unavailable` for an unreadable path, `invalid_export` for non-UTF-8 bytes.** [6]
- **The body that is only handed out for an artifact the validator accepted.** [7]
- The defect the layer below makes unreachable. [8]
- The four storage operations this seam delegates to. [9]
- The reader and validator the seam composes for its read-only half. [10]
- The request and result vocabulary this seam takes and returns unchanged. [11]
- The three sibling seams this module sits beside. [12]
- The layer ranks that make a lower owner consume models rather than this module. [13]
- The nodes that drive the conforming round trip and the read-only recovery recipe through the public operations. [14]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The artifact may be exported to and imported
from anywhere, but nothing in this seam reads another repository or writes a ledger row.

No meaningful cross-repo references found.
