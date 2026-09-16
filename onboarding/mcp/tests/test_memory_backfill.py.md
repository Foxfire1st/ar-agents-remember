# mcp/tests/test_memory_backfill.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_backfill.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T03:43 |
| lastVerifiedCommitHash | `67b21aeb66df96a971a33ae431a13992f2528b45` |
| lastVerifiedCommitDate | 2026-09-15T06:37:48+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Nearest governing overview](overview.md)

Committed-source review: inspected at 2026-09-15T03:43 UTC against `7cbda30d9a9a4c2944382fbef46ac58b85329935`.
Normal closeout owns final verification-metadata stamping for this committed source.

## Purpose

Exercises explicit historical-memory attribution migration with disposable real repositories:
selection and loss accounting, message/object replay, rescue and named-ref safety, table-artifact
carry, and the actual CLI path.

## Code Commentary

### Logic

The plan cases check that carryable memory pairings receive attribution, conflicts follow the
recorded order rather than hash order, and losses name their winners. Missing objects, unreachable
commits, code commits absent from their repository, abbreviated cells, stable digests, and digests
that distinguish lost claims are separate assertions.

Apply cases read real trailers, prove a second run changes no refs, compare trees/identities/dates,
and require a total rewritten-ID map. The trailer-only proof now calls the ordinary
`read_ledger_source` directly: that runtime API has no table fallback, so the old fabricated absent
`relative` path is no longer needed.

`test_the_rescue_ref_holds_the_original_tip_before_the_rewrite` now creates two named target refs,
applies to both in the same request, verifies the rescue still holds the original tip, and checks
both targets moved to the returned new tip. This exercises the newline-framed multi-ref stdin batch.
Other cases retain rescue collision/namespace and stale-preview-digest refusals.

Historical table-reading cases intentionally permit a disagreeing header while refusing an absent
migration table. Table carry checks resolved abbreviations, unchanged code cells/code base, and
updated memory IDs. Those are migration-artifact contracts, not runtime cache authority. CLI cases
exercise a branch-name tip and retry after apply through the real argument/command functions.

The existing CLI branch-name/retry case also creates `ar/peer` and passes two explicit `--ref`
arguments to apply. It verifies that the peer reaches the same rewritten tip as the leaf, reads the
retained rescue tip and both attributions, then repeats apply with the same target set while
checking that the rescue ref and leaf tip stay unchanged. This extends the retained CLI case;
it adds no new test definition.

### Conventions

Each class builds disposable repositories with explicit identities and cleanup. The test module
uses actual object IDs and Git readers rather than treating returned strings as proof. Historical
cache commits and rescue refs are fixture data; no shared repository is rewritten by these tests.

### Invariants And Boundaries

- Multi-ref apply must update every named target while retaining the original rescue tip.
- Unrepresentable claims and data holes remain observable.
- The runtime proof reads only committed trailers; historical tables are used only by explicit migration cases.
- Tree/identity/date preservation and same-history idempotence stay asserted.
- Test source and focused results are not authorization or evidence of a live backfill.

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
| Plan selection distinguishes conflict outcomes, missing data, and stable/loss-sensitive digests. | L222-L392 | [mcp/tests/test_memory_backfill.py](mcp/tests/test_memory_backfill.py) |
| The actual two-ref apply regression retains the original rescue tip. | L579-L596 | [mcp/tests/test_memory_backfill.py](mcp/tests/test_memory_backfill.py) |
| Runtime proof uses the ordinary Git-only reader. | L467-L550 | [mcp/tests/test_memory_backfill.py](mcp/tests/test_memory_backfill.py) |
| Historical table read/carry and real CLI boundaries stay covered. | L645-L672; L675-L764; L767-L920 | [mcp/tests/test_memory_backfill.py](mcp/tests/test_memory_backfill.py) |
| The production target-update stream emits exactly one newline between commands. | L837-L879 | [mcp/src/agents_remember/kernel/memory_backfill.py](mcp/src/agents_remember/kernel/memory_backfill.py) |
| The existing CLI case applies two named refs and retries the same target set. | L853-L909 | [mcp/tests/test_memory_backfill.py](mcp/tests/test_memory_backfill.py) |
| The committed implementation uses native reversed topological traversal. | L784-L791 | [mcp/src/agents_remember/kernel/memory_backfill.py](mcp/src/agents_remember/kernel/memory_backfill.py) |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History

- 2026-09-15 — Preserved the following dated pre-takeover review notes from the parent working tree. They describe that earlier candidate; current behavior is documented above. Exact original files and patches are retained in the master cutover report.

