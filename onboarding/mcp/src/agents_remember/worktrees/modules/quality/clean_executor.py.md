# mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

This module runs one pinned Dagger quality graph in a clean Ubuntu/Playwright container and publishes its latest reports into the worktree enclosure. It replaces ad-hoc nested-Docker execution with one explicit, observable executor selected by settings.

## Code Commentary

### Logic

`run_clean_quality` validates mode and candidate roots, prepares an isolated sandbox containing the exact staged candidate and required Git ancestry, invokes the pinned Dagger module while streaming progress, and publishes only recognized reports. It parses the exported result rather than trusting the Dagger CLI transport exit code alone.

`_publish_reports` writes immutable generation artifacts and atomically publishes the schema-1.0
manifest pointer. Publication and recovery share `published_quality_manifest.py`; this module no
longer carries an alternate attestation-only reader. `published_quality_attestation` and
`published_report_path_from_manifest` both consume the already parsed strict snapshot.

### Conventions

The Dagger, Codex, and base image versions are constants. The scratch sandbox is self-overwriting inside the enclosure and is separate from durable reports.

### Invariants And Boundaries

- No Docker socket or nested Docker daemon is mounted into the test container.
- Invalid/missing exported status fails closed; local quality is not a fallback.
- Candidate Git identity must match before and after sandbox materialization.
- Reports are atomically replaced, not accumulated per run.
- `quality-report-set.json` has one strict object-root schema and one shared reader. Unknown fields,
  legacy shapes, malformed digest/size records, and partial manifests fail closed.
- Recovery callers pass one immutable manifest snapshot through every artifact lookup; a pointer
  rotation cannot mix generations.
- Report promotion uses the kernel-owned `atomic_replace` primitive after copying to the target's
  sibling temporary file; this keeps replacement semantics on the shared platform boundary.

### Todos

None.

## Docs References

The repository source pins the toolchain; no external Domain Documentation source is configured in memory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Tool and image versions are repository-owned pinned inputs. | `DAGGER_VERSION`; `CODEX_VERSION`; `PLAYWRIGHT_IMAGE` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:40-45 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The executor validates, materializes, streams, parses, and publishes one clean quality run. | `run_clean_quality` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:112-193 |
| Helper boundaries preserve Git identity, atomic report publication, and native Dagger resolution. | `_publish_reports`; `_resolve_dagger` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:276-351; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:597-598 |

## Cross-Repo References

The only external boundary is the pinned container/tool runtime, not a sibling repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| Dagger is explicitly resolved through the native subprocess boundary. | `_stream_dagger`; `_resolve_dagger` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:491-548; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:597-598 |

## 260821-DAGQC-L2 Canonical Publication Manifest

Report publication and crash recovery now share the strict schema-1.0 manifest model. The writer
publishes exactly the vocabulary the reader accepts, while recovery resolves attestation and result
paths from one captured snapshot. There is no compatibility reader or root-shape fallback.

## 260824-PDLS — Immutable Certifying Publication

The clean executor passes the Dagger admission facts into the graph, exports the route-neutral
`pytest-phases.json` beside the ordinary quality artifacts, and publishes one immutable schema-2
generation bound to the candidate tree. Only a digest-verified passed generation can mint
`CertifyingTestEvidence`. Diagnostic payloads and phase reports cannot be supplied as substitutes.

## Update History

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T21:23+02:00 — 260824-PDLS added phase export and the sole certifying evidence factory
  at verified publication altitude.
- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: unified report publication and recovery on the strict schema-1.0 manifest and one-snapshot artifact lookup. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: report publication now carries an attestation; added `published_quality_attestation`. Verification remains closeout-owned.

- 2026-08-14T06:36+02:00 — L23 final candidate review: the Dagger executor starts a fresh attempt,
  makes two report projections share one authoritative result, bounds live output, prunes stale
  predecessor reports, and fails closed on status reads; no local runner remains.

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: recorded that report promotion now routes through `kernel.atomic_write.atomic_replace` instead of calling `os.replace` directly. Verification metadata remains closeout-owned.

- 2026-08-12T15:19+02:00 — Created for L23's pinned, observable Dagger quality executor; verification provenance remains closeout-owned.
