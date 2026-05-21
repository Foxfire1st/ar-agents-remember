# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/agents-md-files/coordinator/AGENTS.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-21T04:09+02:00                     |
| lastVerifiedCommitHash | `0462de46a1da1bf1997e3979f4cc5bc53d1132f6` |
| lastVerifiedCommitDate | 2026-05-21T08:30:44+02:00|

## Purpose

This file is the package-owned template for the installed coordinator root
`AGENTS.md`. It is intended to land at `ar-coordination/AGENTS.md` after the
runtime package is installed.

## Code Commentary

### Logic

The template combines the checkout's task-format routing with coordinator
runtime guidance. It requires agents to choose Chat, W-02, or W-01 before
changing code, points agents to the sibling installed `system/`, `tasks/`, and
`skills/` `AGENTS.md` files when those scopes become relevant, resolves active
repository context with C-08 before trusting memory or task surfaces, checks
configured providers after C-08 resolves the target coordination root, and uses
coordinator `system/*` files for workspace-wide defaults. It also routes
important developer clarifications through
`C-01-findings-capture` and requires
verification against code reality before onboarding propagation through C-05.
The context retrieval path is routed at the coordinator entrypoint: source work
that relies on onboarding, providers, or repository source goes through
`C-04-retrieval-strategy-router`, which owns Semantics, Relationship, and Intent
routing across optional providers, route indexes, onboarding, and bounded source
confirmation. The memory-layer read path is also explicit: memory repos are not
expected to provide a root-level `AGENTS.md`; repo-specific guidance is read
from `system/settings.md`, `system/tools.md`, `system/sources.md`, and optional
`system/coding-guidelines.md`.

### Conventions

The coordinator root is a workspace-wide default layer. It may direct agents to
global settings, tools, sources, companion installed `AGENTS.md` files, and
durable clarification capture, but repository-specific rules belong in the
resolved memory layer. Memory-layer `system/*` files are listed as read-first
surfaces once C-08 identifies the target repository. Provider readiness is
checked only when enabled `contextProviders` are configured in coordinator
settings. The coordinator names C-04 as the retrieval strategy owner instead of duplicating
provider, source, and onboarding ordering rules inline.

### Invariants And Boundaries

The installed coordinator root template must not become a per-repository policy
file, and it must not imply that memory repos need their own root `AGENTS.md`.
Developer clarifications must not be copied into onboarding verbatim; code
reality mismatches are surfaced before propagation. Configured provider readiness
is checked after C-08.
C-04 owns retrieval strategy and source/onboarding confirmation after the
relevant repository context is known. The template
also preserves workflow approval boundaries by forbidding protected branch
movement and worktree lifecycle operations unless the selected workflow has
granted the required approvals.

### Todos

None.

### Docs References

No external documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

This onboarding is backed by the source template itself.

| Finding                                                                                                                       | Citations | Source Path |
| ----------------------------------------------------------------------------------------------------------------------------- | --------- | ----------- |
| The template installs the same Chat/W-02/W-01 routing and workflow-before-code rule expected at a coordinator root.           | L3-L24    | [runtime/agents-md-files/coordinator/AGENTS.md](agents-remember-md/runtime/agents-md-files/coordinator/AGENTS.md) |
| The installed `AGENTS.md` routing section tells agents when to read sibling `tasks/AGENTS.md` instructions. | L28-L38   | [runtime/agents-md-files/coordinator/AGENTS.md](agents-remember-md/runtime/agents-md-files/coordinator/AGENTS.md) |
| The onboarding section routes context-backed source reading to `C-04-retrieval-strategy-router`, which owns Semantics, Relationship, and Intent routing across providers, route indexes, onboarding, and bounded source confirmation. | L40-L49 | [runtime/agents-md-files/coordinator/AGENTS.md](agents-remember-md/runtime/agents-md-files/coordinator/AGENTS.md) |
| The developer-clarification section routes important clarifications through C-01/C-05 only after code-reality checks. | L50-L60 | [runtime/agents-md-files/coordinator/AGENTS.md](agents-remember-md/runtime/agents-md-files/coordinator/AGENTS.md) |
| The resolver section requires C-08 before relying on memory/task surfaces, then checks provider readiness when `contextProviders` are enabled in coordinator settings. | L65-L78 | [runtime/agents-md-files/coordinator/AGENTS.md](agents-remember-md/runtime/agents-md-files/coordinator/AGENTS.md) |
| Memory-layer routing sends repository-specific guidance to memory-layer `system/*` files after C-08 resolves `memory_root`. | L79-L102 | [runtime/agents-md-files/coordinator/AGENTS.md](agents-remember-md/runtime/agents-md-files/coordinator/AGENTS.md) |
| Branch/worktree approval boundaries and memory-layer authority remain listed in the template. | L104-L120   | [runtime/agents-md-files/coordinator/AGENTS.md](agents-remember-md/runtime/agents-md-files/coordinator/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed for this package template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-21T04:09+02:00: Added the configured-provider readiness check after C-08 in the coordinator root template.
- 2026-05-21T03:05+02:00: Updated coordinator routing so C-04 owns retrieval strategy across GrepAI Semantics, CGC Relationship, and Intent proof.
- 2026-05-18T21:44+02:00: Refreshed after pulling the committed C-04 onboarding read-mode rename from `origin/main`.
- 2026-05-18T21:38+02:00: Refreshed against the current committed coordinator template, removing unlanded C-04 read-mode wording and updating verification metadata.
- 2026-05-18T17:03+02:00: Updated the coordinator onboarding to route onboarding-backed source reading to `C-04-retrieval-strategy-router` instead of duplicating the sidecar lookup and fallback-search protocol inline.
- 2026-05-18T14:09+02:00: Added coordinator-entrypoint guidance for deterministic sidecar lookup and made broad onboarding `rg`/`find` fallback-only discovery after direct sidecar plus governing overview reads. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-15T15:08+02:00: Added installed `AGENTS.md` routing guidance and developer clarification capture rules that require C-01, developer approval for onboarding documentation, and code-reality checks before C-05 propagation.
- 2026-05-15T04:23+02:00: Removed the optional memory-repo `AGENTS.md` lookup from the coordinator template and documented `system/*` files as the memory guidance surface.
- 2026-05-15T00:38+02:00: Refreshed after the coordinator template became one of four runtime `AGENTS.md` templates and absorbed the checkout task routing plus coordinator and memory-layer guidance. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-13T19:11: Created onboarding for the coordinator AGENTS.md install template.
