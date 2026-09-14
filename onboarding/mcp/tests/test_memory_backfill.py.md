# mcp/tests/test_memory_backfill.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_backfill.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T18:20+02:00 |
| lastVerifiedCommitHash | `270704b86116728a64ada83ee258a0e7726206b4` |
| lastVerifiedCommitDate | 2026-09-14T18:18:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The rule that chooses a trailer, and that it writes exactly one. The migration this module tests is
the one operation in the trailer transition that no `git revert` can undo, so the cases aim at the
properties that make it safe rather than at its happy path. Four are load-bearing: every pairing the
table records that a trailer CAN hold receives one, because a commit renders one value per trailer
key and the reader takes the last, so which pairings the format cannot hold is a decision the code
makes and therefore a decision a test has to pin; a duplicate pairing whose memory commit changed
onboarding or any other file content is not dropped when nothing else contradicts it, because
repeated onboarding repair is the history of the process and collapsing it is the documented failure;
a conflicting claim is resolved by the table's own order and REPORTED with the winner named, so no
code commit loses its mapping without being named; and the rewrite reproduces every commit's tree,
identity and timestamps, so the trailer is the only difference between an original and its
replacement. A second run planning nothing and moving no ref is what makes the plan its own dry run
and the migration re-runnable rather than one-shot.

**The acceptance proof deliberately reads the rewritten tip through an ABSENT ledger path.**
`read_ledger_source` merges the table it finds at the ledger path into the rows the trailers name, so
reading it after the table is carried forward proves the TABLE survived and says nothing about the
trailers — which is exactly how 60 omitted pairings passed an earlier green suite. The proof reads the
same tip through a path no commit carries, so the table contributes nothing and the comparison is
against Git-parsed trailers alone. No file is deleted and no reader is made tolerant to get there.

Every fixture is a throwaway repository under `tempfile`. Nothing here reads or writes the
coordination tree, the installed memory repository, or any shared ref, and nothing here claims that a
backfill has been applied to a real repository.

## What Each Case Pins

| Class | The property it pins |
| --- | --- |
| `MemoryBackfillPlanTests` | Which pairings the selection carries, which it declines, and that every loss is named |
| `MemoryBackfillApplyTests` | What the rewrite writes, what it must leave exactly as it found it, and that the trailers alone preserve the table's pairings |
| `MemoryBackfillLedgerReadTests` | Reading the table the history carries, without the header check the strict reader keeps |
| `MemoryBackfillCarryTests` | Moving the table's memory cells onto the ids the rewrite produced |
| `MemoryBackfillCliTests` | The real `agents-remember memory-backfill` path, aimed at a branch-name tip |

## Code Commentary

### Logic

`BackfillFixture` cit:([`BackfillFixture`], mcp/tests/test_memory_backfill.py:134-223) builds two real Git repositories
under one `tempfile.TemporaryDirectory` — a memory repository (on a configurable branch, so the CLI
cases can use a name rather than `main`) and a code repository beside it. Its `table` method writes a
ledger whose header agrees with its own first row, exactly as the real one does
(`_write_table` cit:([`_write_table`], mcp/tests/test_memory_backfill.py:93-131)), and `commit=False` re-records a
table's row ORDER over the same commits without adding one: committing the second table would rebuild
the memory line, so a comparison about which of two claims wins would differ in object names as well
as in the order under test. Commits are created through the production runner with
`GitRunnerOptions(identity=...)` cit:([`_commit`], mcp/tests/test_memory_backfill.py:78-90), so the fixture depends on
the same identity mechanism the rewrite replays. `tip` reads the branch tip from the ref rather than
from HEAD, because a rewrite moves refs and not a checked-out HEAD.

