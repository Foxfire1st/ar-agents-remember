# C-04-retrieval-strategy-router/SKILL.md

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember-md                                     |
| path                   | `runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-05-21T04:09+02:00                                 |
| lastVerifiedCommitHash | `0462de46a1da1bf1997e3979f4cc5bc53d1132f6`             |
| lastVerifiedCommitDate | 2026-05-21T08:30:44+02:00|
| governingOverview      | `../../overview.md`                                    |

## Governing Overview

[overview.md](../../overview.md)

## Purpose

C-04 is the retrieval strategy router for context-backed source work. It chooses
between semantic search, relationship graph queries, and intent-oriented
onboarding/source confirmation before reading broadly.

## Code Commentary

### Logic

The skill defines three substrates. `Semantics` is for known concepts with
unknown structure, route, or file location and prefers GrepAI over direct memory
repo search when the provider is available. `Relationship` is for
known anchors with unknown callers, callees, dependencies, ownership, or impact
neighborhoods and prefers CodeGraphContext when the provider is available.
`Intent` is for known anchors or locations where the missing truth is a contract,
invariant, workflow rule, or behavioral reason; it reads onboarding and source
as the proof layer.

Every discovery path produces a candidate packet: question, retrieval contract,
provider status, candidate routes, candidate source anchors, evidence read so
far, rejected routes, and the next confirmation step. GrepAI and CGC output are
candidate discovery only; final claims still require onboarding or source
evidence.

### Conventions

Use GrepAI with the memory repo root as the working directory and a small JSON
result budget:

```bash
cd <coordination_root>/memory-repos
<coordination_root>/providers/_bin/grepai search "<query>" --json --compact --limit 5
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

Relationship probing has a small budget: prefer `find name`, `find pattern`,
`analyze callers`, `calls`, `deps`, `tree`, or `chain`, and switch to Intent
after no more than two CGC probes.

### Invariants And Boundaries

Provider output is never final proof. C-04 must confirm selected candidates with
source and/or verified onboarding before answering. If optional providers are
not available, the skill continues with Intent using route indexes, governing
overviews, sidecars, and bounded source reads. Route indexes remain
availability metadata, not proof: `coveredFiles` means a sidecar exists, while a
source path inside `sourceScope` but absent from `coveredFiles` means skip
sidecar probing and read source first.

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
| C-04 is now named `c-04-retrieval-strategy-router` and frames routing around semantic, relationship, and intent substrates. | L1-L34 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md) |
| Candidate packets record the retrieval contract, provider use or fallback, route/source candidates, and the next source/onboarding confirmation step. | L36-L54 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md) |
| Semantics uses GrepAI as bounded candidate discovery and then switches to Intent for proof. | L56-L90 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md) |
| Relationship uses provider-wrapped `cgc ... run -- <native args>` commands and switches to Intent after a small graph-query budget. | L92-L147 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md) |
| Intent preserves route-index, overview, sidecar, and bounded source confirmation as the proof layer. | L149-L208 | [C-04 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-04-retrieval-strategy-router/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

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
