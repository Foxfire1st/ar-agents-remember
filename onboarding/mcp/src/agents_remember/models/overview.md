# Response Contracts, Shared Wire Values, And Text Knowledge Models

## Governing Overview
[mcp/overview.md](../../../../overview.md)

## Purpose

Capsule operation selection now carries an explicit all/sections audience contract. Sections-mode validation examines the complete source before projecting common and addressed text. Declared step-detail references carry source, revision, bytes and named step separately from inline blocks; the selected-content seal does not change their original source revisions or tool grants.

`mcp/src/agents_remember/models/` owns named contracts shared by MCP responses, serving projections, task and lifecycle owners, capsule compilation, and knowledge readers. It supplies strict package-owned shapes, deliberately flexible detail envelopes, closed vocabularies, immutable identities, and pure construction predicates. Model validation establishes the declared shape and the consistency checks actually implemented; it does not establish observed runtime authority, successful execution, semantic truth, publication approval, or recovery.

The governing route is `mcp/overview.md`. `models/tools/` remains governed here. Responsibility-specific packages include `role_capsules/`, `knowledge_files/`, `closeout/`, `queue/`, `lifecycles/`, `structural/`, and `certification/`. These homes separate stable values from the application, storage, selection, and mutation owners that use them.

Knowledge is text in Git after MIK-R26. `knowledge_files/` owns the record, onboarding-sidecar, census, and history formats. `knowledge/` retains reader vocabulary, source locators, revision aggregate mappings and digests, comparison values, and review displays. Its facade does not export the former canonical database command batch, stored-anchor writer, snapshot-publication commands, or composition commands. Retained operation/refusal spellings and reader-oriented draft values do not restore those APIs.

## Hot Path Summary

MIK-R109 wire contracts name knowledge, not its text. `NamedFile` carries existence, card location/state/counts and per-row limitations/refusals; `NamedRecord` identifies actionable records and exact heading or explicit title fallback. `ReadArFilesResponse` carries call-local overview locations and code/memory observation state, not source/card/overview bodies or `published_intent`. `SlimContextPacket` is the version-3 agent roots/task/actions/build/pair shape beside the retained full `ContextPacketV2` builder contract. Knowledge-read rows carry text ID/kind/state/location with selection provenance; diff answers carry compared trees, counts, bounded decision records and whole-report location. `resolve_context` is removed from the public roster/response route, and all four L109 reads have final answer bounds, not interim rows.

A tool result is first validated through `tools/tool_registry.py::TOOL_RESPONSE_MODELS`. `tools/tool_response.py::finalize_tool_response` optionally enriches the validated envelope, serializes it with absent optional fields omitted, and finalizes token accounting. The application boundary then constructs the answer delivered to an agent: `application/tool_response.py::complete_tool_response` selects a supplied compact answer or, by default, strips `tokens`, `tokenizer`, `tokenCountExact`, and `operation` and truncates long lists from the finalized whole result. It translates the selected answer's `nextStep` into `next`, records the whole result where possible, and applies the delivered-answer bound. A supplied projection does not automatically inherit whole-result enrichment. Dashboard and command-line consumers retain the whole-result path. Consequently, token fields belong to the modeled whole result and log accounting; they are not promised on the delivered agent answer.

tools/public_roster.py owns the advertised 41-name tuple and tools/tool_registry.py maps current names to their response models. Both are model-layer wire vocabulary, not live execution or advertisement. Native role start/set/message, receipt-tracked retirement and knowledge read/diff/integrity remain; removed terminal, inbox, gate, readiness, manager-nudge and internal spawn response registrations do not survive here.

The current public source roster has41 names: the 40 after dispatch_agent removal plus the mounted knowledge_write; the41-name L109 composition and pre-sync R11142-name account are historical. SHAPED_TOOL_BOUNDS carries final task/landing/role delivery rows, including direct_execution_grant at150 tokens with no raw interim-map entry. Some other shaped tools retain raw L111 interim-map spellings, so final assembled rows, bound lookup and interim_leaf_for are not interchangeable observations. TaskDocResponse is the rich whole model: removed-read refusal alone may lack parsed identity, successful writes still require it, checklist-read models/steps are gone, and optional phrase, by-file, synchronization-error and fact-report fields support surviving operations. WorktreeSummary adds an optional taskDocumentCopies notice, not exhaustive copy equality or mutation permission. Model declarations and illustration labels are not universal observed maxima or acceptance.

> **Retained historical source account — superseded by the current route account:**
> A tool result is first validated through `tools/tool_registry.py::TOOL_RESPONSE_MODELS`. `tools/tool_response.py::finalize_tool_response` optionally enriches the validated envelope, serializes it with absent optional fields omitted, and finalizes token accounting. The application boundary then constructs the answer delivered to an agent: `application/tool_response.py::complete_tool_response` selects a supplied compact answer or, by default, strips `tokens`, `tokenizer`, `tokenCountExact`, and `operation` and truncates long lists from the finalized whole result. It translates the selected answer's `nextStep` into `next`, records the whole result where possible, and applies the delivered-answer bound. A supplied projection does not automatically inherit whole-result enrichment. Dashboard and command-line consumers retain the whole-result path. Consequently, token fields belong to the modeled whole result and log accounting; they are not promised on the delivered agent answer.

> Retained L109 incoming interim-policy account; finalized L111 shaped bounds below supersede its L1114000 claim:
> The answer policy is presently mixed rather than uniformly final: L100's `retire_child` and `role_start_set`, and L111 tools, retain named interim rows at 4,000 tokens; `role_message` and `server_info` have explicit 4,000-token exceptions. L110 memory/coherence tools now have `SHAPED_TOOL_BOUNDS` between 400 and 1,500 tokens, including 850 for curator coherence. Retained drift/migration bound entries do not advertise removed tools. L112 final rows assign `runtime_install` 600 tokens and `dispatch_agent` 1,500. Lookup checks exceptions, shaped bounds, interim ownership, then finalized task rows (including L109 and L112), and otherwise returns the 4,000-token net. General lists have a 20-entry cap; status projections use a 10-entry cap where selected, and overflow has a separate 400-token short form. These are source declarations, not a fresh measurement that every delivered answer meets them. Logging failure is reported without failing the underlying call.

> **Retained historical source account — superseded by the current route account:**
> Historical pre-L113 registry account, not current membership or response-registry evidence: `tools/public_roster.py` declared the advertised tuple once, independently of live registration and response-model registration. Its then-current literal contained 41 names, including the added `retire_child` and `role_start_set`; their response models are registered without restoring the other retired operations. `PUBLIC_TOOL_RESPONSE_MODELS` filters the full registry by the explicitly declared internal compatibility names. Those internal rows include trusted session, inbox, gate, readiness, and manager-nudge builders; their presence does not advertise public tools. The public knowledge family is `knowledge_read`, `knowledge_diff`, and `knowledge_integrity_check`. Provider operations, the former knowledge mutations/projection, and status-change wait are not entries in the present public tuple.

> **Retained historical source account — superseded by the current route account:**
> The answer policy is presently mixed rather than uniformly final: L100's `retire_child` and `role_start_set`, and L109/L111 tools, retain named interim rows at 4,000 tokens; `role_message` and `server_info` have explicit 4,000-token exceptions. L110 memory/coherence tools now have `SHAPED_TOOL_BOUNDS` between 400 and 1,500 tokens, including 850 for curator coherence. Retained drift/migration bound entries do not advertise removed tools. L112 final rows assign `runtime_install` 600 tokens and `dispatch_agent` 1,500. Lookup checks exceptions, shaped bounds, interim ownership, then L112 final rows, and otherwise returns the 4,000-token net. General lists have a 20-entry cap; status projections use a 10-entry cap where selected, and overflow has a separate 400-token short form. These are source declarations, not a fresh measurement that every delivered answer meets them. Logging failure is reported without failing the underlying call.

