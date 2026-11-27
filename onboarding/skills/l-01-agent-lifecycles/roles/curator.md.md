# skills/l-01-agent-lifecycles/roles/curator.md

## Governing Overview

[overview](overview.md)

## Purpose

Defines the curator’s current leaf and repository-foundation responsibilities: reconcile existing intent, ruled intent and implemented reality; maintain affected memory; author justified knowledge through the admitted writer; and report exact outcomes and unresolved limits.

## Foundation carrier and writer admission

The Curator seat opens only on a leaf task document. Repository foundation is regular task work: after setup reports memory and baseline state, the user starts the Architect, which opens the real foundation task — a registered leaf under a master — and the Curator starts on that task document and uses its actual enclosure contract. Before any task exists, Bootstrap reads and reports the foundation state and names the user-started Architect as the next step; no instructed session substitutes for task admission, and a missing task is reported rather than fabricated, as are a worktree and an enclosure. The writer routes, developer commit word and one-writer/independent-review boundaries remain distinct.

## Code Commentary

### Logic

`roles/curator.md` is a concise Tier-1 role manual (32 lines) stating Curator's leaf-only start, contract-scoped MCP and brief-opening rules, `ar:needs producer-list` intake contracts, producer-field preservation, single-writer (`knowledge_write` or serving-build CLI `--commit`/`commit: true`) and product-owned state boundaries, 3-repair stop, and `task_doc(set_step)` completion rule. Detailed procedures sit behind its `## Reference index` table: `reference/knowledge/{use,commands,serving-build}.md`, `templates/curator-handoff-ingestion.md`, `reference/curator/{intent-reconciliation,worklist,knowledge-ingest,publication-report,family-obligations,change-routing,encountered-records,current-prose-and-history,card-sentence-decisions,card-formats-and-citations,governing-sources,coherence-judgments,memory-handover,exceptions-and-recovery,repository-foundation}.md`, `reference/writing/technical-english-profile.md`, `reference/message-handover.md`, `reference/worker/sync-and-repairs.md#synchronize-the-leaf`, `reference/sandbox-actors.md`, and `operations/orientation.md#ask-for-a-developer-decision`.

The Curator opens briefs via `read_ar_files`/`context_packet` (`task_context`) and calls `knowledge_read` (`workspace.memoryRoot`), using `knowledge_read` `impact`/`search`/`records` before authoring. MCP calls are scoped with the leaf contract (else refresh blocks start), check `onboardingRoot`, and preview with `dry_run=true`.

Producer fields remain owned by their producer (no re-judge); Curator owns Curator fields (initialized `null`) and requires a passing `handoff-check`. `knowledge_write` / serving-build CLI (`commit: true` / `--commit`) writes `onboarding/` and `knowledge/` files in the leaf memory worktree without a Git commit; derived indexes are never edited by hand. Falsified claims are withdrawn; discoveries use `capture-candidate`, never current intent. Product sets status (`retired` to retire; decisions keep their own status). One Curator writer lane owns placement, admission, meaning, checks, and handover with no helper writers.

The Curator does not run Git writes, edit code/gate/lifecycle/contract/closeout state, start roles, create fake hashes/attestations, or set model/harness keys. It fixes faulty inputs on the same writer, repairs own/tool/coherence faults, stops after 3 failed repairs on one item and tells Manager, and marks curation `done` via `task_doc(set_step)`.

### Current onboarding judgment and second-reader duties

The new converted onboarding contract takes current source-bound updated/no_impact rows: updated requires authored Markdown/reference change, not realizes/proves-only or mechanical anchor edits; source movement reopens the answer.

Before closeout a seat that wrote none of the leaf's cards or records fact-checks every changed statement against final code, each history disposition/effect/reason against the diff and important omissions. Blocking findings are repaired. This is a lifecycle step, not a new automated closeout gate; full quality/coherence and Curator helpers do not supply independent acceptance.

- Independent non-author fact-check precedes closeout without adding a closeout predicate. [14]


### Bound native intake and admission

Read the rendered task-document files named in the handover with the harness's own file tools before acting; document changes go through task_doc only, since edits to copies are never read back. Use `arMcpContext.readerArguments` and each tool's actual schema; `task_context` carries both canonical task and enclosure contract. Resolve the named source/field before reporting it missing. Read immutable baseline/candidate knowledge before semantic changes, preserve the baseline, contain knowledge/onboarding outputs in the selected memory root and read admitted records back. Evidence/report outputs instead follow the task/scratch custody boundary stated above.

