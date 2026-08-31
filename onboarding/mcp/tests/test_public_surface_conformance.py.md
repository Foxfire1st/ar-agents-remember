# mcp/tests/test_public_surface_conformance.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/tests/test_public_surface_conformance.py`          |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-08-30T22:33:39+02:00                               |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`              |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

This is ARSPAWN-L4's executable acceptance for public dispatch advertisement, strict wire input,
shared candidate identity, and the repository's eight production MCP starter registrations.

## Code Commentary

### Two deliberately separate launch proofs

The production-starter proof parses the committed Claude, Codex, Cursor, VS Code, Hermes, OpenClaw,
Pi, and Antigravity registrations. Every one must launch `uvx` with exactly one
`--refresh-package agents-remember-mcp` and `agents-remember-mcp@latest`. This preserves the starter
promise that users do not have to remember to refresh their MCP package manually.
The Codex registration must additionally forward `AR_HOSTED_SESSION_ID` and `AR_SPAWN_ROLE`, which
preserves ambient versus hosted process identity across its MCP subprocess boundary.

The disposable candidate proof must answer a different question: whether the exact code under
review advertises the required live surface. Launching `@latest` there would certify the last
published package and could conceal the stale-install defect. It therefore starts a clean stdio MCP
process with the current test interpreter and source, while retaining each starter-derived settings
path and hosted-process environment. `server_info` must report the expected source digest, package
root, interpreter, and boot identity; live tools and dispatch schema must agree with that identity.

### Additional forcing cases

- Live ordered registration and response-model parity pass through `validate_public_surface`.
- Every inventory authority and malformed schema family has an explicit negative case; error
  branches cannot satisfy CRAP/diff coverage through only the happy path.
- The consumer-scoped validator rejects both a renamed dispatch tool and a non-object schema before
  delegating to the shared schema contract.
- An undeclared spend override and an invalid role are rejected before the handler runs.
- Ambient unknown-task resolution returns the typed public refusal.
- Success, queued, unknown-task, role-altitude, and persistence-refusal outcomes round-trip through
  the strict `DispatchAgentResponse` envelope without leaking private session identity.
- The test is explicitly classified as integration evidence and uses bounded 30-second protocol
  operations.

### Invariants And Boundaries

- Never replace the production self-update assertion with a local-source launch.
- Never replace the exact-candidate launch with `@latest`; those proofs cover different risks.
- The test uses the public stdio/list/call boundary, not FastMCP private state.
- Starter parsing must fail on malformed or missing entries rather than guess a filename or shape.
- Codex starter validation requires the exact two lifecycle environment variables; forwarding an
  incomplete or broader guessed set is not accepted.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| All production starters retain automatic package refresh. | `test_all_eight_production_starters_keep_self_updating` | mcp/tests/test_public_surface_conformance.py:506-529 |
| Each controlled harness certifies the exact candidate over stdio. | `_inspect_exact_candidate`; `test_each_controlled_harness_launches_the_exact_candidate_over_stdio` | mcp/tests/test_public_surface_conformance.py:170-226; mcp/tests/test_public_surface_conformance.py:531-555 |
| Strict input and ambient output behavior enter through the registered tool. | `PublicDispatchContractTests` | mcp/tests/test_public_surface_conformance.py:226-330 |
| All fail-closed inventory, schema, description, and ordering clauses have negative forcing cases. | `PublicSurfaceFailureTests` | mcp/tests/test_public_surface_conformance.py:337-503 |

## Update History

- 2026-08-31T13:42+02:00 — A005 closeout repair covered the consumer validator's wrong-name and
  non-object-schema branches without adding a second schema implementation.

- 2026-08-30T22:33:39+02:00 — 260821-ARSPAWN-L5 recorded exact Codex lifecycle-identity
  forwarding while preserving the self-updating starter contract.

- 2026-08-30T17:08:05+02:00 — ARSPAWN-L4 Dagger repair: added explicit forcing cases for every
  public-surface refusal family and live-order drift. Verification remains closeout-owned.

- 2026-08-30T15:15:36+02:00 — 260821-ARSPAWN-L4: created the eight-harness, exact-candidate, and
  public-surface acceptance suite. Final verification provenance remains closeout-owned.
