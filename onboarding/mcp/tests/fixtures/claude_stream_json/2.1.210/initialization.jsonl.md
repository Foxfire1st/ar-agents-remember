# initialization.jsonl

## Governing Overview

[mcp/tests overview](../../../overview.md)

## Purpose

Provides the current Claude 2.1.210 fake-transport startup and model-catalog fixture used by the
ACPUI-L1 capability tests. The version labels reproducible test evidence; it is not a production
compatibility pin.

## Code Commentary

### Logic

The four JSONL frames model the native token-free discovery sequence: correlated control
initialization, `system/init`, a zero-turn and zero-cost bootstrap result, and a correlated
`list_models` response. The catalog includes a reasoning model with its own effort menu, a model
without effort, and an account-disabled model.

### Conventions

Each line is one vendor-shaped frame. Request ids intentionally match the adapter's startup
constants, and the initialize payload intentionally omits the obsolete `models` and `account`
fields because model discovery now has its own control request.

### Invariants And Boundaries

- Discovery evidence remains prompt-free and token-free: the bootstrap result records zero turns
  and zero cost.
- Effort values belong to their advertised model and are not a global enum.
- Disabled models remain catalog evidence but are not selectable.
- The fixture contains no credentials or model-generated response content and does not authorize a
  version gate or fallback behavior.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation entries are configured in the resolved source registry.

No configured live documentation source was available for this pass.

### Repo-Internal References

The Claude adapter suite selects this versioned fixture root explicitly and proves both the
token-free discovery sequence and the normalized catalog projection.

- The fixture loader selects the 2.1.210 directory and parses each JSONL frame. [1]
- Discovery and running advertise consume the initialization and catalog frames without a model turn. [2]
- The dedicated parser validates model identity, model-local effort, disabled state, and current-model selection. [3]

### Cross-Repo References

No meaningful cross-repo references were needed for this fixture.

No meaningful cross-repo references found.
