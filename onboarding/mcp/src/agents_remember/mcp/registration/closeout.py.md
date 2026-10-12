# mcp/src/agents_remember/mcp/registration/closeout.py

## Governing Overview

[registration route overview](overview.md)

## CCR-R12@v5 Current Public Contract

The registered closeout and integration tools advertise transaction previews and applies. A
closeout apply validates explicit approval, candidate/source identity, and Git safety before
committing code, refreshing and committing attributed external memory, and refreshing the
consumer ledger cache when possible.
Integration rejudges a converted leaf's closeout-cell pair before refs move in preview and apply. Master final, checkpoint and recorded routes run validator, net staleness, actual-endpoint chain proof and new-history ownership. Recorded leaf landing runs the shared leaf-pair judgment and keeps the closed-history check. Direct landing accepts `leaf_id`, or infers the sole open owner. These descriptions do not add broad quality/certification/review gates.
Neither public route promises or invokes strict code quality, memory quality, selected
certification, curator coherence, or independent review during normal execution; full suites are
only an explicit developer request. The older altitude-ladder wording below is historical
pre-R12 documentation and is superseded for these routes.

## Granted direct publication contract

direct_landing selects the exact canonical leaf. With code_commit it verifies existing code; without it create mode needs code_commit_message, memory_commit_message and the previewed code candidate_tree on apply. Direct create executes its own pre-code exact-pair census before one provisional code commit and pairs memory in the same accepted generation. This explicit direct route is the exception to ordinary closeout/integration no-test/review execution, not a new generic transaction gate or settings fallback.

## Historical pre-CCR-R12 EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## 260731-EFA-L17 Change

The five tool declarations are all keyword-only (bare `*` — the L8 remediation completed
here for `worktree_cleanup`/`worktree_abandon`, which still had positional parameters),
and the published docstrings now state the quality altitude ladder: preview/apply
describe the leaf change-set-scoped contract (`--targeted`: changed files +
reverse-import closure + derived test subset, mandatory CRAP over the changed modules)
and say the full wrapper is NOT a leaf gate; `worktree_integrate` states that it runs the
altitude-routed gate itself before any merge (leaf targeted; master full with
host-managed RAM/swap by default and an optional explicit
`orchestration.qualityGate.memoryCapBytes`). The registered tool surface is
unchanged.

## Purpose

`register_closeout_tools(server, config)` declares the **landing half** of a task:
`direct_landing` (the explicitly selected branch-addressed delivery for a leaf implemented without
an enclosure, requiring its current external canonical-leaf grant),
`worktree_closeout_preview`, `worktree_closeout_apply`,
`worktree_integrate`, `worktree_checkpoint_landing`, `worktree_cleanup`, `worktree_abandon`.

`worktree_checkpoint_landing` (260831-LOCR-L30, docstring corrected by 260831-LOCR-L34 and again by 260831-LOCR-L36) is the
partial-master landing route registered between `worktree_integrate` and `worktree_record_landing`.
Its published docstring is the contract a client sees: it **partially publishes** an **unfinished**
atomic master's accumulated line and keeps the master open, shares `worktree_integrate`'s whole preflight and ref move
while dropping only the completion assumptions (`worktree_integrate` proves the task document
`Completed`, one landed enclosure per canonical leaf, **and a completed closeout** — an unfinished master
has none of those), captures the master's own committed refs (the live series code work branch tip
and the live memory work branch tip) and proves the source ancestry before landing
exactly those, records the integration cell as `checkpointed` rather than `completed`, retires nothing
and runs no cleanup, and is MUTATING with a `dry_run` preview. The L34 correction matters because the
published text is the only thing a client reads: the old wording omitted the closeout requirement,
which is exactly what made the route unreachable.

**The L36 correction is the route's name.** The description used to open "Use this to pause a
master", which routes an ordinary stop request into a protected-branch publication: the ref move puts
the master's committed code and memory where every other master sees them, under an explicitly
required developer approval. A pause is a separate matter — it stops the master's work, publishes
nothing, moves no ref, and leaves its branch, worktrees and enclosure private. The published text says
so, and a case in `mcp/tests/test_tools.py` pins the distinction. **The stop itself is real since
260831-LOCR-L37**, registered as `worktree_pause` by the sibling working-half registrar
(`mcp/registration/worktrees.py::_register_worktree_stop_tools`), and its own description points back
at this publication as the separate, explicitly requested one. This route registers only the
publication; the L36 sentence above must not be read as "no such tool exists" — it did not at L36, and
it does now.

The public registration entry delegates to four cohesive helpers:
`_register_direct_landing_tools` for the branch-addressed direct landing (260815-DAG-L16),
`_register_closeout_command_tools` for preview/apply,
`_register_integration_command_tools` for integration/cancellation, and
`_register_reclamation_command_tools` for cleanup/abandonment. The `_tools` suffix is deliberate:
the structural exemption remains attributable only to tool declarations and registrar functions,
not arbitrary helpers. The split changes registration structure only; tool names, signatures, and
payload owners remain unchanged.

