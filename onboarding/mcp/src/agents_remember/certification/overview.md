# Certification Contract Overview

## Governing Overview
[MCP overview](../../../overview.md)

## Purpose

This area supplies the repository-neutral contracts for five ordered closeout gates: pre-test code quality; the ordinary test suite; post-test code quality consuming declared suite artifacts; clean-room integration and end-to-end testing; and memory-domain onboarding, citation, and coherence quality. It owns canonical registry and profile vocabulary, bounded admission, deterministic plans, content identities, typed terminal results, certificates, and lifecycle boundary records. These contracts describe what an executor or lifecycle owner must supply; compiling them does not prove execution or acceptance.

Gate meaning is fixed. Concrete Gate 1–4 inventories, adapters, commands, runtime inputs, publication policies, ownership, and applicability belong to repository-profile data. The concrete Agents Remember profile remains outside this package at `mcp/certification-profile-v1.json`. Gate 5 remains memory-domain authority: this package consumes its rail declarations and exact inputs rather than owning memory checker execution.

`layers.toml` declares certification at rank 3, after root errors, feature-free kernel primitives, and served wire models, and before control-plane, worktree, and application consumers. This is an allowed-dependency and responsibility contract, not a report that the current graph passed a checker. Concrete profiles, executors, lifecycle terminalization, and memory gates remain with their owners. The adjacent control-plane package owns durable interaction records and their policy. The architecture declares strict downward imports with no baseline or exceptions; its historical checker claims are not fresh verification here.

## Hot Path Summary

Start with `certification_lane.py` for the R22 repository-plan to R11 registry/plan bridge, `certificate_admission.py` for exact authority alignment, and `results.py` plus `certificate_authority.py` for complete terminal catalogs and green certificate issuance. The bridge preserves applicable repository rails' adapter, runtime, evidence, artifact, applicability, and ownership contracts. An explicitly not-applicable repository gate instead contributes a bounded applicability declaration carrying its reason and plan identity; it makes no rail-execution or suite-artifact claim. Missing Gate-5 rails or rails outside Gate-5 memory-domain authority refuse admission.

The production quality owner freezes a complete `FrozenCertificationRun` before execution. It retains the canonical repository profile, repository plan, generic registry and certification plan, original admission, and provenance. Recovery reopens the supplied frozen object by its exact stored reference rather than discovering authority from summary journals. Generic admission and gate-certificate semantic identities exclude creation provenance; the complete frozen-run digest includes it.

`worktrees/modules/quality/gate.py` resolves that authority, invokes the clean quality executor, and processes a published terminal generation before its nonzero-return refusal. `certification_run.py` reads the exact decoder artifact and passes its catalog to `certification_records.py`. That seam requires the exact candidate, profile digest, repository-plan digest, and selection. Complete supplied green, red, interrupted, and not-applicable observations have distinct handling; unsupported or insufficient observations remain typed refusals. Certificates require validated green results, while non-green results and interrupted publication do not acquire certificates.

Publication verifies every nested result evidence and artifact binding against the accepted immutable report generation. Selected certificates and terminal results retain their original object references and physical publication; selected certificate generations are protected until journal replacement or cleanup. Selected code readback requires the complete Gate 1–4 prefix, original stored objects, publication authority, nested evidence verification, and certificate-chain validation. The strict success path additionally requires certifying lifecycle evidence and an unchanged staged candidate. A missing publication or an exception before publication is not a complete terminal catalog.

`lifecycle_admission.py` and `lifecycle_recovery.py` supply contracts consumed by `worktrees/integration/closeout/certification/admission.py`, `selection.py`, and `recovery.py`. The closeout owner observes real candidate authorities, compiles admission and recovery, and derives input changes from retained owner objects. The application composition supplies prepared memory certification and the finalization continuation. Library functions and default bindings establish construction seams, not proof that a particular operation completed.

## Construction And Ownership

