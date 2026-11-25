# MCP Tests

`test_role_launch_acp_instruction.py` asserts that a configured ACP provider receives the caller's prompt, a blank line and the wait instruction, with the stored handover digest covering those bytes; its configured non-ACP-provider case asserts that the instruction is absent.

## Governing Overview
[overview](../overview.md)

## Purpose

Reference-anchor coverage is split among census classification and captured-input/artifact tests, shared-rule/readiness and pair-route tests, actual publication-owner tests, note-only revision tests and the separate baseline refusal/repaired-adoption case. Existing conversion, link, trace and report-only suites expect anchor debt beside their original findings. Fixture code readers supply the pinned bytes named by fixture anchors. Lane and lifecycle catalogs select and own this evidence; declarations establish no test execution.

`mcp/tests/` holds the package's Python behavioral tests, shared fixture and support modules, recordings and data, pytest composition, and two governed evidence catalogs. Its purpose is to preserve distinct user operations, consequential failures and regressions with the smallest maintainable protection. Module cards describe individual assertion sets; this overview explains composition, responsibility and authority across the route.

The integration lane selects the crossing dependent writer test once. It checks whether a dry plan resolves a branch name to the commit supplying the dependent confirmation.

The native stdio memory regression uses a generated converted leaf and repeats its fixed 28-call selection three times in one bound process. It checks the completed task, paged knowledge, quality and writer receipts before applying the Linux memory limits.

The canvas suite (MIK-R104, MIK-R105) protects the generated page's host and the presenter. `test_canvas_host` covers the served policy, the proof binding and the protocol boundary; `test_canvas_serving` the saved-first read, session document/asset isolation and revocation; `test_canvas_kit` and `test_canvas_kit_assets` the manifest inventory, byte verification and static self-containment (no browser runs in them; the browser smoke test is separate); the retained `test_canvas_presenter`, `_files`, `_host`, `_settings` and `_store` sources assert stored-attempt identity/activity, cancellation/publication races, symlink and held-parent IO confinement, host receipt/control fixtures, packet-tree source grants and attempt retention; `test_canvas_prospective` and `test_canvas_readiness` the load before publication and the static check; `test_canvas_capsule_text` the installed capability text against its canonical copy. These are source-declared assertions, not a fresh run. The governing route is [MCP package overview](../overview.md).

A test declaration, fixture, source citation, catalog membership or historical delivery statement is not evidence that a test ran on this candidate. Native-host and protocol cases qualify their exact tested surfaces; they imply neither a paid provider turn nor universal containment or semantic acceptance. Retained internal services and fixtures do not restore deleted public tools. The literal public roster currently registers 44 names in `PUBLIC_TOOLS`, including the architect's `explainer_control`, with `dispatch_agent` among the removed APIs; native `role_start_set`, `retire_child` and `direct_execution_grant` remain declared. This source census establishes neither execution nor restoration of the other removed APIs.

The shipped skill surface is the canonical corpus at `skills/` together with its single serving copy in `mcp/src/agents_remember/package_data/runtime/skills`; `test_role_message_wording.py` pins that count at two and `test_role_instruction_corpus.py` checks the canonical tree and the copy against `composition-manifest.json`. `scripts/sync-skills.py` takes its one copy target from `generated-copies.json`, so no harness mirror supplies a second test root. The shipped skill surface is the single `l-01-agent-lifecycles` skill; setup, repository preparation and baseline adoption live in the public docs, and worktree closeout is the lifecycle operation `operations/closeout.md`. The corpus checks follow the composition manifest rather than a directory listing. These are source-declared assertions, not a fresh run.

The initializer handover cases in `test_knowledge_bootstrap.py` assert state-first Architect/regular-task/Curator guidance for complete recorded/not-recorded trees and a nonlegacy unavailable-publication case. Partial-index repair, legacy conversion, preserved refusal fields and no-write checks retain their own boundaries. The converted bootstrap journey asserts the same Architect continuation after baseline adoption. These are source-described assertions, not a fresh execution or foundation-readiness verdict.

## Hot Path Summary

The instruction-renewal test family separates authored authority from generated current facts. `test_instruction_digest_renewal.py` checks relocation, explicit unit/evidence/clause bindings, held-hash-proven HEAD diagnostics, copied repository-map cases and reader-level uncovered-prose decisions. `test_instruction_manifest_renewal.py` checks pointer-derived steps/audiences, authored role reasons and no-step decisions, live-manifest reason policy, and command check/renew/check journeys on copied trees. `test_instruction_pointer_renewal.py` checks withdrawal, retained-policy refusals and working command remedies; existing wording-pin and budget consumers keep their separate shape, authored-decision and measurement checks. These are source-defined assertion responsibilities, not a new execution or acceptance record.

`test_fresh_repository_knowledge_path.py` uses `fresh_repository()` to initialize and baseline-adopt a repository, then opens its cardless baseline as a leaf whose onboarding directory is absent. `test_empty_leaf_memory_scope.py` uses `open_external_contract_fixture` for live-leaf scope and mode-owned roots; `test_empty_onboarding_readers.py` initializes memory and removes the empty onboarding directory for its reader cases, with a separate file-at-path refusal case. `test_cardless_knowledge_writer.py` plans and commits the first entries without a Markdown card while references still require one; `test_cardless_sidecar_validation.py` checks the validator's entries-only exception and keeps identity, link, anchor and history checks. Together their source assertions cover empty route/drift/baseline reads and first knowledge through a per-file sidecar without a Markdown card, full quality, writer, coherence and closeout preview. Their source assertions and catalog membership do not establish that a new execution or landing occurred.

The grouping regressions exercise writer-authored source maps for cardless deleted, mixed live/deleted and singleton groups, plus existing-trace precedence. The mixed case supplies the persisted group-map shape; it does not establish native emission of mixed groups. These source assertions preserve the unchanged gate's exact comparison and do not prove that a real leaf's grouped rows were accepted.

Native task/status protection now follows the single server producer. `test_task_entries.py` declares native-stage precedence over host activity, `in-turn`/permission precedence over idle/ended observations, contributor-owned event times, explicit unknown-versus-paused, missing-document/addressless entries, ordered membership with documented-subTask explicit-master precedence and genuinely absent-master fallback, preserved subTask unresolvable master literals, once-only full-content disagreement reporting, deterministic conflict/cycle handling, reachability and shared counts. `test_task_document.py` asserts that mirrored master status follows the native document even when step progress disagrees. Start/abandon source cases inspect both the leaf and mirrored parent stage; the series topology case prepares and publishes one master/sprint batch. These assertion bodies are not fresh execution or acceptance evidence.

`test_host_activity_projection.py` protects startup/new-boot reconciliation, unknown authority, notification-only intake and no extra activity reads during idle/full/degraded safety wakes. `test_host_supervisor.py` describes real child/pidfd fixtures with controlled identity inspection, double identity proof, one exit invalidation and unknown on subscription failure; it is not a run against a native host here. Role registration/revival tests combine the actual TypeScript publisher in a Node child with controlled native listings/events and a fake runtime, checking registration-before-resume, restart ordering, later archive reclamation and receipt-backed restoration. Those process boundaries do not prove a paid turn or installed-host adoption.

`test_changeset_cache.py`, `test_intent_summary_cache.py` and `test_task_document_body_cache.py` declare native-byte/conditional-return parity, consumed-input invalidation, unreadable/racing-input non-reuse and bounded retention. Selected cases address object loss/restoration, index-byte versus timestamp changes, ignored/input selection changes, grant changes, HTTP body revalidation and symlink confinement; the intent concurrency case blocks its reader while another change-set route completes. Warm-cache zero-Git/zero-reparse assertions describe their controlled scenarios, not measured fleet latency, CPU, whole-build performance or fresh runtime results. Raw workspace Event River rows retain task `scopeKey`, without `lifecycleId`/`sessionId`; they are diagnostic events, not task stage/activity.

A controlled case builds the serving runtime and uses two Projector subscriptions to check landing interest until the final subscriber leaves; separate controlled-refresher cases check disconnect during discovery, unchanged-answer age bands and rewrite/reopen/new/removal at two populations. Provider metrics activity regression instead calls the original periodic safety loop across empty/live/revoked/between-tick/restart/malformed authority, with launch refusal separate. These controlled in-process assertions establish neither native outbound/CPU totals nor real fleet or installation acceptance. Both modules retain ordinary catalog selection and existing support ownership; no task-local trace becomes a promoted fixture.

Task-order source assertions cover ordinary field writers, unknown/self/cycle refusals, parent Markdown refresh and dependency outputs from the corpus read_task_documents path. The current `test_dependency_keeps_its_full_relative_reference_and_own_document_stage` also calls the on-demand body reader for two addressed documents and compares `waitsForTasks`, `neededByTasks` and `bodyRevision` with corpus projection; it checks the nested dependency's full relative reference and its own Completed-derived graph frontier. These cases do not prove every possible body/corpus join. Native task creation tests the five-major/eight-child count, while model/readiness assertions retain child obligations. Finalizer cases distinguish preserved decision arrays, newly written completion time, unchanged legacy completion and retry/rollback bytes. Catalog membership and declared source assertions remain distinct from a run or independent acceptance.

L109 protection follows the naming owners: `test_read_ar_files` covers twenty string paths, no document text, removed-argument/schema refusal, stateless repeat calls, per-row confinement/card/index failures and own-section headings; `test_knowledge_name_projection` covers named rows/endpoint roles, declarations, provenance and continued walks. `test_context_packet_slim` distinguishes agent roots/actions from the retained full builder. `test_knowledge_diff_report` checks whole reports, atomic publication/refusal and admitted resource accounting. `test_tool_entry_point_read_only.ReadOnlyMarkTests` checks list completeness/disjointness, every advertised mark and changes to the read world (including Git metadata and non-index runtime controls). `test_tool_answer_table` and `fixtures/l109_tool_answers/PROVENANCE.md` retain the final four rows and honest fixture epochs. These are source-described tests and inherited fixtures, not tests run by this semantic review or fresh certification.

The conformance source declares ROSTER_SIZE = 44, TOOL_MODULE_COUNT = 14 and TOOL_HANDLER_COUNT = 46. Its structural tests compare registry and adapter populations in both directions, compare PUBLIC_TOOLS with the registered surface, reject duplicate roster entries and unadvertised registrations, and assert the roster count. These are source declarations and assertions, not a recorded test run or a measurement of the developer’s host. The current lifecycle catalog contains 18 contract and 120 artifact declarations; these are source declarations, not executions.

Landing cut/add observations are report-only; use the measurement owner and canonical Curator/Reviewer duties for independent memory judgment.

Start with the operation or failure being protected and its retained module, rather than an old case count. Ordinary pytest selects units with four workers; integration selects the small real-boundary population, and combined selection observes both. Candidate commands use the code worktree's own environment as its repository tool notes prescribe; a run record names its interpreter. Focused file/node runs and serial debugging are useful development work without becoming certification.

Collection first establishes isolated candidate imports and configuration, reads integration/stress file membership, and skips those files before import for the exact default `not integration` expression. Registered plugins then enforce bootstrap, lane membership and database-retirement boundaries. Lane resolution is explicit and may include class/node overrides; competing markers, unsupported provider classification, stale or missing membership and unusable catalogs refuse. Budgets count selected parametrized items, without recursively invoking pytest or collecting a second population.

The tool sweep derives its census from the advertised roster and uses one classifier for returned calls and controls. It attempts to validate the recorded whole result against the registered response model, checks delivered top-level keys against that result and framework keys, and distinguishes boundary-validation, unvalidatable, raised, bare-not-ok, refusal and payload outcomes. Each tool gets separate unvalidatable and boundary-validation subTests; raiser, bare-not-ok and census checks have separate population subTests. The sweep uses `tool_entry_point_sweep_support.py::_whole_result`, which returns the delivered payload when `log` is absent/non-string, the detail cannot be read or parsed, or its JSON is not an object. Failure to obtain detail therefore does not itself force `unvalidatable`; the substituted payload is model-validated. Preserve the intended independent whole-result check as inherited intent, not as an implemented no-fallback guarantee.

The ordinary entry-point world's socket-denial control calls `server_info` with the socket wake-up send refused and requires the ordinary classifier to return a payload. Test-owned loops use the shared bounded selector from the Python testing support route so queued callbacks can run despite the denied wake-up.

> The sweep compares observed error-arm and bare-not-ok populations with separately declared pins. `ENVELOPE_LOSING_RAISERS` and `UNMARKED_NOT_OK` are empty. No executable ambient lifecycle-state matrix or `STATE_DEPENDENT_RAISERS` pin remains in the two entry-point worlds or sweep module; `lifecycle_finalize_task` has an ordinary contract-addressed dry-run request. Exact equality checks distinguish a measured exception from an accidentally weakened population. `_attach_coherence_readiness` supplies code, error and nextAction when it reports coherence-required. This source correction is not a fresh sweep result.

For memory work, preparation may discover exact-pair quality findings, commit-owned findings, missing onboarding, stale indexes and source drift before expensive certification. That worklist is not Gate 5. Interactive catalog projection does not acquire affected-closure or code-prefix authority. Final publication remains with the existing prepared-output and lifecycle owners; the finalization helper validates a selected prefix of the original certificates and takes the envelope's memory tree from the current Gate 5 inputs (`certification/certificate_authority.py:158-186`), while an allowed retained prefix can include all five certificates whose recorded inputs differ from the current ones (`certification/certificate_authority.py:285-308,347-361`) — so the helper's validation does not establish equality with the current Gate 5 inputs, and no mounted publication equality follows from it.

## Construction And Ownership

### Current reviewer test boundary

The current reviewer test slice protects semantic present/absent/unresolved operands, the required judgment carrier and independent proof descriptions rather than the retired assessment/evidence envelope API. Retained SubjectAssessmentState model tests still protect their own count consistency; that model is not thereby a restored Reviewer channel. Read-latency cases protect fresh post-edit answers and no leaf memory-tree diff, and the memory-watch module separately asserts observation/notification behavior. Catalog consumer declarations select their actual support; they are not test runs or native-host/whole-MEMORY acceptance. The family/assessment vocabulary elsewhere in this overview remains explicitly scoped inherited intent, not the current Reviewer payload.


