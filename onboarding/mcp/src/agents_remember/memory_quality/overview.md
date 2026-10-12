# Memory Quality

## Governing Overview
[mcp/overview.md](../../../overview.md)

## Purpose

`memory_quality/` owns the package's memory integrity and style checks, exact governed-memory census, converted knowledge validator, curator checklist rendering, and final memory-coherence certification machinery. It compares authored memory with the paired source and comparison trees, reports mechanical defects and review limitations, and supplies explicit refusal evidence to application and lifecycle owners. Mechanical validity, reference currentness, authored semantic judgment, operational readiness and certification are distinct responsibilities.

The route supports both legacy onboarding and converted text knowledge. The converted-format discriminator is `knowledge/layout.json`; applicability follows the tree being measured rather than a historical cutover date. The validator checks structure and declared relationships, not whether prose or an authored judgment is true. Curator judgment remains necessary even when mechanical checks pass.

## Hot Path Summary

Landing cut/add observations are report-only; use the measurement owner and canonical Curator/Reviewer duties for independent memory judgment.

`check.py` normalizes the selected names and dispatches the registered checks. Without drift context its default population is style-only; supplied context adds integrity. Required unavailable inputs must be visible in a result rather than interpreted as an empty success. Enforcing findings affect `ok`; report-only findings remain separately counted and sampled. Total counts and bounded detail samples have different meanings.

On legacy trees, drift compares verification metadata and source state; citation checks resolve ranges and reopen claims whose anchored evidence changed; document checks inspect shape and entity inventory alignment; Update History checking remains separate from its explicit fixer. Entity-catalog structure and citation checks are designated pre-refresh checks. The post-refresh population repeats citations without temporary provenance and includes drift, shape and history ordering. Temporary leaf-base provenance is comparison input for dirty unstamped claims, never a verification stamp.

On converted trees, legacy Update History ordering, citation range resolution and claim reopening return `not-applicable-converted`. The drift slot runs `knowledge.converted`: the complete knowledge validator plus report-only stale-reference observations. A supplied `KnowledgeBasePort` provides the converted comparison base and a named failure when it cannot be built. When that port reports failure, `R24.7-converted-base` refuses and the base-dependent `R22.6-anchor-path` refusals are withheld; independently measurable reference states remain reported. The no-port helper instead attempts converted memory `HEAD` and returns no bases when that read fails or `HEAD` is unconverted. These are distinct composition contracts; the named-refusal guarantee must not be generalized to every direct library call.

The application controller owns synchronous/start/poll transport and contract-scoped composition. Its completed whole result retains the computed finding populations; `application/memory_quality/answer.py` selects bounded blocking entries in repair, missing-onboarding and stale-index order. The controller computes that answer once and retains its status/recovery fields beside the whole result, keeping delivery sampling separate from full result retention. It revalidates scope before and after checking, binds the comparison-base port, checks candidate stability, and combines quality, missing onboarding, route-index alignment, governing-overview resolution and knowledge-gate findings. The full leaf-scoped run publishes one deterministic enclosure checklist and its structured attestation. Repository-only diagnostics do not establish candidate acceptance.

The checklist's actionable count is exactly repairable findings plus missing onboarding plus stale route indexes. Knowledge-review summaries, invariants without proof and the rendered knowledge worklist add no independent term. Open worklist items nevertheless become actionable through the application knowledge gate's repair findings. A zero checklist requires explicit source-candidate dispositions in the structured curator-coherence authority; a free-text readiness sentence or path mention is insufficient.

Interactive `finalFullCatalog` is a non-certifying readiness projection and supplies no affected-closure plan digest. Prepared closeout has a separate production composition: its application adapter compiles the affected-closure plan, executes that closure, runs full quality and missing/index observations, requires current coherence and the selected four-certificate prefix, and calls final memory-coherence certification. This source wiring establishes a caller, not a successful execution or delivery receipt.

## Construction And Ownership

`check.py` owns the public package runner, available-check population and pre/post-refresh populations. `integrity/onboarding_drift_check/` owns legacy discovery, classification and bounded summaries. Git reads use the kernel Git-command owner rather than private runners; its repository-selector isolation matters because a verdict must describe the named repository. `models/drift.py` owns the shared status vocabulary. The classifier packet uses required status and optional detail fields; consumers read optional fields with `.get`.

