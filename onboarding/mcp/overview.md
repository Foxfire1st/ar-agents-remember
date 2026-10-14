# mcp/ — Agents Remember Package Overview

## Governing Overview
[overview.md](../overview.md)

## Purpose

`mcp/` packages the Agents Remember MCP transport, application composition, typed contracts, deterministic service domains, command-line adapters, and shipped runtime assets. Its purpose is to make coordination, task identity, memory maintenance, role launch, review, and paired Git publication explicit operations with named authority and refusal boundaries. Installation assets describe the installed runtime; this checkout is their source package, not evidence that an installed host has adopted this build.

The package separates transport from decisions. MCP registration and HTTP routes expose bounded typed requests; application owners resolve admitted context and compose services; models define shared wire vocabulary; kernel and domain owners implement the underlying behavior. A reported absence, an unavailable source, an unmeasured collection, an incomplete computation, and a successful empty result are different facts. Neither a finished agent turn nor a green diagnostic supplies AR review, curation, lifecycle, or Git acceptance.

The present public roster has 41 names on this successor, after `resolve_context` was removed from the rejected freeze’s 42-name tuple; older39/41 epochs are historical. It includes structural `dispatch_agent`, native `role_start` and `role_message`, task/worktree/memory operations, and three knowledge operations: read, diff, and integrity. Public `retire_child` calls the native receipt-tracked owner; retained structural retirement code is not its handler. Historical counts of 63 or 66 tools are not the present inventory. The SEP-2640 skill surface remains resource/protocol transport: `skills/list`, `skills/get`, individual skill resources, and this server's convenience `skill://index.json`. Its registrar now registers resources rather than the historical capsule/catalog tools. Serving a skill grants no capability and does not turn supplied prose into local-file authority.

MIK-R112 changes the retrieval account: harness-native onboarding and source search replace CGC/GrepAI retrieval. Generated lifecycle settings contain an empty provider map and disabled `contextProviders`, regardless of the authority configuration. Retained provider implementation does not restore public provider tools or enabled lifecycle blocks. Runtime installation retains the old-watcher stop: a failed stop is recorded with recovery information and does not abort the install.

## Hot Path Summary

MIK-R109 changes agent reads from document carriers to names. `read_ar_files` accepts up to twenty path strings and names governing cards, states/counts and overview locations once per call, nearest first; it returns no text and keeps no session delivery state. `knowledge_read` pages record IDs/kinds/states/locations, and `knowledge_diff` names trees/counts/decision records beside a whole comparison report. Agents open files natively. Mounted `context_packet` is the slim version-3 roots/task/actions/build/pair answer; the internal resolver and full context builder remain separate. Every registered tool receives `readOnlyHint` from `mcp/read_only.py`; context freshness and diff capture/report capability are marked false.

Landing cut/add observations are report-only; use the measurement owner and canonical Curator/Reviewer duties for independent memory judgment.

For transport, start with `mcp/server.py`, `mcp/registration/`, the literal roster in `models/tools/public_roster.py`, response registration, and `mcp/public_surface.py`. The server closes the `dispatch_agent` schema and rejects undeclared inputs before its handler. The surface validator compares independently declared inventory, response contracts, registration, and dispatch schema; inspecting its source does not establish that a live server passed it. Response completion validates the full result and may deliver the tool's own bounded status projection; the detail log retains the whole result, while the guard and observer use the delivered answer count. Quality projection belongs to `application/memory_quality/answer.py`; execution and readiness remain controller-owned. Application response ownership and measuring-build identity distinguish the serving build from a candidate checkout.

For memory retrieval, select the repository and task scope before selecting files. Onboarding route indexes narrow routes and identify deterministic file cards; missing index coverage can skip a card probe but never forbids reading source. Published intent selects the resolved memory tree and reads its derived index. Taskless scope uses canonical external memory; leaf scope uses the contract's memory worktree, with no substitution between them. Legacy onboarding remains readable as `legacy-format`; mounted knowledge reads refuse legacy/database inputs with conversion guidance. A missing registration or selector is named rather than filled from another repository or scratch dataset.

Converted knowledge is authored text: onboarding cards and sidecars plus records, histories, and census files. SQLite here is a disposable derived index, keyed by a captured memory tree and stored outside Git working trees, not a canonical write destination. Partial index input cannot become a complete-looking result. The family-complete leaf read returns the seed's invariants and entries, containing families and their remaining members, reference rows for already returned members, and an advertised one-hop frontier. Mechanical governing route-chain families follow that content, including for an entry-less governed path. This is retained internal family-complete content. Mounted `read_ar_files` is stateless naming and carries no chain body or session-served state; mounted `knowledge_read` projects its selected content to names.

Knowledge pages share the declared 8,000 `tiktoken:o200k_base` threshold across the whole block. Counts distinguish total, returned, and remaining selection. Continuations bind memory tree, seed, policy/order, and the code tree measured on the first page; mismatches require restarting the seed. Deferred seeds remain visible; an excessive queued tail is refused as `seed_queue_exceeded`. A single indivisible oversized row is returned whole with its explicit flag. Currentness is measured against the selected code tree, never silently against HEAD: current, stale, unverifiable, and unrealized remain visible, and reads do not re-anchor or judge.

For authoring, `knowledge-ingest` admits a leaf or crossing through its contract; `knowledge-bootstrap` admits a taskless wave. Ordinary ingest requires a nonblank authorization reference. Planning reads, resolves, validates and reports without writing; `--commit` writes files, not Git history. The writer validates the resulting tree and owner history before publication, while registry-declared writer deferrals name their later refusing commit/landing route. The leaf route supplies its paired memory base for counted-card comparison, falling back to the operation base only when unresolved. New onboarding, membership/no-family and decision/facet record judgments are distinct row domains with writer-owned source/revision fields; they do not license an unsupported producer. Authored realization rationale is required rather than manufactured. Mechanical carry supplies no semantic disposition. Crossing resolves existing conflicting records at one revision above the higher side rather than authoring new records.

For leaf maintenance, the worklist compares exact B/K_B/C/K_C, task declarations and maintenance scope. It classifies entries and record changes, reaches families once, reconciles planned effects, checks routes, classifies unexplained changes and surfaces one-hop reconsideration. New or newly unlisted live invariants raise membership work; changed surviving base decisions/facets compare both JSON and retained unparsed Markdown. Only the leaf's own open raise with an otherwise status-only reconsideration mark is exempt. The final sorted/digested list includes the membership and touched-record kinds and subject-based planning marks on the kinds passed through planning. Unreadable input is named incomplete scope. Persisted worklists are projections; the mandatory gate recomputes its inputs.

For publication, ordinary closeout captures and revalidates an exact candidate, checks approval, and calls the converted-memory knowledge gate before publishing either side. It subsequently refreshes memory metadata/entities/routes, closes the owner's history, and validates/gates the exact memory output before its commit. Recovered memory outputs are judged too. Integration/checkpoint preview and apply call the landing knowledge boundary; series landing validates against the parent memory tip and checks currentness over the net changed code paths. Leaf landing applies its cutover boundary rather than inventing a second leaf worklist verdict. These present calls qualify the inherited statement that normal transaction routes have no quality prerequisites: the mandatory converted-knowledge gate is distinct from automatically running the complete code-quality/certification sequence.

