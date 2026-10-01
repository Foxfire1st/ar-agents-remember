# l-01-agent-lifecycles/operations/bootstrap.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The **bootstrap** operation: the new user's first hour, end to end, with the memory repository as
its centre of gravity. It is one of the nine operation-scoped blocks in
`skills/l-01-agent-lifecycles/operations/`, and it is the one the tenth role carries and no other
role does.

It owns the ordered workflow, the failure-state inventory, the conformance-evidence standard and
the authority gates. It **runs** the surface that owns each step and **points at** the `c-*` skill
that documents it; it never restates the skill's procedure.

## Code Commentary

### Logic

**Selection.** The operation applies when a repository has no working memory root yet, or has one
that does not resolve: no memory root, a memory root with no baseline, the removed repo-local
layout, a coordination root that will not resolve, or providers configured but not indexing. Once a
repository has an attributed baseline and a resolving context, ordinary work belongs to the
lifecycle roles — this operation is not a maintenance posture, and re-entering it to "tidy" a
working installation is out of scope.

**The carrier is a free agent.** The block states its own start route rather than leaving it to the
role card: a regular session opens a session with `role=bootstrap` and **no task document**, the
role travels into the new session's environment as `AR_SPAWN_ROLE`, and the role is admitted by name
as a taskless seat so the call opens rather than refusing. There is no brief because nothing
dispatches it; the operation's instructions reach that session as the compiled capsule. It
therefore never waits for a task document to appear and never treats its absence as a condition to
repair. The `## Who carries it, and their job` table names exactly one carrier.

**Required inputs are facts about a workspace, not about a task**: which code repository and its
absolute root, the resolved `coordinationRoot`/`workspaceRoot` from `server_info`, whether a memory
root already resolves and its state, and the developer's three decisions asked one at a time —
which code branch is the **spear** the memory is founded on, new versus existing memory repo, and
index now versus defer.

**The workflow is seven ordered steps**, each naming its owning surface: say what Agents Remember is
and what the setup will change before asking anything; establish the resolved context or report the
exact missing fact; take and confirm the decisions; initialize or repair the memory root through
`memory_init` with `dry_run=true` first; scaffold the first onboarding through
`c-03-repo-bootstrap`; adopt the first attributed baseline through `memory_baseline_adopt` with
`memory_baseline_status` read before and after and the drift-acceptance decision put to the
developer; and configure indexing or say plainly that it is deferred.

**The failure inventory is seven rows**, each with the surface it is observed from: no memory root,
unsupported topology, dirty memory repo before adoption, missing providers, unresolvable
coordination root, memory root that is not a Git repository, and baseline already adopted. Two are
worth naming here because they are the ones a reader is most likely to get wrong. *Unsupported
topology* is refused by name and never substituted, and an existing repo-local `ar-memory/` root is
**reported with its exact path and never migrated, rewritten or deleted**. *Dirty memory repo before
adoption* records that adoption commits the content it finds, so uncommitted work becomes the
baseline — read the tree, not the drift report, and get explicit agreement before adopting.

### Conventions

- The operation block carries no procedure copy. Every step names the surface that owns it and the
  `c-*` skill that documents it.
- **Every effectful step is previewed with `dry_run=true`, and every mutating step is followed by a
  call that states the resulting state.** A step that was applied but never read back is not
  complete.
- The report is written to a durable, developer-visible path, and the report's own first line
  states that exact path, because nothing dispatches this agent and nothing names a path for it.

### Invariants And Boundaries

- **One carrier, and it is a free agent.** No other role carries this operation; a seat already in a
  sprint, master or leaf does not become a bootstrap seat to fix its own context — it resolves
  context through `c-08-ar-coordination-context-resolver` and, if setup is genuinely missing, says
  so and stops.
- **The conformance standard is re-derivability, not acceptance.** This agent has no independent
  acceptor: no task document, no gate, no reviewer in its loop. Its report is *completion truth* —
  a claim by the seat about itself — and must never be presented as an acceptance.
- **A failure is reported as a failure.** The report's own "Steps Skipped Or Failed" section carries
  the real output; a report with an empty failure section and a success claim that cannot be
  re-derived is the defect this standard exists to catch.
