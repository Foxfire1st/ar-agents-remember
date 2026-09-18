# mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675`|
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is configured. | N/A | N/A |

## Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

| Finding | Anchor | Source |
| --- | --- | --- |
| The selected leg must still match the retained intent. | `_selected_leg` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py:37-46 |
| The private binding retains the exact selected parent, admitted tree, message, and owner. | `private_git_binding` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py:49-66 |
| The capability reopens selection and actual private policy around commands. | `_capability` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py:69-92 |
| Original commands are selected and their observed terminals retained once. | `_terminal_record` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py:95-115 |
| Output observation proves the named committed object and current policy. | `observe_private_output` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py:186-200 |
| Only an unstarted suffix runs; uncertain prior commands are retained for named-output recovery. | `prepare_private_output` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py:203-237 |
| The selected intent supports only code and memory-content output legs. | `require_prepared_output_matches_intent` | mcp/src/agents_remember/models/lifecycles/preparation.py:380-414 |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | N/A | N/A |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Clarified the two supported output legs while preserving the executor's create/materialize/commit ordering, strict private proof, and no-rerun behavior. Source SHA-256 `1a789fe8836353b0fdf58dfac8cde1c1cef5b7266664a6194c7801918bb82798`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
