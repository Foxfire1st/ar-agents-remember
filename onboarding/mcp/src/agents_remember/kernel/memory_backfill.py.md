# mcp/src/agents_remember/kernel/memory_backfill.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/memory_backfill.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T18:20+02:00 |
| lastVerifiedCommitHash | `270704b86116728a64ada83ee258a0e7726206b4` |
| lastVerifiedCommitDate | 2026-09-14T18:18:08+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

The **migration** half of the trailer transition. `kernel/memory_attribution.py` reads a
`Code-Commit:` attribution back out of a commit message; this module is what puts one there for the
memory history written before that rule existed. It derives which commits must receive a trailer
from the table that history already records, and rewrites exactly those commit objects with the
trailer appended. A memory commit older than the rule contributes its row from the ledger table its
own tree records, so the attribution is the form of that mapping which survives a hand edit to the
table.

**The tool is fixed and proven, and it has not been applied to any real repository.** Its evidence is
a disposable-fixture regression suite plus a read-only **plan** measurement of the real history; no
rewrite has been run on the real memory repository by this code, and the shared source line
`7317108b` still carries **0** trailers. The rewrite is deferred to this master's integration into
IAS, where the shared line's ids change anyway. An earlier, pre-fix confined attempt on this master's
own line (`7aa4cd97` → `df863a24`) was verified and then reverted by developer ruling, because
rewriting the shared ancestors renumbered them and left the master's memory line with no common
ancestor to its super; the plane's lineage gate then refused everything downstream. That reversal is
why the apply is a sequencing obligation rather than unfinished code.

## Measured State At The Two Tips

Counted read-only on the real memory repository. The shared source line and this master's memory tip
differ by the master's own commits, which is why the two columns differ at all.

| quantity | at the shared line `7317108b` | at this master's tip `7aa4cd97` |
| --- | --- | --- |
| tracked table rows (pairings) | 474 | 472 |
| distinct code commits | 419 | 428 |
| duplicate rows (a code sha beside several memory commits) | 55 | — |

The plan at `7aa4cd97`, which is what the selection is judged by, carries **455** memory commits and
names **418** of the table's 428 code commits. The 418 is the maximum any set of single-trailer
commits can reach there — confirmed independently with Hopcroft-Karp — and 455 of 455 named memory
commits receive a trailer. Ten code commits end with no trailer and each is reported as a
`LostClaim`. Against the review that found the defect: 52 of the 60 omitted pairings are now carried,
5 of the remaining 8 are provably uncarryable (two equally constrained claims with nothing to fall
back on) and 3 are the same tie resolved by the table's own order. A variant that scored 55 of 60
exists but selects its winner by hash order and was deliberately refused: the table's recorded order
decides.

**The bound is structural, not a shortfall of the matching.** 472 pairings compete for 455
single-trailer memory commits and at most 418 matchable code commits, so 455 pairings across 418 code
commits is the ceiling the format allows; the remaining rows are either duplicates of a pairing that
is carried or a contested claim whose loser is named. The 13 projection exclusions at the shared line
are two classes and only one of them is a rewrite problem: 11 name a memory commit that exists but
sits outside the tip's ancestry (orphaned by an earlier history edit, and they become ancestors at
this master's tip, where exclusions fall to 0), and 2 name no object at all —
`1e9f28bc0373eda5` and `54bdab74d49def84`. Those two are **permanently unreproducible by any
rewrite** and are reported as holes in the table rather than as declines.

The superseded figures, kept so a later reader can tell a re-measurement from a regression: the leaf
document that scoped this work carried 104 duplicate rows, 513 trailers to write and 10 skips, none
of which reproduce; the pre-fix plan reported 67 skips at the shared line (44
`row-is-not-the-oldest-for-its-code-commit`, 23 `memory-commit-not-reachable-from-the-tip`) and 44 at
the tip, under a four-literal vocabulary and an oldest-row-per-code-commit rule that no longer exist.

## Code Commentary

### Logic