- **The absent task altitude, worktree and gate are the shape, not a gap to close.** The block says
  so explicitly and forbids adding a task altitude to make the seat look like the other roles.
- **The capsule delivery gap is stated, not smoothed**: the capsule that is this agent's only
  instruction source is delivered to a launch by separate work, and until then a started session is
  booted with no instructions.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local operation block.

No relevant documentation found after checking live sources.

### Repo-Internal References

- Canonical source this package-data copy is sync-propagated from. [1]
- Selection rule, carrier start route, and the one-carrier table. [2]
- Required inputs, including the three developer decisions. [3]
- The seven-step ordered workflow, each step naming its owner. [4]
- The seven-row failure inventory a new user actually hits. [5]
- The conformance standard: re-derivability, no independent acceptor, failures reported as failures. [6]
- The authority gates, including the absent-altitude-is-the-shape rule. [7]
- The two known failure-handling rows, including the capsule-delivery gap. [8]
- The manifest entry binding this operation to its single carrier. [9]
- The operation vocabulary extension that publishes `bootstrap` as the ninth operation. [10]
- The role card this operation is the procedure for. [11]

### Cross-Repo References

No sibling-repository contract defines this operation block.

No meaningful cross-repo references found.

## 260921-ICR-L27 The Operation's Sixth Step Reaches The Knowledge Foundation

`260921-ICR-L27` (`ICR-R27@v1`) inserts a new step 6 — *Reach the repository's knowledge foundation* —
into this operation and renumbers the steps around it (baseline adoption becomes 7, provider indexing
becomes 8). "What it covers" gains the foundation among the first hour's stages, and "When it is
selected" records that a repository which resolves but whose knowledge foundation is not recorded is
reached by **step 6** rather than by a re-entry.

The step states the seat gate in the code's own vocabulary, and `260921-ICR-L32` changed it on the
developer's 2026-09-24 ruling: the roles admitted without a task document are the taskless seats
`chat`, `terminal`, `bootstrap` **and `curator`**, while every other role is refused (`400
task-binding-required`, "named role scope is required"). So this seat reads the state, reports which of
the four states it is, and hands the authoring on — to a **taskless curator session** for a repository
with no task at all, which authors the foundation under the curator's own rules; it **authors no
records** itself. The step is also explicitly **not conditional** on the operation's other steps:
it needs a memory line that resolves `HEAD`, not an onboarding corpus and not an adopted baseline, so a
repository whose knowledge begins before its onboarding is a supported order rather than a defect.
> **Seat-policy note at L27's bytes (dated 2026-09-24).** This records the policy of the candidate that curation read: code base `06ed70cfcde7e3860ee5b53435727e7512e4335c` plus that leaf's working-tree delta, where a document-less `curator` session was refused `task-binding-required` because `TASKLESS_SEAT_ROLES` was `{"chat", "terminal", "bootstrap"}`. That was true of those bytes and is **superseded** — whether `curator` joined the set was then a product decision under revision, and it was taken in `260921-ICR-L32`.
>
> **Seat-policy note at these bytes (L32 curation, dated 2026-09-24T17:20+02:00).** At the bytes this curation read — code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus this leaf's working-tree delta — `TASKLESS_SEAT_ROLES` is `{"chat", "terminal", "bootstrap", "curator"}`: a document-less `curator` session is **admitted** and receives the curator capsule, while every other role is still refused `task-binding-required`. Read the sentences above as the policy **at these bytes**, not as a permanent property of the product.

The failure table gains four knowledge rows, and their whole point is that the states stay distinct:
`not-recorded` (step 6's real work, not a failure), `recorded` (read it before extending it; never
reinitialize), `unusable` with the shipped refusal code (`selected_input_unavailable` when there is no
file to open, `snapshot_unavailable` when the bytes are not the expected dataset — report state, path and
code, and never delete, overwrite or migrate it, and never report it as `not-recorded`), and
`context-not-admitted` as an **admission failure that is not a knowledge state at all**. The prohibition
list gains "It does not author the knowledge foundation", and the completion sentence now requires the
foundation's state — recorded at an identity, or the named state that says it is not.

**This card describes a generated copy**, propagated from
`skills/l-01-agent-lifecycles/operations/bootstrap.md` by `scripts/sync-skills.py` into this package-owned
copy and the eight harness starter packages.
