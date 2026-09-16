# mcp/src/agents_remember/application/knowledge_snapshot.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_snapshot.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T11:30+02:00 |
| lastVerifiedCommitHash | `3332a4ce7029777d49feca22b499350435a9f83c`|
| lastVerifiedCommitDate | 2026-09-16T11:50:16+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The second composition seam of the knowledge substrate**: the candidate lifecycle (create, clone, open,
disposal authorization) and snapshot publication, as one composed operation beside the single candidate write in
`application/knowledge.py`. Both seams exist so each entry point reads as one intent; nothing here decides
authority and nothing here holds durable state.

It admits a candidate directory plus an explicit resolution into typed values, delegates to
`memory.knowledge`, and returns the typed result **unchanged**. Storage ranks below application, so a lower owner
— the worktree or memory-quality package that captures a published database — receives
`models.knowledge` values and never an import of this module or of the store.

Two non-claims are load-bearing and were deliberate in the ruled design:

- **No Git commit.** The published snapshot is a closed *file*; capturing it into a memory tree is the existing
  candidate-tree owner's operation. This module creates no commit, moves no ref and writes no ledger row.
- **No IAS landing.** The writable candidate belongs to the experimental master; a landing on the parent sprint is
  a separate decision and is not reachable from anything here.

## Code Commentary

### Logic

Nine thin entry points, each a rename of one storage operation onto admitted inputs:

- `admitted_candidate_destination(directory, repository, resolution)` is the constructor the admitted-authority
  path calls after its own checks. It confers no authority by itself; it exists so the lifecycle and publication
  operations receive a typed handle rather than a bare path, which is what keeps a deserialized request from
  becoming admitted input.
- `candidate_write_destination(candidate, authorship)` addresses the single-record and batch write operations at
  this candidate's database. The path is **derived from the layout** rather than passed a second time, so a caller
  cannot write into one database and publish another; the `authorship` envelope is the admitted provenance for the
  writes, and the receipt binds the candidate, not the writer.
- `create_knowledge_candidate` / `clone_knowledge_candidate` / `open_knowledge_candidate` delegate to
  `create_candidate` / `clone_candidate` / `open_candidate`.
- `authorize_knowledge_candidate_disposal` delegates to `authorize_candidate_disposal` and returns the verdict.
- `publish_knowledge_snapshot(candidate, request)` freezes and installs one candidate's point;
  `publish_prepared_knowledge_snapshot(prepared, request)` installs an already-frozen stage through the **same**
  publication contract, so a caller that produced a validated closed database (a merged result, an import, a
  restored artifact) reaches the destination on the same path.
- `knowledge_publication_state(candidate, published_path)` compares a live candidate with the closed snapshot a
  read is about to answer from, and returns the measurement.

### Conventions

- Every function is a pure delegation with a docstring that states the boundary it does not cross; the module
  keeps no state, opens nothing itself and closes nothing.
- The seam returns storage's typed values unchanged, so a caller can branch on `state`/`refusal` without an
  application-level wrapper type — the same shape `application/knowledge.py` uses.
- The docstrings state the two non-claims (no commit, no IAS landing) rather than leaving them to be inferred.

### Invariants And Boundaries

- **Path derivation is one-way.** `candidate_write_destination` derives the database path from the admitted
  candidate, so write and publish cannot name different files.
- **No authority is conferred here.** The admitted destination is a shape, not a grant; approval, acceptance and
  task status are not representable in anything this module returns.
- **No durable state and no Git.** The module creates no commit, moves no ref and writes no ledger row; capturing
  a published snapshot belongs to the candidate-tree owner.
- **Storage ranks below application.** No lower-ranked package may import this module; a lower owner receives
  `models.knowledge` values.
- **The seam is not yet wired to a tool.** Like `application/knowledge.py`, this module has no non-test importer
  in `mcp/src` as of this leaf; transport wiring remains an explicit later extension.

### Todos