For native role work, `application/role_launch_context.py` resolves canonical task topology; CLI role preparation compiles the assignment and binding; Paseo launch stores an exact replay call and receipt. AR chooses identity and assignment, while Paseo owns the native session. A repeated stored call converges on the same agent and distinguishes created, refused, and no-answer outcomes. Immediate starts carry their first message; held starts omit the host prompt and retain the opening handover. The owning Manager's `role_start_set` prepares Worker, Reviewer and Curator siblings with deterministic per-seat request IDs: Worker opens immediately, Reviewer opens with supplied first work or stays held, and Curator stays held. Partial sets preserve successful seats for reconciliation. Leaf holders persist across completed turns; explicit replacement is starter/launcher-authorized, and native `retire_child` requires the original starter and explicit active-turn interruption authority. Leaf handovers expose exact sibling role/task arguments, not sibling runtime ids. Worker checks use the candidate worktree's own environment according to repository tool notes, disclose a missing setup command, and record the interpreter actually used; this does not replace a serving runtime or certify a focused run.

Ordinary memory operations on legacy-format input refuse before writes, including never-converted repositories (MIK-R46). Recovery is first conversion or exact crossing sync with merge-memory from converted source; card reads return no knowledge, and existing continue/cancel recovery stays with its transaction owner. Unreadable Git/object probes retain named errors rather than becoming legacy absence. Converted/converting validation is unchanged; retired citation_migrate and memory-citations --migrate are not current routes.

## Construction And Ownership

Root `docs/` remains authored documentation, not one of the five current runtime synchronizer targets. The removed unowned documentation mirrors confer no current packaging guarantee; the retained package tool-details.md is separate. Mirror-only cards with no realization/proof entries are retired with their complete original bytes in Git and the renewal intake archive; canonical docs and existing governing cards retain their authority.

Directness is an external canonical-leaf grant, not a harness setting or task-document flag. Developer dashboard and launch-bound architect are the pre-start mutation owners. A granted leaf reuses existing master series checkouts without an enclosure, with separate role report/scratch folders and current canonical reader/revival binding. Explicit direct publication separates existing-code verification from exact-pair create/generation recovery; ordinary closeout and integration keep their own transaction boundaries.

The packaged worker brief delegates candidate setup to repository tool notes: build the code
worktree's own environment, run candidate checks in it, disclose a missing build command and
record the interpreter actually used. This does not replace the landed tool server or memory CLI
with the candidate, alter the shared runtime pin, or make a focused test a certification result.
Host bootstrap accepts the contract uv minimum or newer from PATH without installing uv;
the certified container retains its exact contract version.

The transport roster is a cycle-free model literal; registration order is separately owned by `TOOL_REGISTRARS`. `server.py` wires the server and delegates startup/application decisions. The public validator makes agreement checkable without treating one declaration as proof of the others. The CLI umbrella exposes maintenance, conversion, indexing, validation, census, file authoring, Paseo, settings-upgrade, provider-removal, and reporting commands; older subcommand counts and the retired `review-record-comparison` producer are historical.

`application/` owns context packets, runtime composition, task operations, role-context resolution, review composition, file authoring, worklists, and the invariant gate. `models/` owns response contracts, role/capsule values, knowledge-file schemas, history vocabulary, and strict terminal results. `tasks/` owns JSON-primary planning documents, canonical task path vocabulary, execution topology, cross-document membership, derived waves, rendering, and supported mutation semantics. Application writers own finite migration and rollback-safe publication. Contract reads parse identity rather than silently healing it; explicit startup/migration routes own repair.

The kernel owns canonical JSON, Git commands and capabilities, file observations, route census/indexing, memory attribution, ledger formatting, and cache materialization. Canonical JSON sorts keys, uses compact Unicode encoding, refuses nonfinite values and duplicate keys. Git subprocess ownership is centralized in `kernel/git_command.py`; its environment removes eight repository selectors, explicit stdin prevents ambient input, and identity injection cannot reintroduce selectors. Present timeout classes are metadata 30 s, local 300 s, tool-bound remote 120 s, and interruptible bulk remote 1,800 s. Parsed diffs carry explicit color, external-driver, and a/b-prefix options. Private object preparation and expected-old ref publication are separate capabilities using that runner.

Route census freezes one Git/path-rule source population with NUL-safe tracked/untracked enumeration, ignored/generated exclusion, and symlink classification without following targets. Callers pass repository/storage authority rather than rediscovering it inside generation. Citation indexing combines storage excludes, Git ignore rules, and scoped caller exclusions in a recorded register. The inherited policy skips and reports oversized files, applies the aggregate budget after exclusions/skips, permits configured caps, and names hard-stop offenders and recovery guidance. Its v10 manifest refuses/rebuilds v9 rather than inventing an absent register. Citation publication preserves declined bytes and binds accepted full-document/source-cell observations before atomic replacement. Only citation fixing admits a finite `documents` list, mutually exclusive with `document`, nonempty and bounded by the curator source-candidate limit. Singleton behavior and the original leaf writer guard remain; converted list repair isolates missing/refused cards and retains both authoring and mechanical repair stages.

Memory attribution is inside immutable commit messages through the shared `Code-Commit` renderer; ledger format and attribution are separate kernel responsibilities. The newest-first ledger is a Git-derived consumer view, allowing later memory states for repeated code revisions without deleting older attributed history. Root `memory.md` is a disposable memory-domain cache, not a second mapping authority or publication prerequisite. Memory content identity excludes that cache while retaining actual Git head/tree observations; this exclusion does not apply to code. Baseline/carryover produce attributed substantive content when needed and report cache refresh separately. Cache failure is availability, not permission to invent a pairing.

The reviewer resolves one admitted comparison for subject inventory, rendering, source expansion, curator records, and currentness. Converted comparisons record exact code and memory endpoints and pin uncommitted candidate objects before exposure. Historical reopening uses retained endpoints, never today's tips; missing history is named unavailable. The comparison and subject-list routes are path-free; source expansion admits a repository-relative listed/context path plus both bound code tree ids, not an arbitrary filesystem root. Unwired ports refuse as not served rather than returning an empty list or file. Transport status/refusal mapping and actionable bodies share one owner.

Expression cards group exact (path, range) locations, display authored rationale or its explicit gap, and use bounded exact-side excerpts/diffs with per-side currentness. Review change navigation now opens `ChangeSetViewer` through `ReviewSurface` using a recorded comparison; removed `SourceExplorer` and `LaneFileFocus` are not current owners. `serving/changeset_comparison.py` supplies recorded code/memory inventories and file diffs. The leaf-tree response and memo retain currentness/worklist rather than a knowledge diff; the shared diff helper remains for public `knowledge_diff`. Subject listing additionally carries an index-derived complete meaning/membership outline through `review_outline.py` and shared `review_record_changes.py` facts. Partial rosters state loaded versus total. Planning marks come from the same leaf-wide comparison. One shared lane classification serves gate linkage, unexplained/unknown navigation, counts, and server-computed change-kind facts; the client does not invent hunk arithmetic. Entry ranges count only at the recorded blob. Unknown/partial input cannot mean unchanged or gate-unexplained. Triage keeps unchanged siblings and does not force unreturned pages to load.

