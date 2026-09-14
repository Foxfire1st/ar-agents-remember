# mcp/tests/test_memory_ledger.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_ledger.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T11:58+02:00 |
| lastVerifiedCommitHash |  `187414cef8150a8004fc1b023a8377f77b24e873`|
| lastVerifiedCommitDate |  2026-09-14T12:13:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused kernel-level proof that the external-memory ledger is newest-first state history rather
than a globally unique code-to-memory map — and, since 260913-LCA-L2, that the ledger's *source* is
the memory commits' own `Code-Commit:` attribution rather than the tracked `memory.md` blob.

## Code Commentary

### Logic

The first scenario starts from one code/memory edge, prepends a later memory commit for the same code
commit, round-trips the canonical text, and proves both views of authority: `find_mapping` returns the
newest memory state while `contains_mapping` still finds the older exact audit edge.

The rest of the file is two fixture worlds over the projection. `_World`
cit:([`_World`], mcp/tests/test_memory_ledger.py:81-130) writes an ordinary ledger blob and a side
branch, and the six `test_projection_*` cases built on it predate the trailer rule: nothing in that
fixture carries a trailer, so every one of them reaches `read_ledger_source` through the read of the
source's **own recorded table** — which since 260913-LCA-L11 is the path every source takes, the
trailers merely being merged into it. The attribution group is `_AttributedWorld`
cit:([`_AttributedWorld`], mcp/tests/test_memory_ledger.py:323-379), a line where each mapping is two
commits — the content commit carrying `Code-Commit: <sha>` and the ledger commit pinning the row
into `memory.md` and carrying none — with one code commit attributed twice (the superseding pair
the ledger keeps both copies of) and one memory commit carrying no trailer at all.

**Two cases added by 260913-LCA-L11, both about what a read may lose.** The first,
`test_a_source_row_the_source_cannot_carry_is_reported_not_kept` (`:473-502`), is the class that
made a real leaf's ledger read as damaged: a table row whose memory commit is not in the source's
ancestry is now **excluded at the read with its reason** (`source.excluded_rows` carrying
`memory-commit-unreachable`) instead of being carried into the projection to be dropped there — the
drop becomes the projection's own stated decision rather than a silent one. The second,
`test_a_partially_trailered_source_still_reads_its_pre_rule_rows` (`:503-532`), is the reader's
second defect made permanent: a source whose table records hundreds of rows and whose history
carries exactly ONE trailer must still read the pre-rule rows, because the reader used to return the
trailers *alone* as soon as there was one — a one-row source for a 479-row line, which is the
"looks like no attribution exists" failure in its most expensive form. It asserts
`source.trailered_commits == 1` and that both the trailered row and the pre-rule row survive.

The helper `_content_commit` (`:466-472`) exists because of the first of those: a row's memory cell
must now name a commit the repository really holds, since the read asks git rather than comparing
strings, so the pre-rule case's placeholder 40-character cells were replaced with real commits.

The ten added cases are the acceptance surface for the projection change. The closed-loop case
walks **every checkpoint** of that line and asserts the projected rows equal the rows the tracked
table carried at the same commit. The hand-edit case writes a row into the table under a matching
header and asserts the projection does not move. The pre-trailer case proves a history with no
trailer anywhere reads its own blob, and the empty-source case proves a source with neither
contributes no rows rather than refusing. The remaining cases are the readers' own rules:
`exclude` selects a branch's own commits, the parse takes the last trailer block and ignores a body
mention, a trailer naming a commit the code repository lacks is not a mapping, a final block with
several trailers is read by key, and a mapping that arrived through a merge is still found because
it is still an ancestor.

