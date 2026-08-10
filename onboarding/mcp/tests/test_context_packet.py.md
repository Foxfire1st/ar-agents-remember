# test_context_packet.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_context_packet.py`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_context_packet.py` verifies the package context-packet application entry point and CLI
against configured repository fixtures.

## Code Commentary

### Logic

The tests build temporary code and external-memory repositories, load MCP
settings, and assert that context packets report repo, memory, compact provider
summary, worktree, and drift state. Coverage includes successful
external-memory packets, V2 field placement, provider current-state file path
reporting without embedded raw status, optional drift summaries, unknown repo
rejection before filesystem resolution, non-Git repo error reporting, active
worktree contract reporting without worktree raw status, and CLI JSON output.
Skipped-provider regression coverage goes through `context_packet_payload(...)`
so the test exercises the public MCP payload wrapper's second validation pass,
not just the direct application entry point call.
The `taskRoot` expectation is built with `Path.as_posix()` because the packet
emits posix paths on every host (including Windows, where `str(Path)` would use
backslashes).

Freshness coverage (issue #54): default packets keep
`freshness == {"status": "not-checked"}`; `include_freshness=true` on the
remote-less fixture reports `code.state == "no-upstream"` with no memory block
(fixture memory root is not a git repo) and no `ledgerMapsCodeHead` (no
`memory.md`); a bare-origin + second-clone fixture proves `code.state ==
"behind"` with the behind count and `ledgerMapsCodeHead` true via a
`create_initial_ledger`-written `memory.md` mapping the code HEAD; a ledger
mapping a different commit proves `ledgerMapsCodeHead` false.

### Invariants And Boundaries

The context packet is a read-oriented bootstrap surface. It should report
provider and worktree facts from configured MCP state, but provider raw status
and full worktree manager payloads belong outside `ContextPacketV2`. The V2
contract keeps path rules under `memory.storage.pathRules` and points provider
detail consumers at `provider_diagnostics`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The context packet application entry point builds the tested payload. | `build_context_packet` | mcp/src/agents_remember/application/context_packet.py:59-102 |
| `ContextPacketV2` defines the compact public response contract. | `ContextPacketV2` | mcp/src/agents_remember/models/context_packet.py:114-124 |
| Shared MCP config fixture helpers provide the settings payload and JSON writer used by this suite. | `settings_payload`; `write_json` | mcp/tests/test_config.py:24-26; mcp/tests/test_config.py:29-46 |

## Update History
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
