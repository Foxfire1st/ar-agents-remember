# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T05:25:19+00:00 |
| lastVerifiedCommitHash | `a0b2c18d2b8d08ac1242a13f65bde900a190df7a` |
| lastVerifiedCommitDate | 2026-09-27T07:57:14+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Owns the sole structured curator-coherence authority resolver, validator, and exact no-impact
projection shared by memory readiness, closeout-door evidence, and closeout admission.

## Code Commentary

### Logic

Live pointer loading delegates generation integrity to `curator_coherence_records`, addressed by the selected content digest. The same reader can open a named historical generation without reclaimed live quality files. `require_current_curator_coherence` remains strict: it observes live quality/dependencies and rechecks the original judgment inputs, so retained custody never grants live readiness. Path and namespace resolution now lives once in `curator_coherence_paths`.

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
cit:([`_QualityAttestationSource`, `_quality_attestation`], mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:108-114; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:450-507).
`require_current_curator_coherence` runs `_require_current_dependencies`, which rebuilds the
`curator-coherence/v1` declaration from the record's code/memory candidate trees, topology
fingerprint, digest-bearing task intent, attestation/report digests, every judgment evidence digest,
and predecessor — refusing `curator-coherence-task-intent-missing`,
`evidence-dependencies-missing`, or `curator-coherence-dependencies-stale`
cit:([`require_current_curator_coherence`, `_require_current_dependencies`], mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:347-443; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:285-344).

### Conventions

Evidence references use exactly one explicit `code:`, `memory:`, or `task:` namespace. The resolver
confines each path to its named root and requires an existing file. Dependency declarations are
recomputed from the same canonical inputs the validator reads — never from caller-supplied tuples.

### Invariants And Boundaries

- There is one stable live manifest per external-memory leaf and no filename search fallback.
- Historical generations and attempt snapshots are audit evidence, not competing authority.
- The machine never parses curator Markdown; it regenerates and byte-compares the projection.
- Ready quality requires the exact attestation/report pair with all repair counts at zero.
- Live readiness consumers use `require_current_curator_coherence`; recorded comparisons use the exact digest-addressed generation reader and do not select the live pointer.
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
| Observation freezes code, memory, task, and attestation identities. | `observe_curator_coherence_source` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:145-208 |
| Loading validates the sole manifest, generation bytes, generated projection, and evidence. | `load_curator_coherence_authority` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:227-272 |
| All admission paths share one currentness validator. | `require_current_curator_coherence`; `curator_coherence_evidence` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:285-344; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:446-447 |
| Exact current judgments project into separate content and route no-impact sets. | `CuratorCoherenceNoImpact`; `curator_coherence_no_impact` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:107-112; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:117-122; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:125-142 |
| Candidate task context binds the authored graph once and returns the bound sprint generation. | `_task_context` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:510-537 |
| Explicit evidence namespaces prevent implicit-root fallback. | `resolve_curator_evidence_ref` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_paths.py:37-68 |
| R03 currentness re-requires the record's declared dependencies and the attestation's pair/tree binding. | `_require_current_dependencies`; `_quality_attestation` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:347-443; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:450-507 |

The following declarations carry the changed boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| A named retained generation is read without asserting live readiness. | `load_curator_coherence_generation` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:275-282 |
| Current readiness still validates live inputs and dependencies. | `require_current_curator_coherence` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:285-344 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| External memory must remain the exact contract-resolved paired worktree. | `require_leaf_external_memory` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_paths.py:22-34 |

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

## KS-R15@v1 Assessment Read Projection And The Record's Own Edges

Two extensions, both on the read side.

`_require_current_dependencies` now recomputes one edge per stored assessment from **the record the
edge points at**: the digest in `review-record` is the assessment's own content address, so a reader
can tell that the stored assessment is the one the record declared rather than a record that was
edited beside it. The dependency is one-directional — the assessment's binding declares the inputs it
examined and deliberately does not declare the record it lives in — which keeps the binding out of the
self-invalidating sequence.

`curator_coherence_assessments` projects the stored collection through `assessment_state_for` without
deciding anything about it, and `curator_coherence_subject_assessment_state` reports one subject's
state; `all_assessment_subject_ids` enumerates the subjects a record holds. `260921-ICR-L15`
(`ICR-R15@v1`) replaced the caller's bare measurement mapping with the shipped
`AssessmentCurrentnessMeasurement` and classifies **per record** through
`supplied_measurement_statuses`, so what the caller supplies is a measurement of the world rather than
a set of stale ids: a record whose declared identities the measurement covers and agrees with is
`current`, one it holds a different value for is `stale`, and — the case this leaf fixed — an
assessment the caller supplied **no measurement for is reported `not-measured`, never `stale` and
never `current`**. Omitting the measurement therefore reports the collection's own identities and
dispositions without claiming either currency or movement: "not measured" is neither "still matches"
nor "has moved", and the old `_stale_assessment_ids` helper that produced the false movement is
deleted rather than aliased.

