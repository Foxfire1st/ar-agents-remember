# PDLS Verification-Ownership Governing Route Map

| Source route | Governing onboarding | Action |
| --- | --- | --- |
| repository root | `onboarding/overview.md` | refresh repository-wide Dagger/evidence boundary |
| `mcp` | `onboarding/mcp/overview.md` | refresh product-versus-verification package topology |
| `mcp/src/agents_remember` | existing nearest route-local overviews | preserve operational product ownership and affected lifecycle contracts |
| `mcp/test_support/agents_remember_test_support` | `onboarding/mcp/test_support/agents_remember_test_support/overview.md` | govern the dedicated Python verification root |
| `mcp/test_support/agents_remember_test_support/code_quality` | `onboarding/mcp/test_support/agents_remember_test_support/code_quality/overview.md` | govern quality planning/execution, ownership, retry, coverage, and causal continuation |
| `mcp/test_support/agents_remember_test_support/testing` | `onboarding/mcp/test_support/agents_remember_test_support/testing/overview.md` | govern admission, lanes, lifecycle, provenance, cadence, retry selection, and route measurement |
| `mcp/tests` | `onboarding/mcp/tests/overview.md` | govern focused forcing and shared test support |
| `scripts` | `onboarding/overview.md` | govern repository verification entry points |
| canonical lifecycle/task skills | existing `onboarding/skills/.../overview.md` routes | preserve canonical requirement and attempt-journal doctrine |
| packaged skill projections | `onboarding/mcp/overview.md` plus exact file sidecars | describe synchronized copies without duplicating canonical authority |
| `dashboard/src` | `onboarding/dashboard/src/overview.md` | preserve consumer-only projection contracts |

## Placement Decision

Verification infrastructure has an independent import and ownership boundary, so
`mcp/test_support/agents_remember_test_support` and its `code_quality` and `testing` children each
earn a route-local pillar. Ordinary forcing tests stay under the existing `mcp/tests` pillar.
Repository scripts retain the root overview because one changed synchronization entry point does
not create a new semantic subsystem.

## Moved Or Deleted Routes

The verification-only `code_quality`, `testing`, and certifying-bootstrap owners moved out of the
product package and retained their histories at the new paths. Candidate A and the deleted Claude
2.1.207 fixture slice were removed. No old-path compatibility sidecar, route overview, facade, or
fallback remains.