Grant/dashboard, direct-leaf role/integration refusal, direct landing and no-grant closeout parity cases exercise their named fixture scopes. Low-level synthetic grants and consumer/lane catalogs are preparation/declarations, not live architect, host or fresh acceptance evidence. Enclosed/master response-preservation uses the explicit source-bound scrubbed comparison, not raw byte equality.

Recorded-meaning regression uses compose_review over converted trees, exact owner/attempt selection, outline and continuation equality, portable L37 historical fixtures and retired/before-only UUID witnesses. Mounted ReviewSurface captures cover badges, step fields, keyboard explanations and missing-versus-empty state. Retained capture/provenance and real-ingest family display are distinct evidence classes; registration or mounted display alone claims no new invocation or installed acceptance.

### Recorded comparison and developer-send witnesses

Recorded-comparison tests distinguish a requested record from the latest answer and an unrecorded number, including separate retained catalogues after cleanup. The delivered-comparison module adds the landed case: a leaf whose worktree is gone and whose last record predates its delivery opens the four exact sides its enclosure records, keeps that earlier record at its own number, refuses a side Git cannot establish and records nothing for a numbered history read. Route-admission cases refuse a negative comparison before calling the port and forward a positive number unchanged. Revision-selection cases check display versions and recorded writer/origin attribution, keeping no recorded writer distinct from an incomplete index. Focused card cases derive each entry’s four memory values from the bound after-side index, retain optional symbol names, omit those values from the lane answer and refuse cache retention after failed memory reads.

`test_developer_messages.py` protects the developer’s tray send through registered HTTP routes, composition, files, the held queue and recipient/log owners with a fake native host. Its cases cover ordered native text/image delivery and SHA-addressed files, exact tree/revision references and pre-filing contradiction/provenance/bound refusals, rollback of newly saved picks, and each message’s own held, terminal or partial-drain outcome. Recipient lists distinguish complete, damaged, truncated and unavailable censuses; sent logs retain bounded recent entries and recipients, and the cross-site guard precedes the tray route. The bridge cases separately check attachment options and malformed-payload refusal, while the native-listing fixture carries completeness into the recipient list.

The dashboard-host case feeds the request head for 500 invariants to the actual h11 parser over two reads and checks foreground/daemon-child and reload limit configuration. Source-endpoint cases check `All changes` wording and truthful no-knowledge inventory, without treating returned text as browser layout evidence. These are source-declared controlled cases; no test execution, installed chat consumption or live-host acceptance is asserted.

### Tool regression witnesses on current input surfaces

Overflow-sensitive archive, activation and install witnesses retain the delivered outcome but
read displaced facts from the exact full log or newly filed report. Long scalar pointers may be
omitted by the guard; report association is checked rather than inferred from an earlier call.
Direct dry-run install flags remain application/component evidence, not a retained public-host
object. Retired capsule/catalog tools stay absent from the SDK roster; resource/extension reads
and role-start compilation retain their distinct boundaries. Startup installs the workspace river writer; start and attach publish the addressed native task facts and derive guidance from the enclosure contract.
Paired lineage fixtures create the memory repository
and both branch edges (`test_worktree_support.py:149-232`), and the socket-bearing support builds on a temporary directory
of its own (`pnt_sandbox_test_support.py:231-255`), which is also where the capsule-launch world builds under pytest's `tmp_path` (`test_capsule_launch_wiring.py:122-126`). This prose does not establish an endpoint-guard identity: the port claim's abstract socket name carries no filesystem path, and no guarded path limit is named here. These are source contracts, not a fresh execution verdict.

The river event cases and the envelope-stripping choke case use `server_info`. The self-contained sweep seeds its code and memory roots, obtains the guarded user-settings path and carries explicit grant/direct-leaf input; overflow-sensitive tests assert displaced facts in the logged whole result. Packaging witnesses author fixture/XDG dimensions before production and compare emitted objects unchanged; log-path witnesses separate preservation within the length domain from exact length/digest shortening. These are assertion contracts, not a fresh whole-lane result or installed-host acceptance.

### Final test-only repair input

Both reopened-history changed-row refusal cases supply the gate’s worklist to the writer. `AnswerAndTextTests` invokes `scripts/renew-instructions.py --check` with `sys.executable`; paired-retirement setup creates and verifies its empty repository lock before the refusal snapshot; and the competing question writer observes lease exclusion before waiting on the native lock, using the shared hang guard.

### Pytest composition and evidence catalogs

`test_paseo_reopened_workspace.py` uses the existing bridge-agent process fixture and key-addressed fake host to protect deterministic archive successors, hidden completed replay, retry convergence, bounded exhaustion and placement refusal. Existing bridge-agent cases retain live/folder-only behavior. Unit-regression and derived artifact-consumer declarations select the module but establish neither a native host journey nor a provider's completed turn.

`conftest.py` puts candidate `mcp/src` and `mcp/test_support` first on the import path, declares the actual test process through the hermetic bootstrap, creates disposable HOME/XDG/Codex/tmux locations, isolates Git configuration, and removes specified inherited credentials and live-service opt-ins. Each case receives its own user-settings configuration directory. Ordinary integration cases automatically request bound worktree services unless certification is selected; units request that fixture explicitly. Teardown resets services and releases the owned environment. This is a bounded isolation design, not a promise about every possible environment variable or external effect.

Three plugins are registered: pytest bootstrap, evidence lanes and database retirement. The latter is intended to catch production database access/file mutation outside its named allowed modules. `--certify` takes a separate genuine-Dagger admission path; ordinary test bootstrap supplies no lifecycle-worker or Dagger capability. The source policy distinguishes ordinary development feedback from immutable candidate-bound evidence issued by the pinned delivery graph and existing lifecycle owners.

The root `pyproject.toml` owns test paths, default selection, four-worker file distribution, strict markers/configuration and collected-case budgets. The current candidate declares 10,000 unit and 2,000 integration cases (`pyproject.toml:334-335`). The current Python test-policy design note agrees on 10,000/2,000. This is source agreement, not fresh collection or execution. File distribution and collection refusal behavior remain their existing owners’ contracts.

`test-evidence-lanes.toml` assigns the explicit base lane of every durable test module. The lane loader derives the repository test population and refuses missing/stale members, invalid categories, noncanonical lists and invalid overrides. Collection requires a Git checkout through that dependency discovery. Membership classifies selection, cost and fidelity; it is not execution or acceptance. Derive populations from the manifest instead of pinning counts in this overview.

`evidence-lifecycle.toml` governs artifacts and contracts: support, fixtures, recordings/generators, authority, fidelity, cadence, lifetime, replacement and supported consumers. Exact and exact-source consumers are compared with source-derived reachability. Governed discovery includes non-test Python under this route, recognized data suffixes, task-shaped proof files, sufficiently large non-source fixtures, the lane manifest and direct Python children of permanent `scripts/e2e_harness` support. The retained production-chain completion proof is not established as current coverage: no module or test in the pinned tree owns that name, and the former case asserting that it owns no governed artifact or contract is absent from the pinned module; the claim is retained as historical material, not as a current proof identity.

Registration intent is one lane entry for a new test module plus canonical consumer derivation by `python -m agents_remember_test_support.testing.evidence_lifecycle --project-root . --write`; new governed artifacts need their own deliberately authored rows. The writer sorts/canonicalizes and repairs supported consumer lists; it does not invent a lane for a new file or decide that an artifact is retired. Deletion removes gone lane paths and repairable consumer paths, but never silently deletes an artifact row or its last gone consumer. An artifact with no surviving/derived consumer requires an explicit retirement decision. Both catalogs use Git union merging; duplicate paths, disorder, resurrected deleted members, duplicate/interleaved rows and parse failures still require canonical repair or explicit restoration/manual repair. Union is not a validity guarantee.

### Shared support, settings and candidate observations

`_user_settings_guard.py` is the shared write-path owner. It derives the product candidate path and compares lexical/resolved identity with the account database's home-based real settings path. A match refuses before returning a path, with a temporary `XDG_CONFIG_HOME` remedy. When the database is unavailable, comparison uses the guard's earliest observed/import-time home; it cannot prove a process-start home mutated before import. The guard creates nothing itself. The world and Paseo helpers call it before settings-parent creation or mutation, including Paseo removal; no current structural-seat settings helper calls it. `EntryPointWorld` can already have constructed disposable fixture repositories before that refusal; the guarantee protects settings, not all world effects.

`test_user_settings_guard.py` describes fake-account refusal/allowed moved configuration, earliest-observation honesty and a child process identifying the reviewed world source. Its `MIK-R135@v1` rule4 scanner recursively selects future nested non-test support under both roots and checks supported raw/aliased resolver calls and literal-path reconstruction. Unsafe controls are source text, not executed scripts. This is bounded syntactic checking, not arbitrary Python dataflow analysis or a second suite execution.

`test_worktree_own_environment.py` protects the Worker candidate-environment action in `roles/worker.md` on the canonical tree and each declared generated copy (two surfaces: `skills/` and the package copy), pinning four clauses once each, plus canonical role/operation/template wording, an independently detectable retired interpreter line, and ignored-environment accounting. Its accounting case builds its own temporary repository, creates its `mcp/.venv` with `venv.EnvBuilder` and populates `dashboard/node_modules` unconditionally before enumerating changes. It does not execute live sync, landing, closeout or cleanup. Its source references the actual change enumerator and forbids environment paths in that result.

The uv-minimum regression module separately checks decimal ordering, equal/newer admission,
missing/older/unreadable refusals, reported identity and rollback after failed sync. Its PATH
shims are gate witnesses, not real successful-build proof. The rollback case requires an
existing environment and checker-valid runtime, and can skip when the latter is unavailable.
Candidate tests use scratch XDG homes; registration is still not execution evidence.

Shared waits provide hang guards and condition-specific failures, not performance ceilings. Negative assertions require the excluded operation's actual opportunity: held locks, blocked dispatch, projector publication, resolve entry or completed durable-record reads. Owner-local injected clocks are preferred for deadline behavior; deliberate expiry tests assert semantic outcomes. It scans Python timing syntax in tests/test support except `waits.py`, and checks production process-state syntax against its closed register. Synthetic-catalog controller cases invoke pytest only on disposable small repositories with hard limits; they do not recursively run this repository's suite.

### Responsibility map and enduring semantic intent

Bounded-knowledge regression distinguishes the public payload outcome from explicitly marked domain-unit detail when the mounted answer cannot keep the whole result. The public fitting/overflow contracts remain checked; raw domain bodies are not pointer retrieval. Series fixtures carry both code and external-memory landing legs, and observation fixtures park held delivery among their five siblings. Exact provider-name admissions and sandbox resolver-key checks protect the current mechanisms rather than licensing wider exceptions.

Knowledge and onboarding tests own text formats, curator writing, validation, histories, planned effects, trace gates, unexplained-change disposition, reconsideration, closeout worklists and derived read/index behavior. A schema failure names its file and makes the tested index result partial; failed or unrun anchor lookups are unavailable rather than observed absence. Historical index/database parity records grant no authority to the retired database substrate.

The existing reconsideration suite now protects candidate-side supersession: a successor suppresses
its base item and appears in the skipped-link summary; the same changed target without a successor
still raises; an unrelated supersedes target preserves the base item and raises no new candidate
item. The successor case separately checks explicit-set versus default stored-predicate behavior.
These are source-described assertions, not a new execution or acceptance. The current reconsideration module has 1,190 lines and imports configuration support from reconsideration_test_support.py; this is a source account, not a test run. Current catalogs, lane ownership and certification remain separate authorities.

Recorded-scope read modules separate selection/grouping/budget from real Git, snapshot, namespace, schema, continuation and path boundaries, sharing `read_scope_test_support.py`. Inherited scope intent stops at directly selected/containing family relationships: advertising an unreached family does not include its further realizations. Claim identities and source locations are counted separately; repeated membership does not invent extra identities. Pages retain one selection/snapshot/manifest and truthful remaining-item information, refusing a bound that cannot hold the next item. Paths are addresses: Git pathspec-magic spellings are refused, while literal glob characters remain authorable/resolvable. Requested-tree absence, blob mismatch, unsupported locator, non-blob entry and unavailable tree remain distinct observations; none promotes an old claim into current truth. Continuations bind the same candidate/snapshot/manifest and refuse substitution or mutation.

Retained family/context/comparison accounts require whole-walk coverage through actual bounded continuations, unique membership rather than repeated sparse projections, and unchanged primary knowledge/evidence/comparison identity/source inventory. Revision selection uses retained heads, sorted identities and explicitly named empty/absent sides rather than guessed chain/fork ancestry. New-member context preserves independent counterparts. Withdrawal is named and unresolved anchors retain their reason. Direct relationship-reach cases label inferred relationships and reject fabricated pairings; the text movement fixture itself asserts no inference. Assessments are append-only corrections rather than edits; a decision is not an export, forged legacy identity is not export authority, and unsupported admission claims refuse. Signals/rendering/read surfaces do not smuggle verdict vocabulary or stored judgments into non-authoring observations.

Reviewer tests divide supplied-tree/observed-task-read capture and failure-sensitive bounded worklist memo reuse from isolated worklist child transport, recorded-read invalidation and shared candidate capture. `test_review_read_latency.py` protects no leaf memory-tree diff and fresh post-edit answers. The current leaf-wide owner is `review_tree_knowledge._compute_leaf_parts`, which computes the worklist; detailed comparison changes open through `ReviewChangeOverlay` and `ChangeSetViewer`. Removed `SourceExplorer` and `LaneFileFocus` are not live owners. The inherited boundary is one leaf-wide computation per comparison, no self-capture, exact child/in-process document/read/body parity, one child shared by identical requests, computation-count bounds, explicit non-retained transport refusals, child/Git lifetime confinement, independent Git configuration, thread-owned tree reads and idempotent pins. Kept results depend only on consumed task documents and other recorded inputs; packet retargeting can reopen a warm gate. Candidate capture observes stable HEAD with a private add-all index, preserving the real index and distinguishing copied timestamps, trust flags, derived exclusions and conversion rules.

> Task tests own canonical document schemas, graph projection, master links, endpoint-correct comparison generations, handover/retirement wording and developer-question routing. Inherited intent keeps completed leaves reachable across an unknown optional writer field while refusing missing required fields; starting a leaf repairs derived lifecycle/master bindings without rewriting substantive authored content, refuses a missing master without writing, and leaves planning unstamped. Parentable roles preserve parent-channel question/recovery/answer provenance, peer ownerRelation routes, relay and permission-notice duties. Role/capsule cases separate admission from mere strings, keep provenance in admitted source bytes and leave the read tree unchanged. Launch cases check the prompt actually sent, model/effort/tier options, one compiled shared block and omission of an undeclared shared source.

