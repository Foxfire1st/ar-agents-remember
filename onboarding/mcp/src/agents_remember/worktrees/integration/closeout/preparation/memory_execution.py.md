# mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935`|
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

Observe a cache-free prepared memory candidate and reopen its selected certification result.

## Code Commentary

### Logic

The candidate derives from the current handoff, fresh physical code view, and an isolated memory candidate tree that explicitly excludes root `memory.md`. Candidate observation is repeated around the physical code-view checks.

Certification requires the registered prepared-memory port and a current handoff. Cache setup runs only when non-cache memory content has actual changes. Clean legacy memory, including a historical HEAD that tracked the cache, therefore acquires neither a new ignore file nor a cache-removal staging delta merely to certify an unchanged content view.

`current_prepared_memory_result` reopens the exact owner, all five selected terminals, result/certificate references, cache-free memory tree, and pair authority. A returned dictionary or previous observation does not supply current authority.

### Conventions

Use the named source owners directly. This source was introduced in landed commit `245057ab16e19afdaabd5c188c9576b22e0c0870`. The earlier introduction and verification records remain historical facts; the current uncommitted candidate changes the behavior described here. The existing commit-verification metadata is retained until its owner records a real committed source revision.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

The certified memory-content tree can differ from an existing historical HEAD tree only by the separately proved cache projection. This observer does not rewrite HEAD or issue a new commit to make the identities look equal. Missing producer or mismatched selected evidence remains a typed refusal.

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
| Candidate construction explicitly excludes memory.md and reobserves the selected code view. | L27-L52 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_execution.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_execution.py) |
| Cache setup is conditional on real non-cache changes before invoking the registered producer. | L55-L79 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_execution.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_execution.py) |
| The selected fifth terminal must bind the actual cache-free tree and logical pair. | L82-L127 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_execution.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_execution.py) |
| The memory reuse record carries distinct raw and certified tree identities. | L43-L69 | [mcp/src/agents_remember/models/lifecycles/preparation.py](mcp/src/agents_remember/models/lifecycles/preparation.py) |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | N/A | N/A |

## Update History

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Recorded cache-free candidate certification, conditional cache setup, and clean legacy no-op behavior while preserving exact selected-certificate checks. Source SHA-256 `1bb554607478692dc36526283758208a90677ac1a1997e8a35f563fffc4dd8eb`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
