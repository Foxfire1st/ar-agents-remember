# mcp/src/agents_remember/application/knowledge_export.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_export.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T17:45+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c`|
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The two boundaries this seam does not cross: an export is not a read response or a projection, and an import creates no commit and restores no ancestry.** | "an export is **not** a filtered read response"; "creates **no Git commit**" | mcp/src/agents_remember/application/knowledge_export.py:1-18 |
| The seam's public surface, including the two constants and the validation report re-exported for a consumer that must not import storage. | `__all__` | mcp/src/agents_remember/application/knowledge_export.py:46-57 |
| The export entry point. | `export_knowledge_artifact` | mcp/src/agents_remember/application/knowledge_export.py:60-63 |
| The import entry point and the carried no-promotion statement. | `import_knowledge_artifact` | mcp/src/agents_remember/application/knowledge_export.py:66-74 |
| **The read-only validation that produces no database at all.** | `validate_knowledge_artifact` | mcp/src/agents_remember/application/knowledge_export.py:77-96 |
| **The value-or-refusal file reader: `selected_input_unavailable` for an unreadable path, `invalid_export` for non-UTF-8 bytes.** | `read_knowledge_artifact` | mcp/src/agents_remember/application/knowledge_export.py:99-109 |
| **The body that is only handed out for an artifact the validator accepted.** | `canonical_body_of_artifact` | mcp/src/agents_remember/application/knowledge_export.py:112-126 |
| The defect the layer below makes unreachable. | `KnowledgeArtifactSeamDefect` | mcp/src/agents_remember/application/knowledge_export.py:129-130 |
| The four storage operations this seam delegates to. | `export_knowledge_dataset`; `import_knowledge_dataset`; `read_artifact`; `artifact_digest` | mcp/src/agents_remember/memory/knowledge/export_import.py:133-192; mcp/src/agents_remember/memory/knowledge/export_import.py:195-244; mcp/src/agents_remember/memory/knowledge/export_import.py:257-290; mcp/src/agents_remember/memory/knowledge/export_import.py:247-254 |
| The reader and validator the seam composes for its read-only half. | `parse_export`; `validate_export`; `logical_body_of_artifact` | mcp/src/agents_remember/memory/knowledge/export_portable.py:490-543; mcp/src/agents_remember/memory/knowledge/export_portable.py:667-712; mcp/src/agents_remember/memory/knowledge/export_portable.py:721-731 |
| The request and result vocabulary this seam takes and returns unchanged. | `ExportRequest`; `ExportResult`; `ImportRequest`; `ImportResult`; `PortableValidation` | mcp/src/agents_remember/models/knowledge/portable.py:36-44; mcp/src/agents_remember/models/knowledge/portable.py:101-133; mcp/src/agents_remember/models/knowledge/portable.py:47-63; mcp/src/agents_remember/models/knowledge/portable.py:136-176; mcp/src/agents_remember/models/knowledge/portable.py:66-98 |
| The three sibling seams this module sits beside. | `write_authorship`; `publish_prepared_knowledge_snapshot`; `merge_resolved_knowledge_datasets` | mcp/src/agents_remember/application/knowledge.py:102-124; mcp/src/agents_remember/application/knowledge_snapshot.py:142-147; mcp/src/agents_remember/application/knowledge_merge.py:55-64 |
|  The layer ranks that make a lower owner consume models rather than this module. | "package.memory"; "package.application" | layers.toml:206-207; layers.toml:314-315  |
| The nodes that drive the conforming round trip and the read-only recovery recipe through the public operations. | "test_a_populated_dataset_round_trips_to_an_equal_logical_dataset"; "test_a_filtered_read_response_cannot_validate_as_a_complete_export" | mcp/tests/test_knowledge_portable_roundtrip.py:356-427; mcp/tests/test_knowledge_portable_roundtrip.py:712-739 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The artifact may be exported to and imported
from anywhere, but nothing in this seam reads another repository or writes a ledger row.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T17:45+02:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): created this one-to-one card for the new fourth composition seam. It records the five entry points — the two pure delegations, the read-only validation that produces **no database at all**, the value-or-refusal file reader whose two failures carry different codes, and `canonical_body_of_artifact`, which **validates before it returns a body** because a body is what a comparison is made of and a refused artifact has no dataset identity to compare — plus the carried non-claims the ruled design made explicit: an export is not a filtered read response and not a Markdown projection, and an import creates no Git commit and restores no Git ancestry. It re-records the wiring boundary because it did not move: like its three siblings, this seam has **no non-test importer in `mcp/src`**. Verification metadata remains empty until closeout stamps the code commit.
