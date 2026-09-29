# mcp/src/agents_remember/application/worktree_services.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/worktree_services.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f` |
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Builds the default service bundle that lets lower-level worktree operations use provider lifecycle, memory checking, citation guards, Gate-5 rail definitions, the mandatory knowledge validator (with its converted-base converter) and the knowledge crossing without importing those higher-level packages.

## Code Commentary

### Logic

ProviderLifecycleAdapter translates the worktree-owned setup specification into provider-owned requests and delegates setup/status/teardown. MemoryQualityAdapter delegates check-group discovery, drift context and memory checks. CitationGuardAdapter obtains the memory-quality citation cache guard.

CertificationMemoryRailsAdapter delegates the admitted selection id to gate_five_memory_rails. build_default_worktree_services installs this adapter beside the existing three services; the re-exported bind_worktree_services installs the resulting bundle when the MCP/CLI composition calls it.

Since MIK-R22 the default bundle also binds `knowledge_validation=GitKnowledgeValidation()`, imported from `memory_quality.knowledge_validator.commit_route`. It implements `worktrees.services.KnowledgeValidationPort`, so the worktree layer's memory commit routes (today the managed sync's memory merge) can run the validator without importing `memory_quality`.

Since MIK-R24 the validator is bound as `GitKnowledgeValidation(base_converter=GitBaseConverter())`, so a converted merge whose base is unconverted (the far side of a crossing sync) is validated against that base's conversion (rule 7), instead of being refused by rule 6. The bundle also binds `knowledge_crossing=GitKnowledgeCrossing()` (`memory/conversion/crossing_port.py`), which implements `worktrees.services.KnowledgeCrossingPort`: the managed sync plans a crossing sync's structural merge through it (rule 8) without importing `memory.conversion`. Both adapters are inert for a merge in which no tree is converted.

### Conventions

Keep imports of providers and memory_quality at this composition boundary. Worktree modules consume protocols from worktrees.services; they do not locate those packages dynamically or construct fallback implementations.

### Invariants And Boundaries

- The bundle wires dependencies; it does not execute a certification gate by being built.
- Supplying Gate-5 rail definitions does not invoke full memory certification or publish coherence.
- Default composition must bind the rail adapter before the Agents Remember certification-record seam requests it.
- Preserve provider teardown and citation-guard ownership while extending the bundle.
- The knowledge validator and the knowledge crossing are bound here and nowhere else. A process without a bound crossing refuses a crossing sync (`crossing sync step 'convert' failed`); it never merges one as plain Git.
- The knowledge validator is bound here and nowhere else. A process that builds its bundle without it gets a refusal, not a skipped validation, for any converted memory commit.

### Todos

The rail-definition adapter is implemented; the complete R07/R08 production execution path remains a separate integration obligation.

### CCR private preparation boundary

The default application bundle installs `PreparedCloseoutContinuation` and `PreparedMemoryCertificationAdapter` explicitly. This supplies production memory/finalization composition through the existing service ports; binding the adapters neither bypasses certification nor establishes a successful execution.

| Finding | Anchor | Source |
| --- | --- | --- |
| The current `build_default_worktree_services` boundary implements the preparation contract above. | "def build_default_worktree_services" | mcp/src/agents_remember/application/worktree_services.py:203-211 |

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Provider translation/delegation | `ProviderLifecycleAdapter` | mcp/src/agents_remember/application/worktree_services.py:33-139 |
| Memory-rail and memory-quality adapters | `CertificationMemoryRailsAdapter`; `MemoryQualityAdapter` | mcp/src/agents_remember/application/worktree_services.py:140-187 |
| The citation guard delegates terminal namespace protection. | `CitationGuardAdapter` | mcp/src/agents_remember/application/worktree_services.py:188-202 |
| The default bundle composes the declared worktree services, including the knowledge validator with its base converter and the knowledge crossing. | `build_default_worktree_services`; `GitKnowledgeValidation`; `GitBaseConverter`; `GitKnowledgeCrossing` | mcp/src/agents_remember/application/worktree_services.py:208-218; mcp/src/agents_remember/memory_quality/knowledge_validator/commit_route.py:31-80; mcp/src/agents_remember/memory/conversion/base.py:101-139; mcp/src/agents_remember/memory/conversion/crossing_port.py:24-52 |
| The canonical binding owner installs the explicit service bundle. | `bind_worktree_services` | mcp/src/agents_remember/worktrees/services.py:181-184 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): Body updated for MIK-R24. The validator is now bound with `base_converter=GitBaseConverter()` (rule 7), and the bundle binds `knowledge_crossing=GitKnowledgeCrossing()` (rule 8). The Purpose, the Logic paragraph and the invariants say so, including that an unbound crossing refuses and never merges as plain Git. The bundle row was re-measured and now cites the two new adapters.

- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): documented the MIK-R22 binding of `GitKnowledgeValidation` in `build_default_worktree_services` and its boundary (bound only here; an unbound validator refuses a converted memory commit). Re-measured the bundle row after the three-line import insertion. The verification stamp is unchanged; closeout owns it.

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the
  prepared-certification adapter import moved to the closeout plane. Re-read every cited range
  against the frozen source: the adapter and bundle ranges hold as the earlier entry records, and no
  claim names the moved module. No wording changed. Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/application/worktree_services.py` changed since the recorded verification
  commit. Re-read the card against the frozen on-disk source and re-checked its claims and cited
  ranges: nothing this card asserts is falsified by the change, so no wording changed. Verification
  metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved the
  prepared-certification adapter import to the closeout plane. Re-derived the adapter and bundle
  ranges against the current source (they were offset before this diff as well); no claim text
  changed. Verification metadata remains closeout-owned.
- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=179eb40af2203494e4402efc7bf9c478d044c3199ce787062c6f7a990eff576e; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-06T23:07:14+00:00 — History-format repair at the actual recorded repair time. The earlier reconciliation note recorded only a local calendar date; its time of day is unknown. Original note preserved verbatim: "- 2026-09-07 — Reconciled the preparation contract introduced by 245057 against surviving d361 source; retained prior history and verification pins."


- 2026-09-05T06:14:14+00:00 — Extended the preserved dependency-composition account with the Gate-5 rail port and its non-execution boundary.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the composition-root services
  bundle. Verification metadata pinned until closeout stamps the L9 code commit.