`plan_memory_backfill` cit:([`plan_memory_backfill`], mcp/src/agents_remember/kernel/memory_backfill.py:257-308) is
read-only and is the dry run. It resolves `request.tip` to the exact commit it names BEFORE anything
else, so every fact downstream — the table, the digest, the rescue set — is stated about one object
rather than about a name that could move under the run. It then reads the table at that commit
(`ledger_rows_at` cit:([`ledger_rows_at`], mcp/src/agents_remember/kernel/memory_backfill.py:901-924), deliberately the
unvalidated structural parse because a header disagreeing with its own first row is one of the shapes
the projection repairs) and resolves both cells of every row to full object names (`_resolved_row`
cit:([`_resolved_row`], mcp/src/agents_remember/kernel/memory_backfill.py:311-324)). Calling it twice against an
unchanged history returns the same digest; calling it after `apply_memory_backfill` returns an empty
plan, which is what makes the plan its own idempotence proof.

**Classified by the row, never by the subject.** A commit subject is prose — it can say
`ledger: map ...` while touching onboarding, or claim index work while doing policy — so what a
commit is *for* is decided by the table's own `Code | Memory` rows, which are data.

**Every pairing the format can hold is carried, and the rule that chooses is declared.**
`%(trailers:key=Code-Commit,valueonly)` renders one line per matching trailer and the reader takes the
LAST, so one memory commit carries one code commit — and the table records more pairings than that
allows. `_choose_trailers`
cit:([`_choose_trailers`], mcp/src/agents_remember/kernel/memory_backfill.py:327-387) separates the rows the history
cannot support at all (`_row_skip_reason`
cit:([`_row_skip_reason`], mcp/src/agents_remember/kernel/memory_backfill.py:562-583)) from the carryable ones, and hands
those to `_select_pairings` cit:([`_select_pairings`], mcp/src/agents_remember/kernel/memory_backfill.py:434-497). The
selection has two halves, and the second is load-bearing rather than cosmetic.

- **A maximum matching.** `_maximum_matching`
  cit:([`_maximum_matching`], mcp/src/agents_remember/kernel/memory_backfill.py:515-540) is Kuhn's augmenting-path algorithm
  (`_augment` cit:([`_augment`], mcp/src/agents_remember/kernel/memory_backfill.py:543-559)), so no code commit is left
  unnamed while a memory commit that could have named it stands empty — the exact shape the previous
  rule got wrong, where a later assignment overwrote an earlier one in a dictionary keyed by memory
  commit and 16 code commits lost their mapping. The **size** of the result is order-independent; only
  *which* pairs pay for the maximum follows the offered order, and the offered order is where both
  halves of the preference live: code commits go **most constrained first** (fewest alternative memory
  commits), because a claim with nowhere else to go is the one a conflict must not displace, and ties
  between equally constrained claims go to the **oldest row**, read off the table with
  `_oldest_row_rank` cit:([`_oldest_row_rank`], mcp/src/agents_remember/kernel/memory_backfill.py:500-512) rather than
  off object names. A winner chosen by hash order is precisely what the review found the old rule
  doing; the alternative tie-break is the object name and was refused.
- **A fill step.** A matching is symmetric and the format is not: a code commit can be named by
  several memory commits while a memory commit carries only one, so one matching alone can never
  reach every named memory commit. Step two gives each of the 37 memory commits the matching did not
  reach its own oldest row. Those rows name code commits the matching already named, so they add no
  new code commit — what they add is the memory commit's OWN attribution, which is the whole record
  of a memory commit created to repair onboarding whose code counterpart was attributed earlier.
  Skipping them was the largest single source of the omissions the review measured.

