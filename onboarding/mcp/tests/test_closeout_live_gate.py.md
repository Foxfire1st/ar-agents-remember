# mcp/tests/test_closeout_live_gate.py

## Governing Overview

[governing overview](overview.md)

## Purpose

MIK-R81 rules 2+3 (F09/F13): the closeout gate watches code/memory/source-tip inputs.

## Code Commentary

The suite checks quiet pass retains every queue without recompute; tasks tree digest moves on any write; code edit recomputes only its own sprint; sweep compaction tick touches no task file; stat touch without content change relists but does not recompute; pinned mtime rewrite still recomputes through ctime. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- MIK-R81 rules 2+3 (F09/F13): the closeout gate watches code/memory/source-tip inputs. [1]