The Knowledge reader is a separate taskless, read-only path/truth/code/census interface over memory trees and derived indexes. It names measured code-tree provenance, pages directories/subtrees, preserves full decision alternatives and reasons, links references, and combines record, history-row, and entry histories without authoring truth. Failed sources are partial/unavailable, not empty; invalid locators and control characters are refused; binary/oversized code yields bounded notices and a directory code request has a typed absence.

`review_evidence_records.py` preserves curator assessments and evidence and measures exact comparison input currentness. Detection signals, verification observations, evidence claims, and matrix-authored effects remain explicitly unavailable with no measured counts after retirement of their canonical owners. Proof entries and worklist history retain their own meanings. Collection availability distinguishes recorded, none-recorded, unavailable, not-measured, and not-selected rather than collapsing all into an empty tuple.

Recorded-read scopes collect file identities and selection observations from shared readers. Conflicting/unreadable observations cannot occupy memo slots; selection changes are checked before target bytes, including JSON-file selection. Worklist process ownership is transient, not a durable job store: identical requests share a flight; at most two children run and eight computations run/wait; sharers do not consume extra computation slots. Parent deadline is 60 s and child deadline 65 s. Whole process groups are reclaimed, abandoned flights stop only when no requester remains, and a child build mismatch names dashboard restart. The protocol deliberately adds no arbitrary total result-byte cap to supported worklist/read-set collections.

Paseo host installation/provision/status/stop, pinned host/Node packaging, native bridge/catalog/frame integration, immutable launch receipts, identity-bound task tools, closed-leaf agent archival, and bounded archive reconciliation have separate owners. Explicit/native-default model choices retain native permission/tool behavior. Investigator selection is resolved from canonical sprint/master topology; leaf selection is refused. Task-owned receipt discovery, complete-set capacity, and exact execution lookup do not introduce another lifecycle or retention store.

The retained hosted-control/conversation implementation has its own lower-level authority: strict normalized wire contracts and ports, app-scoped runtime composition and authorization, independently owned active/library/control children, private exact-identity IPC, capability observations, and native protocol adapters. Its existence is not fresh native-host qualification. Native history/evidence domains stay distinct; hydration uses native authority rather than a flattened transcript cache. Signed cursors bind purpose/scope/epoch/generation. Control acknowledgements do not equal settlement, ambiguous post-write loss does not justify blind resend, raw vendor evidence is not public control data, and fixture/version observations cannot independently promote capabilities.

Generated package runtime skills/assets come from canonical repository sources and sync generators; package copies are distribution evidence, not authoring homes. The compiler uses packaged instruction bytes, while installed coordinator copies serve human/runtime browsing. Dashboard assets are git-ignored release output, not one-to-one onboarding subjects; a source build without them can serve a named 503 and absent `dashboardBuild`. The tracked tokenizer vocabulary is a different population: exact bytes are verified before the scoped tiktoken cache override, preventing corruption from becoming a network download or installed-tree rewrite. Its reentrant lock permits nested loading.

Converted-memory landing admission is exact-pair judgment on every publication/recording route, not trust in a previous verdict. Leaf recovery, integration and recording share one leaf-pair judge; master final/checkpoint/recorded routes combine validator, net staleness, chain proof and new-history ownership. This does not make full MQC or independent review a landing-time operation.

Role-message transport spans existing strict contracts and registration, dynamic settings, task-owned message-file storage and the delivery facade. Full payloads remain files while wake/reply text is bounded; same-ID source relocations preserve receipt/capacity/archive authority. The private host plugin adds mechanical turn-end wakes, not a new semantic acceptance or task-state writer.

### Landing observations and human review

The existing memory-quality answer now carries cut-card and added-file counts with bounded first rows, while the logged whole result and a full leaf checklist retain complete observations. These rows are report-only: they create no automated refusal, actionable repair count, new public tool or landing-time semantic judgment. The canonical and shipped Curator role sources require the handover to name the task change that made removed text untrue and put evidence/working files in the task record or scratch root, not memory. The Reviewer role source reads both reports and judges unsupported removals and requirement-unplaced additions in the independent memory lane. Source and assertion inspection here supplies no new compiled-harness, test or closeout acceptance.


### Native selection and source-owner qualifications

Role-message transport runs from `mcp/registration/role_agents.py` through `mcp/tools/role_agents.py` to `cli/paseo_role_tools.send_role_message`. The native facade owns recipient resolution, receipt/capacity checks and deliver-or-hold decisions; `cli/role_message_delivery.py` supplies shared message preparation, filing, long-reply and successor helpers, while `cli/role_message_files.py` owns task-scoped file storage. `role_message_limit` rereads settings on each call. Full `body` and attachment records are carried by message files rather than wake text; a long wait reply is filed whole when possible and cut in the answer, with an explicit warning if filing fails. Moving shared helpers does not transfer receipt, capacity or archive authority or admit a runtime source relocation. The private plugin's `index.server.ts` and `server/turn_ended.ts` add bounded mechanical parent wakes, not a semantic acceptance or task-state writer.

Fresh converted leaf closeout validates its exact output in `worktrees/modules/closeout_external.py`. Its `require_gated_recovery`, leaf integration in `worktrees/modules/integration_gate.py`, and leaf recording in `worktrees/modules/record_landing.py` call `leaf_pair_refusal` again. Recovery uses the parent memory tip; integration uses the current source memory tip; recording requires the contract's recorded memory base and retains the closed-history check. Recording judges the recorded closeout code when the landed code contains it, otherwise the landed code itself. Master/checkpoint integration and master recording use the landing-gate port, with net staleness and newly closed history ownership in `application/knowledge_gate/landing.py`, plus the chain proof in `worktrees/series_closeout.py`. Final integration requires all non-abandoned canonical leaves landed; checkpoint and recorded landing prove the leaves already landed, up to the pair they publish or record.

- Retrieval doctrine now uses onboarding/route indexes and harness-native search, not CGC/GrepAI. `providers/settings.lifecycle_settings_from_config` emits disabled, empty context-provider settings, and `providers/setup_common.provider_enabled` treats the two retired providers as never enabled. `install/provider_watchers.stop_provider_watchers_before_refresh` retains cleanup of old watchers; it reports a failed stop without aborting refresh, not a restored install/start/watch route.
- Public native `role_start`, `role_start_set` and `role_message` enter through the role-agent registration/payload adapters and `cli/paseo_role_tools.py`. Only the owning Manager starts the three-seat leaf set through `role_start_set`: Worker opens immediately, Reviewer opens with its optional first message or is held, and Curator is held. `cli/role_launch_routes.dispatch_leaf_set` derives per-seat request identities and reconciles partial retries. `cli/role_launch_liveness.py` owns occupied-seat replacement, including the explicit launcher path; public `retire_child` instead reaches `cli/role_retire.retire_native_seat` and checks the original starter. Workspace-local held delivery lives in `cli/role_held_messages.py` and the serving lifespan actor, not the retired public hosted-seat messaging path. This does not remove the separate public `dispatch_agent` structural/ambient route. Permission decisions remain developer-owned: pending prompts are held rather than answered by message delivery. Execution receipts remain separate from task acceptance.

