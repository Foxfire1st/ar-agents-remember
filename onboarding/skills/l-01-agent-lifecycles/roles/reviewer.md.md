# skills/l-01-agent-lifecycles/roles/reviewer.md

## Stage end and round recording

The whole requirement verdict, findings and coverage ends this independent stage. Reviewer records ordinary begin/result within the actual review-state settings limit; Manager records architect/developer authorization beyond it. A record-only check preserves the last round only on byte-identical candidate with all candidate findings closed. A finding states the broken required property; a case is its proof, not a replacement finding or automatic new round. MEMORY stays a separate sealed lane.

## Landing evidence in the independent memory lane

The independent MEMORY review reads both landing populations in the quality result. Removed text without a named change is a finding; an added file outside the knowledge without a place in the task requirement is a finding. These are human judgments, not automatic refusing diagnostics. CODE evidence, MEMORY findings/pass count and Manager acceptance/transaction authority stay separate.

## Message/file transport

This canonical role/operation requires messages to be short wake-ups naming requested work or a handover and its files. Report, verdict, list and evidence contents travel through file-only `body` or existing-file `attach`, not pasted into message text. Within a shared task, files stay with its record and a leaf workspace exposes the message-folder link. Text uses the effective settings limit without a pinned number. The canonical source and the packaged copy the tool server serves share this contract; transport does not change their existing write/start powers, peer destinations or independent acceptance authority.

## Governing Overview

[overview](overview.md)
## Purpose

This is the canonical independent-review lifecycle. It inspects the exact candidate and adjudicates
each stable requirement ID from the same applicable set dispatched to the worker.

## Code Commentary

### Bound native review intake

Review only the owner’s explicit assignment. Read the rendered task document and canonical JSON at `documents[0].taskDocReadArgs.rendered_path` and `documents[0].taskDocReadArgs.json_path`, and use the tools on `agents-remember-task` only, with `arMcpContext.readerArguments` and actual bound schemas; per-call context includes the canonical task and enclosure contract. Read only the documents required by the assigned seam and write only contained task-local report artifacts. Missing fields/capabilities are reported gaps, not permission to switch AR servers or retrieve unscoped material.

The baseline inspects every changed file in the complete candidate, including unattributed files. Knowledge before/after, family interactions and unchanged sibling realizations add a review dimension rather than reducing that population. Preserve producer Curator hand-off fields for co-resolution. Peer clarification uses `role_message` with the handover's sibling role and exact leaf task references — the Worker about the candidate, the Curator about memory; a dashboard Reviewer needs no parent and starts no role. Developer questions go to the parent when one exists; without one they stay in the own chat.

### Logic

The leaf seam is organizational leaf route review. Its verdict still goes to Worker, code PASS also to Curator and the memory verdict to Curator. Atomic-master, master-exit and portfolio seams retain their own bindings/destinations.

The reviewer does not accept a worker assertion at face value. For every stable ID it independently
opens the implementation/deliverable and verification citations, checks the evidence class, and
records `accepted` or `rejected` with its own rationale. Missing rationale, invalid citations,
wrong-class evidence, or an absent durable developer ruling for blocked/changed delivery forces
rejection. One rejected ID prevents an overall pass.

The first citation check is the version-addressed canonical packet itself: its ID/version must
match, its state must be approved, and it must carry the durable corpus ruling. A task summary or
worker paraphrase cannot substitute for that approved revision.

Adjudication binds the exact immutable worker attempt, leaf manifestation, and candidate. The
reviewer appends its own record without editing the worker record and classifies each rejection
with one of five exact classes. Accepted attempts remain closed; a finding alone cannot reopen accepted work or
extend scope.

The worker record is lightweight: the reviewer verifies its requirement-specific status,
rationales, citations, findings/failure class, and the digest plus exact anchor of the immutable
expanded evidence. Internal implementation/test/evidence protocol events may support a claim but
are never adjudicated as worker attempts and never inflate attempt or rejection counts.

The append target is the same single physical leaf journal that contains the worker attempt. The
reviewer's separately authored verdict links that journal anchor instead of duplicating the
adjudication as another authority.

**The declared knowledge effects.** Step 7 (`:73`) also checks: when the leaf's task document declares `expectedKnowledgeEffects`, the reviewer checks
that declaration against the leaf's requirement packet — its declared subjects and effects match what the
packet requires, with no effect missing and none invented — and a mismatch is a finding. The check is stated inline in step 7; it is not a criteria catalog entry. Who writes the declaration stays procedural; `task_doc` has no per-field role gate.