**The rule chooses, so the rule says what it chose.** The skip vocabulary is closed at five literals
and splits into two families: `SKIP_MEMORY_COMMIT_MISSING`, `SKIP_MEMORY_COMMIT_UNREACHABLE` and
`SKIP_CODE_COMMIT_NOT_HELD` are **holes** in the history or the code repository that no selection
could repair, while `SKIP_MEMORY_COMMIT_CLAIMED` and `SKIP_CODE_COMMIT_ALREADY_NAMED`
cit:([`SKIP_REASONS_THE_RULE_CHOSE`], mcp/src/agents_remember/kernel/memory_backfill.py:99-99) are rows the rule
**declined**. `_decline_reason` cit:([`_decline_reason`], mcp/src/agents_remember/kernel/memory_backfill.py:390-403)
keeps the two declines apart: a row whose code commit another carried row already names is a
duplicate and costs the history nothing, while a row whose memory commit carries a different code
commit is a mapping genuinely gone. `SKIP_REASONS`
cit:([`SKIP_REASONS`], mcp/src/agents_remember/kernel/memory_backfill.py:87-93) orders all five so
`MemoryBackfillPlan.render` cit:([`render`], mcp/src/agents_remember/kernel/memory_backfill.py:200-224) reports every
rule on every run, zeroes included.

**A loss is named, not counted.** `_lost_claims`
cit:([`_lost_claims`], mcp/src/agents_remember/kernel/memory_backfill.py:406-431) returns one `LostClaim`
cit:([`LostClaim`], mcp/src/agents_remember/kernel/memory_backfill.py:130-141) per code commit no trailer names, carrying
the contested memory commit and the code commit that took it. Reporting a count alone was the gap:
an attribution that cannot be carried is a fact about the history a reader has to adjudicate, and the
winner is what makes the loss checkable against the diff that recorded it.

**The counts answer different questions and all of them are needed.** `assigned_attributions` is the
eligible set — rows that passed the history's own checks, before the one-trailer rule takes its share
(472 at `7aa4cd97`); `len(trailers)` is how many commits must be rewritten; `named_code_commits` is
the census the conflict rule is judged by and is deliberately NOT `len(trailers)`, because several
trailers legitimately name one code commit; and `lost_code_commits` is what keeps
`MemoryBackfillPlan` cit:([`MemoryBackfillPlan`], mcp/src/agents_remember/kernel/memory_backfill.py:145-224) honest.
`is_empty` cit:([`is_empty`], mcp/src/agents_remember/kernel/memory_backfill.py:182-193) is therefore **not** "there
are no trailers": a history can be fully written and still have lost a mapping, and a plan reporting
that as empty would claim a completeness the history does not have. The digest is taken over
`PlanMaterial` cit:([`PlanMaterial`], mcp/src/agents_remember/kernel/memory_backfill.py:586-605) — inputs, chosen
pairs, rewrites, skips AND losses — so two runs that lose different mappings cannot share a digest.

**Idempotent twice over, and the second reason is the stronger one.** The plan-level check is what
avoids 500-odd pointless rebuilds. Underneath it, `_rewrite_history`
cit:([`_rewrite_history`], mcp/src/agents_remember/kernel/memory_backfill.py:755-781) replays every commit that needs
neither a new trailer nor a moved parent through `git commit-tree` as itself, and that replay
reproduces the commit's object id exactly — verified 977 of 977 on the real history — so a run that
rebuilt everything would still move nothing.

**The rewrite changes messages and nothing else.** `_rebuild`
cit:([`_rebuild`], mcp/src/agents_remember/kernel/memory_backfill.py:794-818) replays the tree, the parents, the author
and committer identities and both timestamps, so a rebuilt commit differs from its original in its
trailer block alone and no two trees anywhere in the repository differ. The identity is replayed
through `%ai`/`%ci`, git's own `<timestamp> <tzoffset>` spelling
(`_IDENTITY_FIELDS` cit:([`_IDENTITY_FIELDS`], mcp/src/agents_remember/kernel/memory_backfill.py:106-106)) and deliberately
not through the strict ISO `%aI`/`%cI`: strict ISO renders a zero offset as `Z`, so a commit whose
header says `+0000` would come back saying `Z` and the replay would no longer be byte-for-byte the
object it replaces. `GitRunnerOptions.identity`
cit:([`GitRunnerOptions`], mcp/src/agents_remember/kernel/git_command.py:115-128) is what carries those names, because
`git commit-tree` reads them from the environment and from nowhere else.