Contract guidance preserves an explicit producer `nextStep`; otherwise the application resolves the response's own contract. The two preview approval stops may use the exact same call's `contract_path` argument and remain summary-only. Actionable guidance that names a contract is withheld when the response has no address or any supplied spelling fails to identify its contract file or immediate containing directory. Guidance without an artifact address can remain. No ambient-session guidance or declared `agentNotifierBanner`/`supervisorBanner` envelope fields remain.

Memory-tree reads carry their selected tree/index, completeness and bounded continuation, plus reader-owned proof, currentness, family, and route-chain blocks when applicable. Git-tree knowledge diffs carry exact revisions, bounded patches and omissions; text-tree integrity reports carry validator inputs, findings and optional leaf worklists. These observations establish neither semantic effect nor code approval.

## Construction And Ownership

DirectExecutionGrant is external task-local authority; observer directGrant is display-only. Direct response adds candidateTree/candidatePaths/codeCommitMessage facts, and lifecycle direct input carries exact canonical leaf plus prospective codeBefore. No task-document flag or anticipated commit hash is introduced.

The recorded-meaning review models separate eligible steps, readable none and unavailable history. Each step keeps authored effect and own judged revision; old family omissions remain explicit and half-recorded rows are invalid. Subject payloads require the field, task context supplies it empty, and outline labels carry the same state/order independently of change-kind facts.

> **Retained historical source account — superseded by the current route account:**
> Memory-quality response codes reach the shared shaping guard without a model length ceiling; malformed/over-long codes are converted there with whole-result custody, not raised first. The current tool-answer interim map explicitly assigns `direct_execution_grant` to L111. No response-model, tool-roster or semantic-acceptance owner moves.

**Envelope and vocabulary ownership.** `base.py` distinguishes `extra="forbid"` package-owned contracts from `extra="allow"` intentional detail surfaces. Both envelope families declare `ok`, token metadata, optional producer/contract `nextStep`, answer-carried `next`, and optional log location/error, without the removed notifier banners. Flexible envelopes also recursively reject the reserved snake-case decision keys, preserving the camelCase decision vocabulary without rejecting unrelated detail. `ResponseEnvelope` names their union. Nullable fields omitted by `exclude_none=True` need optional defaults. Inherited policy requires explicit nested owned models, or a narrow `model_validate` adapter, rather than silently treating arbitrary dictionaries as owned contracts.

The enduring vocabulary rule is one declaration consumed by producers and readers. Ownership can be at a producer or at this lower wire layer when importing the producer would create a cycle. Worktree lifecycle and guidance aliases now live in `models/worktree.py`; Git state/freshness and readable memory mode are imported from their kernel owners. The leaf-reference refusal vocabulary (`LeafRefStatus`) and its type-derived `VALID_LEAF_REF_STATUSES` membership set are owned by `worktrees/leaf_refs.py`; no model in this package consumes them. The historical drift-repair examples explain why a copied status set can reject a producer's real payload after its operation already occurred; they do not establish present exhaustive coverage.

`ContextPacketV2` owns compact startup context, with storage path rules nested in the memory storage shape rather than duplicated at top level. A retained inconsistency needs explicit description: `ContextDiagnosticsHint.providerDiagnosticsTool` still defaults to `provider_diagnostics`, while that name is absent from the public roster and response registry. This default is present schema wording, not an actionable public-tool recommendation. Provider summary/detail models may survive without making deleted provider tools public.

**Offline token accounting.** `tokens.py` constructs the default exact `o200k_base` counter at module scope. Before loading the encoding it verifies the shipped vocabulary's presence, supported encoding name, and SHA-256. Only then does it temporarily point `TIKTOKEN_CACHE_DIR` to the verified file's parent, under a reentrant lock, restoring the previous environment value afterward. The filename is derived from the source URL's SHA-1 cache key. Verification must precede the library load: the inherited intent is to refuse missing or byte-wrong package data rather than permit a startup download or rewrite. The lock coordinates participating callers only; unrelated threads can still observe or modify the process-global environment. `ApproximateTokenCounter` exists as a separately selectable implementation, but the default exact counter does not automatically fall back to it on vocabulary failure. Whole-result accounting includes its metadata through a stable-count loop.

> **Retained historical source account — superseded by the current route account:**
> **Task, structural, and native role identities.** `TaskDocumentRef` is a frozen repository-qualified JSON task-document identity, hashed by repository and normalized confined path. Repository identity prevents cross-repository collisions; task altitude remains topology-owned. `TaskScopedReaderContext` adds the canonical absolute enclosure contract address rather than a provider actor/workspace identity. `task_document.py` owns `MasterExecutionNature` (`organizational|atomic`). Structural agent/gate contracts separate public task/role outcomes from internal runtime correlation and occupant identity.

`role_agents.py` and `role_launcher.py` own single/set role starts, messaging and launcher request/response shapes. Start/message status vocabularies admit product-held state; set responses carry per-seat results, and message responses carry held-message identity and waiting counts. Calls declare replacement and held-message withdrawal operands. These fields do not confer caller-controlled permission policy: the shared launch selector refuses permission-bearing feature overrides. `structural/agent.py` separately restores `RetireChildRequest` and `RetireChildResponse` for native receipt-tracked retirement; original-starter authorization belongs to `cli/role_retire.py`. The inherited native-launch intent separates canonical task/workspace identity, explicit requested model/effort/mode/feature choices, per-choice provenance, and actual host observations. Requested immutable `sessionOptions` are not proof that the host observed mode or service tier. Dynamic validation and launch/replay behavior belong to the native launcher owners, not these schemas. This proposal does not independently certify that full launch path.

The removed terminal/dispatch DTO family is not a current model home. Native role launch request/response and receipt-owned retirement remain separate retained models; their structural identities do not become a promise about removed carrier, terminal readiness or dispatch-brief transport.

**Lifecycle, closeout, and publication contracts.** Lifecycle models retain generation, enclosure, legal control, successor, termination, mutation, preparation, recovery and bounded legacy evidence separately from disposable scheduling projection. The strict internal operation record may hold fingerprints, candidate trees, process identity, approval claims and recovery detail; its public projection states the exact journal identity (contract path, generation, record revision and candidate/plan/identity digests), task intent, result, failure and guidance text, an approval `claimed|unclaimed` observation, a worker liveness observation, a recommended action, legal controls and projection effects, while process and lease authority stay internal. Root-journal evidence is not replaced by a queue projection. `queue/` is the waiting-door request/response surface, while `closeout/projection.py` owns its scheduling vocabulary; earlier selected/in-flight/certified queue accounts are historical.

`closeout/input.py`, `source.py`, and `projection.py` respectively own accepted input, exact candidate provenance, and scheduling facts. The inherited input contract distinguishes raw messages, resolved plans, enabled/not-applicable legs, and structured refusals; below validation there should be no invented subject or blank sentinel. Memory-content attribution belongs to `kernel.memory_attribution.render_memory_content_message`, reached by closeout through its effective-input wrapper: preserve the authored message and append the exact landed code commit trailer. Code and memory outputs remain distinct from informational `ledgerCache` refresh. `memory_content_excludes.py` declares `memory.md` and `bootstrap` once as worktree-relative names; these are not pathspec strings. The inherited account says the ledger is a rebuilt cache with no current ledger-only commit producer, and unattributed historical commits yield no computed mapping. A stale comment in the exclusion module still mentions its own transaction; that comment alone does not establish a present producer.

