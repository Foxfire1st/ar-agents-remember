# mcp/src/agents_remember/tasks/ — JSON-Primary Task Documents

## Governing Overview
[mcp/overview.md](../../../../overview.md)

## Purpose

Code reviewState and the post-landing memoryReviewState are independent persisted evidence lanes. Recorded rounds retain their kind and findings-remain facts for step-up counts; record-only checks add no try, and a memory result cannot reset passed code. Ordinary reads remain strict. The private launch-only fallback preserves malformed raw review evidence without making it a counted or accepted round; in-flight pre-rollout memory checks are not migrated.

`tasks/` owns the persisted `ar-task-document/v1` work-content model and its Markdown rendering. JSON holds plans, progress, decisions, references, review evidence, and optional lifecycle/enclosure bindings. Markdown is a generated view; it is not parsed back into task authority. Light and master documents write to `task.json`/`task.md`; a `subTask` uses its slug. This lets planning and running work share a task-document source while runtime lifecycle, enclosure, Git, and queue owners retain their separate responsibilities.

The route also owns structural sprint/master/leaf addressing, canonical parent-row/leaf binding, normative task-intent projection, completion-readiness predicates, execution-graph validation, semantic topology identity, and same-root leaf-to-master synchronization. Structural addressing does not itself select a live runtime occupant. Reopening an enclosure belongs above this route in `worktrees`; its document reset still uses the task persistence owner.

## Hot Path Summary

master_order derives ordinary-master waves and dependency facts from declared waitsFor and each matched child's document stage, falling back to the authored row only without that child document. Matched child titles likewise take precedence over row-name fallback. Waves are supplied to Markdown and projection, never stored, and dependency readiness is not a second host/task activity source. Backend progress.py owns major-only counts and current-work labels that can name nested work units. Frontend dashboard/src/panels/detail-panel/model.ts::stepDisplayState infers an unfinished major's displayed current state from active or done children; it does not author canonical status. completion_blockers separately examines every major and child obligation. Optional nonGoals, acceptance, completedAt and waitsFor remain compatible with old field absence, and new normative fields participate in intent/effect classification.

The application `task_doc` entry point loads or creates a validated document, applies an operation, enforces the applicable mutation rules, and prepares publication. A sub-task edit can include a planned update to its same-root master's row. The publisher retains exact accepted JSON/Markdown source pairs and rechecks those pairs before publication. It writes the prepared task documents, refreshes their copies, and restores accepted task sources if copy publication fails.

Projection scope follows the accepted/candidate field delta. Topology, normative-intent, and completion-readiness changes invalidate affected projections; evidence and operational-audit changes alone do not. The shared task-fact publisher validates, resolves the fixed-order scope union, publishes task truth, attempts invalidation for each scope, and then rebuilds projections independently. Invalidation and rebuild failures become reported per-scope effects after task publication; queue output is not planning authority and its failure does not undo the published task truth.

The inherited CLIVE/DAGQC account requires short serialization against structural/integration races and describes task truth plus invalidation as one atomic publication. The examined publication bodies establish source-pair comparison and the ordered operations above, but do not by themselves establish that complete concurrency guarantee. Keep that policy intent distinct from a verified whole-call-path locking claim.

Persistence prepares JSON and rendered Markdown payloads, refuses duplicate output targets, snapshots prior destination bytes, and uses individually atomic replacements. A failed replacement triggers restoration of the complete prior file set; failure of both publication and rollback is surfaced. This is failure atomicity, not a filesystem transaction providing simultaneous visibility of every file. The write-and-remove variant also rejects overlapping write/removal targets and restores touched files on failure.

## Construction And Ownership

JSON stays the authored plan source. Renderer accepts optional supplied direct-grant evidence; store reads it per publication batch and reuses it only within that batch. Rendered Markdown is an annotation snapshot, not permission, and no grant field is serialized into TaskDocument.

`document.py` defines `TaskDocument`, steps/substeps, decisions, examples, header notes, sections, sub-task rows, sprint seats, execution nodes/graphs, enclosure references, execution registrations, expected knowledge effects, and discard audits. Shared document/step status and execution-nature vocabulary lives in `models/task_document.py`; route-review models live in `tasks/route_review.py`. These are persisted contracts, not MCP response models.

