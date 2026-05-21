# C-04-retrieval-strategy-router/SKILL.md

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember-md                                     |
| path                   | `runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-21T16:14+02:00                                 |
| lastVerifiedCommitHash | `00aae9dad3d8740e10a41ab285f87ecab8608745`             |
| lastVerifiedCommitDate | 2026-05-21T23:53:08+02:00|
| governingOverview      | `../../overview.md`                                    |

## Governing Overview

[overview.md](../../overview.md)

## Purpose

C-04 is the retrieval strategy router for context-backed source work. It chooses
between semantic search, relationship graph queries, and intent-oriented
onboarding/source confirmation before broad source reads.

## Code Commentary

### Logic

The skill defines three retrieval substrates. `Semantics` is for fuzzy concepts
whose route, structure, or source location is unknown and prefers GrepAI over
direct memory repo search when available. `Relationship` is for known anchors
whose callers, callees, dependencies, ownership, inheritance, or impact
neighborhoods are unknown and prefers CodeGraphContext when available. `Intent`
is for known anchors or locations where the missing truth is a contract,
invariant, branch-valid behavior, or fix direction; it uses onboarding plus
bounded source confirmation as the proof layer.

The Semantics section now teaches GrepAI through the lifecycle-managed
`grepai run -- ...` wrapper rather than a global user config. It shows two
high-value synthetic response shapes: broad semantic routing with
`--toon --compact`, and scoped memory-project search with compact JSON anchors.
It links to the sibling `grepai-high-leverage-usage.md` catalog for the full
GrepAI command selection notes and synthetic example outputs.

The Relationship section teaches CGC as a structural tool rather than a
file-line locator. It keeps the basic provider-wrapped `find name` and
`analyze callers` commands, then shows two high-value synthetic response shapes:
`analyze calls` for downstream impact tracing and `analyze complexity` for risk
triage. The examples deliberately use placeholder repo ids, symbols, and paths
so reusable docs do not expose private project code. The skill links to the
sibling `codegraphcontext-high-level-methods.md` catalog for the full command
set and synthetic example outputs.

### Conventions

Use GrepAI through the provider lifecycle wrapper so native search receives the
provider-owned workspace environment:

```bash
python <coordination_root>/scripts/provider-lifecycle.py grepai \
  --coordination-root <coordination_root> \
  --json \
  run -- search "<query>" \
  --workspace <workspace> --toon --compact --limit 5
```

Use the provider lifecycle wrapper for CGC queries so native CGC commands run
with the managed FalkorDB-backed provider environment:

```bash
python <coordination_root>/scripts/provider-lifecycle.py cgc \
  --coordination-root <coordination_root> \
  --repo-id <repoId> \
  --json \
  run -- find name <anchor>
