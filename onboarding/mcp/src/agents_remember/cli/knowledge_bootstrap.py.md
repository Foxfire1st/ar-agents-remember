# mcp/src/agents_remember/cli/knowledge_bootstrap.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

The taskless knowledge-bootstrap CLI admits a named repository and writes a named wave of converted text knowledge through the existing file writer.

## Code Commentary

`run` validates the hand-off list, authorization, configured settings and taskless admission before `_run` selects the converted route. A converted root delegates to `run_wave_write`; an unconverted root refuses as legacy-format or by the cutover lock. The parser accepts no database destination, staging root, status or discard mode. Planned/written, writer refusal and invocation refusal remain distinct outcomes. The old canonical bootstrap progress, staged publication and resume/discard command modes are retired.

### Logic

**Settings resolution is the umbrella CLI's own, with no second convention** (`:183-196`): `--config`
when given, otherwise `discover_config(Path.cwd())`, and a discovery or read failure is returned as a
sentence that names the route (`pass --config with the document the harness registers`) rather than as a
traceback.

### Invariants And Boundaries

- Without `--commit` nothing is written — no batch, no publication, no progress record.
- `--config` reuses the umbrella CLI's trusted discovery; no environment variable is invented.

## Evidence

### Repo-Internal References

- `add_arguments` owns the current boundary described above. [27]
- `run` owns the current boundary described above. [28]
- `_run` owns the current boundary described above. [29]

### Repo-Internal References

- **Settings resolution through the umbrella CLI's own discovery, with no second convention.** [30]
- The one admission this invocation runs under, or the refusal that stopped it. [31]
- The typed refusal payload a refusal is rendered from. [32]
- The `--wave` argument, required only for converted memory. [33]
- **The admission resolver this entry point is the public face of.** [34]
- The wave passes the admitted authority's coordination root, so requirement endpoints resolve (MIK-R13, review F4). [35]
- knowledge-bootstrap refuses unconverted memory once the repository holds converted memory. [36]
