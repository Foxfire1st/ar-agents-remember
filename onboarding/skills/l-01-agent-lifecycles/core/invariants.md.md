# skills/l-01-agent-lifecycles/core/invariants.md

## Current L113 source qualification

The following landed account controls only the changed start, launch-setting and completion seams it names. It is carried here from the former distribution-card owner during source-owner reconciliation; the canonical source remains the authority. Older incompatible dispatch, hosted-selector, notifier or capsule-injection wording below is historical, not restored behavior. Unchanged L54 explanations, inherited qualifications, complete reference groups and typed-entry provenance remain preserved. Source declarations and inherited tuples are not a new execution, CODE verdict, MEMORY grade or fresh whole-file anchor qualification. The incoming account's no-todo and live-source-discovery negatives are inherited editorial history, not new searches.

## Purpose

The shared **invariants** block: the facts every role can count on, authored once so a role file
names the invariant it depends on instead of restating the set.

## Code Commentary

### Logic

`## Continuity lives in durable state, never in transcripts` states why short-lived workers and reviewers
are safe and why **every seat writes its artifact of record** — a finding held only in a chat is a bug.
`## The decision surface` routes decision-needing questions to the task doc's `openQuestions` with the
analysis in `notes/`, and keeps backend seats behind the architect relay.

`## Sequencing is decided by the dependency graph, not by habit` sets parallel-by-default up to the
`orchestration.concurrency` cap, requires a named gate / one-writer dependency / explicit ruling for any
sequential exception, and states that build concurrency never grants landing order. `## Observability`
keeps coordination seats as `task_doc` leaves with attached chats. `## The spine: task doc → branch →
worktree` fixes what creates a branch or worktree, that design and portfolio work never touch git, and
that chat is never a build route.

`## Default behavior, and where it is overridden` states the fill-small-blanks default, the one-rung
escalation for a plan delta beyond blank-filling, and that the **spirit test is orchestrator-only**.
`## Knob resolution and capability doctrine` fixes the resolution order (role-file defaults < global
settings < repo-local settings), which rows are settings keys, the deliberate absence of per-harness role
files, and `role_start` as the harness-independent role-agent fan-out. Current launch rows are harness, model, effort, serviceTier, mode and featureValues; the retained launchArgs/sessionCommands/promptKeywords keys load but are no longer read. `## Instruction-surface boundaries`
assigns task-collaboration doctrine to `tasks/AGENTS.md`, the task format to
`w-02-light-task-workflow`, repository specifics to the memory layer, and the corpus's own division of
labour to `roles/` / `operations/` / `reference/`.

### Conventions

Keep each invariant to the statement and its consequence; long rationale belongs in
`reference/rationale.md`.

### Invariants And Boundaries

- Continuity lives in the task tree plus written artifacts, never in a transcript.
- Sequential execution is the exception and must name its reason.
- Only the launch-setting rows are settings keys; `dispatch` and `tools` are structural descriptions.
- There are deliberately no per-harness role files.
- The retained corpus describes core/role/operation inheritance, but native role launch selects its role and operation without injecting this shared core; source doctrine is not evidence of delivered capsule contents.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References

- Task intent creates its branch and build worktree; design and chat are not build routes. \[1] [10]

- Launch settings own current knob rows; removed launchArgs/sessionCommands/promptKeywords load but are unused. \[2] [11]

- Task collaboration, format, memory-specific commands and role/operation duties have separate instruction owners. \[3] [12]

- Core inheritance is retained corpus doctrine and does not prove current native capsule contents. \[4] [13]

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.

## Preserved L54 canonical account

The following pre-sync account retains its explanations and evidence. Its statements on the specifically superseded seams are historical; other meanings and their original citation identities remain intact.

<details>
<summary>L54 canonical prose and inherited source-epoch custody</summary>

## Governing Overview

[Lifecycle instruction overview](../overview.md)

## Purpose

This retained shared-invariants document records continuity, decision surfaces, dependency-based sequencing, observability, branch/worktree intent, bounded autonomy, portable settings and ownership of instruction surfaces. Its intended author-once arrangement lets a role name a dependency rather than restating the full set.

## Commentary

### Durable continuity and visible decisions

Continuity lives in task-tree masters/leaves/statuses, decision logs, `openQuestions`, contracts, inbox rows, worktree contracts and each seat's written artifacts, not transcripts. Short-lived sessions may die, compact or resume because the state is durable; a chat-only finding is a bug. Decision-needing questions belong in task-doc `openQuestions`, analysis in `notes/`, and rulings that change task, branch or orchestration state in the decision log with surviving analysis behind them. The retained shared rule places backend questions behind the Architect relay rather than direct developer presentation.

