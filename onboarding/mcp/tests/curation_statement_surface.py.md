# mcp/tests/curation_statement_surface.py

## Governing Overview

[overview](overview.md)

## Purpose

Names the three facts a guard-tooth case needs about a retired curation sentence: the sentence fragment 1 shipped, the surface it shipped on, and a surface that never carried it.

## Code Commentary

`DECLARED_SURFACE` is `l-01-agent-lifecycles/templates/curator-brief.md`, the template the registry records for fragment 1. `UNDECLARED_SURFACE` is the lifecycle criterion `l-01-agent-lifecycles/criteria/code-seam.md`, which never carried the sentence. `fragment_one_surfaces` selects the registry row in `RETIRED_CURATION_STATEMENTS` whose reason starts with `fragment 1:` and whose sources are exactly that one skill path, and returns the statement with both surface names. The registry is the authority; this module only picks one row.

## Invariants And Boundaries

The guard these cases feed is a census of surfaces, not a single-file check. The undeclared surface is a surviving lifecycle criterion that never carried the sentence, while the declared surface keeps the exact registered fragment and its source scope. A row that does not match the selection raises from `next` rather than answering a default.

## Evidence

### Repo-Internal References

- The declared and undeclared surfaces are named here once, and the sentence comes from the retired-statement registry. [1]
