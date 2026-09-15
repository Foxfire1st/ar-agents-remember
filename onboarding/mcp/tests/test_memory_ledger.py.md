# mcp/tests/test_memory_ledger.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_ledger.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935` |
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Nearest governing overview](overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Tests the ledger's newest-first data format and verifies that runtime ledger readers derive
mappings from committed attribution while treating cached tables only as observations.

## Code Commentary

### Logic

The serialization case preserves repeated code commits as ordered memory history: `find_mapping`
returns the newest row and `contains_mapping` can still find an older exact pair. These are lookup
semantics of derived data, not permission to perform Git operations.

`_World` now creates real code commits and attributed memory commits. Its projection cases check
unreachable cache rows, ordering and header differences, a byte-identical correct cache, and forged
metadata/pairs whose objects exist but whose claimed attribution does not. Contract and named-ref
reads survive absent or malformed caches; the named-ref case also creates a same-named tag to prove
that the exact local branch is selected. An unreadable Git commit still raises the explicit refusal.

`_AttributedWorld` retains historical cache-checkpoint commits as a fixture alongside actual
attributed content. The reader must produce the attributed rows at each checkpoint, ignore
hand-written table pairs, and emit no mappings from wholly unattributed history. A partially
attributed history contributes only its real trailers. Invalid source and branch code targets are
reported as exclusions instead of retained. Reversed or incomplete cached superseding pairs cannot
change the order supplied by actual memory history.

The remaining cases cover empty history, branch exclusion, last trailer-block parsing, body
lookalikes, mixed trailer blocks, optional code-object filtering, and attributed commits inherited
through a merge. The writer/reader round trip commits a message rendered by the real effective
closeout input, so it checks that the actual writer's key is recognized by the actual Git reader.

### Conventions

The file retains twenty tests. Historical ledger commits are explicit fixture data for testing
cache independence; they do not prescribe current runtime writes or a fallback reader. Literal
trailer spellings in parser tests are independent oracles, while the writer round trip deliberately
uses the production renderer. Temporary repositories and source assertions provide focused
development evidence, not certification or live integration proof.

### Invariants And Boundaries

- Runtime projection cannot union pre-rule cached rows into attributed Git history.
- A valid-looking pair of existing objects is insufficient without matching committed attribution.
- Cache absence/damage remains distinct from a genuine Git lookup failure.
- Invalid code targets remain visible as exclusions; merged-in attributed history remains visible.
- Repeated valid code-to-memory states keep Git-derived newest-first ordering.
- Historical entries below do not require restoring retired table-authority assertions or ledger legs.

### Todos

No new file-local follow-up is established by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Data round-trip and current-versus-historical lookup semantics. | L53-L68 | [mcp/tests/test_memory_ledger.py](mcp/tests/test_memory_ledger.py) |
| Actual attributed fixtures, cache forgery, cache misses, and exact local-ref selection. | L91-L179; L315-L335; L338-L360 | [mcp/tests/test_memory_ledger.py](mcp/tests/test_memory_ledger.py) |
| Unattributed and partially attributed histories cannot inherit cached pairs. | L499-L519; L550-L569 | [mcp/tests/test_memory_ledger.py](mcp/tests/test_memory_ledger.py) |
| Invalid targets are reported and superseding order comes from actual history. | L529-L547; L572-L613 | [mcp/tests/test_memory_ledger.py](mcp/tests/test_memory_ledger.py) |
| The real writer/reader round trip and merged-in attribution stay covered. | L717-L751; L754-L784 | [mcp/tests/test_memory_ledger.py](mcp/tests/test_memory_ledger.py) |
| The runtime projection under test separates computed mappings from cache observations. | L222-L249; L334-L396 | [mcp/src/agents_remember/worktrees/ledger_projection.py](mcp/src/agents_remember/worktrees/ledger_projection.py) |

## Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No additional configured cross-repository evidence is claimed. | — | — |

## Update History

- 2026-09-15T00:51 UTC — Replaced obsolete table-union, cached-metadata, additions, and malformed-table refusal expectations with Git-only attribution, cache forgery/miss checks, exact local-ref selection, and invalid-target reporting; retained twenty focused cases and the format/parser/merge protections. Working candidate verified by source inspection; real last-touch commit metadata retained, with no future commit hash or certification claim.


- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of
  10 claim(s) whose anchor no longer sat in its cited range and normalised 13 further range(s) in
  this card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T11:58+02:00 — 260913-LCA-L11 curator (uncommitted change set on `ar/260913-lca-l11-ar`,
  base `4214d7a1`): recorded the module's two new cases — the source row the source cannot carry is
  excluded at the read with its reason and reported rather than dropped in silence, and a partially
  trailered source still reads its pre-rule rows — plus the `_content_commit` helper they forced,
  because a row's memory cell must now name a commit git can resolve. Corrected the framing the
  reader change falsified: the six pre-trailer projection cases no longer reach the reader through a
  *fallback*, they read the source's own recorded table, which is the path every source takes.
  Repointed every citation in this card to its current range (the module grew from 642 to 702 lines
  and the kernel attribution module's own ranges had drifted), and stated the measured shape the
  second case protects: a line whose table records hundreds of rows and whose history carries one
  trailer must not read as a one-row source. Verification metadata remains closeout-owned; no
  acceptance claim and no verification stamp advanced.
- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`,
  base `5bb124d4`): one import moved. `CODE_COMMIT_TRAILER_KEY` is now imported from
  `agents_remember.kernel.memory_attribution` (`:11`) instead of from
  `agents_remember.models.closeout.input`, because the writing model stopped naming the constant when it
  began delegating to the kernel's renderer. No case changed and no assertion changed — the round-trip
  case still renders through the real writer and reads the code commit back out through the real reader —
  so the module's evidence and the oracle rule both stand; recorded the import's source and added the
  census case that owns the one-definition rule behaviourally as a reference. Verification metadata
  remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T23:24+02:00 — 260913-LCA-L2 follow-up (same uncommitted change set): the module gained
  its tenth added case, `test_the_rendered_trailer_is_the_one_the_reader_parses`, after the writer and
  the reader were found to hold two separate `Code-Commit` literals. The case renders through the real
  writer, commits the message as a real memory commit and reads the code commit back out through the
  real reader, so a writer-side key change loses the row and fails this case rather than passing
  silently. Recorded that the module now imports `CODE_COMMIT_TRAILER_KEY` from
  `kernel/memory_attribution.py` (the key's one declaration), that the literal `Code-Commit` text in
  the trailer-parse cases is a deliberate independent oracle which must not be "corrected" to read the
  constant, and repointed every citation to the grown file. Verification metadata remains
  closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T23:08+02:00 — 260913-LCA-L2 curator (uncommitted change set on `ar/260913-lca-l2-ar`):
  recorded the nine added cases that make the ledger's source the memory commits' own
  `Code-Commit:` attribution — the every-checkpoint closed loop, the hand-edit case that proves the
  live table cannot move the projection, the pre-trailer blob fallback, the bootstrap source that
  contributes no rows, `exclude` selecting a branch's own commits, the last-block-wins parse, the
  unknown-code-commit drop, the by-key read of a multi-trailer block, and the merged-in mapping that
  a first-parent walk would miss. Recorded the two fixture changes those cases needed
  (`--allow-empty` commits, and a `_ledger` that tolerates an empty row list), the checkpoint
  snapshots that are no longer aliased to the live row list, and that the six pre-existing
  projection cases reach `read_ledger_source` through the per-commit blob fallback. Repointed the
  stale citation for `test_roundtrip_preserves_newest_same_code_history` (32-47 → 38-53), and
  replaced the superseded "sealed pure-unit route" evidence note with the module's actual
  `unit-regression` lane registration plus the statement that registration is not execution
  evidence. Verification metadata remains closeout-owned; no acceptance claim and no verification
  stamp advanced.

- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_roundtrip_preserves_newest_same_code_history` repointed to mcp/tests/test_memory_ledger.py:32-47. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `find_mapping`; `contains_mapping` repointed to mcp/src/agents_remember/kernel/memory_ledger.py:255-257; mcp/src/agents_remember/kernel/memory_ledger.py:260-268. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-26T14:32+02:00 — Created for the IAS ledger-history correction. Verification metadata
  remains blank until the source commit exists.
