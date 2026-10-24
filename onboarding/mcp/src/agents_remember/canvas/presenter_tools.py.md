# mcp/src/agents_remember/canvas/presenter_tools.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The shared guarded authoring implementation for a prepared input folder and an output folder: immutable input digests, descriptor-anchored output paths, a separate read-only documentation surface, and a model-free draft render. The normal bound task server exposes these operations to an explainer; this module starts no standalone server.

## Code Commentary

- `AuthoringTools` admits either the retained presenter’s `host/` grants or the explainer’s supplied `instructions/` grants and `drafts/` output folder. A non-object manifest or a grant naming another prepared folder is refused; the input digest and descriptor-anchored asset guards remain the implementation boundary.
- `DOCUMENTATION_HOSTS` bounds where authoring documentation may be read from, and that surface is separate from the review's evidence.

## Evidence


- The shared authoring implementation admits the prepared folder and its exact input grants. [1]

- The documentation surface is a bounded, separate read. [2]

- AuthoringTools admits the prepared input grants and output folder; the standalone presenter server constructor and CLI entry are removed. [3]