Atomic-series activation is contract-scoped, not protected-source-pair-scoped. Its strict v2 record carries the contract fingerprint, selected master, canonical contract path, revision, time, and state. The present record state admits `vacant` as well as `reconciling|active`; the separately declared selection vocabulary admits only the latter two, and observed state additionally admits `unreadable`. This is disposable selection, not task truth or lifecycle acceptance. Independent atomic masters sharing a protected pair must not overwrite one another's selection. Worktree activation/admission projections explain the addressed contract's state and corrective action; a foreign live master is not this contract's blocker. Real predecessor dependencies remain execution-graph concerns. Sync projections retain resolution, resume, cancellation, completion, malformed/identity-invalid evidence and bounded quarantine; exact refs, admitted heads and per-side progress remain journal-owned durable facts.

Curator coherence keeps requirement revision, delivery attempt, source candidates, authored judgments, immutable generation, stable authority and optional attempt snapshot separate. `status|prepare|publish|validate` is closed. The nine identity/publication members are declared once and drive validation, refusal wording and prepare guidance. Optional `judgments_file` transports judgments and assessments without joining that required identity set; the request shape refuses this content on non-publication actions, and the publication owner refuses explicit inline/file duplication, including explicitly supplied empty lists. Response models add candidate counts by kind, candidate-set digest/file locations, publication counts and the judgments-file SHA-256. Transport changes supply neither semantic judgments nor acceptance authority. Judgment coverage is unique and exact over source candidates; assessments are a separate optional collection outside that coverage obligation. Publication-only input is refused for non-publication actions, and only publication may freeze an attempt snapshot. `MemoryCandidatePairIdentity` is shared rather than copied by quality, coherence and closeout contracts. Certification primitives, corrective dispositions and exact stored-object references live in `certification/`; registry/plan compilers and certificate storage retain semantic and storage authority. `test_evidence.py` makes candidate-bound certifying evidence opaque to ordinary construction and requires the verified Dagger publication capability for accepting consumers. Diagnostic output is not acceptance evidence.

`ServingBuildPayload` is the shared strict boot identity for dashboard and server information: version and boot time are required, while exact content/build/interpreter/package/commit/dirty observations may be absent. A version alone is not an exact candidate identity. Master retirement and sprint execution-edge models separately describe archived proof, removed linkage, affirmed graph edges, reasons and source digests; declaring that proof does not perform retirement.

**Capsule and skill construction.** `role_capsules/` separates manifest parsing, exact scope selection, bidirectional source-set admission, instruction resolution, tool narrowing and compilation. Declared role/operation vocabulary constrains manifest edits; no nearest-match selection or fallback operation is intended. Resolution collapses byte-identical duplicates and refuses equal-authority contradiction. Admitted input, semantic content and diagnostic output stay structurally separate: timestamps, unselected sources, conflict rows and refusal text do not enter the semantic digest.

Tool requests are narrowed against admitted policy and cannot grant new capability. Skill references are a distinct channel: every declared skill is carried as an origin/identity/URI/content-revision pointer to admitted root content, without applying tool-grant policy. No declared skill may silently disappear. The digest includes manifest schema, seat/role/operation, repository/work branch, task/document/requirements, composed specializations, ordered block identities/revisions, requested tool identities, skill identities/revisions, and verified task-context identity when supplied. Order contributes to identity. Empty or non-UTF-8 admitted instruction sources use typed capsule source refusals; emptiness can be discovered during actual composition after admission.

`role_capsule_resources.py` and `skill_resources.py` own response/discovery formats, origin-plus-name identity, declared provenance and server-supplied-data trust statements. Enumeration returns references and metadata rather than opening bodies; an observed declared tool set is not applied permission. These model owners do not import the MCP protocol layer. The removed Eve carrier has no current parsing, serialization or environment-vocabulary contract. Retained LaunchCapsule values carry compiled instructions; native writer/launch consumers own their actual reading, delivery and execution admission.

**Text knowledge construction.** `knowledge_files/documents.py` maps the twelve record kinds, layout marker, file/route sidecars, history and four census schemas to models and refuses unknown schemas. `FileModel` is frozen, extra-forbidden and alias-serialized, and refuses explicit null keys at its model boundary. Canonical formatting is formatting only; it must not silently change content. IDs distinguish minted six-character suffixes from legacy-derived eight-character suffixes; slugs are display rather than identity. Each relationship has one owning record/sidecar surface, rather than duplicate second-owner fields.

Repository paths use the confined plain-Git-path rule. `RoutePath` alone also admits `.` for the root route; inherited intent permits a family there only when no narrower home exists. That semantic placement policy is not inferred from the type's ability to represent `.`. Leading-colon pathspec magic is refused, while literal glob characters are permitted as names. Anchor content identity is `sha256:` over the exact blob bytes: one-based inclusive line ranges preserve each terminator and split on newline only; whole-file anchors use all bytes; symbol resolution supplies a range to this shared hasher. It never decodes the bytes to establish identity.

Admission meanings remain `spans_locations`, `guarded_by_test`, `family_guarantee`, `prevents_costly_mistake`, `joint_guarantee`, `real_alternatives`, and `constrains_future_work`. Mechanical support for the first two uses sidecar realization/proof facts; reviewer judgment owns the others. An exported record is recognized by a legacy identity that actually derives its record ID, not mere `legacyId` presence; decisions receive no export exemption. Census baseline, inventory, claims and route-status formats retain provenance and distinguish import disposition from authored semantic assessment. Root route slug is `@root`; claim IDs use `CLM-` plus six Crockford characters; latest status across censuses governs. Pinning and append-only checks belong to the validator rather than format construction.

History files are leaf, wave or crossing-owned and contain one row per subject. The registry retains invariant, family, onboarding_trace, planned, unexplained and reconsideration and adds membership and record. Invariant/family dispositions keep their covered-entry/examined-member obligations and governing changed-or-retirement rule. Reopened files merge by attempt, with later subjects superseding earlier ones. The merged latest-file closed flag is not each winning row's provenance: winning_row_closed computes those own-file flags separately. Closed-base history stays frozen, and unchanged-revision changed rows remain restatements rather than a new arbitrary judgment.

Onboarding trace rows allow updated/no_impact and writer-filled SourceBlob bindings. Each SourceBlob has a repository path and lowercase hex object token or absent sentinel; source paths are distinct. Updated requires sources in the model, while old sourceless rows remain syntactically readable and answer only in their own closed files. The normal gate checks source equality and counted Markdown/nonmechanical references, not realizes/proves-only changes. Crossing markers retain their structured list and root subject onboarding:overview. L53's rollout exception permits its own measured changed card through the old producer with no invented updated/no_impact row or later backfill. Planned effects retain their disposition-specific references, of which the writer resolves the requirement, decision, invariant and row forms; a deferred `ref.leaf` is only checked for `OwnerId` shape and is not resolved to an existing follow-up leaf.

Unexplained hunk identity is changed-line based; nontext subjects bind the candidate object or absence. The pure helper reads a subject-to-row map but does not establish row currency or count a card edit. Covered items keep no_invariant; uncovered items use the application gate's typed current onboarding answer, so an elsewhere source edit can reopen that answer without changing hunk identity. Unreadable sidecars or unstated coverage do not pass. Reconsideration subject/index, still_rejected/raise forms, refreshable triggers and derived decision supersession remain separate rules, not substitutes for onboarding currentness.

