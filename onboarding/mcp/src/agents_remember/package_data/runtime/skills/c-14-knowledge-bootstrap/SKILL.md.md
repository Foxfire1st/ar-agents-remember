# c-14-knowledge-bootstrap/SKILL.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T19:49:05Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d` |
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../overview.md)

## Purpose

**The repository's knowledge foundation gets an operational procedure, and it is the curator's.**
A repository's memory has two halves created in different ways. Onboarding is Markdown a seat writes
(`c-03-repo-bootstrap`, maintained by `c-05-create-or-update-onboarding-files`); the **knowledge
foundation** is authored records in the knowledge database — invariants and facets, the families and
guarantees that hold obligations together, exact source realizations, and the external sources they
rest on. Nothing scaffolded the second half. `c-14-knowledge-bootstrap` is the procedure that authors
it — for a repository that has none, and for one resuming a foundation that is already part-built.

**This card describes a generated copy.** The canonical instruction home is the root source
`skills/c-14-knowledge-bootstrap/SKILL.md`; `scripts/sync-skills.py` copies the root `skills/` tree into
this package-owned copy (`mcp/src/agents_remember/package_data/runtime/skills/`) **and** into the eight
harness starter packages (`.claude/`, `.codex/`, `.cursor/`, `.github-vscode/`, `.hermes/`,
`.openclaw/workspace/`, `.pi/`, `.agents/`). Nine generated targets in total, plus the canonical tree.
A change is made in root `skills/` and propagated by running the generator; the copies are never edited
in place and never define independent behaviour.

## Code Commentary

The installed bootstrap invocation explicitly supplies --config with the active MCP authority settings. This is the existing CLI option and does not expand config discovery or checkout authority.

### 260921-ICR-L27 A Procedure, Not A Role — And Three Entries That Actually Exist

**What the procedure owns.** The semantic owner is the **existing curator**, the writer is the
**existing admitted knowledge batch writer**, and the publication lands at the **one location the
ordinary read route already selects**. The skill states the order those existing owners are used in and
the states a run must distinguish; it adds no agent, no second database and no parallel onboarding
track.

**Which session carries it is the product's decision, and the product decides by the task document.**
The opener admits a role with **no** task document only for the taskless seats, and the procedure
quotes the refusal verbatim (`400 {"status": "task-binding-required", "detail": "named role scope is
required"}`) rather than paraphrasing it. The shipped constant behind that gate is `TASKLESS_SEAT_ROLES`
at `mcp/src/agents_remember/serving/task_binding.py:83`. **`260921-ICR-L32` changed it**: on the
developer's **2026-09-24 ruling** the set is `{"chat", "terminal", "bootstrap", "curator"}`, and the
carrier text this card describes now enumerates **three entries plus the taskless curator seat the
ruling admitted** rather than asserting a fourth that does not exist:

- **A task exists** — the curator is opened on that task's document, and the leaf entry is its writer.
- **No task exists, first hour** — the **bootstrap** seat carries the read-and-report half: it is the
  seat the product admits without a task document *and* instructs to read the foundation's state and
  report it, handing the authoring on. It does **not** author records.