The three document kinds remain distinct. Masters reject steps, code examples, `codeExamplesNote`, direct `lifecycleId`, and execution registrations. Nonmasters reject master-only row, discard, command, and seat populations, permit only freeform extra sections, and reject execution nature/graphs. A note explaining absent examples cannot accompany nonempty examples. Execution registrations are sub-task-only, unique by source kind and role, and retain compact first-observation markers so reclamation of seat/report stores does not turn historical execution into apparent nonexecution. Discard audits have unique identities, cannot overlap live rows, and must carry proof identity matching the parent repository and child source filename.

An orchestration sprint is a master with commands or retained retirement rows. Consequently a sprint remains a sprint after its last master is retired. Typed live `masterRef` rows require commands; seats are sprint-only and planned/active roles must be unique after role canonicalization. An execution graph requires commands; a sprint cannot carry master execution nature. `integrationBranch` is trimmed, nonblank, master-only, and sprint-owned rather than inferred from the checkout branch.

`render.py` deterministically assembles the view from a validated model. Leaf sections follow the ordinary template, with freeform sections appended after References. Master sections form an ordered render plan: freeform bodies remain prose, while sub-task indexes and shared decisions are generated. A commanding sprint with rows but no explicit sub-task section receives a generated Master Index. Headers expose status notes, extra header notes, commands, seats, maintenance scope, and expected knowledge effects when present. Step headings retain titles; checkboxes show outcomes or titles and include notes/dispositions. A step with no outcome, substeps, note, or disposition is heading-only. Empty examples use `codeExamplesNote` when provided. Binary Markdown checkboxes do not replace the four-state JSON progress vocabulary. Master-row markers use a direct status lookup, making an unsupported status visible as a rendering failure.

Execution-graph rendering separates machine identity from labels. Structural nodes compare/hash by kind, owning document reference, and leaf IDs; callers use `.ref` for addressed document identity. Legacy bare-reference lump nodes are explicitly lifted and serialized back as a separate wire contract. Mermaid private IDs use declaration-order ordinals shared by declarations and endpoints, while labels remain human-readable, escaped, and truncated. Masters are grouped and segments ordered using waves and declaration order. `execution_graph_titles.py` joins master titles by reference key and leaf titles by `(master reference, leaf ID)`. Missing/invalid title sources use raw reference/leaf labels rather than borrowing another master's equal local row number.

`execution_graph_validation.py` supplies indexed intrinsic analysis: unique structural nodes, exclusive lump/segment ownership, unique placed leaf IDs, resolved endpoints, no self-edges or duplicate resolved edges, dependency waves, and named cycle refusal. `document_refs.py` owns repository-qualified resolution, containment, role altitude, commanded-master membership, sprint linkage, and the module-level `repository_master_documents` census. A standalone nature-less or atomic master resolves at master altitude; an explicitly organizational standalone master still requires a sprint parent. That addressing exception does not supply a missing explicit nature to an authored DAG. Recovery diagnostics name `task_doc.author_execution_graph`. Exact command aliases resolve by canonical folder name, document ID, or title and must identify one master without duplicate aliases. An unreadable directly addressed directory refuses; unreadable other directories are skipped by this scoped exact-membership resolver. Missing-master diagnostics name the sprint and missing master, report an archive location when found, and explain restoration followed by retirement. Typed-row or graph checks can refuse before this diagnostic is reached.

`leaf_binding.py` owns the pure composite join between a master row and a direct child sub-task document. Parent kind/address, child kind/directory, row number, direct Markdown filename, derived JSON reference, document ID, and stem must agree; absent or ambiguous joins refuse. `semantic_topology.py` projects `semantic-topology/v2` from exact sprint/master/leaf refs, the uniquely bound parent row, effective nature, and candidate placement. Graph-less scheduling explicitly projects atomic-sequential placement and rejects a supplied DAG context. An authored graph requires an index bound to that graph and an explicit master nature. `semantic_topology_graph.py` compares authored/resolved canonical graph bytes, refuses work populations that exceed the budget before immutable admission, and builds one recursively immutable generation with placement and incident-edge indexes for bounded candidate reuse. These identities are semantic projections, not queue-private whole-document hashes.

