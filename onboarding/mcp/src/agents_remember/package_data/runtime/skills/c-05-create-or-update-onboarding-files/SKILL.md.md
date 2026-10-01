# c-05-create-or-update-onboarding-files/SKILL.md

## Purpose

This skill defines `c-05-create-or-update-onboarding-files` skill, the onboarding creation and maintenance skill. It routes file-level onboarding and repo-level entity catalogs to the appropriate workflow, points file-level onboarding at inline adapter additions when storage-specific syntax is needed, records the nearest governing route-local overview for file-level onboarding, maintains deterministic entity fingerprints, keeps entity inventory entries matched to fingerprint rows, routes structural source-slice maintenance to `c-03-repo-bootstrap` skill, preserves useful onboarding across refactors before deletion, and requires documentation discovery to follow the target repository's resolved `Domain Documentation` sources without hard-coding a provider.

## Code Commentary

### Seat Routing (260707-HFX-L11)

A new "Seat routing" paragraph, inserted immediately after the context-resolver intro, states that
in the manager -> builder -> reviewer -> curator chain (`l-01-agent-lifecycles` `roles/curator.md`)
onboarding create/update duty during leaf work belongs to the curator seat, not the builder — the
builder produces code and a turn report only. The curator runs this skill's workflows from a change
set (landed diff), the leaf task doc, and notes/ fed to it by the manager, and routes each item to
the right onboarding home (a concrete sidecar or the governing overview whose subject it is; the L3
Operational-Notes target is last-resort only, never a default). This is an additive paragraph only
— the strict 1-to-1 source mapping, governing-overview links, and metadata rules below are
unchanged; only the writing seat moved. A solo flat session with no separate curator seat runs this
skill itself, exactly as before. No workflow/template file under
`skills/c-05-create-or-update-onboarding-files/` needed edits — the mapping/metadata machinery is
role-agnostic by construction.

### Logic

`c-05-create-or-update-onboarding-files` skill tells agents to classify the onboarding target and the shape of the source change, use `c-08-ar-coordination-context-resolver` skill for the active coordination context and resolved roots, use sources as discovery aids rather than citation targets, preserve useful existing content, append update history entries when onboarding changes, and keep file-level onboarding self-sufficient while linking it back to the nearest governing overview. Its source-discovery rule makes the resolved memory layer's `Domain Documentation` category the required discovery plan: live sources named by that registry are authoritative, local mirrors/caches are only orientation aids, and missing/stale local docs trigger live retrieval through the registry's named tool or MCP before an agent records that no domain documentation exists. Dashboard task 14 adds a worktree-specific pre-write rule: when onboarding maintenance happens inside a `c-09-git-worktree-manager` worktree, check `worktree_status` and run `worktree_sync` first if source branches moved, before creating memory entries. It handles single-file work directly, routes package/module/source-route creation, refresh, move, or deletion cleanup to `c-03-repo-bootstrap` skill `existing-memory-slice-maintenance`, keeps route overview `## Hot Path Summary` sections current, refreshes generated route indexes after onboarding changes, and owns the curation/refresh of `git-blob-set-v1` entity evidence paths that `c-02-memory-quality-control` skill checks deterministically. Its lifecycle rules enforce body-before-metadata: every body update pairs with a same-pass `Update History` entry, and a changed source that genuinely warrants no content change records an explicit `No content impact: <reason>` (file sidecar) or `No route impact: <reason>` (governing route overview) history entry — deliberate reviewed-no-impact attestations that closeout surfaces in its tool response; header-only or unmarked history-only refreshes fail the closeout gates. Its preservation rule makes behavior-preserving moves update the mirrored onboarding path, makes splits/merges/behavior relocation reuse still-accurate old onboarding in new targets, and allows deletion or retirement only after proving the documented behavior is gone. When `c-02-memory-quality-control` skill reports missing or orphaned entity fingerprint rows, `c-05-create-or-update-onboarding-files` skill reviews whether the entity was removed, renamed, moved, or simply lacks verification.

**Converted memory (L37 fix round P1b).** A new `## Converted Memory` section comes before the routing table:
check the memory tree first, and when it holds `knowledge/layout.json` follow
`workflows/converted-card-workflow.md`, not the metadata, Update History and citation-table rules of the rest of
the skill. A card's evidence is `- <finding> [n]` lines over sidecar `references`; the curator writes the evidence
as a citation table and `citation_fix` authors the sidecar with resolved anchors; a change with no onboarding
impact is an `onboarding_trace` row written through `knowledge-ingest`. Sidecar JSON is never written by hand.
Everything else in the skill applies to unconverted memory, which is only read once its repository holds
converted memory.