The packaged worker brief delegates candidate setup to repository tool notes (`system/tools.md`): build the code worktree's own environment, run candidate checks in it, disclose a missing build command and record the interpreter actually used. This does not replace the landed tool server or memory CLI with the candidate, alter the shared runtime pin, or make a focused test a certification result. `scripts/bootstrap-mcp-venv.sh` resolves uv from PATH and accepts the minimum in `scripts/python-runtime-contract.env` or newer without installing uv. The certified container's `.dagger/src/agents_remember_quality/main.py` installs exactly that contract uv version.

- Source comparison: `mcp/src/agents_remember/providers/settings.py:32 (def lifecycle_settings_from_config)` — generated settings disable context providers and contain no provider blocks.
- Source comparison: `mcp/src/agents_remember/install/provider_watchers.py:128 (def stop_provider_watchers_before_refresh)` — retained stop-only cleanup reports failure and lets runtime refresh continue.
- Source comparison: `mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md:12 (## Retrieval Substrates)` — harness-native retrieval, with the downstream route-index recipe.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them. The held public roster is `models/tools/public_roster.py`, wired by `mcp/registration/__init__.py`; retained provider diagnostics do not restore provider MCP tools, and native document-chat discovery is a serving route, not a new tool in that roster.

Directness is an external canonical-leaf grant stored by `kernel/direct_execution_grants.py`, not a harness setting or task-document flag. `application/direct_execution_grants.py` admits the launch-bound architect and `serving/direct_execution_grants.py` owns the developer dashboard control. Give/revoke prove the leaf unstarted; reclaim only removes grants for abandoned, never-started leaves with determinably clean series checkouts, preserving Completed leaves and abandoned leaves that started. A granted leaf reuses existing master series checkouts through `cli/role_launch_workspace.py` without an enclosure, with separate role report/scratch folders. `application/task_scoped_mcp.py` admits readers against the canonical leaf and series contract; `cli/role_launch_preparation.py` recomputes that binding before revival. Explicit direct publication in `worktrees/direct_landing.py` verifies the existing series HEAD when `code_commit` is supplied, or creates from the exact previewed candidate tree behind the pair gates and a durable recovery generation when it is absent. Ordinary closeout and integration keep their own transaction boundaries and do not require that grant.

The existing memory-quality answer carries cut-card and added-file counts with bounded first rows. `memory_quality/converted_check.py` attaches the report-only landing observations from `memory_quality/landing_report.py`, comparing against the admitted leaf base when available and otherwise the run's comparison base. An unreadable base is a named observation gap, not proof that no text was cut. `application/memory_quality/answer.py` projects the counts and first rows; the logged whole result retains the full lists, and the full leaf checklist receives complete report-only observations through `application/memory_quality/controller.py`. These rows create no automated refusal, actionable repair count, new public tool or landing-time semantic judgment. The canonical and shipped Curator role sources require the handover to name the task change that made removed text untrue and put evidence/working files in the task record or scratch root, not memory. The Reviewer role source reads both reports and judges unsupported removals and requirement-unplaced additions in the independent memory lane. Source and assertion inspection here supplies no new compiled-harness, test or closeout acceptance.

Native document-chat discovery is a serving POST preload in `cli/role_document_chat_tree.py` (`/api/role-launch/document-chats/tree`), not a public MCP tool. It bounds selections and receipt bytes, reads each canonical launch receipt once per request, and calls `cli/paseo_status.read_live_agents` once; `cli/paseo_bridge.mjs` pages that live-ID census and explicitly reports whether it ended. `cli/role_document_chats.py` (`/api/role-launch/document-chats`) remains the correcting single-document authority. Unreadable, mismatched, oversized or census-incomplete selections are unknown (`agents: null`); host unavailability is explicitly marked, never authoritative empty chats. The frame descriptor in `cli/paseo_frame.py` names a `provisionCommand` built by `serving/paseo/paseo_remedy.py` from the active settings for an older-plugin notice, without executing it. Existing launch/replay/lifecycle/acceptance owners are unchanged.

## Invariants And Boundaries

Planning truth stays upstream of scheduling. Task mutation publishes before disposable readiness projections are invalidated/recomputed. Canonical sprint Judgment and Priority Registers have a strict grammar on writer admission; status can expose absent/ok/malformed facts without upgrading malformed prose to authority. The retained graph-less atomic-sequential planning intent declares no invented dependencies; this intent is not proof that the task-authoring API currently admits an absent graph. Real authored predecessor edges gate execution. Activation is one replace-in-place record per canonical contract, not per shared protected pair: concurrent masters keep independent selections. Only the addressed reconciling contract waits for its exact sync. Foreign, absent, or unreadable authority is not reconstructed from task prose, queue rows, legacy files, or ambient Git. Git conflicts remain in operation-owned worktrees/journals until authorized continuation/cancellation. Queue and caches own no commit, certification, recovery, integration, or terminal truth.

Structural dispatch retains the distinction between injected plane identity and an ambient launcher. Plane authorization does not fall back after refusal; caller role/spend overrides cannot manufacture authority. Canonical task-and-role seats, exact pinned initial briefs, replacement-aware ordinary delivery, and internal session primitives have distinct responsibilities. Present native role handovers supply explicit binding and instructions rather than requiring the launched agent to infer a second role/hierarchy from older ambient routing prose. Role messages retain named missing/ambiguous-seat refusals rather than guessing an occupant or starting duplicate work. Unfinished starts, permission waits and unavailable mid-turn writes ordinarily hold messages in the recipient's `.ar-product/held-messages` store; twenty waiting messages per recipient is the cap, overflow refuses without dropping messages, and senders may withdraw their own uncommitted messages. `cli/role_held_messages.py` owns ordered delivery and held-seat opening; the serving lifespan owns the retry sweep. Permission decisions remain developer-owned, and mutually waiting seats can deadlock. A completed turn is not an acceptance record.

Converted knowledge maintenance retains authored responsibility rather than automatic repair. Families have directory routes, coverage, and nonempty-location obligations, with explicit unrealized/legacy/report-only exceptions. Route suggestions are labelled mechanical and ambiguous renames are not silently chosen. Reached families receive the route conditions; an unrelated leaf is not charged for a route already dead at its base. A route-condition answer needs a qualifying non-`no_impact` row and a satisfying or retired family record. Retired families raise no route items.