**The rule's cases are in `MemoryBackfillPlanTests`**
cit:([`MemoryBackfillPlanTests`], mcp/tests/test_memory_backfill.py:226-396).
`test_every_recorded_pairing_that_can_be_carried_gets_its_own_trailer`
cit:([`test_every_recorded_pairing_that_can_be_carried_gets_its_own_trailer`], mcp/tests/test_memory_backfill.py:233-252) records a
code commit twice — paired once early and repaired again later — and asserts BOTH pairings keep a
trailer, that nothing is reported lost, and that three code commits are named. This is the case the
fill step exists for: a maximum matching alone would leave the second memory commit unattributed.
`test_a_contested_memory_commit_names_the_oldest_claim_and_reports_the_loss`
cit:([`test_a_contested_memory_commit_names_the_oldest_claim_and_reports_the_loss`], mcp/tests/test_memory_backfill.py:254-275) has two code
commits naming ONE memory commit with neither having another row: the bottom-most row is the older
claim and it wins, the loser is asserted through `lost_claims` (`code_commit`, `memory_commit` and
`winner`, not merely counted), `lost_code_commits` names it, and the plan is asserted NOT empty.
`test_the_winner_does_not_depend_on_hash_order`
cit:([`test_the_winner_does_not_depend_on_hash_order`], mcp/tests/test_memory_backfill.py:277-303) is the regression for the
reviewed defect: the same two code commits and the same table with the two rows swapped, asserting the
bottom-most row's owner wins in both — a rule that let hash order decide would name one commit when it
sits on top and the other when it does not. `test_a_declined_row_names_whether_it_is_a_duplicate_or_a_lost_mapping`
cit:([`test_a_declined_row_names_whether_it_is_a_duplicate_or_a_lost_mapping`], mcp/tests/test_memory_backfill.py:305-339) holds the two
tables a single skip count cannot tell apart: in the first the declined row is a duplicate and costs
nothing, in the second the same decline IS the lost mapping, and only `lost_code_commits` separates
them. The three hole cases follow — a code commit the repository lacks
cit:([`test_a_code_commit_the_code_repository_lacks_skips_its_whole_row_group`], mcp/tests/test_memory_backfill.py:341-351), a cell naming
no object kept apart from an unreachable commit
cit:([`test_a_cell_naming_no_object_is_not_confused_with_an_unreachable_commit`], mcp/tests/test_memory_backfill.py:353-360), and the
abbreviated cell resolving to the commit it names
cit:([`test_an_abbreviated_cell_is_the_same_row_as_its_full_name`], mcp/tests/test_memory_backfill.py:362-372). The last two cases pin the
digest: stable across two identical plans
cit:([`test_the_same_history_plans_the_same_digest_twice`], mcp/tests/test_memory_backfill.py:374-380), and DIFFERENT for a plan that
lost a mapping versus one that did not
cit:([`test_a_plan_that_lost_a_mapping_does_not_share_a_digest_with_one_that_did_not`], mcp/tests/test_memory_backfill.py:382-396), because the
digest is what a caller pins an apply to and a previewed digest must not authorize a different
decision.

`MemoryBackfillApplyTests` cit:([`MemoryBackfillApplyTests`], mcp/tests/test_memory_backfill.py:399-629) is the writing half.
`test_the_written_trailer_is_the_code_commit_the_row_named`
cit:([`test_the_written_trailer_is_the_code_commit_the_row_named`], mcp/tests/test_memory_backfill.py:406-420) reads the trailer back off
the REPLACEMENT commit through the total identity map, because the plan names the original commit.
`test_a_second_run_rewrites_nothing_and_moves_no_ref`
cit:([`test_a_second_run_rewrites_nothing_and_moves_no_ref`], mcp/tests/test_memory_backfill.py:422-437) drives a real first apply,
carries the table through the production seam, and asserts the second plan is empty, the second run's
old and new tips are equal, no ref moved, and the branch tip is unchanged.
`test_every_commit_keeps_its_tree_identity_and_dates`
cit:([`test_every_commit_keeps_its_tree_identity_and_dates`], mcp/tests/test_memory_backfill.py:439-449) compares tree, both
identities, both dates and the subject across the whole line before and after.
`test_the_identity_map_is_total_so_every_original_id_has_a_replacement`
cit:([`test_the_identity_map_is_total_so_every_original_id_has_a_replacement`], mcp/tests/test_memory_backfill.py:451-460) is what makes the
carry and any saved contract cell resolvable.