MembershipRow names membership:<invariant> with no_family, current candidate revision and distinct considered family IDs; it cannot answer a listed invariant. RecordRow names a decision/facet at candidate revision: changed requires effect, retired requires retire, no_impact forbids effect and because is optional. Unknown-subject checks resolve the membership invariant and record subject. These candidate schemas are not authority to write new kinds through an unsupported main-line producer.

The reconsideration satisfying function accepts `superseded=frozenset()` after its item and rows.
A matching row closes an item only when no changed fact carries the `refresh_not_current` trigger,
which returns the item open before the row map is consulted; without a row, a valid reconsideration
subject also closes when its decision ID belongs to the supplied superseded set. The empty default
preserves two-argument
behavior. Supersession is derived, never stored; subject spelling, triggers, dispositions, row kinds
and decision status schema are unchanged. MIK-R148 rule3 is pure-function plus fresh-run agreement:
the worklist supplies both-side context and omits superseded items before judging, while the registered
gate wrapper does more than rows-only calling: `reconsideration_row_open` hands the candidate, code and
rows to `reconsideration_gate_reason`, which derives candidate supersession and measures each refreshed
anchor before calling the satisfying function with that superseded set. A manually constructed old item
is not promised closed by that wrapper.

**Reader and review construction.** Recorded-scope seeds distinguish path, invariant identity/revision and family identity/revision; they carry no scoring or inferred relevance. Context binds namespace and snapshot, and source resolution requires both repository root and code tree. A missing task reference is a supported planning read. Counts partition total/cumulative returned/remaining, and page completeness agrees with continuation presence. Shared `knowledge-continuation/v2` tokens use `kc2.`, bind tree, response/view, seed/order, policy/version, manifest, position, threshold and optional code tree, and queue at most 64 seeds without a local path. Queue overflow is the named `seed_queue_exceeded` boundary. Scope, view and comparison cursors retain their separate contracts; rebinding cannot silently combine different revisions.

`classification.py` separates authored provenance from registered versioned mechanical rules; no mixed/default provenance or semantic rank is intended. The three retained views are source context, invariant and family. Their bounded completeness is within declared scope, not project truth; not-applicable quantities carry reasons rather than invented zeroes. `KnowledgeViewReader` supplies snapshot/count/row/membership/anchor observations rather than letting a renderer open storage. Membership has its own method because it is not interchangeable with generic record rows. A source-path seed uses `PathSeed`; absent restriction differs from a measured empty realization set. Realization display rows can carry authored role, path and locator without inferring them. `ReadArFilesResponse` declares named files, call-local overview locations, memory/code state and refusal fields; it has no `published_intent` or source/card/overview body carrier. Its naming response is separate from the bounded `knowledge_read` views and has no continuation or per-session delivery state.

Review models display records owned elsewhere and define no new record kind. `review.py` re-exports focused vocabulary owners, including `review_refusal.py`; the surface version remains `knowledge-review-surface/1`. Task context is a meaningful absence of a subject selector/comparison, tied to `not_compared`, while the source inventory still records the bound code pair. Present text, absent/binary/unresolved source, measured/partial/unavailable inventory, exact unrepresentable path bytes, and mode/content changes stay distinct. Inventory and attribution counts must reconcile. Attribution uses changed paths and disjoint exhaustive buckets; source movement is separate from authored obligation movement, and a diff is not a semantic effect finding. Text-record statement replacement is represented by removed/added transitions rather than an invented predecessor relationship.

The subject catalogue carries invariant/family identity, label and `before_only|after_only|both` presence rather than a per-subject comparison count. `ReviewEntryListResult` also declares optional `ReviewOutline` beside its entries and totals. Its current producer reads the two derived indexes for navigation identities, family titles/membership and change marks, and invariant statement summaries of at most 120 characters; it does not open source or create a second source inventory. This display addition defines no new record kind and supplies no packet authoring or acceptance authority. Total subjects sum invariant and family totals, cover the returned page, and are zero on refusal. Revision selection declares compared, unresolved, added and removed states with the corresponding before/after presence pairs; ambiguous belongs to the historical five-state model, not the current union. It carries recorded heads and retained revisions and does not select by timestamp, similarity, rank or latest label. Movements name their recorded pairing basis, both sides or a reasoned transition, and displayed-side gaps; missing identity requires an explicit gap. Rename inference is labeled Git detection and separates measured pairing, measured non-pairing and unmeasured inference. Relationship collections can include associations without source addresses.

Current tree review requires the judgment pane rather than projecting supporting-record channel bags, curator-assessment displays or applicability summaries. The pane carries this leaf’s selected-subject history rows in attempt order and proof entries with authored facets and after-code currentness; these are not executed proof results or inferred semantic conclusions. Measured no judgment and unreadable history remain distinct. Task context has no selected knowledge subject and reports unavailable judgment rather than an empty successful collection. The judgment model requires nonempty rows exactly in its rows state and keeps proof currentness separate from execution.

Historical pre-L57 record-availability/applicability DTO account, not a current tree-review payload: Record availability retains six classes and five states: recorded, none-recorded, unavailable, not-measured, not-selected. Counts exist only for counted answers; positive/zero requirements follow the state, and unanswered channels name what would produce an answer. An unreadable individual remains named beside available siblings. Applicability labels require their recorded references, keep direct/historical subject identity explicit, and partition every supplied record across six treatments. Related family context carries true subject, recorded relationship, author/role and references without importing judgment content. An absent optional treatment means unstated treatment, not unrelatedness.

Lifecycle assessment currentness remains a separate contract, not a tree-review assessment-display channel: failed measurement is unavailable, a measured disagreement is stale even if other axes remain unmeasured, complete matching coverage is current, and missing coverage is not-measured. The low-level equality comparison remains separate from this measurement-aware projection. Subject counts partition entries and derive status in stale → unavailable → unresolved → not-measured → current precedence; no recorded assessment is the separate none-recorded state. The former tree-review assessment display is removed; this does not retire authored lifecycle assessment records. Submission is display-only, with stale-disable coupling; its dispositions confer no approval. Previous binding names only the replaced display, and absence supplies no invented previous generation. Recorded-history selection addresses the leaf's published record; live selection is the absent-history case.

Collection pages distinguish selection totals from walk totals and require a continuation for a remainder. Refused pages carry a separate refusal rather than zero counts. Family context distinguishes recorded/not-recorded/not-resolved/unreadable, preserves authored guarantees and exact membership occurrences, and reports a true no-family-recorded zero separately. Roster `complete` describes the walk: only a complete first page can be checked as the whole roster; a complete continued final page carries only its own share. Member-source locator states share a producer/validator rule. Anchor observations may carry resolved ranges only on exact recorded blobs; unsupported, missing, different and unrequested observations remain distinct.

Tree review retains four exact code/memory trees and optional converted-base inputs. Unavailable history and pre-conversion legacy unavailability are named rather than substituted. `same_trees` compares task/leaf, every side's repository and tree, and converted base. The side model documents committed-commit versus uncommitted-ref ownership; this local class does not itself implement an exclusive commit/ref validator, so its prose must not be promoted into a constructor guarantee or a claim about the entire call path. Focused entries distinguish recorded absence from unavailable/unresolved ranges, bound exact excerpts to 400 lines/48,000 characters, retain authored role/rationale or proof facet and currentness, and classify change as changed/unchanged/undetermined. Leaf-wide views do not fabricate focused entries.

