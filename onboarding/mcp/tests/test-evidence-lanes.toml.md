# mcp/tests/test-evidence-lanes.toml

## Governing Overview

[tests route overview](overview.md)

## Purpose

The canonical evidence-lane catalog: which test modules belong to which lane, so a leaf's checks can name the population they ran. Membership declares the selected population, never that an invocation ran or passed.

## Code Commentary

The catalog assigns each current test module exactly one evidence lane, one module
path per row, kept sorted within the lane. The extracted capsule serving-surface and
memory-opt-out refusal suites remain in `unit-regression`; those incoming registrations
are not additions authored by this leaf. L112 adds `test_context_packet_cli.py`,
`test_provider_setup_retired.py`, `test_providers_remove.py`, `test_role_single_server.py`
and `test_tool_descriptions.py` to that lane. Earlier line/population totals were
source-snapshot observations, not a current or permanent count. Canonical source
membership is the authority; registration never proves that the tests ran.

The worktree-environment regression module is also in `unit-regression`. Candidate test and
catalog commands use the worktree's own environment as repository tool notes prescribe; the
editable install supplies the candidate source, and test-support imports alone need their
explicit path.

The shared-support settings guard suite is registered in `unit-regression` too.
That suite requires refusal of the account's real settings path and verifies the
recursive support scanner without writing a real account. Its registration is
selection evidence, not an execution or acceptance claim.

The landing, ownership, strict-refusal and dependency-bound suites are selected in `unit-regression`; `test_curator_coherence_closed_out.py` is in `integration`. These catalog memberships select the population and certify no invocation.

## Evidence


- Extracted capsule surface suite in unit-regression [835]



- Opt-out refusal suites in unit-regression [836]




- Lane lists retain one path per module, with the worktree-environment guard registered in unit-regression. [837]



- The module the lane names. [838]



- The new module joins this lane. [839]





- The lane catalog with the host module rows. [840]





- The worktree-environment regression module belongs to unit-regression. [841]





- The guard suite is selected in unit-regression; its cases refuse real-path writes on made-up accounts. [842]


- The guard and recursive scanner cases carry the support-settings contract. [843]