## Code Commentary

Closeout apply accepts typed `RedCatalogDisposition` values and forwards them as a tuple to the payload/application owner. These are explicit corrective dispositions, not permission to bypass a failed catalog or weaken gate authority.

Current IAS policy treats coverage as diagnostic and production CRAP above 20 as a review signal, not a numeric rejection. The retained registration docstrings still contain older mandatory-CRAP wording; that wording is stale and must not restore a metric gate. Full suite and whole-master review remain master-end obligations. The registrar preserves distinct commit messages and approval intent, and an accepted journal generation survives disposable queue loss.

### Logic

Current registered signatures expose code and memory commit messages. Direct landing requires the canonical leaf reference: verify-existing needs no code message, while create needs its code_commit_message and applicable memory_commit_message. Integration and checkpoint
landing take no ledger message, and PR landing records only code plus optional memory content.
The retained ledger is a downstream computed cache, never an MCP-requested Git output.

The preview/apply pair (`worktree_closeout_preview` L24-L46, `worktree_closeout_apply` L47-L76)
share `CloseoutCommitMessages(code, memory)`, built in each body from
the two flat message arguments. Apply keeps a **second** object, `CloseoutApproval(intent_note,
dry_run)`, precisely so the approval-bearing half cannot be confused with the commit text: folding
`dry_run` in with the messages would let a preview read as an approved apply. A preview is a
read: it writes only the leaf's worklist, its quality reports and the judged tree's objects, and
never falls back to writing anywhere else.

**Historical quality-gate registration, superseded by the current transaction boundary above.**
The former docstrings stated a pre-commit gate order. Preview reports whether strict
project-owned quality under the selected project checks will run — since 260731-EFA-L4 the
description is specific about *what it runs over*: "over the staged task worktree before the code
commit", not merely "before the code commit".

Apply's docstring was rewritten in the same leaf, and it is now a conditional statement rather
than an unconditional one. It reads: when code would commit **AND the checkout carries the
project-owned quality wrapper**, apply resets the index, stages the whole task worktree, and runs
strict quality with diagnostic CRAP reporting **over exactly that staged content**, before any
code, memory, ledger, contract, or applied-gate **commit**; then commits code, memory and ledger
in order. It states four things the previous text did not:

- **Staging is what lets the gate see files the task created**, not only the ones it edited; the
  **reset** is what makes a retry stage what a first run would, instead of inheriting a refused
  attempt's index.
- **Staging is not undone when the gate refuses** — the checkout staged is the task's own
  disposable worktree.
- The **two refusals guard that staging step**, so they run only where the gate runs: apply
  refuses before staging when the code checkout is not a task worktree (a series/master contract
  records the repository path itself) or has unresolved merge conflicts.
- A checkout carrying **no wrapper** runs neither the gate nor those refusals and reaches the
  ordinary commit step's own `git add -A` exactly as it always has.

The blocker wording also narrowed from "before any … mutation" to "before any … commit", which is
the accurate claim now that staging is itself a mutation the gate performs. The published process
recommends preview before approval/apply, but apply independently validates the same effective
input and does not treat a prior preview as authority; apply requires `intent_note`.

The publication and reclamation tools forward flat:

- `worktree_integrate(contract_path, strategy='ff-only'|'replay', dry_run)` —
  checks accepted candidate/source and Git authority, then moves branch refs; protected branches need explicit approval.
- `worktree_checkpoint_landing(contract_path, strategy='ff-only'|'replay', dry_run)` — **partially publishes** an **unfinished** atomic master's line and keeps the master open;
  requires the same explicit developer approval as `worktree_integrate`; captures the master's own
  live code and memory work-branch tips and proves source ancestry; records `checkpointed`,
  retires nothing, runs no cleanup. It is not the pause: a pause publishes nothing and moves no ref.
- `worktree_cleanup(contract_path, dry_run, teardown_providers=True)` — removes worktrees and merged
  task branches **after** integration, and by default reclaims the worktree's isolated provider stack.
- `worktree_abandon(contract_path, dry_run, force)` — discards a task without integrating it. Unlike
  cleanup it needs no completed integration; without `force` it refuses dirty worktrees and unmerged
  branches and reports the commits, with `force=true` it discards them
  (`git worktree remove --force`, `git branch -D`). Since 260831-LOCR-L30 the series abandon guard
  also refuses a master whose integration cell reads `checkpointed`, not only `completed`.

### Conventions

Keep registered signatures and descriptions aligned with the application request models. Registrars pack inputs; they do not acquire a second publication authority.

### Invariants And Boundaries

