# skills/c-03-repo-bootstrap/templates/cross-repo-boundary-pack-template.md

## Governing Overview

[overview](../../../overview.md)

## Purpose

This template defines a research evidence pack for allowed cross-repository or external-system boundaries discovered during repository bootstrap. The canonical source is under `skills/c-03-repo-bootstrap/`; its packaged twin is distribution content, not a separate authoring home.

## Code Commentary

### Logic

The pack records repository/route identification, generation time, topology and completion status, followed by allowed adjacent repositories and expected/actual branches, boundary summary, confirmed interfaces and shared contracts. Later sections retain branch/topology notes, same-repository facts that must remain repo-internal, confidence-labelled risks, and low-confidence ties needing developer confirmation.

### Conventions

The example records adjacent repositories as read-only or ignored and explicitly explains exclusion on branch mismatch. Same-repository helper calls belong in `Repo-Internal References`, not cross-repository evidence. The pack header and status placeholders describe research output; neither those values nor a populated template grant access to another repository or permission to change its memory.

### Invariants And Boundaries

The current supporting bootstrap skill, rather than this blank template, directs Phase 4F to prepare packs for priority routes with inbound or outbound cross-repository signals. Its safeguards allow adjacent reads only under the resolved topology and branch rules, keep adjacent repositories read-only, require real system-boundary evidence and park naming-only LOW-confidence ties rather than promoting them to durable facts. Only the target repository memory is updated in that documented bootstrap scope.

This card describes a template as source; it is not an instance of that template. Converted onboarding uses mirrored Markdown and a companion authored by the supported writers: no metadata table or in-card Update History, and normally no hand-authored companion JSON. Citation tables are authoring input for the fixer, not the final evidence representation. Describing an older template format does not authorize new legacy-format memory writes. Use the fixer and writer first. Only a covered correct-input write refusal permits the declared same-tool/input-class recovery, with owner notification, manual provenance, checks and a defect issue. Missing admission/capability is not such a refusal; read/check/validation/sync, starts, product guards, commit gates and denied or unanswered permission requests keep their stops.

## Evidence

### Docs References

No external documentation is needed for this repository-local template; its account rests on the source and the local workflow definitions.

### Repo-Internal References

The template proves the pack layout. The actual bootstrap skill proves Phase 4F applicability and boundary safeguards; these cross-file obligations are not inferred from placeholder headings.

- The template records allowed adjacent repositories, boundary summaries, confirmed interfaces and shared contracts. [1]
- The template retains branch/topology notes, same-repository exclusions, boundary risks and developer-confirmation needs. [2]

- The bootstrap skill directs Phase 4F packs for priority routes with inbound or outbound signals and bounds adjacent reads and LOW-confidence ties. [3]

- The bootstrap preservation contract keeps adjacent-repository evidence read-only and limits memory updates to the target repository. [4]

### Cross-Repo References

A template for future boundary evidence is not itself a verified sibling-repository boundary.

- Converted cards keep metadata stamps, card-local change history and completed citation tables out of their bodies; the fixer writes the numbered evidence lines and the sidecar. [5]

- Only a covered correct-input write refusal admits the same-tool recovery ladder. [6]