The catalogue and changed-intent summary results additionally declare an optional nonnegative comparison number. Selected revision values retain their exact revision IDs separately from optional display versions and per-side writer observations. `ReviewRevisionWriter` distinguishes recorded, introduced, not_recorded and unavailable; its validator requires owners exactly for recorded or introduced states. These are transported provenance observations, not an additional revision-selection policy or acceptance verdict. Focused card sides carry an optional exact symbol name, and entries can carry four after-index memory values: realizing-invariant count at the located path, incoming-link count, lack of proof and open-weakness count. `ReviewEntryMemoryState` separately names available/unavailable values, the after tree and complete/partial index state or failure reason. A declared shape and optional fields do not by themselves establish that every producer has read a complete index.

`review_lane.py` owns `ReviewLaneHunk`, `ReviewLaneFile`, `ReviewLaneDestination`, `ReviewUnexplainedLane` and `ReviewLaneSummary`, preserving hunk classification, membership state, per-file reasons, destinations and changed-file buckets. Lane-summary partial/unavailable states carry no totals; the full lane's partial state retains measured-path totals and names its unmeasured scope. Exact source expansion is owned by `review_source_content.py::ReviewSourceExpansion` and its request/result contracts. These live model owners do not establish a live `SourceExplorer` or `LaneFileFocus` implementation. Change-kind models derive primary facts and marks, with unknown on unresolved range and reasons required for unknown facts/membership. Changed-intent summaries keep counted/partial/unavailable separate, sum per-kind added/removed, and leave realization-only, membership-only and unresolved outside plus/minus. These models render observations rather than selecting subjects or deciding semantic correctness.

Final-output receipt v2 binds the complete retained comparison and digest to required delivered code and memory commits/trees. Its two stored verdicts are bound or moved, with both exact candidate-tree matches required for bound. The shared helper also returns unmeasured for an incomparable channel, but that does not make unmeasured a valid v2 receipt state. Sync rebinding v2 similarly derives current/moved/unmeasured from exact captures, with memory head/tree present together. Sync-movement displays retain the source comparison and only applicable moved-channel observations. These values authorize neither clearance nor successor publication; missing observation is never a favorable match.

RoleMessageCall and RoleMessageRefusal/response models carry file-only body/attachment inputs and named file/hash/limit/successor outcomes. The existing answer exception describes bounded returned reply text with complete reply-file retention, not loss of the complete native reply. These declarations are source contracts, not proof of installed host consumption.

## Invariants And Boundaries

Preserve the inherited requirement that advertised tools, live registration and response-model ownership agree, including name-to-model assignment rather than mere set equality. `finalize_tool_response` directly indexes the registry, so a missing row is consequential. The present proposal compares source declarations only; `server_info` cannot independently prove roster completeness by repeating the roster itself. Worktree top-level next-tool guidance is validated against the public tuple. The earlier `session_retire` builder account is historical, not a current task-document response route or a reason to widen that tuple.

Owned stable fields belong in strict contracts. Flexibility is justified by intentional upstream/detail ownership, not by avoiding declaration of this package's keys. Optional defaults and omission behavior are part of the wire contract. Single vocabularies, exact identity, explicit unsupported/absent/unmeasured states, bounded resources, and refusal-versus-success distinctions must survive extraction or migration. A frozen value is not proof that storage prevents revision updates. A model's lack of I/O is not evidence that an entire operation lacks authorization, confinement, or recovery checks.

Proofs describe what a test demonstrates, not whether it passed or whether an invariant holds. Currentness uses the named code tree; no-code-tree realized invariants remain unverifiable rather than receiving HEAD. Currentness failure stays visible without refusing the read. Registration absence and selector absence are different questions, neither a no-impact judgment. Partial reads/diffs/indexes and omitted patches must remain explicitly bounded. Authored claims, mechanical observations, judgments, storage acceptance and publication approval are separate responsibilities; no structural success, empty actionability count, matching digest, or valid DTO supplies another owner's semantic verdict.

## Historical And Verification Limits

All original reference identities and excluded metadata remain under parent custody. This body replaces incremental chronology with responsibility and policy; retained old references do not acquire current proof truth. The full supplied card was read in consecutive bounded chunks and its bytes matched the supplied SHA-256. HEAD matched the supplied source commit. This was source inspection only: no tests, product imports, runtime launches, network calls, sync, publication, or edits occurred, and no fresh execution or acceptance verdict is claimed.

The KS canonical-database writer history is retired by MIK-R26, including command batches, label edits, stored-anchor construction, snapshot preparation/publication/disposal, structural dataset merge/reconciliation, portable import/export, route mutation, envelope facets, stored detection, supporting records, authored-effect/change-set composition, registered-scope/family-integrity composition, and generated projection. Its enduring intent remains distinct: resolve and compare exact admitted identity instead of trusting remembered digests; seal context and recheck below bypassable constructors; keep expected-present/expected-absent explicit; never let caller content confer authorship or acceptance; separate logical identity from frozen file identity; distinguish incomplete staging from unconfirmed publication durability; carry explicit discard authorization rather than infer disposability; and report only structural merge facts, never correctness.

Historical merge intent distinguished supplied versus unique resolved bases, complete changed-table/operation coverage, exact engine-attributed rows versus row-less referential conflicts, and non-inferred conflict counts. Retraction depended on arriving insertion rather than the code alone; row-less decisions could not overwrite, and ordered one-row reconciliation sequences retained earlier authored decisions without becoming a side-preference policy. Portable intent required exact source/destination expectation, complete empty-inclusive table coverage, verified identity separate from publication, canonical artifact validation, and no acceptance inferred from transferred accepted state. Removed routes are not resurrected by these reasons.

Historical facet, evidence, effect, detection and pipeline intent separated content from admission provenance, interpretation from verdict, stored designation from latest inference, evidence coverage claims from execution observations, preservation from effect, and grouping/actionability from closeout readiness. It retained exact opaque references, unresolved references as values, closed effect labels with split/merge cardinality, no generated semantic summary, declared scope/policy and per-side relationship provenance, explicit no-record states, and zero-actionable as necessary but insufficient. Detection distinguished both-declared/union-with-probe/trigger-only input sets, required recorded order and limitations, kept unresolved retention separate from empty manifests, and prohibited rewriting original signals on currentness reads. These are inherited semantic intentions of retired surfaces, not claims that their old constructors or producers exist now.

Named limits remain: reference numbered 199's former `candidate.py` extent is explicitly unresolved historical evidence and supplies no current command-union guarantee. External KS-R02, KS-R07, KS-R08 and Doc12/Doc13/Doc14 rulings and requirement packets were not independently inspected here. The old ICR-R24 account that the TypeScript mirror lacked movement fields is historical; present dashboard adoption was not adjudicated. The capsule ten-role digest observations, sixteen pre-existing layer violations, 165-of-213 context failures, 62/73/84-model or tool censuses, nine-to-two strict-model sweep and its dismissals in `notes/reports/260918-TSIP-L4-worker-report.md`, and twelve-versus-two merge recovery attempts are historical candidate-specific observations, not fresh acceptance. Their old reports/receipts were not inspected. The historical wire-vocabulary test module is not fresh exhaustive protection; this proposal did not collect or execute tests. Pre-cutover statements that runtime consumers were absent are historical and must not override current text-format ownership. Old native readiness, hosted-protocol, delivery, landing, quality, memory and whole-build claims likewise supply no new certification.

Legacy final-output receipts and sync rebindings remain readable under their explicit v1 classes. Their original verdicts are retained, but exact reviewed memory-tree evidence was not recorded and therefore cannot establish v2 tree-pair coverage. `worktree_status_wait` and its response are historical; a retained lifecycle wait literal is not a mounted replacement operation. Historical union sizes, source line counts, rail repairs, delivery dates, and fixture hashes describe their old witnesses only.