- **No task exists, the foundation is to be built now** — a **taskless curator session** authors it under
  the curator's own rules (the ruling's second carrier), and the taskless writer is run by an instructed
  session that holds the procedure, from a workspace with **no enclosure in scope** (the writer refuses
  one with `enclosure_in_scope`, so a bootstrap can never publish onto a task's memory line).
- **A taskless *curator* seat exists.** `curator` joined the taskless seat roles by the developer's
  **2026-09-24 ruling**, taken when the missing route was put to them, so a document-less `curator`
  session is admitted and receives the curator capsule; every other role is still refused.

> **Seat-policy note at L27's bytes (dated 2026-09-24).** This records the policy of the candidate that curation read: code base `06ed70cfcde7e3860ee5b53435727e7512e4335c` plus that leaf's working-tree delta, where `TASKLESS_SEAT_ROLES` was `{"chat", "terminal", "bootstrap"}` and a document-less `curator` session was refused `task-binding-required`. That was true of those bytes and is **superseded**: whether `curator` joined the set was then a product decision under revision, and it was taken in `260921-ICR-L32`. The carrier instructions and their ten generated copies changed first and this memory followed them.
>
> **Seat-policy note at these bytes (L32 curation, dated 2026-09-24T17:20+02:00).** At the bytes this curation read — code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus this leaf's working-tree delta — `TASKLESS_SEAT_ROLES` is `{"chat", "terminal", "bootstrap", "curator"}`: a document-less `curator` session is **admitted** and receives the curator capsule (`instructionMode.role` `curator`, task reference `free-agent:curator`), while every other role is still refused `task-binding-required`. `scripts/sync-skills.py --check` reports all nine generated targets `ok`, so all ten copies of this carrier carry the corrected text. Read the sentences above as the policy **at these bytes**, not as a permanent property of the product.

**Four knowledge states are four different facts, and a fifth is not a state at all.** `not-recorded`
(uninitialized — no publication is recorded), `recorded` (populated — a dataset bound to this repository
stands there; read it before extending it and never reinitialize it), `unusable` (something stands there
that is not a dataset this route can answer from, or it belongs to another repository's authority home
— observed with `selected_input_unavailable` when there is no file to open and `snapshot_unavailable`
when there are bytes that are not the expected dataset; report the exact state and path and **do not
delete, overwrite or migrate it**), and `context-not-admitted`, which is the **admission** refusing and
is **not a knowledge state at all**. A location with no file-system entry is `not-recorded`; a location
holding a directory where the dataset belongs is `unusable`; a null or missing count is never rendered
as a measured zero.

**Two writers, and the enclosure is what separates them.** The taskless entry
`agents-remember knowledge-bootstrap --repo <repo_id> --list <hand-off list> --authorization-ref <ref>
--commit` derives its own admission (the declared repository entry, the memory layer the read route
resolves, the exact code and memory revisions the real checkouts stand at); the leaf entry
`agents-remember knowledge-ingest --contract <this leaf's enclosure contract> … --publish --commit
--json` is the curator's ordinary route for a leaf's own change set. **Planning is the default and
planning is the dry run**: without `--commit` no batch, no publication and no retained progress record
is written. `--authorization-ref` must not be blank and must not be invented — it is one reference, so
"who authorized this" and "who authored it" stay one recorded fact. The destination is **derived, never
accepted**: it is the location the ordinary read route itself selects. A repository whose only
knowledge is its first knowledge needs no development leaf, worktree or synthetic enclosure, and
creating one to satisfy an argument list is exactly what this entry exists to make unnecessary.

**Exit zero is not a publication claim.** The report is the result, and each fact is stated separately:
`run.batchState` with the entries under `run.committed` / `run.skipped` / `run.refused` (a per-entry
refusal is a **result**, not a tool failure), `publication.state` with `publishedIdentity` read back
through the read route's own owner (`confirmed` / `mismatch` / `unavailable`), `destinationContents`
with `publishedByThisRun`, and `remaining` / `unmeasured` / `carried` / `remainingBasis`. An empty
destination, a batch that committed nothing, or an exit status of zero is not a populated foundation. A
partial run stays explicitly partial and keeps a resumable next action; a run that did not examine a
required area cannot claim the foundation complete for it.

**Asymmetric by construction: what is authored here and what is only read here.** Onboarding is
**optional input, never a precondition** — a repository with no onboarding file at all is a supported
starting state, and the procedure writes no onboarding and changes no other skill's owner. External
sources are declared under the hand-off list's own external-source key, so a document identity is never
written as a repository path with a Git blob. Existing records are reused or revised, not duplicated:
matching text is not an identity rule, and a correction is a successor that names the stored identity
and the revision it supersedes. Where code contradicts accepted intent, the intent is **preserved and
the contradiction recorded** rather than either half being quietly rewritten. Collection and search
assistance may be delegated; the semantic reconciliation, the record actions, the family guarantees and
the memberships are the curator's, and the curator's hand-off list is the only thing handed to the
writer.

**The refusal vocabulary is the product's, and the procedure reports it rather than working around
it**: `repository_not_allowed`, `coordination_root_unavailable`, `code_checkout_unavailable`,
`code_checkout_is_not_a_git_checkout`, `code_revision_unavailable`, `memory_revision_unavailable`,
`memory_layer_not_resolved`, `memory_line_moved`, `enclosure_in_scope`, `destination_unusable`, and
`staging_belongs_to_another_operation`. A moved input revision is an explicit new observation, not a
silent reuse. The staging root is removed by its own bounded owner
(`knowledge-bootstrap --repo <repo_id> --discard-staging`) **only** when the declared location provably
holds the very dataset the staged candidate holds, read from both files rather than inferred from a
finished-looking run.

### Invariants And Boundaries

- The knowledge batch writer, the publication owner and the location the ordinary read route selects are
  the only ones used — no second database, second writer or second destination.
- No new agent role, harness, scheduler or parallel onboarding implementation.
- No blind onboarding import, and no hard cutover of operational Markdown.
- Admission is derived from the repository entry and the real revisions, **never** from a boolean
  argument; the commit word is the developer's and the authorization reference is the run's own.
- No fabricated development leaf, worktree, enclosure or task document, and no manually created
  database, to satisfy an input shape.
- No invented project truths, no back-dating, no backfilled task history, no favorable default in place
  of absent evidence; a fixture, prototype or another repository's dataset is never presented as this
  repository's foundation.
- The delivery gates keep their owners: this procedure reports its outcome, while installation,
  closeout, integration and activation stay with the seats and surfaces that already own them.

### Todos

No open file-local todos.

## Docs References

The procedure's external-source obligations are stated in the skill itself; no repository-external
document is needed to prove this contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is needed to prove this repository-local procedure contract. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The skill is the procedure that authors the knowledge foundation (invariants, families, source realizations, external sources) as distinct from Markdown onboarding, and it adds no role and no second store. | `# c-14-knowledge-bootstrap Knowledge Bootstrap`; "This is a procedure, not a role and not a second orchestration system." | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:6-319 |
| The new-project entry is a **taskless** seat, and since the developer's 2026-09-24 ruling the procedure states that a taskless curator seat **exists** and authors the foundation when no task does, instead of asserting a refusal the product no longer makes. | `## Who Runs It`; "A taskless *curator* seat exists"; `"task-binding-required"` | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:38-83 |
| Onboarding is optional input and never a precondition; a repository with no onboarding file is a supported starting state. | `## When To Use`; "Onboarding is **optional input, never a precondition**." | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:22-37 |
| The three reachable entries and the delegated-assistance boundary: collection may be delegated, the authored result may not. | "Collection and search assistance may be delegated; the authored result may not."; `enclosure_in_scope` | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:62-62; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:78-78 |
| Step 1 separates the four knowledge states, and a refused admission is not one of them. | `### 1. Resolve the entry and name the current state`; `not-recorded`; `recorded`; `unusable`; `context-not-admitted`; `snapshot_unavailable` | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:102-117 |
| Step 2 bounds the inventory to root and area contracts with real anchors rather than one record per file, and treats a missing optional source as absent rather than failed. | `### 2. Build a bounded source inventory and a coverage plan`; "A missing optional source is **absent, not failed**" | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:118-132 |
| Step 3 hands the evidence to the curator in the shape the hand-off-list template owns, and states the reconciliation the curator performs — including the deliberate no-family outcome with its basis and the unexamined obligation that is never reported as family-free. | `### 3. Hand the evidence to the curator`; `no_family`; `unexamined`; "existing records are reused or revised, not duplicated" | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:133-158 |
| The taskless writer entry, with planning as its default and `--commit` as the developer's whole write act. | `### 4. Author through the curator's own writer`; `--authorization-ref`; "--commit"; "Planning is the default, and planning is the dry run." | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:151-177 |
| The authoring procedure names the installed leaf command and distinguishes declared from caller-selected publication destinations. | `### 4. Author through the curator's own writer` | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:159-203 |
| Step 5 reads the report as the result: batch state, per-entry outcomes, the independent publication read-back, destination contents, and the remaining/unmeasured/carried work. | `### 5. Read the result back — the report is the result`; `run.batchState`; `publishedIdentity`; `destinationContents`; `remainingBasis`; `progressRecordWritten` | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:204-221 |
| A partial run reports itself partial; an empty destination, a committed-nothing batch or a zero exit is not a populated foundation. | `### 6. Report coverage and unresolved work`; "An empty destination, a batch that committed nothing, or an exit status of zero is not a populated foundation." | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:222-237 |
| Staging is removed only by its bounded owner and only against a proven dataset match; it is never removed to tidy an unpublished run. | `### 7. Clean up through the bounded owner, when there is anything to clean`; `--discard-staging` | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:238-248 |
| The failure table carries the product's own refusal codes and its `nextAction` route for each, including the enclosure guard and the destination that must not be overwritten. | `## Failure And Recovery Behavior`; `destination_unusable`; `staging_belongs_to_another_operation`; `memory_line_moved` | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:249-262 |
| The eight preservation boundaries, including no fabricated leaf/worktree/enclosure, no invented authority, and the delivery gates that keep their owners. | `## Preservation Boundaries`; "No fabricated development leaf, worktree, enclosure or task document" | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:263-283 |
| The relationship table places the procedure against its neighbours: c-13 reaches it, c-03 names it, c-00 reports the location's state, c-10 is a baseline and not a foundation, and the l-01 carriers house the owner and the first-hour seat. | `## Relationship To Other Skills`; `c-13-install-and-onboard`; `c-03-repo-bootstrap`; `c-00-initialize-memory-repo`; `c-10-adopt-memory-baseline`; `templates/curator-handoff-list.md` | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:284-296 |
| The acceptance criteria state the reachable entries, the state read before authoring, the planning default, the derived admission, the read-back, partiality, the published location and the no-new-owner boundary. | `## Acceptance Criteria`; "a zero exit status is never quoted as a publication" | mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:297-319 |
| The taskless seat set the procedure's gate rests on, which `260921-ICR-L32` changed on the developer's 2026-09-24 ruling so that it admits `curator`. | `TASKLESS_SEAT_ROLES` | mcp/src/agents_remember/serving/task_binding.py:91-91 |
| Propagation is generated, not hand-maintained: the root tree is copied into the package-owned copy and the eight harness starter packages. | `CANONICAL_SKILLS`; `TARGETS` | scripts/sync-skills.py:15-15; scripts/sync-skills.py:43-56 |

Current working-candidate evidence for this card:

| Finding | Anchor | Source |
| --- | --- | --- |
| The procedure and its nine generated copies are byte-identical on this candidate, and the leaf's own catalog case reads the served bytes back against the canonical tree. | `PROCEDURE_FILE`; `procedure_text` | mcp/tests/test_knowledge_bootstrap_procedure.py:110-110; mcp/tests/test_knowledge_bootstrap_procedure.py:127-130 |

## Cross-Repo References

No sibling repository evidence is needed for this procedure.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-09-26T21:16:39+00:00: Generated citation repair: `### 5. Read the result back — the report is the result`; `publishedIdentity`; `destinationContents`; `remainingBasis`; `progressRecordWritten` repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:204-221; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:210-210; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:212-212; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:215-215; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:217-217. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:16:39+00:00: Generated citation repair: `### 6. Report coverage and unresolved work`; "An empty destination, a batch that committed nothing, or an exit status of zero is not a populated foundation." repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:222-237; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:235-236. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:16:39+00:00: Generated citation repair: `### 7. Clean up through the bounded owner, when there is anything to clean` repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:238-248. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:16:39+00:00: Generated citation repair: `## Failure And Recovery Behavior`; `destination_unusable`; `staging_belongs_to_another_operation`; `memory_line_moved` repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:249-262; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:257-257; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:258-258; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:255-255. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:16:39+00:00: Generated citation repair: `## Preservation Boundaries`; "No fabricated development leaf, worktree, enclosure or task document" repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:263-283; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:276-276. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:16:39+00:00: Generated citation repair: `## Relationship To Other Skills` repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:284-296. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:16:39+00:00: Generated citation repair: `## Acceptance Criteria`; "a zero exit status is never quoted as a publication" repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:297-319; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:313-313. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T19:49:05Z — The generated bootstrap examples supply --config with the active MCP authority settings to the installed CLI. Configuration discovery and checkout authority are unchanged; this is the existing explicit installed invocation.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `enclosure_in_scope`; "Collection and search assistance may be delegated; the authored result may not." repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:62-62; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:78-78. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `### 2. Build a bounded source inventory and a coverage plan`; "A missing optional source is **absent, not failed**" repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:118-132; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:129-129. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `### 3. Hand the evidence to the curator`; `no_family`; `unexamined`; "existing records are reused or revised, not duplicated" repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:133-155; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:145-145; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:146-146; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:150-150. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "agents-remember knowledge-ingest"; "the two are mutually exclusive" repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:188-188; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:194-194. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `### 5. Read the result back — the report is the result`; `publishedIdentity`; `destinationContents`; `remainingBasis`; `progressRecordWritten` repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:196-213; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:202-202; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:204-204; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:207-207; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:209-209. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `### 6. Report coverage and unresolved work`; "An empty destination, a batch that committed nothing, or an exit status of zero is not a populated foundation." repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:214-229; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:227-228. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `## Failure And Recovery Behavior`; `destination_unusable`; `staging_belongs_to_another_operation`; `memory_line_moved` repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:241-254; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:249-249; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:250-250; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:247-247. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `## Acceptance Criteria`; "a zero exit status is never quoted as a publication" repointed to mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:289-311; mcp/src/agents_remember/package_data/runtime/skills/c-14-knowledge-bootstrap/SKILL.md:305-305. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **body update — the seat policy this card stated is brought forward, dated, and the earlier note is kept as what was true at its own bytes.** `260921-ICR-L32` added `curator` to `TASKLESS_SEAT_ROLES` on the developer's 2026-09-24 ruling and corrected the carrier text this card describes, so the card's own enumeration of entries is restated as the three entries plus the taskless curator seat the ruling admitted; the L27 seat-policy note is retained verbatim in substance, retitled to L27's bytes and marked superseded, and a second note records the policy at **these** bytes (`71a17079…` plus this delta) where a document-less `curator` session is admitted and receives the curator capsule while every other role is still refused. The row naming the constant is corrected with it — the declaration moved to `:91`, and "unchanged by this leaf" was false of L32. No verification stamp is advanced as a commit: the candidate is uncommitted, so the header's pair is the leaf's base commit plus this working-tree delta, and the governed closeout owns the real stamp.
- 2026-09-24T12:20:00+02:00 — 260921-ICR-L27 curator (uncommitted change set on `ar/260921-icr-l27-ar`, code base `06ed70cfcde7e3860ee5b53435727e7512e4335c`): **created.** The card documents the newly delivered `c-14-knowledge-bootstrap` procedure on its generated package-owned copy; the canonical instruction home is root `skills/c-14-knowledge-bootstrap/SKILL.md`, propagated by `scripts/sync-skills.py` into nine generated targets. It records the product's real admission (`TASKLESS_SEAT_ROLES` is `{"chat","terminal","bootstrap"}`, so a taskless **curator** seat is refused `task-binding-required`) instead of the admission an earlier draft of the procedure asserted, the four knowledge states with a refused admission kept out of them, the two writers and the enclosure that separates them, the planning-by-default dry run, and the read-back facts that make a report a result rather than an exit status. No verification stamp is advanced as a commit: the candidate is uncommitted, so the header's pair is the leaf's base commit plus this working-tree delta, and the governed closeout owns the real stamp.
