# mcp/tests/tool_refusal_census_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/tool_refusal_census_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T19:50+02:00 |
| lastVerifiedCommitHash | `7879f5b22c34a912f939e27868786818463c3b9c`|
| lastVerifiedCommitDate | 2026-09-19T20:18:09+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l6-ar` uncommitted source (new file, **253 lines**, sha256 `5ad77371b0025d7a…`); base `a1351504` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The measured population behind L6's refusal conformance check: **one production failure
invocation per public tool**, kept in a support module rather than inside the test module so the
same census is reproducible from a probe as well as from pytest. This is not a test module — it
is imported by `mcp/tests/test_tool_refusal_conformance.py` and contributes no collected case of
its own, which is why it carries no lane row.

**The question it answers for every tool.** L5's `test_tool_entry_point_sweep.py` sweeps the
surface with a *benign* argument set. This table asks the complementary question: driven down a
path that cannot succeed, does the tool answer with a typed refusal naming what refused, why and
the next action — or does it lose the envelope to a bare exception, or answer `ok: true` for an
operation it did not do? `T34` lived in the second answer for nine tools, and `T62`'s preview
crashed on its own producer's output.

## Code Commentary

### Logic

**The table is asserted equal to the roster in both directions, before anything is driven.**
`failure_invocations` (`:54-228`) is keyed by tool name; `drive_census` (`:229-253`) refuses a
table that is not `PUBLIC_TOOLS` (`missing` or `extra`) rather than driving a partial population
and reporting a clean census over it. A new tool cannot arrive uncensused and a stale entry cannot
rot.

**Every entry is the production call a consumer would make** — the same adapter, the same
argument model — not a private function call, so the census measures the entry point's own
behaviour. Where a tool offers `dry_run`, the failure path is reached with it set, so the census
never mutates the world it measures. The addresses it hands out are the fixture's own:
`TASK_REF` (`:35`), `LEAF_REF` (`:36`) and `ABSENT_REF` (`:37`) are real documents inside
`EntryPointWorld` where a tool must first resolve an address to reach a *later* refusal, while
`absent_contract` (`:40-47`) and `outside_contract` (`:48-53`) are the absent and
out-of-confinement contract paths the contract-address family raises on.

**One ordering fact is arranged rather than assumed.** `EntryPointWorld.build` ends the
fixture's lifecycle, so `drive_census` starts one before driving the table: that is what makes
`lifecycle_start`'s own failure path (one is already active) the one measured, and it leaves
`lifecycle_resume` in the unprepared state the pin already records.

**What the caller does with the result.** Each row is `{"kind": ..., "payload": ...}` where
`kind` distinguishes a returned envelope from a raise — the distinction the conformance module
reads as its three-way partition — and `payload` is empty for a raise, because a bare raiser
has no payload at all.

### Conventions

A support module under `mcp/tests/`, imported by path name from the test module beside it; no
`test_` prefix, no collected cases, **no lane row** in `mcp/tests/test-evidence-lanes.toml`
(the manifest registers test modules, and this is not one). The constants at the top
(`REPO` `:27`, `ADOPT_REPO` `:28`, `MASTER` `:29`, `LEAF_ID` `:30`, `WORKTREE_NAME` `:31`) name
the fixture's entities once so the 67 invocations cannot spell them differently.

### Invariants And Boundaries

- **It owns no assertion about correctness.** The table says which call to make; whether the
  answer is acceptable is the conformance module's partition, and the pins live there.
- **It is not execution evidence.** Driving `EntryPointWorld` is a hermetic, disposable-world
  check; nothing here certifies a tool.
- **The roster is the only population source.** There is no literal count anywhere in this
  module: the completeness check is a set comparison against `PUBLIC_TOOLS`, which is what makes
  the census shrink-proof.

## Docs References

No external Domain Documentation source is configured in this memory root. These are
repository-owned fixture facts; no external library behaviour is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The anchors below identify current behaviour of this module; they are not execution evidence and
they make no acceptance claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| The 67 production failure invocations, one per advertised tool. | `failure_invocations` | mcp/tests/tool_refusal_census_support.py:54-228 |
| The driver: roster equality first, then one drive per tool, with the lifecycle arranged so `lifecycle_start`'s own failure path is measured. | `drive_census` | mcp/tests/tool_refusal_census_support.py:229-253 |
| An absent contract path inside the coordination root, for the contract-address family. | `absent_contract` | mcp/tests/tool_refusal_census_support.py:40-47 |
| A contract-shaped path outside the coordination root, for the confinement refusals. | `outside_contract` | mcp/tests/tool_refusal_census_support.py:48-53 |
| The fixture document addresses a tool must resolve to reach a later refusal. | `TASK_REF`; `LEAF_REF`; `ABSENT_REF` | mcp/tests/tool_refusal_census_support.py:35-35; mcp/tests/tool_refusal_census_support.py:36-36; mcp/tests/tool_refusal_census_support.py:37-37 |
| The advertised roster the table is asserted equal to before anything is driven. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-91 |
| The hermetic world every invocation addresses, shared with the benign sweep. | `EntryPointWorld` | mcp/tests/test_tool_entry_point_sweep.py:325-866 |
| The conformance check that drives this census and asserts the three-shape partition. | `FailurePathCensusTests` | mcp/tests/test_tool_refusal_conformance.py:191-282 |

## Cross-Repo References

No cross-repository implementation evidence is required for this fixture. Every address it hands
out is inside the disposable world the calling test module builds.

| Finding | Anchor | Source |
| --- | --- | --- |
| No repository or external-system boundary is proved by this module. | N/A | N/A |

## Update History

- 2026-09-19T19:50+02:00 — 260918-TSIP-L6 curator (uncommitted change set on `ar/260918-tsip-l6-ar`, base `a1351504`): **created**. The module is new in this leaf (**253 lines**, sha256 `5ad77371b0025d7a…`) and holds the leaf's measured refusal population — one production failure invocation per public tool, asserted equal to `PUBLIC_TOOLS` in both directions before anything is driven, with the fixture addresses and the lifecycle ordering that make `lifecycle_start`'s own failure path the one measured. Recorded that it is a support module with no collected case and therefore no lane row, and that it owns no assertion about correctness: the three-shape partition and both pins belong to `mcp/tests/test_tool_refusal_conformance.py`. Verification metadata is the recorded base commit; the candidate is uncommitted and the governed closeout stamps the real code commit.