> Delivery tests distinguish actual code/memory objects, refs, source ancestry and ownership from derived cache bytes. Transaction-only closeout/integration and recovery retain attributed memory-content commits through `Code-Commit:`; missing, malformed, forged or changed ledger cache does not itself create commits or authorize/block delivery. Producer census intent is total attribution through one renderer, preserving hostile caller body bytes and a final separate trailer block; recovery's owed memory-content commit belongs to the same external-closeout producer rather than a new recovery producer. Backfill owns deliberate disposable history rewriting, loss reporting, trailer-only acceptance, byte-faithful objects, idempotence and multi-ref publication.

Current attribution cases in `test_memory_attribution_producers.py` compare body-only and genuine final-block messages with Git for their declared shapes. `test_weakness_closure.py` exercises the registered weakness writer and both weakness/record reads across pending, attributed and unavailable closure states, explicit commits and historical closure episodes. Its direct history fixtures remain distinct from the registered authoring checks. `test_weakness_closure_closeout.py` uses the application closeout route and public read payload to assert that the judged tree becomes the committed memory tree and that attribution is returned without rewriting the reviewed weakness record. These are source-described assertions, not a fresh execution or a settlement of a live weakness.

> Protected landing still checks current source heads, fast-forward ancestry, exact admitted outputs and clean owned checkouts. The production `integration_ref_transaction.py` owns protected-ref transaction and recovery paths. Sync/source-lineage accounts separate settleable auto-carry, read-only preview refusal, escalation of unprovable breaks, parked dirty-candidate restoration on completion/resume/cancel and preserved unmerged-index refusal. Checkpoint landing is an explicitly requested unfinished-master publication, with plan/apply parity and stale/conflicting-ref refusal; checkpointed work stays continuing, is not upgraded into reclaimable final integration, and closeout accepts its own recorded source head while refusing foreign movement.

> Pause is a separate stop-only operation: release only this contract's activation, publish nothing, preserve siblings and task work, and hand the turn back without manufacturing a next call. Never-selected/already-vacant success differs from leaf, unreadable, unowned, foreign-vacant and intervening-record refusals. Activation is per contract, not a shared source-pair mutex; sibling masters keep private work and can progress concurrently, while real sprint graph predecessor edges still gate. The pause structural test explicitly covers static AST import reachability, including function-local imports and excluding TYPE_CHECKING, but does not follow dynamic imports; it is not a whole-process call-graph proof. Terminal finalize/cleanup must name the stopped component and nonempty reason, distinguish already-gone provider runtime from permission failure, and retain retry truth. Abandoned rows require no landing; a landed abandoned row refuses. Master retirement and finalization retain distinct outcomes: a sprint master finalizes without archive, an uncommanded master finalizes through retire-only without archive, and an unbound standalone leaf refuses task-document-resolution-blocked while preserving its snapshot. Partial-hook retries and archive receipts remain separate controls.

Blocker-reason tests own the surviving terminal protection: a cleanup blocker always names its component and a non-empty reason, and a torn-down provider does not invent one. The retired stores include `terminal-sessions.json`; the workspace projection carries no terminal catalog, and the pinned source defines neither `paneDiagnostic` nor `CatalogTurnEvidence`. Native projectors and adapter evidence own turn/outcome/identity/interruption truth, and bounded protocol correlation/paging remains distinct from live-host qualification.

Serving owns startup and recurring observation independently of browser requests or notifier enablement. Startup compacts the workspace river, schedules projection priming and recurring loops, then yields. The fixture replaces `projector.prime` with an async mock, so real prime internals are not exercised; the parked invocation is the recurring archive-recovery owner's own first pass, identified by coroutine identity — the parked task's coroutine qualname is `_leaf_archive_recovery_loop` (`test_serving_shutdown_drain.py:252-257`). Archive-recovery attempts sleep after completion and preserve the recovery scan bounds; exceptions are logged while cancellation remains visible. No observer-health row is published: `terminal-observer-health.json` is a retired store whose writers are gone, and the recurring archive-recovery loop only ticks, logs its failure and sleeps. The served tail carries `watcherHealth(running, downSince)` beside `servingBuild`; adding it at serve time does not change the core projection ETag.

Logical-clock evidence is not wall-clock performance acceptance.

Parent wake uses the paseo plugin’s in-memory turn tracker. `turn_events.ts` creates one tracker per registration and forwards `agent.turn.after` with host turn identity and outcome; `turn_ended.ts` only treats completed eligible turns as silent. Its reach is wider than the parent line: a completed leaf-seat turn — Worker, Reviewer or Curator — judged silent is sent a message of its own after one 60-second wait checked against host state at the send, at most twice in a row, and every silent end from the third on sends the seat nothing and gives its parent the line marked with the count ; a turn of the seat beginning inside the wait cancels it without counting. A failed send keeps its line only inside the same tracker, so retry and overlapping-flush cases deliver each line once; a fresh tracker holds nothing, and the pinned source contains no row → marker → attempt recovery, no durable per-seat pending row and no reviewer/curator projector wiring. The wake path neither closes task documents, supplies a review verdict nor validates curator coherence/readiness. Current turn-end handling recognizes declared helper and background waits.

Native launch fixtures check metadata without feature fan-out and one selected-model lookup per selected request. Status tests check that a held launch lock suppresses host reads and a parked receipt observation permits Start. Native Antigravity launch and Retry cases distinguish a missing agent, a reconciled exact agent, and a replayed ACP payload. Native launch and host tests retain exact launch/replay/provenance, runtime/settings/bridge/catalog admission, independent model/effort/tier validation, previous-host removal, bounded sandbox process ownership, one request authority and idempotence; the current unknown-outcome/replay and withdrawal assertions belong to role launch in `test_paseo_launch_outcomes.py` and `test_paseo_launch_repeat.py` and to held messaging in `test_held_queue.py`, not to this route. Conversation projection declares only handshake, list, read and resolve-resume-target and preserves ordered read windows with truthful ordinal pagination; it carries no one-use-attachment or submission-retention state. Independent SDK-client/SEP protocol, Python/TypeScript, real Node and capsule-harness accounts each retain their stated fixture/process boundary; none extends itself to paid turns or final memory certification.

Landing regression suites distinguish exact-pair refusal, authentic history ownership, record retention, merge-chain admission, explicit direct owner and honest post-publication aftermath. Coherence closed-out is an integration case; dependency bounds/old-record compatibility are model/publication witnesses. Read-boundary and synthetic cutover fixtures that hold another gate passing prove only their declared surface, never that gate's acceptance.


### Call-scoped parsing, build identity and measured coherence

`test_definition_scope.py` covers scope reuse, fresh operations and source-content identity. `test_definition_scope_boundaries.py` covers MCP, finite CLI and background operation boundaries. `test_knowledge_index_build_identity.py` covers loaded-build cache isolation, private unknown-build reads, reuse after restart, cold lookup contention, shared failure and retry, and pruning of abandoned build files. `test_curator_coherence_measured_quality.py` covers unchanged quality after publication, measured-binding invalidation and historical record readability. These are source-described assertions and establish no new execution result.

### Landing-report regression scope

`test_landing_report.py` declares controls for measured cuts and the below-measure boundary, proven-deleted sources versus unproven absence, route overviews and full card removals, code-named renames versus duplicate-blob copies, admitted leaf-base comparison after commits and base updates, extra-knowledge file sizes, symlinks without target traversal, Git administrative exclusions, unreadable-base notes, bounded answer rows and linear line-multiset work. The report and checklist cases in `test_landing_report.py` and the operation, gate and adapter cases in `test_landing_report_closeout.py` distinguish descriptive rows from existing refusals; the closeout-phase fixture mocks adjacent services, so it is not whole-landing acceptance.

The Curator role-text case retains source/compiled facet checks, including its scoped equivalent. The Reviewer case compiles the Reviewer review capsule for each discovered source root, requires that `reference/review-memory-changes.md` is not a delivered detail, and checks each landing sentence in the delivered `roles/reviewer.md` section "Inspect and verify the candidate" and in the emitted launch instructions, each with a removal mutant. It is not a live every-harness consumption witness. The module is selected once in `unit-regression`. The lifecycle catalog declares it as an exact consumer of four artifacts: `_user_settings_guard.py`, `curator_coherence_test_support.py`, `fixtures/repository_profiles/node/package-lock.json` and `landing_report_test_support.py`. This is declarative membership, not evidence of runtime fixture consumption. Registration and these source-described assertions establish neither a new invocation nor a PASS.


### Native selection and source-owner qualifications

Message transport source coverage is split across settings-limit validation, filesystem/collision/rollback, body and attachment behavior, bounded replies, archived-successor/start-authority checks and source/compiled-return wording. The private turn-end decision cases are in `mcp/src/agents_remember/package_data/paseo_plugin/server/turn_ended.test.ts`, outside this Python tests route, and use a controlled sender without a host. Catalog membership and controlled-runtime assertions do not establish live host callbacks, every-harness consumption or independent acceptance. Actual-parent-ID developer questions stay distinct from role/task ordinary returns.

[`test_user_settings_guard.py`](test_user_settings_guard.py.md) contains refusal assertions on made-up accounts, including a real child that identifies the reviewed world source. Its bounded recursive static scan includes future nested non-test support modules, rejects raw/import-aliased resolver calls and supported literal-path rebuilds, and never executes its deliberately unsafe controls. This is a bounded support-settings scanner, not arbitrary Python dataflow analysis or another suite execution. Its `unit-regression` registration declares selection, not execution or independent acceptance.


This account describes source assertions; it supplies no execution or acceptance result. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Historical citation custody is distinct from active support: current operative claims, including the renewal below, require claim-matched current source extents; preserved keys or historical tuples alone do not establish currentness or proof truth.

The reconsideration suite contains candidate-side supersession assertions: a successor suppresses its base item and appears in the skipped-link summary; the same changed target without a successor still raises; an unrelated supersedes target preserves the base item and raises no new candidate item. The successor case separately checks explicit-set versus default stored-predicate behavior. These are source-described assertions, not a new execution or acceptance. The current file has 1,190 lines. The file-size measurement is neither a test result nor a policy waiver. Lane ownership and certification policy are separate from these assertions.

Recorded-meaning regression uses `compose_review` over converted trees, exact owner/attempt selection, outline and continuation assertions, portable L37 historical fixtures and retired/before-only UUID witnesses. Mounted `ReviewSurface` source cases over retained captures assert badges, step fields, keyboard explanations and missing-versus-empty state. Capture/provenance bytes and the F04 real-ingest attribution are retained evidence classes, not reconstructed invocations; registration or mounted display alone claims no new execution or installed acceptance.

`paseo_launch_test_support` owns the shared hand-written stateful runtime/catalog and fixture-derived dispatch expectations. Launch and status test classes inherit that support; the document-chat read/tree classes inherit it through `StatusTestCase`, while the first-start preparation class has its separate `RoleToolsTestCase` base. Document-chat source cases assert one-census tree discovery, unknown versus empty, corruption isolation, repeated receipt-path reads and byte budgets. `test_paseo_status_bridge` composes the production Node listing script with a controlled daemon client; `test_paseo_frame` asserts settings-bound provision-command disclosure. Catalog ownership and source assertions are not live-host or executed acceptance proof.

Paseo startup tests check the exact create payload and the grant recorded in the receipt for the seat's own task server. The role-launch fixture covers the full create input for Architect, Orchestrator, Manager and Worker. The catalog fixture checks all seven role choices on Claude, Codex and Pi. Its payload and grants name only the seat's own task server even with a second server in the fixture's configuration. Mounted-server fixtures compare the ordinary and bound explainer advertisements with their respective Codex startup rosters. The explainer host fixture checks the full Codex roster with the four additions and preserves Claude's identity tool with those same additions.

The enforced collected-case pair is 10,000 unit and 2,000 integration cases.

## Invariants And Boundaries

A new case must justify distinct protection; consolidate or replace overlapping tests and remove unused support before growing budgets. Private branch coverage and metric improvement are not sufficient reasons to add tests. General policy forbids recursive repository pytest and repeated repository census to test the suite. The specifically named bounded scanner and disposable synthetic-controller exceptions retain their own scope.

Coverage and changed-line coverage are diagnostic. Production-only CRAP 20 is a review trigger, excluding tests/support, not a delivery blocker. No coverage ratchet, mandatory percentage, changed-line floor or score-exception registry is implied. Lint, formatting, typing, structural rules and test failures enforce; diagnostic-tool failures remain visible separately from metric findings. A successful report tool invocation is not metric acceptance.

Preserve genuine admission, process identity, disposable state, credential isolation, exact code/memory candidate binding and publication ownership. A host pytest pass, copied report, green helper or merely using Dagger cannot issue final authority. Certification runs only when explicitly requested; closeout and landing run the knowledge gate and commit check, and no tests. External-memory candidate identity binds the configured repositories, roots, branches, bases, onboarding root and contract digest; the ledger path is excluded from candidate-tree content. Validation checks the current candidate pair. The interactive final catalog reports finalizationEligible=false and fullFinalRequired=true. Retry proof supports exact reuse and dependency-complete delta reuse.

Keep fixtures honest about fake inspectors, synthetic profiles, hand-built payloads, pending finalizers, controlled adapters and process doubles. Preserve useful support only for actual consumers. Source assertions demonstrate declared protection; execution receipts alone demonstrate a run.

## Historical And Verification Limits


Read the lane manifest for the selected test modules. The current configuration declares 10,000 unit and 2,000 integration selected cases. The testing design document agrees with the current configuration on 10,000 unit and 2,000 integration selected cases.

The canonical catalog writer drops gone consumers but never removes an artifact row; its owner decides whether the artifact is retired and the row should be removed.


Read-latency and Git-tree review modules share fixture definitions from `agents_remember_test_support.testing.review_git_trees`.

No absence of a guard across an entire call path is inferred from a local helper.

## Retained Route And Coverage Metadata

The route metadata supports navigation and source custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.


| Field | Value |
| --- | --- |
| sourceRoute | `mcp/tests/` |

### Native-source claim qualifications

- The guard refuses a matched account or earliest-observed settings path before returning a write path; it creates nothing.