**The order of `apply_memory_backfill`** cit:([`apply_memory_backfill`], mcp/src/agents_remember/kernel/memory_backfill.py:625-661)
is what makes it recoverable rather than merely careful, and the order of its guards is part of that.
The plan is derived and optionally pinned against the caller's previewed digest; the **empty-plan
short-circuit comes before the rescue-ref guard**, because a run with nothing to write rescues
nothing and a second run over an already-migrated history must be a no-op rather than a refusal about
refs the first run created. Only then does `_refuse_unsafe_rescue`
cit:([`_refuse_unsafe_rescue`], mcp/src/agents_remember/kernel/memory_backfill.py:672-688) check that the rescue ref
lives under `refs/`, is not one of the refs the run moves, and does not already exist.
`_write_rescue_refs` cit:([`_write_rescue_refs`], mcp/src/agents_remember/kernel/memory_backfill.py:691-728) writes the
rescue set for the tip and every named ref **and reads each one back** while every original commit is
still the tip of a live ref, and `_move_targets`
cit:([`_move_targets`], mcp/src/agents_remember/kernel/memory_backfill.py:837-879) then creates the new objects and
moves the named refs in ONE `git update-ref --stdin` transaction, so a refusal part-way through leaves
either every ref moved or none of them.

**Every name is resolved to an exact commit before any ref is written.** `_resolve_commit`
cit:([`_resolve_commit`], mcp/src/agents_remember/kernel/memory_backfill.py:731-748) is applied to the tip and to every
target when the rescue set is built, and `_full_ref_name`
cit:([`_full_ref_name`], mcp/src/agents_remember/kernel/memory_backfill.py:882-898) resolves each target to git's own
full ref spelling before the transaction is assembled. Both are the same bug class the review found
in two places, and neither is tidiness: `request.tip` is a ref NAME on the ordinary path — the CLI
passes the contract's memory work branch — so a rescue set verified against a name can never read
back equal to a hash, and the run would write its rescue refs and then refuse, leaving a refusal that
has already mutated the repository plus a retry that trips the existing-ref check on refs its own
predecessor created. Likewise `update-ref --stdin` takes ref names for git to write, and a branch
short name is only resolved against `refs/heads/` where git chooses to. The tip is compared by
resolved commit and the transaction is guarded by the value it expects, so a ref that moved between
the plan and the move is refused by git rather than overwritten.

**The map from old to new ids is total**, so a caller holding an original id — the table it just
read, a contract cell, a saved plan — always finds its replacement and never has to know which
commits happened to move; unchanged commits map to themselves, which is what makes "the identity map
is the idempotence proof" literally true. `carry_ledger_cells`
cit:([`carry_ledger_cells`], mcp/src/agents_remember/kernel/memory_backfill.py:927-972) is the second half of the
migration: a message rewrite changes the id of every commit it touches, and the tracked table that
records those commits still names the old ids, so a source read straight after a rewrite would report
every recorded row as excluded. The carry resolves each cell through git before mapping it
(`_full_name` cit:([`_full_name`], mcp/src/agents_remember/kernel/memory_backfill.py:1004-1012)), because the tracked
table really does carry an abbreviated cell beside full ones and a textual find-and-replace cannot
tell an eight-character prefix from the first eight characters of some other full id — it would
silently leave the abbreviation naming the old commit, which is exactly one excluded row surviving a
migration that otherwise reads clean. The header is not recomputed from scratch: the code column and
`baseCodeCommit` are carried through untouched because memory commits are what move, while
`baseMemoryCommit` and the two `last*` fields move with the column they name.

### Conventions

A frozen-dataclass family — `TrailerToWrite`, `SkippedRow`, `LostClaim`, `MemoryBackfillPlan`,
`MemoryBackfillRequest`, `MemoryBackfillResult`, `PlanMaterial` — over plain module-level functions
taking `Path`s, mirroring `kernel/memory_ledger.py` and `kernel/memory_attribution.py`. All four
request facts travel in one object because no rewriting run is meaningful without them, and the two
that are easy to leave implicit are the two that make it safe: `rescue_ref` is the only undo a
message rewrite has, and `update_refs` is the complete list of refs the run may move, so a branch
nobody named cannot be touched by accident. One command reads several commit fields at once through a
`\x1f`-joined `--format`
(`_commit_fields` cit:([`_commit_fields`], mcp/src/agents_remember/kernel/memory_backfill.py:992-1001)), and
`MemoryBackfillRefusal` is a `RuntimeError` so a caller can print it as a refusal line. The selection
is computed in one place (`_select_pairings` and its three helpers) rather than folded into the
census, so which pairings survive is readable as an algorithm instead of as a dictionary's iteration
order.

