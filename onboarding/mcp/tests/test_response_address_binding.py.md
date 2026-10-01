# mcp/tests/test_response_address_binding.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The guidance a tool response carries must be bound to **that response's own task**. This module
pins the three repairs `260918-TSIP-L6` landed around one mechanism: the address guard in
`application/tool_response.py::bound_next_step` (`T54`), the refreshed-onboarding census in
`worktrees/modules/closeout.py` (`T71`), and the `ok`/`state` pair in
`memory_quality/style/citations/migration.py` (`T64`).

**The recorded defect (`T54`).** A `worktree_closeout_apply` response for one leaf of one master
shipped a `nextStep` whose `nextArgs.contract_path` named a **different master's** contract, while
the outer `nextTool` named the caller's own operation. The closeout itself was unambiguous — the
right state, the right commits, the right leaf — and only the guidance block, the thing a seat is
told to follow, pointed into another task's enclosure.

**The mechanism, traced rather than assumed.** Guidance is produced by
`application/next_step.py::next_step_for` from the *process-global* ambient lifecycle: it reads
`LifecycleState.enclosure` and runs the worktree state machine against that contract, while the
response has its own address. The only thing connecting them is `bound_next_step`, and it fired
on neither of its exits for the recorded payload: it returned the step unchecked when the
response declared **no** contract path (a closed closeout declared none, because `status_payload`
emits the snake_case `contract_path` while the guard reads the envelope's
`contractPath`/`enclosurePath`), and it required the guidance's path set to be **exactly**
`{expected}`, so a hint carrying both spellings survived when only one of them was the
response's. Both are repaired, and `_closed_result_payload` now declares its own `contractPath`.

## Code Commentary

### Logic

**The guard's four cases, at the guard's own level.** `guidance` (`:60-75`) builds the shape the
worktree state machine emits — both spellings set to the contract file, as all four producers do
— and `closeout_response` (`:76-81`) builds a real `WorktreeCloseoutApplyResponse`, so the guard
is driven by the envelope it will meet.

- `test_guidance_naming_another_task_is_withheld_from_a_response_with_no_address` (`:82-94`) is
  the recorded `T54` shape: the response declares nothing, so nothing could be checked, and the
  guidance is withheld rather than emitted unchecked. This is the case the old guard let through.
- `test_guidance_agreeing_with_the_responses_own_address_is_kept` (`:95-109`) is the positive
  control: without it the repair above would be satisfied by dropping every hint, which would cost
  a seat the operational chain the guidance exists to carry.
- `test_one_stale_path_spelling_is_enough_to_withhold_the_guidance` (`:110-122`) pins the second
  exit in both directions: a hint whose `contract_path` agrees but whose `enclosure_path` does not
  is withheld, and the reverse too.
- `test_guidance_that_names_no_artifact_is_left_alone` (`:123-133`) keeps the guard from becoming
  a blanket refusal — guidance with no path in its args cannot contradict anything.

**`T71`: a list that counts entries it cannot name.** The closeout payload read
`item["source_path"]` alone, so every regenerated **document** entry — appended by
`worktrees/modules/onboarding.py::_refresh_regenerated_documents` with `source_path: ""` because
it has no source file — arrived as a blank string, and the payload reported a `count` that
included entries its own sample could not name.
`test_the_refreshed_onboarding_census_names_every_entry_it_counts` (`:134-175`) drives
`_refreshed_onboarding_paths` (`mcp/src/agents_remember/worktrees/modules/closeout.py:127-141`)
and `_bounded_paths`, and requires each entry to be named by its `source_path` **or** its
`onboarding_file`, with a blank refused rather than counted.