- The made-up-account child asserts its reviewed source and empty fake home on refusal. Recursive population, syntactic scanner and deliberately unexecuted unsafe controls are source-described assertions.


- Candidate successor, changed-target/no-successor and unrelated-supersedes controls protect the boundary. The current configured collected-case budgets are 10,000 unit/2,000 integration. Neither source assertion nor policy declaration is execution evidence.


- Recorded-meaning backend source assertions, mounted ReviewSurface capture-based assertions and retained capture/provenance records are distinct source/evidence classes; no new invocation or installed acceptance is inferred.


- The lifecycle catalog currently lists test_landing_report.py as an exact consumer of the existing curator-coherence support and Node lockfile artifacts; no new artifact/contract identity or execution is inferred.




- The outline uses RecordChanges for intent, guarantee and membership facts.


- The change-kind projection delegates intent and membership to the same RecordChanges owner used by the outline.


- The Node fixture lockfile artifact currently declares `mcp/tests/test_review_change_kinds.py`, `mcp/tests/test_review_closeout_result_block_through_real_tool.py`, `mcp/tests/test_review_comparison_reclamation_real.py` as exact consumers; these are lifecycle consumer entries, not lane rows or execution evidence.


- The worktree-closeout source case asserts invalid-card refusal, unchanged open history bytes and commitment of closed history with the same rows on a valid retry.


- The Node fixture lockfile artifact currently declares `mcp/tests/test_knowledge_closeout_gate.py`, `mcp/tests/test_knowledge_conversion.py`, `mcp/tests/test_knowledge_conversion_toolchain.py` as exact consumers; these are lifecycle consumer entries, not lane rows or execution evidence.


- The Node fixture lockfile artifact currently declares `mcp/tests/test_review_unexplained_lane.py`, `mcp/tests/test_reviewer_worklist_process.py` as exact consumers; these are lifecycle consumer entries, not lane rows or execution evidence.


- The Node fixture lockfile artifact currently declares `mcp/tests/test_reconsideration_surfacing.py`, `mcp/tests/test_record_integrity.py`, `mcp/tests/test_record_landing.py` as exact consumers; these are lifecycle consumer entries, not lane rows or execution evidence.


- The Node fixture lockfile artifact currently declares `mcp/tests/test_knowledge_reader.py`, `mcp/tests/test_knowledge_reader_tree_coverage.py`, `mcp/tests/test_knowledge_reopen.py` as exact consumers; these are lifecycle consumer entries, not lane rows or execution evidence.


- The lane manifest declares `mcp/tests/test_knowledge_decisions.py` in `unit-regression`; selection is not execution or acceptance.


- The Node fixture lockfile artifact currently declares `mcp/tests/test_family_route_conditions.py` and `mcp/tests/test_file_size_detector.py` as exact consumers; the retired final-catalog-plan test is absent. These are lifecycle consumer entries, not lane rows or execution evidence.

Current declaration checked at `mcp/tests/evidence-lifecycle.toml:2457-2458`, with the two consumers at lines 2693 and 2695; the retired test is absent from the parsed Node fixture consumer list.

- The lane manifest declares `mcp/tests/test_planned_knowledge_effects.py` in `unit-regression`; selection is not execution or acceptance.


- The Node fixture lockfile artifact currently declares `mcp/tests/test_planned_knowledge_effects.py` as an exact consumer; this is a cumulative consumer declaration, not execution evidence.


- The lane manifest declares `mcp/tests/test_onboarding_trace_gate.py` in `unit-regression`; selection is not execution or acceptance.


- The Node fixture lockfile artifact currently declares `mcp/tests/test_knowledge_currentness.py`, `mcp/tests/test_knowledge_cutover.py`, `mcp/tests/test_knowledge_database_retired.py` as exact consumers; these are lifecycle consumer entries, not lane rows or execution evidence.


- The Node fixture lockfile artifact currently declares `mcp/tests/test_knowledge_worklist.py`, `mcp/tests/test_knowledge_worklist_leaf.py`, `mcp/tests/test_knowledge_writer.py` as exact consumers; these are lifecycle consumer entries, not lane rows or execution evidence.


- The Node fixture lockfile artifact currently declares `mcp/tests/test_knowledge_file_canonical.py`, `mcp/tests/test_knowledge_file_formats.py`, `mcp/tests/test_knowledge_gate_routes.py` as exact consumers; these are lifecycle consumer entries, not lane rows or execution evidence.


- The Node fixture lockfile artifact currently declares `mcp/tests/test_read_anchor_memo.py`, `mcp/tests/test_read_ar_files.py`, `mcp/tests/test_reader_task_context_protocol.py` as exact consumers; these are lifecycle consumer entries, not lane rows or execution evidence.


- The lane manifest declares `mcp/tests/test_knowledge_review_revision_selection.py` in `unit-regression`; selection is not execution or acceptance.


- The three fresh-user harness artifacts declare test_fresh_user_harness.py as an exact-source consumer; source cases assert over-cap/branch fixture shape and blocked-step/report-argument contracts without proving fresh-user acceptance.


- The lane manifest declares `mcp/tests/test_fresh_user_harness.py` in `unit-regression`; the retired citation-index-resilience test is absent. Membership is selection only.

Current declaration checked at `mcp/tests/test-evidence-lanes.toml:4-5` and `mcp/tests/test-evidence-lanes.toml:187`; the retired test is absent from the parsed lane.

- The lifecycle catalog declares `scripts/e2e_harness/fresh_user_fixture.py`, `scripts/e2e_harness/fresh_user_scenario.py` and `scripts/e2e_harness/run_fresh_user.py` as permanent `shared-support` artifacts with exact-source consumer lists and their respective `node:` replacement contracts; registration alone is not acceptance.


- The lane manifest declares `mcp/tests/test_memory_backfill.py` in `unit-regression`; selection is not execution or acceptance.


- The lane manifest declares `mcp/tests/test_memory_attribution_producers.py` in `unit-regression`; selection is not execution or acceptance.


- The current Node fixture lockfile lifecycle artifact names its exact retained consumers; old terminal-liveness/observer modules are not current consumers. This is a metadata declaration, not a lane or execution result.


- The lifecycle catalog registers `mcp/tests/read_scope_test_support.py` with `contract:knowledge-read-scope-cases` and an exact consumer list; the contract separately names its owner and evidence node. This is declaration, not a read invocation.


- The lane manifest declares `mcp/tests/test_knowledge_read_scope.py` in `unit-regression`; selection is not execution or acceptance.


- The lifecycle catalog registers `mcp/tests/diff_scope_test_support.py` with `contract:knowledge-diff-cases` and an exact consumer list; the contract separately names its owner and evidence node. This is declaration, not a comparison invocation.


- The lifecycle catalog lists `mcp/tests/test_terminal_blocker_reasons.py` as an exact consumer of governed artifacts with their respective replacement contracts. The separate `synthetic-test-evidence-candidate` contract names its own support owner and dependency-census evidence node. These current declarations do not establish a nine-row addition or execution.


- The `_evidence_catalog_fixture.py` artifact declares its current exact consumer list under `contract:synthetic-test-evidence-candidate`; its owner, replacement contract and consumers are catalog declarations, not a four-registration change receipt or execution.


## Source Epochs And Evidence Limits


## Clean-sync and visible-repair regressions

The clean-sync door module tests real Git path/blob/mode comparison and the original review-digest provenance, including distinct CR/LF pathname identities. Rendered instruction wording and audience tests guard clean-sync no-round behavior, immediate repair, per-finding evidence and Manager precedent handling. Its unit/affected-closure catalog registration is selection metadata, not an executed certificate or an Owner closure plan.


## Current Behavior

`test_changeset_cancellation.py` covers (scheduler admission, queued withdrawal, disconnect child reaping, copied-context reclamation and one kill owner) ; `test_changeset_cache.py` covers (id-keyed no-observation, uncached working view, unknown-status non-reuse, bounded request memo) ; `test_intent_summary_cache.py` covers (freshness children filtered, refusal settlement). The cancellation module is declared in the unit-regression lane and on the existing lifecycle consumer rows. These are source assertions and selection declarations, not a fresh whole-suite run.

The review-evidence and frame contracts are measured by `test_review_evidence_packet.py`, `test_review_evidence_residuals.py` and `test_review_frame_store.py`; the sidebar's step-tooltip contract by the dashboard's `stepTitles.test.tsx`. Registration in the evidence lanes selects the population and certifies no invocation.

The suite has cases for provider subagents, the usage report judgement, the limit file, the held-message check and drain, the layering port, extra harness arguments and the projection types.

`test_explainer_browser.py` covers the explainer’s browser: the product-owned folder and its two variable names, one fetch at the pin through the product Node, a refusal that names what is missing and the command, a named module used as given, and the notice prepared before the first fetch. The prospective, host and server suites cover the load's browser readiness, the module handed to a launch, and the announce answered at the serving path. The module is declared in `unit-regression`; selection is not a run.

## Current discovery-startup test selection

The current named regression is `test_dashboard_autostart_after_discovery.py`. Its two fresh autoStart=true processes assert the joint outside-scratch sweep and dashboard-supervision start: neither begins during preparation, server creation or the produced-list-answer snapshot before the event-loop callback; the later callback or the no-list first-call fallback starts each once through the same process latch. Dashboard and host launchers and the reconciliation seam are recorders. The parsed source declarations contain 18 lifecycle contracts, 120 artifacts and 793 lane memberships. These are source assertions and selection metadata, not a new server, test or live-host run.

## Additional source contracts


- Lane selection proves explicit source membership and refuses incomplete/stale catalogs.
- Canonical rewriting preserves retirement decisions and refuses ambiguous rows.
- Recorded-result retrieval in the swept support world has a delivered-payload fallback; the classifier validates that substituted object.

## Concurrent dispatch and preview regressions

`test_mcp_dispatch_concurrency.py` exercises real transport responsiveness, cancellation ordering, conditional bypass and ContextVar/cache/log separation. `test_citation_preview_runs.py` checks synchronous/background preview equality, unchanged memory bytes, shared registry capacity and identity, detached results, scope changes, worker failures and refusal of background writes. The log test separately prevents two concurrent detail writers from spending the same remaining budget. Catalog selection and these source assertions do not establish a fresh test execution.

- Selected-case budgets and default worker/selection policy have one executable configuration owner.

- Source cases retain committed leaf deltas and exclude files already present in an updated base.

The source-file regression exercises the synchronous public quality route with Git fixture repositories. It checks uncited listing and size/count cases, then readable citation mutation and unavailable link/large-file reasons. The current root selected-case ceilings are 10000 unit and 2000 integration; test_memory_quality_source_files.py is declared in integration without weakening the collection guard.

- **The fixture and the governed contract it is registered under.**


> The root `pyproject.toml` owns test paths, default selection, four-worker file distribution, strict markers/configuration and collected-case budgets. The current candidate declares 10,000 unit and 2,000 integration cases (`pyproject.toml:334-335`). The current Python test-policy design note agrees on 10,000/2,000. This is source agreement, not fresh collection or execution. File distribution and collection refusal behavior remain their existing owners’ contracts.



Source cases separate named renames, copies, Git metadata, full-removal threshold and proven/unproven absence.

Source cases separate named renames, copies, Git metadata, full-removal threshold and proven/unproven absence.

The current references point to the landing-report tests, their support, the test-policy design note and root configuration.

### Test registration

The lane manifest registers `test_knowledge_writer.py` once.

The lane manifest declares `test_knowledge_review_one_sided_statements.py` in `unit-regression`.

The lane manifest declares `test_capsule_serving.py` and `test_capsule_serving_surface.py` in `unit-regression`.

The lane manifest declares `test_memory_attribution_producers.py` in `unit-regression`; membership alone does not prove a test invocation.







The instruction-renewal subprocess in AnswerAndTextTests uses sys.executable.

## Retained Evidence Context

- The MIK-R05 lane row.

- The planned-effects module's consumer line. Source caption: `mcp/tests/test_planned_knowledge_effects.py`

- The paging lane row.

- The current settings-guard and Node-lockfile artifact consumer lists both declare test_knowledge_paging.py; these are lifecycle consumer declarations, not lane rows or invocation evidence.

- The lifecycle catalog lists test_knowledge_currentness.py as an exact consumer. Source caption: `mcp/tests/test_knowledge_currentness.py`

Current lifecycle artifact lists declare that named module as a consumer; the historical count does not establish a current three-row census or invocation.



- No lane array in the current catalog declares test_notes_listing.py; this establishes no current selection or invocation.

The current lifecycle catalog declares relationship-line, relationship-movement and relationship-reach modules as exact consumers of both diff_scope_test_support.py and read_scope_test_support.py. Lane membership is declared separately in test-evidence-lanes.toml; these declarations establish no execution.

- The shared read-scope fixture has an exact consumer list.

- The read-scope support artifact mcp/tests/read_scope_test_support.py declares mcp/tests/test_knowledge_review_one_sided_statements.py as an exact consumer. The declaration establishes dependency reachability, not execution.


- Terminal-result blockages are built through _blocker, which refuses a missing, blank or non-string reason; _blocked_reason names a malformed or reasonless item.


- The two integration-lane rows the read's boundary and path modules occupy.




- The composed declarative evidence catalog contains 18 contracts and 120 artifacts; declarations and derived consumers are not fixture-consumption or execution evidence.

Retired means the anchor no longer stands, not that the cited subject was deleted.

## Retirements

Retired means the anchor no longer stands, not that the cited subject was deleted.

Retired means the anchor no longer stands, not that the cited subject was deleted.

Retired means the anchor no longer stands, not that the cited subject was deleted.

Retired means the anchor no longer stands, not that the cited subject was deleted.

- A lifted decision round-trips with its requirement endpoints reported.


Anchor: `test_a_lifted_decision_round_trips_and_its_requirement_endpoints_are_reported`

Current source: The lifted-decision test source first asserts a version-mismatched requirement endpoint is reported with refusal and unchanged memory, then repairs that endpoint and asserts the decision is written and an identical second ingest is unchanged. These are test assertions, not a new execution result.

- The sweep source gives each tool separate unvalidatable and boundary-validation subTests, then separate raiser, unmarked and census subTests.

Current source: The sweep source gives each tool separate unvalidatable and boundary-validation subTests, then separate raiser, unmarked and census subTests. It compares observed error-arm tools with ENVELOPE_LOSING_RAISERS and bare-not-ok tools with UNMARKED_NOT_OK by equality, and separately asserts the error pin in both directions. These are source assertions, not execution results.

