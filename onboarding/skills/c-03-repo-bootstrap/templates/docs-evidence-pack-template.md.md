# skills/c-03-repo-bootstrap/templates/docs-evidence-pack-template.md

## Governing Overview

[Repository onboarding overview](../../../overview.md)

## Purpose

This template defines the documentation evidence pack used when bootstrap needs domain, protocol, vendor, library, or business-rule evidence. It is a reusable format with placeholders, not a completed documentation pass or an attestation of evidence availability.

## Code Commentary

### Logic

The docs pack records scope, checked documentation sources, confirmed findings with evidence, documentation constraints, terms and definitions, files likely affected, explicit no-evidence records, and open questions. Its metadata provides repository, area or route, generation time, the source-registry routing field, and alternative statuses; the example finding includes evidence lines, a canonical-document link, applicability, and confidence.

### Conventions

The pack uses `system/sources.md` only as a routing index, not as proof. Bootstrap Phase 4E uses its Domain Documentation category for discovery and requires actual documentation or local-mirror evidence, an account of checked sources when nothing relevant exists, and source-document confirmation instead of treating embedding hits as evidence. The template demonstrates a canonical-document URL in the finding row; downstream onboarding citation tables instead use plain source-path ranges, with the canonical documentation URL described in prose.

### Invariants And Boundaries

Docs packs support documentation-sensitive claims; they do not substitute for repo-internal source evidence or cross-repository boundary evidence. Phase 4E assigns the template to priority routes where domain behavior, external protocols, vendor/library behavior, or business rules matter. Empty placeholders and offered status choices establish no actual findings, completed pack, or authority to proceed.

### Historical Notes

The inherited TODO, “Fill verification metadata after the source file is committed,” is retained here as historical legacy guidance, not as a live command or a statement that the prerequisite has been satisfied. Current bootstrap citation rules describe reference resolution through citation tables and a fixer, rather than commit-verification metadata.

### Docs References

Inherited applicability note: the old card treated this as a repository-local template requiring no external documentation and reported no relevant external documentation found. The account is bounded to local template and bootstrap-skill evidence, not a new survey of all external documentation.

## Evidence

### Repo-Internal References

The following same-repository source ranges support the template description and the retained cross-file bootstrap responsibilities. The template and skill define the format and responsibilities, not an actual completed bootstrap wave.

- The template supplies placeholder identity and status metadata. [1]
- The pack format covers scope, documentation sources, findings, constraints, terms, affected files, missing evidence, and questions. [2]
- The example finding records evidence lines, a canonical-document link, applicability, and confidence. [3]
- Phase 4E writes docs packs for documentation-sensitive priority routes and requires direct documentation evidence or explicit missing-evidence accounts. [4]
- Downstream onboarding uses source-path ranges, keeps canonical URLs in prose, excludes routing registries as proof, and delegates sidecar creation to the fixer. [5]

### Cross-Repo References

Inherited boundary note: the old card reported no sibling-repository evidence needed and no meaningful cross-repository references found. The account is supported by same-repository evidence; the inherited absence statement does not establish the absence of relevant evidence in every sibling repository.
