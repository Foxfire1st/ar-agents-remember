# interactions.jsonl

## Governing Overview

[mcp/tests overview](../../../overview.md)

## Purpose

Provides the Claude 2.1.210 permission and user-question frames used to keep durable interaction
routing covered alongside the ACPUI-L1 startup fixture cohort.

## Code Commentary

### Logic

The first frame requests permission for a Bash tool invocation. The second requests one structured
single-select answer through `AskUserQuestion`; the adapter test replies through the durable
interaction response path and verifies the vendor response shapes.

### Conventions

The request and tool-use ids are stable fixture correlations. Questions preserve Claude's nested
header, option label, description, and `multiSelect` fields without turning fixture text into
application policy.

### Invariants And Boundaries

- Fixture requests never authorize an automatic permission or user-input decision.
- The frames contain no credentials or model-generated answer content.
- Interaction evidence remains separate from model-catalog discovery and from terminal completion.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation entries are configured in the resolved source registry.

No configured live documentation source was available for this pass.

### Repo-Internal References

The Claude adapter suite loads both frames and proves permission and question responses through the
same durable interaction boundary.

- The fixture loader selects the 2.1.210 directory. [1]
- The fixture loader parses each JSONL frame through `_load_fixture`. [2]
- The interaction test consumes both frames and verifies the explicit permission and question responses. [3]

### Cross-Repo References

No meaningful cross-repo references were needed for this fixture.

No meaningful cross-repo references found.
