# mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935`|
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

At-most-once journal-bound private Git execution for code and memory-content outputs.

## Code Commentary

### Logic

Each enabled code or memory-content output has the ordered create, materialize, and commit commands. These are command steps for one output, not three commit legs. There is no private ledger-output command in the current preparation model.

Each command start is selected before its single kernel call; actual exit/output hashes or unknown outcome are retained afterward. Live ownership and effective policy are reopened at action boundaries. Successful steps are not rerun, unresolved preparation is retained, and a named committed output is physically reobserved instead of discovering another commit. Shared execution does not advance logical branches.

### Conventions

Use the named source owners directly. This source was introduced in landed commit `245057ab16e19afdaabd5c188c9576b22e0c0870`. The earlier introduction and verification records remain historical facts; the current uncommitted candidate changes the behavior described here. The existing commit-verification metadata is retained until its owner records a real committed source revision.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

Private output proof stays strict over the complete admitted tree. The logical-memory cache projection belongs to existing-memory observation and finalization, not to this private checkout capability. A failed or unknown original commit may be inspected for its named output, but never rerun speculatively.

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
| The selected leg must still match the retained intent. | L37-L46 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py) |
| The private binding retains the exact selected parent, admitted tree, message, and owner. | L49-L66 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py) |
| The capability reopens selection and actual private policy around commands. | L69-L92 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py) |
| Original commands are selected and their observed terminals retained once. | L118-L183 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py) |
| Output observation proves the named committed object and current policy. | L186-L200 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py) |
| Only an unstarted suffix runs; uncertain prior commands are retained for named-output recovery. | L203-L237 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py) |
| The selected intent supports only code and memory-content output legs. | L26-L26 | [mcp/src/agents_remember/models/lifecycles/preparation.py](mcp/src/agents_remember/models/lifecycles/preparation.py) |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | N/A | N/A |

## Update History

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Clarified the two supported output legs while preserving the executor's create/materialize/commit ordering, strict private proof, and no-rerun behavior. Source SHA-256 `1a789fe8836353b0fdf58dfac8cde1c1cef5b7266664a6194c7801918bb82798`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
