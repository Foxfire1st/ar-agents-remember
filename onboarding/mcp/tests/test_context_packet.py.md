# test_context_packet.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_context_packet.py`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T08:39+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_context_packet.py` verifies the package context-packet controller and CLI
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
not just the direct controller call.
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

| Finding | Source Path |
| --- | --- |
| The context packet controller builds the tested payload. | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py) |
| `ContextPacketV2` defines the compact public response contract. | [context_packet.py](agents-remember/mcp/src/agents_remember/models/context_packet.py) |
| MCP config fixtures come from `test_config.py`. | [test_config.py](agents-remember/mcp/tests/test_config.py) |

## Update History

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