## KS-R23@v1 The Paths Resolve A Durable Attestation Copy

`260915-KS-L23` item 18's second measurement reached this resolver. `CuratorCoherencePaths` gained the
`attestations` directory (`:85`) and `attestation_copy(digest)` (`:93-103`), and
`curator_coherence_paths` resolves it at `:169` — inside the same
`notes/reports/curator-coherence/<leaf>/` history the record itself survives in (`:163-169`).

The copy's name is the attestation's own digest, so one digest names one file and a re-publication over
unchanged bytes reuses an immutable copy instead of rewriting it. It exists because the record's
`attestationPath` points inside the leaf's **enclosure**, which `lifecycle_finalize_task`'s automatic
cleanup reclaims: without a copy in the surviving task tree, an authority's `attestationSha256` commits
to bytes recoverable nowhere, and a reader cannot tell a candidate-empty publication from one whose
attestation listed candidates. This resolver only *names* the location — the write, its verification
against the observed digest, and the refusals that guard it live in the publication module (see that
card).

## Update History

- 2026-09-27T05:25:19+00:00 — Reconciled the L41 moved record/path owners and explicit retained-parent recovery boundary with current source. Prior generated history and real verification stamps are preserved.

- 2026-09-27T05:23:46+00:00 — Re-resolved 5 source-linked citation claim(s) against the extracted or shifted L41 owners. Each selected symbol uses its current declaration extent; other source references and prior generated history remain unchanged. Verification stamps remain closeout-owned.

- 2026-09-27T04:56:35+00:00 — Reconciled shared durable reading with strict live readiness after the owner extraction. Verification hashes/dates remain closeout-owned.
- 2026-09-23T12:00:00+02:00 — 260921-ICR-L15 curator (uncommitted change set; leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58` plus the working-tree delta): **cleared the two enforced `citation_anchor_absent_from_range` rows in this document (two table rows).** (a) The shared-admission row cited `:501-502` for `curator_coherence_evidence`, whose definition this candidate leaves at `:503-504`; the range was widened to `501-504`, which now reaches it. (b) The no-impact row cited `:115-141` for `curator_coherence_no_impact`; the projector's declaration is at `:143` (extent `:143-160`), so the range was widened to `115-160`, which now reaches it and still holds `CuratorCoherenceNoImpact` at `:136`. Claims, anchors and the other ranges are unchanged; no claim was re-worded and no range was dropped to silence a row. **Recorded rather than repaired:** the `KS-R15@v1 Assessment Read Projection` section below still states the superseded default — "an assessment the caller supplied **no entry for is reported `stale`**" — which this leaf's `ICR-R15@v1` change replaces: an omitted or empty measurement now answers `not-measured` through `supplied_measurement_statuses`, and the route overview's own `260921-ICR-L15 Measured assessment currentness` section records the new behaviour. No verification stamp was advanced: the candidate is uncommitted — the honest basis is the leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58` plus the working-tree delta — so no commit contains the content a stamp would claim to have verified, and the governed closeout owns the real code and memory commits.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-18T19:56:14+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the three enforced `citation_anchor_absent_from_range` rows in this document** (two table rows). (a) and (b) The no-impact row cited `107-112` and `115-132` for `CuratorCoherenceNoImpact` and `curator_coherence_no_impact`; this leaf's changes left the dataclass at `134` and the projector at `141`, so the second range was widened to `115-141`, which now reaches both. (c) The evidence row cited `487-488` (an exception branch) for `curator_coherence_evidence`, whose definition is at `501-502`; that cell cites it now. Claims, anchors and the other ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_require_leaf_external_memory` repointed to mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:673-685. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:25+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **recorded the durable attestation-copy path this leaf's item 18 added, which this card did not mention.** `CuratorCoherencePaths` now carries an `attestations` directory (`:85`) with `attestation_copy(digest)` (`:93-103`), resolved by `curator_coherence_paths` at `:169` beside the generations and attempt snapshots — the task-local tree the record survives in, so the bytes `attestationSha256` commits to outlive the enclosure that finalize's automatic cleanup reclaims. The section above states it and the boundary that this resolver only names the location while the publication owns the write and its refusals. The existing reference rows were left untouched for the citation-range repair pass that owns them, and the verification stamp is not advanced: the candidate is uncommitted and closeout owns the real code commit.
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:521-548` -> `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:551-578`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:614-645` -> `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:714-745`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:559-571` -> `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:659-671`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `_QualityAttestationSource`, `_quality_attestation`, `_require_current_dependencies`, `curator_coherence_evidence`, `require_current_curator_coherence` repointed to mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:314-372, mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:375-454, mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:457-458, mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:461-518, mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:98-104. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `CuratorCoherenceNoImpact`; `curator_coherence_no_impact` repointed to mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:107-112; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:115-132. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_task_context` repointed to mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:521-548. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `resolve_curator_evidence_ref` repointed to mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:614-645. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_require_leaf_external_memory` repointed to mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:559-571. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

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
