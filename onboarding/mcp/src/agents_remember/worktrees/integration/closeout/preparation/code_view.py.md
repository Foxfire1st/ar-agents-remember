# mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634`|
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

Physical code execution views for selected preparation, bound to the canonical logical memory pair.

## Code Commentary

### Logic

Observation requires an already selected original output, reloads typed stored objects, rechecks raw commit and physical Git facts, and binds the canonical logical pair to the actual read root. `prepare_code_view` performs preparation first; `observe_prepared_code_view` only reopens the existing view. Neither fabricates historical memory attribution for an in-flight pair.

`observe_selected_prepared_code_view` can reprove a journal-selected output after the running worker has returned. It validates the selected record and uses the same kernel observers instead of claiming a live worker lease. Existing code is checked with a strict `ExistingGitPreparationBinding`; created code uses the named private capability and a callback that reopens the original record and policy. Both paths remain code-domain checks, even if a file happens to be called memory.md.

### Conventions

Use the named source owners directly. This source was introduced in landed commit `245057ab16e19afdaabd5c188c9576b22e0c0870`. The earlier introduction and verification records remain historical facts; the current uncommitted candidate changes the behavior described here. The existing commit-verification metadata is retained until its owner records a real committed source revision.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

Physical code execution root and logical code/memory pair identity are separate facts. The memory cache option cannot relax this code view, and a constructed view is not a replacement for its selected raw output or owning journal.

### Todos

No additional source-local TODO is asserted by this maintenance pass.

## Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is configured. | N/A | N/A |

## Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

| Finding | Anchor | Source |
| --- | --- | --- |
| The running-owner observation reloads the selected output and builds a bound physical view. | n/a | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py) |
| The selected-record path reuses strict existing-code or sealed private-code proof without inventing a worker lease. | n/a | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py) |
| Selected record and intent currentness are rechecked around observation. | n/a | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py) |
| The execution view binds the exact output bytes, raw commit/tree, and logical pair. | n/a | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py) |
| Preparation precedes a fresh observation when the caller requests a prepared view. | n/a | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py) |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | N/A | N/A |

## Update History

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Documented strict existing-code bindings in both live-worker and selected-record views, preserving the physical-root/logical-pair distinction. Source SHA-256 `afc00f38d2cee203d28a9a2bdc35d61a641d5b73ea818f66c3d4d6f2ba811705`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py` changed since
  the recorded verification commit. Re-read the card against the frozen on-disk source and
  re-checked its claims and cited ranges: nothing this card asserts is falsified by the change, so
  no wording changed. Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (a pure, net-zero import relocation of the memory candidate-pair
  resolver). Re-read the card: no claim names the moved module and the cited range is exact. No
  wording changed; verification metadata remains closeout-owned.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `prepare_code_view` repointed to mcp/src/agents_remember/worktrees/integration/closeout/preparation/code_view.py:221-226. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