The converted drift summary is built from the converted checker alone. It names its basis, code and memory roots, successfully observed reference-bearing sidecar count, current/stale anchor counts, refusing validator count, report-only count, unreadable sidecars and bounded samples. Stale anchors supply its actionable count; refusing validator violations have a separate count. Sidecars whose references contain only non-code targets can count as sidecars without contributing code/test anchor counts. Unreadable sidecars are named and excluded from those counts. A failed converted-tree measurement returns an error without fabricated counts. A zero observation count therefore needs its unreadable/violation context; it does not itself prove the entire tree was readable.

Report-producing drift calls can write Markdown and a best-effort observer snapshot from the same result. The shared snapshot-path helper provides the producer/pruning/cleanup filename contract. Snapshots carry measurement time and pair provenance and are dashboard conveniences, not fresh acceptance. Explicit `write_report=False` suppresses both report and snapshot writes; the low-level output object's default is report-producing.

`integrity/check_missing_onboarding.py` owns the pre-code-commit added-source check. Its intended scope is current eligible worktree additions, not whole-repository adoption. Sidecar and inline storage have different absence/readability findings; unsupported storage or non-UTF-8 source is not silently treated as complete. Full prepared certification separately enumerates eligible source paths for its complete missing-onboarding population.

`integrity/governing_overview_resolution.py` resolves legacy declared governing routes. It only grades a card with a nonempty metadata `governingOverview` field. Field targets try card directory, onboarding root and its parent; the first Markdown link in the body's Governing Overview section is resolved card-relative. The two failures are independent. Missing sections or sections without links are observations, not repair obligations. Cards without the field receive no findings from this owner, even if they have a body link. The application publishes this result separately from the closed `checks` population and adds its findings to curator repairs.

`curator_checklist.py` owns deterministic grouping, the three-term count, report rendering and structured attestation. The report and JSON attestation are separate atomic replacements, not one atomic two-file transaction. The attestation binds pair identity, exact candidate trees through dependency records, onboarding root, report path/digest and the complete source-change candidate set. Missing provenance belongs to closeout only when the onboarding document is untracked; tracked historical debt remains repairable. Operational artifacts live outside both Git worktrees and their enclosure owns their lifetime.

`knowledge_review.py` renders recorded assessment links and counted `unresolved`, `stale`, `not-measured` and `partial-scope` limitations. Measured movement differs from absence of measurement. Negative or contradictory counts refuse summary construction; stale plus unmeasured cannot exceed assessment count, and dispositions correspond to recorded assessments. A subject without an assessment gets no disposition row. The implemented partial-scope calculation means missing comparison or scope references; its broader comment about matching the current scope manifest is not an implemented comparison here. The application summary reader reports already-published assessment authority and does not perform a new currentness measurement.

`knowledge_worklist_section.py` renders persisted worklist state, identity, digest, pairing, unreadable inputs and item facts. Planned effects retain declaration keys, requirement references, matching or unmatched reasons and whether a planned row answers them. Items expose planning marks, affected routes/entries, rename destinations, unmapped locations and labelled mechanical suggestions. Route items require a satisfying family row rather than `no_impact`; unexplained changes show hunk/file scope, coverage, realization counts and required authored/onboarding answers; delete-only hunks retain their `no_invariant` restriction. Reconsideration candidates expose addressed alternatives, changed targets, triggers and the need for a reasoned `still_rejected` or `raise` row. Onboarding trace facts are also rendered. Rendering these facts does not itself enforce or author an answer.

`memory_census.py` and `memory_census_scope.py` own exact governed-memory comparison. Scope names the canonical pair, code mode, candidate tree, baseline, working/committed/memory changes and the actual memory comparison tree, including a converted baseline where appropriate. `converted_cards.py` derives card kind/source from location and a matching-schema sidecar's declared path, using the legacy metadata vocabulary as an internal census shape. Mechanical anchor blob/line/content refreshes are distinguished from counted card edits through onboarding-trace comparison. Census identity proves Git inputs, not acceptance. `future_code_candidate.py` and `memory_candidate_pair.py` now belong to `worktrees/modules/`; the historical moves into this route do not make them current local owners. The preparation adapter belongs to `application/prepared_certification.py`.

