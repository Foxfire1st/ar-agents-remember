# mcp/tests/test_citation_cache_reclamation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_citation_cache_reclamation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T23:30+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The executable statement of the managed citation cache's reclamation contract: **admission reclaims
the dead, and only from a positive terminal verdict.** The subject is a bounded global resource whose
unit of consumption is *per leaf* — `MANAGED_NAMESPACE_LIMIT` namespaces for the whole coordination
root — because the cache exists to make citation repair affordable, and a repair that cannot get a
namespace cannot run at all.

The recorded defect (S5 of `260915-CAPS-L21`): the limit was a slot count that fit one repository, a
finished leaf released its slot only through its *own* terminal cleanup, and `reclaim_managed_namespace`
had zero callers. A leaf that closed out without a worktree cleanup therefore leaked its slot forever,
and the refusal told the blocked leaf to clean up **another master's** leaf — an operation it has no
authority to perform. The leak was invisible because the two consumers behave differently: the quality
run opens its namespace with `create=False` and completes anyway, while citation repair opens with
`create=True` and refuses outright.

## Code Commentary

### Logic

`CacheReclamationTests` drives the real `ManagedCacheAuthority` / `admit_managed_namespace` entry
points against a scratch coordination root, so every arm reads a tree rather than a mock. `OccupantFacts`
(100) names only what a case varies — `cleanup`, `worktrees`, `phase`, `bytes_of_payload`,
`contract_exists`, `publish` — and `occupy` (159) writes one namespace's control facts plus its payload,
so a case reads as the boundary it is testing.

The arms are the operator-visible outcomes plus the inputs that must **not** license eviction:

- **Release then admit** — `test_a_terminal_cleanup_frees_the_slot_and_a_fifth_leaf_is_admitted` (182)
  occupies the cache to its ceiling with exactly one terminal occupant, admits a newcomer, and requires
  the newcomer's namespace to be present **and** the population to stay at the limit. That is the two
  halves of the recorded block in one sequence.
- **A live leaf is never evicted** — `test_a_live_leaf_is_never_evicted` (198) fills the cache with
  working occupants and requires `reclaimed` to be empty.
- **The byte bound decides** — `test_the_byte_bound_decides_even_under_the_count_ceiling` (211) shows the
  resource is bounded by bytes, not only by a slot count, so a large payload is refused while the count
  ceiling still has room.
- **Positive evidence only** — `test_a_stuck_record_is_reclaimed_only_on_positive_terminal_evidence` (226)
  and `test_a_record_that_cannot_be_read_is_never_evidence_of_a_dead_leaf` (242) split the two ways an
  occupant can fail to present a verdict: a *readable* record that proves nothing leaves the occupant
  alone, and an unreadable record proves nothing either.
- **Fix round F2** — `test_a_corrupted_contract_is_never_evidence_of_a_dead_leaf` (250) is the case that
  closed the counterexample the baseline review reproduced: an occupant whose control record is
  perfectly readable and says `phase: active`, whose namespace is published, but whose **contract bytes
  fail to parse**, was reclaimed. Parse failure is now `None`, not evidence.
- **A lease is not overridable** — `test_a_live_namespace_is_left_alone_even_when_it_reads_as_terminal`
  (289) keeps an occupant whose contract reads terminal while another process holds its lease.
- **The refusal must not misdirect** — `test_a_full_cache_refuses_without_telling_one_leaf_to_clean_up_another`
  (305) pins the message itself: a full cache may not instruct the blocked leaf to clean up a leaf it
  does not own, which was the recorded defect's most costly property.

### Conventions

- Fixtures are real parseable leaf contracts written into a throwaway coordination root, so
  `_prove_terminal` is exercised through its real readers rather than a patched contract object.
- `occupy(publish=False)` (159) deliberately leaves only the control record — the state of a leaf that
  holds a reservation but has stored no index — because that is the state admission must refuse when
  there is no room.
- Namespace identity is derived from the leaf name (`authority`, 139), so a case never invents a
  namespace id that the production path would not produce.

### Invariants And Boundaries

- **The guarantee is fail-closed, and that is the honest statement of it.** An occupant is evicted only
  when it presents a positive terminal verdict, so nothing *unproved* is ever reclaimed. It is **not**
  the stronger claim that no live occupant can ever be evicted: the licensing verdicts are read from
  bytes a live process could in principle still be sitting behind (a parsed terminal `cleanup` cell; a
  parsed contract whose stated worktrees are both gone). The module docstring states this boundary
  rather than claiming an absolute.
- **Contract bytes that do not parse are not evidence.** F2's repair, and the case above pins it.
- **Reclamation is capacity, not authority.** Evicting a dead occupant frees a slot; it never confers
  or transfers a lease, and it never mutates another leaf's contract or enclosure.

## Docs References

No Domain Documentation source is configured for this repository; the subject is the repository's own
cache module and its control records.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source applies; the resource, its records and its readers are all repository-owned. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The bounded resource whose reclamation this module pins, and the limit that names it. | `MANAGED_NAMESPACE_LIMIT` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:48-48 |
| The admission path that reclaims the dead and the authority it inspects. | `admit_managed_namespace`; `ManagedCacheAuthority` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:304-346; mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:71-106 |
| The safety property every verdict is asserted against. | `_prove_terminal` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:429-464 |
| The control record whose phase and outcome are read as terminal evidence. | `CacheControlState` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:110-132 |
| The lease whose holder is honoured even when the contract reads terminal. | `TerminalNamespaceGuard`; `terminal_namespace_guard` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:554-759; mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:763-795 |
| The compatibility reclamation entry point that had zero callers at the base commit. | `reclaim_managed_namespace` | mcp/src/agents_remember/memory_quality/style/citations/source_index_cache.py:798-826 |

## Cross-Repo References

No external repository boundary is exercised; the fixture contracts are written into a throwaway
coordination root owned by the test.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T23:30+02:00 — 260915-CAPS-L21 curator: created this card for a source file **new in this
  leaf** (S5's repair, with fix round F2's `test_a_corrupted_contract_is_never_evidence_of_a_dead_leaf`
  already in the tree). Anchors and ranges were read from the current worktree source; the file is
  untracked at this tip, so verification metadata is pinned to this leaf's code base commit
  `997305a9` and the governed closeout stamps the real code commit. No hash or fingerprint was invented
  here, and the fail-closed boundary above is the module's own stated guarantee, not a stronger claim
  read into it.
