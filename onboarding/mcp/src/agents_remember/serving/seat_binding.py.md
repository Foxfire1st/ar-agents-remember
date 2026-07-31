# mcp/src/agents_remember/serving/seat_binding.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/serving/seat_binding.py`            |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-07-10T15:07+02:00                                       |
| lastVerifiedCommitHash |                                                              `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |                                                              2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[serving overview](overview.md)

## Purpose

`seat_binding.py` is the shared vocabulary and normalization boundary for a hosted session's
current leaf-seat identity. It keeps orchestration binding state separate from immutable launch
provenance so worker, reviewer, curator, manager, architect, and terminal seats can coexist on one
canonical leaf while a live same-role owner still has exclusive claim to its pair.

## Code Commentary

### Logic

`migrated_seat_role` gives terminal rows the fixed `terminal` role and migrates harness rows from
persisted `seatRole`, then `spawnRole`, then legacy `chat`. `attach_seat_role` uses an explicit
operator choice first, otherwise spawn provenance or a previously typed non-chat binding; an
untyped hand-opened harness returns `None` so the attach surface emits `role-required` instead of
inventing an occupant. `role_suffixed_leaf_base` recognizes old `leaf-role`, `leaf/role`, and
`leaf:role` workarounds only after normal leaf resolution fails, allowing callers to reject them
with canonical-leaf-plus-role guidance.

### Conventions

Role strings remain open rather than a closed Python `Literal` because the attach UI also permits
future/custom seat names. The tuple lists the maintained pipeline roles used only for detecting
legacy suffix hacks.

### Invariants And Boundaries

- `spawnRole` records where the session came from; `seatRole` records who currently occupies the
  binding. Reattaching may change only the latter.
- Plain terminals always occupy `terminal`; callers cannot relabel a shell as an orchestration
  seat.
- A hand-opened harness without explicit or previously declared identity is never silently
  assigned `chat` during attach.
- This module normalizes roles only. Catalog persistence, live-owner arbitration, and HTTP/MCP
  refusal payloads stay in their owning modules.

### Todos

Reviewer O2 records the deliberate local single-operator trust model: attach-with-role is the
role-claim authority. If the product becomes multi-user, authentication/authorization belongs at
the public attach boundary rather than as validation inside this pure helper.

## Docs References

No external domain sources are configured for this repository; the current seat-binding contract
is defined by same-repository source and tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document is configured for this local runtime contract. | — | — |

## Repo-Internal References

The catalog persists the normalized role, assignment performs live pair arbitration, and the tests
pin migration, role-required attach, coexistence, and suffix refusal.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Catalog rows expose `binding_role` and atomically move `leaf_key` plus `seat_role`. | L44-L84; L478-L497; L534-L552 | [terminal_catalog.py](terminal_catalog.py) |
| Attach resolves the requested role, refuses an untyped harness, liveness-checks the same-pair owner, and persists one pair move. | L32-L50; L53-L114 | [terminal_leaf_assignment.py](terminal_leaf_assignment.py) |
| Pair migration and attach behavior are covered at the catalog/assignment seams. | `TerminalCatalogTests`; `TerminalLeafAssignmentTests` | [test_terminal_catalog.py](../../../tests/test_terminal_catalog.py); [test_terminal_leaf_assignment.py](../../../tests/test_terminal_leaf_assignment.py) |

## Cross-Repo References

No meaningful cross-repo references found; seat binding is local runtime state.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No sibling repository owns this catalog identity. | — | — |

## Update History

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/serving/seat_binding.py` since the L2 base commit is the whole-tree
  `ruff format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change whatsoever.
  Checked by parsing both revisions and comparing the abstract syntax trees (identical) and the
  comment tokens (identical), so no symbol, signature, default, decorator, control-flow branch,
  docstring, or assertion this card describes has moved, and every claim this card makes about its
  own source still holds.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: created for the shared `(leafKey, seatRole)`
  normalization contract, explicit hand-opened role claim, legacy-row migration, and rejection of
  role-suffixed leaf workarounds. Verification metadata remains blank until closeout stamps the
  eventual L17 code commit.