`knowledge_validator/` reads directory or Git memory trees and paired code paths, parses authored files, applies one registry and emits sorted violations. Its imported rule modules cover structure, references, family routes, census, admission, decisions, reconsideration, history and overview order. The commit API applies whenever the candidate or any comparison base is converted, including merge parents. Standalone conversion is an explicit mode with specific exemptions, not a general commit-rule bypass.

`knowledge_census/` owns byte-oriented migration-census parsing, integrity checks, measures and reports. Its Git inventory and writer belong to `memory/knowledge_census/`. Baseline/inventory are pinned; claim identity, text, location, kind and applicability remain stable; linked records and routes must resolve. Status and assessment histories grow by prefix against one base and by subsequence against merge parents. The assessable cohort preserves `N = T + F + U + P`; non-claims and historical non-applicable claims remain counted outside it. Measures stay separate, include their counts, and treat zero denominators as not applicable. Realization/relevant truth coverage remains not applicable without a reference inventory. The latest status across censuses governs each route, without mechanically deciding assessment truth.

`final_certification/` owns the complete catalog, prerequisite-prefix validation, exact semantic-input assembly and typed green/red/blocked result. Shared typed certification models are imported from the certification layer; they are not all locally declared here. The API consumes caller-supplied checker results and does not itself launch those checks. Its attestation compares the executed population with the plan. Only green is finalization-eligible. `gate_five_rails.py` contributes deterministic enforcing memory-domain rails whose configuration binds catalog/registry versions and population; declaring rails does not execute them. `incremental_scope/` provides dependency scope, affected planning/execution and content-addressed subresult machinery used by the prepared application composition.

The knowledge validator refuses deletion of any record a comparison base holds: retirement retains its file. A merge-moved disagreeing row is report-only only outside leaf publication; at publication every mismatch refuses. These narrow mandatory invariant checks are not the full curator memory-quality operation.

### Landing observations, not another gate

`landing_report.py` owns the shared measure: at least eight removed base lines and strictly more than twice the added lines, with order-insensitive multiset deltas. It observes shortened/removed cards and overviews, exempts only proven leaf source deletion when code sides are known, and follows code-named Git renames. It also inventories candidate additions outside `onboarding/`, `knowledge/` and `system/`, retaining sizes and the sum without following symlink targets or counting Git administration. The converted drift slot includes these report-only rows by default; application callers bind the admitted contract base independently from the validator base, and bare diagnostic callers retain their comparison-base fallback. Neither population changes refusing findings, `ok` or the actionable count. The drift-summary reader explicitly uses `include_landing=False`, so its validator/reference counts and conditional report/snapshot filing remain separate. Complete full-leaf rows belong in the enclosure checklist and whole-result log, never as working evidence inside memory.

## Invariants And Boundaries

The inherited policy requires passing complete converted knowledge validation before memory commits. `require_valid_commit` enforces that policy for its applicable calls and has no rule-selection or skip parameter. Registry report-only flags never refuse. `writer_reports` is narrower: designated rules remain refusing in validator/commit reports while the writer may treat them as reports during incomplete leaf work. This local API evidence is not an independent audit of every possible Git-writing path.

The validator judges declared structure, identity, references, ownership, route membership, anchor path existence and history preservation. It does not establish prose meaning, reference-content currentness, plausibility of a justification or the truth of an assessment. Newly introduced anchor paths and routes differ from unchanged carried ones: missing carried paths/routes are report-only maintenance observations. Standalone conversion carries rather than authors anchors and has no paired code tree for those existence checks.

Family routes are evaluated over realizations, never proof entries. Added routes must exist in the paired code tree; realizations need coverage and routes need members. Retired families are exempt. Unrealized families waive non-empty and are reported; exported legacy-unassessed routeless families retain their route-assignment exemption. Suggestions are labelled mechanical and never written by this validator. Appropriate route breadth/depth remains curator judgment.

Admission governs creation. A record is new when no base holds its ID and it is not a genuine derived-ID export. Decisions are never exports. Retired invariant/family records are exempt from admission refusal. New records refuse legacy-unassessed admission, reference-only justification and unsupported mechanically checkable `spans_locations` or `guarded_by_test` criteria; missing criterion shape is rejected earlier. Existing/exported unsupported claims and live unassessed counts are reported. Multiple realization files and proof entries are observed directly from sidecars, not by importing the derived-index layer. Other criteria and plausibility require human judgment.

