# dashboard/src/panels/detail-panel/worktreeSpine.test.tsx

## Current operative account — MIK-R199

- The module renders `WorktreeSpine` directly with a fixture enclosure, and renders `DetailPanel` for the whole-view
  case. Fixtures come from `./test-utils` (`enclosure`, `seedTaskEntries`, `taskEntry`, `taskSummary`); rendering comes
  from `@testing-library/react`, assertions from `vitest`.
- The fixture enclosure carries the fields the spine reads: `worktreeGroup`, `cleanup`, `codeWorktreeExists` and
  `memoryWorktreeExists`, plus `repoName` and `taskName`. The cases vary those fields and nothing else about the
  enclosure, so the spine's input surface is the enclosure's own facts.
- Module-level word lists hold the assertion vocabulary. `RETIRED_LANE_WORDS` names the engine lane labels that must not
  reach the surface again. `UNSUPPORTED_HISTORY_WORDS` names creation-history phrasing the projection cannot support:
  absence is a present-tense fact, and a checkout that was cleaned up answers the existence boolean the same
  way as one that was never made. Both lists are asserted with `not.toContain` against rendered text.
- Lane text is read through test ids: the spine root is `worktree-spine`, a lane is `spine-lane-code` or
  `spine-lane-memory`, and the `cleanupMeta(view, kind)` helper returns a lane's `textContent` (empty string when
  absent).
- The mixed case (code checkout present, memory checkout absent, cleanup pending) asserts the spine header reads
  `worktree · <worktreeGroup>`; the code lane prints `code checkout`, the enclosure's repo name, and
  `worktree present · pending cleanup`; the memory lane prints `memory checkout`, `ar-agents-remember`, and
  `worktree absent · pending cleanup`; and no retired lane word appears anywhere in the spine's text.
- The parameterised case covers both histories of an absent checkout — absent before anything was created (cleanup
  pending) and absent after a completed cleanup. For each, both lanes must read `worktree absent · <cleanup> cleanup`,
  must not read `worktree present`, must carry no unsupported-history word, and must still print its label and repo name
  while the spine header keeps the group path. The case comment states the reason: `EnclosureNode` has no
  creation/cleanup-history field to distinguish the two, so the label may only report current absence.
- The both-present case (completed cleanup) asserts the code and memory lanes read
  `worktree present · complete cleanup`, keep their repo names, and that no unsupported-history word appears in the
  spine.
- The whole-view case seeds a task entry and renders `DetailPanel` for `taskdoc:<key>`. It asserts the spine carries the
  enclosure's worktree group and repo name, the panel's text carries the task title, and no retired lane word appears
  anywhere in the rendered container.
- The assertions are text containment over rendered `textContent`. There is no snapshot file, and nothing in the module
  reads a provider map or an engine lane from the store.

### Source and authority bounds

- Source comparison: `dashboard/src/panels/detail-panel/worktreeSpine.test.tsx:1-137`, read in full.
- Source comparison: `dashboard/src/panels/detail-panel/worktreeSpine.test.tsx:16-35` (fixtures, word lists, lane
  helper).
- This card records what each case body asserts. No test run, runner invocation or coverage result is claimed here, and
  the card makes no claim about `worktreeSpine.tsx`'s implementation beyond the test ids and labels this module
  asserts.

## Evidence

- Lane text is reached by test id, and the two lanes are named `code checkout` and `memory checkout` beside their presence and cleanup facts. [1]
- Absence is asserted as current absence under both cleanup histories, with history phrasing refused on each lane. [2]
- A present checkout keeps the present/cleanup label and its repo name on both lanes. [3]
- The Tasks view keeps the enclosure and task facts and drops every retired lane word from the whole panel. [4]
- The retired engine vocabulary is a named list asserted against rendered text. [5]
