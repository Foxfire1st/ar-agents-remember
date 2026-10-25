# skills/c-03-repo-bootstrap/SKILL.md

## Governing Overview

[Repository area overview](../../overview.md)

## Purpose

Bootstrap onboarding in bounded, locality-first waves for a new repository or an existing source slice.

## Current Contract

Resolve context and source eligibility before building root and route-local overviews, evidence packs, file cards and file-level onboarding. The source-inventory gate precedes automation; uncertain low-confidence claims remain unresolved. The skill owns the planning/promotion sequence, while c-05 owns file-level card semantics. Converted evidence is authored through citation_fix rather than hand-written sidecars. Handoff names the actual cards, fixer state, baseline and moment-specific foundation state. Bootstrap output does not itself establish a baseline or knowledge foundation; onboarding/bootstrap audit files and a memory-root bootstrap staging directory have different commit treatment. This is the instruction contract, not evidence of an executed bootstrap or adopted baseline.

## Canonical Source Ownership

The byte-equal packaged skill is a distribution carrier, not an independent role, task or permission authority. The current source account above does not certify inherited prose, actual execution, launch delivery or grading.


- The canonical source supplies the current instruction or template contract described above; the package copy is derived. [1]


## Current Source Qualification

The current relationship table pairs this skill with `c-05-create-or-update-onboarding-files` for post-bootstrap promotion: touched files move from deferred to covered under that skill, which now also carries the memory-quality and findings-capture procedures. The retired `c-02-memory-quality-control` skill the inherited copy names in that row is history of those bytes, not a current neighbour.

## Inherited Source-Epoch Commentary

The following complete distribution-copy commentary and reference-note meanings are retained as inherited context. Earlier incompatible claims on the current seams explained above are historical, not restored authority. Historical reference labels do not allocate this card's references.

