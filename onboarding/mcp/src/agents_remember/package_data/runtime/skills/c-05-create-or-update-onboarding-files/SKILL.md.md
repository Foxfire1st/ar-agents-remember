# c-05-create-or-update-onboarding-files/SKILL.md

| Field                  | Value                                                                     |
| ---------------------- | ------------------------------------------------------------------------- |
| repository             | agents-remember                                                        |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md` |
| doc_type               | `file-level-onboarding`                                                   |
| lastUpdated            | 2026-07-08T00:00+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`                                |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|

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

### Conventions

File-level onboarding mirrors one source file directly under the resolved onboarding root. Route-local overview files may exist beside mirrored source folders as governing context, but they do not replace file-level onboarding. Generated route indexes carry coverage, sidecar absence inference, and `hotPath` summary/hints; they are refreshed from overview/sidecar state rather than hand-edited. Repo-entity catalogs describe recurring real entities and carry deterministic fingerprints over the smallest practical set of load-bearing evidence files. Every inventory entry should have exactly one fingerprint row. Sources and tools files are registries, not proof for onboarding claims. Provider-specific documentation systems belong in resolved memory-layer source registries, not in this package's generic `c-05-create-or-update-onboarding-files` skill source.

### Invariants And Boundaries

`c-05-create-or-update-onboarding-files` skill updates onboarding content, but it should not turn task plans into current-state documentation, flatten structural route changes into unrelated file-level edits, or discard old onboarding before checking whether its documented behavior moved. It must keep references verifiable, avoid overwriting unresolved warnings without evidence, and keep same-repository, docs, and cross-repo evidence in the correct buckets. It must not treat local documentation caches as authoritative when the resolved source registry names a live retrieval path, and it must record live-source checks or blockers when no relevant documentation is found.

### Todos

After this working-tree update lands, refresh verification metadata to the committed `c-05-create-or-update-onboarding-files` skill source revision.

### Docs References

No external domain documentation applies to the repository-local onboarding maintenance contract. The resolved `agents-remember` source registry has no configured `Domain Documentation` entries, so the relevant evidence for this package behavior is repository source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

`c-05-create-or-update-onboarding-files` skill is the content-update counterpart to `c-02-memory-quality-control` skill's detection.

| Finding | Anchor | Source |
| --- | --- | --- |
| Routing sends file-level onboarding, repo-level entity catalog work, and route/slice maintenance to different workflows or `c-03-repo-bootstrap` skill modes. | `## Routing` | mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md:40-54 |
| `c-05-create-or-update-onboarding-files` skill handles simple file/entity updates directly, requires proof before treating deleted files as cleanup-only, and routes package/module/source-route creation, refresh, move, split, merge, relocation, or deletion cleanup to `c-03-repo-bootstrap` skill when file-by-file work would lose structure. | `## Route-Level Maintenance Routing` | mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md:55-76 |
| The onboarding preservation rule treats existing onboarding as durable memory, moves one-to-one behavior-preserving sidecars, reuses accurate old content after splits/merges/relocation, and deletes or retires only when no safe current target remains. | `## Onboarding Preservation Rule` | mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md:77-85 |
| Sidecar placement rules now use the resolved onboarding root directly, include route-local `overview.md` files under mirrored source folders, and record generated route indexes with hot-path summary/hints. | `## Sidecar Placement Rules` | mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md:86-106 |
| Quick rules require file-level onboarding to stay self-sufficient, link to the nearest governing overview, preserve reference explanations, maintain deterministic entity fingerprints, refresh route indexes, keep `Hot Path Summary` current, and avoid deleting onboarding before checking whether behavior moved. | `## Quick Rules` | mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md:107-129 |
| Route index refresh derives coverage, scope, copied `hotPath.summary`, candidate hints, anchor hints, and indexed sidecar absence from current onboarding/source state. | `## Route Index Refresh` | mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md:130-172 |
| Source discovery requires the resolved `Domain Documentation` category, treats live registry-named documentation sources as authoritative, uses local mirrors only as orientation caches, and triggers live retrieval before reporting no domain docs. | `## Source Discovery Rule` | mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md:173-185 |
| Reference and lifecycle rules require verified links, correct bucket selection, metadata refresh, preservation-first handling for moves/splits/merges/relocation/deletion, entity cleanup review for removed/renamed/moved cases, and `c-03-repo-bootstrap` skill routing for package/module/source-route moves or deletions. | `## Reference Section Rule` | mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md:186-202 |
| Worktree-backed onboarding maintenance checks `worktree_status` and runs needed `worktree_sync` before writing memory entries. | `## Lifecycle Rules` | mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md:203-231 |

