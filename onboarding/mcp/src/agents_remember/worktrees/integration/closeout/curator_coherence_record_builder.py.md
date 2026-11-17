# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_record_builder.py

## Governing Overview

[Closeout](overview.md)

## Purpose

Constructs the immutable curator-coherence record and its Markdown projection from an observed candidate.

## Code Commentary

The builder combines the observed candidate and complete quality evidence with the shared measured dependency binding, caller, requirement revision, delivery attempt and publication inputs. It validates the resulting typed record and renders its deterministic projection.

Construction writes no files and does not move the authoritative pointer. Publication checks the stored generation before replacing that pointer.

## Relationships

The publication module owns persistence and pointer replacement; the binding module owns shared dependency construction; the renderer owns the readable projection.

## Evidence

- Record construction uses the observed candidate, quality evidence and publication inputs. [1]
