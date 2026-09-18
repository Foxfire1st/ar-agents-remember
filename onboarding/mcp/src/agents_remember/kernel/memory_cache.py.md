# mcp/src/agents_remember/kernel/memory_cache.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/memory_cache.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:02 |
| lastVerifiedCommitHash |  `ea9cf0abeab4fe88961bda10b4f54d30266a9634`|
| lastVerifiedCommitDate |  2026-09-17T23:56:19+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[Nearest governing overview](../../../overview.md)

The initial implementation is committed at `7cbda30d`; the terminal-cache correction described here is the current L9 working change.

## Purpose

Owns derivation and materialization of the disposable consumer ledger. Its rows and revision
metadata come from committed memory attribution; cache files do not become Git-operation authority.

## Code Commentary

`discard_memory_cache_changes` is used only before an authorized memory-worktree removal. It restores a tracked root cache from HEAD or removes its staged/untracked representation. Ordinary non-forced Git removal still checks all real content. This function creates no commit and moves no ref.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Terminal removal discards only the root memory cache. | `discard_memory_cache_changes` | mcp/src/agents_remember/kernel/memory_cache.py:94-111 |
| Derivation reads Git attribution and computes current/base metadata. | n/a | [mcp/src/agents_remember/kernel/memory_cache.py](mcp/src/agents_remember/kernel/memory_cache.py) |
| Preparation excludes the cache and refresh reports materialization outcomes. | `refresh_memory_cache` | mcp/src/agents_remember/kernel/memory_cache.py:65-91 |
| Committed attribution and row mapping have one reader. | n/a | [mcp/src/agents_remember/kernel/memory_attribution.py](mcp/src/agents_remember/kernel/memory_attribution.py) |
| The consumer representation supports empty derived history. | n/a | [mcp/src/agents_remember/kernel/memory_ledger.py](mcp/src/agents_remember/kernel/memory_ledger.py) |
| Cache independence and exact local-ref derivation are exercised by the retained projection tests. | `test_cache_misses_preserve_contract_and_named_ref_history` | mcp/tests/test_memory_ledger.py:338-360 |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History

- 2026-09-15T06:37:50+02:00 — LCA L9 terminal delivery: `discard_memory_cache_changes` is used only before an authorized memory-worktree removal. It restores a tracked root cache from HEAD or removes its staged/untracked representation. Ordinary non-forced Git removal still checks all real content. This function creates no commit and moves no ref.


- 2026-09-15T01:02 UTC — Created the paired sidecar for the new computed-cache owner, documenting derivation, explicit staging preparation, best-effort materialization, and the absence of ledger commit/ref authority. Working candidate verified by source inspection; commit metadata records real committed history only.
