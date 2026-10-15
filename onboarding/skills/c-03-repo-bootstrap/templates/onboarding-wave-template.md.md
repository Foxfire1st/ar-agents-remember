# skills/c-03-repo-bootstrap/templates/onboarding-wave-template.md

## Governing Overview

[Repository onboarding overview](../../../overview.md)

## Purpose

This template defines route-overview and file-onboarding wave manifests. It is a planning and coordination format for bounded work, not durable documentation of a source file’s behavior or a record that a wave has actually been assigned or completed.

## Code Commentary

### Logic

The wave manifest records repository and generation metadata, wave type, bootstrap mode, alternative statuses, goal, included cards, excluded or deferred paths with revisit triggers, required evidence packs, worker instructions, assignments, completion criteria, and developer review questions.

### Conventions

Waves are small, bounded units. The template instructs workers to read their assigned card first and only its listed files and evidence, use the route-local overview template for overview waves, and invoke or follow `c-05-create-or-update-onboarding-files` for file onboarding. Workers keep planning notes out of durable onboarding, preserve strict one-to-one source mapping, backlink to the nearest governing overview, avoid absolute filesystem paths and registry or embedding proof, and return changed onboarding paths with unresolved questions. Phase 4H additionally directs file workers to read governing and listed ancestor overviews and escalate before widening source/evidence reads.

### Invariants And Boundaries

The manifest coordinates workers rather than replacing their durable onboarding output. Its done criteria require onboarding or an explicit blocker for every included target, evidence-backed documentation and cross-repository claims, recorded unresolved items, and curator review that passed or listed required fixes. These are template criteria, not a declaration that review passed. The canonical bootstrap skill assigns file-level semantics to c-05 and calls for route-index refresh after a file-onboarding wave changes sidecars.

### Historical Notes

The inherited TODO, “Fill verification metadata after the source file is committed,” is retained as historical legacy guidance only; it is not a live instruction. The manifest format alone does not prove current reference resolution, actual worker assignments, updated indexes, or completed review.

### Docs References

Inherited applicability note: the old card treated this as a repository-local template requiring no external documentation and reported no relevant external documentation found. The account is bounded to local template and bootstrap-skill evidence, not a new survey of all external documentation.

## Evidence

### Repo-Internal References

The following same-repository source ranges support the template description and the retained cross-file bootstrap responsibilities. The template and skill define the format and responsibilities, not an actual completed bootstrap wave.

- The manifest provides placeholder metadata, goals, included and deferred cards, and evidence requirements. [1]
- Worker instructions preserve bounded reads, source mirroring, overview backlinks, evidence boundaries, and output reporting. [2]
- The format records completion criteria and developer review questions without asserting an actual wave outcome. [3]
- Bootstrap overview waves are deliberately small and bounded. [4]
- Phase 4H uses this manifest, delegates file-level work to c-05, defines bounded sizing and reading duties, and calls for index refresh. [5]
- The canonical bootstrap skill names c-05 as owner of file-level semantics and delegates file output rules to it. [6]
- c-05 is the onboarding entry point; its converted-memory branch overrides the legacy workflow/template routing below it. [7]

### Cross-Repo References

Inherited boundary note: the old card reported no sibling-repository evidence needed and no meaningful cross-repository references found. The account is supported by same-repository evidence; the inherited absence statement does not establish the absence of relevant evidence in every sibling repository.
