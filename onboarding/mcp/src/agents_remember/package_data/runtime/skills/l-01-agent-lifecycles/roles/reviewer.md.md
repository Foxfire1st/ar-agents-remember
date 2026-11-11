# l-01-agent-lifecycles/roles/reviewer.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Current operative account — MIK-R113

Operator settings (`harness`, `model`, `effort`, `serviceTier`) are not the Reviewer's to set. Message files carry complete payloads, while wake text names the request and files. The Reviewer runs full suites and drift reporting only on an explicit developer request; the complete `memory_quality_check` stays the Curator's ordinary curation pass.


## Current supported-pair account — R100/R116 composition

The whole requirement verdict, findings and coverage ends this independent stage. Reviewer records ordinary begin/result within the actual review-state settings limit; Manager records architect/developer authorization beyond it. A record-only check preserves the last round only on byte-identical candidate with all candidate findings closed. A finding states the broken required property; a case is its proof, not a replacement finding or automatic new round. MEMORY stays a separate sealed lane.


## Landing evidence in the independent memory lane

The independent MEMORY review reads both landing populations in the quality result. Removed text without a named task change is a finding; an added file outside the knowledge without a place in the task requirement is a finding. These are human judgments, not automatic refusing diagnostics. CODE evidence, MEMORY findings/pass count and Manager acceptance/transaction authority stay separate.


- When reviewing the Curator's memory change the Reviewer inspects the quality result's cutCards and addedFiles reports: text removed without a named change and a file added outside the knowledge without a place in the task's requirement are findings. [33]


## Message/file transport

This packaged copy makes role messages short wake-ups naming requested work or a handover and its files. Complete report, verdict, list and evidence contents travel through file-only `body` or existing-file `attach`, never pasted into message text. Within a shared task, message files remain with its record and a leaf workspace exposes the message-folder link. Wake text uses the effective settings limit, not a number pinned in this role/template.

- Messages wake; complete payloads and evidence travel as files.


## Current operative account — MIK-R112

The review budget comes from `orchestration.loops.defaults.maxRounds`, read when the next round begins; agents read the effective task limit, including approved extra rounds, from `task_doc`’s `reviewState.limit` on `agents-remember-task`. Code and memory reviews use the same settings limit with separate counts and sealed findings. Beyond-limit work needs a recorded architect or developer approval, which the Manager requests through its assigned reporting route and records.

The Reviewer's stage ends when the verdict over the whole requirement, findings and coverage is recorded. The Reviewer repairs faults in its own work or instruments, corrects invalid input through the same tool, names the repair in the verdict and continues. It stops for an open permission prompt, an Agents Remember tool refusal other than of a covered correct write, unowned state, a requirement-meaning question, or an effect outside its assigned worktree, scratch folder and task. A Reviewer with a parent that ends a turn unfinished tells that parent what and whom it awaits.

When all candidate findings are closed and only the Worker’s report/evidence/hash/anchor remains to repair, the same Reviewer records the repaired record on its last round without `begin_review` or a count increase. This holds only while the candidate stays byte-for-byte the one that round recorded; if it changes, the tool refuses and names `begin_review` as the next step.

A Reviewer finding states the required property the candidate breaks; the showing case is proof, not the finding. If a repair leaves that finding open, the Worker states the property for every case and proves the construction or changes it, reporting which. A beyond-limit request carries that property-and-construction account.


- A first cold requirement read comes before any code candidate, Worker attempt or code round.
- Leaf verdicts go directly to the Worker and the Curator, with code and memory in separate lanes.

## Purpose

The independent Reviewer examines one explicitly assigned seam or loop round, refutes or confirms each claim and supplies verdict evidence rather than decisions.

## Current Contract

Native intake reads the rendered task-document files named in the handover, read with the harness's own file tools before acting; change documents through `task_doc` only, because edits to copies are never read back and are lost on the next publication. Each call carries its task/contract scope; use actual reader schemas. Write only contained task-local review artifacts. Missing authority or capability is reported rather than substituted.

A baseline inspects the complete diff, including unattributed files, against the applicable standing catalog, three lenses and exact requirement evidence class. Knowledge mapping adds before/after family and unchanged-sibling examination. Preserve producer handoff fields for co-resolution.

The Reviewer binds catalogs from its review type's row in the catalog table alone; a brief that names catalogs changes nothing, and the Reviewer chooses none during the review. The verdict's Catalog Binding section names the review type, the catalogs the table gives it, and for each conditional catalog whether it is bound and why, naming the changed surfaces that decide it. Code is reviewed against `system/coding-guidelines.md` and instruction texts against `system/skill-writing-guidelines.md`, where present.

