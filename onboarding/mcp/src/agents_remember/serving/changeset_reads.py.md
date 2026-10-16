# mcp/src/agents_remember/serving/changeset_reads.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Wrap existing native Git/content reads with exact-input retention for change-set routes, without adding a diff or endpoint parser.

## Code Commentary

Working changed-file reads bind the repository’s working generation and observe applicable .gitattributes paths before native computation. Selected HEAD/branch reads track their literal reference; counters are retained by the exact measured value tuples.

A failed command is not retained as a reusable result. A missing committed file is retained only after native ls-tree proves absence in a readable tree, not merely because show failed. Working text binds the requested path. Every wrapper computes normally when no app-owned cache read context exists; the common cache, not these helpers, owns bounds and stable-observation admission.

## Evidence

- Working diff counters use the native reader and register attribute inputs. [1]
- A missing text result needs successful native absence proof before retention. [2]
- Only successful fixed native command results are retained. [3]