`task_paths.py` is the single task-layout vocabulary below `worktrees`; `worktrees/task_resolver.py` re-exports it for its callers. Enclosure enumeration prunes notes/archive descent while retaining real `enclosures/<leaf>/series-contract.md` positions, including a leaf directory named `notes`. Foreign membership resolves the task artifact against the repository tasks directory derived from the contract's physical position, rather than trusting recorded roots; consumers own warnings and skipped-item detail.

`leaf_doc.py` provides case-insensitive identity matching by document ID, enclosure leaf ID, or filename stem. Its ordinary finder is fail-soft and returns the first matching readable nonmaster; terminal resolution is stronger, refusing blank IDs, duplicate matches, unreadable stem claimants, and invalid/mismatched asserted direct JSON paths. Blank-ID recovery names restamping the contract or branch-addressed direct execution. Lifecycle restamp planning fills absent derived master-link fields without rewiring existing bindings. Exact enclosure registration is different: it checks the canonical resolved document's address and can prepare a replacement enclosure entry for a missing or mismatched address, together with missing master linkage and an optional lifecycle stamp. Its no-op requires exact enclosure address, existing derived linkage, and any requested matching lifecycle. Completed candidates expose readiness blockers. The convenience `restamp_leaf_doc_lifecycle` definition has no other textual use under `mcp/src`; this observation is narrower than a dynamic reachability verdict.

`master_sync.py` plans same-root leaf-to-master updates, validates parent kind, refuses duplicate numbered rows and retired targets, checks an existing row's source path, and derives leaf ID/title/rendered filename/native status while retaining manual `scope`. A sub-task's cross-series master reference remains navigation metadata and receives no automatic write. A master instead uses the native commanding-sprint census and exact typed/legacy row correlation: several commanding sprints, unreadable naming documents or ambiguous rows refuse; an absent command/row supplies no invented write. The matched sprint row mirrors the master's own status. `folder_master_json_path` is the shared rule for an unnamed sub-task: use the existing folder `task.json`; named-master and non-sub-task documents return no folder fallback. Finalize and reopen consume that rule. `require_task_document_in_place` prevents rewriting a document to a different kind/slug-derived destination; their leaf and parent preparation paths apply it before writes.

## Invariants And Boundaries

JSON authority and generated Markdown remain separate. Prose intended to survive regeneration belongs in the model. Structured master sections preserve their authored bodies and render selected machine populations; this does not promise that every field on an arbitrary accepted master appears automatically in its view. Rendering itself is a data transformation, while persistence and disk-backed title joins own I/O.

Readiness is explicit. `completion_blockers` returns every unresolved declared step/substep or master row; an empty document is ready vacuously. Master rows are resolved by the shared `{Completed, abandoned}` set. `master_is_terminal` accepts `abandoned` independently, but accepts `Completed` only with no completion blockers. Abandonment is a deliberate terminal decision and need not finish untouched planning rows. It must not be collapsed into completed work.

Leaf-to-parent status projection mirrors the task document's native stage verbatim; step completion is progress, not a second stage authority. The former progress-based rollup is retired: even a readable legacy `Completed` document with inconsistent steps is mirrored as `Completed`, not silently reclassified here. Native start/abandon publish their stages, while finalize, reopen and explicit corrections retain their own admission and publication authority. Mirroring therefore does not itself prove landing or completion readiness. A synchronized completed master is still demoted when unresolved parent rows remain. Segment placement treats terminal predecessor masters as resolved; unplaced planned leaves derive placement in the latest unblocked segment by wave/declaration order, or the latest overall with an explicit all-blocked flag. Lump masters cover leaves implicitly; unknown placed and unplaced planned leaves remain distinguishable facts.

`document_field_effects.py` exhaustively classifies persisted root/nested fields into structural topology, normative intent, readiness, progress, evidence, lifecycle, and prose audit. Missing, stale, or empty classifications refuse instead of silently admitting schema growth. Mutation classification follows actual accepted/candidate differences. Progress/readiness, normative prose, evidence, and operational audit are not interchangeable.

`task_intent.py` hashes a validated, allowlisted normative projection using canonical JSON. Exact requirement strings remain normative and cannot be blank. Approved packet references supplement exact text; references without exact text refuse with an explicit v2-cutover requirement. Packet locators must be task-relative Markdown paths confined after resolution, before reading; recorded root/locator resolutions and locator-keyed byte identity expose retargeting even when target bytes are identical. Structured packet identifiers and version must match; repeated structured metadata fields refuse. Typed acceptance-obligation questions affect intent; ordinary questions and audit/progress notes do not. Master intent uses its own normative projection, combined with child identities by the review-scope owner.