Adjudicate each exact requirement revision/worker attempt separately, including declared knowledge effects against the packet; a rejected requirement blocks overall pass. Seal stable findings and observable repair criteria. Fix-verification covers only the preceding outstanding IDs without baseline reset, new findings or added scope; the review-state round limit holds.

Keep task-bound attempt/verdict evidence, requested seam distinctions and the Reviewer's own ordinary code-round begin/result; the memory check keeps its separate sealed reports, ids and pass count. Normal curation authoring remains the full-MQC exception; an explicit report-only curator admission cannot claim that pass complete.

## Conventions

Canonical skills/l-01-agent-lifecycles/roles/reviewer.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy, the sole generated skill target, which the tool server serves as MCP resources; no generated file defines a separate obligation.

## Invariants And Boundaries

No self-review, implementation, task acceptance/publication, packet rewrite, verdict laundering or second completion authority. Developer questions go to the parent with `role_message`; a dashboard-started Reviewer has no parent and asks in its own chat. Peer questions go to the Worker about the candidate and to the Curator about memory, with the handover's sibling role and exact leaf task references.

## Code Commentary

Intake opens the `rendered_path` and `json_path` that `taskDocReadArgs` supplies, with the harness's own file tools; task documents change only through `task_doc`. `knowledge_read` takes `workspace.memoryRoot`; `context_packet` and `read_ar_files` take `task_context` with the canonical task reference and enclosure contract. Missing fields or refused capabilities are reported as gaps, never bypassed through another Agents Remember server.


### Logic

The seam table names what each seam binds, its start leaf and its verdict recipient: a leaf route review reports to the Worker, with a code PASS also to the Curator and the memory verdict to the Curator; an atomic-master integration review reports to the integration owner, master-exit to that Manager, a portfolio plan review to the Architect and super-exit to the Orchestrator. Leaf-review intake comes from the Manager or the Architect, candidate-review intake from the Manager, and the Worker's freeze handoff brings the freeze report, candidate identity and attempt records.

The Reviewer adjudicates the Worker attempt records against the exact candidate identity: a tree or commit, or a non-code digest and anchors, never a branch name. A malformed Worker row already handed over is a formal attempt, rejected in its failure class and never edited.

The role file defines one Reviewer across leaf code-change and full-loop review, atomic-master integration review, master exit, plan review and super exit. The seam fixes the review's scope and verdict recipient. The posture is refute-or-confirm over the seam's candidate, task documents and bound catalogs, and the result is a verdict artifact, not a decision.

The three lenses are completion against task documents, scoped implementation evidence, and onboarding against code. Criteria come from the catalogs the review type binds, plus the exploratory mandate. The exit-seam rubrics cover the accumulated change set, its evidence and decomposable fix leaves. The verdict is written under the seam's `notes/reports/` path, with an impact-analysis and an onboarding-coherency report for each material route.

### Conventions

The role file holds the intake, the seam and catalog tables, the inspection steps, the artifacts and the boundaries. The intake and verdict handover, round recording and review boundaries live in `operations/review.md`, the baseline method in `reference/review-baseline.md`, and the criteria in the `criteria/` catalogs.

### Invariants And Boundaries

**VERDICTS ARE EVIDENCE, NOT DECISIONS.** The Reviewer never decides a gate: non-leaf seams keep their decider, and the Manager keeps gate acceptance, closeout, integration and task status. At an exit seam a baseline BLOCK goes to the owning Manager at master-exit, or to the Orchestrator at super-exit, as decomposable fix leaves that each name scope, target files or documents, evidence and done-when. A leaf's sealed findings go directly to its existing Worker, and a fix-verification BLOCK returns only the sealed outstanding identifiers and creates no new fix leaf. An unreviewable change set, including a missing diff or task documents, is itself a blocking finding. A finding names the property the candidate breaks, and the failing case is its proof.

**Declared knowledge effects.** In step 7, when the leaf's task document declares `expectedKnowledgeEffects`, the Reviewer compares it with the leaf's requirement packet: the declared subjects and effects must match what the packet requires, with none missing and none invented, and a mismatch is a finding. The check stands in the role file rather than a criteria catalog, because the code-seam catalog promotes a candidate criterion to standing only after it catches a real defect in two separate first-review engagements.

### Todos