- A returned call is judged from the whole result and the delivered answer through one shared classifier.

Current source: In `tool_entry_point_world.py`, a returned call routes through `_returned_arm`, which reads the whole result from the answer-named file; missing/unreadable/non-object files are unvalidatable. _judge_delivered validates the whole result with the tool response model and separately judges the delivered answer, including stripped-envelope and same-place key checks. This is the ordinary world's classifier implementation, not proof of a sweep run.

- The literal PUBLIC_TOOLS tuple in models/tools/public_roster.py contains 44 names, including explainer_control and citation_note_revision. The separate conformance test source pins ROSTER_SIZE = 44, TOOL_MODULE_COUNT = 14 and TOOL_HANDLER_COUNT = 46.


Anchor: `ROSTER_SIZE`

Current source: The literal PUBLIC_TOOLS tuple in models/tools/public_roster.py contains 44 names, including explainer_control and citation_note_revision. The separate conformance test source pins ROSTER_SIZE = 44, TOOL_MODULE_COUNT = 14 and TOOL_HANDLER_COUNT = 46. A literal roster and source pins are distinct from a fresh collection or execution result.

- The leaf-read lane row.

Current source: The current unit-regression lane selects test_knowledge_leaf_read.py. The current lifecycle catalog declares test_knowledge_leaf_read.py as an exact consumer of mcp/tests/_user_settings_guard.py, mcp/tests/anchor_fixture_models.py, mcp/tests/fixtures/repository_profiles/node/package-lock.json, mcp/tests/knowledge_index_test_support.py, mcp/tests/knowledge_rows_test_support.py. These current declarations establish no test execution or acceptance.

- The lifecycle catalog declares test_knowledge_leaf_read.py as an exact consumer of five artifacts.

Current source: The current lifecycle catalog declares test_knowledge_leaf_read.py as an exact consumer of mcp/tests/_user_settings_guard.py, mcp/tests/anchor_fixture_models.py, mcp/tests/fixtures/repository_profiles/node/package-lock.json, mcp/tests/knowledge_index_test_support.py, mcp/tests/knowledge_rows_test_support.py. These current declarations establish no test execution or acceptance.


Current source: The current mcp/tests/evidence-lifecycle.toml declares schema_version = "ar-test-evidence-lifecycle/v3", 18 contract records and 120 artifact records. These are source declarations, not test execution, code delivery or acceptance evidence. The current mcp/tests/test-evidence-lanes.toml selects 793 distinct test modules across its existing lane identities; this count states no earlier insertion, displacement or consumer-addition event.



Current source: The current mcp/tests/evidence-lifecycle.toml declares schema_version = "ar-test-evidence-lifecycle/v3", 18 contract records and 120 artifact records. These are source declarations, not test execution, code delivery or acceptance evidence. The current mcp/tests/test-evidence-lanes.toml selects 793 distinct test modules across its existing lane identities; this count states no earlier insertion, displacement or consumer-addition event.


Current source: The current mcp/tests/evidence-lifecycle.toml declares schema_version = "ar-test-evidence-lifecycle/v3", 18 contract records and 120 artifact records. These are source declarations, not test execution, code delivery or acceptance evidence. The current mcp/tests/test-evidence-lanes.toml selects 793 distinct test modules across its existing lane identities; this count states no earlier insertion, displacement or consumer-addition event.



The current lifecycle catalog declares mcp/tests/test_fresh_user_harness.py as an exact consumer of the fresh_user_fixture.py, fresh_user_scenario.py and run_fresh_user.py support artifacts. The suite contains fixture-shape assertions for oversized source, vendored content, non-default spear and distinct sprint branches, plain fixtures and confinement under the run root. Its scenario assertions require an unrun step to report blocked with reason and owner, unreachable and not completed; it also checks governed-module existence and required report arguments. Catalog declarations and test assertions establish neither test invocation nor acceptance.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.


- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.