`knowledgeMaintenanceScope` is optional lifecycle context, outside normative intent; its true header signals the inherited policy of classifying every memory-base entry. `expectedKnowledgeEffects` is leaf-only normative intent, shaped as subject/effect/requirement reference. Malformed, empty, or duplicate subject/effect declarations refuse, and absent declarations omit the optional digest slot. Task validation checks shape rather than reading knowledge existence. The inherited worklist policy distinguishes planned/unplanned effects and reports undelivered declarations as `planned_untouched`; task-field authorship is procedural rather than a per-field role gate, and the reviewer compares declarations against the packet.

`leaf_decisions.py` supplies strict task-owner answers. It scans the task folder's JSON population, rejects ambiguous claims and unreadable documents still naming the leaf, and resolves a cited decision timestamp only when exactly one decision matches. No document, no decision, and duplicate timestamps are distinct refusals. Inherited consumers must treat unresolved lookup as incomplete, not as an absent declaration or default scope.

Recorded-read behavior is owner-specific. `read_task_doc` records the original byte identity before parsing, or absence/unreadability on failed reads, preserving universal-newline parsing behavior. The source-pair reader, master-source parser, and disk title join also parse task JSON directly, so not every task reader automatically participates in that recorder. Strict lookup uses a nested recording scope: an established claimant replays its own rows plus nonplain-byte rows, while a no-claimant result retains all reads and the observed direct JSON listing. Expected resolution failures/broken claims replay their reads before refusal. Siblings read and ruled out by ordinary byte identity do not become dependencies of a successful leaf result; consumers retaining a result must re-establish the keyed lookup to expose a new claimant. A recorded consumed identity binds an answer to consumed bytes; it is not a complete history of intervening edits.

Route reviews retain candidate-tree identity, task intent, route evidence, and optional atomic-master scope/child identities. Partial content addressing refuses: evidence digests, verdict digest, dependencies, and record digest must appear together; the record digest is checked against canonical record bytes. Store publication rejects a present review with missing task-intent identity, but that local gate does not independently reread every evidence source or recompute current task intent. Dedicated application review operations own stamping and mutation authority.

Retirement rows are abandoned and carry no live `masterRef`; a legacy seat `file` may remain to preserve historical reachability. `sprint_rows.sprint_census` reads exactly the direct `<task root>/<folder>/task.json` documents and distinguishes commanding, retirement-recording, unreadable-naming, and other unreadable populations, including inaccessible task folders; a `task.json` deeper inside a task folder is not a task document and is never read, counted or listed. Finalization refuses unreadable documents naming its master; retirement refuses the entire unreadable direct-document population because archival cannot safely assume no unseen membership. The running-model preflight checks topology field availability and retirement-field availability before the corresponding authoring paths; it no longer discovers distributions, rejects editable installs, or enforces a wheel version floor.

## Historical And Verification Limits

This is a source-only proposal for the supplied checkout, not a test result, delivery receipt, aggregate memory acceptance, or authorization to publish. Original route/status/coverage metadata and reference identities remain parent-owned; indexes and the single aggregate sync remain separate work.

L11 and 260731-EFA-L6 explain why enclosure reopening moved from `tasks` to `worktrees`: rewriting both document and enclosure must not make the task layer depend upward. In the present checkout, shared reopen contract reset and frozen landing removal live in `worktrees/reopen_reset.py`, used by leaf and series reopen. Typed `ContractCells`/`amend_contract` reset review/closeout/integration/cleanup vocabulary, including `cleanup: reopened`; free-text/boolean resets use `replace`. The frozen landing record is removed so a reopened arc can acquire fresh landing facts, and reset failures remain visible. The historical L4 account of a missing reader vocabulary member causing a context-packet `ValidationError`, unchecked `replace` keywords, and byte-identical then-current output is retained as historical explanation, not re-proven here. Its old line numbers, claimed sole producer, and ledger-field reset list are not current owner assertions.

260718-CHATS-L5I's stale completed-landing concern and L23's task-first recovery of cleaned completed leaves remain intent: stable task identity must yield an actionable reopen plan before deliberately removed descendant branches are treated as lineage failure. This review does not certify every current lineage/recovery path.