No task-independent TODO is declared by this job file.

## Docs References

No external domain documentation applies to this repository-local orchestration job file.

No relevant external documentation found.
## Working folders and reports

Agent-authored temporary files, experiments and working copies live only in the handover's real `workspace.scratchRoot`, outside code, memory and task folders; reports and evidence go in the handover's local report folder, which the product copies to canonical notes before removal.

## Evidence

### Repo-Internal References


- The Reviewer returns exit-seam fix leaves to the seat it reports to: the owning Manager at master-exit, the Orchestrator at super-exit. [30]


- The Reviewer independently examines one assigned seam or review round, refutes or confirms the claims against the bound criteria catalogs, and writes and hands over the verdict. [2]


- The Reviewer's brief starts the work, and the verdict artifact is its durable handoff. [3]


- The Reviewer refuses another seat's pasted brief and reports it to the seam's decider, and never absorbs another seat's work. [5]


- A baseline review runs the bound catalogs, required routes and exploratory mandate, covers all three lenses explicitly, and tries to refute each claim before confirming it. [6]

- The Reviewer requires the catalogs bound by its review type and does not choose catalogs during the review. [7]

- Each review type binds a fixed set of criteria catalogs, listed in the role's review-type table from master-exit and super-exit to leaf, integration, full-loop and plan review. [8]


- At master-exit the Reviewer accounts for every master requirement, leaf, substep and accepted gap fill; completion against task documents is an affirmative duty, not a formatting check. [10]


- A master handover packet that reads as complete while silently omitting unfinished leaf work, a substep or an accepted gap fill has a blocking finding. [12]


- Baseline review checks the Worker's targeted checks and regressions against the past for the requested scope; full suites and drift reporting run only on an explicit developer request. [13]


- The onboarding staleness criterion checks every present-tense card or overview sentence against the as-landed code, keeps historical accounts in history rows, and does not accept a true paragraph added beside a contradictory claim. [14]

- Super-exit review inspects changed paths and sidecars and route overviews among the integrated portfolio evidence. [15]

- Full suites and drift reporting run only on an explicit developer request, while the normal curation authoring pass always runs the complete memory_quality_check, which a subset cannot replace. [16]

- At master-exit a baseline BLOCK goes to the owning Manager as decomposable fix leaves. [17]

- At super-exit a baseline BLOCK goes to the Orchestrator as decomposable fix leaves. [18]

- The Reviewer writes the verdict under the seam's notes/reports path using the verdict template and writes fix-leaf descriptors for non-leaf baseline blocks. [19]


- The permitted review surface is read-only retrieval and scoped checks, report/journal artifacts, bound leaf messages, and ordinary review-round begin/result recording.


- The role's operator-settings passage is a prohibition: harness, model, effort and serviceTier are not the Reviewer's to set. [23]


- The role keeps the master-exit and super-exit seam rubrics and their blocking rule. [24]


### Cross-Repo References

No sibling repository evidence is needed for this orchestration job file.

No meaningful cross-repo references found.

## Current Contract Evidence


- Reviewer leaf messages use role_message on agents-remember-task with the handover's sibling role and exact leaf task references; product-supplied agent identifiers stay whole and unchanged. [29]


- The Reviewer reads the rendered task document and canonical JSON at the supplied taskDocReadArgs paths, reads only the seam's required documents, and uses the Agents Remember tools on agents-remember-task only. [34]

- The Reviewer may write its review artifacts, retrieve read-only through read_ar_files, use scoped system/tools.md checks and report templates, inspect full memory_quality_check curation evidence, run requested drift reporting and send the direct leaf messages and Manager notices; ordinary leaf begin/result records are evidence, not gate acceptance. [22]

- Review starts only on the owner's assignment, reads the rendered task document and canonical JSON at the handover's taskDocReadArgs paths, and requires every applicable intake input before candidate inspection. [26]

- A baseline review reports every standing criterion, the sealed baseline findings with stable identifiers, evidence and fix-acceptance criteria, and a complete route-coverage table. [27]

- The Reviewer's permitted read and check surface and its prohibitions on implementing, recording task acceptance, starting roles, publishing Git, deciding gates and absorbing another seat's work. [28]

- The Reviewer reads the current review-state limit from the task_doc answer and never runs an unapproved round or splits the scope to avoid that limit. [31]

- The stage ends with a recorded verdict covering the whole requirement, its findings and coverage; the review step is marked done through task_doc only after the last round is recorded as passed. [32]
