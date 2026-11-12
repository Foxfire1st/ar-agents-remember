# mcp/src/agents_remember/certification/certification_lane.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Derives the canonical R11 authority for a run from its admitted R22 Gates 1–4 plan and caller-supplied Gate-5 memory rails, then freezes the R21 admission manifest.

## Code Commentary

### Logic

compile_certification_lane requires applicable repository gates and a nonempty memory-domain Gate-5 contribution. It projects each admitted compiled rail into RailDefinition without inventing adapter, runtime, artifact or evidence fields, creates one certifying five-gate registry profile, canonicalizes it, compiles the certification plan and creates the admission manifest.

CertificationLane carries registry, certification plan, repository plan and admission together. admit_certification_lane recompiles from the current profile and memory contribution and compares the resulting lane with the supplied lane; movement raises a typed certification-lane-mismatch. Registry identity may be supplied explicitly or derived from the repository id.

### Conventions

Semantic digests exclude creation provenance. The projection preserves repository rail contracts instead of translating them into an unrelated registry vocabulary.

### Invariants And Boundaries

- Gate-5 contribution must be nonempty and every supplied rail must belong to Gate 5 with memory-domain authority.
- This local validation does not independently census the full memory checker population; that belongs to the memory provider.
- A non-applicable repository gate refuses this five-gate certifying admission.
- Deriving admission neither executes gates nor proves that all declared artifacts have producers.
- Exact currentness checks must not be replaced by a manually copied registry digest.

### Todos

Production lifecycle finalization and telemetry remain separate consumers; this bridge alone does not connect them.

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

External domain documentation is not configured.

### Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

- Lane identity and five-gate compilation [1]
- Currentness recompilation/refusal [2]
- Registry construction preserves rail contracts [3]
- Applicability and memory-rail validation [4]

### Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

No cross-repository evidence is required for these file-local claims.
