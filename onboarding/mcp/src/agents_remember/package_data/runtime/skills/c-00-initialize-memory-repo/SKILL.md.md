# c-00-initialize-memory-repo/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-00-initialize-memory-repo/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T11:30+02:00                     |
| lastVerifiedCommitHash | `dc25f5a63de359926985c925096aad9019968bf4` |
| lastVerifiedCommitDate | 2026-06-02T18:31:01+02:00|

## Purpose

This skill describes first-run memory-root initialization for Agents Remember target repositories.

## Code Commentary

### Logic

The skill now owns only memory-root scaffolding. It defaults to internal memory under `<code-repository-root>/ar-memory/`; when the developer explicitly chooses external memory, it creates or repairs `<coordination-root>/memory-repos/ar-<repo-name>/` after verifying the coordinator runtime has already been installed. It creates missing `system/`, `onboarding/`, and `docs/` directories plus starter `settings.md`, `settings.json`, `sources.md`, and `tools.md` files, adding `docs/.gitkeep` for empty external memory repos so the scaffold can be committed. It leaves `onboarding/` empty so `c-03-repo-bootstrap` skill can own generated onboarding content.

### Conventions

Default internal setup is local-first. External-memory setup is explicit and belongs in the per-repo memory repo under the installed coordination runtime. The skill does not install runtime files, expose harness skills, create worktrees, or generate onboarding. Runtime and harness skill installation are requested through `runtime_install` MCP tool and `skills_install`.

### Invariants And Boundaries

`c-00-initialize-memory-repo` skill creates missing memory scaffolding only and must not overwrite existing files without approval. Cross-repo policy and path rules live in the memory-layer `system/settings.json`; coordinator runtime settings are not the authority for one repository's durable memory policy.

### Todos

If `c-00-initialize-memory-repo` skill gets an executable helper later, mirror this wording in code and add smoke tests for internal and external-memory scaffold shapes.

### Docs References

No external documentation is needed for this repository-local skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `c-00-initialize-memory-repo` skill initializes memory roots, not coordinator runtime assets, and leaves onboarding content to `c-03-repo-bootstrap` skill. | L8-L12; L23-L30 | [`c-00-initialize-memory-repo` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-00-initialize-memory-repo/SKILL.md) |
| Internal memory resolves to repo-local `ar-memory/`; explicit external memory resolves to `ar-coordination/memory-repos/ar-<repo>/` after runtime install is verified. | L35-L64 | [`c-00-initialize-memory-repo` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-00-initialize-memory-repo/SKILL.md) |
| Starter settings examples keep storage and path rules under memory-layer `system/settings.json` and seed common generated/vendor/build/local excludes. | L121-L214 | [`c-00-initialize-memory-repo` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-00-initialize-memory-repo/SKILL.md) |
| Common outcomes preserve existing docs, system files, and onboarding content when a partial memory scaffold is repaired. | L262-L276 | [`c-00-initialize-memory-repo` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-00-initialize-memory-repo/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-02T11:30+02:00: Dropped the removed `layout="tree"` argument from the `c-00-initialize-memory-repo` skill setup-example `skills_install` call (the `layout` input was removed in 2.0.0; the installer is always flat). Example-only correction, in place at L35 — documented behavior and citations unchanged. Verification metadata stays pinned until closeout. docs/hn-launch-hardening branch.
- 2026-05-29T20:25+02:00: Reviewed for the act-by-default `dry_run` flip — `c-00-initialize-memory-repo` skill setup-tool examples now model preview-first then apply for `memory_init`/`runtime_install`/`skills_install`.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-23T14:20+02:00: Updated setup guidance to request `runtime_install` MCP tool and `skills_install` instead of deleted source-side installer scripts.
- 2026-05-15T03:30+02:00: Renamed `c-00-initialize-memory-repo` skill to initialize memory repo and narrowed the skill boundary to memory-root initialization.
- 2026-05-14T21:38+02:00: Refreshed after `c-00-initialize-memory-repo` skill starter `settings.json` snippets gained the standard path-rule exclusion baseline. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T18:51+02:00: Updated after the skill frontmatter moved to a lowercase skill name and explicit external-memory scaffolding stopped treating `.env.example` as runtime input.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-09T22:57: Refreshed verification metadata and replaced design-spec-only evidence with current skill citations.
- 2026-05-09T21:59: Created onboarding after `c-00-initialize-memory-repo` skill was aligned to the ar-memory memory-root model.
