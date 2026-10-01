# c-00-initialize-memory-repo/SKILL.md

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
packages already carry harness-visible skills. `external` is the **only supported
topology**: it creates or repairs `<coordination-root>/memory-repos/ar-<repo-name>/`
after verifying the coordinator runtime has already been installed. Repo-local
internal memory under `<code-repository-root>/ar-memory/` was **removed from the
product** and is reported by its exact path with the route out rather than created
or migrated. It creates missing `system/`,
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

No relevant external documentation found.

## Evidence

### Repo-Internal References

- `c-00-initialize-memory-repo` skill initializes memory roots, not coordinator runtime assets, harness skills, task worktrees, or onboarding content; package-based first-run setup gets harness skills from copied starter packages and uses `skills_install` only for maintenance/manual paths. [1]
- Repo-local `ar-memory/` **was removed from the product** and is now reported by its exact path with the route out rather than created, read or migrated; explicit external memory resolves to `ar-coordination/memory-repos/ar-<repo>/` after runtime install is verified, and `external` is the only supported topology. [2]
- Starter settings examples keep storage and path rules under memory-layer `system/settings.json` and seed common generated/vendor/build/local excludes. [3]
- Common outcomes preserve existing docs, system files, and onboarding content when a partial memory scaffold is repaired. [4]

### Cross-Repo References

No sibling repository evidence is needed for this skill.

No meaningful cross-repo references found.
