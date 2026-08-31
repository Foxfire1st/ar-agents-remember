# mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T08:05+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

This module runs one pinned Dagger quality graph in a clean Ubuntu/Playwright container and publishes its latest reports into the worktree enclosure. It replaces ad-hoc nested-Docker execution with one explicit, observable executor selected by settings.

## Code Commentary

### Logic

`run_clean_quality` validates mode and candidate roots, prepares an isolated sandbox containing the exact staged candidate and required Git ancestry, invokes the pinned Dagger module while streaming progress, and publishes only recognized reports. It parses the exported result rather than trusting the Dagger CLI transport exit code alone.

The recognized immutable report set includes both the source-built base-interpreter proof and the
candidate-venv proof (`python-runtime.json` and `python-venv-runtime.json`). Runtime provenance is
therefore exported with the same candidate-bound quality generation instead of living in an
ephemeral console transcript.

`_publish_reports` writes immutable generation artifacts and atomically publishes the schema-2.0
manifest pointer. Publication and recovery share `published_quality_manifest.py`; this module no
longer carries an alternate attestation-only reader. `published_quality_attestation` and
`published_report_path_from_manifest` both consume the already parsed strict snapshot.

Report publication preserves approved nested paths instead of flattening them. The exporter walks
the complete report tree without following links, rejects irregular entries and any file or
directory outside the explicit allowlist, hashes every relative file, copies parent directories
into one staged generation, validates the complete recursive inventory, and only then advances the
manifest pointer. This keeps the ambient E2E summary and both run reports in one coherent candidate
generation while path traversal, symlink substitution, and undeclared evidence fail closed.

Before advancing that pointer, the publisher strictly reads the prior canonical generation (when
present), validates every managed 64-hex historical generation entry without following links,
prunes stale generations while protecting both the prior live generation and the candidate, removes
the declared legacy projection, and repeats destination preflight. The atomic pointer replacement is
the final operation: there is no cleanup step that can commit a candidate and then report failure.

### Conventions

The Dagger, Codex, and base image versions are constants. The certifying graph and executor share
the exact Codex 0.151.0 pin so admission evidence cannot claim a different client than the container
actually executes. The scratch sandbox is self-overwriting inside the enclosure and is separate
from durable reports.

### Invariants And Boundaries

- No Docker socket or nested Docker daemon is mounted into the test container.
- Invalid/missing exported status fails closed; local quality is not a fallback.
- Candidate Git identity must match before and after sandbox materialization.
- Reports are atomically replaced, not accumulated per run.
- Base-runtime and venv-runtime proofs are recognized quality artifacts and are published only as
  members of the immutable result generation.
- `quality-report-set.json` has one strict object-root schema and one shared reader. Unknown fields,
  legacy shapes, malformed digest/size records, and partial manifests fail closed.
- Recovery callers pass one immutable manifest snapshot through every artifact lookup; a pointer
  rotation cannot mix generations.
- Nested report identity is relative-path preserving. Only declared files and their exact parent
  directories may be published; links and irregular filesystem entries are refused.
- Every managed historical-generation entry is inspected before cleanup; the prior live generation
  remains protected until the new pointer commits, and publication performs no fallible cleanup
  after that commit.
- Report promotion uses the kernel-owned `atomic_replace` primitive after copying to the target's
  sibling temporary file; this keeps replacement semantics on the shared platform boundary.

### Todos

None.

## Docs References

The repository source pins the toolchain; no external Domain Documentation source is configured in memory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Tool and image versions are repository-owned pinned inputs. | `DAGGER_VERSION`; `CODEX_VERSION`; `PLAYWRIGHT_IMAGE` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:49-54 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The executor validates, materializes, streams, parses, and publishes one clean quality run. | `run_clean_quality` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:112-193 |
| The export allowlist includes the base and venv Python runtime proof artifacts. | `EXPORTED_REPORT_NAMES` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:48-70 |
| Helper boundaries preserve Git identity, pre-pointer cleanup, atomic report publication, and native Dagger resolution. | `_publish_reports`; `_published_generation_or_none`; `_prune_report_generations`; `_resolve_dagger` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:299-351; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:428-435; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:560-579; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:703-704 |
| Recursive inventory and generation validation preserve nested evidence without accepting undeclared paths. | `_validated_export_inventory`; "def report_tree_inventory("; `_validate_generation` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:347-358; mcp/src/agents_remember/worktrees/modules/quality/report_publication_paths.py:62-78; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:523-540 |

## Cross-Repo References

The only external boundary is the pinned container/tool runtime, not a sibling repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| Dagger is explicitly resolved through the native subprocess boundary. | `_stream_dagger`; `_resolve_dagger` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:599-656; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:703-704 |

## 260821-DAGQC-L2 Canonical Publication Manifest

Report publication and crash recovery now share the strict schema-2.0 manifest model. The writer
publishes exactly the vocabulary the reader accepts, while recovery resolves attestation and result
paths from one captured snapshot. There is no compatibility reader or root-shape fallback.

## 260824-PDLS — Immutable Certifying Publication

The clean executor passes the Dagger admission facts into the graph, exports the route-neutral
`pytest-phases.json` beside the ordinary quality artifacts, and publishes one immutable schema-2
generation bound to the candidate tree. Only a digest-verified passed generation can mint
`CertifyingTestEvidence`. Diagnostic payloads and phase reports cannot be supplied as substitutes.

## Update History

- 2026-08-31T08:05+02:00 — 260821-ARSPAWN-L5 A004 correction: recorded strict prior-pointer
  resolution, pre-pointer historical-generation validation/pruning with prior-live protection, and
  the invariant that atomic pointer replacement is the final publication operation.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: documented recursive,
  allowlisted publication of the ambient E2E directory and staged-generation validation that
  prevents nested evidence from being silently discarded. Verification remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 refreshed the executor's exact Codex admission pin from 0.147.0 to 0.151.0 in lockstep with the certifying Dagger graph. Verification remains closeout-owned.

- 2026-08-29T16:27+02:00 — Added both canonical Python runtime proofs to the immutable recognized
  quality-report generation.

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