### Conventions

File-level onboarding mirrors one source file directly under the resolved onboarding root. Route-local overview files may exist beside mirrored source folders as governing context, but they do not replace file-level onboarding. Generated route indexes carry coverage, sidecar absence inference, and `hotPath` summary/hints; they are refreshed from overview/sidecar state rather than hand-edited. Repo-entity catalogs describe recurring real entities and carry deterministic fingerprints over the smallest practical set of load-bearing evidence files. Every inventory entry should have exactly one fingerprint row. Sources and tools files are registries, not proof for onboarding claims. Provider-specific documentation systems belong in resolved memory-layer source registries, not in this package's generic `c-05-create-or-update-onboarding-files` skill source.

### Invariants And Boundaries

`c-05-create-or-update-onboarding-files` skill updates onboarding content, but it should not turn task plans into current-state documentation, flatten structural route changes into unrelated file-level edits, or discard old onboarding before checking whether its documented behavior moved. It must keep references verifiable, avoid overwriting unresolved warnings without evidence, and keep same-repository, docs, and cross-repo evidence in the correct buckets. It must not treat local documentation caches as authoritative when the resolved source registry names a live retrieval path, and it must record live-source checks or blockers when no relevant documentation is found.

### Todos

After this working-tree update lands, refresh verification metadata to the committed `c-05-create-or-update-onboarding-files` skill source revision.


## CCR-R12@v5 Transaction Boundary

Current contract: curators update affected sidecars, route overviews, indexes, and entity records from current source, preserving body plus history and reporting every check result honestly. Curation is always complete: the curator runs the full `memory_quality_check` operation for the leaf and publishes the coherence authority when the checklist requires it. Closeout consumes that prepared memory leg, including the completed curation, as a Git transaction; it does not rerun the operation and does not turn onboarding maintenance into an automatic certification gate.

### Docs References

No external domain documentation applies to the repository-local onboarding maintenance contract. The resolved `agents-remember` source registry has no configured `Domain Documentation` entries, so the relevant evidence for this package behavior is repository source.

No relevant external documentation found after checking live sources.

## Evidence

### Repo-Internal References

`c-05-create-or-update-onboarding-files` skill is the content-update counterpart to `c-02-memory-quality-control` skill's detection.

- Routing sends file-level onboarding, repo-level entity catalog work, and route/slice maintenance to different workflows or `c-03-repo-bootstrap` skill modes. [1]
- `c-05-create-or-update-onboarding-files` skill handles simple file/entity updates directly, requires proof before treating deleted files as cleanup-only, and routes package/module/source-route creation, refresh, move, split, merge, relocation, or deletion cleanup to `c-03-repo-bootstrap` skill when file-by-file work would lose structure. [2]
- The onboarding preservation rule treats existing onboarding as durable memory, moves one-to-one behavior-preserving sidecars, reuses accurate old content after splits/merges/relocation, and deletes or retires only when no safe current target remains. [3]
- Sidecar placement rules now use the resolved onboarding root directly, include route-local `overview.md` files under mirrored source folders, and record generated route indexes with hot-path summary/hints. [4]
- Quick rules require file-level onboarding to stay self-sufficient, link to the nearest governing overview, preserve reference explanations, maintain deterministic entity fingerprints, refresh route indexes, keep `Hot Path Summary` current, and avoid deleting onboarding before checking whether behavior moved. [5]
- Route index refresh derives coverage, scope, copied `hotPath.summary`, candidate hints, anchor hints, and indexed sidecar absence from current onboarding/source state. [6]
- Source discovery requires the resolved `Domain Documentation` category, treats live registry-named documentation sources as authoritative, uses local mirrors only as orientation caches, and triggers live retrieval before reporting no domain docs. [7]
- Reference and lifecycle rules require verified links, correct bucket selection, metadata refresh, preservation-first handling for moves/splits/merges/relocation/deletion, entity cleanup review for removed/renamed/moved cases, and `c-03-repo-bootstrap` skill routing for package/module/source-route moves or deletions. [8]
- Worktree-backed onboarding maintenance checks `worktree_status` and runs needed `worktree_sync` before writing memory entries. [9]

- The skill routes a converted memory tree to the converted-card workflow. [10]

### Cross-Repo References

`c-05-create-or-update-onboarding-files` skill can handle cross-repo references when actual boundary evidence exists, but this skill doc does not require a sibling repository citation.

No meaningful cross-repo references found for current skill semantics.
