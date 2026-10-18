# mcp/tests/test_memory_quality_is_independent_of_the_closeout_plane.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Keep the pure memory-quality service independent of the closeout plane.

## Code Commentary

The AST scan walks every Python file below the imported memory_quality package and names imports beginning with the closeout, integration-lifecycle or operation-model prefixes. It inspects absolute ImportFrom.module and Import names; relative-import resolution, dynamic imports and arbitrary runtime dependency paths are outside this scanner. The separate API case checks module-level imports are non-None; it does not physically remove closeout modules or prove a sandboxed import. Neither source inspection nor stored assertions establish a fresh run.

## Evidence

- The forbidden set contains closeout, integration-lifecycle and operation-model import prefixes. [1]
- The scanner records absolute ImportFrom.module and Import names from each Python AST. [2]
- Every scanned memory_quality Python file must have no imports starting with the forbidden prefixes; offenders are named. [3]
- The imported quality API and module are non-None; this is not physical closeout removal or dynamic dependency proof. [4]
