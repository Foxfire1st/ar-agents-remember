# mcp/src/agents_remember/controlplane/signal_routing.py

| Field                  | Value                                                             |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/signal_routing.py`           |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-07-31T00:00+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                                      |

## Governing Overview

[overview.md](overview.md)

## Purpose

R4 (260707-HFX2-L1): derive a signal's routed owner address from catalog spawn provenance — one
hop up the spawn edge (worker -> its manager, manager -> its orchestrator), never further (a
developer ruling: no layer is addressed its grandchildren's noise). `is_seat_dead` is the liveness
check the rebind/mailbox machinery uses to treat "no evidence of life" the same as "confirmed
dead". The escalation ladder's two-hop skip-level walk (`derive_skip_level_owner`) is DELETED with
the ladder (260713-TES-L5); dead-owner rows surface through the rebind/mailbox machinery.
**260713-TES-L4 (R13/N14)** adds repository+sprint-scoped architect custody
(`derive_architect_owner(catalog, leaf_key=...)` — never global first-match) and row-based
sweep-time owner derivation (`derive_row_owner`), the identity machinery behind N14 rebinding.

## Code Commentary

### 260707-HFX2-L17 Current-Seat Routing

Current discovery, leaf anchoring, chain credit, manager scoping, and architect lookup use
`binding_role`/`binding_leaf_key`. Different roles on one leaf are visible and unbound replacements
still credit their declared leaf. The historical `_derive_spawn_owner` ladder hop is deleted with
the escalation ladder (260713-TES-L5) — nothing reconstructs a dead seat's spawner for a skip-level
walk anymore.

### 260707-HFX2-L13 Manager-First Routing And Chain Progress

Worker, reviewer, and curator signals now resolve the live direct manager first, then a manager
proven on the same qualified leaf/master, and otherwise the role-only manager mailbox. Address-time
routing never guesses a manager from another master and never jumps directly to orchestrator or
architect. The older spawn-provenance walk is gone with the ladder (260713-TES-L5).

`leaf_chain_has_progress` suppresses stale expectations, inactivity signals, redelivery, and rung
escalation when another exact-leaf seat, the current manager, or an unbound reviewer/curator spawned
by that manager in the subject worktree has progressed. Current code deliberately excludes unbound
workers from that active-phase credit. The round-2 reviewer accepted the resulting bounded
false-inactivity refire risk as non-blocking because manager addressing, cooldowns, the five-minute
floor, and completion wake bound it; HFX2-L14 S7 owns extending same-worktree/current-manager credit
to the unbound worker without cross-leaf suppression. Do not document or infer that S1 is fixed here.

### Logic

Architect ownership is now resolved inside the row's exact repository+sprint boundary. A bound
architect may retain custody after leaf movement, but no lookup falls back to an architect from a
different sprint or to one workspace-global architect. Rebind-chain traversal likewise stops at
the sprint boundary, preserving N14 routing isolation while reusing the existing
`derive_architect_owner` seam.

**260707-HFX2-L15 replacement-chain discriminator.** An unbound worker, reviewer, or curator counts
as progress for a leaf only when it was spawned by the current manager and its catalog row carries
`replacementForLeaf == leafKey`. The former same-`cwd` comparison was removed because production
seats share the workspace root and could let activity on a parallel leaf suppress this leaf.

`_OWNER_ROLE_BY_SENDER_SPAWN_ROLE` maps the SENDER's own spawned-as role to its owner's role:
`worker -> manager`, `manager -> orchestrator`. Any other spawn role (orchestrator, strategist,
reviewer, designer, ...) has no entry, so `derive_signal_owner` returns an empty `RoutedOwner()` —
"no route derived, keep the caller's explicit `recipient_role`" — this module never fabricates an
address.

`derive_signal_owner(catalog, sender_agent_id=, message_kind=)`: a `message_kind ==
"decision-item"` always routes to the reserved `architect` role regardless of provenance (the
routing TARGET is reserved here; the decision-item QUEUE itself is a different leaf's job, AQR
Q3). Otherwise it looks up `sender_agent_id` in the catalog and reads the address straight off the
SENDER's own row: `spawned_by_session` / `spawned_by_lifecycle`
(`serving/terminal_catalog.py:48-59`) — no second catalog lookup is needed to resolve "the
manager's own session id" because that field IS it.

`RoutedOwner` is a frozen dataclass, not a Pydantic model — this module is pure derivation logic
with no wire/persistence concern of its own; the caller (`mcp/tools/operator_inbox.py::
operator_inbox_post_payload`) stamps the result onto the durable `OperatorInboxEntry`'s
`ownerRole`/`ownerAgentId`/`ownerLifecycleId` fields at post time.

**260707-HFX2-L4 (R2/R4).** `is_seat_dead(catalog, agent_id)` — `True` for `None`, an unknown
catalog id, or any non-`running` status; "no evidence of life" reads the same as "confirmed dead"
here, since there is nothing live to route TO. The two-hop `derive_skip_level_owner` walk
(rung-2 skip-level + dead-upstream grandparent target) is deleted with the escalation ladder
(260713-TES-L5): dead-owner rows surface through `derive_row_owner` rebinding and the scoped
architect mailbox, and `evaluate_dead_upstream_findings` still signals the grandparent via the
ordinary one-hop `derive_signal_owner` (no dead-node walk).

### 260713-TES-L3 Master-Key Helper Promotion

The former private `_master_key` helper is now the public `master_key`
cit:([`master_key`], mcp/src/agents_remember/controlplane/signal_routing.py:52-58): the qualified `repo/master` prefix of a qualified leaf key, or
`None` for an unbound/legacy key. It remains the scope filter inside `_scoped_managers`
cit:([`_scoped_managers`], mcp/src/agents_remember/controlplane/signal_routing.py:110-128) (replacing the private-name call), and since 260713-TES-L3 it is also
consumed by `serving/state_signals.py` to master-scope compound-idle membership on EVERY arm
(binding + spawn provenance): a worker joins a manager's set only when
`master_key(worker.binding_leaf_key) == master_key(manager.binding_leaf_key)` (fix round 1,
F1). This is a mechanical rename + promotion with no routing-behavior change: `derive_signal_owner`
remains the one-hop manager→orchestrator route the compound-idle emitter and the manager
non-reaction residue use.

### 260713-TES-L4 Scoped Architect Custody And Row-Based Owner Derivation

`derive_architect_owner(catalog, *, leaf_key=None)` cit:([`derive_architect_owner`], mcp/src/agents_remember/controlplane/signal_routing.py:294-325) now
resolves the architect bound to the row's repo+sprint scope instead of picking the first running
architect globally (R13). The row's `leafKey` resolves to its master scope via `master_key`;
only running harness seats with `binding_role="architect"` whose `binding_leaf_key` or
`replacement_for_leaf` falls inside that scope are candidates, with an exact-leaf binding
preferred over the master-scope set. An unscoped/ambiguous set — or no scoped seat — resolves to
the role-only architect mailbox, fail-closed: a second repository's architect can never capture
another repo's rows. Dead-owner-chain rows surface to this mailbox through the rebind/expiry
machinery (N3/N14); no ladder `next_step` pass-through remains (260713-TES-L5).

`derive_row_owner(catalog, entry)` cit:([`derive_row_owner`], mcp/src/agents_remember/controlplane/signal_routing.py:364-383) is the N14 sweep-time derivation: the
row's durable subject identity (leaf key + seat role + subject agent), never its stamped address.
`dispatch-brief` rows return an empty owner (exact-pinned, never rebound). A worker/reviewer/
curator subject re-resolves its live manager (`derive_leaf_manager_owner`); a manager subject
re-resolves its orchestrator — live spawn provenance first, then a master-scoped replacement
(`_live_scoped_orchestrator`), else the role-only orchestrator mailbox. `_owner_for_stamped_role`
falls back through the stamped `ownerRole` for rows with no seat-role subject. A row whose entire
owner chain is dead surfaces to the scoped architect mailbox (N3 mailbox-not-rung) via
`_rebind_expired` in the sweep, not through this module.

### Conventions

Every "no route" case returns the same empty `RoutedOwner()` sentinel (all fields `None`) rather
than raising — routing derivation is best-effort surfacing, never a hard requirement a caller must
satisfy before posting.

### Invariants And Boundaries

- **`derive_signal_owner` remains one hop only**, unchanged by this leaf: a worker's signal never
  chases the chain past its manager to the orchestrator, even though the manager's OWN
  `spawned_by_session` is the orchestrator — routing reads only the SENDER's provenance, never
  recurses. A locked existing test (`test_no_layer_is_addressed_its_grandchildren_noise`) pins this
  invariant for THIS function specifically.
- Pure and catalog-read-only: neither function ever mutates the catalog or posts an inbox entry.
- `decision-item` routing to `architect` is unconditional — it does not consult the catalog at all
  (unchanged, `derive_signal_owner` only).
- The ladder's two-hop walk and its 64-node chain guard are gone (260713-TES-L5); the remaining
  derivations are bounded and pure (catalog-read only).

### Todos

None.

## Docs References

No meaningful external design-doc references found yet (created this leaf); the "no layer is
addressed its grandchildren's noise" rule is a developer ruling recorded in the leaf spec, not an
existing design doc.

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The owner address is read straight off the sender's own `spawned_by_session`/`spawned_by_lifecycle` catalog fields. | "class TerminalCatalogEntry:" | mcp/src/agents_remember/models/terminal_catalog.py:68-72 |
| The compound-idle consumer of the public `master_key` scope filter (both membership arms). | `compound_idle_sets` | mcp/src/agents_remember/serving/state_signals.py:69-103 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

## 260713-TES-L5 Current Delta — Skip-Level Walk Demolished

`derive_skip_level_owner` and `_derive_spawn_owner` are deleted with the escalation ladder: no
two-hop owner's-owner walk remains, and dead-owner chains surface through `derive_row_owner`
rebinding, the rebind-grace expiry, and the scoped architect mailbox. `evaluate_dead_upstream_findings`
still signals a live worker/manager's dead direct owner through the ordinary one-hop
`derive_signal_owner` (grandparent = owner of the owner by provenance, not a ladder rung). This
entry supersedes any earlier description in this sidecar that conflicts with the current source
behavior above; verification metadata stays pinned to the pre-commit source history until
closeout.

## Update History

- 2026-08-10T10:30+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded sprint-scoped architect custody and the
  no-cross-sprint rebind boundary. Verification metadata remains pinned until closeout stamps the
  code commit.

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the skip-level demolition —
  `derive_skip_level_owner`/`_derive_spawn_owner` deleted; dead-owner chains surface via rebind +
  scoped architect mailbox; dead-upstream signaling stays one-hop provenance. Verification
  metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded scoped architect custody (R13) —
  `derive_architect_owner(catalog, leaf_key=...)` resolves the repo+sprint-scoped architect
  with exact-leaf preference and fail-closed role-only fallback, never global first-match — and
  the N14 row-based derivation family (`derive_row_owner`, `_owner_for_role`,
  `_orchestrator_owner`, `_live_scoped_orchestrator`, `_owner_for_stamped_role`). Noted the
  `escalation_ladder.next_step` leaf-key pass-through. Verification metadata pinned until
  closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: recorded the `_master_key` → public
  `master_key` promotion (used by `_scoped_managers` and, since L3, by
  `serving/state_signals.py` for master-scoped compound-idle membership on every arm). No
  routing-behavior change; `derive_signal_owner` stays the one-hop manager→orchestrator owner
  for the compound-idle and manager-residue signals. Verification metadata pinned until
  closeout stamps the 260713-TES-L3 commit.
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.


- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 2 repository-reference citations (2/2 anchored and sourced; scoped citation check clean).

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/controlplane/signal_routing.py` since the L2 base commit is the whole-
  tree `ruff format` pass in `00e8379`, which re-wrapped 9 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds. Noted while checking: the references table also
  cites line ranges inside `terminal_catalog.py`; those ranges shifted because this task edited
  those files, so treat the cited numbers as approximate and the linked cards as authoritative.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: moved current routing and chain credit to binding
  identity while preserving the one intentional historical spawn-provenance ladder hop.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: replaced same-worktree unbound-seat credit with the
  explicit `replacementForLeaf` + same-manager discriminator and extended the allowed replacement
  roles to worker/reviewer/curator without cross-leaf suppression. Verification metadata remains
  pinned until closeout stamps the eventual L15 code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round 2: replaced stale one-hop leaf addressing with
  current-manager resolution, separated historical skip-level provenance, and added chain-progress
  suppression. Recorded the accepted S1 truth that unbound workers remain excluded until HFX2-L14.
  Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 (R2/R4, escalation ladder + dead-upstream detection):
  added `is_seat_dead` (liveness check — unknown or non-`running` reads as dead) and
  `derive_skip_level_owner` (a second, separate two-hop owner's-owner walk that skips PAST dead
  intermediates, feeding the ladder's rung-2 skip-level target and the dead-upstream grandparent
  signal). `derive_signal_owner`'s existing one-hop behavior is UNCHANGED — the locked
  `test_no_layer_is_addressed_its_grandchildren_noise` still asserts it. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T14:25+02:00 — 260707-HFX2-L1: created for R4 hierarchical routing derivation (worker
  -> manager, manager -> orchestrator, decision-item -> architect). Verification metadata pinned
  until closeout stamps the 260707-HFX2-L1 commit.