`canonical.py`, `limits.py`, `validation.py`, and `planning.py` form the generic registry-to-plan pipeline. Canonicalization collapses exact semantic duplicates while retaining conflicting declarations for validation. Admission bounds work before expensive normalization, digest allocation, or semantic finding materialization. Within the admitted boundary, validation gathers independently discoverable findings and planning binds the canonical registry digest, selected profile, exact candidate, complete gate rail catalogs, and deterministic execution waves.

`repository_profiles/authority.py` resolves exactly one explicit canonical repository-relative profile file, rejects traversal, symlink components, escape, and wrong repository identity, then parses, canonicalizes, and validates it. There is no profile-discovery substitute for missing authority. `repository_profiles/planning.py` binds repository selections and semantic inputs. Environment reconstruction, generated candidate inputs, rail execution/runtime, selectors, executor adapters, result decoders, and publication policies retain their declared consuming gates and content identities. Semantic inputs are deterministically ordered and duplicate input identities refuse compilation.

`repository_profiles/source_selection/` owns explicitly declared source-path applicability over an exact candidate source observation. Its compiler selects declared changed paths; full mode makes such a rail applicable, while other modes use whether the declared path selection is nonempty. The decision binds its declaration, source observation, mode, selected paths, and applicability reason/identity. This contract does not replace dependency-closure test selection or prove gate execution.

`frozen_run/` retains the original admission and candidate-authority records before execution. Its complete run model recompiles admission alignment, requires the exact original admission, and verifies its whole-record digest. Summary admission and gate journals serve presentation and retention; supplied immutable owner references select recovery authority.

Memory rail composition crosses an explicit worktree service port. `certification_records.py` refuses an unbound `certification_memory_rails` port. The default application adapter delegates to `memory_quality/gate_five_rails.py`, which derives one enforcing, applicable, memory-domain rail per complete final-catalog item with deterministic identities, configuration, and ordering. The records seam does not contain the former repository-name restriction. Neither the generic bridge nor the worktree records owner absorbs the memory checker registry.

`telemetry/` owns a separate observation vocabulary and durable stream. Its closed execution kinds, event matrix, certificate dispositions/refusal codes, terminal classes, and immutable event schema constrain event identity and cardinality. Adapters project owner-produced R11/R20/R21/R22 objects without inventing authority. The store publishes content-addressed, digest-chained revisions with CAS checks, separate closeout-generation and diagnostic-run envelopes, operation-scoped capacity, and a named reclamation owner. Projection preserves boundary and Gate 1–5 observations with a content digest. Stream validation reports missing, duplicate, out-of-order, cross-identity, cardinality-invalid, and result-inconsistent observations; it neither reruns rails nor derives a rail pass from telemetry alone. Diagnostic events cannot acquire gate, certificate, delivery, approval, or finalization authority.

`diagnostics/` represents the optional non-certifying real-Codex replication of the canonical scenario catalog. Result types fix `acceptanceEligible=false` and `certifying=false`, bind exact candidate/plan/environment/runtime authority and diagnostic nonce, and keep scenario, infrastructure, parser, aborted, and hard-failure outcomes distinct. Pass/fail results carry diagnostic-altitude manifests; immutable attempt/result chains retain their digests. Planning requires a diagnostic profile with the complete earlier-gate prefix and the canonical certifying scenario rail contracts, refusing a second scenario catalog. The readiness projection permits not-requested-optional only for an absent lane, preserves requested history, selects the newest terminal result, and blocks on a failing or plan-stale terminal result. Historical passes cannot erase newer failure, and diagnostic passes never satisfy final certification. The worktree diagnostic executor owns trusted R12 admission and the Gate 1–3 green barrier; it delegates runner/store ownership rather than privately provisioning or retiring shared resources.

`final_codex/` represents the certifying Gate-4 two-fresh, independent, no-retry proof. Its closed types fix acceptance eligibility and certification true, retry count zero, exact candidate/plan/runtime binding, fresh per-repetition identities, typed failures, teardown records, and self-verified digests. One passing repetition cannot compensate for a failed, aborted, stale, retried, or authority-mismatched repetition. Planning requires the exact canonical R11 certifying plan and complete Gate 1–4 prefix; the predecessor barrier requires exact green certifying Gate 1–3 manifests for that candidate and plan. Projection distinguishes not-started, running, two-fresh-pass, red, and stale. Certificate compilation binds both repetition results, teardown, shared runtime authority, and ordered Gate 1–3 certificate identities. Diagnostic evidence has no certifying result shape here. Actual control belongs to the worktree final-Codex executor and trusted R12 authority.