## Historical Reference Provenance

These retired source accounts preserve earlier intent only. Their former citation numbers are inert, not current source guarantees.

- Historical pre-L57 reference account only; the named supporting-record acquisition/availability/applicability owner is removed, not a current wire guarantee: **The availability vocabulary, its five states and the validator that refuses a favourable default.** (historical reference 4; retired in L57)

- Historical pre-L57 reference account only; the named supporting-record acquisition/availability/applicability owner is removed, not a current wire guarantee: **The owner that resolves every channel, so the vocabulary has a producer and not only a shape.** (historical reference 6; retired in L57)

`knowledge/review_evidence.py`, `knowledge/review_evidence_read.py` and `knowledge/review_frame.py` declare the packet, read-receipt and frame shapes the application owners return: comparison binding and collections, finite limits and measurements, supplemental receipts, claims and coverage, frame manifest and atomic pointer, drafts, reclamation receipts, and the opening, staleness and regeneration answers. Model validation establishes the declared shape and the consistency checks it implements; it observes no execution, truth or acceptance.

## Evidence

- The packet shapes bind one comparison and refuse an inconsistent collection or coverage count. [325]
- A frame manifest refuses an inconsistent asset digest, an unlisted entrypoint and a non-older parent. [326]

- **The refusal record the new code travels in, and the result that carries it as one of exactly two outcomes.** [2]
- The surface version that stays `/1`, with the reasoning recorded beside the constant. [3] [252]
- **The field the evidence pane gained, and the re-export that keeps the vocabulary reachable through the payload module.** [5]
- The cases that measure the vocabulary's refusals and its presence in the served wire schema. [7]
- The anchor observation and its region validator. [8]
- The member-source reference and its one locator-state rule. [9]
- **The vocabulary module's own statement of the five rules its shape enforces, and the movement with its four validators.** [10]
- The closed unions: the kinds, the side states, the transitions, the gap codes and the recorded pairing bases. [11]
- **The unresolved fact as a value, and the side whose validator refuses a recorded state without a relationship identity.** [12]
- **The labelled rename inference, whose validator ties a pairing to its state and refuses a similarity word on an unmeasured one.** [13]
- **The pane row that now carries the association beside its address, and the pane that carries the whole collection.** [14]
- The display owner that fills the vocabulary, and the traversal that builds the movements. [15]
- **The presence union on the vocabulary, beside the subject-kind union it parallels.** [16]
- **The entry value with `presence`, and the entry list with the totals and their agreement validator.** [17]
- The catalogue owner that fills these values, and the adapter that delegates to it. [18]

- The current revision-selection value declares the four-state union compared/unresolved/added/removed and validates the respective pair-presence combinations; the earlier five-state account is historical. [19]

- **The three validators that make a misreading unconstructible.** [20]
- **The pane field that carries the value, with its one-direction validator.** [21]
- **The policy that computes the value from authored heads.** [22]
- The shared route-directory type. [23]
- The family record's routes use it. [24]
- The four census schemas registered for dispatch. [25]
- The latest status entry across every census governs. [26]
- The range's bytes. [27]
- The content identity. [28]
- The onboarding-trace row and its `markers` list. [29]
- The file result's format fields. [30]
- The optional field (beside the later `currentness`, `families` and, since MIK-R05, `routeChain`) and the docstring boundary. [31]
- The one continuation token and what it binds. [32]
- The read response's page state and fields, re-read when MIK-R05 added `routeChain`. [33]
- The integrity response's optional fields. [35]
- The sync response's worklist summary. [36]
- The optional field and its docstring paragraph. [37]
- The row kind's docstring with MIK-R30's meaning. [38]
- The planned forms, the key and the gate predicate. [39]
- The planned row and its disposition-bound ref. [40]
- The invariant criteria's meanings, and which two the validator checks. [42]
- The derivation that identifies an export. [43]
- The response kinds a token pages, and the public queue cap. [44]
- The optional `families` field on the read response, followed since MIK-R05 by `routeChain`. [45]
- At least two alternatives, exactly one chosen. [46]
- Superseded is derived from later decisions' `supersedes`. [47]
- The reconsider links and MIK-R14's subject. [48]
- The ref namespace and the durable record. [49]
- The tree view's answer. [50]
- The subjects, the row subject and the gate predicate. [51]
- The no_invariant row. [52]
- The optional field. [54]
- The docstring paragraph. [55]
- The range and change states and the excerpt bounds. [56]
- One entry on one side, and on both sides. [57]
- The tree view's field for the entries. [58]
- The lane's literals: buckets, hunk classes, range reasons, membership states, gate linkage. [59]
- The lane reconciles; an unmeasured value carries no totals. [60]
- The tree view's two new fields, and the summary's. [61]
- The facts derive the primary and the marks. [62]
- The entry's facts describe exactly its returned members. [63]
- The reconsideration row retains its own subject and disposition grammar. [66]
- Public MCP payload builders validate through the response model registry. [67]
- The advertised public roster's single definition, in this route's zero-import `tools/` leaf; the adapter re-exports the identical object. [68]
- The response model that reads the roster to enforce the worktree surface's next move against `PUBLIC_TOOLS`. [69]
- The registry maps every modeled builder and the advertised public subset to response models. [70]
- Contract tests prove public tool coverage and schema generation. [71] [77]
- The record-landing envelope is declared on this route. [72]
- The checkpoint-landing envelope is declared on this route. [73]
- The checkpoint registry row sits between the integrate and record-landing rows; the record-landing row follows it. [74]
- Lifecycle finalizer response model covers the terminal task finalization payload. [79]
- Next-step computation consumes the resolved worktree contract and retains its landing approval stops, not ambient session state. [81]
- The answer boundary preserves producer guidance, permits the same-call summary stop, and bounds actionable guidance to the response's own contract address. [316]
- Strict envelope fields retain contract guidance and answer/log accounting without notifier banners. [317]
- Flexible envelope fields use the same current guidance/answer/log header without restoring removed declared banner fields. [318]
- The wire-test module documents the 165-of-213 `context_packet` baseline. [82]
- The worktree model declares the contract-cell vocabulary aliases (moved from worktrees by 260731-EFA-L9) with `MemoryMode` imported from kernel. [83]
- The worktree model declares the phase/next-operation/next-tool vocabulary (moved from guidance by L9). [84]
- Guidance consumes the phase/next-operation/next-tool aliases declared by the wire model through one grouped import. [85]
- The drift-status vocabulary and `DriftSummaryPacket` that `drift.py` and `memory.py` import. [86]
- Direct landing returns cache observations separately from commits. [87]
- Public message transport names only code and memory. [88]
- None [89]
- Strict lifecycle operation record/projection. [90]
- Queue candidate projection. [91]
- The served knowledge vocabulary as an explicit re-export list — re-cited against the working tree, which the graph half extended. [94]
- The frozen base and the refusal to rewrite a non-canonical identifier. [95]
- The invariant identity and revision aggregate, including the display-label-versus-identity separation. [96]
- The sealed payload, with the predecessor set inside the digest and the digest field excluded. [97]
- The provenance envelope and its normalized-UTC requirement. [98]
- The typed operation, refusal-code and result contract — re-cited against the working tree, which the graph, candidate-change, snapshot, merge, authored-judgment and detection halves have each extended since. [100]
- The storage owner that writes this vocabulary. [102]
- The capsule envelope keeps one shape for success and refusal, with the seat facts it established. [103]
- The requested-versus-granted split that makes the compiler's narrowing auditable. [104]
- Identity is origin plus name, and a listing cannot reach a body. [105]
- The trust statement is a constant and a declared tool set is observed, never applied. [106]
- The three registry rows that make the new names returnable. [107]
- The family identity, the immutable revision aggregate and its self-consistency rules. [108]
- The retained graph subset is exact membership and authored role vocabulary. [109]
- The two payload versions and the family payload's sealed field set. [111]
- The shared accepted/proposed rule both revision aggregates apply at construction. [112]
- The extended served surface, including the graph names. [113]
- The family module reads exact sealed index revisions; canonical writers are retired. [116]
- KnowledgeLane retains reader-context spellings; the old tuple constant is retired. [122] [130]
- The resolved context and its two consistency validators. [123] [131]
- The module-level digest the validator calls and the operation re-derives. [124] [132]
- The resolution shape that deliberately omits the dataset identity. [128] [135] [136]
- The two candidate-boundary codes and the three operations that leaf added to the served vocabulary. [138]
- The served operation union the candidate-boundary leaf joined. [139]
- The operation and refusal vocabulary this leaf extended. [153] [164]
- The facade that re-exports the whole snapshot surface as the served vocabulary. [154]
- The one code and the two operations this leaf added to the shared vocabulary. [171]
- The read sub-route module: the closed seed union, the context, the page and the cursor. [175]
- **The corrected count model and the truncated page that cannot claim completeness.** [176]
- The one operation and six codes this leaf added to the shared vocabulary. [177]
- **The shared Git-pathspec rule, with `*`, `?` and `[` admitted as literal characters.** [178]
- Current PathSeed uses the shared path rule; the stored-anchor writer validator is retired. [179]
- **The facade's ninth source, which this leaf did add to `__all__`.** [180]
- The cursor decoder the read re-exports through the facade. [181]
- The cursor encoder the read re-exports through the facade. [182]
- The nodes that hold these models to their own invariants. [183]
- The comparison sub-route module: the two sides, the request, the item, the page and the result. [184]
- **The record half and the source half, with no field that could hold a verdict and `missing_side` as a reason rather than a third change statement.** [185]
- **The binding and the digest derived from it, which is how a candidate change invalidates a continuation by construction.** [186]
- **The counts that keep the comparison total and the display total apart, and the two closed vocabularies.** [187]
- The expansion as a value, with the carried partition and its three path lists. [188]
- **The comparison's own cursor and its two functions, deliberately not the read's decoder.** [189]
- **The one operation this leaf added, and the unchanged code union.** [190]
- **The node that measures the absent verdict over the serialized response, and the node that holds the two change statements apart.** [191]
- The nodes that hold the page and result invariants: the truncated comparison and the unestablished limitation. [192]
- The two operations the route write layer added, so a route refusal names a route operation. [193] [195]
- The shipped code an inadmissible record payload is refused with — reused rather than widened, and re-cited by hand against the current tree. [194] [196]