### Invariants And Boundaries

- **The trigger for a rewrite is the row, not the subject.** A commit is rewritten because the table
  says it records a code commit, never because its message reads a certain way.
- **One memory commit carries one code commit, and the selection has two halves.** A maximum matching
  first, so no code commit is left unnamed while a memory commit that could have named it stands
  empty, then a fill that gives every memory commit the matching did not reach its own oldest row.
  Dropping the fill is not a simplification: a matching is symmetric and the format is not, so it
  leaves dozens of named memory commits unattributed.
- **A conflict resolves on the table's recorded order, never on a hash.** The table is newest-first,
  so the bottom-most row naming a pair is the pairing recorded first and it wins; code commits are
  offered most-constrained-first and ties go to the older claim. A winner chosen by object name is
  the defect this rule exists to exclude, and the variant that did so was refused even though it
  scored higher.
- **The skip vocabulary is closed at five literals and split in two.** Three are holes no selection
  can repair; two are declines the rule chose, exported as `SKIP_REASONS_THE_RULE_CHOSE`, and the two
  declines are kept apart because a duplicate costs nothing while a lost mapping does.
- **A loss is named with its winner.** `LostClaim` carries the code commit, the contested memory
  commit and the code commit that took it; a bare count would not be adjudicable.
- **A plan that lost a mapping is never empty.** `is_empty` includes `lost_code_commits`, so a fully
  written history that dropped a pairing still reports work, and the digest covers the losses so a
  previewed digest cannot authorize a different decision.
- **Every name is resolved to an exact commit before the first ref is written.** The tip, the rescue
  set and every moved target; a name that cannot be restored refuses rather than being recorded.
- **The empty-plan check precedes the rescue-ref guard.** A retry over an already-migrated history is
  a no-op, not a refusal about the rescue refs its own predecessor created.
- **The table is the input, and the table is carried afterwards.** A run that rewrote the history and
  left the table naming the old ids would report every recorded row as excluded; `carry_ledger_cells`
  is part of the migration, not an optional tidy-up.
- **A rescue ref is written and read back before the first new object exists.** No `git revert`
  restores a rewritten commit object, so the rescue ref is the only undo this operation has, and an
  existing rescue ref refuses a run that would rewrite something.
- **All refs move in one transaction, or none do.** `update-ref --stdin` is the only ref-mutation
  path here; a run never leaves half the named refs on the new history.
- **Only the named refs move.** `update_refs` is the complete permission list, and a ref whose commit
  maps to itself is skipped rather than reported as a move.
- **The rewrite is byte-faithful apart from the trailer.** Tree, parents, identities and both
  timestamps are replayed exactly, and the dates are read in git's internal spelling rather than
  strict ISO so a `+0000` offset is not rewritten as `Z`.
- **A no-op is an exact no-op.** A second run over a migrated history plans nothing and moves no ref;
  a rebuild of an untouched commit reproduces its object id.
- **Two rows are permanently unreproducible.** A memory cell naming no object cannot be given a
  trailer by any rewrite and is reported as a hole in the table rather than as a decline.
- **The format's ceiling is a measured fact, not a shortfall.** 472 pairings compete for 455
  single-trailer memory commits and at most 418 matchable code commits, so the selection is judged
  against that bound and every code commit outside it is named.
- **Nothing here is a lifecycle authority.** The module reads and rewrites Git objects; whether a
  rewrite should happen, and when, is the developer's ruling and this master's integration step.

### Todos