**The acceptance proof** is
`test_the_trailers_alone_preserve_every_pairing_the_ledger_file_recorded`
cit:([`test_the_trailers_alone_preserve_every_pairing_the_ledger_file_recorded`], mcp/tests/test_memory_backfill.py:462-545). Its fixture is a six-row
table over six memory commits and four code commits in which five pairings can be carried and the
sixth is a contested claim with no fallback. It reads the rewritten tip through `_ABSENT_LEDGER`
cit:([`_ABSENT_LEDGER`], mcp/tests/test_memory_backfill.py:75-75), a path no commit carries, so the table contributes
nothing; asserts no exclusions; and compares the mapped historical pairings against the Git-parsed
trailers by SET EQUALITY, where the expected set is the historical rows classified explicitly and
mapped through the old-to-new ids. It then asserts the loser and its winner by name, that every named
memory commit carries a trailer including the contested one, and that the plan is not empty. An
omission that is not named as a loss therefore fails the proof, which is the property the earlier
version lacked. `test_a_content_bearing_duplicate_that_would_be_dropped_fails_the_proof`
cit:([`test_a_content_bearing_duplicate_that_would_be_dropped_fails_the_proof`], mcp/tests/test_memory_backfill.py:547-572) reproduces the
reviewed omission's shape — a pairing repaired later under the same code commit — and asserts the
older pairing is readable from the trailers and from nowhere else.

The four refusals are pinned as refusals that leave the history alone:
`test_the_rescue_ref_holds_the_original_tip_before_the_rewrite`
cit:([`test_the_rescue_ref_holds_the_original_tip_before_the_rewrite`], mcp/tests/test_memory_backfill.py:574-583),
`test_an_existing_rescue_ref_refuses_before_anything_is_rewritten`
cit:([`test_an_existing_rescue_ref_refuses_before_anything_is_rewritten`], mcp/tests/test_memory_backfill.py:585-594) (which also asserts the tip
did not move), `test_a_previewed_digest_that_no_longer_matches_refuses`
cit:([`test_a_previewed_digest_that_no_longer_matches_refuses`], mcp/tests/test_memory_backfill.py:596-609), where recording another row is
what invalidates the preview, and the two rescue-ref shape refusals
cit:([`test_the_rescue_ref_may_not_be_one_of_the_refs_the_run_moves`, `test_a_rescue_ref_outside_refs_is_refused`], mcp/tests/test_memory_backfill.py:611-621; mcp/tests/test_memory_backfill.py:623-629).

`MemoryBackfillLedgerReadTests` cit:([`MemoryBackfillLedgerReadTests`], mcp/tests/test_memory_backfill.py:632-659) holds the two
read-shape cases: `test_a_header_disagreeing_with_its_own_first_row_is_still_read`
cit:([`test_a_header_disagreeing_with_its_own_first_row_is_still_read`], mcp/tests/test_memory_backfill.py:639-654) pins the unvalidated
structural parse, because a header disagreeing with its own first row is one of the shapes the
projection repairs; `test_a_tip_with_no_ledger_refuses_rather_than_planning_nothing`
cit:([`test_a_tip_with_no_ledger_refuses_rather_than_planning_nothing`], mcp/tests/test_memory_backfill.py:656-659) is the difference
between "there is nothing to write" and "there is nothing to read".