Decision content requires at least two alternatives, exactly one chosen alternative, and reconsideration conditions for rejected/deferred alternatives. Stored `superseded` is refused from raw JSON because supersession is derived. Reconsideration links must address an in-range non-chosen alternative. Missing governing links are reported. These rules apply to new and carried decisions; task-origin shape and requirement-endpoint resolution have their own owners. Linked alternatives preserve index against every comparison base by following unique option text from both sides. Rewording in place and appending alternatives are allowed; simultaneous move-and-reword and duplicate option text remain explicit limits of that matching method.

All history-row record subjects must resolve, including retired records. Re-anchor checking reads open histories and, at leaf publication, histories not already closed in a base or supplied frozen commit. A locally set closed flag is not a waiver. Previously closed histories preserve the historical tree they described. Across an owner's attempts only its latest row about a subject is re-anchor-checked. A later disposition may not hide an unlanded `changed` invariant/family judgment: invariant change can remain changed or become deleted; family change can remain changed or become retired. Merge-created mismatches whose identical parent row formerly agreed are reported for the next leaf gate; preexisting mismatches refuse. Revision/examined-member currentness belongs to the gate rather than this structural validity check.

The additional `R48-family-judgment` rule requires new/edited changed family judgments in published history files to carry their own revision and authored effect. Authored revisions must agree with the candidate family. Exact rows already recorded in bases or closed frozen histories retain the historical exemption; merely reusing an ID or setting the candidate closed flag does not create that authority. This rule is refusing and has no writer-report flag.

Overview rules require the first level-two section after an optional Governing Overview to be `Purpose`, `What This Repo Is` or `What This Area Is`; reject leaf/date section headings; and place numbered citation lines together in the final section's trailing citation region. The rules parse ATX headings outside fences and marker syntax outside escaped/code forms. Once that region begins, only citation lines, blanks and fenced-code lines are permitted. These checks remain refusing and imported into the same registry, but return during standalone conversion or outside leaf publication. Leaf closeout/direct or recorded landing activates them; baseline adoption/status, census and ordinary writer validation do not. Curation conforms adopted scaffold stubs before publication rather than blocking their adoption.

Converted reference checking reports code/test anchors as current when their blob matches or located content still hashes identically; absent paths, ambiguous/unresolved symbols or changed content are stale. Staleness is report-only here and routes through onboarding refresh/gating rather than becoming a new refusal in this checker. Mechanical fixing re-records only unchanged-content movement, requires unique exact-byte recovery for moved ranges, and never rewrites stale claim meaning, notes or target lists. One-sidecar scope restricts the reported population. The application `citation_fix` composition also accepts named-document batches: each converted card is authored and mechanically refreshed separately, refused cards remain excluded from refresh, and a missing name refuses that card without stopping independent siblings. This batching changes scope and transport, not authority to rewrite stale meaning. Authoring-refused sidecars are excluded from mechanical refresh/write so refused card bytes remain preserved while independent siblings can proceed. The exclusion is checked after sidecar enumeration/parsing; it is not a promise that excluded sidecars are never read.

Legacy citation repair admits exact unique moves through the shared source-index authority. Cross-file retargeting additionally requires that no cited file survives, the sighting is unique, the anchor existed at the document's honest verification point, and its extent kind is unchanged. `anchor_left_live_file`, `anchor_continuity_unproven` and `anchor_kind_changed` name distinct refusals. Deletion alone is no continuity proof. The migration relocation composition shares this authority, while the card records that its continuity branches were unreachable from that entry point by construction.

A changed construct whose citation remains uniquely current normally supplies report-only semantic review, including a whole source file absent at the stamp. Absent, ambiguous or out-of-range evidence remains hard. Generated mechanical-projection history changes that boundary: matching projected claims ask whether the new evidence supports the words and are enforced rather than treated as already reviewed. Ordinary evidence-change review stays a warning; preexisting-provenance demotion applies only to invalid-provenance debt, and absent Git authority does not demote findings. Format-only reflow and unrelated constructs do not reopen a claim; changed resolved dependency versions can. A dishonestly advanced verification stamp can hide an unreviewed change and remains beyond the check's proof.