The tenth case is the cross-boundary one:
cit:([`test_the_rendered_trailer_is_the_one_the_reader_parses`], mcp/tests/test_memory_ledger.py:634-671) renders the trailer through the
**real writer** (`EffectiveCloseoutInput.memory_content_message`, which since 260913-LCA-L4 delegates to
the kernel's one renderer), commits that message as a real memory commit, and reads the code
commit back out with `attributed_commits` / `ledger_rows_from_attribution` /
`parse_code_commit_trailer`. It exists because the writer and the reader had briefly held two separate
`Code-Commit` literals: a writer whose key the reader does not parse loses the row entirely, and that
looks like "no attribution exists" rather than like a bug. Nothing in the case restates the key — it
goes through the writer and the trailer walk — because a case comparing one literal with another
could not catch a changed constant.

### Conventions

The scenario uses the public immutable ledger helpers directly, plus the attribution module's public
readers (`attributed_commits`, `ledger_rows_from_attribution`, `parse_code_commit_trailer`) and, for
the round-trip case, the writer's `EffectiveCloseoutInput`/`EnabledCloseoutLeg` and
`CODE_COMMIT_TRAILER_KEY`. Since 260913-LCA-L4 that constant is imported from
`agents_remember.kernel.memory_attribution` rather than from `agents_remember.models.closeout.input`
(`:11`): the writing model no longer names the key at all, so the kernel module is the only place the
module under test can read it from — the key's declaration and its one interpolation now live there
together. The
attribution fixture writes real 40-character object names rather than labels, because git reads a
trailing block as a trailer only when the value looks like an object name; `CODE_ONE`/`CODE_TWO`/
`CODE_OWN` are those names. Each checkpoint records an immutable `tuple` snapshot of its rows, so a
later mapping cannot edit a checkpoint that was already asserted. `_commit` gained `--allow-empty`
and `_ledger` now tolerates an empty row list, because a checkpoint can pin the same bytes twice and
the bootstrap checkpoint has no rows yet — without both, the fixture could not represent the
unattributed commit at all.

**The literal `Code-Commit` text in this module is deliberate, and must not be "corrected" to read the
constant.** The trailer-parse cases and the mixed-trailer-block case spell the key out on purpose:
they are independent oracles, and a case that read `CODE_COMMIT_TRAILER_KEY` would follow a wrong
constant instead of catching it. Only the round-trip case touches the constant, and it does so to
prove the *writer* uses it, not to define what the reader accepts.

The module is registered in the `unit-regression` evidence lane
(`mcp/tests/test-evidence-lanes.toml`). A lane registration says where the module executes; it is not
a recorded execution, and a focused run outside the delivery graph is not acceptance evidence.

### Invariants And Boundaries

- Repeated code commits are valid when they record ordered memory states.
- The newest matching row is current authority.
- Older exact rows remain preserved audit history.
- The projection answers from the attribution, not from the live table; a table edit is not a
  mapping.
- The source's own recorded table is read on every path, not as a fallback: the `_World` cases
  depend on it, and a partially trailered line depends on it more (the trailers merge into it).
- A row the source cannot prove is excluded at the read with a recorded reason and a count, never
  dropped in silence; a placeholder memory cell is now a row the read reports rather than keeps.
- This test does not weaken ledger schema, metadata, or first-row validation.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this repository-local ledger format.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is required for this repository-owned regression contract. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused scenario proves newest current lookup and exact historical containment after round-trip serialization. | `test_roundtrip_preserves_newest_same_code_history` | mcp/tests/test_memory_ledger.py:43-65 |
| The kernel owns the current-versus-historical lookup distinction. | `find_mapping`; `contains_mapping` | mcp/src/agents_remember/kernel/memory_ledger.py:255-257; mcp/src/agents_remember/kernel/memory_ledger.py:260-268 |
| The pre-trailer projection cases: untrue rows dropped, the source tail restored to source order, a disagreeing header recomputed, an already-correct table left byte-identical, metadata the projection did not compute preserved, and an unreadable source refused with its remedy. Every one of them reads the source's own recorded table directly, which is the path every source takes; none of them carries a trailer. | `test_projection_drops_a_row_whose_memory_content_never_landed`; `test_projection_moves_the_source_ledger_back_to_the_tail`; `test_projection_recomputes_a_header_that_disagrees_with_its_first_row`; `test_projection_leaves_an_already_correct_ledger_byte_identical`; `test_projection_keeps_the_metadata_it_did_not_compute`; `test_projection_refuses_an_unreadable_source_ledger_with_a_remedy` | mcp/tests/test_memory_ledger.py:168-196; mcp/tests/test_memory_ledger.py:197-222; mcp/tests/test_memory_ledger.py:223-247; mcp/tests/test_memory_ledger.py:248-265; mcp/tests/test_memory_ledger.py:266-279; mcp/tests/test_memory_ledger.py:280-302 |
| The closed loop: the projection at every checkpoint of a realistic attributed line equals the rows that checkpoint's tracked table carried, including the superseding pair, and each code commit resolves to the same memory commit the table did. | `test_projection_is_the_ledger_the_attributed_history_records` | mcp/tests/test_memory_ledger.py:382-411 |
| The trailers decide: a row hand-written into the table under a matching header does not appear in the projection. | `test_projection_reads_the_trailer_and_never_the_live_table` | mcp/tests/test_memory_ledger.py:412-433 |
| The pre-trailer history reads its own recorded table, with cells that name real commits because the read asks git rather than comparing strings. | `test_projection_reads_an_unattributed_commit_from_its_own_ledger` | mcp/tests/test_memory_ledger.py:434-465 |
| **New at 260913-LCA-L11:** a source row whose memory commit the source does not carry is excluded at the read with its reason (`memory-commit-unreachable`) and reported in `excluded_rows`, rather than carried into the projection to be dropped there — the class that made a real leaf's ledger read as damaged. | `test_a_source_row_the_source_cannot_carry_is_reported_not_kept` | mcp/tests/test_memory_ledger.py:473-502 |
| **New at 260913-LCA-L11:** one trailer must not hide the history the trailer rule never reached. A line whose table records many rows and whose history carries exactly ONE trailer still reads its pre-rule rows, because the reader used to return the trailers alone as soon as there was one. | `test_a_partially_trailered_source_still_reads_its_pre_rule_rows` | mcp/tests/test_memory_ledger.py:503-532 |
| The one-row helper the new exclusion rule forced: a row's memory cell must name a commit the repository holds. | `_content_commit` | mcp/tests/test_memory_ledger.py:466-472 |
| A source with no trailer anywhere and no ledger blob contributes no rows instead of refusing — the bootstrap state. | `test_projection_contributes_nothing_for_a_source_that_says_nothing` | mcp/tests/test_memory_ledger.py:533-541 |
| `exclude` selects a branch's own attributed commits and not the source's. | `test_attribution_reads_only_the_commits_a_caller_asks_for` | mcp/tests/test_memory_ledger.py:542-560 |
| The message parse takes the last trailer block, ignores a body mention of the key, and rejects a value that is not an object name. | `test_trailer_parse_takes_the_last_block_and_ignores_a_body_mention` | mcp/tests/test_memory_ledger.py:561-586 |
| A trailer naming a commit the code repository does not hold is not a mapping; the row-level truth test is opt-in and drops it. | `test_attribution_reports_only_commits_the_code_repository_holds` | mcp/tests/test_memory_ledger.py:587-601 |
| A final trailer block holding several trailers is read by key rather than by last line. | `test_attribution_reads_a_message_whose_final_block_carries_several_trailers` | mcp/tests/test_memory_ledger.py:602-633 |
| A merged-in mapping is still an ancestor, and the case asserts the second parent really is off the first-parent line so a first-parent walk could not have found it. | `test_attribution_reads_a_mapping_that_arrived_through_a_merge` | mcp/tests/test_memory_ledger.py:672-703 |
| The readers under test: the attribution walk, the row map, and the message parse. | `attributed_commits`; `ledger_rows_from_attribution`; `parse_code_commit_trailer` | mcp/src/agents_remember/kernel/memory_attribution.py:148-181; mcp/src/agents_remember/kernel/memory_attribution.py:213-232; mcp/src/agents_remember/kernel/memory_attribution.py:132-147 |
| The cross-boundary case: the real writer renders the trailer, the message is committed, and the real reader resolves the code commit out of it — the guard against the writer and the reader holding two `Code-Commit` literals. | `test_the_rendered_trailer_is_the_one_the_reader_parses` | mcp/tests/test_memory_ledger.py:634-671 |
| The single key both sides use: declared in the kernel reader **and rendered there**, and imported by this test module from that kernel module (`:11`) rather than from the writing model, which stopped naming it at 260913-LCA-L4. | `CODE_COMMIT_TRAILER_KEY`; `render_memory_content_message` | mcp/src/agents_remember/kernel/memory_attribution.py:56-56; mcp/src/agents_remember/kernel/memory_attribution.py:72-98; mcp/tests/test_memory_ledger.py:11-11 |
| The producer census that now owns the one-definition rule the round-trip case guards behaviourally. | `test_the_attribution_key_is_named_and_rendered_in_exactly_one_module`; `test_every_census_producer_reaches_the_shared_renderer` | mcp/tests/test_memory_attribution_producers.py:86-137 |
| The writer path the round-trip case drives, now a delegation to the kernel renderer instead of a local f-string. | `memory_content_message` | mcp/src/agents_remember/models/closeout/input.py:148-166 |
| The evidence lane the module executes in, which is where it runs rather than proof that it ran. | "mcp/tests/test_memory_ledger.py" | mcp/tests/test-evidence-lanes.toml:73-73 |

## Cross-Repo References

No cross-repository implementation source governs this focused unit.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
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
