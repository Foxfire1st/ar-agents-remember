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

## Evidence

- Extracted capsule surface suite in unit-regression [835]
- Opt-out refusal suites in unit-regression [836]
- Lane lists with one row per module [837]

- The module the lane names. [838]

- The new module joins this lane. [839]

- The lane catalog with the host module rows. [840]