None recorded for this slice. The unwired status is a carried limitation of the increment, not a defect this leaf
left open: wiring a public tool name is a later extension by the packet's own statement.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The admitted-destination constructor that confers no authority by itself. | `admitted_candidate_destination` | mcp/src/agents_remember/application/knowledge_snapshot.py:67-82 |
| The write destination derived from the candidate layout rather than passed twice. | `candidate_write_destination` | mcp/src/agents_remember/application/knowledge_snapshot.py:85-99 |
| The three lifecycle delegations. | `create_knowledge_candidate`; `clone_knowledge_candidate`; `open_knowledge_candidate` | mcp/src/agents_remember/application/knowledge_snapshot.py:102-107; mcp/src/agents_remember/application/knowledge_snapshot.py:110-115; mcp/src/agents_remember/application/knowledge_snapshot.py:118-123 |
| The disposal-authorization delegation. | `authorize_knowledge_candidate_disposal` | mcp/src/agents_remember/application/knowledge_snapshot.py:126-131 |
| The two publication entry points that share one contract. | `publish_knowledge_snapshot`; `publish_prepared_knowledge_snapshot` | mcp/src/agents_remember/application/knowledge_snapshot.py:134-139; mcp/src/agents_remember/application/knowledge_snapshot.py:142-147 |
| The read-side publication gate. | `knowledge_publication_state` | mcp/src/agents_remember/application/knowledge_snapshot.py:150-155 |
| The candidate lifecycle this seam delegates to. | `create_candidate`; `clone_candidate`; `open_candidate`; `authorize_candidate_disposal` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:85-98; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:100-126; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:129-138; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:141-173 |
| The publication half this seam delegates to. | `publish_candidate_snapshot`; `publish_prepared_snapshot` | mcp/src/agents_remember/memory/knowledge/publication.py:66-111; mcp/src/agents_remember/memory/knowledge/publication.py:114-170 |
| The read-side comparison this seam exposes. | `publication_state` | mcp/src/agents_remember/memory/knowledge/materialization.py:34-99 |
| The sibling seam this module sits beside, and the provenance envelope it reuses. | `write_authorship`; `Authorship`; `AdmittedKnowledgeDestination` | mcp/src/agents_remember/application/knowledge.py:102-124; mcp/src/agents_remember/models/knowledge/authorship.py:32-60; mcp/src/agents_remember/models/knowledge/context.py:32-37 |
| The vocabulary these entry points take and return. | `AdmittedCandidateDestination`; `CandidateBaseline`; `CandidateDisposition`; `PublishSnapshotRequest`; `SnapshotPublicationResult`; `PublicationState` | mcp/src/agents_remember/models/knowledge/snapshot.py:70-93; mcp/src/agents_remember/models/knowledge/snapshot.py:96-106; mcp/src/agents_remember/models/knowledge/snapshot.py:351-354; mcp/src/agents_remember/models/knowledge/snapshot.py:252-256; mcp/src/agents_remember/models/knowledge/snapshot.py:259-293; mcp/src/agents_remember/models/knowledge/snapshot.py:296-321 |
| The composed-path support module that drives this seam end to end. | `build_case`; `create`; `clone`; `publish` | mcp/tests/snapshot_lifecycle_test_support.py:177-205; mcp/tests/snapshot_lifecycle_test_support.py:207-211; mcp/tests/snapshot_lifecycle_test_support.py:213-221; mcp/tests/snapshot_lifecycle_test_support.py:357-379 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): created this one-to-one card for the new candidate-lifecycle/publication composition seam. It records the derived write destination that keeps write and publish on one file, the two publication entry points sharing one contract, the two non-claims the ruled design made explicit (this seam creates no Git commit, and no IAS landing is reachable from it), and the carried limitation that — like `application/knowledge.py` — it still has no non-test importer in `mcp/src`, because public tool wiring is a later extension. Verification metadata remains empty until closeout stamps the code commit.