Legacy document transactions bind complete original bytes, source-cell/projection inputs and the held frozen index lease, compose generated history with cell edits, and refuse the affected document batch on conflict. Independent documents can still publish. LF/CRLF bytes are preserved. Preview validates a prospective digest without completing writes. An admitted document disappearing after conflict cannot become a successful empty post-scan; initially missing input refuses before source acquisition. Atomic replacement prevents partial files but provides no mutex against an uncooperative writer between final read and replacement, and lease identity is not a new live-source freshness check.

Legacy Trees acquisition combines settings exclusions, recorded `.gitignore` rules and caller exclusions into one generation-bound register. Settings accept the documented onboarding/root locations and malformed values refuse by name. Git owns ordinary Git-worktree membership; the bounded non-Git matcher deliberately permits a negated child under an excluded parent, unlike Git's reinclusion restriction. Converted check/fix returns before this acquisition route and does not forward caller globs; document selection and authoring-refused-sidecar exclusions are its separate scope mechanisms.

Index schema 10 records the exclusion register; incompatible older manifests require rebuilding rather than silently losing population rules. Default source limits remain 4 MiB per-file, 512 MiB aggregate after exclusions/skips, 2 GiB hard stop, 100,000 files and 256 MiB database. Per-file cap skips must name file/size; aggregate/index failures remain actionable named states rather than bare client errors or silent omissions. The quality runner catches source-index acquisition errors, and prepared admission has its own typed refusal. Explicit Git candidate selection binds membership separately from content, admits eligible tracked build/ignored paths, excludes Git metadata and refuses unsafe/unavailable/mismatched members. Ordinary filesystem traversal retains its eligible dirty/untracked population. Candidate-bound R06/R07 lease and membership evidence do not by themselves establish final certification.

The inherited operational policy keeps style checks from blocking the start of normal implementation, places new checks under the appropriate style/integrity responsibility, and reserves mechanical rewrites for focused apply owners. Quality measurement does not repair code or memory; operational report publication is an explicit separate effect outside their worktrees. Curator reruns full contract-scoped quality until repairs reach zero. The legacy refresh policy assigns real commit-derived stamps and once-then-recheck behavior to closeout; converted history traces and exact-output knowledge guards are distinct. This policy does not establish that every ordinary transaction automatically executes the complete quality or certification sequence.

Preview and apply should share eligibility meaning. Historical deliberate exceptions remain named: `worktree_start` omits two reservation-binding checks from preview because they are inseparable from compare-and-swap; carryover apply additionally requires ordinary checkout and cleanliness; abandon/cleanup historically evaluated blockers but differed in verdict/state vocabulary, with cleanup summary omitting blockers. These are inherited exception accounts, not freshly verified behavior at this source head. Prefer shared eligibility evaluation; a prospective plan is not proof that apply enforced or completed it. Legacy migration preview separately distinguishes call success from `planned`/`converted`/`refused` state and outcome, and does not read post-write remaining findings during dry run. Definition-outside-range reporting remains diagnostic rather than changing its enforcing count; GFM pipe unescaping is a bounded cell-to-anchor normalization, not a general escape parser.

## Historical And Verification Limits

This body was adjudicated from the pinned source checkout and the complete input card without executing product entrypoints, tests or certification. It proposes narrative changes only. The parent preserves the original metadata, reference identities and targets; no lifecycle status or acceptance receipt is assigned here.

The former SQLite-era `family_review.py` pipeline and its five-owner status composition are retired accounts, not current ownership. Preserve their intent: grouping must retain all matched conditions and supporting paths/edges; movement, failed measurement and no measurement are distinct; stale records remain readable without reuse; missing assessments are not clearance; semantic conclusions are authored rather than inferred from labels, rationale, bytes or counts. The historical six-state projection vocabulary was `none-recorded`, `stale`, `unavailable`, `unresolved`, `not-measured`, `current`; there was no compatible/default clearance. The three-term actionable formula and factual checklist boundary endure through current owners.

Earlier statements that validation/gating was inert because no production tree had the layout marker describe pre-cutover conditions, not present deployment facts inferred from this checkout. Similarly, historical no-caller/pending-Gate-5 claims are superseded as source ownership claims by the prepared adapter and closeout port, while successful deployment and delivery remain unestablished here. Red certification evidence cannot authorize memory-content preparation.

