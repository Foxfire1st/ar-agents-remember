# README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/README.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T03:30+02:00                     |
| lastVerifiedCommitHash | `dc25f5a63de359926985c925096aad9019968bf4` |
| lastVerifiedCommitDate | 2026-06-02T18:31:01+02:00|

## Purpose

`mcp/src/agents_remember/package_data/runtime/system/defaults/examples/README.md` explains why system examples are split into target-shaped folders instead of encoded through file names.

## Code Commentary

### Logic

The file defines two example targets: `examples/coordinator/` for workspace-wide
coordinator files and `examples/memory-repo/` for repository-specific
memory-layer files. It states that coordinator files can define global defaults
but should not encode one-repository rules, while memory-layer rules win for
their own repository. It also notes that the memory-repo examples include a
`git-workflow.md` landing-flow starter (for repos that land through a gated
branch) and a code quality report template for implementation validation summaries.

### Conventions

Examples are arranged by destination folder shape so users can copy a whole directory and preserve normal target file names such as `AGENTS.md`, `settings.md`, and `tools.md`.

### Invariants And Boundaries

Coordinator guidance is global by default; memory-repo guidance is more
specific and overrides it for the target code repository. The packaged report
template is example scaffolding and should be adapted to the target
repository's actual quality tools.

### Todos

None.

### Docs References

No external documentation is needed for this example index.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The source file itself is the active example index.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The README states that examples are split by target folder rather than by inferred ownership from file names. | L1-L4 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/README.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/README.md) |
| The README defines coordinator examples as workspace-wide/global, memory-repo examples as repository-specific, and names the memory-repo `git-workflow.md` landing-flow starter and quality-report template. | L8-L34 | [mcp/src/agents_remember/package_data/runtime/system/defaults/examples/README.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/README.md) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-02T16:24+02:00: Normalized skill references in the example coordinator README to full lowercase skill ids plus the word "skill" (was abbreviated, e.g. C-08). Reference-style normalization; example guidance unchanged.
- 2026-06-02T03:30+02:00: Documented the new memory-repo `git-workflow.md` example (gated-branch landing flow) alongside the code-quality report template (mcp 1.0.2). Verification metadata pinned until closeout.
- 2026-05-28T12:32+02:00: Updated after the examples index began mentioning the memory-repo code quality report template.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-13T13:38: Created onboarding for the folder-shaped system examples index.