Current source: The current mcp/tests/evidence-lifecycle.toml declares schema_version = "ar-test-evidence-lifecycle/v3", 18 contract records and 120 artifact records. These are source declarations, not test execution, code delivery or acceptance evidence. The current mcp/tests/test-evidence-lanes.toml selects 793 distinct test modules across its existing lane identities; this count states no earlier insertion, displacement or consumer-addition event.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The four `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.

Current source: The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance.

- The lifecycle catalogue declares test_landing_report.py as an exact consumer of the three governed artifact/replacement-contract records for _user_settings_guard.py, curator_coherence_test_support.py and the Node package-lock fixture. These bindings cite those existing artifact/replacement-contract identities; they are declarations, not runtime fixture-consumption evidence. ENVELOPE_LOSING_RAISERS is empty and the current sweep case compares it with observed error arms. STATE_DEPENDENT_RAISERS and the ambient lifecycle-state matrix/population are absent, not retained as empty live structures; lifecycle_finalize_task is an ordinary contract-addressed dry-run request in the main sweep, not evidence of membership in a separate state population. the retained finalize-request and comparison targets carry those claims.

Current source: The lifecycle catalog declares test_landing_report.py among the consumers of _user_settings_guard.py, curator_coherence_test_support.py and the Node package-lock fixture; this named subset is not its whole declared artifact population. ENVELOPE_LOSING_RAISERS is empty, and the sweep compares its observed error-arm population with that pin. No executable STATE_DEPENDENT_RAISERS or ambient lifecycle-state matrix remains in the sweep/support/world; lifecycle_finalize_task has an ordinary contract-addressed dry-run request in the main benign table. These are declarations and source assertions, not a fresh run.

The envelope-loss pin is empty. Current source pins distinguish44 advertised tools,14 modules and46 handlers; the source declaration is not fresh collection, execution or live advertisement. ENVELOPE_LOSING_RAISERS is empty. the current assembled table imports ToolAnswerRow and _apply_l111_shaped_rows from tool_answer_l111_test_support and applies nonempty L111 shaped rows after L109; interim-map declarations and retained L100/L109 rows remain separate. Removed task reads are asserted as operation-removed; review, linkage and retirement assertions inspect canonical task state, whole application results or retained whole logs rather than assuming every field survives the delivered answer. Fixed40 roots normalize ordinary token controls, distinct from content/location measurements. Packet-owned refusal tests preserve positive gates and full no-write frames; the runnable-step tests use answer-supplied arguments/display on space/quote/dollar roots, with converted-line and unknown seam limits explicit. Requirement-copy fixtures cover metadata, missing notices, source drift and rollback seams, not real-host acceptance. Role-answer tests force overflow to check a missing filename in a shortened start warning and a whole fitting message warning. A guard test retains `warningCut` through a refit when error text takes the available room. The start row’s sizing fixture models a deep-root capture with representative absolute paths and its log field. declaration, source assertions and prior grades remain different evidence classes.

Current source: The conformance source declares ROSTER_SIZE = 44, TOOL_MODULE_COUNT = 14 and TOOL_HANDLER_COUNT = 46. Its structural tests compare registry and adapter populations in both directions, compare PUBLIC_TOOLS with the registered surface, reject duplicate roster entries and unadvertised registrations, and assert the roster count. These are source declarations and assertions, not a recorded test run or a measurement of the developer’s host.

The current sweep compares the observed envelope-losing raisers with its explicit pin; the retained source assertions do not prove execution. none states a raiser population, and no catalog block can replace that evidence; the sweep source remains the witness.

Current source: The current sweep source compares observed error-arm tools with the explicit ENVELOPE_LOSING_RAISERS pin by equality in both directions. This source assertion establishes no execution or acceptance.

The current catalog names test_landing_report.py on four existing artifact consumer lists; these declarations establish no execution or new artifact identity.

Current source: The current lifecycle catalog declares test_landing_report.py as an exact consumer of mcp/tests/_user_settings_guard.py, mcp/tests/curator_coherence_test_support.py, mcp/tests/fixtures/repository_profiles/node/package-lock.json, mcp/tests/landing_report_test_support.py. These are source declarations, not invocation, code delivery or acceptance evidence.

- The replacement after-discovery test source asserts one joint sweep/dashboard start across scheduling and no-list fallback in fresh autoStart=true processes. The launchers and reconciliation seam are recorders; no execution is asserted here.

Current source: The replacement after-discovery test source asserts one joint sweep/dashboard start across scheduling and no-list fallback in fresh autoStart=true processes; parsed catalog declarations contain 18 lifecycle contracts, 120 artifacts and 793 selected lane members. The launchers and reconciliation seam are recorders; no execution is asserted here.

The explainer tests check bound reading inputs, moved Update with preserved stage files, and exact essay-first defaults. The capability cases pin the shipped stage wording and 1,500-word budget. Separate video cases check the runner's media map, the static attributes and the store's publication and readback.

The task-entry fixture supplies stale helper work and an obsolete declared wait to a closed seat. It observes paused with no waiting seats, then work on the next turn (test_task_entries.py:537–560). Separate fixtures cover archive timestamp ordering and receipt-backed registry restoration before the dashboard snapshot.

The recorded-base suite tests inheritance across an untrailed memory merge, exact commit ancestry and converted onboarding cards. The carry-over tests judge inherited memory and carried payloads against one receiving-leaf base. The live review and precompute cases distinguish a changed memory-base commit even when the captured trees match.

## Evidence

### Repo-Internal References

- A closed seat’s stale helper and wait fields leave the task paused. Its next turn contributes work. [1843]

- The lifted-decision test source first asserts a version-mismatched requirement endpoint is reported with refusal and unchanged memory, then repairs that endpoint and asserts the decision is written and an identical second ingest is unchanged. These are test assertions, not a new execution result. [1443]


- The sweep source checks unvalidatable and boundary-validation outcomes separately for each tool. Population checks compare the error arm, bare-not-ok arm and tool count. A separate exact equality assertion checks the error-arm pin in both directions. [1704]


- The current sweep source compares observed error-arm tools with the explicit ENVELOPE_LOSING_RAISERS pin by equality in both directions. This source assertion establishes no execution or acceptance. [1751]


- The literal PUBLIC_TOOLS tuple in models/tools/public_roster.py contains 44 names, including explainer_control and citation_note_revision. The separate conformance test source pins ROSTER_SIZE = 44, TOOL_MODULE_COUNT = 14 and TOOL_HANDLER_COUNT = 46. A literal roster and source pins are distinct from a fresh collection or execution result. [1807]


- Transport cases preserve per-call context and write ordering. [1810]

- Preview cases preserve synchronous semantics without writes. [1811]

- Concurrent detail writes share one budget. [1812]



- The door regression exercises exact clean-sync provenance and byte path discrimination. [1786]

- Delivered role wording keeps sync, precedent and repair-entry obligations visible. [1785]

- Master validation in placement applies only to documented subTasks; other listed kinds retain list placement under existing identity/cycle guards, not a kind-rejection or own-master-validation rule. [1783]

- Controlled-host cases protect archive successor identity, live-only use, bounded traversal and placement refusal; catalog declarations do not prove execution. [1775]

- A controlled actual-serving-runtime case uses two real Projector subscriptions to check landing interest until the final subscriber leaves. Separate direct controlled-refresher cases check disconnect during discovery, clock/age bands and current-identity resets; they do not build the serving composition. [1766]

- Controlled real-loop tests preserve periodic safety independent of launch-authority state. [1767]

- The module's own statement of what it protects. [1495]


- The isolated pytest setup declares three default plugins: pytest bootstrap, evidence lanes and database retirement. Certifying configuration loads its separate bootstrap plugin. [3]











































- The partial-index case preserves the remaining invariant answer and marks that answer and the cache report partial. [1472]





















- The synthetic catalog builder writes artifact category and fidelity metadata; this is fixture declaration. [1516]

- The synthetic catalog builder writes artifact category and fidelity metadata; this is fixture declaration. [1522]


- The unwired, invalid-selector, authority-error and missing-path transport cases require the ACTIONABLE fields. A separate typed domain case preserves its own refusal payload. [1518]












- The shared synthetic evidence catalog builder produces fixture metadata; its declarations do not establish production composition or test execution. [1532]








- The field-row case asserts the exact acceptance_ref/lifecycle/payload_digest roster, absent-before and present-after text-knowledge acceptance_ref, and proposed-to-accepted lifecycle. It does not assert a both-sides structured-value round-trip. [1545]



- The Python producer tests and renderer tests exercise the same statement-side contract with independently authored fixture text. The renderer source uses its own added, removed, present and unresolved examples. The Python comment still points to the renderer and describes a literal match that the current source does not contain. [1549]


- A task-attached launch's capsule is the compiler's own result for the same seat -- trusted instructions and semantic digest -- never a hand-built literal. [1550]

- One decision point with two answers: a capsule role compiles, and every other seat refuses with a status that names the role and delivers nothing. [1552]

- The free agent's admission names its absent task plane and its capsule identity moves with the seat; the replacement route refuses by name for an unmarked stage part, a role the stage lacks and a missing required file. [1553]





- The SEP entry contract is asserted in mcp/tests/test_capsule_serving_surface.py separately from this server's own index shape. [1558]


- One case asserts SEP-2640 entry fields, frontmatter and resource bytes. A separate case asserts the server index shape and distinguishes its keys from the SEP entry. [1802]


- The current SDK client/server exchange and separate traversal-refusal case live in mcp/tests/test_capsule_serving_surface.py. The exchange asserts both extension methods succeed and absent/unregistered calls fail; it does not assert the exact -32602 error code. [1559]

- The current SDK client/server exchange and separate traversal-refusal case live in mcp/tests/test_capsule_serving_surface.py. The exchange asserts both extension methods succeed and absent/unregistered calls fail; it does not assert the exact -32602 error code. [1803]

- The case that keeps the seeded-mutation evidence honest lives in mcp/tests/test_capsule_serving_surface.py. [1560]

- The case that keeps the seeded-mutation evidence honest lives in mcp/tests/test_capsule_serving_surface.py. [1804]













- A traced closeout apply commits the actual code and memory pair. A separate case interrupts the production application handler after the code commit, then supplies that exact commit to direct closeout recovery. The recovered memory-content commit retains code attribution and recreates the missing cache. [1604]







- Current path cases assert typed magic-spelling refusal and literal glob-character path authoring, storing, seeding and exact blob observation. [1611]

- The missing requested-tree case reports unavailable before lookup, distinct from a genuine absent path. [1612]




- The current case asserts present-outside-selection versus absent-from-snapshot side by side and names the outside-selection omission. [1621]












- The signal suite includes the nine-field required-input table and the two conclusion-bearing-field/detail refusal controls. [1636]



- Two full renders leave both datasets canonical row counts unchanged. [1644]





- Current test_the_carrier_uses_the_field_spellings_the_answer_returns asserts card, recordCounts, actionNeeded, overviews, codeState and memoryState in carrier text, and excludes published_intent, repository_overview, route_overviews and served_earlier. It does not derive vocabulary from a real page. [1656]


- The former history-sentence/ambiguity case is retired. Current family-context population asserts recorded-empty versus absent, before-context retention for additions/removals and authored-population preservation; no new revision-chain-history assertion is claimed. [1663]







































- One case asserts SEP-2640 entry fields, frontmatter and resource bytes. A separate case asserts the server index shape and distinguishes its keys from the SEP entry. [1744]


- The case that keeps the seeded-mutation evidence honest lives in mcp/tests/test_capsule_serving_surface.py. [1746]

















- The shared comparator checks call-day paths, causal directory entries, log details and completed-call river records. [1707]

- The module docstring names the instruction-wording and ignored-environment duties. The four cases protect shipped instruction wording and ignored-environment accounting, with no lifecycle execution. [1708]
























- The install case checks an overflow answer and the uniquely filed reports for the first and updated calls, including host facts and redaction. It matches reportPath when supplied. [1701]




Candidate isolation, three plugin registrations and ordinary/certifying composition are explicit. [1716]

Lane selection proves explicit source membership and refuses incomplete/stale catalogs. [1719]

Artifact discovery and exact consumer comparison have bounded source owners. [1720]


- The canonical rewriter refuses ambiguous duplicate contract or artifact rows and table headers its line scan misses. It removes missing consumer paths only when a listed consumer survives and leaves artifact-row retirement to the author. Both catalogs merge by union. The catalog validator offers --write to canonicalize both. The role test checks the raw Curator text in both discovered deliveries and one compiled canonical Curator capsule. [1721]





- The environment fixtures check interpreter wording and candidate accounting with a real standard-library venv. Node coverage here is a populated node_modules directory with fixture.js, rather than a Node installation or runtime qualification. [1726]










- The skill surface is the canonical tree plus its one packaged serving copy declared in `generated-copies.json`. [1805]


- The sync script parses generated-copies.json, selects the skills source and resolves paths from its declared targets. [1813]


- The current reconsideration module imports extracted configuration support and its current fixture owners. [1769]


- The relabelled changed-row control preserves its revision-refusal assertion with the admitted worklist. [1771]



- The real paired-enclosure fixture initializes and verifies its empty repository lock before measuring refusal. [1773]



- The competing writer directly observes lease exclusion and uses the shared hang guard. [1774]


- The native pidfd fixture asserts one exit invalidation with controlled process identity; this source is not a fresh native-host run. [1777]

- The nested-dependency case compares on-demand body dependencies and bodyRevision with corpus projection for two addressed documents; not executed here. [1778]

- The intent-cache concurrency case blocks its own reader while another route completes; static assertion inspection is not measured runtime evidence. [1779]

- Raw tool-event assertions require task scopeKey and absence of session/lifecycle attribution; not executed here. [1780]

- Reviewer landing wording is checked in each discovered root's delivered Reviewer role section and its emitted instructions, not in a separate step-8 detail. The discovered roots are the canonical tree and its packaged serving copy. [1782]


- Current Reviewer source cases distinguish required judgment/semantic side states and retained assessment count consistency from the retired reviewer envelope; latency and memory-watch modules protect their separate read/observation boundaries. No execution is asserted. [1784]


- Numbered comparisons preserve their own outline/counts and retained catalogue answers; route admission refuses negative input before the port and forwards positive input unchanged. [1789]

- Selected display versions and converted-history writer outcomes distinguish recorded/introduction, no recorded writer and unavailable history. [1790]

- Card-entry memory values come from the bound after index; lane omission and failed-memory non-retention remain explicit. [1791]


- Developer-send and seat-list cases use in-process owners with a fake native host. Separate sent-log and cross-site cases cover bounded storage and the pre-route guard. [1792]


- The controlled bridge asserts native attachment options and pre-operation invalid-payload refusal; complete versus truncated listings carry into the recipient list. [1793]

- The request head for 500 invariants is checked against actual two-read h11 parsing and foreground/daemon-child plus reload configuration. [1794]



- The landed-leaf test opens the delivered code and memory commits, keeps the earlier numbered comparison and asserts each comparison's counts. A separate case refuses when Git cannot produce the delivered pair. [1796]


- Cardless source-map cases inspect real writer rows while preserving the mixed-group qualification. [1797]



- Initializer tests assert regular-task and Curator guidance for empty and recorded memory, partial and legacy outcomes, and unchanged files under dry-run. The converted journey checks guidance and a second fixer refusal after baseline adoption. [1800]




- Source-file scenarios call the synchronous memory-quality controller. Helpers assert read-policy refusals, successful citation resolution, and stale content after the cited bytes change. [1809]























- The conformance source declares ROSTER_SIZE = 44, TOOL_MODULE_COUNT = 14 and TOOL_HANDLER_COUNT = 46. Its structural tests compare registry and adapter populations in both directions, compare PUBLIC_TOOLS with the registered surface, reject duplicate roster entries and unadvertised registrations, and assert the roster count. These are source declarations and assertions, not a recorded test run or a measurement of the developer’s host. [1733]

































































- In `tool_entry_point_world.py`, a returned call routes through `_returned_arm`, which reads the whole result from the answer-named file; missing/unreadable/non-object files are unvalidatable. _judge_delivered validates the whole result with the tool response model and separately judges the delivered answer, including stripped-envelope and same-place key checks. This is the ordinary world's classifier implementation, not proof of a sweep run. [1705]




- The instruction-renewal subprocess in AnswerAndTextTests uses sys.executable. [1772]



- The renewal family separates digest bindings, manifest routing/no-step authority and pointer withdrawal/refusal controls. [1832]

- The default options select the unit population and four workers. [1]
- The current repository-root collected-case declarations are 10,000 unit and 2,000 integration. [2]

- Integration and stress-durability files are skipped before import when the marker expression is exactly `not integration`. [5]

- The collected cases are counted against the two budgets. [6]
- The collection hook loads the lane manifest and marks each item with its lane. [7]
- The real catalogs load through both loaders. [11]
- The current source test asserts that the catalog stays closed over the governed inventory and declares no unreferenced contract. [12]
- The union merge attribute for both catalogs. [13]
- Which files of this route are governed test artifacts. [15]

- During canonical rewrite, the lane rewriter removes entries for missing files, and the lifecycle rewriter removes missing entries from artifact consumer lists. [16]

- The task-scoped MCP reader cases. [18]
- The previous-host removal guard. [19]
- The bounded sandbox process cases. [20]

- Launch cases cover refusals, unanswered catalogues, ACP task-server binding and the merge of feature values. [21]

- At configuration, conftest reads integration and stress-durability file membership from the lane manifest. [22]
- The lifecycle loader refuses a catalog that is not canonical or does not agree with the source tree. [24]

- General test policy forbids recursive suite execution and repeated repository scans to test the suite; coverage stays diagnostic and the canonical-form module uses four real-pytest cases in temporary synthetic repositories. The bounded timing scanner reads its named support roots and excludes waits.py. [25]

- The lane loader refuses a test file without a lane and a lane list that is not canonical. [26]
- The gate's warm pass becomes the refusal when a packet locator is retargeted. [497]

- The review port captures one code and one memory witness on the first read. The leaf worklist uses those witnesses without capturing its own, and repeated or pinned reads reuse the one computation. [498]


- The real child matches the in-process worklist, source reads and answer body at both response sizes. It uses the held capture and conversion without a second base lookup. [499]


- The source case admits twelve waiters sharing one computation and nineteen across eight computations, then refuses one more distinct computation. [500]


- The kept-view case reuses its answer through changes to unread task documents and recomputes when the observed leaf document changes. [501]

- The Python timing scan covers mcp/tests and mcp/test_support, excluding the shared waits.py; it reports syntactic timing violations without running the repository suite. [502]
- The process-state scanner compares syntactic process state under mcp/src/agents_remember with the exact closed register. [503]
- Finalizing a master no sprint commands keeps it and names the retire route. [504]
- A landed abandoned row refuses by name. [505]
- The partial-hook-failure retry keeps the retirement and cleans up only. [506]

- The lane row. Source caption: `mcp/tests/test_review_change_kinds.py` [1414]

- A leaf is ready once current rows answer every item; editing the source again reopens four items: invariant, family, file trace and route trace. [1415]
- The worktree-closeout refusal restores the history file and closes it once valid. [1416]

- The sync-merge case permits a consistent own-side history row and preserves the moved sidecar. An inconsistent own-side row refuses with R09-history-rows. [1417]


- The lane manifest declares test_knowledge_closeout_gate.py in unit-regression. Membership establishes no execution. [1418]

- The folder-master finalize cases. [1419]

- The task-reopen cases assert that reopen resets the contract, task document and master row, including the folder-master row for a leaf that names no master. [1420]


- The bucket case reconciles buckets and destinations. The live route test asserts typed HTTP 200 refusals for admitted paths of 1,025 and 4,096 characters and checks clipping of the offending input. [1421]


- The current lane manifest declares mcp/tests/test_review_unexplained_lane.py in unit-regression. This exact named-module registration establishes neither invocation nor acceptance. [1422]

- The registry compared as a set. [1423]

- The current lane manifest declares mcp/tests/test_reconsideration_surfacing.py in unit-regression. This exact named-module registration establishes neither invocation nor acceptance. [1424]


- The module describes a code repository and converted memory repository with recorded knowledge, onboarding, census and history over two fixture commits. [1425]

- The walk-tree case (F16, R3-1, R3-2). [1426]
- The route case: every view, 503 unwired, nothing written. [1427]

- The lane row. Source caption: `mcp/tests/test_knowledge_reader.py` [1428]

- The cards-read case and its four helpers. [1429]

- The proof admission at the route. [1430]

- The Q8 case. [1431]
- The budget and resumption case. [1433]
- The lacking-revision case on resume and fresh read. [1434]
- The entry-less page in the leaf-read module. [1435]
- Delete-only: only no_invariant. [1437]
- The knowledge items, without the unexplained kinds. [1438]

- The current lane manifest declares mcp/tests/test_review_git_trees.py in unit-regression. This exact named-module registration establishes neither invocation nor acceptance. [1439]

- A repeat read writes nothing. [1440]
- Archival deletes only the task's own artifacts. [1441]

- The decision-record lane row. Source caption: `mcp/tests/test_knowledge_decisions.py` [1442]

- A decision is never an export (review F6). [1444]

- The conforming directory move. [1448]
- A forged legacy ID does not make a record exported. [1449]
- The writer refuses an unsupported admission claim. [1450]

- The current lane manifest declares test_planned_knowledge_effects.py in unit-regression; membership does not establish execution. [1451]


- The lane manifest declares mcp/tests/test_knowledge_paging.py in unit-regression. Membership declares selection, not invocation. [1453]


- The onboarding trace gate's lane row (`mcp/tests/test_onboarding_trace_gate.py`). [1455]


- The gate fixture pairs real code and converted memory repositories through a Code-Commit trailer and a leaf series contract. [1456]


- The current lane manifest declares mcp/tests/test_knowledge_currentness.py in unit-regression. This exact named-module registration establishes neither invocation nor acceptance. [1457]


- The lane manifest declares test_knowledge_worklist.py in unit-regression. Membership establishes no execution. [1459]


- The lane manifest registers mcp/tests/test_knowledge_proofs.py in unit-regression. Membership selects evidence and does not establish execution. [1460]

- The migration-pass case. [1462]

- The current lane manifest declares mcp/tests/test_knowledge_conversion.py in unit-regression. This exact named-module registration establishes neither invocation nor acceptance. [1463]


- The lane manifest registers mcp/tests/test_knowledge_writer.py once in unit-regression. Membership does not establish execution. [1464]

- The conforming example's measures carry their counts. [1465]
- A recorded assessment is never edited; a correction appends. [1466]

- The current lane manifest declares mcp/tests/test_knowledge_census_files.py in unit-regression. This exact named-module registration establishes neither invocation nor acceptance. [1467]

- The Doc14 family example validates. [1468]
- A file failing its schema marks the index partial and is named. [1470]
- Parity of the reused selection over the index and the database. [1471]

- The lane manifest declares test_knowledge_index.py in unit-regression. Membership establishes no execution. [1473]

- The based converted fixture passes with carried legacy debt. Registration pins the merge-report and migration-debt sets and contains zero plain report-only rules. [1474]
- The managed sync refuses, keeps the merge staged, and syncs after the repair. [1475]

- The lane manifest declares test_knowledge_validator.py in unit-regression. Membership establishes no execution. [1476]

- The freeze cases. [1477]
- The parallel-merge case. [1478]

- The current lane manifest declares mcp/tests/test_knowledge_history_files.py in unit-regression. This exact named-module registration establishes neither invocation nor acceptance. [1479]


- The nine Doc14 fixtures each parse as their declared model type and round-trip to identical canonical bytes in the source test. [1480]


- The current lane manifest declares mcp/tests/test_knowledge_file_canonical.py in unit-regression. This exact named-module registration establishes neither invocation nor acceptance. [1481]

- The module's own statement of what it pins. [1482]

- The route serves an unrecorded committed view with HTTP 200, preserves its serialized state and answers an unknown leaf with a named HTTP 404. [1484]

- The fake-client recorder reads each line of `record.jsonl` as JSON. [1485]

- The source-endpoint cases use production capture and recorded-endpoint composition. [1486]


- The module's own statement of the admitted population and its cases. [1487]


- The lane manifest registers mcp/tests/test_knowledge_review_attributed_source_content.py in unit-regression. Membership selects evidence and does not establish execution. [1488]

- The task-document body lookup has corpus-independent touches on its named fixture: a leaf reads its own document and owning master, a master reads its own document, while sprint reads the addressed document and three explicitly related master documents. It is not an every-request one-document guarantee. [1489]
- The count-based scaling case. [1490]

- Its lane registration. Source caption: `mcp/tests/test_task_document_body_lookup.py` [1491]

- Availability loss reported, not remembered. [1496]

- The current lane manifest declares mcp/tests/test_read_anchor_memo.py in unit-regression. This exact named-module registration establishes neither invocation nor acceptance. [1497]

- The movement module uses synthetic index-shaped rows with production composition; converted-tree public-resolution cases provide separate evidence. [1499]

- Current removed-claim/new-claim case renders a retraction and an addition under the same invariant identity, with no pairing basis or counterpart path. Same identity alone does not supply a movement edge. [1500]

- A withdrawn realization remains visible with its deleted file and identity. A source rename does not fabricate relationship inference. [1501]


- The cases check a family association reassigned between revisions, the relationships from declared routes, the distinction between an unread side and an ungoverned side, and the state and reason of an unresolved side. [1502]

- The relationship-reach module states the withdrawn-association boundary and tests a member with two unpaired revisions. [1503]
- A member with two unpaired revisions is a retraction with no gap and never denied; withdrawals remain visible. [1504]
- The selected judgment omits same-leaf sibling rows. [1506]

- The unit-regression registry includes the revision-selection test module (`mcp/tests/test_knowledge_review_revision_selection.py`). [1507]


- The module declares the evidence_unit pytest marker, and the lane catalog selects the module in unit-regression. [1508]

- Two text-backed snapshots under one namespace expose their own retained revision identities. The current selection fixture supports a single revision per side. [1509]
- Current test_a_single_retained_revision_pair_compares_head_to_head asserts one retained head on each side. [1510]
- Current heads are the sorted retained population: every retained revision is a head because text records hold no predecessor edge. [1511]

- The direct review composition test asserts that the selected retained head on each side supplies the present statement in the payload. [1512]

- Current subject-surface cases assert compared, present before/after statements and exact comparison fields. [1513]

- **The module's own statement of what it measures — endpoint-correct, generation-bound, through the operations the dashboard really calls.** [1514]


- **The shared master-shaped world and its builder.** [1515]

- The historical-committed-leaf module drives recorded-review resolution through its HTTP route and separately checks typed refusal paths. [1517]

- The fixture builds a FastAPI app and registers the actual review routes with a fixture runtime config and the supplied ports. [1519]

- **The conforming example at the transport, with no `payload` key so a refusal cannot read as a success.** [1520]
- **The status family derived from the refusal's own code.** [1521]

- **The module's own statement of the requirement and of the property behind each case.** [1523]


- **The first case: both bound objects' own bytes, each against an independent `git show` observation.** [1524]


- **The content classes the fixture materializes for real, and the routes wired as the composition root wires them.** [1525]


- The cases assert generation binding, unavailable source when one Git object cannot be read, and refusal for a path outside the measured change set. [1526]


- The source controls refuse a commit in the generation field, an unlisted path, the wrong baseline, an omitted generation and an unwired route. A separate case asserts the listed entry and its expansion identify the same path. [1527]

- **The shared R01 fixture these cases extend rather than duplicate.** [1528]

- The fixture wires the application source-content owner and drives it through the /api/review/intent/source-content route. [1531]

- The review wire requires judgment and omits the retired evidence, assessment and context channels. [1533]
- The endpoint fixture creates a real external-memory repository and linked worktree. [1534]

- The changed-path partition case asserts three disjoint and exhaustive buckets against the source inventory. It excludes an unchanged mapped path and counts a multiply mapped changed path once. [1535]

- The attribution cases distinguish readable and unreadable knowledge halves, preserving the readable side and marking the unavailable remainder unknown. [1536]
- One collected subject covering all three arrivals at the series publication. [1537]
- The interrupted reset resumes rather than stranding the branches the series stands on. [1538]
- The one collected case pins all three directions of the step rule. [1539]
- A position descending from a step cannot vacate it. [1540]

- The current lane manifest declares mcp/tests/test_knowledge_review_one_sided_statements.py in unit-regression. This exact named-module registration establishes neither invocation nor acceptance. [1541]


- The module declares the evidence_unit pytest marker, and the lane catalog selects the module in unit-regression. [1542]

- The fixture builds two snapshots under one namespace with added, removed and shared revision identities. [1543]

- **The addition and the removal: the complete present-side statement beside the named absent side, with the comparison's own side-absence code.** [1544]


- The one-sided-record case and the task-context case. [1546]

- The worklist module’s fixture world and synthetic corpus. [1555]

- The admission guarantees: no role acquisition by string, no caller-selected source, no write to the read tree. [1556]


- Four serving cases cover catalog-path containment, unreadable skill index refusal, directory and frontmatter name agreement, and idempotent extension registration. [1557]


- The lane row selects mcp/tests/test_capsule_serving.py into unit-regression. Membership is selection, not execution. [1561]


- The leaf-bound controller fixture exercises worklist persistence, checklist rendering and route-index generation on a fresh shared clone. It stubs the quality runner, census and final-catalog projection. [1566]


- The interactive full-check controller projects the complete final catalog and describes missing certification authority. The projection carries exact pair authority and leaves the affected-closure plan digest unset. [1567]

- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1570]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1572]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1573]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1574]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1575]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1576]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1577]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1578]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1579]
- The live public-surface inventory contract for the advertised MCP tool tuple. [1581]

- The terminal-status tests cover both accepted cleanup tools, validate the emitted argument mapping against the named tool, require the three next-move fields, and check refusal of an unregistered nextTool. [1583]


- The lane row that admits the L3 module: `test_memory_backfill.py` in the `unit-regression` lane. [1584]

- The contract-scoped activation record: one record per series contract, keyed by the contract fingerprint rather than a source pair. [1585]

- The L37 structural half: the pause's import closure is disjoint from every publication module. [1587]

- The ordered lifecycle playthrough covers master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf commanded after the landing still starts. [1588]

- The lane manifest currently registers mcp/tests/test_memory_attribution_producers.py in unit-regression. The current membership declaration selects evidence and does not establish execution. [1590]



- An already torn-down provider fixture finalizes on the first call. A real permission failure names the provider-runtime reason on both the first call and identical retry and leaves the leaf open. Separate direct cases exercise result normalization and the blocker builder’s reason requirement. [1594]


- The pause module tests the public stop boundary and its refusal cases. Its never-selected case asserts the already-vacant success. [1596]
- **The mid-flight reporting boundary:** a completed pass beside a reconciling selection is not this call's success, and a refusal left beside one leads with the mid-flight state. [1601]
- The contract-scoped activation forcing suite and its shared-source-pair fixture. [1602]
- The registered admission refusal addresses only the addressed contract's own state. [1603]
- Cache damage cannot change the accepted integration pair or block ref publication. [1605]
- The migration acceptance proof reads only committed trailers. [1606]
- Cache damage cannot change the accepted integration pair or block ref publication. [1607]
- The migration acceptance proof reads only committed trailers. [1608]
- **The completeness node that derives the mandatory set from recorded rows rather than from the implementation's own page manifest.** [1609]
- The ordering and truncated-page cases. [1610]
- The lookup that could not be run at all, reported as the same fact. [1613]

- The source case checks that each returned cursor binds its page manifest and a substituted manifest refuses with continuation_binding_mismatch before yielding a page. [1614]



- The lifecycle catalog registers mcp/tests/read_scope_test_support.py with contract:knowledge-read-scope-cases and an exact consumer list; the contract separately names its owner and evidence node. This is declaration, not a read invocation. [1615]



- The lane manifest declares mcp/tests/test_knowledge_read_scope.py in unit-regression. Selection is not execution or acceptance. [1616]


- The lane manifest declares mcp/tests/test_knowledge_read_boundaries.py and mcp/tests/test_knowledge_read_paths.py in integration. Membership is selection, not execution. [1617]



- The lifecycle catalog registers mcp/tests/read_scope_test_support.py with contract:knowledge-read-scope-cases and an exact consumer list; the contract separately names its owner and evidence node. This is declaration, not a read invocation. [1618]



- The lane manifest declares mcp/tests/test_knowledge_read_scope.py in unit-regression. Selection is not execution or acceptance. [1619]

- A realization removed from the candidate retains its baseline source in the comparison union. [1620]
- **The forbidden-overreach case: nine verdict words searched over the serialized response, with a positive control.** [1622]
- **The node that drives a real candidate write and refuses its continuation, and the substituted-snapshot refusal.** [1623]
- The expansion, the visible unattributed gap, and the filter that narrows the display and never the comparison. [1624]


- The comparison fixture is registered under the knowledge-diff-cases contract. [1625]




- The comparison fixture is registered under the knowledge-diff-cases contract. [1626]



- The wire-shape case builds a world, reads the complete review, then checks that the current payload carries judgment and omits the retired evidence channels. [1627]

- An over-budget selected population raises UsageError before its tests execute. [1628]
- The publish refusal names the one omitted member, for each of the nine. [1629]
- The all-nine refusal names every member in declaration order. [1630]
- The positive control binds the declaration to the request model's own field order. [1631]
- The prepare text is asserted from the real `_prepare` path. [1632]
- The sibling refusal names the supplied member for each read action. [1633]
- The multi-field refusal names every supplied field in model order, `judgments` included. [1634]
- The freeze branch keeps its own named refusal. [1635]

- The lifecycle catalog registers mcp/tests/read_scope_test_support.py with contract:knowledge-read-scope-cases and an exact consumer list; the contract separately names its owner and evidence node. This is declaration, not a read invocation. [1639]



- The lane manifest declares mcp/tests/test_knowledge_read_boundaries.py and mcp/tests/test_knowledge_read_paths.py in integration. Membership is selection, not execution. [1640]



- The comparison fixture is registered under the knowledge-diff-cases contract. [1641]


- The judgment-evidence case module declares its evidence-unit lane marker. [1642]

- The forbidden-name set the whole payload schema is walked against. [1643]


- The case that the adapter selects nothing, compared value for value. [1645]


- The transport case: typed result, a 400 and a 503. [1646]

- The collection hook compares selected parametrized unit and integration populations with their configured budgets and raises `UsageError` when a budget is nonpositive or exceeded. [1650]
- The attributed-source-content module exports the _pair test scaffold. [1651]
- The publication-input cases in their new home, asserting the declaration is the model's own field order. [1652]


- The source-endpoint cases exercise captured, recorded and unrecorded endpoint resolution, source inventory and task-context selection through production composition. [1653]


- Review resolution delegates closed and recorded comparisons, uses the shared live candidate capture, and reads recorded committed ranges through their endpoint resolver. [1654]
- `_selection()` resolves published intent, asserts a `PublishedIntentSelection`, and returns it to the invalid-seed case. [1655]
- The memory initializer reports an unconverted memory tree as legacy-format. [1657]


- **The no-datasets fixture shape and the selector-less request the task-context cases use.** [1658]



- Real-repository inventory cases cover renames, binary content, spaces, tabs and newlines, non-renderable paths, unavailable or partial inputs and non-UTF8 pathnames. [1660]


- One case keeps a selected knowledge comparison beside a measured empty source inventory. Another checks that an inventory carrying an unnameable path is partial. [1661]

- New-member context preserves the independent family counterpart. [1662]
- The record-only successor case (L47-R1-F3). [1665]
- The cutover module's docstring describes its current scope. [1666]
- The reopen module's docstring. [1667]
- The public closeout refuses an open item and commits once it is answered. [1669]

- The worktree next-move contract declares nextAction, nextTool and nextArgs together. [1670]

- refuse a `nextTool` outside the roster (`_require_registered_public_next_tool`) [1671]

- Development commands, budgets, diagnostic metrics and isolation. [1677]

- Certifying publication and accepting consumers. [1678]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1680]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1681]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1682]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1683]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1684]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1685]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1686]
- The lifecycle catalog declares four permanent scripts/e2e_harness artifacts with exact-source consumer sets: fresh_user_fixture.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; fresh_user_scenario.py lists test_fresh_user_harness.py and run_fresh_user.py; reporting.py lists test_fresh_user_harness.py, fresh_user_scenario.py and run_fresh_user.py; run_fresh_user.py lists test_fresh_user_harness.py. These declarations establish registration, not test execution or acceptance. [1687]

- The lane row that admits the L3 module: `test_memory_backfill.py` in the `unit-regression` lane. [1689]

- The contract-scoped activation record: one record per series contract, keyed by the contract fingerprint rather than a source pair. [1690]

- The lane manifest registers `mcp/tests/test_memory_attribution_producers.py` in `unit-regression`. Membership selects evidence and does not establish execution. [1693]

- The contract-scoped activation forcing suite and its shared-source-pair fixture. [1696]

- The running mismatched host requires a restart and is left untouched. [1702]

- The node module. [1703]
- Registered preview preserves startup/Git state while checking call records. [1706]
- The shared support guard refuses protected settings paths before returning a write path. [1709]
- The world child proves its reviewed source and leaves the fake-account home empty on refusal; the scanner derives its support population recursively. [1710]
- The comparison selector proof over recorded trees [1711]

- Review outline and change classification share the RecordChanges definition for known facts. [1712]


- Review outline and change classification share the RecordChanges definition for known facts. [1713]


- Reconsideration cases assert successor suppression, a still-open changed target without a successor and an unchanged base item despite an unrelated candidate decision. Pytest declares limits of 10,000 unit and 2,000 integration cases, enforced after collection. [1714]

- Recorded-meaning regression uses compose_review over converted trees, exact owner/attempt selection, outline and continuation equality, portable L37 historical fixtures and retired/before-only UUID witnesses. [1715]
- Source controls cover cut measure, threshold, deletion proof and overviews. [1716]
- Source cases retain committed leaf deltas and exclude files already present in an updated base. [1717]
- Fixture assertions keep landing reports non-refusing while preserving existing refusals; adjacent closeout services are mocked. [1719]
- Source cases inventory live/dangling links at own size and bound counted multiset hash work. [1720]

- The landing-report module (`mcp/tests/test_landing_report.py`) is selected in unit-regression; registration is not execution. [1722]

- Settings refusal compares account home or earliest observed home before returning a write path. [1724]
- The support scanner derives nested support and checks supported syntactic bypasses. [1725]
- The retained production ref transaction checks protected heads, ancestry and exact landing output. [1728]
- The bounded timing scanner reads its named support roots and excludes waits.py. [1730]


- Launch, status and document-chat tests share the stateful launch fixture through their own test classes. [1732]



- Pytest setup isolates the test process and declares three default plugins. Certifying configuration loads a separate bootstrap plugin. [1735]


- The module states that an addressed task body reads only the named documents and preserves the corpus projection. [1736]

- **The fixture that makes retained populations real: two independently built text-tree snapshots under one namespace, with heads read from what is retained.** [1739]

- One case compares a retained singleton pair head to head. A separate case records the before head and an empty after side as a removal. [1740]

- Revision selection compares retained singleton heads; a known-empty after side records the before head as removed. [1741]
- The surface derives its selected record sides from current tree heads. [1742]

- Capsule-serving cases check catalog escape, an unservable index, a directory-name mismatch and idempotent extension registration. [1743]

- Family-context cases distinguish recorded-empty from absent, retain before-context for additions and removals and preserve sparse authored populations. [1749]

- The case asserts a missing before acceptance_ref and an after reference beginning with text-knowledge:. It asserts the lifecycle as proposed before and accepted after. [1755]


- The partial-index case preserves the remaining invariant answer and marks that answer and the cache report partial. [1756]

- The synthetic catalog builder writes artifact category and fidelity metadata; this is fixture declaration. [1757]
- The four exception/unwired transport controls require ACTIONABLE fields; typed domain refusals are asserted separately in their own body shape. [1758]
- The shared synthetic evidence catalog builder produces fixture metadata; its declarations do not establish production composition or test execution. [1759]
- Current path cases assert typed magic-spelling refusal and literal glob-character path authoring, storing, seeding and exact blob observation. [1760]
- The missing requested-tree case reports unavailable before lookup, distinct from a genuine absent path. [1761]
- The current case asserts present-outside-selection versus absent-from-snapshot side by side and names the outside-selection omission. [1762]
- The signal suite includes the nine-field required-input table and the two conclusion-bearing-field/detail refusal controls. [1763]
- Two full renders leave both datasets canonical row counts unchanged. [1764]

- The Python comment describes a historical literal match. The current renderer uses its own fixture text to exercise added, removed, present and unresolved statements. [1765]

- The current collected-case declarations are 10,000 unit and 2,000 integration; neither source assertions nor declarations establish execution. [1768]
- The changed-row refusal passes `world.gate().worklist` into `WriteRequest`. [1770]
- The selected static task-entry case asserts authored-stage precedence over host activity and an unknown-host outcome (`test_task_entries.py::test_stage_has_priority_over_host_activity`); event contribution and the known-empty-host outcome are asserted by the module’s other case. Not executed here. [1776]
- The selected evidence-packet case asserts that a foreign repository with equal trees is never this comparison (`test_review_evidence_packet.py::test_f01_a_foreign_repository_with_equal_trees_is_never_this_comparison`); the packet, read, claim and prepared-address contracts are asserted by the module's other cases, not by this one. [1787]

- No-knowledge task-context source cases assert All changes wording, absence of `. ` in the statement and inventory truth without browser-layout evidence. [1795]


- Capsule-serving cases check catalog escape, an unservable index, a directory-name mismatch and idempotent extension registration. [1801]

- The current root and testing design agree on 10000 unit and 2000 integration selected cases; the named tests retain their independent source assertions. Target: mcp/tests/test_landing_report.py. [1814]
- The current root and testing design agree on 10000 unit and 2000 integration selected cases; the named tests retain their independent source assertions. Target: mcp/tests/test_landing_report.py. [1815]

- The current root and testing design agree on 10000 unit and 2000 integration selected cases; the named tests retain their independent source assertions. Target: docs/design/python-pytest-bootstrap.md. [1816]


- Current targets retain the landing-report regression cases. These targets contain current source rather than an archive. The host-test policy is the design note's Python test policy. The root declaration is 10000 unit and 2000 integration cases. The root classifies scripts/agent_evals as verification. Target: mcp/tests/test_landing_report.py. [1817]


- Current targets retain the landing-report regression cases. These targets contain current source rather than an archive. The host-test policy is the design note's Python test policy. The root declaration is 10000 unit and 2000 integration cases. The root classifies scripts/agent_evals as verification. Target: docs/design/python-pytest-bootstrap.md. [1818]


- Current targets retain the landing-report regression cases. These targets contain current source rather than an archive. The host-test policy is the design note's Python test policy. The root declaration is 10000 unit and 2000 integration cases. The root classifies scripts/agent_evals as verification. Target: pyproject.toml. [1819]


- Current targets retain the landing-report regression cases. These targets contain current source rather than an archive. The host-test policy is the design note's Python test policy. The root declaration is 10000 unit and 2000 integration cases. The root classifies scripts/agent_evals as verification. Target: pyproject.toml. [1820]

- Source cases separate named renames, copies, Git metadata, full-removal threshold and proven/unproven absence.  Anchor: rename, linked-worktree and removed-card controls Target: mcp/tests/test_landing_report.py. [1821]
- Source cases separate named renames, copies, Git metadata, full-removal threshold and proven/unproven absence.  Anchor: rename, linked-worktree and removed-card controls Target: mcp/tests/test_landing_report.py. [1822]

- Current targets retain the landing-report regression cases. These targets contain current source rather than an archive. The host-test policy is the design note's Python test policy. The root declaration is 10000 unit and 2000 integration cases. The root classifies scripts/agent_evals as verification. Target: mcp/tests/test_landing_report.py. [1824]


- Current targets retain the landing-report regression cases. These targets contain current source rather than an archive. The host-test policy is the design note's Python test policy. The root declaration is 10000 unit and 2000 integration cases. The root classifies scripts/agent_evals as verification. Target: docs/design/python-pytest-bootstrap.md. [1825]


- Current targets retain the landing-report regression cases. These targets contain current source rather than an archive. The host-test policy is the design note's Python test policy. The root declaration is 10000 unit and 2000 integration cases. The root classifies scripts/agent_evals as verification. Target: pyproject.toml. [1826]


- Current targets retain the landing-report regression cases. These targets contain current source rather than an archive. The host-test policy is the design note's Python test policy. The root declaration is 10000 unit and 2000 integration cases. The root classifies scripts/agent_evals as verification. Target: pyproject.toml. [1827]

- Source cases separate named renames, copies, Git metadata, full-removal threshold and proven/unproven absence. These are source assertions and policy declarations, not execution evidence. The current test and support own the case/fixture logic. The design note declares 10,000 unit and 2,000 integration cases. The current configuration declares the same pair. Target: mcp/tests/test_landing_report.py. [1828]
- Source cases separate named renames, copies, Git metadata, full-removal threshold and proven/unproven absence. These are source assertions and policy declarations, not execution evidence. The current test and support own the case/fixture logic. The design note declares 10,000 unit and 2,000 integration cases. The current configuration declares the same pair. Target: mcp/tests/landing_report_test_support.py. [1829]

- Source cases separate named renames, copies, Git metadata, full-removal threshold and proven/unproven absence. These are source assertions and policy declarations, not execution evidence. The current test and support own the case/fixture logic. The design note declares 10,000 unit and 2,000 integration cases. The current configuration declares the same pair. Target: docs/design/python-pytest-bootstrap.md. [1830]

- Source cases separate named renames, copies, Git metadata, full-removal threshold and proven/unproven absence. These are source assertions and policy declarations, not execution evidence. The current test and support own the case/fixture logic. The design note declares 10,000 unit and 2,000 integration cases. The current configuration declares the same pair. Target: pyproject.toml. [1831]
- The retained landing-check method invokes instruction renewal with the running interpreter. [1833]
- Current fixtures compare body-only and final-trailer attribution with Git, exercise registered weakness writes and both reads across closure states and episodes, and assert that public closeout commits the judged memory tree without rewriting the reviewed record. These are source assertions, not a fresh execution or settlement of a live weakness. [1834]

- Startup compacts the river and schedules projection and enabled recurring owners before yielding. The shutdown fixture substitutes projector priming and identifies the archive-recovery coroutine. Archive recovery bounds each scan by entry count, depth and time. The installer lists retired Observer stores. Serving adds watcher health to a copy of the projection. [1835]



- The plugin registers one in-memory turn tracker and forwards agent.turn.after with turn identity and outcome. A completed eligible silent end arms a sixty-second wait. A new turn cancels that wait and delivery checks current host facts. A failed held-line send stays queued for ordered retry. Helper and background declarations go through wait tracking and scheduling. [1836]



- test_definition_scope.py declares focused checks for scope reuse, fresh operations and source-content identity; this is source-described coverage, not a new test execution. [1837]

- The definition-scope tests check native MCP, finite CLI, dashboard and detached quality boundaries. The journal cases distinguish request-local reuse from process ownership. [1838]


- The build-identity tests cover loaded-build isolation, reuse after restart, private unknown-build reads, cold lookup contention, failure and retry, and temporary-file eviction. [1839]

- test_curator_coherence_measured_quality.py declares focused checks for unchanged quality after publication, measured-binding invalidation and historical record readability; this is source-described coverage, not a new test execution. [1840]

- Task-context endpoint cases retain a measured source inventory when knowledge is wholly unavailable or one knowledge half is damaged; both named-subject requests refuse with 404 candidate_dataset_absent. [1659]

- The catalog-census test checks equality between governed and cataloged artifact paths and equality between declared and referenced contract IDs. [1731]

- The frame-store restart case opens the latest revision through a fresh store after ten publications and checks retained revision usage. [1788]

- The mounted planned Build regression checks the words delivered to the seat. The direct service test separately checks the wording when passed planned history. [1841]

- The landing answer matrix measures both states across five controlled delivery shapes. The shared guard regression checks the current drop count after scalar removal. [1842]

- The integration lane registers the crossing dependent writer test once. [1844]

- The current unit-regression lane selects test_knowledge_leaf_read.py. The current lifecycle catalog declares test_knowledge_leaf_read.py as an exact consumer of mcp/tests/_user_settings_guard.py, mcp/tests/anchor_fixture_models.py, mcp/tests/fixtures/repository_profiles/node/package-lock.json, mcp/tests/knowledge_index_test_support.py, mcp/tests/knowledge_rows_test_support.py. These current declarations establish no test execution or acceptance. The `anchor_fixture_models.py` artifact row declares `test_knowledge_leaf_read.py` as an exact consumer. The `fixtures/repository_profiles/node/package-lock.json` artifact row declares `test_knowledge_leaf_read.py` as an exact consumer. The `knowledge_index_test_support.py` artifact row declares `test_knowledge_leaf_read.py` as an exact consumer. The `knowledge_rows_test_support.py` artifact row declares `test_knowledge_leaf_read.py` as an exact consumer. [1445]
- The current lifecycle catalog declares test_knowledge_leaf_read.py as an exact consumer of mcp/tests/_user_settings_guard.py, mcp/tests/anchor_fixture_models.py, mcp/tests/fixtures/repository_profiles/node/package-lock.json, mcp/tests/knowledge_index_test_support.py, mcp/tests/knowledge_rows_test_support.py. These current declarations establish no test execution or acceptance. The `anchor_fixture_models.py` artifact row declares `test_knowledge_leaf_read.py` as an exact consumer. The `fixtures/repository_profiles/node/package-lock.json` artifact row declares `test_knowledge_leaf_read.py` as an exact consumer. The `knowledge_index_test_support.py` artifact row declares `test_knowledge_leaf_read.py` as an exact consumer. The `knowledge_rows_test_support.py` artifact row declares `test_knowledge_leaf_read.py` as an exact consumer. [1446]
- The current mcp/tests/evidence-lifecycle.toml declares schema_version = "ar-test-evidence-lifecycle/v3", 18 contract records and 120 artifact records. These are source declarations, not test execution, code delivery or acceptance evidence. The current mcp/tests/test-evidence-lanes.toml selects 795 distinct test modules across its lane identities. [1498]
- The current mcp/tests/evidence-lifecycle.toml declares schema_version = "ar-test-evidence-lifecycle/v3", 18 contract records and 120 artifact records. These are source declarations, not test execution, code delivery or acceptance evidence. The current mcp/tests/test-evidence-lanes.toml selects 795 distinct test modules across its lane identities. [1529]
- The current mcp/tests/evidence-lifecycle.toml declares schema_version = "ar-test-evidence-lifecycle/v3", 18 contract records and 120 artifact records. These are source declarations, not test execution, code delivery or acceptance evidence. The current mcp/tests/test-evidence-lanes.toml selects 795 distinct test modules across its lane identities. [1530]
- The evidence registry has twelve exact-consumer rows that name `mcp/tests/test_terminal_blocker_reasons.py`. [1638]
- The current mcp/tests/evidence-lifecycle.toml declares schema_version = "ar-test-evidence-lifecycle/v3", 18 contract records and 120 artifact records. These are source declarations, not test execution, code delivery or acceptance evidence. The current mcp/tests/test-evidence-lanes.toml selects 795 distinct test modules across its lane identities. [1647]
- The lifecycle catalog declares test_landing_report.py among the consumers of _user_settings_guard.py, curator_coherence_test_support.py and the Node package-lock fixture; this named subset is not its whole declared artifact population. These are declarations and source assertions, not a fresh run. The `curator_coherence_test_support.py` artifact row declares `test_landing_report.py` as an exact consumer. The `fixtures/repository_profiles/node/package-lock.json` artifact row declares `test_landing_report.py` as an exact consumer. ENVELOPE_LOSING_RAISERS is empty. The sweep compares its observed error-arm population with that pin. No executable STATE_DEPENDENT_RAISERS or ambient lifecycle-state matrix remains in the sweep support. None remains in the entry-point world. None remains in the sweep module. lifecycle_finalize_task has an ordinary contract-addressed dry-run request in the main benign table. [1723]
- The current lifecycle catalog declares test_landing_report.py as an exact consumer of mcp/tests/_user_settings_guard.py, mcp/tests/curator_coherence_test_support.py, mcp/tests/fixtures/repository_profiles/node/package-lock.json, mcp/tests/landing_report_test_support.py. These are source declarations, not invocation, code delivery or acceptance evidence. The `curator_coherence_test_support.py` artifact row declares `test_landing_report.py` as an exact consumer. The `fixtures/repository_profiles/node/package-lock.json` artifact row declares `test_landing_report.py` as an exact consumer. The `landing_report_test_support.py` artifact row declares `test_landing_report.py` as an exact consumer. [1753]
- The after-discovery test source asserts one joint sweep/dashboard start across scheduling and no-list fallback in fresh autoStart=true processes. The launchers and reconciliation seam are recorders; no execution is asserted here. The parsed lifecycle catalog contains 18 lifecycle contracts and 120 artifacts. The parsed lane catalog contains 795 selected lane members. [1808]