The preview-parity ledger/cache account was explicitly superseded by the two-output Git transaction account. Historical private candidate `b34f4a59562b76a3e2413027468e0f699117b36f` is not fresh evidence. The old D32 statement that readiness comparison is reached only after raw `ready-for-closeout`, and that no master leaf had reached it, remains a named historical reach limit; its former execution witness was not established here. The historical refusal to gate missing Governing Overview sections avoided 96 new obligations; that number is not a current census.

The retired whole-new-file regression suites do not prove present coverage. Historical 115 unresolvable findings, 120 definition-outside-range rows, 283 enforced findings and three wrapped-citation constructs in two documents describe their old populations only. The response-address truth table and decoy-Git-selector test are named historical witnesses, not tests rerun here. The historical test-file capacity of 1199/1200 lines and its requested split is not a fresh capacity measurement. The old R2-3 citation-location discrepancy around `_refuse_official_memory` remains historical, not a relocated current source claim.

The linked-alternative reorder experiment used pre-rule scratch `31d761a2`; that scratch and its measured refusal contrast are not re-established. Its enduring algorithmic limits are retained: duplicate option text and a move combined with rewording are not tracked by unique-text matching. Old notes carrying reviewer work to L31/L32, admission/landing work to L09, and demotion/census follow-up to R19 remain historical allocation notes rather than new implementation assignments or completion claims.