`MemoryBackfillCarryTests` cit:([`MemoryBackfillCarryTests`], mcp/tests/test_memory_backfill.py:662-751) covers the table carry.
`ledger_text` cit:([`ledger_text`], mcp/tests/test_memory_backfill.py:669-694) builds a ledger whose header is valid for its own
first row with both bases overridable.
`test_an_abbreviated_cell_is_carried_to_the_full_new_name`
cit:([`test_an_abbreviated_cell_is_carried_to_the_full_new_name`], mcp/tests/test_memory_backfill.py:696-709) is the trap a textual
find-and-replace falls into: an eight-character cell is a prefix, so leaving it behind would keep one
row naming the OLD commit and one row would stay excluded.
`test_the_code_column_and_the_code_base_are_carried_through_untouched`
cit:([`test_the_code_column_and_the_code_base_are_carried_through_untouched`], mcp/tests/test_memory_backfill.py:711-723) pins the direction
of the migration — memory cells and `baseMemoryCommit` move, code cells and `baseCodeCommit` do not.
`test_a_cell_absent_from_the_map_is_carried_as_its_own_resolved_name`
cit:([`test_a_cell_absent_from_the_map_is_carried_as_its_own_resolved_name`], mcp/tests/test_memory_backfill.py:725-738) states the
partial-map behavior the total map makes unreachable in production but which must not corrupt a cell.
`test_the_carried_table_validates_and_reads_with_no_exclusion`
cit:([`test_the_carried_table_validates_and_reads_with_no_exclusion`], mcp/tests/test_memory_backfill.py:740-751) is the closed loop: the
carried table validates through the strict parser, its first row equals the header's
`lastMemoryContentCommit`, and the real source read at the new tip returns zero exclusions.

**`MemoryBackfillCliTests` exists because the reviewed defect was invisible from everywhere else.**
cit:([`MemoryBackfillCliTests`], mcp/tests/test_memory_backfill.py:754-902) Every other case calls the kernel with a resolved
full commit hash, while the CLI passes the contract's memory WORK BRANCH NAME. Nothing short of the
real command path exercises that, so the class builds a leaf contract whose memory work branch is a
name cit:([`contract_path`], mcp/tests/test_memory_backfill.py:770-829) and drives `run` through the same parser the
console script builds cit:([`invoke`], mcp/tests/test_memory_backfill.py:831-838).
`test_the_cli_applies_a_branch_name_tip_and_survives_its_own_retry`
cit:([`test_the_cli_applies_a_branch_name_tip_and_survives_its_own_retry`], mcp/tests/test_memory_backfill.py:840-891) asserts planning reports work
(exit 1), the apply succeeds from a name (exit 0) and moves the branch, the rescue ref holds the tip
the rewrite replaced, the rewritten line carries both recorded attributions — and then that a SECOND
apply, which meets the rescue ref the first run created, still returns 0, still leaves the rescue ref
on the pre-rewrite tip and still leaves the branch where the first run put it.
`test_the_cli_refuses_a_contract_whose_memory_repository_is_missing`
cit:([`test_the_cli_refuses_a_contract_whose_memory_repository_is_missing`], mcp/tests/test_memory_backfill.py:893-902) is the adapter's own refusal
path (exit 2).

### Conventions

Real Git object names and real repositories throughout: the fixture runs `git init` on a real branch,
commits through the production runner, and asserts on object ids read back with `git rev-parse`,
because a rewrite claim is only meaningful against real objects. The ledger fixture is written as the
real one is — fenced JSON metadata whose `lastVerifiedCodeCommit`/`lastMemoryContentCommit` are its own
first row — so a case that depends on a valid header can use it and a case that must survive an
invalid one edits it in place. Two spellings of one object are used deliberately
(`_ABBREVIATION = 8`) so abbreviation is exercised rather than assumed, and `_ABSENT_LEDGER` is a
declared constant so the acceptance proof's denial of the fallback is visible rather than implied by a
temporary rename. Every case is a `unittest` method on one of five `TestCase` classes, each with its
own fixture and `addCleanup`, so no case can observe another's refs.

The module drives the real CLI rather than a re-implementation: it imports `add_arguments` and `run`
from `agents_remember.cli.memory_backfill` and rebuilds the subparser exactly as the console script
does, so a change to the registered flags is a failing case rather than a silent divergence.