Every unexplained changed hunk/nontext change needs its coverage-appropriate disposition. Coverage is judged at K_B. Covered changes use an attach/author that actually links the change or an authored `no_invariant` reason; uncovered changes use onboarding trace. Delete-only linkage comes from K_B and insertion-only linkage from K_C. An attach/author cannot explain a deleted-only hunk; an uncovered `no_invariant` row closes nothing and is only reported unnecessary. Nontext identities and identical-line hunk sharing retain their own subject rules.

Expected effects are keyed by declared subject/effect, not list position. With no declaration items are unplanned; unreadable task input is not an absent declaration. A declared strengthening is not delivered by `no_impact`. An undelivered declaration needs a planned row with a resolvable disposition reference; taskless waves cannot invent the task owner's decision for a dropped effect. Optional declaration absence preserves existing intent digests.

Ordinary onboarding traces require the leaf's latest eligible source-bound row for each card and nearest governing overview: `updated` also needs an authored Markdown or nonmechanical reference change; `no_impact` binds unchanged contract meaning. Realizes/proves-only edits and mechanical reanchoring do not count. Source movement reopens the row; sourceless historical rows remain valid only in their own closed files. Mixed or unreadable sides cannot pass. This leaf's amended R53 rule 1 separately permits its own measured changed card under the pre-landing producer, with no unsupported updated row, no changed-card no_impact and no later backfill. Converted semantic gating is not Update History ordering. Closed-history checks preserve base/recorded-closeout scope and cannot be bypassed by setting a flag.

New invariant/family/decision admission needs a supported criterion and justification in words. Former blanket existing/exported/unrealized reporting is replaced by named route rules: merge_reports refuses existing-admission failure, gone family routes, unrealized live families, anchors at gone paths and merge-moved history at commit/landing, reporting only during sync merge. Existing-path blob/content drift is not the gone-path rule. Migration_debt reports base-carried missing-card, unresolved-citation, route-unassigned and legacy-unassessed debt only until every onboarding route is migrated/excluded; new debt refuses at once. R13.3-governs refuses a decision governing nothing. Writer-only reports permit across-run repair, never permanent publication exemption. Decisions retain two alternatives, exactly one chosen and reconsideration grounds for rejected/deferred options; supersession is derived. Unresolved requirement endpoints remain separately reported.

Reconsideration is explicit, one-hop, and triggered only by linked grounds; unresolved endpoints/tasks without manifests do not invent a trigger. Superseded decisions are skipped visibly. The curator can reaffirm rejection or raise a developer question, never reverse the decision. A reaffirmation refreshes only fired, still-matching links to the judged mapped state; a new change needs a new explicit answer, and an identical retry is a no-op. A raise appends its task question before knowledge-file publication and refuses without the task-question owner. Reordering linked alternatives is guarded, subject to the historical rewording limit below.

The mandatory converted-memory gate recomputes exact inputs, checks kind-specific satisfying rows and validator refusals, and treats incomplete reads/Git failures as named repair findings. There is no waiver/report-only gate mode. Memo reuse requires identical tree/contract/parent/task/build inputs and unchanged recorded reads; conflicts, unreadable observations, and incomplete/Git-failed runs are not reusable acceptance. Closeout asks before approval consumption/publication and again over its exact refreshed/closed memory output. It rejects physical tree or admitted branch movement, stages the judged tree, and restores its own preparations only while bytes still match. A partial publication/proof failure remains recoverable evidence, not an invented rollback success. Once converted memory exists in the repository, unconverted writes/publications use the cutover refusal and named crossing route.

Paired acceptance binds configured repositories, physical worktree roots, branches, bases, onboarding root, and contract digest. Ledger location is informational. Candidate capture uses an isolated add-all index and stable observed HEAD without staging the user's index. Changed pair/candidate inputs invalidate stale acceptance; operation reconciliation cannot call a moved HEAD its output without exact identity or journaled mutation proof. Series/direct-existing routes retain committed-tree semantics. Closeout/integration preserve approval, source lineage, Git/ref/tree compare-and-swap, exact recovery, and publication ownership; queue projections do not grant these powers.

Full contract-scoped curation distinguishes raw quality repairs, coherence-required and current validated coherence; preparation is not a final certificate. Before closeout, a non-author second reader checks every changed card, sidecar and record statement against final code, every history disposition/effect/reason against the diff and important omissions; blocking findings are repaired. This role duty is not a new transaction-enforced review predicate. Historical certification owners remain separate from host-test authority and converted-knowledge admission; the broad old CCR-R12 no-prerequisite wording does not erase present knowledge-gate calls.

Ordinary development supports isolated host pytest, including focused/serial investigation, without certifying authority. The declared case budgets are 5,000 unit and 1,000 integration cases (`pyproject.toml:298-299`); D226 raises only the unit ceiling from 4,000 and leaves integration and guard behavior unchanged, not the old milestone totals. Distinct user-operation/failure/regression protection justifies cases; unused support and duplicate matrices are not restored for coverage. Coverage is diagnostic, production CRAP 20 is a review trigger, and Radon reports do not enforce acceptance. Lint, formatting, typing, structural rules, and test failures remain enforcing; diagnostic execution errors remain visible. Certifying claims require genuine pinned Dagger admission and the existing lifecycle publication owners, exact candidate/process identity, disposable state, and credential isolation. A copied report, host pass, sync result, or use of Dagger alone is insufficient.

Finalization preserves landed reachability, carryover-before-cleanup, actual edit/ancestry protection, task work-branch scope, exact task-document resolution, and terminal blockers. Present `finalize.py` delegates document resolution/publication to `finalize_task_documents.py`; older private-owner locations are historical. The inherited master rule distinguishes completion from archival: abandoned rows do not block master completion, finalizing a master does not archive it, and explicit task retirement owns master archival. Cleanup excludes/discards only the computed memory ledger cache, preserves parent/source branches, and derives review-artifact deletion from the archived task's identity with physical confinement. Agent archival and review cleanup do not establish new historical knowledge.

## Historical And Verification Limits

Source descriptions, surviving reference identities and declared interfaces do not supply a fresh execution, installed-runtime, native-host, landing or acceptance verdict. Historical limits below retain their original evidence scope; they do not endorse a changed requirement.

The incremental MIK/ICR/KS chronology records important intent but its old claims of inertness before MIK-R37, production population, installed-build adoption, and test totals are dated context. Converted gating is present source; whether a particular live memory line is converted or an installed runtime adopted it was not measured. Canonical database ingest/publication, copied candidate/baseline placement, empty-first-generation manufacture, dataset comparison recording, canonical detection/verification/evidence records, and the review matrix were retired. Their old replay/namespace/allocation/publication accounts must not be reintroduced as current routes. Historical allocated identity separates creation retry keys from stored truth continuity; present continuity must name stored identities rather than treat a local label or enclosure as the truth's permanent namespace.

Named unresolved or accepted historical limits remain visible without their old task-local witnesses being available in this bounded source pass:

