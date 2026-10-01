# c-03-repo-bootstrap/SKILL.md

## Purpose

This skill describes repository onboarding bootstrap. It defines a minimum root-overview bootstrap, a larger route-local memory build, and an existing-memory slice maintenance mode for added, moved, deleted, refreshed, or newly important source routes, with preservation-first handling for moved or deleted route memory.

## Code Commentary

### Logic

`c-03-repo-bootstrap` skill resolves context with `c-08-ar-coordination-context-resolver` skill, writes all bootstrap paths relative to the resolved `onboarding_root`, and builds bootstrap memory in phases. The minimum output is `overview.md`; larger runs proceed through source inventory, area research, coverage planning, governing route mapping, route-local overview cards, route-local overview waves, docs and boundary evidence packs, file cards, file-level onboarding waves, curator reviews, and handoff. Existing-memory slice maintenance starts from verified existing memory and handles expansion, refresh, move, or cleanup for a bounded source slice. For moved or deleted routes, it now asks whether documented behavior moved, split, merged, or actually disappeared before removing stale artifacts. Root and route-local overviews record route-based verification metadata and a compact `## Hot Path Summary` so `c-02-memory-quality-control` skill can later detect deterministic overview drift by `sourceRoute` and `c-04-retrieval-strategy-router` skill can use generated route-index hot-path hints as part of the Intent substrate.

### Conventions

Bootstrap no longer branches on an internal bootstrap mode: the skill resolves its memory root through `c-08-ar-coordination-context-resolver` and works under the resolved `onboarding_root`, which is the selected per-repo memory repo at `ar-coordination/memory-repos/ar-<repo-name>/`. The repo-local `ar-memory/` root was **removed from the product** (`CAPS-R12@v1`) and the generated skill text no longer names it; the skill's own `topology` input is an optional pass-through hint, not a mode selector. Durable route-local overview files belong in the mirrored onboarding hierarchy directly under the resolved onboarding root, while `bootstrap/` artifacts are promotion, review, and handoff artifacts. Generated `overview.index.json` files live beside overviews and include coverage plus `hotPath` fields.

### Invariants And Boundaries

`c-03-repo-bootstrap` skill writes durable onboarding, not task coordination state. Task artifacts stay in the coordinator. Source inventory review is the pre-automation intake gate; automated bootstrap stops at handoff and asks whether separate closeout should run. Candidate eligibility comes from `settings.json` path rules; the skill's exclude list is a settings checklist/example, not a hidden replacement filter. Route-local overviews may become durable memory, but file-level onboarding remains separate and self-sufficient; `c-03-repo-bootstrap` skill prepares file cards and waves while `c-05-create-or-update-onboarding-files` skill owns canonical file-level content. Existing onboarding produced by `c-03-repo-bootstrap` skill is later consumed through `c-04-retrieval-strategy-router`. Route cleanup must not remove old memory until preservation, movement, retirement, or removal has been explicitly classified.

### Todos

If bootstrap gains executable helpers, use `c-08-ar-coordination-context-resolver` skill's `memory_root`, `coordination_root`, `sources_path`, and `tools_path` fields directly rather than deriving paths from prose.

### Docs References

No external documentation is needed for this repository-local skill.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- `c-03-repo-bootstrap` skill defines root overview as the minimum bootstrap, under the resolved onboarding root, and introduces targeted work for existing-memory source slices. [1]
- The design requires durable route-local overview placement directly in the mirrored onboarding hierarchy, generated route indexes with hot-path hints, and self-sufficient file-level onboarding. [2]
- `c-03-repo-bootstrap` skill preserves thin orchestrator behavior, confidence tags, `c-08-ar-coordination-context-resolver` skill topology resolution, cross-repo read-only semantics, and `c-05-create-or-update-onboarding-files` skill ownership of file-level onboarding. [3]
- Automated mode starts only after source inventory is accepted or corrected, writes artifacts relative to the resolved `onboarding_root`, and treats common excludes as `settings.json` path-rule defaults. [4]
- The skill lists all bootstrap templates used for ledgers, state, plans, route maps, evidence packs, cards, waves, reviews, and handoff. [5]
- Phase 3 and Phase 4D require route-based overview verification metadata and `Hot Path Summary` sections so `c-02-memory-quality-control` skill can compare recorded `sourceRoute` scopes and `c-04-retrieval-strategy-router` skill can use compact route hints inside the Intent substrate. [6]
- Existing-memory slice maintenance reuses current memory, covers expansion, refresh, move handling, deleted-slice cleanup, asks whether moved/deleted route behavior relocated before removal, and supports cleanup, move, preservation, or removal plans. [7]
- Phase 4 classifies deleted, moved, and stale onboarding routes; Phase 5 handoff records removed/moved/retired memory and keeps closeout outside automated bootstrap. [8]

As of the 260703-L9 lifecycle convergence, the bootstrap-trigger table row names `l-01-agent-lifecycles` (an active orchestrator job entering an uncovered area may trigger targeted bootstrap); the bootstrap flow itself is unchanged.

### Cross-Repo References

No sibling repository evidence is needed for this skill.

No meaningful cross-repo references found.

## 260921-ICR-L27 Onboarding Is Not The Repository's Knowledge Foundation, And The Handoff Now Says So

`260921-ICR-L27` (`ICR-R27@v1`) adds one boundary paragraph and one relationship row to this skill, and
both exist to stop a handoff from reading as complete when the repository's **knowledge foundation** has
never been authored. The foundation — the authored invariants, families, source realizations and external
sources in the knowledge database — is a separate step owned by `c-14-knowledge-bootstrap` and carried by
the curator. Onboarding is **one optional input** to it: the foundation needs no onboarding file to
start, and this skill neither requires the foundation to exist first nor claims it as its own output.

The handoff must therefore **name** the foundation, with the state of the knowledge location where that
state is known (`not-recorded`; `recorded`, with the identity; or `unusable`, with its code and path), and
say that it is the curator's step. An unrun or absent foundation is a **named fact of the handoff**, never
an omission that the handoff's own "trusted coverage" reads as completeness. Acceptance criterion 17
carries the same obligation.

**This card describes a generated copy.** The canonical instruction home is
`skills/c-03-repo-bootstrap/SKILL.md`; `scripts/sync-skills.py` propagates the root tree into this
package-owned copy and the eight harness starter packages, and nothing here is edited by hand.
