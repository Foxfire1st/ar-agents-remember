# skills/c-03-repo-bootstrap/templates/cross-repo-boundary-pack-template.md

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

This template defines a research evidence pack for allowed cross-repository or external-system boundaries discovered during repository bootstrap. The canonical source is under `skills/c-03-repo-bootstrap/`; its packaged twin is distribution content, not a separate authoring home.

## Code Commentary

### Logic

The pack records repository/route identification, generation time, topology and completion status, followed by allowed adjacent repositories and expected/actual branches, boundary summary, confirmed interfaces and shared contracts. Later sections retain branch/topology notes, same-repository facts that must remain repo-internal, confidence-labelled risks, and low-confidence ties needing developer confirmation.

### Conventions

The example records adjacent repositories as read-only or ignored and explicitly explains exclusion on branch mismatch. Same-repository helper calls belong in `Repo-Internal References`, not cross-repository evidence. The pack header and status placeholders describe research output; neither those values nor a populated template grant access to another repository or permission to change its memory.

### Invariants And Boundaries

The current supporting bootstrap skill, rather than this blank template, directs Phase 4F to prepare packs for priority routes with inbound or outbound cross-repository signals. Its safeguards allow adjacent reads only under the resolved topology and branch rules, keep adjacent repositories read-only, require real system-boundary evidence and park naming-only LOW-confidence ties rather than promoting them to durable facts. Only the target repository memory is updated in that documented bootstrap scope.

This card describes a template as source; it is not an instance of that template. Converted onboarding uses mirrored Markdown and a companion authored by the supported writers: no metadata table or in-card Update History, and no hand-authored companion JSON. Citation tables are authoring input for the fixer, not the final evidence representation. Describing an older template format does not authorize new legacy-format memory writes.

### Todos

The inherited card asked to fill verification metadata after committing the source. Preserve that as a historical maintenance note, not a converted-card task: converted cards have no `lastVerifiedCommit*` fields, and the note establishes no current commit or verification result.

## Evidence

### Docs References

The inherited card recorded that no external documentation was needed or relevant for this repository-local template. The account is supported by source and local workflow definitions, not a fresh external-document search result.

### Repo-Internal References

The template proves the pack layout. The actual bootstrap skill proves Phase 4F applicability and boundary safeguards; these cross-file obligations are not inferred from placeholder headings.

- The template records allowed adjacent repositories, boundary summaries, confirmed interfaces and shared contracts. [1]
- The template retains branch/topology notes, same-repository exclusions, boundary risks and developer-confirmation needs. [2]
- The bootstrap skill directs Phase 4F packs for priority routes with inbound or outbound signals and bounds adjacent reads and LOW-confidence ties. [3]
- The bootstrap preservation contract keeps adjacent-repository evidence read-only and limits memory updates to the target repository. [4]
- Converted cards use writer-owned companions rather than legacy verification metadata or in-card history. [5]

### Cross-Repo References

No sibling-repository evidence was needed for the inherited explanation of this template, and none was read here. A template for future boundary evidence is not itself a verified sibling-repository boundary.