260913-LCA-L5 records an earlier `tasks -> worktrees` import inversion, 17 violations/2 cycles versus 16/1 with those imports deleted, and subsequent relocation of path rules into `task_paths.py`. The named historical residual was the `memory_quality <-> worktrees` cycle and `worktrees -> memory_quality` edges. Those figures, the then-red layering rail, absence of a baseline/exception, and the corrected comparison are inherited historical witnesses; no checker was run here and their current repository-wide disposition is unverified.

The L15/L2 preflight history retains the 3.0.0rc7 incompatible persistent-write failure, restore/reapply concern, former noneditable wheel floor `3.0.0rc8`, and former typed distribution-discovery/metadata/read/stat/version failure boundary. Those describe a previous implementation. Current source checks the running model's fields and explicitly says task-plane edits do not consult installed distribution versions. Historical expected-error translation must not be presented as a present code path or fresh acceptance.

MIK-R38/D32 records divergent unnamed-master resolution leaving 15 rows stale, repaired by resync, and R1's risk of a misplaced light/master document overwriting canonical `task.json`. The inherited R2 read-only sweep of 557 sub-tasks and 39 masters with no refusals is historical coverage, not a sweep of this checkout. The exclusion of format migration and document migration remains the scope of that historical change. The current shared resolver and placement guard are source-confirmed; historical repair and delivery outcomes are not re-executed.

LOCR-L33's silently discarded top-level step note remains the reason for declaring, classifying, and visibly rendering `Step.note`. Current rendering also considers dispositions, so note-only and disposition-only steps have checkbox lines. CCR-L01, DAGQC L1, EFA-L9, and the retirement additions explain semantic projection, identity separation, shared vocabulary, and retained audit ownership without supplying new verification receipts.

