# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Owns the sole structured curator-coherence authority resolver, validator, and exact no-impact
projection shared by memory readiness, closeout-door evidence, and closeout admission.

## Code Commentary

### Logic

`observe_curator_coherence_source` captures the isolated add-all code tree, external-memory tree,
candidate-relevant task topology, and exact ready memory-quality attestation. The stable manifest
selects one generation under the leaf's task-local history. `load_curator_coherence_authority`
proves manifest identity, content-addressed paths, record/report digests, deterministic projection,
and judgment-evidence bytes. `require_current_curator_coherence` then compares that record with a
fresh observation. `curator_coherence_no_impact` projects only the validated record's explicit
`no-content-impact` and `no-route-impact` identities for the onboarding body gates; it does not
derive semantic decisions. `current_curator_coherence_predecessor` digests even malformed stable bytes so a
prepared CAS repair cannot deadlock on a damaged pointer.

Candidate topology observation now supplies the already resolved authored graph to `graph_context`
and returns the sprint containing that context's sole bound immutable graph. Coherence therefore
hashes the same admitted graph generation as queue projection and the closeout door; a second mutable
resolution cannot be mixed into the frozen task-topology identity.

Under CCR-R03@v1 the observation and currentness seam binds declared dependencies. The attestation
reader takes `_QualityAttestationSource` (attestation/report paths, pair identity, and the exact
code/memory candidate trees) and re-requires the attestation's dependency declaration against those
trees (`memory-quality-attestation-dependencies-stale` refuses)
cit:([`_QualityAttestationSource`, `_quality_attestation`], mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:98-106; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:470-529).
`require_current_curator_coherence` runs `_require_current_dependencies`, which rebuilds the
`curator-coherence/v1` declaration from the record's code/memory candidate trees, topology
fingerprint, digest-bearing task intent, attestation/report digests, every judgment evidence digest,
and predecessor — refusing `curator-coherence-task-intent-missing`,
`evidence-dependencies-missing`, or `curator-coherence-dependencies-stale`
cit:([`require_current_curator_coherence`, `_require_current_dependencies`], mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:323-383; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:384-465).

### Conventions

Evidence references use exactly one explicit `code:`, `memory:`, or `task:` namespace. The resolver
confines each path to its named root and requires an existing file. Dependency declarations are
recomputed from the same canonical inputs the validator reads — never from caller-supplied tuples.

### Invariants And Boundaries

- There is one stable live manifest per external-memory leaf and no filename search fallback.
- Historical generations and attempt snapshots are audit evidence, not competing authority.
- The machine never parses curator Markdown; it regenerates and byte-compares the projection.
- Ready quality requires the exact attestation/report pair with all repair counts at zero.
- Every consumer calls `require_current_curator_coherence` or its evidence adapter.
- No-impact projection is candidate-bound and disposition-exact; downstream gates decide whether
  an accepted identity is actually eligible to clear.
- Coherence currentness now includes the declared dependency equality: a record whose code/memory
  trees, topology, intent, or evidence digests drift from its declaration refuses publication
  state, and no evidence digest points back into a semantic projection.

### Todos

None recorded.

## Docs References

No external source governs this repository-local lifecycle authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Observation freezes code, memory, task, and attestation identities. | `observe_curator_coherence_source` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:128-178 |
| Loading validates the sole manifest, generation bytes, generated projection, and evidence. | `load_curator_coherence_authority` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:237-322 |
| All admission paths share one currentness validator. | `require_current_curator_coherence`; `curator_coherence_evidence` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:323-383; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:466-469 |
| Exact current judgments project into separate content and route no-impact sets. | `CuratorCoherenceNoImpact`; `curator_coherence_no_impact` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:117-143 |
| Candidate task context binds the authored graph once and returns the bound sprint generation. | `_task_context` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:530-559 |
| Explicit evidence namespaces prevent implicit-root fallback. | `resolve_curator_evidence_ref` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:623-656 |
| R03 currentness re-requires the record's declared dependencies and the attestation's pair/tree binding. | `_require_current_dependencies`; `_quality_attestation` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:384-465; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:470-529 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| External memory is still the exact contract-resolved paired worktree, not an arbitrary repository. | `_require_leaf_external_memory` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:568-582 |

## MCAR-L03 Exact Pair Authority

Observation now proves the full pair before candidate-tree or attestation work. The source
attestation must name that same pair, the immutable record stores it, and currentness comparison
includes it. Pair failures retain their named field and exact repair arguments through the typed
coherence error adapter.

## 260831-CCR-R03 Dependency-Current Coherence

Coherence currentness now requires the record's typed `curator-coherence/v1` declaration and the
attestation's `memory-quality-attestation/v1` declaration to match the exact candidate trees,
topology, intent, and evidence digests; the door therefore stales exactly when a declared input
changes and never when unrelated semantics move (worker handover:
notes/reports/260902-CCR-L03-worker-delivery.md).

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the dependency-currentness seam (`_QualityAttestationSource`, `_require_current_dependencies`, attestation dependency re-requirement) added by the R03 leaf; prior graph-binding and pair authority prose preserved.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: candidate topology observation now binds
  the already resolved authored graph once and freezes the same immutable graph generation used by
  queue and door consumers. Verification remains closeout-owned.

- 2026-08-29T21:46+02:00 — MCAR-L03: made exact pair identity a first-class observation,
  attestation, record, and currentness fact. Verification remains closeout-owned.

- 2026-08-29T18:29+02:00 — Added the disposition-exact no-impact projection consumed by the
  onboarding body gates; semantic decisions remain curator/developer-owned.
- 2026-08-29T11:00+02:00 — Re-read the shared admission claim against the current source and
  widened its citation through `curator_coherence_evidence`; the disposition remains unchanged.
- 2026-08-29T08:52+02:00 — Created for the single structured coherence authority and shared
  currentness validator. Verification remains closeout-owned.