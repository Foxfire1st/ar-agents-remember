# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py

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
cit:([`_QualityAttestationSource`, `_quality_attestation`], mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:109-115; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:475-532).
`require_current_curator_coherence` runs `_require_current_dependencies`, which rebuilds the
`curator-coherence/v1` declaration from the record's code/memory candidate trees, topology
fingerprint, digest-bearing task intent, attestation/report digests, every judgment evidence digest,
and predecessor — refusing `curator-coherence-task-intent-missing`,
`evidence-dependencies-missing`, or `curator-coherence-dependencies-stale`
cit:([`require_current_curator_coherence`, `_require_current_dependencies`], mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:372-468; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:286-346).

**The mandatory invariant gate (MIK-R09 rule 3, leaf 260928-MIK-L09).** After every other check passes,
`require_current_curator_coherence` calls `_require_knowledge_gate(contract, observation)`, which asks
`worktrees.knowledge_gate.leaf_gate_refusal` over the very code and memory candidate trees this authority binds
(`observation.code_candidate_tree`, `observation.memory_candidate_tree`). On converted memory the gate recomputes the
worklist, decides every item through its kind's predicate and runs the validator (as a leaf publication, against the
parent line's memory tip); any open item, incomplete run or violation raises `curator-coherence-knowledge-gate-refused`
with next action `memory_quality_check`, naming every finding. A converted leaf with no bound gate refuses
(`GATE_UNBOUND`). An unconverted leaf is not gated and is validated exactly as before. The curator-coherence record,
its identity checks and pair identity are unchanged (MIK-R09 Preservation): the gate is one more refusal after them.
Because the curator publication computed the same memo key, this read is normally served from the gate's memo.
cit:([`_require_knowledge_gate`, "_require_knowledge_gate(contract, observation)"], mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:345-369).

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

## Evidence

### Docs References

No external source governs this repository-local lifecycle authority.

No configured Domain Documentation source applies.

### Repo-Internal References

- Observation freezes code, memory, task, and attestation identities. [1]
- Loading validates the sole manifest, generation bytes, generated projection, and evidence. [2]
- All admission paths share one currentness validator. [3]
- Exact current judgments project into separate content and route no-impact sets. [4]
- Candidate task context binds the authored graph once and returns the bound sprint generation. [5]
- Explicit evidence namespaces prevent implicit-root fallback. [6]
- R03 currentness re-requires the record's declared dependencies and the attestation's pair/tree binding. [7]

The following declarations carry the changed boundary.

- A named retained generation is read without asserting live readiness. [8]
- The closeout validator's gate over the exact candidate, refusing with every finding (MIK-R09). [9]
- The closeout validator refuses until the gate passes and never runs ungated. [10]
- Current readiness still validates live inputs and dependencies. [11]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings.

- External memory must remain the exact contract-resolved paired worktree. [12]

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
