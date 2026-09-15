# mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935`|
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

Prepare code and memory-content outputs after memory certification, without publishing logical refs.

## Code Commentary

### Logic

`PreparedMemoryOutputs` carries the handoff plus exactly code and memory outputs. `_MemoryIntentSelection` supplies the memory parent, admitted tree, existing proof, and write decision. `prepare_memory_outputs` reopens current certification, selects the genuine code output, and either creates memory content or retains the actual existing memory HEAD. No ledger output, mapping lookup, ledger blob comparison, or third preparation leg remains.

For a created memory output, `_intent` renders `normalizedMessage` through the kernel's one `Code-Commit` renderer against the candidate's code commit. The stored message is exactly what private execution uses and finalization publishes; attribution is inside the hashed object. For a no-write output the message and private root are absent, so an unchanged memory HEAD can be reused even when a memory write/message is not enabled.

Existing reuse keeps the historical raw HEAD tree as `admittedTree` and separately carries `existingMemoryProof.certifiedContentTree`. The kernel reproves that only root memory.md separates these trees. Created memory uses the cache-free certified tree directly. Each selected memory intent retains its exact Gate-5 certificate, and previously selected outputs are physically reproved.

Only a real write-enabled output stages the logical memory content. Staging uses `MEMORY_CACHE_EXCLUDE`, removes the cache from the real index, requires the staged tree to equal the certified candidate, and reopens current certification again. These index changes do not advance either logical branch.

### Conventions

Use the named source owners directly. The earlier introduction and verification records remain historical facts; the current uncommitted candidate changes the behavior described here. The existing commit-verification metadata is retained until its owner records a real committed source revision.

### Invariants And Boundaries

The memory-content message uses the single kernel renderer; nothing appends attribution after the selected message or commit object is created. Existing raw HEAD/tree identities must never be relabelled as the cache-free certificate subject. New private memory output must exclude the cache, while unchanged historical memory is reused without a synthetic mapping-only commit.

The inspected production tree still has no caller of `certification/execution.execute_selected_closeout`. The committed producer census checks the renderer call; neither that census nor focused disposable boundary checks establish a public end-to-end certification result. The owning runtime evidence is required for execution, delivery, or acceptance claims.

### Todos

No additional source-local TODO is asserted by this maintenance pass.

## Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain source is configured. | N/A | N/A |

## Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The bundle has code and memory outputs only. | L44-L48 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py) |
| Created memory uses the one renderer; no-write intent has no message or private root. | L59-L122 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py) |
| Memory attribution is appended to the caller's body by one shared renderer. | L67-L92 | [mcp/src/agents_remember/kernel/memory_attribution.py](mcp/src/agents_remember/kernel/memory_attribution.py) |
| Selected output is reobserved, with actual existing HEAD bytes reused for no-write memory. | L159-L198 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py) |
| Output selection binds raw legacy trees separately and stages only certified non-cache content for actual writes. | L201-L236 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py) |
| The stored normalized message becomes the private commit message. | L49-L66 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py) |
| The committed census checks that every listed producer reaches the shared renderer. | L119-L137 | [mcp/tests/test_memory_attribution_producers.py](mcp/tests/test_memory_attribution_producers.py) |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | N/A | N/A |

## Update History

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Retired ledger-output preparation and documented two-output selection, real trailer attribution, raw/certified tree separation, disabled-write no-op reuse, and exact cache-excluding staging. Source SHA-256 `2ee68ae731e22bddf20478e1181247c758e145c097ebf86fa7aca1386711f886`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.

- 2026-09-14T17:20+02:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base
  `7317108b`): `_ledger_tree` now hands the runner one
  `GitRunnerOptions(input_text=content.decode("utf-8"))` object instead of an `input_text=` keyword,
  which is the whole of the change to this module. No content impact: this card stated no `run_git`
  call form, so the attribution claims above are unchanged. The five-line call and the one-line import
  grew the file, so every citation was re-derived against the current source: `_ledger_tree`
  227-244 → 228-248 (its end moved five lines, not one), `prepare_memory_outputs` 246-308 → 251-313,
  `_prepare` 178-225 → 179-225, `_output` 164-176 → 165-176, `_intent` 74-142 → 75-142,
  `PreparedMemoryOutputs` 57-64 → 57-63, and the inline ranges in the Logic paragraph
  (`_intent` `:73-137` → `:75-142`, the per-leg branch `:91-97` → `:92-98`, the renderer call
  `:92-94` → `:93-95`, the ledger leg `:96` → `:97`, `normalizedMessage` `:123` → `:124`, and the
  payload row 106-126 → 107-139, plus `_PRODUCERS` 55-65 → 55-63); verification metadata remains
  closeout-owned.

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