None. The fixed tool has not been applied to any real repository and its evidence is fixtures plus a
read-only plan measurement; the deferred apply is a recorded sequencing obligation owned by this
master's integration into IAS, not unfinished work in this module. The measurement that ended the
apply-first plan — the shared line and its dependents, not the tool — is recorded on the route
overview and in this card's history rather than as a code TODO.

## Docs References

The trailer is git's own mechanism rather than a repository-local format, and the module depends on
no documented git behaviour beyond `%(trailers:key=...)` rendering, `git commit-tree` reading its
author and committer from the environment, `git rev-list --reverse --all`, and
`git update-ref --stdin`. The repository's configured `system/sources.md` names no Domain
Documentation source for this code repository, so no external document is cited here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured for this repository; the proving evidence is git's own trailer rendering and commit plumbing plus this repository's source. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The plan is the dry run: the tip resolved to an exact commit first, the table at that commit, both cells resolved to full object names, and a digest over the inputs, the decision and the losses. | `plan_memory_backfill`; `ledger_rows_at`; `_resolved_row`; `PlanMaterial`; `_plan_digest` | mcp/src/agents_remember/kernel/memory_backfill.py:257-308; mcp/src/agents_remember/kernel/memory_backfill.py:901-924; mcp/src/agents_remember/kernel/memory_backfill.py:311-324; mcp/src/agents_remember/kernel/memory_backfill.py:586-605; mcp/src/agents_remember/kernel/memory_backfill.py:608-622 |
| The selection's two halves: a maximum matching offered most-constrained-first with the older claim winning a tie, then the fill that gives every unreached memory commit its own oldest row. | `_select_pairings`; `_maximum_matching`; `_augment`; `_oldest_row_rank` | mcp/src/agents_remember/kernel/memory_backfill.py:434-497; mcp/src/agents_remember/kernel/memory_backfill.py:515-540; mcp/src/agents_remember/kernel/memory_backfill.py:543-559; mcp/src/agents_remember/kernel/memory_backfill.py:500-512 |
| The closed five-literal vocabulary and its two families: holes no selection can repair, and the declines the rule chose. | `SKIP_REASONS`; `SKIP_REASONS_THE_RULE_CHOSE`; `_choose_trailers`; `_row_skip_reason`; `_decline_reason`; `SkippedRow` | mcp/src/agents_remember/kernel/memory_backfill.py:87-93; mcp/src/agents_remember/kernel/memory_backfill.py:99-99; mcp/src/agents_remember/kernel/memory_backfill.py:327-387; mcp/src/agents_remember/kernel/memory_backfill.py:562-583; mcp/src/agents_remember/kernel/memory_backfill.py:390-403; mcp/src/agents_remember/kernel/memory_backfill.py:122-127 |
| A loss is named with the memory commit that took the pairing, and the plan cannot report empty while one exists. | `LostClaim`; `_lost_claims`; `is_empty`; `MemoryBackfillPlan` | mcp/src/agents_remember/kernel/memory_backfill.py:130-141; mcp/src/agents_remember/kernel/memory_backfill.py:406-431; mcp/src/agents_remember/kernel/memory_backfill.py:182-193; mcp/src/agents_remember/kernel/memory_backfill.py:145-224 |
| The four counts that must stay apart: eligible rows, commits to rewrite, code commits named, and code commits no trailer can name. | `MemoryBackfillPlan`; `render`; `count_of` | mcp/src/agents_remember/kernel/memory_backfill.py:145-224; mcp/src/agents_remember/kernel/memory_backfill.py:200-224; mcp/src/agents_remember/kernel/memory_backfill.py:195-198 |
| The recoverable order with its guards in the right sequence: plan, digest pin, empty-plan short-circuit, rescue guard, name resolution, rescue refs, one transaction. | `apply_memory_backfill`; `_require_expected_digest`; `_refuse_unsafe_rescue`; `_write_rescue_refs`; `_resolve_commit`; `_move_targets`; `_full_ref_name` | mcp/src/agents_remember/kernel/memory_backfill.py:625-661; mcp/src/agents_remember/kernel/memory_backfill.py:664-669; mcp/src/agents_remember/kernel/memory_backfill.py:672-688; mcp/src/agents_remember/kernel/memory_backfill.py:691-728; mcp/src/agents_remember/kernel/memory_backfill.py:731-748; mcp/src/agents_remember/kernel/memory_backfill.py:837-879; mcp/src/agents_remember/kernel/memory_backfill.py:882-898 |
| The total identity map and the byte-faithful replay: parents are decided oldest-first, unchanged commits map to themselves, and the dates come back in git's internal spelling rather than strict ISO. | `_rewrite_history`; `_rebuild`; `_identity`; `_IDENTITY_FIELDS` | mcp/src/agents_remember/kernel/memory_backfill.py:755-781; mcp/src/agents_remember/kernel/memory_backfill.py:794-818; mcp/src/agents_remember/kernel/memory_backfill.py:821-834; mcp/src/agents_remember/kernel/memory_backfill.py:106-106 |
| The table carry that makes a rewritten history read clean again, resolving each cell through git before mapping it so an abbreviated cell cannot survive as a text prefix. | `carry_ledger_cells`; `_full_name` | mcp/src/agents_remember/kernel/memory_backfill.py:927-972; mcp/src/agents_remember/kernel/memory_backfill.py:1004-1012 |
| The one writer of the trailer this module appends, and the one reader whose last-value-wins rule forces the one-trailer constraint. | `render_memory_content_message`; `parse_code_commit_trailer` | mcp/src/agents_remember/kernel/memory_attribution.py:72-97; mcp/src/agents_remember/kernel/memory_attribution.py:132-145 |
| The ledger format this module reads and rewrites, and the path that moved here from the projection because the path is a property of the ledger. | `LEDGER_RELATIVE_PATH`; `parse_ledger_text_unvalidated`; `ledger_to_text`; `LedgerRow` | mcp/src/agents_remember/kernel/memory_ledger.py:25-25; mcp/src/agents_remember/kernel/memory_ledger.py:66-125; mcp/src/agents_remember/kernel/memory_ledger.py:180-205; mcp/src/agents_remember/kernel/memory_ledger.py:28-31 |
| The runner option object that carries the identity `git commit-tree` can only be told by environment, and the single-Python-module function whose signature it replaced. | `GitRunnerOptions`; `run_git` | mcp/src/agents_remember/kernel/git_command.py:115-128; mcp/src/agents_remember/kernel/git_command.py:149-213 |
| The CLI adapter that makes the plan the default and refuses any target the leaf contract does not name. | `add_arguments`; `run`; `_apply` | mcp/src/agents_remember/cli/memory_backfill.py:41-73; mcp/src/agents_remember/cli/memory_backfill.py:76-97; mcp/src/agents_remember/cli/memory_backfill.py:100-114 |
| The regression module that pins the rule, the reported loss, the trailer-only acceptance proof, the byte-faithful replay and the CLI's own retry. | `MemoryBackfillPlanTests`; `MemoryBackfillApplyTests`; `MemoryBackfillCliTests` | mcp/tests/test_memory_backfill.py:226-396; mcp/tests/test_memory_backfill.py:399-629; mcp/tests/test_memory_backfill.py:754-902 |

