# l-01-agent-lifecycles/templates/manager-brief.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/manager-brief.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T15:48+02:00 |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814`                                  |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|

## Purpose

The manager dispatch packet — the "ninth template" the adversarial review demanded (AR-12): the
orchestrator compiles a manager's entire session start from this shape, ending the
manager-dispatch folklore the same way worker-brief.md ended the worker's. It carries the ONE
load-bearing base fact only the orchestrator's own file used to state: the manager's master
integration branch bases off the **current super branch** (with the super-tip commit written in as
the reconciliation anchor), never off main.

## Code Commentary

### Logic

**260707-HFX2-L15 reviewer N7 current-source debt.** The source brief still says hosted delivery is
counted from a post-boot echo. L15's current runtime accepts the unique id only from the bound
harness log; a future doctrine edit must align this template without reviving screen predicates.
This note documents the mismatch on the unchanged source.

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/templates/manager-brief.md`. Opens with the canonical `ROLE BRIEF —
manager` header line (the router's condition-2 recognizer). Placeholder slots: the master + its
leaf list with dependency notes; orchestrator-compiled trust facts (no checkpoint re-run); the
branch base block (master branch off the CURRENT super @ tip); dispatch defaults (worker-brief
template, `AR_SPAWN_ROLE=worker`, pair claims from environment role plus qualified leaf keys, the
manager -> builder -> reviewer -> curator leaf closeout chain, fresh curator spawns with
`AR_SPAWN_ROLE=curator` on the curator `(leaf, role)` pair, concurrency,
and — **260707-HFX-L7** — a one-line "Provider degradation:" bullet); the exit block (spawn the
reviewer with `AR_SPAWN_ROLE=reviewer`, RAISE `master-handover-approval` with the verdict attached
— the ORCHESTRATOR decides; escalation to the orchestrator, never the developer; the human-pinned
kinds named); the report obligations (master-handover packet, leaf-review notes, decision-log
entries per delegated gate and reopen). Compiler notes bind the orchestrator: fill every
placeholder, state the super-tip anchor, echo-confirmed paste delivery.

**260707-HFX-L7 (provider degradation protocol):** the dispatch-defaults bullet list gains one new
bullet — "Provider degradation: on `messageKind="degradation-alert"`, do not start provider setup,
provider watchers, watcher restarts, or `retry_provider_setup` until an all-clear. Managers have no
provider kill authority; provider stops and fixes route through the orchestrator and
system-specialist." — placed after the existing curator-spawn bullet and before the concurrency
bullet. This is the SAME rule `roles/manager.md`'s new "Provider Degradation Alert" subsection
states in full; the template only needs the compact one-liner because the orchestrator compiling
this brief is telling a freshly-dispatched manager what to do, not re-deriving the doctrine — the
manager's own role file remains the authoritative source the brief's line summarizes. No other
brief section (branch base, exit block, report obligations) changed for this addition.

As of cycle 5: the exit block states the wait=false raise and the gateId-in-packet hand-off. Cycle 6: the raise call carries `enclosure="<master task name>"` (the integration guard's address), the exit block adds the all-human conditional (the raise blocks; do not pass wait=false), and "The master" block gains a planner-master path slot (`<path or n/a (flat run)>`), resolving the planner-master reach for a seat that must not read orchestrator.md. Cycle 7: the exit block pins the address to the EXACT master task name as the contracts carry it and states that the raise refuses without one (AR4-1c).

As of 260707-HFX-L11 (curator activation, R1/R4) the "Dispatch defaults" section's curator lines
were rewritten: the leaf closeout chain line now adds "— never before the curator pass exists"; the
curator-spawn line now points at `../templates/curator-brief.md` (not just `roles/curator.md`) and
states explicitly what the brief FEEDS — the landed change set (leaf contract's base-to-head
range) + the leaf task doc + notes/ — and that the curator routes each piece to the right onboarding
home (specific sidecar or governing overview; L3 Operational-Notes last-resort only) before writing
onboarding.

As of 260707-HFX2-L11: the "Dispatch defaults" section's "Cleanup" line now states that
`worktree_integrate` auto-lands successful worker/reviewer seats into the landed archive
(`retirement.autoLandOnIntegration`, default ON); `session_retire` is available for a
stuck/abandoned worker/reviewer/curator seat of the manager's OWN master only, and server policy
refuses any other target.
This is placed in Dispatch defaults (not the exit block) because the landing automation rides the
per-leaf integrate edge, the same section that already documents the worker-brief/AR_SPAWN_ROLE/
qualified-leaf-key/curator-chain dispatch defaults.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-10T15:48+02:00 — 260707-HFX2-L17 generated-runtime doctrine delta: manager, worker, and
  curator dispatch defaults now describe the environment-role-plus-qualified-leaf pair claim, and
  cleanup now names the manager's worker/reviewer/curator retirement boundary. Verification
  metadata remains pinned until closeout stamps the L17 commit.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 reviewer N7: recorded the stale post-boot-echo
  instruction as doctrine debt; no source behavior changed.

- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator correction: the manager brief template sidecar
  now describes `worktree_integrate` as auto-landing successful worker/reviewer seats into the
  landed archive (`autoLandOnIntegration`); `session_retire` remains only for exceptional
  stuck/abandoned seats under the manager's authority. Verification metadata pinned until closeout
  stamps the HFX2-L11 commit.

- 2026-07-08T02:55+02:00 — 260707-HFX-L8 (seat lifecycle: retirement, issue #12): the "Dispatch
  defaults" section gains a "Cleanup" line — `worktree_integrate` auto-retires a landed leaf's
  worker/reviewer seats (config-gated, default ON); `session_retire` is available for a
  stuck/abandoned seat of the manager's OWN master only, server policy refuses any other target.
  Sync-propagated bundle copy. Verification metadata pinned until closeout stamps the HFX-L8
  commit.

- 2026-07-08T02:10+02:00 — 260707-HFX-L11 curator activation (R1/R4): Dispatch defaults section
  updated to match the new curator-brief template — curator spawns now point at
  `../templates/curator-brief.md` and name the fed inputs (landed change set over the leaf
  contract's base-to-head range, task doc, notes/) and the mgmt-L4 routing rule; the leaf closeout
  chain line adds "never before the curator pass exists." Doctrine-only change set (7 canonical
  `skills/` files: 6 edits + 1 new template, each synced to 9 mirrors, 0 Python); sync-propagated
  (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/l-01-agent-lifecycles/templates/manager-brief.md`. Verification metadata pinned — no
  commit yet on `ar/260707-hfx-l11-curator-activation` (working-tree change, synced onto the landed
  HFX-L7 base).