Diagnostic and final-Codex stores keep stable candidate manifests, immutable ordered results, digest verification, and typed CAS refusals. Final-Codex refuses another live attempt and a terminal successor with the same plan identity; changed plan identity is a distinct admission, not a retry slot. Partial publication cannot become two-fresh-pass. Namespace separation remains required intent. The local stores enforce equal/ancestor/descendant overlap refusal against the `forbiddenRoots` supplied in their policies; those lists default empty, so these constructors alone do not establish that all forbidden production roots were supplied.

`replay/` owns the measured replay protocol, not a performance acceptance claim. Freeze identity binds source revision, candidate sequence, R22 profile, R11 plan, configuration, runtime/toolchain/executor/image, machine class, instrumentation, and measurement schema; observation metadata is excluded from pair identity. The incident population retains frozen-original generations 1–8, post-analysis-tail generations 9–13, and append-only dated supplements 14+. The denominator helper includes original and tail strata and excludes supplements. Span reduction computes reproducible per-category union-wall measurements; measurement folds R16 exports into gate facts; seventeen mandatory scenario projections and the digest-bound baseline/treatment comparison consume measured evidence. Outcomes include green, red, refused, and not-applicable vocabulary. Numeric reduction thresholds are intentionally absent: protocol availability is neither a completed replay nor an approved numeric cost-reduction claim.

The route facade exposes the contract subpackages. That public surface does not establish a production caller for every API.

## Invariants And Boundaries

Registry work is refused when its admission budget cannot be satisfied; it is not truncated or silently replaced with safe-full selection. Reachability performs a prospective storage refusal before allocating its digest/query structures, then measured traversal reservations. It does not repeat the dominated exact-storage refusal. Exact duplicates may collapse; conflicting variants remain visible. The bounded registry pipeline supplies no compatibility or fallback selection path.

Plans and results remain exact to their admitted registry, profile, candidate, and gate contracts. Dependencies and artifact consumption cannot depend on later gates. Applicable Gate 3 certification must bind at least one exact artifact from the green Gate-2 certificate, with all consumed artifacts coming from Gate 2. Explicit not-applicability is an applicability disposition rather than a test pass or suite artifact; the applicable-Gate-3 condition matters.

Terminal result compilation requires every planned rail exactly once and validates identity, applicability, evidence, artifacts, ownership/posture contracts, and blocker semantics. A failed direct same-gate prerequisite requires a blocked dependent result with exactly those blockers; an independent rail cannot be silently marked blocked. Enforcing fail/blocked results make the gate red. Report-only or diagnostic observations cannot promote a failing enforcing result into certifying success. Generic wrapper exceptions are not substitutes for typed terminal catalogs and their evidence.

Green certificate issuance requires aligned admitted authority, exact current predecessors or explicitly retained predecessor authority, certifying profile and altitude, and complete green results. Gate 5 requires exact memory semantic inputs; Gates 1–4 forbid those inputs. Physical evidence verification and publication retention belong to the quality/lifecycle owners that consume these contracts.

Lifecycle admission retains exact candidate and authority observations with zero gate starts. Recovery binds admitted certificate identities, classified input changes, and reuse decisions. Finalization requires a currentness reread of candidate, certificate authority, operation/door/approval authority, commit intent, and journal state, and authorizes only the exact unfinished durable leg with zero certification starts. It does not own Git publication or lifecycle terminalization.

Inherited preparation intent limits commit outputs to code and memory content; the computed ledger contributes no additional preparation output or acceptance identity. Present `FinalizationLeg` and `_FINALIZATION_LEGS` name code commit, external-memory commit, and contract finalization. However, `FinalizationJournalState.legs` still requires exactly four entries while its order validator requires the three-entry tuple. Preserve this source inconsistency alongside the intended removal of the ledger leg; do not describe the finalization journal as an established usable three-leg contract.