The historical preview exceptions, migration continuity reach limit, unavailable semantic review proof, dishonest-stamp limit and memory-file mutex gap remain explicit wherever their original execution witnesses were not accessible or were not examined. Present source can corroborate a predicate or caller; it cannot turn any of those historical delivery/test accounts into current acceptance.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/memory_quality/`  |

| Source File | Onboarding | Status |
| --- | --- | --- |
| `future_code_candidate.py` | [../worktrees/modules/future_code_candidate.py.md](../worktrees/modules/future_code_candidate.py.md) | **relocated out** by `806649b9`; card moved with it |
| `memory_candidate_pair.py` | [../worktrees/modules/memory_candidate_pair.py.md](../worktrees/modules/memory_candidate_pair.py.md) | **relocated out** by `806649b9`; card moved with it |
| `memory_census_scope.py` | [memory_census_scope.py.md](memory_census_scope.py.md) | covered |

## Evidence
- Retained reference account (no fresh execution or acceptance inferred): The MCP application entry point builds drift context, including temporary leaf-base provenance, and calls the package runner. [1]
- Retained reference account (no fresh execution or acceptance inferred): Tool metadata and server registration expose `memory_quality_check` to agents. [2]
- Retained reference account (no fresh execution or acceptance inferred): The update-history fixer is a dedicated mutating module rather than a `memory_quality_check` option. [3]
- Retained reference account (no fresh execution or acceptance inferred): The missing-onboarding checker catches newly added worktree files before code commit. [4]
- Retained reference account (no fresh execution or acceptance inferred): The shared drift model declares the vocabulary used by drift-check wire responses. [5]
- Retained reference account (no fresh execution or acceptance inferred): The context-packet application entry point that returns `DriftSummaryPacket` from its drift seam. [6]
- Retained reference account (no fresh execution or acceptance inferred): The curator checklist renderer owns deterministic grouping, closeout-provenance separation, and atomic publication. [7]
- Retained reference account (no fresh execution or acceptance inferred): Memory candidate identity excludes consumer cache availability. [8]
- Retained reference account (no fresh execution or acceptance inferred): Projection admission precedes staging; declined claims retain their original bytes. [9]
- Retained reference account (no fresh execution or acceptance inferred): A relocation proves continuity through the established provenance path before a tree-wide match is admitted. [10]
- Retained reference account (no fresh execution or acceptance inferred): The walk resolves one document's continuity and feeds it to the planner. [11]
- Retained reference account (no fresh execution or acceptance inferred): The migration pass consults the same continuity authority before a cross-file relocation, although its continuity branches are unreachable from that entry point by construction. [12]
- Retained reference account (no fresh execution or acceptance inferred): A mechanically projected range is ENFORCED at `error` severity with the support question instead of asserting currency; the ordinary evidence-change item stays `warning`. [13]
- Retained reference account (no fresh execution or acceptance inferred): Accepted batches check complete document bytes and held source/cell bindings before atomic publication. [14]
- Retained reference account (no fresh execution or acceptance inferred): Complete catalog items become deterministic memory-domain rails and a population-bound configuration digest. [15]
- Retained reference account (no fresh execution or acceptance inferred): The application surface projects readiness with no affected-closure plan. [16]
- Retained reference account (no fresh execution or acceptance inferred): Full certification requires explicit evidence and predecessor authority supplied by its caller. [17]
- Retained reference account (no fresh execution or acceptance inferred): The one construction point folding settings, ignore file and call into one register. [18]
- Retained reference account (no fresh execution or acceptance inferred): The two settings keys, and the refusal-by-name discipline for a malformed value. [19]
- Retained reference account (no fresh execution or acceptance inferred): The bounded non-Git matcher and its pinned divergence from Git. [20]
- Retained reference account (no fresh execution or acceptance inferred): A caller exclude that cannot mean anything is refused by name. [21]
- Retained reference account (no fresh execution or acceptance inferred): The ruled numbers, the skip vocabulary and the status vocabulary. [22]
- Retained reference account (no fresh execution or acceptance inferred): The register's three sources and recorded authority values. [23]
- Retained reference account (no fresh execution or acceptance inferred): The closeout gate refuses by name rather than letting a bare error out. [24]
- Retained reference account (no fresh execution or acceptance inferred): The caller-exclude surface on the registered tool and the CLI. [25]
- Retained reference account (no fresh execution or acceptance inferred): One root gives one authority on both acquisition routes. [26]
- Retained reference account (no fresh execution or acceptance inferred): The index opens either the explicit candidate selection or the ordinary filesystem policy. [27]
- Retained reference account (no fresh execution or acceptance inferred): R06 checks candidate selection and exact indexed membership. [28]
- Retained reference account (no fresh execution or acceptance inferred): R07 validates and forwards the unit candidate tree to its selected-document checker. [29]
- Retained reference account (no fresh execution or acceptance inferred): The package's module map and public API. [30]
- Retained reference account (no fresh execution or acceptance inferred): The single registry. [31]
- Retained reference account (no fresh execution or acceptance inferred): The commit route's call, with no skip parameter. [32]
- Retained reference account (no fresh execution or acceptance inferred): The Git adapter the worktree port binds to. [33]
- Retained reference account (no fresh execution or acceptance inferred): The registered rule sets, with their report-only flags. [34]
- Retained reference account (no fresh execution or acceptance inferred): One family's route state over its members' realizations. [35]
- Retained reference account (no fresh execution or acceptance inferred): The six registered rules, three report-only and three writer-reported. [36]
- Retained reference account (no fresh execution or acceptance inferred): The registry flag a writer reads. [37]
- Retained reference account (no fresh execution or acceptance inferred): The nine census rules. [38]
- Retained reference account (no fresh execution or acceptance inferred): The measures in Doc12's order. [39]
- Retained reference account (no fresh execution or acceptance inferred): The registration with the validator. [40]
- Retained reference account (no fresh execution or acceptance inferred): Stale references are report-only. [41]
- Retained reference account (no fresh execution or acceptance inferred): The converted run's legacy-format checks and its validator slot. [42]
- Retained reference account (no fresh execution or acceptance inferred): The runner's dispatch by format. [43]
- Retained reference account (no fresh execution or acceptance inferred): The commit route's optional base converter. [44]
- Retained reference account (no fresh execution or acceptance inferred): The escaping rule on the validator's grammar. [45]
- Retained reference account (no fresh execution or acceptance inferred): The one symbol-binding rule. [46]
- Retained reference account (no fresh execution or acceptance inferred): The defaulted input and its section. [47]
- Retained reference account (no fresh execution or acceptance inferred): The section and the summary. [48]
- Retained reference account (no fresh execution or acceptance inferred): The checklist's defaulted inputs. [49]
- Retained reference account (no fresh execution or acceptance inferred): The fixer's converted-tree early return. [50]
- Retained reference account (no fresh execution or acceptance inferred): The planned-effects block and the `planned_untouched` facts. [51]
- Retained reference account (no fresh execution or acceptance inferred): The item table's **Plan** column. [52]
- Retained reference account (no fresh execution or acceptance inferred): A new record is refused for an unsupported claim, legacy-unassessed or a reference-only justification. [53]
- Retained reference account (no fresh execution or acceptance inferred): An export is a record whose legacy ID derives its ID. [54]
- Retained reference account (no fresh execution or acceptance inferred): The three rules, one refusing and two report-only. [55]
- Retained reference account (no fresh execution or acceptance inferred): The route item's facts, its affected set and its suggestion text. [56]
- Retained reference account (no fresh execution or acceptance inferred): The kind-to-renderer table (since MIK-R10 it also maps the two unexplained kinds). [57]
- Retained reference account (no fresh execution or acceptance inferred): The five rules, four refusing and one report-only. [58]
- Retained reference account (no fresh execution or acceptance inferred): A stored superseded is named from the raw document. [59]
- Retained reference account (no fresh execution or acceptance inferred): A decision is never an export for admission. [60]
- Retained reference account (no fresh execution or acceptance inferred): An unexplained item's facts: where, coverage, delete-only, and what answers it. [61]
- Retained reference account (no fresh execution or acceptance inferred): The two unexplained kinds in the renderer table. [62]
- Retained reference account (no fresh execution or acceptance inferred): Moves followed from both sides by unique option text. [63]
- Retained reference account (no fresh execution or acceptance inferred): The refusing guard, registered on import. [64]
- Retained reference account (no fresh execution or acceptance inferred): A reconsideration item's facts. [65]
- Retained reference account (no fresh execution or acceptance inferred): The files the re-anchor check reads. [66]
- Retained reference account (no fresh execution or acceptance inferred): The refusing and the merge-reported rule. [67]
- Retained reference account (no fresh execution or acceptance inferred): The registering import. [68]
- Retained reference account (no fresh execution or acceptance inferred): The leaf-publication route of the adapter. [69]
- Retained reference account (no fresh execution or acceptance inferred): The section's lead: the gate counts each open item. [70]
- Retained reference account (no fresh execution or acceptance inferred): A converted card's kind and source. [71]
- Retained reference account (no fresh execution or acceptance inferred): What the task edited on a converted tree. [72]
- Retained reference account (no fresh execution or acceptance inferred): The converted check's bases. [73]
- Retained reference account (no fresh execution or acceptance inferred): The re-recording scoped to one sidecar. [74]
- Retained reference account (no fresh execution or acceptance inferred): A history file closed in a base or a frozen commit is left out of the re-anchor check. [75]
- Retained reference account (no fresh execution or acceptance inferred): A later row of another disposition that would replace the leaf's changed row is found. [76]
- Retained reference account (no fresh execution or acceptance inferred): The drift item of a converted tree is the converted check's result. [77]
- Retained reference account (no fresh execution or acceptance inferred): Adoption-only card discovery is sorted and root-relative; unreadable files remain with validator/drift owners. [78]
- Retained reference account (no fresh execution or acceptance inferred): Mechanical refresh skips sidecars refused by citation authoring before refresh/write. [79]

- Format dispatch substitutes converted validation and retires three legacy-format checks; complete counts and samples remain separate. [80]
- Named converted-base refusal depends on the supplied port; no-port HEAD reads can yield no bases; reported base failure withholds anchor-path refusals. [81]
- One registry includes the working-tree overview rules; applicable commit calls refuse failing reports without a subset parameter. [82]
- Purpose heading, leaf/date heading and trailing citation rules refuse, with standalone-conversion exemptions; their implementation is presently an untracked working-tree file. [83]
- Checklist actionability has three terms; operational report and attestation receive separate atomic writes and exact bindings, and the returned whole result retains the three blocking populations. [84]
- Governing resolution requires a metadata field, tests field/body independently, and observes missing body links. [85]
- Converted summary names measured counts and unreadable sidecars; report/snapshot writes are conditional. [86]
- Currentness is mechanical and report-only; scoped fixing excludes refused sidecars before refresh/write, after parsing. [87]
- Family judgments newly published or edited require authored effect and their actual revision; exact historical rows are exempt. [88]
- Interactive catalog projection supplies no affected-closure plan and does not claim certification eligibility. [89]
- Prepared application composition actually invokes affected planning/execution and final certification. [90]
- Prepared closeout invokes the registered producer and refuses its absence. [91]
- Certification consumes explicit executed-check evidence and only green permits finalization. [92]
- Document preview and publication revalidate original bytes and held lease; publication then atomically replaces bytes. [93]

- Overview-order rules activate at leaf publication, not conversion or ordinary adoption/census/writer validation. [94]

- report-only landing measurement with separate read-summary scope [80]