The existing MIK writer remains authoritative. Use only the source-bound command admitted for the selected runtime. If this compiled capsule exposes no writer and admits no such command, report the required records not written; that is a capsule capability limit, not a general absence of MIK’s writer. Another installation, unscoped call or internal writer cannot substitute.

An explicitly report-only admission supplies only the requested report and bound upstream message and claims none of the normal authoring pass complete. The normal pass retains its complete contract-scoped MQC, exact blocked findings, reruns and required prepare → publish → validate coherence. Developer questions go to the parent when one exists and to the own chat only without one; native peer clarification uses the actual parent/task role, and dashboard launch needs no parent. Operator settings, including serviceTier, remain outside Curator authority.

At its stage end an unfinished Curator sends what it awaits, and from whom, to its parent with `role_message` on `agents-remember-task`; its own chat text is not a return. Faults its own work or instrument causes — a faulty-input refusal, a wrong anchor — are repaired through the same admitted tool and reported, and a coherence finding on its writes is repaired rather than relabelled.

### Conventions

Canonical skills own instructions. Generated copies are synchronized artifacts; curate the matching sidecar against its own source path. One output list preserves the producer’s nine fields and fills only curator-owned decisions.

### Invariants And Boundaries

- Ground every record in accepted scope and real source evidence; do not create records to inflate coverage.
- Exact retained revisions are reused without rewriting old meaning or provenance.
- New membership edges are not new invariant revisions or semantic acceptance.
- A refusal or unexamined plane stays explicit; no favorable default substitutes for it.

### Todos

No additional work is asserted by this card. Actual project publication and semantic acceptance remain separately evidenced outcomes.

## Name the effect

When the curator restates a family's guarantee, the hand-off names the family as a
changed row with the curator's authored `effect`; the writer fills the family's own
revision. The changed-effect and writer-revision rule is in `reference/curator/family-obligations.md`, reached by the role's pointer before deciding family coverage or updating a family.

The overview contract reads from purpose: title, governing overview, then `## What This Repo Is`, `## What This Area Is` or `## Purpose`; construction follows, then invariants/boundaries, and all citation lines stand together at the end. An overview change belongs in its applicable body section, never a leaf- or date-named section. The instruction states these as authoring rules and names no validator refusal for them; source instruction is not evidence that a validation invocation ran.

The review budget is settings-owned (`orchestration.loops.defaults.maxRounds`), read at each begin; the task’s effective limit, including approved extras, is exposed by `task_doc.reviewState.limit`. CODE and MEMORY have separate counts under the same setting. Beyond-limit work needs recorded Architect or developer approval, which the Manager requests through its assigned reporting route and records.

The Worker passes the handover checks on a clean copy of the frozen candidate and hands the freeze report to the Reviewer. After code PASS, it runs the requirement’s listed final checks once on the passed tree and reports the results to the Reviewer and Manager. The Reviewer records whole-requirement coverage and its verdict. The Curator writes, checks and publishes knowledge through the installed build and obtains clean full quality/coherence evidence before handing MEMORY directly to the independent Reviewer. Each stage repairs its own input/instrument slips through the same admitted tool and continues; permission prompts, other correct-input refusals or unowned state, requirement-meaning questions and out-of-scope effects remain stops; covered correct writes follow only their scoped recovery.

## Landing evidence and retained intent

For every card cut by the quality check, the handover names the source evidence that makes the removed text untrue. Text is never removed merely to clear a quality finding. Evidence and working files belong to the task record, the hand-over's scratch root, or — for what must not live under the projects home — the hand-over's outside scratch root, never the memory worktree; durable onboarding and knowledge remain the Curator’s writable memory surface. This adds review content without transferring the one writer, full-quality loop or landing authority.

## Current composition and authoring contract

The role retains complete leaf-only intake, producer-field preservation, single serving-build writer, product-owned revision states, 3-repair stop, and `task_doc(set_step)` completion bookkeeping, routing detailed procedures through its `## Reference index` table (`reference/curator/*`, `reference/knowledge/*`, `reference/worker/sync-and-repairs.md#synchronize-the-leaf`, `reference/message-handover.md`, `reference/sandbox-actors.md`, `templates/curator-handoff-ingestion.md`, and `operations/orientation.md#ask-for-a-developer-decision`).

## Evidence

## Current account — the authoring routes