Beside the verdict, the reviewer emits **its own curator hand-off list** (`:93`) — its verdicts and
findings in the shape `../templates/curator-handoff-list.md` owns, as data rather than as verdict prose
for the curator to re-read. Each entry is one finding or one requirement adjudication, carrying the
source it came from and the place it was found at, and a finding the reviewer minted carries its own
stable ID; the list is what the curator ingests. It is emitted **in the same list shape the worker
emits**, because the curator consumes one contract: it names where the thing lives rather than where
the reviewer looked — the path and the construct inside it come from one resolution act — and carries
the reviewer's own statement and evidence verbatim rather than re-telling them.

**Neither a weakness record nor a document's staleness is a finding** (`reference/review-baseline.md`). A weakness the task met outside
its own scope, and a document that stands on code the task changed, are recorded knowledge: they refuse
no review, gate or closeout, and neither their presence nor their absence changes a verdict. What is a
finding is a weakness inside the task's scope that was left unrepaired, and a document the task changed
whose dependent record carries no confirmation.

If the manifestation candidate moves before adjudication, the stale attempt is rejected and a
successor is reviewed. A successor reuses the sealed reports rather than re-censusing routes.

The role serves the assigned leaf/master/plan/super seams and the seam table still fixes the review candidate and verdict destination. Actual ownership comes from the explicit canonical assignment, rather than an inferred plane generation. For native clarification use the actual parent/task role through bound messaging; a dashboard Reviewer has no parent and needs none. The Reviewer starts no role.

### Invariants And Boundaries

Requirement adjudication and the durable-evidence stable-contract-or-expiry hold point
are independent mandatory concerns. Accepted attempts remain closed.
One reviewer role serves leaf, master, plan and super seams under an explicit assignment. Developer questions go to the parent when one exists, and peer clarification uses the actual parent/task role; a Reviewer without a parent asks in its own chat. The role text names hand-over values by their full path, such as `documents[0].taskDocReadArgs.rendered_path`, `workspace.memoryRoot` and `workspace.scratchRoot`, and carries no bare nested name.

## CCR-R12@v5 Transaction Boundary

Current role duty remains targeted/scoped evidence with failed or unrun results visible, followed by the existing authorized paired Git transaction under its real contract. Requested independent review preserves the sealed monotonic finding set and settings budget. The normal Curator authoring pass remains the standing full memory-quality/coherence exception; an explicitly report-only admission claims none of that normal pass complete. No finished turn or green check supplies semantic acceptance or Git publication.

## Current composition and authoring contract

Reviewer requires explicit independent assignment, exact seam/mode, approved revisions and ruling, immutable candidate and attempts, bound catalogs and check contract. Inputs, complete standing-criterion reporting, sealed findings, route coverage, verdict, producer list, route reports and immutable journal remain inline. Complete-diff review is not filtered by invariant attribution.

The numbered steps hold knowledge before/after/family/sibling inspection and producer preservation, expectedKnowledgeEffects adjudication and the `cutCards`/`addedFiles` memory checks inline; the master-exit completeness duty is inline as well. Procedures sit behind "Before you …, read" pointers: `operations/review.md` (intake and leaf verdict handover, boundaries, code-round recording, round-limit verification, record-only recheck), `reference/review-baseline.md` (route partitioning, baseline evidence checks, the three lenses, sealing and focused-test selection), `reference/knowledge/use.md#reviewer-inspect-every-changed-file`, `reference/knowledge/commands.md`, `reference/message-handover.md`, `reference/sandbox-actors.md` and `operations/orientation.md` for developer questions.

The same Reviewer records code rounds and the separate memory lane; neither recording is Manager gate acceptance. Memory IDs/reports/count stay separate, with the same ordinary limit and recorded approval for extras. Only a recorded passed last round plus a matching review step permits its own set_step done; cold reads, blocked verdicts and progress do not. No matching step means report and set nothing. Record-only unchanged-candidate checks retain the last round, and scoped fix verification cannot silently reset the sealed baseline.

When the candidate changes instruction texts, the Reviewer reviews them against `system/skill-writing-guidelines.md` when present, as it reviews code against `system/coding-guidelines.md`. For a finding about every member of a set, it scripts a scan of the whole candidate and reruns that scan during verification.

No role starts, code/onboarding writes or Git publication are granted. Non-leaf seam recipients and owner recording, immutable attempt history, exact caller identity, permission stops and scratch/report custody remain.

## Evidence

### Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

### Repo-Internal References

Worker envelope, reviewer verdict template, manager exact-set dispatch, and governing route overview.

- Every exact requirement attempt and candidate receives a separate independent accepted/rejected record. [1]

- The verdict template structurally repeats one adjudication block per stable ID. [2]

- The reviewer emits its own curator hand-off list in the shared producer shape. [3]

### Cross-Repo References