- Historical candidate-change commands and their union were retired with the canonical database write boundary (MIK-R26); candidate.py now owns read-context identities, not that widened write operation. [199]

- **The six operations this leaf added to the shared vocabulary, and the unchanged code union.** [205]
- Condition/input-set vocabulary remains as Literal types. [207]
- **The closed conclusion-name list and the declared-field-set review that makes "no conclusion is representable" checkable rather than asserted.** [208]
- Retained mechanical observation vocabulary names granularity, scope and limitations. [209]
- **The declared-input-set discriminator contract: two sides and no probe, both sides and the probe, or one side and no probe.** [210]
- **The manifest reference and its two-state resolution, which reports an unresolvable reference with what would resolve it rather than as an empty manifest.** [211]
- **The all-required signal field set, and the `detail`-equals-rendering rule that refuses a verdict in prose as it refuses a verdict field.** [212]
- **The two operations and the one refusal code this leaf added to the shared vocabulary.** [216]
- **The recorded quotation-degree ruling, and the absence it turns on: no payload field is the operative obligation.** [221]
- The two operation members the requirement record group added, and the fact that no refusal code was added with them. [222]
- The module's own non-definition: it defines no record kind. [227]
- The three pane names, declared once. [228]
- The dispositions the existing authority accepts, published rather than owned. [229]
- The present-side-requires-text rule. [230]
- The author and examined inputs a displayed assessment must carry. [231]
- The stale/submission coupling, checked at construction. [232]
- The unassessed-is-an-absence rule for counts. [233]
- One outcome per comparison result: a payload or one refusal. [234]
- **The two reviewable subject kinds, declared here once so the transport, the entry list and the panes cannot disagree.** [235]
- **The reviewed subject as the comparison selected it: a recorded identity, its own label and the operation's count, with no field for a path, a file, a display version or a ranking.** [236]
- **The entry read's typed outcome, whose validators refuse a refused read that offers any entry, non-zero totals beside a refusal, and a total smaller than the page beside it (`ICR-R09@v1`).** [237]
- The sixth refusal code, for a subject the resolution could not name. [238]
- **The seventh refusal code, added by this leaf: the generation a listing published no longer resolves to the two code objects it bound, so there are no bytes to serve for that entry.** [239]
- **The new field, on the strict response model that declares it.** [242]
- **The owning module that decides the shape this model declines to re-declare.** [243]
- The strict envelope base the field joined. [244]
- The registry entry for the tool whose payload carries the field; unchanged by this leaf. [245]
- **The inventory's own model, with the count checked against the list and the rule that an unrepresentable path makes the inventory measured and partial.** [246]
- **The pane that now requires the inventory as its first fact, and carries the measured partition beside it.** [247]
- **The request whose selector may be absent, and the absence as a meaning rather than a default.** [248]
- **The comparison identity that states whether it compared knowledge, with the selector and both snapshot digests all-or-nothing.** [249]
- **The knowledge pane's selection state and its required reason, and the payload validator that holds it in agreement with the identity and the staleness state.** [250]
- **The third staleness state, which is the task context and not a flavour of current.** [251]
- The cases that measure the new states: a measured empty inventory beside an untouched comparison, and the structural rule that an inventory which could not carry a name is partial by construction. [253]
- **The one granularity, the three buckets, the four link labels and the three side states.** [254]
- **The partition value with its validator and its three bucket accessors, and one side's contribution beside it.** [255]
- **The two new closed-vocabulary members, and the model's own second producer of the undetermined limit.** [256]
- **The six counts declared once, and the pane that carries the partition.** [257]
- **The nine partition cases, and the unavailable-partition honesty case beside the partial-denominator case.** [258]
- The counts and their sum check. [259]
- One outcome per state. [260]
- The package map and the shape-only boundary. [261]
- The base every file model inherits. [262]
- An invariant record carries no second-owner fields. [263]
- Schema dispatch refuses unknown schemas. [264]
- The history file: one owner, one row per subject, a strict `closed` flag. [265]
- The freeze predicate. [267]
- The history schema in the dispatch table. [268]
- The history row ID kind. [269]
- The three current responses declare tree read, Git-tree diff and text validation. [270]
- All of an owner's history files read as one. [272]
- The attempt-qualified history path. [273]
- Why a row cannot govern an invariant whose revision the leaf changed. [274]
- Current imported source owns this scoped route boundary. [275] [276] [277] [278]
- A second computation over moved inputs is refused as inputs_changing; a process failure keeps its own code. [279]
- The dashboard's tokens for the codes. [280]
- Overload is its own refusal code with a true action. [281]
- The closed union of refusal codes. [282]
- The typed refusal with its code, detail and next action. [283]
- The surface version. [284]
- The overload failure carries the code reviewer_busy. [285]
- The response shape. [286]
- `TaskReopenResponse` lives in `task_doc.py` while keeping the `WorktreeCommandResponse` shape. [287]
- `worktree_checkpoint_landing` joins the `NextTool` vocabulary; its preview and refusal both emit it. [288]
- `PUBLIC_TOOLS` is one tuple with a single definition, re-exported unchanged. [289]
- The worktree response declares the next-move triple and refuses any `nextTool` outside `PUBLIC_TOOLS`. [290]
- ReviewEntryListResult gains the optional ReviewOutline field beside its entry population and counts. [291]


