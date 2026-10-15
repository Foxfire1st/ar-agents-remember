# skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

This source defines the retained file-level onboarding workflow for one concrete source file: one-to-one mirrored placement, a backlink to governing route context, source discovery, explanatory commentary, reference health, and preservation when behavior moves. It also identifies when a structural change must be routed to `c-03-repo-bootstrap` rather than handled as isolated file documentation. Inline storage shares its semantic model but has a separate storage adapter.

## Code Commentary

### Logic

The workflow begins by confirming one source file, its mirrored onboarding path, and the nearest existing governing overview found by walking ancestor onboarding directories. Sidecar names append `.md` to the source filename under the resolved onboarding root. Inline storage keeps the section semantics while delegating syntax, placement, digesting and fallback to `inline-onboarding-workflow.md`. The workflow is a schema source for the retained file-level model, not a replacement for the converted-card workflow.

Discovery starts with the resolved `system/sources.md` `Domain Documentation` category, not adjacent onboarding alone. When the registry names local and live documentation, the live source is authoritative and the local mirror is an orientation cache. Missing, stale or insufficient cached material prompts live retrieval before an absence claim; a failed search or blocked retrieval must be recorded. The registry chooses the search space but is not evidence. The actual documentation, code, generated artifact, onboarding or boundary source must prove the finding.

Creation reads the source and relevant documentation, establishes the governing backlink, fills the applicable template and checks references. Health checks preserve and correct useful explanation, check that cited targets exist and support the prose, and retain cross-repo classification only for a real boundary. Maintenance re-reads source and onboarding, corrects affected purpose, logic, conventions, invariants and references, and delegates inline serialization to its adapter.

### Conventions

The retained unconverted shape includes a metadata table with `governingOverview`, `## Governing Overview`, purpose, code commentary, three top-level reference sections and `## Update History`. Its commentary subsections are Logic, Conventions, Invariants And Boundaries and Todos. In particular, `Docs References` is top-level in that retained schema, not nested under Code Commentary. Reference sections preserve useful explanatory prose and add Finding/Anchor/Source evidence; the workflow rejects the superseded Citations/Source Path column shape. Its legacy timestamps come from the named time tool, verified commit fields identify the latest source-file commit, and verification fields remain empty for planned source that does not yet exist. Legacy history is append-only and newest-first. These describe retained source text, not requirements for this converted card.

The file-level template requires a real relative Markdown governing-overview link, not just a bare path or prose, and a self-sufficient explanation rather than “see overview.” The workflow's create step describes `memory-citations --fix` as range repair with no migration mode; it says a superseded tree converts to text knowledge before converted curator authoring. Reading that instruction is not evidence of a conversion, repair run or accepted maintenance result.

### Applicability To Converted Memory

The workflow's opening sends memory containing `knowledge/layout.json` to `converted-card-workflow.md`. The canonical skill additionally says unconverted memory is read-only after cutover and never permits hand-written sidecar JSON. Converted cards have prose at the mirrored `.md` path and a companion `.json` authored by the proper owners; they have no metadata table, verification stamps or Update History. Finding/Anchor/Source tables are temporary authoring input: the citation fixer assigns references and replaces the tables, so a finished converted card does not retain them. The table is only an authoring intermediate; the fixer produces the final reference representation.

Converted maintenance follows the converted workflow's writer-owned current source-file and nearest-route history rows, not a legacy history-entry shortcut. Its move/delete handling separates typed-entry changes through the writer from card/reference authoring through the fixer. Source instructions and templates describe these routes; they do not authorize running them or grant a seat any additional permission.

### Invariants And Boundaries

The file card must remain useful when opened directly, explain its source rather than active plans, and point to the nearest governing overview. Route-level creation, refresh, move or deletion belongs to the named bootstrap mode. Before deleting old onboarding for a move, split, merge or relocation, inspect it and reuse accurate purpose, commentary, invariants and evidence in current targets. True deletion requires proving the behavior did not move. Repair affected indexes and cross-links and consider entity-catalog or nearby-card consequences. Legacy metadata/history steps in the retained workflow do not override converted format.

### Retained Notes And Discovery Scope

The inherited card labels its converted-memory correction “L37 fix round P1b,” names MIK-R46 conversion-first/no-migration guidance and records old-format-section removal as MIK-R65. Those labels are retained historical context, not a new claim that the named work has completed. The opening redirect and no-migration wording are present in the canonical source.

The inherited TODO says to refresh verification metadata after its working-tree change lands. That is a historical legacy-format follow-up, not an instruction to add stamps to a converted card or an assertion that a landing occurred. Its documentation notes say this repository-local workflow needed no external domain documentation, that the then-resolved registry had no Domain Documentation entries, and that no relevant external documentation was found after live checks. Its boundary notes say no sibling evidence was needed and no meaningful cross-repo references were found. Those scoped past-discovery statements are preserved, not repeated as a fresh registry inspection or live search. Repository-local source and templates support this contract account; the discovery observations remain historical.

## Evidence

- The workflow delegates converted memory to the converted-card workflow instead of its retained metadata, history and citation rules. [1]
- One source file has one onboarding unit; structural slice maintenance is routed to the named bootstrap mode. [2]
- Documentation discovery uses the configured category, live-source checks and actual proving evidence rather than the registry itself. [3]
- Mirrored placement appends .md, preserves one-to-one mapping and links the nearest overview; inline syntax is delegated. [4]
- The retained schema includes verification fields, top-level reference sections, commentary subsections and append-only history; these are legacy, not converted-card requirements. [5]
- Creation confirms single-file scope, reads the overview and proving sources, checks reference health and describes repair without a migration option. [6]
- Maintenance re-reads evidence, preserves knowledge across relocation and requires behavior-deletion proof before retirement. [7]
- The file template requires a relative Markdown governing link and a useful standalone purpose. [8]
- Canonical skill-level precedence makes unconverted content read-only and prohibits hand-authored companions. [9]
- Converted creation uses a canonical source title, relative governing link and temporary evidence table, with fixer-owned references. [10]
- Converted no-change answers use writer-owned source and nearest-route history rows; legacy stamps and hand-allocated references are forbidden. [11]
- Converted relocation separates writer-owned typed entries from card and reference repair, and deletion first checks whether behavior moved. [12]