> # c-03-repo-bootstrap/SKILL.md
>
> ## Purpose
>
> This skill describes repository onboarding bootstrap. It defines a minimum root-overview bootstrap, a larger route-local memory build, and an existing-memory slice maintenance mode for added, moved, deleted, refreshed, or newly important source routes, with preservation-first handling for moved or deleted route memory.
>
> ## Code Commentary
>
> ### Logic
>
> `c-03-repo-bootstrap` skill resolves context with `c-08-ar-coordination-context-resolver` skill, writes all bootstrap paths relative to the resolved `onboarding_root`, and builds bootstrap memory in phases. The minimum output is `overview.md`; larger runs proceed through source inventory, area research, coverage planning, governing route mapping, route-local overview cards, route-local overview waves, docs and boundary evidence packs, file cards, file-level onboarding waves, curator reviews, and handoff. Existing-memory slice maintenance starts from verified existing memory and handles expansion, refresh, move, or cleanup for a bounded source slice. For moved or deleted routes, it now asks whether documented behavior moved, split, merged, or actually disappeared before removing stale artifacts. Root and route-local overviews use reference-anchor currentness and a compact `## Hot Path Summary`; generated route-index hot-path hints support Intent discovery. Cards have no metadata stamps or Update History. Citation tables are temporary fixer input, replaced by numbered evidence and fixer-authored sidecars; authors do not choose numbers or write sidecar JSON.
>
> ### Conventions
>
> Bootstrap no longer branches on an internal bootstrap mode: the skill resolves its memory root through `c-08-ar-coordination-context-resolver` and works under the resolved `onboarding_root`, which is the selected per-repo memory repo at `ar-coordination/memory-repos/ar-<repo-name>/`. The repo-local `ar-memory/` root was **removed from the product** (`CAPS-R12@v1`) and the generated skill text no longer names it; the skill's own `topology` input is an optional pass-through hint, not a mode selector. Durable route-local overview files belong in the mirrored onboarding hierarchy directly under the resolved onboarding root, while `bootstrap/` artifacts are promotion, review, and handoff artifacts. Generated `overview.index.json` files live beside overviews and include coverage plus `hotPath` fields.
>
> ### Invariants And Boundaries
>
> `c-03-repo-bootstrap` skill writes durable onboarding, not task coordination state. Task artifacts stay in the coordinator. Source inventory review is the pre-automation intake gate; automated bootstrap stops at handoff and asks whether separate closeout should run. Candidate eligibility comes from `settings.json` path rules; the skill's exclude list is a settings checklist/example, not a hidden replacement filter. Route-local overviews may become durable memory, but file-level onboarding remains separate and self-sufficient; `c-03-repo-bootstrap` skill prepares file cards and waves while `c-05-create-or-update-onboarding-files` skill owns canonical file-level content. Existing onboarding produced by `c-03-repo-bootstrap` skill is later consumed through `c-04-retrieval-strategy-router`. Route cleanup must not remove old memory until preservation, movement, retirement, or removal has been explicitly classified.
>
> ### Todos
>
> If bootstrap gains executable helpers, use `c-08-ar-coordination-context-resolver` skill's `memory_root`, `coordination_root`, `sources_path`, and `tools_path` fields directly rather than deriving paths from prose.
>
> ### Docs References
>
> No external documentation is needed for this repository-local skill.
>
> No relevant external documentation found.
>
> ## Evidence
>
> ### Repo-Internal References
>
> - `c-03-repo-bootstrap` skill defines root overview as the minimum bootstrap, under the resolved onboarding root, and introduces targeted work for existing-memory source slices. (historical reference 1)
> - The design requires durable route-local overview placement directly in the mirrored onboarding hierarchy, generated route indexes with hot-path hints, and self-sufficient file-level onboarding. (historical reference 2)
> - `c-03-repo-bootstrap` skill preserves thin orchestrator behavior, confidence tags, `c-08-ar-coordination-context-resolver` skill topology resolution, cross-repo read-only semantics, and `c-05-create-or-update-onboarding-files` skill ownership of file-level onboarding. (historical reference 3)
> - Automated mode starts only after source inventory is accepted or corrected, writes artifacts relative to the resolved `onboarding_root`, and treats common excludes as `settings.json` path-rule defaults. (historical reference 4)
> - The skill lists all bootstrap templates used for ledgers, state, plans, route maps, evidence packs, cards, waves, reviews, and handoff. (historical reference 5)
> - Root and route overviews obtain currentness from reference anchors and fixer-authored evidence, retaining compact hot-path summaries. (historical reference 6)
>
> ### Converted authoring and handoff
>
> Before first adoption no leaf enclosure exists: use the existing fixer without a contract and verify `pre-baseline` admission. The application owner measures the declared converted root, absence of attributed baseline and absence of linked memory worktrees; after adoption a contractless write refuses and names the leaf route. This is not a knowledge writer or commit route.
>
> The handoff names cards, a clean tree fixer dry run, baseline state/commit and the knowledge state at that moment with its actual next step. Fresh unborn memory reports context-not-admitted/memory_revision_unavailable; after adoption an unrecorded foundation reports not-recorded. Onboarding is not a foundation. The onboarding-relative bootstrap artifacts ship as an audit trail unless removed beforehand; only memory-root-level bootstrap is excluded from content commits.
>
> - The author-facing rules require temporary citation tables and verified contractless pre-baseline admission, with no manual sidecar JSON or number allocation. (historical reference 9)
> - Handoff distinguishes card, fixer, baseline and knowledge outcomes, and preserves the onboarding/bootstrap audit trail. (historical reference 10)
> - Existing-memory slice maintenance reuses current memory, covers expansion, refresh, move handling, deleted-slice cleanup, asks whether moved/deleted route behavior relocated before removal, and supports cleanup, move, preservation, or removal plans. (historical reference 7)
> - Phase 4 classifies deleted, moved, and stale onboarding routes; Phase 5 handoff records removed/moved/retired memory and keeps closeout outside automated bootstrap. (historical reference 8)
>
> As of the 260703-L9 lifecycle convergence, the bootstrap-trigger table row names `l-01-agent-lifecycles` (an active orchestrator job entering an uncovered area may trigger targeted bootstrap); the bootstrap flow itself is unchanged.
>
> ### Cross-Repo References
>
> No sibling repository evidence is needed for this skill.
>
> No meaningful cross-repo references found.
>
> ## 260921-ICR-L27 Onboarding Is Not The Repository's Knowledge Foundation, And The Handoff Now Says So
>
> `260921-ICR-L27` (`ICR-R27@v1`) adds one boundary paragraph and one relationship row to this skill, and
> both exist to stop a handoff from reading as complete when the repository's **knowledge foundation** has
> never been authored. The foundation — the authored invariants, families, source realizations and external
> sources in the knowledge database — is a separate step owned by `c-14-knowledge-bootstrap` and carried by
> the curator. Onboarding is **one optional input** to it: the foundation needs no onboarding file to
> start, and this skill neither requires the foundation to exist first nor claims it as its own output.
>
> The handoff must therefore **name** the foundation, with the state of the knowledge location where that
> state is known (`not-recorded`; `recorded`, with the identity; or `unusable`, with its code and path), and
> say that it is the curator's step. An unrun or absent foundation is a **named fact of the handoff**, never
> an omission that the handoff's own "trusted coverage" reads as completeness. Acceptance criterion 17
> carries the same obligation.
>
> **This card describes a generated copy.** The canonical instruction home is
> `skills/c-03-repo-bootstrap/SKILL.md`; `scripts/sync-skills.py` propagates the root tree into this
> package-owned copy and the eight harness starter packages, and nothing here is edited by hand.