No meaningful cross-repo references.

## Exit seams

Master-exit review covers the exact organizational candidate or the atomic branch diff and accounts for every master requirement, leaf, substep and accepted gap fill as `addressed`, `delta justified` or `MISSING` with its evidence anchor. At either exit seam a baseline BLOCK goes to the owning Manager, or to the Orchestrator at super-exit, as decomposable fix leaves; integration branches are not repair workbenches.

## Stage Boundary

The Reviewer ends with a recorded verdict over the whole assigned requirement, its findings and coverage. Record-only repairs use the last recorded round without a new begin only on the authority-proven unchanged candidate; the sealed remainder can only shrink.

Own work/instrument slips and invalid caller input are repaired through the same admitted tool and work continues. Stops remain permission prompts, correct-input product/AR refusals or unowned state, requirement-meaning questions, and effects outside the worktree/scratch/task. An unfinished final turn sends what is awaited, and from whom, to its parent with `role_message` on `agents-remember-task`. Worker/Reviewer repairs answer the required property and construction, not a succession of examples; extra-round requests carry that account.

The review budget is the settings number `orchestration.loops.defaults.maxRounds`, read at each begin; the effective task limit includes approved extras and is read from the `task_doc` answer. CODE and MEMORY retain separate counts under the same setting. Beyond-limit work needs recorded Architect or developer approval; the Manager requests it through its reporting route.

## Current Source Evidence

- The baseline detail binds the catalogs, the three lenses and the exploratory mandate, and holds that a recorded weakness or a document's staleness is never a finding, while an unrepaired in-scope weakness is. [16]

## Working files

The Reviewer's closing paragraph sends temporary files, experiments and working copies to the hand-over's real `workspace.scratchRoot` and, for what must not live under the projects home (a sandbox root) and for one short `TMPDIR`, to `workspace.outsideScratchRoot`, with `XDG_CONFIG_HOME` inside `workspace.scratchRoot` and that root never removed. Product/tooling temporary files, test-runner temporary files and explicitly admitted repository sandboxes keep their own owners, and reports and evidence stay in the hand-over's local report folder for the product to copy to canonical notes before removal. Temporaries stay outside code, memory and tasks.

- The Reviewer seam table names organizational leaf, atomic-master integration, master-exit, portfolio plan and super-exit scope, start selection and verdict recipient; candidate identity comes from the intake rather than the hosting enclosure. [5]

- The Reviewer records ordinary CODE rounds and separately sealed MEMORY rounds under the actual task review-state limit; Manager gate acceptance and recorded architect/developer approval beyond the limit remain separate. [6]

- The Reviewer stage ends at a recorded verdict covering the whole requirement, findings and coverage. Own-step completion waits for a passed recorded last round; record-only repair reuses the last round only with every candidate finding closed and candidate bytes unchanged; a finding states the required property its case proves. [7]

- Organizational leaf route review sends code findings to Worker and memory findings to Curator; code PASS first notifies Manager so it can start Curator, and readiness for closeout names both passed lanes. [9]

- Reviewer intake uses exact rendered/JSON paths and actual scoped read schemas, reads only the assigned seam and writes only contained task-local report artifacts. [10]

- Reviewer requires the dispatched exact stable IDs and versions, the durable approval record, exact candidate and Worker attempts, and its bound catalogs and repository tools rather than choosing a rubric on the spot. [11]

- Reviewer inspects every changed file of the complete candidate diff and reads the baseline detail at step 4; a subset never replaces the Curator's complete authoring memory-quality operation. [12]

- Baseline is sealed under the step-4 baseline detail; fix verification reuses that sealed evidence and only listed IDs without a new-lens or whole-seam rediscovery mandate. [13]

- Each exact requirement revision is adjudicated accepted or rejected against its Worker attempt/candidate in a separate immutable reviewer record in the same leaf journal; Worker and earlier records stay unchanged. [14]

- The Reviewer emits every bound standing criterion, sealed findings, complete route coverage, a seam-shaped verdict and producer-data handoff list plus durable per-route reports. [15]

- The Reviewer records ordinary leaf CODE begin/result and separate MEMORY rounds with unchanged code state; Manager records beyond-settings authorization and retains gate acceptance. [17]

- A moved review candidate is stale and requires a successor exact Worker attempt and reviewer record; changed scope or identity does not manufacture a new first review. [18]

- Reviewer marks only its own named review step done after the last round is recorded passed, and its stage ends at a recorded verdict covering the whole requirement, findings and coverage. [19]

- Reviewer repairs its own recording or evidence faults and answers input-fault refusals through the same tool; record-only repair preserves a round only while all candidate findings are closed and candidate bytes remain unchanged. [20]
