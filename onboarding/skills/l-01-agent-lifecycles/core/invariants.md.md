# skills/l-01-agent-lifecycles/core/invariants.md

## Purpose

The shared **invariants** block: the facts every role can count on, authored once so a role file
names the invariant it depends on instead of restating the set.

## Code Commentary

### Logic

`## Keep continuity in durable state` states why short-lived Workers and Reviewers are safe and why
**every seat writes its artifact of record** — a finding held only in chat is a defect. It is also the
home of the shared evidence rules: check the complete population and read the producing call before
counting, claim absence only from an unfiltered search, report what a check ran and left out, read the
clock for each recorded time, compare the serving tool build with the code before calling a mismatch a
defect, and name the graphics setup behind a browser measurement. `## Record decisions on their durable
surface` puts developer-needing decisions on the visible task decision surface with the analysis in
`notes/`, and sends a parented seat's developer questions through that parent.

`## Let dependencies determine the work order` makes independent work parallel by default, requires a
named reason for sequential work (a gate, one writer for a shared file, an explicit ruling or a harness
without sub-agents), forbids an invented concurrency cap, keeps landing order serial, and forbids adding a
new guard or restriction without a repeated issue the developer accepts. `## Keep the work observable`
keeps coordination seats on their selected task documents and chats; taskless Architect and Bootstrap
seats need no invented document. `## Connect task, branch and worktree` fixes what creates a branch or
worktree, that planning and design create none, and that chat is never a build route; small code work
uses the leaf task template.

`## Fill small gaps without changing the plan` states the fill-small-gaps default, sends a larger plan
change to the parent, and keeps the **spirit test Orchestrator-only**, defined in the Orchestrator role.
`## Resolve settings and capabilities` resolves launch settings from the global and repository layers,
then role and level overrides, then an admitted call; the role-setting keys are harness, model, effort,
serviceTier, mode, featureValues, notes, extraArgs and stepUp; unknown orchestration keys fail loudly,
except that `designer` and `strategist` role keys are accepted and reported as ignored; there are
deliberately no per-harness role files; and `role_start` is the harness-independent role-agent start.
`## Keep each instruction on its owning surface` sends scoping to `reference/tasks/collaboration-method.md`,
task authoring to the leaf, master and requirement-packet templates and
`reference/tasks/document-authoring.md`, and repository specifics to the memory layer's `system/*` files,
including `system/skill-writing-guidelines.md` and `system/design-guidelines.md`. It states that a started
role's first message carries its role text, operation text and the every-role digest and loads no other
core file, and that Git runs only against a resolved code or memory root.

### Conventions

Keep each invariant to the statement and its consequence; reference files own delivered details and
supporting reasons.

### Invariants And Boundaries

- Continuity lives in the task tree plus written artifacts, never in a transcript.
- Sequential execution is the exception and must name its reason.
- Only the launch-setting rows are settings keys; `dispatch` and `tools` are structural descriptions.
- There are deliberately no per-harness role files.
- The corpus splits ownership: roles own duties, operations own step procedures and reference files own delivered details; a started role's first message carries its role, its operation and the every-role digest and loads no other core file; source doctrine is not evidence of delivered capsule contents.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References

- Task intent creates its branch and build worktree; planning, design and chat are not build routes. [10]

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.

- Shared durable continuity and artifact-of-record obligation, with the shared evidence rules. [1]

- Questions, analysis, rulings and parent relay. [2]

- Dependency-based sequencing, the guard rule and observability. [3]

- Small gaps, escalation to the parent and Orchestrator-only spirit test. [5]

- Portable roles, settings precedence, permitted role-setting keys and harness-independent role start. [6]

- Task collaboration, task format, repository memory commands, role duties, operation procedures and reference details have separate owners. A started role receives its own role, operation and every-role digest; it loads no other core file. [7]

- Selected Orientation starts from supplied assignment and forbids loading other role/core files. [8]

- The Architect owns the developer conversation for delegated work; a parentless seat uses its own chat and backend seats keep their parent relay. [9]

- Launch settings own the role-setting rows: harness, model, effort, serviceTier, mode, featureValues, notes, extraArgs and stepUp. [11]

- Task collaboration, format, memory-specific commands and role/operation duties have separate instruction owners. [12]

- The instruction-boundary rule states that a started role receives its role text, operation text and the shared every-role digest in its first message, and loads no other core file. Retained core corpus is an authoring reference, not evidence of a particular launch. [13]
