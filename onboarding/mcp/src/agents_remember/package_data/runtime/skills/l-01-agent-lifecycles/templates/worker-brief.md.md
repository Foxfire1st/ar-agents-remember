# l-01-agent-lifecycles/templates/worker-brief.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/worker-brief.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-13T14:32+02:00 |
| lastVerifiedCommitHash | `a89a6fc88d9330eb2749c87b3dcc3f6c4e46c4bd`                                  |
| lastVerifiedCommitDate | 2026-08-14T12:44:51+02:00|

## Purpose

Packaged runtime copy of the complete worker dispatch brief. The canonical template owns the packet;
the sync process installs this exact artifact.

## Code Commentary

### Logic

The manager calls `dispatch_agent` with the canonical leaf document, role `worker`, and this brief.
The control plane binds the occupant privately. The worker edits code, runs the scoped checks, and
writes the builder report; it never commits or writes onboarding. Its curator handoff supplies
observations and evidence, while the curator independently reconciles existing, ruled, and
implemented intent before writing memory.

### Conventions

Fill every placeholder, include exact code and memory worktree paths, state the quality ladder, and
keep the worker's authority limited to code plus its report. Edit the canonical template and
synchronize.

### Invariants And Boundaries

- The brief addresses `(leaf document, worker)` and carries no runtime address.
- Leaf closeout requires builder code, reviewer verdict, and curator coherence.
- Forward-looking observations are not accepted system intent until curator reconciliation.
- This packaged artifact must remain byte-identical to the canonical template.

### Todos

None recorded.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

### 260731-EFA-L17 — Change-Set-Scoped Leaf Checks

The worker brief's Checks section makes the pinned Dagger graph the Agents Remember acceptance
boundary. Leaf work selects targeted mode and supplies its explicit leaf diff base; full mode is
not a worker check and runs once at master integration. Direct host pytest/wrapper commands are
refused, never acceptance or fallback. `memory_quality_check` stays a per-leaf closeout gate.

## L23 Final Candidate Disposition

Worker briefs name the governing ownership route and required forcing evidence so the later
independent review can bind its verdict to the exact candidate. Workers do not self-certify Dagger
acceptance or carry durable-operation secrets.

## R39 Generic Worker Brief Contract

The template tells the dispatcher to copy repository-specific acceptance command, environment,
and evidence requirements from resolved memory. It forbids an invented runner or fallback and
keeps acceptance at leaf closeout and master integration only.

## Update History

- 2026-08-14T11:25+02:00 — R39 curator: made worker acceptance instructions repository-resolved
  and exact-once. Verification remains closeout-owned.
- 2026-08-14T06:34+02:00 — L23 synchronized runtime template: worker briefs retain route ownership
  and candidate evidence needed for independent review without delegating acceptance authority.

- 2026-08-13T14:32+02:00 — L23 final curator pass: synchronized Dagger-only targeted leaf
  acceptance, the required explicit diff base, master-owned full mode, and diagnostic-only host
  commands. Verification remains closeout-owned.
- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: synchronized the
  worker brief's host-managed master-gate default while preserving literal
  pytest `-n=auto` and targeted leaf checks.

- 2026-08-11T19:58+02:00 — Reconciled `worker-brief.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the worker-brief
  template's targeted leaf-check command and the full-wrapper master-gate home.
  Verification metadata stays pinned until closeout stamps the 260731-EFA-L17
  commit.

- 2026-08-05T21:55+02:00 — 260731-EFA-L16 curator: recorded the brief's new "Coding guidelines" section (developer ruling) — the brief is the worker's entire session start, so a rule absent from this template does not exist for a spawned worker; that is how `system/coding-guidelines.md` sat unread through three violating leaves. Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-07-10T15:48+02:00 — 260707-HFX2-L17 generated-runtime doctrine delta: the worker dispatch
  contract now states that `AR_SPAWN_ROLE=worker` and the qualified leaf together claim the
  worker's `(leaf, role)` seat. Verification metadata remains pinned until closeout stamps the L17
  commit.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 reviewer N7: recorded the stale echo/paste-chip
  instruction as current source debt awaiting a doctrine follow-up. No source behavior changed.

- 2026-07-07T21:40+02:00 — 260707-HFX-L6R3 curator seat: worker briefs now state
  the manager -> builder -> reviewer -> curator closeout chain, mark the memory worktree as
  context for changed-path notes, and require curator handoff input instead of same-pass onboarding
  writes by the worker. Sync-propagated bundle copy. Verification metadata pinned until closeout
  stamps the HFX-L6 commit.

- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the fenced brief opens with the canonical ROLE BRIEF — worker line (uniform with manager-brief).. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - Created file-level onboarding for the new worker-brief template (L9
  lifecycle convergence): the proven L3–L8 dispatch shape institutionalized, absorbing frictions
  F-E/F-F/F-H/F-I. Verification metadata pinned until closeout stamps the L9 commit.