Inherited reference 1 commentary (not a revalidated target):

> `c-03-repo-bootstrap` skill defines root overview as the minimum bootstrap, under the resolved onboarding root, and introduces targeted work for existing-memory source slices.
>
> Anchor: `# Repo Bootstrap`

Inherited reference 10 commentary (not a revalidated target):

> Handoff distinguishes card, fixer, baseline and knowledge outcomes, and preserves the onboarding/bootstrap audit trail.
>
> Anchor: "The handoff lists"

Inherited reference 2 commentary (not a revalidated target):

> The design requires durable route-local overview placement directly in the mirrored onboarding hierarchy, generated route indexes with hot-path hints, and self-sufficient file-level onboarding.
>
> Anchor: `### Locality-first memory`

Inherited reference 3 commentary (not a revalidated target):

> `c-03-repo-bootstrap` skill preserves thin orchestrator behavior, confidence tags, `c-08-ar-coordination-context-resolver` skill topology resolution, cross-repo read-only semantics, and `c-05-create-or-update-onboarding-files` skill ownership of file-level onboarding.
>
> Anchor: `## Behavior To Preserve`

Inherited reference 4 commentary (not a revalidated target):

> Automated mode starts only after source inventory is accepted or corrected, writes artifacts relative to the resolved `onboarding_root`, and treats common excludes as `settings.json` path-rule defaults.
>
> Anchor: `## Control Modes`

Inherited reference 5 commentary (not a revalidated target):

> The skill lists all bootstrap templates used for ledgers, state, plans, route maps, evidence packs, cards, waves, reviews, and handoff.
>
> Anchor: `## Templates`

Inherited reference 6 commentary (not a revalidated target):

> Root and route overviews obtain currentness from reference anchors and fixer-authored evidence, retaining compact hot-path summaries.
>
> Anchor: "Currentness"

Inherited reference 7 commentary (not a revalidated target):

> Existing-memory slice maintenance reuses current memory, covers expansion, refresh, move handling, deleted-slice cleanup, asks whether moved/deleted route behavior relocated before removal, and supports cleanup, move, preservation, or removal plans.
>
> Anchor: `### Existing-memory slice maintenance`

Inherited reference 8 commentary (not a revalidated target):

> Phase 4 classifies deleted, moved, and stale onboarding routes; Phase 5 handoff records removed/moved/retired memory and keeps closeout outside automated bootstrap.
>
> Anchor: `## Phase 4 — Bottom-Up Memory Build`

Inherited reference 9 commentary (not a revalidated target):

> The author-facing rules require temporary citation tables and verified contractless pre-baseline admission, with no manual sidecar JSON or number allocation.
>
> Anchor: "These tables"
