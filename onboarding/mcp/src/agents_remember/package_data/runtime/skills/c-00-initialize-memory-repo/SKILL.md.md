# c-00-initialize-memory-repo/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-00-initialize-memory-repo/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-03T18:58+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|

## Purpose

This skill describes memory-root initialization or repair for Agents Remember
target repositories. It no longer owns first-run harness skill exposure; copied
starter packages provide the initial skills and native harness files.

## Code Commentary

### Logic

The skill owns only memory-root scaffolding through MCP `memory_init`. It does
not install the coordinator runtime, expose harness skills, create task
worktrees, or generate onboarding content. If the coordinator runtime scaffold is
missing or stale, it requests `runtime_install`; it explicitly avoids
`skills_install` in the package-based first-run path because copied starter
packages already carry harness-visible skills. It defaults to internal memory
under `<code-repository-root>/ar-memory/`; when the developer explicitly chooses
external memory, it creates or repairs
`<coordination-root>/memory-repos/ar-<repo-name>/` after verifying the
coordinator runtime has already been installed. It creates missing `system/`,
`onboarding/`, and `docs/` directories plus starter `settings.md`,
`settings.json`, `sources.md`, and `tools.md` files, adding `docs/.gitkeep` for
empty external memory repos so the scaffold can be committed. It leaves
`onboarding/` empty so `c-03-repo-bootstrap` skill can own generated onboarding
content.

### Conventions

Default internal setup is local-first. External-memory setup is explicit and
belongs in the per-repo memory repo under the installed coordination runtime.
The skill does not install runtime files, expose harness skills, create
worktrees, or generate onboarding. Runtime repair is requested through
`runtime_install`; harness skill exposure comes from copied starter packages in
the normal first-run path, with `skills_install` reserved for manual maintenance
or non-package setups.

### Invariants And Boundaries

`c-00-initialize-memory-repo` skill creates missing memory scaffolding only and must not overwrite existing files without approval. Cross-repo policy and path rules live in the memory-layer `system/settings.json`; coordinator runtime settings are not the authority for one repository's durable memory policy.

### Todos

If `c-00-initialize-memory-repo` skill gets an executable helper later, mirror this wording in code and add smoke tests for internal and external-memory scaffold shapes.

### Docs References

No external documentation is needed for this repository-local skill.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `c-00-initialize-memory-repo` skill initializes memory roots, not coordinator runtime assets, harness skills, task worktrees, or onboarding content; package-based first-run setup gets harness skills from copied starter packages and uses `skills_install` only for maintenance/manual paths. | `skills_install` | mcp/src/agents_remember/package_data/runtime/skills/c-00-initialize-memory-repo/SKILL.md:45-46 |
| Internal memory resolves to repo-local `ar-memory/`; explicit external memory resolves to `ar-coordination/memory-repos/ar-<repo>/` after runtime install is verified. | "<code_repository_root>/ar-memory" | mcp/src/agents_remember/package_data/runtime/skills/c-00-initialize-memory-repo/SKILL.md:68-68 |
| Starter settings examples keep storage and path rules under memory-layer `system/settings.json` and seed common generated/vendor/build/local excludes. | "Machine-readable storage" | mcp/src/agents_remember/package_data/runtime/skills/c-00-initialize-memory-repo/SKILL.md:150-150 |
| Common outcomes preserve existing docs, system files, and onboarding content when a partial memory scaffold is repaired. | "Preserve existing" | mcp/src/agents_remember/package_data/runtime/skills/c-00-initialize-memory-repo/SKILL.md:314-314 |

## Cross-Repo References

No sibling repository evidence is needed for this skill.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 6 initial citation findings (3 anchor, 0 prose, 3 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-06-03T18:58+02:00: Updated for package-first first-run setup: this skill initializes or repairs memory roots only, requests `runtime_install` only for missing/stale coordinator scaffold, and leaves initial harness skills/files to copied starter packages; `skills_install` is maintenance/manual. Verification metadata stays pinned until closeout.
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
