# mcp/src/agents_remember/controlplane/signal_routing.py

| Field                  | Value                                                             |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/signal_routing.py`           |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated | 2026-08-11T09:50+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                                      |

## Governing Overview

[overview.md](overview.md)

## Purpose

Routes owner signals through canonical task-document containment and role, resolving only the current
catalog occupant after the structural owner is known.

## Code Commentary

### Logic

`derive_signal_owner` walks exactly one role-appropriate parent edge; decision items route to the
sprint architect. `_current_occupant` prefers the current document binding, accepts a singular
staged replacement only when no incumbent remains, and refuses ambiguity. Progress checks follow the
task chain rather than spawn ancestry.

### Conventions

The returned `RoutedOwner` carries stable role/document identity with optional current
agent/lifecycle correlations.

### Invariants And Boundaries

- Task containment, never spawn ancestry, defines parent routing.
- Missing or ambiguous occupants are not replaced by a global same-role guess.
- Runtime correlations are delivery evidence, not the route key.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current occupant selection is document-and-role scoped and ambiguity-strict. | `_current_occupant` | mcp/src/agents_remember/controlplane/signal_routing.py:44-81 |
| Owner routing follows structural role and task containment. | `derive_signal_owner` | mcp/src/agents_remember/controlplane/signal_routing.py:165-196 |
| Progress evaluation follows the same task chain. | `task_chain_has_progress` | mcp/src/agents_remember/controlplane/signal_routing.py:228-265 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current control-plane card for `signal_routing.py` with plane-owned seat identity, routing, and enforcement boundaries.
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