- Keep `CloseoutApproval` separate from `CloseoutCommitMessages`.
- The public direct-landing description must distinguish its narrow leaf-without-enclosure route
  from ordinary master/series closeout and integration; contract kind alone does not select direct
  execution, and those ordinary lifecycle routes do not gain a grant prerequisite.
- Preview is the non-mutating inspection surface, but it is not durable authority that apply may
  trust. Preview and direct apply each normalize the same effective input independently; apply
  additionally carries `CloseoutApproval`. A direct apply must therefore remain safe without a
  preceding preview.
- Closeout is worktree-only; the retired `direct_closeout_*` tools are not registered anywhere.
- Application composition lives in `application/worktree_tools.py`; Git publication and recovery
  belong to the worktree operation owners.
- **These docstrings are the published MCP tool descriptions**. They must describe the current
  candidate/source checks, explicit approval, and code/memory publication behavior. The historical
  wrapper-gate description above is superseded and must not restore a normal quality gate.
- Keep internal registrar helper names ending in `_tools`; the suffix is part of the narrow
  structural-rule attribution for this declaration-only route.
- **The checkpoint docstring must name the whole completion refusal set, not two of three
  (260831-LOCR-L34).** It said the route dropped only the two "master is finished" assumptions while
  the code also demanded a completed closeout — and that omission described a route a client could
  not actually use. A published refusal list is a promise about what will *not* happen; keep it
  complete when the gate changes.
- **The checkpoint description must present a partial publication and deny being the pause
  (260831-LOCR-L36).** "Use this to pause a master" invited an agent to publish unfinished work for
  an ordinary stop request — changes the developer never asked to publish. The text must keep saying
  that the route moves committed refs onto the protected source branch under explicit approval, and
  that pausing is a separate matter which is NOT this call. `mcp/tests/test_tools.py` pins the
  wording (`PUBLISH`, "not a pause", "separate matter and is NOT this call") and asserts the old
  invitation is gone.

### Todos

No additional file-local TODO is established by this candidate review.

## Evidence

### Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

No configured external domain source applies.

### Repo-Internal References


- Registered direct/ordinary closeout and integration tools expose no ledger message or landed-ledger argument. [1]

- The payload builders these forward to. [2]

- The checkpoint-landing tool declaration and the payload builder it forwards to. [3]

- `CloseoutCommitMessages` and `CloseoutApproval` remain distinct request concepts. [4]
- Refuse to stage anywhere except a task's own throwaway worktree. [5]
- Refuse before staging when the checkout has unresolved conflicts. [6]
- Prepare and certify a fresh candidate through the ordinary gate entry point. [7]
- The case that pins the checkpoint description as a partial publication and denies it is the pause. [8]
- The wrapper condition decides whether the gate — and therefore staging and its refusals — runs; the preview exposes the selected mode, executor, and cap. [9]

### Cross-Repo References

No separate cross-repository implementation claim is made.

No external implementation source applies.

### Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.


### Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
## Historical R39 Integration Tool Contract

Before the current transaction-only boundary, the integration description stated that leaf integration lands the acceptance already
bound to its closeout commit without rerunning it. Only master integration owns a new acceptance
run: full mode through the pinned Dagger executor.

## 260815-DAG Master Full-Gate Repair

`_register_direct_landing_tool` was renamed to `_register_direct_landing_tools` (the direct-landing registration group); the registered tool surface is unchanged.

## 260821-CLIVE-L1 Public Surface

Worktree closeout and direct landing expose optional message fields syntactically because enabledness is route/contract/candidate-dependent; runtime validation requires each enabled field to be stripped and nonblank. Worktree preview/apply accepts code and memory fields and returns `effectiveInput` or field-specific `invalidFields` with `resolvedPlan` and `correctedCall`. For direct landing, verify-existing accepts memory intent without a code message; create accepts explicit code and memory intent with the canonical bound leaf and previewed tree. The memory message is required only when its contract-derived leg is enabled; a typed not-applicable leg may omit it. Invalid input is refused before authority or Git.

## 260821-CLIVE-L2 Current Contract

The current source seams include `register_closeout_tools`. The public schema/composition layer exposes task-addressed controls plus explicit legacy and enclosure-adoption routes without private operation ids. Registration and payload building do not own journal state or compatibility decisions.

### Reconciled Source Evidence

- The current module exposes `register_closeout_tools` at this ownership boundary. [10]

## 260821-CLIVE Final Closeout Tool Descriptions

The public descriptions now state the durable ownership boundary directly: direct landing and
closeout recovery use the retained operation journal, never a transient landing lock or queue row;
queue invalidation does not affect an accepted generation. Cleanup and abandon first archive and
read back bounded canonical enclosure evidence, publish the external receipt, and only then remove
worktrees, branches, reports, providers, and the enclosure root. Active, ambiguous, unreadable, or
mismatched evidence refuses deletion. Shared grade/admission request types come from the canonical
closeout-source model.
