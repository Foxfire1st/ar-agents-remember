# test_context_packet.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_context_packet.py`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Allowed-repository context packet and freshness reporting tests.

## Code Commentary

### Logic

The packet exposes versioned nested repo/memory/worktree/provider facts, publishes provider diagnostics without raw state, and leaves drift unchecked unless requested. Unknown repository IDs refuse before filesystem resolution. A real remote-branch fixture reports code lag and exact ledger mapping.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Unavailable providers do not become fabricated healthy state. The retained tests do not prove every optional packet field or inline-memory variant.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Builds packet from allowed repo. | `test_builds_packet_from_allowed_repo` | mcp/tests/test_context_packet.py:27-63 |
| Rejects unknown repo before filesystem resolution. | `test_rejects_unknown_repo_before_filesystem_resolution` | mcp/tests/test_context_packet.py:65-71 |
| Freshness reports behind code branch and ledger mapping. | `test_freshness_reports_behind_code_branch_and_ledger_mapping` | mcp/tests/test_context_packet.py:73-107 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled the L2 test boundary represented by the changed source. Verified at code commit `1d446724`.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T12:19:51+02:00 — 260731-EFA-L6 S18-B01 curator: reconciled the bounded worker ledger; source-clear citations were repaired, split, rewritten, or deleted as applicable, then the exact scoped fixer/check passed.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:25+02:00 — 260731-EFA-L4 curator: No content impact: the entire diff for this file
  is one fixture literal — the active-worktree `ContractTask` now asks for
  `workflow_kind="light-task"` instead of the bare `"light"`, because 260731-EFA-L4 removed the
  un-reconciled `chat`/`light` members from `WorkflowKind` (they had zero occurrences across the
  213 contracts on disk, no production writer, and were absent from `worktree_start`'s own
  docstring; the equality is now held by
  `test_wire_vocabulary_exhaustiveness.py::AdvertisedVocabularyTests`). This card documents what
  the packet must report — repo, memory, compact provider summary, worktree, drift and freshness
  facts — and has never named a workflow kind, so nothing it claims moved. Verified against the
  source that no test was added, removed or renamed, that the four freshness cases and the
  `taskRoot` `as_posix()` note still describe assertions actually present, and that the three
  Repo-Internal targets still exist.
- 2026-07-31T16:50+02:00 — No content impact: the active-worktree fixture now calls
  `default_contract` with the `ContractTask`, `LeafIdentity`, and `RepoBranchPlan` parameter
  objects instead of fourteen loose keywords, and one `contractPath` assignment was reflowed onto
  a single line by `ruff format`. The card documents what the packet must report — repo, memory,
  compact provider summary, worktree, drift, and freshness facts — and never named the
  contract-construction keywords, so the coverage list is unaffected. Verified against the source
  that no test was added, removed, or renamed and that the `taskRoot` `as_posix()` note and the
  four freshness cases still describe the assertions actually present.
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-10T08:39+02:00: Added four freshness tests (default not-checked, no-upstream fixture, behind + ledger-mapped fixture, unmapped-head ledger) for the issue #54 freshness section.
- 2026-06-08T09:57+02:00: Moved skipped-provider regression coverage to the public `context_packet_payload(...)` path so serialization and wrapper re-validation are exercised.
- 2026-05-29T08:53+02:00: Updated after the `taskRoot` assertion switched from `str(path)` to `path.as_posix()` so it matches the packet's posix paths on Windows hosts.
- 2026-05-28T19:52+02:00: Updated after context packet tests moved to `ContextPacketV2`, rejected duplicate top-level path rules, and rejected embedded provider/worktree raw status.
- 2026-05-28T12:32+02:00: Updated after context packets began exposing provider current-state files and aggregate current state.
- 2026-05-23T18:05+02:00: Created during direct closeout prep for context-packet test coverage.
