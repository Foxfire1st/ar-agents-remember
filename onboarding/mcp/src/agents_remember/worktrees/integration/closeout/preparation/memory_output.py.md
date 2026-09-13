# mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T23:52+02:00 |
| lastVerifiedCommitHash | `52875e7a8695fc7b67bff21ebb07a67268213967`|
| lastVerifiedCommitDate | 2026-09-14T00:06:58+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

Ordered post-certification private M and L preparation.

## Code Commentary

### Logic

`_MemoryIntentSelection` carries a typed memory-content or ledger leg, parent, tree, existing proof and write-enabled decision into `_intent`. The private output observer is an explicit module dependency. Ordered M/L preparation, exact existing-proof reuse and disabled-write refusals remain unchanged.

prepare_memory_outputs reopens current prepared-memory certification, selects the genuine code output and either creates M or retains a proved existing M. It reads the exact ledger blob, retains a matching existing C-to-M mapping or builds the required new ledger tree in an isolated index, then prepares/selects L. Every selected memory intent carries the exact Gate-5 certificate and enabled-leg policy. Previously selected outputs are physically re-proved. Both logical branches remain untouched by this owner.

**The memory-content leg is attributed, and the ledger leg is not.** `_intent` (`:73-137`) renders
`normalizedMessage` through one branch per leg (`:91-97`): the memory-content leg calls
`kernel.memory_attribution.render_memory_content_message(effective.message_for("memory"),
result.candidate.codeView.codeCommit)` (`:92-94`) — the kernel's one writer of the `Code-Commit:`
trailer, so this route names the code commit its candidate was certified on without owning a second
renderer — while the ledger leg keeps the plain `effective.message_for("ledger")` (`:96`) and names no
code commit. The message is stored under `normalizedMessage` (`:123`) and is consumed by
`private_execution.py:61` as the private commit's message, which is why the attribution is rendered at
intent construction rather than appended later: `finalization.py` publishes that exact prepared object to
the live memory ref, so the trailer is inside the object the ref receives and cannot be added afterwards
without rewriting it.

### Conventions

Use the named source owners directly. The implementation is present in landed IAS; this preparation pass does not advance verification stamps.

### Invariants And Boundaries

The memory-content intent's message carries exactly one `Code-Commit: <sha>` trailer, naming the code
commit the candidate was certified on, and it is rendered by the kernel's single renderer rather than by
a route-local format. The ledger intent is deliberately trailerless: the `memory.md`-only commit names
no code commit, and a second trailered commit for one code commit would project a duplicate row in the
attribution-derived ledger. Nothing is appended to a message after it is stored — `normalizedMessage` is
the message the private commit is created with, and finalization publishes that object.

The route has **no behavioural case of its own**: its production entry point
(`certification/execution.execute_selected_closeout`) has no caller, so nothing can be published through
it to observe. What protects the attribution here is the source census case in
`mcp/tests/test_memory_attribution_producers.py`, which asserts this module's renderer call by name; that
is the residual gap stated on the kernel card rather than hidden.

The documented types and paths do not themselves establish execution, certification, delivery or
acceptance. Those claims require the corresponding owning runtime evidence.

### Todos

No source-local TODO is asserted here.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `PreparedMemoryOutputs` owns the corresponding behavior described above. | `PreparedMemoryOutputs` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py:57-64` |
| `_intent` owns the corresponding behavior described above, and it is where the per-leg message is chosen. | `_intent` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py:74-142` |
| The memory-content leg renders its message through the kernel's one writer, against the candidate's certified code commit; the ledger leg keeps the plain message and carries no trailer. | `render_memory_content_message`; `message_for` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py:91-97`; `mcp/src/agents_remember/kernel/memory_attribution.py:72-97` |
| The rendered message is what the private commit is created with, and finalization publishes that exact object to the live memory ref. | `normalizedMessage` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py:106-126`; `mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py:51-61` |
| `_output` owns the corresponding behavior described above. | `_output` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py:164-176` |
| `_prepare` owns the corresponding behavior described above. | `_prepare` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py:178-225` |
| `_ledger_tree` owns the corresponding behavior described above. | `_ledger_tree` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py:227-244` |
| `prepare_memory_outputs` owns the corresponding behavior described above. | `prepare_memory_outputs` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py:246-308` |
| The census case that is this route's only attribution protection, because the route has no reachable public entry point. | `test_every_census_producer_reaches_the_shared_renderer`; `_PRODUCERS` | mcp/tests/test_memory_attribution_producers.py:119-137; mcp/tests/test_memory_attribution_producers.py:55-65 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed for this card. | N/A | N/A |

## Update History

- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`,
  base `5bb124d4`): this module is the producer the master's 2026-09-13T22:05 census missed and the
  2026-09-13T23:50 decision added. `_intent` now chooses the normalized message per leg (`:91-97`): the
  memory-content leg renders through `kernel.memory_attribution.render_memory_content_message` against
  `result.candidate.codeView.codeCommit`, while the ledger leg keeps the plain `message_for("ledger")`,
  and `:123` stores the result under `normalizedMessage`, which `private_execution.py:61` commits and
  `finalization.py` publishes to the live memory ref — so the trailer is inside the object the ref
  receives. Added the Logic paragraph, the attribution invariants (including the deliberate absence of a
  behavioural case for this route and the census case that covers it instead) and the renderer/message
  reference rows, and rebound every stale symbol range in the table to the grown file
  (`_intent` 73-129 → 74-142, `_output` 152-163 → 164-176, `_prepare` 166-212 → 178-225,
  `_ledger_tree` 215-231 → 227-244, `prepare_memory_outputs` 234-296 → 246-308). Verification metadata
  remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-09-06T21:46:58+00:00 — Reconciled landed IAS helper ownership and source anchors. Verification pins and historical evidence remain unchanged; no certification or delivery is asserted.

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