The module is registered in the `unit-regression` lane of `mcp/tests/test-evidence-lanes.toml`
(`mcp/tests/test-evidence-lanes.toml:69`). It declares **no** consumer row in
`mcp/tests/evidence-lifecycle.toml`, and that is correct rather than an omission: it imports nothing
from `mcp/tests/` — its only imports are the production modules under test plus stdlib — so no
`consumer_scope = "exact"` shared support artifact is reached. Consumer declarations are ownership
accounting only; they are not execution or acceptance evidence.

### Invariants And Boundaries

- **The migration is irreversible at the object level, so every safety property has a case.** The
  rescue-ref cases, the digest-pin case and the two ref-shape refusals exist because no `git revert`
  restores a rewritten commit.
- **A pairing the format can hold is not dropped.** The fill step is asserted by the
  duplicate-pairing case: both pairings of one code commit keep their own trailer, because a memory
  commit that changed onboarding is its own fact.
- **A conflict is resolved by the table's order and the loser is named.** The hash-order case and the
  contested-claim case are one property from two sides: a winner chosen by object name fails, and a
  loss reported as a bare number fails.
- **A duplicate and a lost mapping are different facts.** Two tables carrying the same decline are
  asserted apart, and only `lost_code_commits` distinguishes them.
- **A plan that lost a mapping is not empty**, and it does not share a digest with a plan that did not
  — so a previewed digest cannot authorize an apply that drops a pairing.
- **The acceptance proof is trailer-only.** It reads the rewritten tip through a ledger path no commit
  carries, because the reader unions the table into the trailers and would otherwise prove the table
  survived rather than the trailers; and it fails if any carryable pairing is omitted.
- **The rewrite is a message change and nothing else.** Tree, parents, identities and both timestamps
  are asserted equal across the rewrite.
- **The identity map is total.** Every original id has an entry, and an unchanged commit maps to
  itself, which is what makes the second-run no-op an object-level fact rather than a plan-level one.
- **The table is carried as part of the migration.** A rewrite without the carry leaves every recorded
  row excluded, so the carry's closed-loop case is a correctness case and not a convenience.
- **The CLI's own path has its own case**, because the branch-name tip and the retry-after-apply are
  shapes no kernel-level case reaches.
- **Nothing here touches shared state.** Every repository is disposable and every ref is inside it;
  these cases are focused development evidence, not certification, and they make no claim that a
  backfill has been applied to the real memory repository.

### Todos

None. The apply that this module's evidence supports is deferred by developer ruling to this master's
integration into IAS — rewriting the shared ancestors removed the master's common ancestor with its
super — so the migration runs then, not now. That is a sequencing decision recorded on the kernel card
and the route overview, not a gap in this module.

## Docs References