The role's authoring routes name the mounted `knowledge_write` beside the serving-build CLI (`--commit` / `commit: true`) under one Curator writer lane; missing writer is not a correct-input refusal, and derived indexes are never edited by hand.

## Scratch roots

`roles/curator.md` ends with its `## Reference index` table; scratch-root rules are carried by `core/every-role.md` and `reference/sandbox-actors.md` rather than an inline closing paragraph in `roles/curator.md`.


- Current Curator intake requires candidate-bound producer data and a passing handoff-check for the freeze, links intent-reconciliation and knowledge-ingest details, keeps one writer, marks only its completed own step, stops after three failed repairs on one item, and relies on operations/curation.md (full checks and OM-2 fact-check), reference/curator/exceptions-and-recovery.md (bounded named encountered-memory repairs and owner routing) and core/every-role.md (scoped covered-write recovery). The family-obligations detail attributes prepared-context unattributed code locations to their family or reports why not, and the change-routing detail retires deleted or renamed source cards while repairing every reference to them. [17]





- Before ingest, earlier subject rows are read and invariant disposition meanings stay distinct from family/onboarding schemas, alongside the Curator's candidate-bound intake, single-writer, own-step, three-repair stop and linked detail rules. [18]












- Current curation verifies card sentences against source, delegates bounded encountered-memory repairs (beyond quality-check findings, named, without a broad sweep) to reference/curator/exceptions-and-recovery.md, routes code concerns, requirement decisions and cross-leaf work to their owners, and requires full checks and the independent OM-2 fact-check before handover. [27]




- The Curator reads the required task, change-set, producer handoff and affected memory inputs. [1]




- Three-way reconciliation, baseline preservation, admitted-record readback and full quality-check duties, including the Manager-leaf-closeout stale dependent-document read. [2]




- The curator’s prohibited writes and source-stamp boundary. [3]




- The knowledge-ingest preparation detail requires each hand-off target’s own authored rationale before ingest; the writer never generates that rationale and refuses an unexplained target. [4]


- The governing-decisions detail lifts each ruling or packet choice that still constrains code into a decision record; task-only choices stay in the task. [5]


- The curator follows the card-format and citation detail: cards hold current prose and numbered evidence lines, and the citation fixer turns citation tables into those lines and sidecar references. [6]



- The admitted knowledge writer writes memory files in the leaf memory worktree; --commit (commit: true) authorizes those file writes, never a Git commit or acceptance. [7]




- Restated guarantees carry an authored effect; the writer fills the revision.



- The memory-review pass limit is the settings limit and a pass beyond it needs Architect or developer instruction recorded by the Manager; the role keeps its stage and authority boundaries. [9]







- The Curator batches citation checks and repairs, completes the full quality/coherence operation and hands memory directly to the independent Reviewer. Faulty inputs are corrected through the same tool; a covered correct-input write refusal uses the scoped recovery procedure with explicit provenance. Permission, validation, unowned-state, meaning and outside-surface stops remain. Extra memory passes require Architect/developer authority recorded by Manager. [10]





- Evidence and working files stay outside the memory worktree. Overview authoring is purpose-first, changes belong in their applicable body section, and all citation lines terminate the overview. [11]


- Via reference/curator/exceptions-and-recovery.md, every quality-check card cut requires source evidence proving the removed text untrue; cutting text merely to clear a finding is forbidden. [12]



- Repository foundation is authored by the Curator inside the real task the user-started Architect opens, a registered leaf under a master, with its actual enclosure. No taskless session or invented task, worktree or enclosure substitutes for task admission. [13]
- Repository foundation is authored by the Curator inside the real task the user-started Architect opens, a registered leaf under a master, with its actual enclosure. No taskless session or invented task, worktree or enclosure substitutes for task admission. [15]


- The worklist detail points to the writer's row, reconsideration and link-repair rules; the governing-sources detail records a rejected simplification or workaround with the chosen design, rejected option and reason, apart from unfinished work. [16]


- Normal knowledge authoring uses mounted knowledge_write or the admitted serving-build knowledge-ingest route. Only a covered correct-input refusal admits the same-tool/input-class recovery procedure, with owner notice, declared provenance and working checks. [26]





- A changed family guarantee carries a Curator-authored effect. The writer fills the revision. [8]





- The role directs opening available saved briefs before its source work. Compact rows can give applicable card status and a brief pointer with saved freshness. Fuller replies can include rule text. `knowledge_read` retrieves text-bearing views (`impact`, `search`, `records`, and `dependent`) paired with the code tree. [30]