- CAPS-L10 adoption FAILED on startup reduction: delivered worker orientation 11,828 tokens versus 5,928 baseline (+5,900), implementation 11,645 (+5,717). Manager/architect were `binding-unresolved` and unmeasured; 36/36 obligation preservation did not make reduction pass. REVISE was a recommendation, not a landing decision. The 4k/32k target was neither achieved nor a truncation rule. Native eve evidence used a deterministic local provider; real-model was UNRUN and matched Codex baseline completion UNRUN-AS-MATCHED. Peak occupancy was unobservable on both harnesses; eve cumulative usage was unobservable; cumulative usage and occupancy were never summed. The unscoped routing-chain baseline excluded on-demand skill reads, so total-session savings and compiler causation were not established.
- CAPS-L9 withholding/no-global-switch measurements were coordination-root scoped. The harness skill corpus remained readable; C6 duplicate-corpus and C7 instruction-replacement union limits were not resolved by installation evidence. Installed corpus is not compiler input. Historical role-eve effort gate D22/L17 and dashboard missing `session_backend` were named separate limitations; this pass does not promote or remeasure them. Library native reopen was deliberately excluded from fresh capsule installation because it resumes vendor identity.
- CAPS-L2's historical layer result had 16 existing violations; compiler structure was not proof the whole layering contract passed. Historical source restructuring/determinism/delivery success did not establish context reduction.
- MIK-L14 Q4 alternative-move-with-reword could evade the text-based reorder guard; Q7 task-question read/modify/write used a two-call window. Historical idempotence and later review closure do not erase those named limitations without a deciding current witness.
- MIK-L29 paired code selection used a memory commit's `Code-Commit` but published/leaf selection used checkout HEAD, with the pairing gap carried to L03. Unsigned continuation tokens were an accepted L02/L29 design limit. MIK-L32 reported 47/178 converted entries at older blobs; exact-blob attribution can therefore become unknown. Neither number is a present census.
- MIK-L25 archival acknowledged a TOCTOU window despite task-id confirmation and physical confinement. Dataset-review/unconverted preservation measurements were historical and do not prove present compatibility or installed cleanup.
- ICR-L34's retired comparison producer was live-leaf-only and ordinary retries could append successors because lineage participated in its seal. These are retired-route limits, not promises or defects attributed to current tree capture. Historical retention creation was retired while custody/release remained; lost trees stay unavailable rather than substituted.
- HFX2-L5 liveness evidence covered six incident classes end-to-end and two hybrid classes because pane capture was noninjectable. HFX2-L13 retained unbound-worker chain-credit S1/S7 and did not certify the HFX3 post-integration retro gate. PHA-L6 carried R10 resource performance; earlier adapter leaves explicitly excluded production cutover. Older immortal-pending inbox semantics were superseded by 48-hour expiry/500-current-id retention. Durable artifacts, not notification rows or copied observer projections, carry truth.
- Conversation history/control retains honesty limits: historical Codex tool loss, Claude never-probed capability refusal, acknowledgement-versus-settlement, unsupported native operations, withdrawal lease expiry, and epoch/cursor boundaries. Capability contract evidence, not version-string comparison alone, governs promotion. Multiplexed approvals use exact RPC/thread identity; unknown vendor methods degrade/preserve evidence, parent known-shape failures remain loud, and delta shedding is counted rather than silently losing truth. These inherited contracts were not requalified against native hosts here.
- LCA-L3 backfill was deferred after a confined rewrite broke shared ancestry and ordered sync could not merge unrelated histories. Its recorded fixed matching reached 418/428 code revisions and attributed 455/455 memory commits under single-trailer constraints; selection declines/holes/lost claims were explicit, and hash-order variants were refused. The confined application was reverted with backup audit custody retained; the later fixed tool was described as fixture/read-only-plan proven, not applied to a real repository. Present shared-line trailer counts and any integration-time application are unknown. LCA-L4's historical five-producer census had a third-way-construction blind spot and no prepared-leg behavioral case; it is not present coverage.
- KS-L1's macOS APSW session/changeset acceptance remained unexecuted. KS-L23's 400/400 integration and 2,278/2,300 unit limits were historical, superseded by current declared budgets. ICR-L19's six stale installed harness copies/seventh updated root were dated observations; package source cannot certify installed user copies.
- MCAR's historical R05 typed finalization, R16 telemetry, and R07/R08 final-memory protocols were reported without production callers. Existing journals, interactive readiness, retained foundation models, and the prepared adapter did not prove those new protocols integrated. This source pass does not adjudicate their full present caller graph.

Old full-suite totals, mutation kills, scratch measurements, captured bodies, browser sizes, sync passes, pin digests, closures, and native scenarios remain historical evidence claims rather than fresh acceptance. Historical tests removed during inventory reductions, or moved/split support, are not restored obligations. A local function's lack of a check cannot establish absence across its callers; conversely, a module docstring naming a retired database path cannot re-enable the route when the current CLI explicitly refuses it.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/`                                     |

### Native-source claim qualifications