```

After a CGC locator query, prefer `analyze calls`, `callers`, `chain`, `deps`,
`tree`, `complexity`, `dead-code`, `overrides`, or `variable` for structure.
Treat CGC output as discovery and confirm selected anchors with bounded source
reads before editing.

### Invariants And Boundaries

Provider output is never final proof. C-04 must confirm selected candidates with
source and/or verified onboarding before answering or editing. If optional
providers are not available, the skill continues with Intent using route
indexes, governing overviews, sidecars, and bounded source reads. Route indexes
remain availability metadata, not proof: `coveredFiles` means a sidecar exists,
while a source path inside `sourceScope` but absent from `coveredFiles` means
skip sidecar probing and read source first.

The skill does not check, install, repair, or reindex providers.

### Todos

None.

## Docs References

No external documentation is cited here. The skill is a repository-local
retrieval contract over installed provider tooling and durable onboarding.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| C-04 defines Semantics, Relationship, and Intent as the three retrieval substrates and describes when to chain them. | L8-L28 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md) |
| Semantics uses the lifecycle-managed GrepAI wrapper with provider-owned environment, then shows synthetic broad semantic routing and scoped memory-project search examples. | L30-L103 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md) |
| Relationship uses the managed CGC wrapper and includes synthetic `analyze calls` and `analyze complexity` examples with sample response shapes. | L105-L172 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md) |
| The inline GrepAI and CGC examples explicitly forbid copying private repository names, symbols, paths, snippets, or results into reusable skill examples. | L51-L54; L125-L127 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md) |
| The skill points agents to `grepai-high-leverage-usage.md` and `codegraphcontext-high-level-methods.md` for full provider usage catalogs and synthetic example outputs. | L100-L103; L168-L172 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md) |
| Intent preserves route-index, overview, sidecar, and bounded source confirmation as the proof layer after discovery. | L179-L213 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md) |
| The sibling GrepAI catalog covers managed invocation, command selection, broad search, project-scoped search, route-scoped snippet search, trace caveats, status, and practical rules using synthetic examples only. | L1-L236 | [grepai-high-leverage-usage.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/grepai-high-leverage-usage.md) |
| The sibling CGC catalog explains all high-level `cgc analyze` methods and practical selection rules with synthetic examples only. | L1-L38, L321-L332 | [codegraphcontext-high-level-methods.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md) |

## Cross-Repo References

The CGC examples in the source docs are synthetic response-shape illustrations.
They do not contain private sibling repository names, symbols, paths, or code.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No source-code contract is imported from a sibling repository. | n/a | n/a |

## Update History

- 2026-05-21T23:55+02:00: Switched GrepAI examples from bare binary/environment setup to `provider-lifecycle.py grepai run -- ...`.
- 2026-05-21T16:14+02:00: Added GrepAI high-leverage usage examples, runtime-owned invocation guidance, and a link to the sibling GrepAI catalog.
- 2026-05-21T15:20+02:00: Replaced private-project CGC examples with synthetic response-shape examples and made `analyze complexity` the second inline high-value pattern.
- 2026-05-21T14:10+02:00: Added CGC high-level method examples to the skill, linked the sibling catalog, and refreshed this sidecar to match the current compact skill.
- 2026-05-21T04:09+02:00: Removed provider lifecycle wording from C-04.
- 2026-05-21T03:05+02:00: Rewrote onboarding for the C-04 retrieval strategy router, including GrepAI Semantics, CodeGraphContext Relationship, Intent proof, and candidate packets.
- 2026-05-19T04:05+02:00: Clarified that the 80-line confirmation output budget requires shell-level output caps and that `rg -m` alone is not enough across many files. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-19T03:58+02:00: Added a general confirmation command-output budget and triage-scope limit so C-04 does not enter implementation-mechanism search unless the prompt asks for it. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-19T03:40+02:00: Tightened bounded confirmation with filename-first narrowing, route-overview fallback rules, and a hard stop once source evidence is sufficient. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-19T03:12+02:00: Changed fast discovery to read root `overview.index.json` before root `overview.md`, making full root overview prose a fallback when the index is insufficient.
- 2026-05-19T02:45+02:00: Added route-index `hotPath` consumption so discovery can use generated summary, candidate hints, and source-anchor hints before reading full overview prose.
- 2026-05-19T02:21+02:00: Added the generalized source-anchor narrowing step before confirmation-mode `rg`, so route labels and broad domain terms are not reused as source queries after they already selected the route.
- 2026-05-19T02:03+02:00: Clarified that missing sidecars or sparse memory are not packet failures; they stay in bounded source confirmation and use targeted source reads/searches.
- 2026-05-19T01:50+02:00: Condensed the source skill to 98 lines and corrected the bounded confirmation handoff so it consumes the discovery candidate packet instead of replaying overview/index reads.
- 2026-05-19T01:37+02:00: Replaced the normal `deterministic-walkthrough` handoff with `bounded-source-confirmation`.
- 2026-05-19T01:11+02:00: Split read behavior into `fast-memory-discovery` and `deterministic-walkthrough` modes.
- 2026-05-18T21:44+02:00: Created onboarding for the renamed and hardened C-04 onboarding read-mode skill after pulling `origin/main`.