- 2026-09-14T23:55+02:00 — 260913-LCA completed-master review follow-up (same uncommitted change set,
  `ar/260913_ledger-commit-attribution`, base `bb65a207`): **the module gained the multi-target ref
  case.** `test_two_declared_branches_move_together_in_one_transaction` creates a second branch at the
  original tip and drives the public apply route with BOTH refs, because the reviewed defect —
  `_move_targets` appended an empty string after each update instruction and joined the list with
  newlines, so a blank line reached `git update-ref --stdin` and aborted the whole transaction with
  `fatal: empty command in input` — was invisible to every single-ref case: one declared branch moved
  only because the one trailing newline its last line needed doubled as the stream's terminator. The
  case pins all three promises together: both declared branches arrive at the rewritten tip, the
  rescue ref still holds the pre-rewrite history, and a second run over the migrated history reports
  `updated_refs == ()` and `rewritten == ()` with both branches unmoved. Every citation in this card
  was re-derived against the grown module (906 → 953 lines): `MemoryBackfillApplyTests` 399-629 →
  399-676, the existing-refusal cases 585-594 → 632-641, 596-609 → 643-656, 611-621 → 658-668 and
  623-629 → 670-676, `MemoryBackfillLedgerReadTests` 632-659 → 679-706 with its cases 639-654 →
  686-701 and 656-659 → 703-706, `MemoryBackfillCarryTests` 662-751 → 709-798 with `ledger_text`
  669-694 → 716-741 and its four cases 696-709 → 743-756, 711-723 → 758-770, 725-738 → 772-785 and
  740-751 → 787-798, and `MemoryBackfillCliTests` 754-902 → 801-949 with `contract_path` 770-829 →
  817-876, `invoke` 831-838 → 878-885 and its two cases 840-891 → 887-938 and 893-902 → 940-949; the
  kernel anchors moved with the module (`_move_targets` 837-879 → 837-880, `carry_ledger_cells`
  927-972 → 940-985, `_full_name` 1004-1012 → 1017-1025) and the projection anchors with its own
  (`read_ledger_source` 302-350 → 315-363, `LedgerSource` 93-112 → 96-115). Verification metadata
  remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-09-15T03:43 UTC — Documented the committed C2 extension of the existing CLI case to two named refs, peer-tip equality, retained rescue/attribution checks, and same-target retry; refreshed source ranges without adding a test or making a live-migration execution claim. Verification hash/date stamping remains with normal closeout.


- 2026-09-15T01:02 UTC — Documented two-ref apply coverage and the removal of the absent-path runtime proof workaround; preserved plan/loss/replay/rescue/CLI protections and separated historical migration-table tests from cache authority. Working candidate verified by source inspection; commit metadata records real committed history only.


- 2026-09-14T18:20+02:00 — 260913-LCA-L3 curator (same uncommitted change set, `ar/260913-lca-l3-ar`,
  base `7317108b`): **the module grew from 543 to 906 lines around the reviewed fix and this card now
  describes it.** The rule's cases were replaced: the oldest-row-per-code-commit case became
  `test_every_recorded_pairing_that_can_be_carried_gets_its_own_trailer` (both pairings of one code
  commit keep a trailer, which is what the fill step exists for); the collision cases became
  `test_a_contested_memory_commit_names_the_oldest_claim_and_reports_the_loss` and
  `test_a_declined_row_names_whether_it_is_a_duplicate_or_a_lost_mapping`; and
  `test_the_winner_does_not_depend_on_hash_order` is new, pinning the reviewed defect directly by
  swapping two rows in the same table. A loss-digest case was added. **The acceptance proof changed
  shape and is now trailer-only**: `test_the_trailers_alone_preserve_every_pairing_the_ledger_file_recorded`
  reads the rewritten tip through `_ABSENT_LEDGER`, a declared path no commit carries, and compares
  the mapped historical pairings against Git-parsed trailers by set equality, failing if any carryable
  pairing is omitted — the earlier proof read the table the migration carries forward, and because
  `read_ledger_source` unions table rows into trailer rows it proved the table survived rather than the
  trailers, which is how 60 omitted pairings passed a green suite.
  `test_a_content_bearing_duplicate_that_would_be_dropped_fails_the_proof` reproduces the documented
  drop shape. A fifth class, `MemoryBackfillCliTests`, drives the real registered command path against
  a branch-name tip and a second apply, because the reviewed second defect — a name resolved nowhere
  before the rescue refs were written, and the rescue guard running before the empty-plan check — was
  invisible from every kernel-level case. Fixture changes recorded: a configurable memory branch and a
  `commit=False` table rewrite that isolates row ORDER from object identity. Every anchor in this card
  is newly derived against the grown module. Verification metadata remains closeout-owned; no
  acceptance claim and no verification stamp advanced.

- 2026-09-14T17:20+02:00 — 260913-LCA-L3 curator (uncommitted change set on `ar/260913-lca-l3-ar`,
  base `7317108b`): created the one-to-one sidecar for this new test module, mirroring the sibling
  `mcp/tests/test_memory_attribution_producers.py` card's structure. Records the three load-bearing
  properties the module is built around (oldest-row-wins with every passed-over row reported; a
  second run plans nothing, moves no ref and rebuilds nothing byte-differently; the rewrite replays
  tree, identity and both timestamps so the trailer is the only difference), the four `TestCase`
  classes and what each pins, the real-`read_ledger_source` before/after case as the closed loop that
  proves the format against its reader, and the disposable-repository boundary. Verifies the
  `unit-regression` lane row this module already has at `mcp/tests/test-evidence-lanes.toml:69`, and
  records that the module deliberately declares no `evidence-lifecycle.toml` consumer row because it
  imports nothing from `mcp/tests/` and therefore reaches no `consumer_scope = "exact"` shared support
  artifact. Verification metadata names the leaf's base commit and remains closeout-owned; no
  acceptance claim and no verification stamp advanced.
