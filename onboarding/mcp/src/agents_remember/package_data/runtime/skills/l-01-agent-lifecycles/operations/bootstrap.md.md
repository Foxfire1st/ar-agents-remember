# l-01-agent-lifecycles/operations/bootstrap.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/bootstrap.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-16T17:59+02:00 |
| lastVerifiedCommitHash | `0dd1df9a950d59ac9622e5fb54250e528df08fa5` |
| lastVerifiedCommitDate | 2026-09-16T20:47:18+02:00|
| governingOverview      | `../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../overview.md)

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

## Docs References

No external or domain documentation governs this repository-local operation block.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source this package-data copy is sync-propagated from. | `# Operation — Session Bootstrap` | skills/l-01-agent-lifecycles/operations/bootstrap.md:1-1 |
| Selection rule, carrier start route, and the one-carrier table. | `When it is selected:`; `How the carrier is started:`; `Who carries it, and their job` | skills/l-01-agent-lifecycles/operations/bootstrap.md:8-8; skills/l-01-agent-lifecycles/operations/bootstrap.md:14-14; skills/l-01-agent-lifecycles/operations/bootstrap.md:21-21 |
| Required inputs, including the three developer decisions. | `Required inputs` | skills/l-01-agent-lifecycles/operations/bootstrap.md:31-45 |
| The seven-step ordered workflow, each step naming its owner. | `Normal workflow` | skills/l-01-agent-lifecycles/operations/bootstrap.md:47-76 |
| The seven-row failure inventory a new user actually hits. | `The failure states a new user actually hits` | skills/l-01-agent-lifecycles/operations/bootstrap.md:78-91 |
| The conformance standard: re-derivability, no independent acceptor, failures reported as failures. | `How conformance is evidenced` | skills/l-01-agent-lifecycles/operations/bootstrap.md:93-111 |
| The authority gates, including the absent-altitude-is-the-shape rule. | `Authority gates` | skills/l-01-agent-lifecycles/operations/bootstrap.md:113-129 |
| The two known failure-handling rows, including the capsule-delivery gap. | `Failure handling` | skills/l-01-agent-lifecycles/operations/bootstrap.md:130-152 |
| The manifest entry binding this operation to its single carrier. | `"applies_to_roles"` | skills/l-01-agent-lifecycles/composition-manifest.json:127-135 |
| The operation vocabulary extension that publishes `bootstrap` as the ninth operation. | `CAPSULE_OPERATIONS` | mcp/src/agents_remember/models/role_capsules/vocabulary.py:98-110 |
| The role card this operation is the procedure for. | `# Lifecycle — Bootstrap` | skills/l-01-agent-lifecycles/roles/bootstrap.md:1-4 |

## Cross-Repo References

No sibling-repository contract defines this operation block.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T17:59+02:00 — 260915-CAPS-L13 curator: created this card for the operation block the leaf
  added (`CAPS-R13@v1`). It records the selection rule, the free-agent start route stated inside the
  block itself, the seven ordered steps with their owning surfaces, the seven-row failure inventory
  (including the unsupported-topology refusal that must never migrate an `ar-memory/` root), the
  re-derivability conformance standard with its no-independent-acceptor rule, and the authority gates
  that forbid "fixing" the absent task altitude. Companion card: `roles/bootstrap.md.md`. Verification
  metadata is left at the leaf base commit because the source is uncommitted — the governed closeout
  stamps the real code commit, and no hash or fingerprint was invented here.