- Candidate setup remains repository-owned; host bootstrap accepts PATH uv at the shared contract minimum or newer, while the certified container keeps the exact contract pin.

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/worker-brief.md:47-50`; `scripts/bootstrap-mcp-venv.sh:28-84`; `scripts/python-runtime-contract.env:12-15`; `.dagger/src/agents_remember_quality/main.py:123-129`.

- Report-only landing producers, bounded answer/full-result custody, and canonical plus shipped human-review role contracts.

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/application/memory_quality/answer.py:202-239`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:107-110`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:147-148`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:105-111`; `mcp/src/agents_remember/memory_quality/converted_check.py:127-189`; `mcp/src/agents_remember/memory_quality/landing_report.py:353-401`; `mcp/src/agents_remember/memory_quality/landing_report.py:717-810`; `mcp/src/agents_remember/application/memory_quality/controller.py:618-632`; `mcp/src/agents_remember/application/memory_quality/controller.py:757-781`; `mcp/src/agents_remember/mcp/tools/memory.py:116-141`; `skills/l-01-agent-lifecycles/roles/curator.md:107-110`; `skills/l-01-agent-lifecycles/roles/curator.md:147-148`; `skills/l-01-agent-lifecycles/roles/reviewer.md:105-111`.

## Evidence

- The runtime synchronizer declares five targets without docs; retained packaged tool details do not add a sixth generator target. [311]

- The facts and where they come from. [1]
- Their vocabulary. [2]
- The gate over a leaf's exact candidate. [3]
- Each kind's own predicate, registered beside the kind. [4]
- The worktree layer's probes, the unbound refusal and the closeout's own write. [5]
- The history-row rule over every file's subjects and the leaf's own file. [6]
- The one rule, named for its three writers. [8]
- The finalizer dispatches a leaf with a named master to _named_parent and a leaf without that name to _folder_parent. [9]
- The placement guard. [10]
- The one classification and where it differs from the gate. [11]
- The three reads. [12]
- The lane's shapes and validators. [13]
- The worklist registrant: what is read, the triggers, route and superseded rulings, the items. [14]
- The writer's rows, the refresh and its link states. [15]
- The manifest lookup. [16]
- The reorder guard, registered on import. [17]
- The reader's entry point: one read-only question per call, the envelope and the typed failures. [19]
- The route: 200 for typed answers, 400 for invalid requests, 503 unwired. [20]
- The Knowledge area's own statement. [21]
- The entries module statement. [22]
- The on-demand cards read at the route. [23]
- The card component's own statement. [24]
- The chain module statement. [25]
- The compact row with its family seed. [26]
- The family seed on the mounted read. [27]
- The two kinds and the coverage lookup. [29]
- The subjects and the gate predicate. [30]
- A delete-only hunk is linked only by a K_B range (and, since MIK-R09, an insertion-only hunk only by a K_C range). [31]
- The four-tree comparison, pinned and recorded. [33]
- The four-tree comparison, pinned and recorded. [269]
- The archive hook's identity sources and confinement. [34]
- The tree view route. [35]
- The index format bump for the seal fix. [36]
- The content rules and derived reads. [38]
- The five registered decision rules. [39]
- The owner resolves each requirement endpoint; unresolved is reported. [40] [270]
- The writer reports each endpoint of the records the run touched. [41]
- A decision is never an export. [42]
- The leaf package statement. [43]
- A path seed of the published-intent block is read as a leaf. [44]
- The mounted read's leaf response, of a path or (since MIK-R05) a family seed. [45]
- The module statement. [46]
- The stored predicate for the gate. [47]
- Step 6 of the run. [48]
- The admission rule's module statement. [49]
- The three registered rules. [50]
- The export test. [51]
- The reconciliation module statement. [52]
- The declaration on the task document. [53]
- The planned row. [54]
- The task owner's strict lookup and decision answer. [55]
- The paging package statement. [56]
- The mounted read's converted-tree branch. [57]
- The whole-block bound of the published-intent block. [58]
- The rule's statement for converted trees. [59]
- The memory-quality dispatch between the two gates. [60]
- The gate chooser both enforcement points share (since MIK-R09 a probe Git cannot answer is an incomplete side). [61]
- The package statement. [62]
- The `knowledge_read` surface, reached through the per-page extras since MIK-R02. [63]
- The published-intent surface. [64]
- The one recompute entry point L08's triggers call (since MIK-R09 a Git failure is named `git`; the gate recomputes over its exact candidate instead). [65]
- The CLI subcommand. [66]
- The two readings of proofs. [67]
- The package template copy's proof guidance. [68]
- The umbrella registers the conversion command. [69]
- The command converts, validates before writing, and commits nothing. [70]
- The pinned conversion-format version. [71]
- A raw three-way line merge that writes nothing. [72]
- A new memory repository is created with the layout marker. [73]
- A converted overview's sidecar feeds the hot-path hints. [74]
- The rule 9 refusal for a leaf whose official line is converted and, since L37, the cutover lock for every other unconverted tree. [75]
- The subcommand registration. [80]
- Inventory pins the baseline and writes through the census writer. [81]
- The writer refuses an unconverted memory tree. [82] [256]
- The subcommand registration. [83]
- The command reads the families and prints them; it writes nothing. [84]
- The six route rules in the registry. [85]
- The subcommand registration. [86]
- The command's report and exit statuses. [87]
- The one dataset resolution every knowledge read applies. [88]
- The cache that refuses any location inside a Git working tree. [89]
- The subcommand registration. [90]
- The command's inputs, scope answer and exit statuses. [91]
- The shared exclusion predicate. [92]
- The batch blob reader. [93]
- The format package's own map and its shape-only boundary. [94]
- The subcommand registration. [95]
- The command's exit statuses. [96]
- The template's informational section. [97]
- The realization admission owner. [100]
- The package-owned template copy stating the superseding target shape. [102]
- **The record-beside-the-bytes namespace, corrected in place: the receipt when there is one, otherwise the before half's own generation record, and the requested repository only when neither exists.** [105]
- **The seal's omission set, which is why naming a predecessor changes the derived id — the fact behind the carried non-idempotence limitation.** [106]
- Current curator records and explicit retired-channel unavailability [109]
- Actual absent/unreadable authority and task-context matrix cases [112]
- Custody and release remain; creation is retired [118]
- Exact retained comparison after cleanup/restart/later landing [121]
- The new module's whole surface, and the rule that a side's state is read rather than inferred from an empty string. [122]
- **The projection that keeps a present structured value out of the absence slot, and the contract that makes `None` mean absence.** [123]
- The adapter's delegation, with the composition unchanged. [124]
- **The served-value change measured through the real composition.** [125]
- The added and the removed statement, each keeping its complete available text beside the named absent side. [126]
- The renderer that decides the four branches from declared state. [127]
- Published intent selects converted memory and its derived index [128]
- File-only ingest arguments/dispatch [131]
- Only three mounted operations [133]
- Read-side index preflight without canonical placement [142]
- Current four-tree capture [147]
- Development commands, budgets, diagnostic metrics and isolation. [150]
- Certifying publication and accepting consumers. [151]
- Exact contract scope, full check and curator worklist publication. [152]
- Interactive catalog names missing authority without eligibility. [153]
- Final memory adapter requires the selected four-code-terminal prefix. [154]
- Finalization consumes original selected fifth-certificate inputs. [155]
- A ledger view is derived from Git and cache write failure is only an availability result. [156]
- Existing preparation retains actual Git binding and allows a distinct memory content view. [157]
- Baseline adoption commits memory content and returns a cache observation. [158]
- The one decision point every launch point calls, with its three answers and named refusals. [159]
- The one workspace rule and the selection that follows it. [160] [273]
- The compiler the port is bound to, including the eve path that reads the admitted workspace back out of the carrier. [161] [274]
- D13's repair, on the registered operation's own resolution path. [162]
- The declared legacy exclusion, and the enumeration case that keeps a fourth launch point from appearing silently. [163]
- The production chain read at the consumer's own gate and at the live runtime's system block. [164]
- Public closeout payload delegates the current task-bound request. [165]
- Projection admission precedes staging; declined claims retain their original bytes. [166]
- Accepted batches check complete document bytes and held source/cell bindings before atomic publication. [167]
- The exact binary-wheel pin and the in-file reason tying it to the session build option. [168]
- The same pin in the requirements manifest. [169]
- The storage home and the one-way import direction, declared as charter wording only. [170]
- The storage package's own boundary statement. [171]
- The one canonical encoder, its policy and its duplicate-key-refusing decoder. [172]
- The route overview this section introduces. [174]
- Exact tree endpoint composition, not candidate directories [183]
- The one route this leaf adds. [188]
- The GET-only registration. [189]
- The typed request the query string parses into, with no path among its inputs. [190]
- The port field on the collaborators dataclass, and the rank reason it exists. [191]
- The registration that reads that port. [192]
- The composition root's two adapter functions. [193]
- The shared collaborators bind the knowledge-review and entry-list ports and the listed source-content port. [194] [268]
- **The two-shape status idiom the routes inherit, `503` included; the signature now accepts all three typed results.** [195]
- **The two ports passed into the shared collaborators.** [196]
- **The two-shape status idiom both routes inherit, `503` included; the signature now accepts both typed results.** [197]
- Current contract-scoped file writing [199]
- **The new application module on this package's route, and the shipped read it delegates to rather than duplicating.** [208]
- **The response field the block travels on, carried by the strict response model rather than re-declared.** [209]
- **The generated carrier this package ships, regenerated from the authored root skill by the repository's own sync script.** [210]
- **The case that holds the carrier to the payload's real field spellings instead of a second vocabulary.** [211]
- **The third review route constant, GET-only, with the comment recording why it is a third path rather than a payload field.** [212]
- **The third collaborator port, with the reason it is a port rather than a field on the review payload.** [213]
- **The expansion route's own unwired answer, which refuses an unwired process rather than serving an empty file.** [214]
- **The application owner the port carries: the admitted paths (a changed path of a measured change set, or unchanged context a recorded realization of the same comparison links — decided by the admission owner), both bound trees read by object id, and the per-side states.** [215]
- The composition root's third review port, and the registration call that passes all three collaborators. [216]
- **The two new owners this route reaches: the application module's own statement of what it answers and does not own, and the vocabulary's own statement of why it is separate from the review payload.** [217]
- The production-composition cases that drive the new route over a real enclosure: an incomplete query refused by the transport, an unwired process refused by name, and an unmeasured generation that still confines the path to a measured change set. [218]
- **The one mapping both adapters reach, and the one body builder it uses.** [219]
- **The two actions the bodies gained, and the not-found body's offending input.** [220]
- **The result-to-status mapping, unchanged, which the new bodies are used beside.** [221]
- The crossing owner's route of knowledge-ingest. [222]
- The bootstrap's database route takes the cutover lock. [223]
- The lock every memory route asks. [225]
- A copied Git index keeps the index file's modification time. [226]
- The cache's ignore rule alone. [227]
- Current imported source owns this scoped route boundary. [228] [229] [230] [231]
- The ledger loader reads through the recorder. [232]
- The limits of the worklist processes. [234]
- One request: digest, join or start, wait, leave. [235]
- The one command line of a child, in its own session. [236]
- The build-mismatch failure asks for a dashboard restart. [237]
- The options every parsed diff passes. [238]
- The shared-read block of the batched blob reader. [239]
- The composition root creates the process owner. [240]
- It supplies the owner's shutdown to the app. [241]
- The waiting bound counts computations, not the requests sharing them. [242]
- A build mismatch asks for a dashboard restart. [243]
- Every parsed diff names its own prefix, colour and driver options. [244]
- Bytes the child consumed are identified across a change and restore, a conflict, an absence and a read error. [245]
- A recording block collects the rows of one computation. [246]
- A kept set is checked with its path selections first. [247]
- A conflict or an unreadable row is a failed observation. [248]
- The contract loader reads through the recorder. [249]
- The removed repository memory root is resolved through the recorder. [250]
- The host step of the install. [251]
- The packaged host contract. [252]
- The skill states the three master rules. [253]
- This source owns the route’s Investigator selection or execution boundary. [254]
- The layout-marker test both commands use. [255]
- **The availability vocabulary and the field that carries it on the served payload.** [257]
- **The production port the cases drive, and the two states F09 collapsed.** [258]
- **The keystone record: the manifest, its layout under the one durable root, the re-derived id and the directory-name agreement.** [259]
- **The two deletion owners and the record that precedes every deletion.** [260]
- **The Git-object retention member this route's `worktrees/` gained.** [261]
- **The two typed failures, and the two boundaries that decide why they are raised.** [262]
- **The one durable-root owner the layout asks instead of restating.** [263]
- **The comparison route constant, GET-only.** [264]
- **The entry route constant, and the comment recording why it is a second path rather than a second adapter.** [265]
- **The entry route's unwired answer: a named refusal with the "not served rather than served empty" reason, never an empty list.** [266]
- **The status mapping success reads as `refusal is None`, so one function serves all three typed results; the four candidate codes answer `404` and the expansion's `source_content_unresolved` falls through to `400`.** [267]
- The batch blob reader. [272]
- The task reopening tool on the registration surface. [285]
- The packaged candidate-environment input delegates setup to repository tool notes and records the used interpreter. [286]
- The enforced collected-case pair is 5000 unit/1000 integration; the unit-only policy raise leaves the guard unchanged. [287]
- The lane row. [18]
- The lane row. [28]
- The lane row. [32]
- The two lane rows. [37]
- The previously named comparison-record CLI producer is retired; the current umbrella parser registers converted file authoring and no review-record-comparison command. [103]
- Knowledge ingest is the contract-scoped converted file writer; unconverted memory is refused with conversion guidance, not a callable prior-task database publication route. [198] [203]
- The converted-card workflow's opening. [224]
- The two lane rows. [233]
- Present public vocabulary has 41 successor names (the rejected freeze had42; resolve_context removed), adds native retire_child and role_start_set, excludes historical provider/capsule/catalog tools and retains three knowledge operations [288]
- Skills registrar installs resources and mandatory methods; no tools or capability grant [289]
- Dispatch advertisement is closed and undeclared inputs refuse before handler [290]
- Generated lifecycle providers are empty independently of configuration [291]
- Old-watcher stop failure is reported and installation continues [292]
- Retrieval uses harness search and bounded source confirmation [293]
- Ingest plans by default, writes files only, and refuses unconverted memory [294]
- Worklist scope is one-pass and insertion/deletion linkage is side-specific [295]
- Closeout invokes mandatory candidate gate before publication [296]
- Exact memory output is validated/gated against parent tip with leaf-publication context [297]
- Integration/checkpoint preview and apply encounter knowledge boundary; leaf and series predicates differ [298]
- Raw quality status and combined coherence readiness remain distinct; a coherence refusal retains its code and next action [299]
- Retired canonical/matrix collections remain unavailable without measured counts [300]
- Investigator refuses leaf selection and validates canonical topology [301]
- Leaf sibling handover supplies canonical role/task arguments [302]
- Replay retains agent identity and typed created/refused/no-answer outcomes; held launch calls omit the first host prompt [303]
- Candidate environment setup and interpreter disclosure are repository-tool-note obligations [304]
- Read revalidation checks selections first and excludes failed observations from memo reuse [305]
- Worklist limits count shared computations and deliberately omit an arbitrary result-byte cap [306]
- Git includes a fourth bulk-remote timeout and fixed parsed-diff options [307]
- Finalization delegates task-document resolution/publication and checks blockers before cleanup/publication [308]
- Current declared collected-case budgets supersede historical totals [309]
- bounded landing answer and human-review role contract [288]
- Native tree preload and correcting single-document HTTP authority, paged live-ID census, and settings-bound explicit provision notice without execution. [310]

- Paired-base authoring comparison and contract write route. [315]
- Named reporting and refusing routes. [312]
- Source bindings, membership and record models. [313]
- Non-author statement/diff/omission fact-check. [314]
