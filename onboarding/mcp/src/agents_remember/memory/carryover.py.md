# mcp/src/agents_remember/memory/carryover.py

## Governing Overview

[Nearest governing overview](../../../overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Plans and applies evidence-backed onboarding carryover after code lands. Selected memory content
is committed in the exact ordinary recovery leaf and attributed to the selected official code tip.
Integration of that leaf remains a separate operation.

## Code Commentary

### Logic

`CarryoverRequest` owns the plan inputs; `CarryoverApplyOptions` contains the intent, explicit
review selections, and memory message. `CarryoverRefs` keeps the base/source/official comparison
frame constant for a plan, and `MemoryOnlyDoc` carries one memory-only candidate's source and target
paths. The former `TargetLedger` handle and ledger message option are retired.

Planning classifies file sidecars, route overviews, memory-only docs, and entity catalogs. Automatic
carry requires proven evidence; exact-landed evidence requires every relevant source-branch commit
to be an ancestor of the official ref. Review-required candidates must be explicitly selected.

Apply verifies configured repository identity and the exact open external-memory leaf. Its code
base and code HEAD must equal the selected official tip, with a clean code checkout. Target memory
must be clean for actual content; `memory.md` is excluded from that check. Explicit target storage
and path-rule authority is resolved before writes and reused for route-index refresh. Source-memory
settings do not grant target write authority.

Copied sidecars receive the official verification metadata. Entity catalog fingerprints are
recomputed against the official code ref and reported; derived route indexes are regenerated on the
target when its code checkout permits that operation. No carried content or no actual content delta
returns `nothing-to-carryover`, refreshes the cache best effort, and creates no commit.

For changed content, cache preparation runs before the shared Git helper commits with
`exclude_paths=("memory.md",)`. The kernel renderer appends attribution to the caller's memory
message without rewriting its body, including when its last paragraph resembles trailer lines.
The result reports `memory_content_commit` and `ledger_cache`. The old `ledger-mapped-head` path,
ledger-only commit, and duplicate local commit helper no longer exist.

### Conventions

The CLI and MCP remain adapters around typed requests and planning/application services. Git
commands use the shared guarded runner and its `GitRunnerOptions` input-text path for patch IDs.
Content committing and identity setup use the shared Git module. Indexes are regenerated rather
than copied, and default read settings cannot substitute for explicit target write authority.

### Invariants And Boundaries

- Only the exact configured recovery-leaf memory checkout may receive carried content.
- Repository identity, open-leaf state, official code tip, and explicit target settings remain checked.
- A missing or malformed cache does not change candidate evidence or admission.
- Nothing-to-carryover cannot invent attribution for a new code state or create a cache-only commit.
- The real memory commit carries the official tip's attribution; cache rows are derived afterward.
- **Carryover writes legacy-format memory only, and only while the repository is not locked (L37, review R1
  F2).** `_apply_carryover_for_request` calls `_require_legacy_format_target` right after its authority checks,
  before the checkout requirement, the plan and every write. A target whose working tree holds
  `knowledge/layout.json` is refused with `CONVERTED_TARGET`, naming the file writer: carryover copies
  legacy-format Markdown and commits it with no format check and no knowledge validator. An unconverted target
  asks the cutover lock on the configured memory repository and is refused, naming the crossing sync, once that
  repository holds converted memory (MIK-R09 rule 6). `memory_carryover_plan` is a read and is unchanged.
  Carryover stays unavailable on converted lines until it is adapted to converted memory.

### Todos

No new file-local follow-up is established by this documentation pass.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

- Candidate comparison and explicit review selection. [1]
- Apply owns one content commit and preserves exact leaf/repository authority. [2]
- Target storage is established from effective explicit settings. [3]
- Shared committing explicitly excludes the consumer cache. [4]
- The public carryover test preserves the caller body, verifies attribution, and proves no extra repeat commit. [5]

- A converted target is refused, and an unconverted one takes the cutover lock. [6]
- Carryover never writes converted memory and takes the cutover lock. [7]

### Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

No additional configured cross-repository evidence is claimed.