## Cross-Repo References

`c-05-create-or-update-onboarding-files` skill can handle cross-repo references when actual boundary evidence exists, but this skill doc does not require a sibling repository citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found for current skill semantics. | n/a | n/a |

## Update History

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 9 citation claims; scoped recheck clean (0 findings).

- 2026-07-08T00:00+02:00 — 260707-HFX-L11 curator activation (c-05 rewiring, R3): added the "Seat
  routing" paragraph documenting that onboarding create/update duty during leaf work routes to the
  curator seat, not the builder, in the manager -> builder -> reviewer -> curator chain. Single
  additive block only — the strict 1-to-1 mapping, governing-overview-link, and metadata rules are
  unchanged (diff confirms no rule lines touched, verified independently by the doctrine reviewer).
  Doctrine-only change set (60 files: 6 canonical `skills/` edits + 1 new template, each synced to 9
  mirrors, 0 Python); sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/c-05-create-or-update-onboarding-files/SKILL.md`. Verification metadata pinned — no
  commit yet on `ar/260707-hfx-l11-curator-activation` (working-tree change).
- 2026-06-23T22:50+02:00 — Dashboard task 14: documented the worktree pre-write rule for onboarding maintenance: check `worktree_status` and run any needed `worktree_sync` before starting memory entries so onboarding/ledger rows land on the current parent branch. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-10T05:20+02:00 — Issue #56 sub-task 2: added the body-before-metadata lifecycle rules and the `No content impact:` / `No route impact:` reviewed-no-impact marker doctrine (Quick Rule 19 + When-code-changes rules 4-5), matching the new closeout body gates.
- 2026-05-29T20:25+02:00: Reviewed for the act-by-default `dry_run` flip — the `c-05-create-or-update-onboarding-files` skill `route_index_refresh` example now omits `dry_run=false` and notes preview-first (`dry_run=true`).
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-22T16:39+02:00: Updated after `c-05-create-or-update-onboarding-files` skill gained explicit preservation-first handling for renamed, moved, split, merged, relocated, or deleted source behavior. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-22T13:32+02:00: Updated after `c-05-create-or-update-onboarding-files` skill source discovery became provider-neutral while treating live documentation sources named by the resolved registry as authoritative over local caches. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-19T02:45+02:00: Updated for generated route-index `hotPath` fields and the requirement to keep route overview `## Hot Path Summary` sections current before refreshing indexes.
- 2026-05-15T12:57+02:00: Clarified that `c-05-create-or-update-onboarding-files` skill owns entity inventory-to-fingerprint coverage and must verify removed, renamed, or moved entities before deleting stale rows or evidence paths. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T11:46+02:00: Refreshed after `c-05-create-or-update-onboarding-files` skill took ownership of curating and refreshing repo entity `git-blob-set-v1` evidence paths for deterministic `c-02-memory-quality-control` skill checks. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-14T21:38+02:00: Refreshed after the skill frontmatter was tightened to expose file-level/entity maintenance plus `c-03-repo-bootstrap` skill routing for package/module/source-slice changes. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T21:16+02:00: Refreshed for resolved onboarding-root placement and `c-03-repo-bootstrap` skill routing of structural source-slice create, refresh, move, and deletion cleanup cases. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-14T18:00+02:00: Refreshed for route-local governing overview support, self-sufficient file-level onboarding, and reference-bucket requirements. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-05-create-or-update-onboarding-files` name.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` and corrected stale `c-05-create-or-update-onboarding-files` skill routing wording after coordination rename verification.
- 2026-05-09T21:15: Created first file-level onboarding baseline for `c-05-create-or-update-onboarding-files` skill documentation.
