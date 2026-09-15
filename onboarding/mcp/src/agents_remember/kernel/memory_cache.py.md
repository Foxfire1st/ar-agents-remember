# mcp/src/agents_remember/kernel/memory_cache.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/memory_cache.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:02 |
| lastVerifiedCommitHash |  `7cbda30d9a9a4c2944382fbef46ac58b85329935`|
| lastVerifiedCommitDate |  2026-09-15T05:15:42+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[Nearest governing overview](../../../overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
This new source file has no committed version yet, so the verification commit fields are deliberately empty; no future hash is invented.

## Purpose

Owns derivation and materialization of the disposable consumer ledger. Its rows and revision
metadata come from committed memory attribution; cache files do not become Git-operation authority.

## Code Commentary

### Logic

`derive_memory_ledger(repository, tip="HEAD", *, repo_name=None)` walks committed attribution and
maps it to newest-first rows. The first row supplies the current code/memory pair and the oldest row
supplies the base pair. A history with no attribution yields empty rows and empty revision fields.
This read never consults `memory.md`.

`prepare_memory_cache` is an explicit preparation helper for an already authorized memory-content
workflow. It adds the root cache ignore rule and removes the cache from the current Git index while
retaining the disk file. That housekeeping belongs to ordinary content staging; the helper does not
create a commit, select a publication ref, or decide whether a Git transaction may proceed.

`refresh_memory_cache` derives the representation and compares it with current bytes before writing
through the shared atomic-text writer. Existing cache read failure is treated as missing prior
bytes. The result reports `updated` or `current`, the path and row count; derivation/serialization or
write failures report `unavailable` with a reason. Those cache outcomes do not determine whether an
already completed Git action succeeded.

### Conventions

Callers own repository/path authority and decide when to prepare or refresh. Use derivation for a
read-only view, preparation inside an owned staging workflow, and best-effort refresh after actual
memory output. The kernel ledger module owns the representation and root-cache filename.

### Invariants And Boundaries

- No cached row, header, or blob contributes attribution.
- Empty derived history is valid and contains no fabricated pair.
- Cache materialization creates no ledger-only commit and moves no ref.
- Preparation is an explicit index/ignore-file mutation, not a read-only status operation.
- A cache failure is reported as cache availability, not promoted into transaction authority.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Derivation reads Git attribution and computes current/base metadata. | L22-L41 | [mcp/src/agents_remember/kernel/memory_cache.py](mcp/src/agents_remember/kernel/memory_cache.py) |
| Preparation excludes the cache and refresh reports materialization outcomes. | L44-L62; L65-L91 | [mcp/src/agents_remember/kernel/memory_cache.py](mcp/src/agents_remember/kernel/memory_cache.py) |
| Committed attribution and row mapping have one reader. | L143-L174; L208-L227 | [mcp/src/agents_remember/kernel/memory_attribution.py](mcp/src/agents_remember/kernel/memory_attribution.py) |
| The consumer representation supports empty derived history. | L173-L184; L187-L212 | [mcp/src/agents_remember/kernel/memory_ledger.py](mcp/src/agents_remember/kernel/memory_ledger.py) |
| Cache independence and exact local-ref derivation are exercised by the retained projection tests. | L338-L360 | [mcp/tests/test_memory_ledger.py](mcp/tests/test_memory_ledger.py) |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History

- 2026-09-15T01:02 UTC — Created the paired sidecar for the new computed-cache owner, documenting derivation, explicit staging preparation, best-effort materialization, and the absence of ledger commit/ref authority. Working candidate verified by source inspection; commit metadata records real committed history only.
