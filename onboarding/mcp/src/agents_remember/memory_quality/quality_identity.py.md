# mcp/src/agents_remember/memory_quality/quality_identity.py

## Governing Overview

[Memory quality](overview.md)

## Purpose

Computes the part of a quality result that coherence uses for freshness.

## Code Commentary

The measured report excludes the top-level `knowledgeReview` section and resumes at the next level-two heading. Every other report byte remains significant. The measured attestation excludes its full report hash and dependency envelope; it keeps the measured report hash and all other attestation fields.

These projections let a published assessment appear in the next report without changing its own measured result. They do not replace the integrity checks of the complete report and attestation.

## Relationships

The checklist publisher writes the measured report hash. The shared coherence binding computes the corresponding attestation identity; the coherence reader checks the complete live files separately.

## Evidence

- Only the assessment-list section is omitted from the measured report. [1]
- The measured attestation retains all fields except the full report hash and dependencies. [2]
