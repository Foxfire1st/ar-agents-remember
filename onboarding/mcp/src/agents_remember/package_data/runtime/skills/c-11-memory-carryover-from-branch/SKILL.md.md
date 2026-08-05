# c-11-memory-carryover-from-branch/SKILL.md

| Field                  | Value                                                                |
| ---------------------- | -------------------------------------------------------------------- |
| repository             | agents-remember                                                   |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-11-memory-carryover-from-branch/SKILL.md` |
| doc_type               | `file-level-onboarding`                                              |
| lastUpdated            | 2026-06-10T10:26+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`                           |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|

## Purpose

This skill documents `c-11-memory-carryover-from-branch` skill, the selective memory carryover workflow for protected-branch environments where a developer has richer memory on another source branch but official code receives delayed batched merges.

## Code Commentary

### Logic

The skill defines `c-11-memory-carryover-from-branch` skill as a memory reconciliation step rather than a normal Git merge. It tells agents to use the `memory_carryover_plan` MCP tool first, review the candidate report, and use `memory_carryover_apply` only with explicit intent. The contract names the five relevant branch roles: official code, source branch code, official memory, source branch memory, and old base. It defines evidence tiers from strongest to weakest, with only exact landed commits, patch-id matches, and final content matches becoming auto-carry candidates by default.

Since GitHub #54 the Output States section also documents `ledger-mapped-head`
(an unmapped official code HEAD — e.g. a PR merge commit — mapped to the
current memory content commit) and the `memory_main_advance` block every apply
reports: memory `main` is fast-forwarded to the official checkout tip after
the carryover commits (states `fast-forwarded` / `already-current` /
`diverged` / `failed` / `skipped`), with a note to push memory `main` per the
repo's git workflow on developer approval.

The Candidate Kinds section (carryover artifact coverage, 2.9.0) names the
four kinds and their `include_review_required` selection keys: `file-sidecar`
(source path), `route-overview` (normalized route), `memory-only-doc` (source
path or route, for docs changed only in branch memory), and `entity-catalog`
(the literal `entity-catalog`; always review-required when differing, with
fingerprints recomputed against the official ref on apply and reported as
`entity_fingerprint_validation`). The `exact-landed-commit` tier wording now
matches the implementation: EVERY source-branch commit touching the path must
have landed.

### Conventions

`c-11-memory-carryover-from-branch` skill output is state-oriented and JSON-friendly. Same-path overlap is intentionally review-required because the official branch may contain another developer's independent change. The skill keeps `--replace-existing` and explicit review-required inclusion as opt-in choices for overwriting different official onboarding content.

### Invariants And Boundaries

`c-11-memory-carryover-from-branch` skill must not copy source branch memory for code that did not land, must not copy source branch ledger rows wholesale, and must refresh carried onboarding verification metadata to the official code commit. `c-02-memory-quality-control` skill remains the accuracy check for the current branch; `c-11-memory-carryover-from-branch` skill only imports richer memory whose source-code validity is proven or explicitly reviewed.

### Todos

Future versions can add structural onboarding merges after the first whole-file carryover path has enough real-world usage.

### Docs References

No external documentation is needed for this repository-local workflow skill.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The skill defines the source-branch-to-official memory carryover use case, command shape, evidence tiers, output states, and boundaries. | `# c-11-memory-carryover-from-branch Memory Carryover From Branch` | mcp/src/agents_remember/package_data/runtime/skills/c-11-memory-carryover-from-branch/SKILL.md:6-76 |
| The package carryover service implements the plan/apply behavior described by this skill. | `build_plan_for_request`; `apply_carryover_for_request` | mcp/src/agents_remember/memory/carryover.py:541-614; mcp/src/agents_remember/memory/carryover.py:776-862 |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-11T15:05+02:00 — The skill doc gained a Candidate Kinds section (file-sidecar, route-overview, memory-only-doc, entity-catalog with selection keys), memory-only evidence values, the `entity_fingerprint_validation` output field, and the corrected `exact-landed-commit` wording (EVERY touching commit must have landed, not at least one).
- 2026-06-10T10:26+02:00 — GitHub #54: documented the `ledger-mapped-head` output state and the `memory_main_advance` block (carryover fast-forwards memory main to the official checkout tip; push on developer approval).
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-23T17:50+02:00: Updated implementation reference after the carryover script route was removed from the skill tree and the MCP package became the only implementation route.
- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-11-memory-carryover-from-branch` name.
- 2026-05-11T19:42: Refreshed verification metadata to `aa85d3862bf21fed791e3170e6957f9288c319e8` and replaced placeholder citations with current source line ranges.
- 2026-05-11T18:34: Updated after `c-11-memory-carryover-from-branch` skill command examples adopted `--code-repository-root` and `--code-repository-name`.
- 2026-05-11T03:00: Created onboarding for the new `c-11-memory-carryover-from-branch` skill memory carryover skill and generalized it from workbench-only to source-branch carryover.