The inherited L4 policy forbids topology edits from promoting live leaf branches into protected super/atomic refs, detaching live owners, or contradicting existing atomic-series edges under repository Git authority. The examined task-domain graph/authoring functions establish structural and judgment checks, not the complete Git-authority enforcement path. Likewise the inherited short-lock/task-plus-invalidation atomicity policy remains unverified at whole-call-path scope. Local absence of a guard or lock is not evidence of its absence from all callers.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/tasks/`                 |

## Review-base evidence

RouteReviewRecord.baseCommit is optional persisted review evidence and is classified in the EVIDENCE plane. Leaf construction stamps the base before its record digest; the field alone does not establish ancestry or currentness. Legacy None-valued fields remain omitted from digest verification. Task-intent, review-state and mutation-class owners remain separate.

## Evidence

- The persisted route-review record declares the optional base stamp. [56]
- The exhaustive field taxonomy classifies the stamp as evidence. [57]




- Retained reference account (no fresh execution or acceptance inferred): Canonical task intent is hashed from the validated normative projection. [1]
- Retained reference account (no fresh execution or acceptance inferred): Exact task text remains mandatory alongside supplemental packet references. [2]
- Retained reference account (no fresh execution or acceptance inferred): Task-document publication rejects a route review missing intent identity. [3]
- Retained reference account (no fresh execution or acceptance inferred): Mutation classification consumes the accepted/candidate field delta. [4]
- Retained reference account (no fresh execution or acceptance inferred): The `task_doc` application entry point authors documents through this package. [5]
- Retained reference account (no fresh execution or acceptance inferred): Leaf writes keep same-root master rows synchronized through the dedicated planner. [6]
- Retained reference account (no fresh execution or acceptance inferred): The task-document renderer regenerates markdown from the validated `TaskDocument`. [7]
- Retained reference account (no fresh execution or acceptance inferred): The persisted worktree contract is the analogous model-to-text precedent. [8]
- Retained reference account (no fresh execution or acceptance inferred): The persisted-contract peer this schema mirrors. [9]
- Retained reference account (no fresh execution or acceptance inferred): Task source snapshots and publication. [10]
- Retained reference account (no fresh execution or acceptance inferred): Application publication transaction. [11]
- Retained reference account (no fresh execution or acceptance inferred): Structural execution-node equality/hash and explicit reference ownership. [12]
- Retained reference account (no fresh execution or acceptance inferred): Qualified leaf-title join. [13]
- Retained reference account (no fresh execution or acceptance inferred): Ordinal Mermaid identity allocation and rendering. [14]
- Retained reference account (no fresh execution or acceptance inferred): The field. [15]
- Retained reference account (no fresh execution or acceptance inferred): Its classification. [16]
- Retained reference account (no fresh execution or acceptance inferred): Its header line. [17]
- Retained reference account (no fresh execution or acceptance inferred): The declaration model and its refusals. [18]
- Retained reference account (no fresh execution or acceptance inferred): The field on the task document. [19]
- Retained reference account (no fresh execution or acceptance inferred): Its normative classification. [20]
- Retained reference account (no fresh execution or acceptance inferred): The optional intent slot, absent when undeclared. [21]
- Retained reference account (no fresh execution or acceptance inferred): The header block. [22]
- Retained reference account (no fresh execution or acceptance inferred): The strict lookup and the decision answer. [23]
- Retained reference account (no fresh execution or acceptance inferred): The one rule for a leaf naming no master, and the sync's own call. [24]
- Retained reference account (no fresh execution or acceptance inferred): The placement guard. [25]
- Retained reference account (no fresh execution or acceptance inferred): The task reader records the bytes it parses, an absent file and a failed read. [26]
- Retained reference account (no fresh execution or acceptance inferred): The strict lookup replays the leaf's own document and every row that is not a plain byte identity when it established the claimant; with no claimant it replays every row it opened, each sibling read in full and the exact direct JSON listing included. [27]
- Retained reference account (no fresh execution or acceptance inferred): The packet owner: recorded resolutions, confinement before the read, bytes recorded under the caller's locator. [28]
- Retained reference account (no fresh execution or acceptance inferred): A retirement proof requires an abandoned row without a live master reference; a legacy seat file may remain. [31]
- Retained reference account (no fresh execution or acceptance inferred): The missing-master message names the sprint, the master, the archive location and the retire operation. [32]
- Retained reference account (no fresh execution or acceptance inferred): The retirement probe refuses a model that cannot parse a retired row. [33]
- Retained reference account (no fresh execution or acceptance inferred): Shared sprint census reports commanding, recording and unreadable populations with caller-specific refusal policy. [34]

- Task reads record consumed bytes; the source-pair reader parses retained bytes separately [35]
- Prepared writes use atomic replacements and restoration; publication only locally requires review intent identity [36]
- Strict lookup retains claimant/nonplain identities or all observations for no claimant [37]
- Completed master terminality requires no blockers; abandonment is independent [38]
- Parent-row stage mirrors the native task document directly, not a step-derived rollup or an independent landing verdict. [39]
- Master-to-sprint mirroring uses the native commanding census and exact typed/legacy row correlation with named ambiguity/unreadability refusals. [54]
- Kind separation, retained sprint identity, and leaf-only expected effects are explicit [40]
- Registration can replace a mismatched enclosure, while missing derived links are separately filled [41]
- Canonical placement guards derived write targets [42]
- Maintenance scope is lifecycle; declarations are normative; invalidation classes are limited [43]
- Exact requirements remain mandatory beside packets; resolution and confinement precede packet bytes [44]
- Partial review content addressing refuses and record canonical digest is checked [45]
- Current preflight checks model fields rather than distribution versions [46]
- Source comparison precedes ordered publication/invalidation/rebuild with reported projection failures [47]
- Shared reopen reset owns typed cleanup and frozen-landing removal [48]
- Exact membership applies scoped unreadability and alias ambiguity refusals [49]
- Immutable graph admission compares canonical bytes and refuses over-budget population [50]
- Retirement census explicitly preserves different caller refusal policies [51]
- Notes/dispositions independently make step checkbox lines visible [52]
- Title joins use qualified leaf keys and a separate direct JSON reader [53]

- A kept view ignores every task document it did not read. [29]
- A document that begins to claim the leaf is not hidden by a kept view. [30]

- Code reviewState and the post-landing memoryReviewState are independent persisted evidence lanes. Recorded rounds retain their kind and findings-remain facts for step-up counts; record-only checks add no try, and a memory result cannot reset passed code. Ordinary reads remain strict. The private launch-only fallback preserves malformed raw review evidence without making it a counted or accepted round; in-flight pre-rollout memory checks are not migrated. [55]
