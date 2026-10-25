# mcp/src/agents_remember/memory_quality/check.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`check.py` runs memory-layer quality checks and returns a single structured
payload for MCP closeout workflows.

## Code Commentary

### Landing-report scope

`DriftCheckContext.landing_base` is an optional independent landing resolver. The converted drift-slot dispatch forwards it to `converted_knowledge_check` alongside the existing `knowledge_base`: contract-bound reports compare with the admitted leaf base, while validator classification keeps its operation-base semantics. This is context propagation, not another refusing check or registry entry.


- The converted dispatch forwards independent validator and landing base ports. [18]



### Logic

The surviving style registry contains diff-marker, entity-catalog-alignment and table-shape checks. A default call without drift context selects those checks; with context it also selects the drift slot. The pre-metadata phase contains entity alignment only, and the post-metadata population contains drift plus the surviving style checks. These are registry declarations, not evidence that ordinary closeout invokes the full quality sequence.

`StyleCheckInputs` carries the onboarding root only. The retained `DriftCheckContext` fields include comparison/landing-base ports and historical provenance/output options; no legacy claim-reopen executor consumes a prepared-history tuple here.

On a converted tree the drift slot runs `converted_knowledge_check` under the result key `knowledge.converted`; all surviving document-shape checks run normally. The legacy Update History, citation-range and claim-reopen registry members and their not-applicable compatibility results were removed. Explicitly selecting a removed name raises `ValueError`. Public memory-quality admission refuses unconverted operational input before this runner rather than interpreting missing legacy checks as a pass.

**The converted check's base (L37 review R3-1).** `DriftCheckContext.knowledge_base` is an optional
`KnowledgeBasePort`; `_converted_check` passes it to `converted_knowledge_check(..., base=...)`. The
application binds it to the shared converted-base cache, so a converted working tree on an unconverted `HEAD`
is validated against `HEAD`'s conversion (MIK-R24 rule 7). Without it the check uses a converted `HEAD`.

The converted checker supplies refusing validator findings, a stale reference anchor among them, and report-only landing observations. A supplied comparison-base failure is a named `R24.7-converted-base` finding, and base-dependent anchor-path refusals are withheld rather than evaluated against an invented empty base. This is not the removed source-index acquisition/error guard. The aggregate runner retains each checker's declared finding count, complete refusing findings, bounded report-only samples and opt-in complete report-only findings.

### Invariants And Boundaries

- Unknown check names raise `ValueError`.
- Drift integrity requires `DriftCheckContext`; style checks can run with only
  an onboarding root.
- The top-level finding count uses each checker result's declared `findingCount`, coerced with `int(result.get("findingCount", 0))`; this still assumes the checker does not supply literal `None`. Complete refusing findings are retained.
- A supplied converted-base failure is reported by the converted checker; the old source-index exception class and guard are absent. Unreadable input must not be credited as measured absence.
- Full internal detail is opt-in and is removed before the public response. Bounded samples remain
  the default transport contract; report generation must not expand normal MCP payloads.

## Evidence

### Repo-Internal References




- The registered `memory_quality_check` dispatches typed sync/start/poll requests to their payload builders; its description names candidate leaf-contract scope and required coherence validation. [1]



- Drift summary provides the integrity checker payload, now typed `-> DriftSummaryPacket`. [3]


- The packet's `status` field typed by the imported status vocabulary, plus its `NotRequired` keys. [4]

- The first pre-code check enforces entity inventory/fingerprint alignment without requiring code metadata. [5]

- StyleCheckInputs now carries only the onboarding root; surviving style runners do not execute claim reopening or prepared-history citation gates. [6]

- Converted dispatch replaces the drift slot with the validator/reference report and runs the surviving document-shape checks; legacy compatibility checks are absent. [7]

- The surviving runner aggregates selected check results; it has no source-index acquisition exception guard. [8]


- The converted checker reports named base-build failure rather than inventing an empty comparison. [9]



- When a supplied converted base cannot be built, its named finding is retained and base-dependent anchor-path refusals are withheld. [10]


- run_check dispatches only the surviving STYLE_CHECKS and refuses an unknown name. [11]

- The aggregate runner retains declared refusing counts and complete findings, with bounded report-only samples and optional complete report-only rows. [13]


- The drift context carries the converted tree's comparison base. [16]


- The converted check receives the base port. [17]