Coordination seats are described as `task_doc` leaves with attached chats so the developer can enter any seat. The retained Architect-only conversation statement must not erase the selected operation's actual parentless/dashboard exception: Orientation permits a seat without a parent to ask in its own chat and addresses developer questions to the supplied parent when one exists.

### Dependency graph before habits

Independent work is parallel by default up to the applicable `orchestration.concurrency` cap. A sequential exception must name a gate, shared-file one-writer dependency or explicit ruling. Build concurrency never grants landing order.

The intent spine is approved task doc → branch → build worktree. In the source's task-execution doctrine, design/portfolio work does not touch Git; super-branch intent begins at portfolio execution; intermediate master branches exist only for `atomic` masters; a leaf branch and worktree arise together because leaf work is build work; an `organizational` master creates no branch. Worktrees live per build/integration edge and are reclaimed afterward. Chat is not a build route: code changes require approved task documents, with small work using the minimal `w-02-light-task-workflow` artifact. Research and design conversation may remain chat.

### Bounded autonomy and portable knobs

The default is fulfill the task and fill only small, unambiguous blanks a competent implementer would fill. Larger plan deltas escalate one rung up rather than straight to the developer or through self-reshaping. The full spirit test is Orchestrator-only; Managers and Workers retain the default and escalate real deltas.

Role files are model-interpreted Markdown, not executors. The portable knob block describes harness/model/effort/tools defaults for host injection. Resolution is role defaults < global settings < repo-local overrides; unknown `orchestration.*` keys fail loudly. Only `harness`, `model`, `effort`, `launchArgs`, `sessionCommands` and `promptKeywords` participate in role/per-level launch settings; `dispatch` and `tools` describe structural authority/capability, never settings keys. The source records the 2026-07-05 decision against per-harness role files: conditional abilities remain in portable doctrine and harness preference is deployment configuration. Its harness-independent `dispatch_agent` fan-out account describes canonical document-plus-role dispatch, not authorization to replace a selected role's present start procedure.

### Instruction ownership and retained composition

`tasks/AGENTS.md` owns task-collaboration doctrine; `w-02-light-task-workflow` owns task format and requirement packets; memory skills and resolved `system/*` own repository commands, coding guidelines and landing flow. The named `system/tools.md`, `system/coding-guidelines.md` and `system/task-publication.md` are read rather than inventing a runner. `roles/` owns duties, `operations/` the current procedure, and `reference/` rationale/history/superseded rulings.

The final core-plus-role-plus-operation injection sentence is retained composition doctrine, not a statement of universal current native injection. The selected Orientation explicitly forbids loading other role/core files for task-bound intake, and the governing overview distinguishes native role-plus-one-operation capsules from retained core material. Preserve the ownership distinctions without treating this card or the underlying prose as a launcher, executable tool, expanded permission set or instruction to load every core block.

### Inherited context and limits

The previous packaged-path card's continuity, sequencing, settings-key and instruction-owner meanings remain useful. Its convention to keep long rationale in `reference/rationale.md` is inherited editorial guidance, not a newly checked cross-file contract. Its test-file `**Inherits:**` citation is retained historical evidence of the earlier corpus account, not a revalidated claim about every present role or executed test. The old no-todo, live-source-search and no-sibling-contract assertions are likewise inherited bookkeeping, not new discovery results. This card describes source declarations and scoped differences; it does not certify execution, launcher availability or present test results.

## Evidence

The quoted anchors below are literal strings in the canonical source ranges. They establish declarations and selected instruction boundaries, not executed outcomes.

- Shared durable continuity and artifact-of-record obligation. [1]
- Questions, analysis, rulings and retained Architect relay. [2]
- Dependency-based sequencing and retained observability doctrine. [3]
- Task/branch/worktree intent and chat/build boundary. [4]
- Small blanks, one-rung escalation and Orchestrator-only spirit test. [5]
- Portable roles, settings precedence, permitted launch keys and harness-independent dispatch. [6]
- Task, memory, role, operation and rationale ownership; retained core composition sentence. [7]
- Selected Orientation starts from supplied assignment and forbids loading other role/core files. [8]
- Present parent routing and explicit parentless exception qualify the retained universal Architect-only statement. [9]

</details>
