# skills/c-00-initialize-memory-repo/SKILL.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The canonical initialization skill describes creation or repair of the external repository memory scaffold. It is instruction, not an independent runtime, task, role, or permission authority. It creates no skill folder: the tool server serves the canonical skill tree from its packaged copy.

## Code Commentary

The normal installed input is `repo_id`; a code root is for conceptual review or source debugging. External topology is the only supported topology. `create-missing` is the default; repair requires an explicit request. The foundation branch defaults to the checked-out code branch and the operation refuses rather than inventing a missing branch name. Setup tools apply by default, so the skill calls for a preview before effectful application.

Before creation, the skill asks for the foundation branch, states the exact external memory path and explains the separate repository, its directories, the automatically produced `memory.md` view and baseline/adoption, and deliberate branch migration in plain language. This describes the skill's setup explanation; it does not grant publication, commit, landing, or ledger ownership to the reader.

Initialization owns missing memory scaffolding only. Runtime repair remains with `runtime_install`, whose scaffold carries no skills copy. Skills are never installed as files: the tool server serves the canonical tree from its packaged copy as MCP resources, so an absent `skills/` directory in a harness, project or coordination root is the expected state. `c-03-repo-bootstrap` owns onboarding generation. Existing files are preserved without explicit overwrite approval. The removed repo-local `ar-memory/` layout is reported by exact path with its route out, not read, migrated, deleted, or recreated by this skill. Legacy content without `knowledge/layout.json` is not initialized around: the source names the first-conversion procedure and `legacy-format` refusal before ordinary memory operations resume. Machine policy and path rules belong to memory-layer `system/settings.json`, not coordinator runtime settings or the explanatory Markdown.

## Current Source Qualification

The current source names no skill carrier at all. It states that skills are not installed as files, that the tool server serves the canonical tree from its packaged copy as MCP resources, that the coordination root carries no `skills/` directory, and that root `skills/` is the source repository's authoring source rather than a runtime dependency of a project. The scaffold list it checks therefore omits `skills/`, and an absent skill folder is not a missing-runtime defect. Earlier starter-package, generated-copy and `skills_install` statements below describe superseded distribution, not current capability.

## Retained Prior Commentary And Historical Claims

The following preserves the earlier curated operative account and the original card's commentary. The original card and all four original reference objects, including their old blob/content tuples and notes, are retained in the Wave10 preimage custody receipt. The canonical evidence at the end is freshly authored by the citation owner; old reference numbers are not manually transplanted. Former packaged-copy source-comparison paths are normalized below to the byte-equal canonical source. Superseded manual-tool/default-internal language stays historical and grants no current route or authority.

### Prior Operative Account — MIK-R112

The current source facts below replaced the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures and evidence are retained here as history; they grant no current call, restored route or fresh execution acceptance.

- That repair's source removed the skill-install route and named copied starter packages as the skill carrier; neither carrier exists now, and the current text serves skills from the package instead (see Current Source Qualification).
- Existing legacy content without `knowledge/layout.json` is not initialized around: `memory_init` writes no marker and names the first-conversion procedure. Ordinary unconverted-memory operations refuse with `legacy-format` even if no converted branch exists. Convert first as `c-13-install-and-onboard` and `docs/guides/first-conversion.md` describe, then resume scaffolding; legacy card reads and conversion remain available.

### Superseded Inventory

- Pre-repair card claim: Card reserves skills_install as an available manual/maintenance route. This is superseded archival wording, not a current prescription.
- Pre-repair card claim: Card's default-internal convention also contradicts its external-only source. This is superseded archival wording, not a current prescription.

### Prior Source And Authority Bounds

- Source comparison, now addressed by the canonical twin: `skills/c-00-initialize-memory-repo/SKILL.md:24`.
- Source comparison, now addressed by the canonical twin: `skills/c-00-initialize-memory-repo/SKILL.md:45-51`.
- Source comparison, now addressed by the canonical twin: `skills/c-00-initialize-memory-repo/SKILL.md:109-133`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Historical citation custody may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

### Historical Original Card — Not The Current Operative Account

<details>
<summary>Retained original source accounts and producer history</summary>

#### Purpose

This skill describes memory-root initialization or repair for Agents Remember
target repositories. It no longer owns first-run harness skill exposure; copied
starter packages provide the initial skills and native harness files.

#### Logic

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

#### Conventions — Superseded Wording Retained

Default internal setup is local-first. External-memory setup is explicit and
belongs in the per-repo memory repo under the installed coordination runtime.
The skill does not install runtime files, expose harness skills, create
worktrees, or generate onboarding. Runtime repair is requested through
`runtime_install`; harness skill exposure comes from copied starter packages in
the normal first-run path, with `skills_install` reserved for manual maintenance
or non-package setups.

The default-internal and reserved-manual-tool claims immediately above are the original, explicitly superseded claims; they are not operative instructions.

#### Invariants And Boundaries

`c-00-initialize-memory-repo` skill creates missing memory scaffolding only and must not overwrite existing files without approval. Cross-repo policy and path rules live in the memory-layer `system/settings.json`; coordinator runtime settings are not the authority for one repository's durable memory policy.

#### Todos — Historical

If `c-00-initialize-memory-repo` skill gets an executable helper later, mirror this wording in code and add smoke tests for internal and external-memory scaffold shapes.

The old internal-shape TODO above does not restore the removed topology or authorize new tests; current source remains instruction-only and external-only.

#### Docs References

No external documentation is needed for this repository-local skill.

No relevant external documentation found. The memory source registry has no configured entries; no external domain behavior is asserted by this card.

#### Cross-Repo References

No sibling repository evidence is needed for this skill.

No meaningful cross-repo references found.

</details>

## Evidence

- The skill initializes memory roots, not coordinator runtime assets, skill copies, task worktrees, or onboarding content. The tool server serves the canonical skill tree from its packaged copy, so the skill neither installs skills nor creates a skill folder anywhere; the prior reference's skills_install and starter-package claims are retained above only as superseded history. [1]
- Repo-local ar-memory was removed and is reported by exact path with a route out, rather than created, read, or migrated; external memory resolves under coordination-root/memory-repos after runtime verification. Legacy content without the layout marker is refused, not initialized around. [2]
- Starter settings examples keep storage and path rules under memory-layer system/settings.json and seed common generated/vendor/build/local excludes. [3]
- Common outcomes preserve existing docs, system files, and onboarding content when a partial memory scaffold is repaired. [4]
- Installed inputs, create-missing default, explicit repair, foundation-branch fallback/refusal and preview-before-effectful-apply are separate setup boundaries. [5]
- The foundation-branch question and plain-language explanation precede confirmation; the skill describes the external repository, directories, generated memory.md view, baseline/adoption and deliberate branch migration. [6]