- 2026-07-08T01:00+02:00 — 260707-HFX-L7 (provider degradation protocol): dispatch defaults gain a
  one-line "Provider degradation:" bullet (no provider starts/watchers/retry until all-clear; no
  manager kill authority; stops and fixes route through the orchestrator/system-specialist),
  mirroring `roles/manager.md`'s fuller "Provider Degradation Alert" subsection in compact
  brief-compiler form. Sync-propagated bundle copy. Verification metadata pinned until closeout
  stamps the HFX-L7 commit.
- 2026-07-07T21:40+02:00 — 260707-HFX-L6R3 curator seat: dispatch defaults now
  name the manager -> builder -> reviewer -> curator leaf closeout chain, the exact closeout
  inputs (builder code + reviewer verdict + curator memory pass), and the fresh per-leaf curator
  spawn. Sync-propagated bundle copy. Verification metadata pinned until closeout stamps the
  HFX-L6 commit.

- 2026-07-05T19:55+02:00 - L8 builder cycle 7: exit block pins the enclosure to the EXACT contract task name + states the enclosure-less raise refusal (AR4-1c). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: enclosure on the raise, all-human conditional, planner-master slot (AR3-1/AR3-2/AR3-6b). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the exit block states the wait=false raise and the gateId-in-packet hand-off.. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:30+02:00 - Created file-level onboarding for the new manager-brief template (L8
  seam-ruling remediation, cycle 4 — closes AR-12's dispatch-determinism gap). Verification
  metadata pinned until closeout stamps the L8 commit.