Environment validation preserves the original Gate-1 producer artifact, exact manifest publication bound, later consuming-gate reconstruction-proof publication with a 4096-byte bound, and selected-producer requirements. The extracted `_validate_environment_artifacts` and `_compile_adapter_inputs` helpers do not themselves introduce a new profile authority or acceptance route.

Onboarding validation remains outside certification ownership. `worktrees/modules/onboarding.py::validate_memory_refresh_attestations` composes the sidecar and governing route body/history validators and aggregates their errors. Current curator control uses that helper on its legacy refresh path, while converted memory uses onboarding history traces. Prepared closeout likewise selects history-trace validation when available; its alternative branch calls the sidecar and route validators separately. Preserve the CCR-L42 intent that both applicable refresh surfaces be validated without claiming both current callers unconditionally invoke the shared helper.

## Historical And Verification Limits

This proposal read all 16,503 characters of the supplied card and records the earlier source adjudication at `8d2e754789e30f0d3be10fdd33f83cf6fe367141`; this source-only requalification uses `23cb164fa24dcbc4a98a56fa1324e1fb42c1bf41` plus the observed working tree. It establishes source predicates and ownership, not test results, executed gates, delivery, integration, acceptance, or performance. No tests or product entry points were executed.

The inherited named histories remain provenance for intent: CCR-L16 / CCR-R16@v3 durable telemetry; CCR-L13 / CCR-R13@v2 optional diagnostic E2E, associated with `4ba18bb23ba90e201bb37341d61c0efc64161fcf`; CCR-L17 / CCR-R17 measured replay, associated with `e84c004c37a4bad082e1a7f1bdc4bd062282a185`; and CCR-L14 / CCR-R14@v3 final real-Codex certification, associated with `54ff803a05209e06f732f2de1f90e2a71a069e08`. Those historical revisions and original execution witnesses were not examined in this present-checkout-only review. Their milestone or delivery claims are not renewed acceptance.

The inherited L30 evidence-retention discussion identifies an earlier limitation: ordinary failed runs raised before the record seam and did not establish a complete R11 population for every terminal outcome. Present source changes that ordering for outcomes with a published manifest, recording before nonzero refusal. Retain the earlier limitation as historical; the new call order still does not prove exhaustive publication for exceptions, absent manifests, unreadable decoders, or incomplete evidence. The original repair's execution witnesses were not examined.

The inherited R05 warning remains: typed finalization and leg-authorization functions, default application bindings, and visible admission/recovery callers do not independently prove a completed operation. The three-versus-four journal shape discrepancy is an additional present source limit, not a repaired invariant or runtime verdict.

The Integrated IAS Recovery Contract records helper extraction while retaining exact producer, reconstruction, ordering, and duplicate-refusal responsibilities. CCR-L42 records refresh validation parity intent, but present converted-memory and prepared-closeout branches differ from the inherited shared-helper composition claim. Neither historical label constitutes current successful validation evidence.

Namespace-isolation intent remains explicit for diagnostic and final-Codex stores. This review established the configured-forbidden-root predicate, not the completeness of every production policy or whole-call-path protection. No absence claim is inferred from a single local function.