- Rows and supplied superseded IDs close items; default context remains empty. [292]

- The subject pattern, the triggers and the refreshed triggers. [64]
- The one spelling of a link target, and the gate's predicate. [65]
- Curator coherence keeps semantic revision, attempt, immutable record, stable authority, snapshot, and action request identities separate and exact. [75]

- Current single literal PUBLIC_TOOLS contains 40 public names and excludes dispatch_agent; native role, retirement and knowledge vocabulary remains. Source census only, no live advertisement, new CODE grade or MEMORY acceptance. [294]
- Full and public registries separate retained internal builders from public responses, including native retirement and set start. [295]
- Whole-result validation/enrichment precedes serialization and token finalization. [296]
- Completion validates the whole result, selects a supplied/default answer and translates the selected answer's lifecycle guidance. [297]
- L110 shaped bounds and L112 final bounds coexist with interim rows and exceptions. [298]
- Provider diagnostics remains a schema default despite public removal. [299]
- Offline exact default verifies bytes before scoped cache mutation; approximate counter is separate. [300]
- Refusal declarations live in a focused module and are re-exported. [301]
- Activation record state includes vacant; selection and observed vocabularies differ. [302]
- Text schema dispatch is distinct from legacy writer exports. [303]
- Shared worklist predicates preserve different covered/uncovered answers. [304]
- Measurement coverage and measured disagreement determine assessment binding status. [305]
- Tree comparison equality includes repository identity; local side fields do not implement exclusive commit/ref validation. [306]
- V2 receipt admits only measured bound/moved states; helper also represents unmeasured. [307]
- Sync currency requires both exact matches and preserves missing memory as unmeasured. [308]
- Capsule skill references and semantic digest exclude diagnostic output. [309]

- **Retained historical source account — superseded by the current route account:** The subject pattern, the triggers and the refreshed triggers. [64]
- **Retained historical source account — superseded by the current route account:** The one spelling of a link target, and the gate's predicate. [65]
- **Retained historical source account — superseded by the current route account:** Curator coherence keeps semantic revision, attempt, immutable record, stable authority, snapshot, and action request identities separate and exact. [75]
- **Retained historical source account — superseded by the current route account:** Present public roster is a single literal with 41 names and no provider diagnostics or knowledge mutations. [294]
- **Retained historical source account — superseded by the current route account:** Full and public registries separate retained internal builders from public responses, including native retirement and set start. [295]
- **Retained historical source account — superseded by the current route account:** Whole-result validation/enrichment precedes serialization and token finalization. [296]
- **Retained historical source account — superseded by the current route account:** Completion validates the whole result, selects a supplied/default answer and translates the selected answer's lifecycle guidance. [297]
- **Retained historical source account — superseded by the current route account:** L110 shaped bounds and L112 final bounds coexist with interim rows and exceptions. [298]
- **Retained historical source account — superseded by the current route account:** Provider diagnostics remains a schema default despite public removal. [299]
- **Retained historical source account — superseded by the current route account:** Offline exact default verifies bytes before scoped cache mutation; approximate counter is separate. [300]
- **Retained historical source account — superseded by the current route account:** Refusal declarations live in a focused module and are re-exported. [301]
- **Retained historical source account — superseded by the current route account:** Activation record state includes vacant; selection and observed vocabularies differ. [302]
- **Retained historical source account — superseded by the current route account:** Text schema dispatch is distinct from legacy writer exports. [303]
- **Retained historical source account — superseded by the current route account:** Shared worklist predicates preserve different covered/uncovered answers. [304]
- **Retained historical source account — superseded by the current route account:** Measurement coverage and measured disagreement determine assessment binding status. [305]
- **Retained historical source account — superseded by the current route account:** Tree comparison equality includes repository identity; local side fields do not implement exclusive commit/ref validation. [306]
- **Retained historical source account — superseded by the current route account:** V2 receipt admits only measured bound/moved states; helper also represents unmeasured. [307]
- **Retained historical source account — superseded by the current route account:** Sync currency requires both exact matches and preserves missing memory as unmeasured. [308]
- **Retained historical source account — superseded by the current route account:** Capsule skill references and semantic digest exclude diagnostic output. [309]

- The recorded-meaning review models separate eligible steps, readable none and unavailable history. [293]

- The shared predicate has a superseded-set exception without a new row kind or a change to default two-argument behavior. [311]

- History registry includes the full set of row forms. [41]
- History registry retains unexplained and its neighboring row kinds. [53]
- Registry includes membership and record. [266]
- SourceBlob and bound onboarding row validation. [312]
- Membership and decision/facet record forms. [313]
- Each winning row retains its own closed-file provenance. [314]

- Historical L111 predecessor source account (not current R113 roster); composed R113 PUBLIC_TOOLS has40 names, and no new module/handler census is asserted here. Current composed literal public roster has41 names after L109 removes resolve_context; direct_execution_grant is included in those41. The earlier42-name caption and its epoch labels below are historical, not current source counts. Earlier Curator caption retained as historical/withdrawn where it contradicts these current populations: The current public source roster has42 names. SHAPED_TOOL_BOUNDS carries final task/landing/role delivery rows, including direct_execution_grant at150 tokens with no raw interim-map entry. Some other shaped tools retain raw L111 interim-map spellings, so final assembled rows, bound lookup and interim_leaf_for are not interchangeable observations. TaskDocResponse is the rich whole model: removed-read refusal alone may lack parsed identity, successful writes still require it, checklist-read models/steps are gone, and optional phrase, by-file, synchronization-error and fact-report fields support surviving operations. WorktreeSummary adds an optional taskDocumentCopies notice, not exhaustive copy equality or mutation permission. Model declarations and illustration labels are not universal observed maxima or acceptance. [315]

- Capsule operation selection now carries an explicit all/sections audience contract. Sections-mode validation examines the complete source before projecting common and addressed text. Declared step-detail references carry source, revision, bytes and named step separately from inline blocks; the selected-content seal does not change their original source revisions or tool grants. [319]

- The response requires judgment and retains knowledge/source identity without the removed supporting-record fields. [320]
- Selected-subject history and membership rows are rendered in attempt order, with proof entries supplied separately and explicit none/unavailable states. [321]
- The regression asserts required judgment and absence of removed wire channels; this is source/assertion evidence, not a fresh test run. [322]
- Lifecycle assessment status partitions remain independently modeled; their existence does not restore the removed tree-review assessment display. [323]
- Judgment rows exist exactly in rows state; proof facets/currentness are not run results. [324]

- The catalogue declares optional nonnegative comparison identity. [327]
- The changed-intent summary declares the recorded comparison it counted. [328]
- Revision writer owner-presence validation is separate from exact selected IDs and display versions. [329]
- Entry-side symbol and entry memory values retain explicit path and count meanings. [330]
- Focused card memory availability carries the after tree and explicit index state or reason. [331]
