# mcp/src/agents_remember/kernel/primitives/version.py

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/version.py` is the installed package identity (moved from the `mcp` package
root by 260731-EFA-L9). Every layer above kernel may name the server/version without importing
the `mcp` package.

## Code Commentary

### Logic

Defines `SERVER_NAME = "agents-remember"` (cit:([`SERVER_NAME`], mcp/src/agents_remember/kernel/primitives/version.py:11-11)).
`_resolve_server_version` reads the installed `agents-remember-mcp` distribution metadata and
returns the committed `3.0.0rc8` identity only when that metadata is unavailable in a source
checkout. `SERVER_VERSION` is computed through that function seam, which keeps reload-based
fallback tests deterministic and gives every upper layer one kernel-owned value.

### Invariants And Boundaries

- Kernel stays importable by every layer; version identity must not drag `mcp` into kernel.
- Installed package metadata is authoritative; the literal fallback is only the matching source-release identity.

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- Package metadata and source-checkout fallback are selected through the explicit resolver. [1]
- Installed metadata is authoritative; only missing package metadata selects the explicit source-checkout release identity. [2]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