## Cross-Repo References

The memory repository this module rewrites is a separate Git repository addressed through the worktree
contract rather than an ambient checkout, and the code repository is read for exactly one fact so a
trailer can never name a code commit that does not exist. Both are real repositories on disk; nothing
here reaches a network or a sibling implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| The ledger table is read at a commit in the memory repository the caller names, never through an inherited Git selector. | `ledger_rows_at`; `_walk` | mcp/src/agents_remember/kernel/memory_backfill.py:901-924; mcp/src/agents_remember/kernel/memory_backfill.py:784-791 |
| The one cross-repository truth test: a trailer is written only for a code commit the code repository actually holds. | `_code_commit_is_held` | mcp/src/agents_remember/kernel/memory_backfill.py:1023-1024 |
| The leaf contract is the write guard the CLI resolves the pair of repositories from, so no argument list can aim a history rewrite at the official memory repository by hand. | `load_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:434-464 |

## Update History

- 2026-09-14T18:20+02:00 — 260913-LCA-L3 curator (same uncommitted change set,
  `ar/260913-lca-l3-ar`, base `7317108b`): **an externally reviewed defect pair was fixed and this
  card now describes the fixed tool.** The selection is no longer "keep the last row per code commit,
  last assignment wins": `_select_pairings` computes a maximum matching (Kuhn, code commits offered
  most-constrained-first with the older claim winning a tie, read off the table rather than off object
  names) and then a **fill** giving every memory commit the matching did not reach its own oldest row
  — load-bearing, because a matching is symmetric and the format is not, so a matching alone left
  dozens of named memory commits unattributed. Measured at `7aa4cd97`: 418 of 428 code commits named
  (confirmed maximal with Hopcroft-Karp), 455 of 455 named memory commits trailered, 52 of the
  review's 60 omitted pairings recovered, 10 code commits reported through `lost_claims`. Recorded the
  structural bound (472 pairings, 455 single-trailer memory commits, at most 418 matchable code
  commits; 5 of the remaining 8 losses provably uncarryable and 3 the same tie resolved by the table's
  order) and that a 55-of-60 variant selecting by hash order was deliberately refused. The skip
  vocabulary is now five literals in two families — holes versus declines, the latter exported as
  `SKIP_REASONS_THE_RULE_CHOSE` — with `LostClaim(code_commit, memory_commit, winner)` naming each
  loss; `assigned_attributions` now means the eligible set before the rule; the old
  `attributions_one_commit_cannot_carry` property is gone; and `is_empty` includes `lost_code_commits`
  so a plan that lost a mapping can never report empty. The second finding: every name is resolved to
  an exact commit before any ref is written (`_resolve_commit`, `_full_ref_name`) and the empty-plan
  check now precedes the rescue-ref guard, so a retry is a no-op instead of a refusal about refs its
  own predecessor created. States plainly that the tool is fixed and proven on fixtures plus a
  read-only plan measurement and **has not been applied to any real repository**; the earlier
  pre-fix confined attempt stays recorded as the reason the rewrite is deferred to this master's
  integration into IAS. The superseded pre-fix figures (67/44 skips, four-literal vocabulary,
  0/7 already trailered) are kept in the measurement section as re-measurement history. Every citation
  in this card was re-derived against the grown module (686 → 1024 lines). Verification metadata
  remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-09-14T17:20+02:00 — 260913-LCA-L3 curator (uncommitted change set on `ar/260913-lca-l3-ar`,
  base `7317108b`): created the one-to-one sidecar for this new kernel module. Records the three
  contract properties and why each is forced (classified by the row rather than the subject; one
  trailer chosen by the oldest-row-per-code-commit rule because the reader takes the last and the
  table is newest-first; idempotence both at the plan and at the object id, the latter verified
  977/977), the closed four-literal skip vocabulary, the total old→new identity map and the
  `carry_ledger_cells` table carry that has to accompany it, the rescue-ref-before-first-object and
  one-`update-ref --stdin` ordering, and the `%ai`/`%ci`-not-`%aI` identity replay. Records the
  measured census at the shared line `7317108b` (474 rows, 419 distinct code commits, 0 trailered, 67
  skips — 44 row-is-not-the-oldest and 23 memory-commit-not-reachable — and 13 exclusions, of which
  11 are reachable-at-the-tip orphans and 2 name no object at all) and at this master's tip
  `7aa4cd97` (472 rows, 428 distinct code commits, 7 trailered, 44 skips, 0 exclusions), and marks
  the scoping document's earlier 104/513/10 census as not reproducible. States the reversal plainly:
  the confined apply was verified and then reverted by developer ruling because rewriting the shared
  ancestors removed the master's common ancestor with its super and the lineage gate refused
  downstream, so the shared line still carries 0 trailers and the backfill is an explicit step at
  this master's integration into IAS. Verification metadata names the leaf's base commit and remains
  closeout-owned; no acceptance claim and no verification stamp advanced.