The inherited statement that no external Domain Documentation source or cross-repository implementation is configured for this memory slice was not revalidated against settings in this bounded review. Repository-owned witnesses decide the present corrections. Existing reference identities, route/status/coverage metadata, and excluded tables remain under parent Curator preservation.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/certification` |

| Source File | Onboarding | Status |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | covered |
| `canonical.py` | [canonical.py.md](canonical.py.md) | covered |
| `digests.py` | [digests.py.md](digests.py.md) | covered |
| `limits.py` | [limits.py.md](limits.py.md) | covered |
| `models.py` | [models.py.md](models.py.md) | covered |
| `planning.py` | [planning.py.md](planning.py.md) | covered |
| `results.py` | [results.py.md](results.py.md) | covered |
| `validation.py` | [validation.py.md](validation.py.md) | covered |
| `certification_lane.py` | [certification_lane.py.md](certification_lane.py.md) | covered |
| `certificate_admission.py` | [certificate_admission.py.md](certificate_admission.py.md) | covered |
| `certificate_authority.py` | [certificate_authority.py.md](certificate_authority.py.md) | covered |
| `certificate_invalidation.py` | [certificate_invalidation.py.md](certificate_invalidation.py.md) | covered |
| `certificate_models.py` | [certificate_models.py.md](certificate_models.py.md) | covered |
| `certificate_store.py` | [certificate_store.py.md](certificate_store.py.md) | covered |
| `lifecycle_admission.py` | [lifecycle_admission.py.md](lifecycle_admission.py.md) | covered |
| `lifecycle_models.py` | [lifecycle_models.py.md](lifecycle_models.py.md) | covered |
| `lifecycle_recovery.py` | [lifecycle_recovery.py.md](lifecycle_recovery.py.md) | covered |
| `readiness.py` | [readiness.py.md](readiness.py.md) | covered |
| `readiness_models.py` | [readiness_models.py.md](readiness_models.py.md) | covered |
| `readiness_transitions.py` | [readiness_transitions.py.md](readiness_transitions.py.md) | covered |

## Evidence
- Retained reference account (no fresh execution or acceptance inferred): `certification` is a present rank-3 package between `models` and `controlplane`; its charter excludes concrete profiles, executors, lifecycle terminalization, and memory gates. [1]
- Retained reference account (no fresh execution or acceptance inferred): The adjacent control-plane charter remains the lowest stateful interaction service, so the lower generic contract does not absorb its record or policy ownership. [2]
- Retained reference account (no fresh execution or acceptance inferred): The strict checker derives direction from the declared order and refuses undeclared packages rather than using a baseline or fallback. [3]
- Retained reference account (no fresh execution or acceptance inferred): Preparation selection is limited to code and memory-content outputs. [4]
- Retained reference account (no fresh execution or acceptance inferred): The bridge compiles one aligned R11/R22/R21 lane and preserves admitted rail contracts. [5]
- Retained reference account (no fresh execution or acceptance inferred): The production seam resolves the exact profile, binds memory rails and persists admission. [6]
- Retained reference account (no fresh execution or acceptance inferred): The ordinary quality gate runs the admitted candidate through its certification executor. [7]
- Retained reference account (no fresh execution or acceptance inferred): The quality gate freezes certification records before execution. [8]
- Retained reference account (no fresh execution or acceptance inferred): Persist complete actual terminal catalogs, including red and interrupted gates. [9]
- Retained reference account (no fresh execution or acceptance inferred): Typed R05 finalization and leg authorization exist as library functions; existence is not caller proof. [10]

- Certification is a rank-3 generic contract below its lifecycle consumers; architecture is a declared direction, not an execution report. [11]
- Explicit not-applicable repository gates contribute bounded applicability authority; applicable rail contracts are preserved. [12]
- R11/R22 admission compares repository, candidate, selection, and applicable rail contracts, with separate not-applicable alignment. [13]
- Original authority and provenance are retained and digest-verified together. [14]
- Memory rails are obtained through a required port; default application composition derives them from the memory catalog. [15]
- A published terminal generation is processed before nonzero run refusal; supplied catalogs remain distinct from missing publication. [16]
- Complete supplied red/interrupted results retain publication; only eligible green results issue certificates. [17]
- Every nested evidence/artifact binding is checked against the accepted publication; selected certificate generations are protected. [18]
- Finalization declares three ordered legs but the journal field requires four entries. [19]
- Store overlap refusal uses caller-supplied forbidden roots, whose policy defaults are empty. [20]
- Curator legacy refresh uses the shared helper; converted memory uses traces, and prepared closeout's alternative branch calls the component validators. [21]
- Applicable Gate 3 requires exact Gate-2 artifacts; diagnostic altitude cannot issue a green certificate. [22]
- Replay denominator includes original and tail generations, excluding dated supplements. [23]