**`T64`: a preview must not read a post-write measurement.**
`_migration_payload` (`:189-210`) and `_declined_item` (`:211-224`) build the producer's own
payload through the real `migration.payload`, and
`test_a_migration_preview_reports_its_outcome_instead_of_a_bare_not_ok` (`:225-291`) pins the
truth table: a dry run that produced its complete plan with nothing declined answers `ok: true`,
`state: "planned"`, `findingsRemaining: null` — `remaining` is a post-write measurement and
reading it while previewing would report a plan as a failure, which is `T64`'s symptom returning
through the other fact the old `ok` folded in. A decline answers `ok: false`, `state: "refused"`.

**The producer half of `T54`, pinned where the defect entered.**
`test_the_closed_closeout_payload_declares_its_own_address_in_the_envelope_spelling`
(`:323-355`) drives `_closed_result_payload` with a closed record and requires the emitted
`contractPath` to be the response's own address in the envelope's spelling — so the guard has
something to compare against, and a re-narrowing of the payload key fails here rather than
silently returning the hole.

### Conventions

Plain module-level pytest functions plus the small builders and stubs above them
(`_StubIndex` `:176-188`, `_Contract` `:303-322`); no `unittest`, no `pytest` marks, so the
module is in the default selection and its lane is **`unit-regression`**
(`mcp/tests/test-evidence-lanes.toml:112`). The constants `OWN` (`:51`), `OWN_ENCLOSURE`
(`:56`) and `OTHER` (`:57`) are the only literals the cases share.

### Invariants And Boundaries

- **The fixture uses the shape the product emits, not a convenient one.** Both spellings are the
  contract FILE, measured on a real `worktree_status` response and on all four producers
  (`worktrees/modules/guidance.py:171-176` and `:443-444`, `application/lifecycle/start_result.py:121`,
  `application/lifecycle/reopen.py:104`). An earlier form of this fixture used a directory, a
  shape no producer emits — that is `L6`'s `F3`, corrected before the leaf froze.
- **The directory tolerance in the guard is exactly the immediate container.** `_names_the_same_place`
  (`mcp/src/agents_remember/application/tool_response.py:31-57`) accepts the contract file or
  `dirname(file)`, and an earlier, wider form that accepted any ancestor was narrowed in the same
  leaf; no case here asserts the wider rule, so re-widening it would be visible.
- **`ok` here means "did the call do what it set out to do".** These cases assert the decision, not
  the write: nothing in this module mutates a real tree, and `_migration_payload` runs the real
  payload builder over a stubbed index.

## Evidence

### Docs References

No external Domain Documentation source is configured in this memory root. These are
repository-owned response-contract facts; no external library behaviour is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The anchors below identify current behaviour of this module; they are not execution evidence and
they make no acceptance claim.

- The guidance shape the worktree state machine emits, both spellings set to the contract file. [1]
- A real closeout response model, so the guard is driven by the envelope it will meet. [2]
- The recorded `T54` shape: a response that declares no address cannot vouch for guidance. [3]
- The positive control: the guard is not a blanket refusal of guidance. [4]
- One disagreeing spelling is enough to withhold the hint, in both directions. [5]
- Guidance that names no artifact is kept; `None` stays `None`. [6]
- `T71`: every counted refresh entry is named by its source path or its own document path. [7]
- The migration payload builder and a declined item, driven through the real producer. [8]
- `T64`: a preview reports its outcome instead of a bare not-ok, and must not read `remaining`. [9]
- The producer half of `T54`: the closed payload declares its own address in the envelope spelling. [10]
- The guard these cases pin, and the two rules it applies. [11]
- The place comparison: the same file, or the directory that immediately contains it. [12]
- The entry namer `T71` repaired: source path, or the document's own path. [13]
- The bounded count that refuses to count a blank. [14]
- `T64`'s decision: `ok` answers whether the call did what it set out to do, with `state` and `outcome` declared separately. [15]
- The lane row that keeps this module in the default selection. [16]
- The refusal axes this module reuses rather than re-deriving, so a refusal is judged once. [17]

### Cross-Repo References

No cross-repository implementation evidence is required for these local response-contract claims.
The cases build no repository and touch no real coordination root.

No repository or external-system boundary is proved by this module.
