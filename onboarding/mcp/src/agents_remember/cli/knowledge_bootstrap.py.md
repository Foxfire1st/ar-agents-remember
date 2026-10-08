# mcp/src/agents_remember/cli/knowledge_bootstrap.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

The taskless knowledge-bootstrap CLI admits a named repository and writes a named wave of converted text knowledge through the existing file writer.

## Code Commentary

`run` validates the hand-off list, authorization, configured settings and taskless admission before `_run` selects the converted route. A converted root delegates to `run_wave_write`; an unconverted root refuses as legacy-format or by the cutover lock. The parser accepts no database destination, staging root, status or discard mode. Planned/written, writer refusal and invocation refusal remain distinct outcomes. The old canonical bootstrap progress, staged publication and resume/discard command modes are retired.

## Evidence

### Repo-Internal References

- `add_arguments` owns the current boundary described above. [27]
- `run` owns the current boundary described above. [28]
- `_run` owns the current boundary described above. [29]