No Domain Documentation source is configured for this repository. The proving evidence is git's own
trailer rendering and commit plumbing exercised through real repositories, plus this repository's
source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for this repository-owned rewrite contract. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The selection under test: a maximum matching offered most-constrained-first plus the fill that gives every unreached memory commit its own oldest row. | `_select_pairings`; `_maximum_matching`; `_augment`; `_oldest_row_rank` | mcp/src/agents_remember/kernel/memory_backfill.py:434-497; mcp/src/agents_remember/kernel/memory_backfill.py:515-540; mcp/src/agents_remember/kernel/memory_backfill.py:543-559; mcp/src/agents_remember/kernel/memory_backfill.py:500-512 |
| The census under test: holes separated from declines, the two declines kept apart, and every loss named with its winner. | `_choose_trailers`; `_row_skip_reason`; `_decline_reason`; `SKIP_REASONS_THE_RULE_CHOSE`; `_lost_claims`; `LostClaim` | mcp/src/agents_remember/kernel/memory_backfill.py:327-387; mcp/src/agents_remember/kernel/memory_backfill.py:562-583; mcp/src/agents_remember/kernel/memory_backfill.py:390-403; mcp/src/agents_remember/kernel/memory_backfill.py:99-99; mcp/src/agents_remember/kernel/memory_backfill.py:406-431; mcp/src/agents_remember/kernel/memory_backfill.py:130-141 |
| The plan under test: the widened empty-plan rule, the counts, and the digest that covers the losses. | `MemoryBackfillPlan`; `is_empty`; `_plan_digest`; `plan_memory_backfill` | mcp/src/agents_remember/kernel/memory_backfill.py:145-224; mcp/src/agents_remember/kernel/memory_backfill.py:182-193; mcp/src/agents_remember/kernel/memory_backfill.py:608-622; mcp/src/agents_remember/kernel/memory_backfill.py:257-308 |
| The rewrite and its ref safety under test: the total identity map, the byte-faithful replay, the name resolution the CLI case forced, and the ordered guards. | `apply_memory_backfill`; `_resolve_commit`; `_write_rescue_refs`; `_move_targets`; `_rewrite_history`; `_rebuild` | mcp/src/agents_remember/kernel/memory_backfill.py:625-661; mcp/src/agents_remember/kernel/memory_backfill.py:731-748; mcp/src/agents_remember/kernel/memory_backfill.py:691-728; mcp/src/agents_remember/kernel/memory_backfill.py:837-879; mcp/src/agents_remember/kernel/memory_backfill.py:755-781; mcp/src/agents_remember/kernel/memory_backfill.py:794-818 |
| The carry under test: cells resolved through git before mapping, code cells and the code base carried untouched. | `carry_ledger_cells`; `_full_name` | mcp/src/agents_remember/kernel/memory_backfill.py:927-972; mcp/src/agents_remember/kernel/memory_backfill.py:1004-1012 |
| The real projection read the acceptance proof drives through an absent ledger path, and the reader's own union behaviour that made the path necessary. | `read_ledger_source`; `LedgerSource` | mcp/src/agents_remember/worktrees/ledger_projection.py:302-350; mcp/src/agents_remember/worktrees/ledger_projection.py:93-112 |
| The strict parser the carried table must satisfy, and the header promise its first row is checked against. | `parse_ledger_text`; `validate_ledger` | mcp/src/agents_remember/kernel/memory_ledger.py:58-63; mcp/src/agents_remember/kernel/memory_ledger.py:168-177 |
| The reader whose last-value-wins rule forces the one-trailer constraint every plan case turns on. | `parse_code_commit_trailer` | mcp/src/agents_remember/kernel/memory_attribution.py:132-145 |
| The CLI adapter the command-path cases drive: its registered flags and its exit-status mapping. | `add_arguments`; `run` | mcp/src/agents_remember/cli/memory_backfill.py:41-73; mcp/src/agents_remember/cli/memory_backfill.py:76-97 |
| The runner option object the fixture commits through, which is the same identity mechanism the rewrite replays. | `GitRunnerOptions`; `run_git` | mcp/src/agents_remember/kernel/git_command.py:115-128; mcp/src/agents_remember/kernel/git_command.py:149-213 |
| The lane row that registers this module, so the evidence-lane manifest's derived-module check admits it. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:69-69 |
| The sibling module that holds the producer census for the same trailer transition, which this module's cases complement rather than duplicate. | `test_the_attribution_key_is_named_and_rendered_in_exactly_one_module` | mcp/tests/test_memory_attribution_producers.py:86-117 |

## Cross-Repo References

Every case builds both repositories it spans — a code repository and an external memory repository —
as real temporary Git repositories, which is why a trailer can be read back with git's own readers
rather than asserted from a returned string. The CLI cases add a third artifact they span: a real leaf
enclosure contract on disk, from which the adapter resolves both repositories. No production
cross-repository authority is claimed by this focused module.

| Finding | Anchor | Source |
| --- | --- | --- |
| The external-memory side of each case is a real second repository created by the fixture, not a mock, and both are discarded with the temporary directory. | `BackfillFixture`; `_commit` | mcp/tests/test_memory_backfill.py:134-223; mcp/tests/test_memory_backfill.py:78-90 |
| The contract the CLI cases resolve their repository pair from, written to disk as a real leaf contract rather than passed as arguments. | `contract_path`; `invoke` | mcp/tests/test_memory_backfill.py:770-829; mcp/tests/test_memory_backfill.py:831-838 |

## Update History

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
