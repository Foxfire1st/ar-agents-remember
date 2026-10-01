# mcp/src/agents_remember/application/knowledge_gate/landing.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The gate at the landing routes (MIK-R09 rules 3 and 4).** `landing_refusal(LandingGateRequest)` is the port's
landing answer: for a leaf's recorded landing, the leaf's history file must be `closed` in the landed memory commit
(rule 3); for a master or checkpoint landing, every entry of the master's memory tree at a path the master's **net**
code diff changed must be `current` at the master's code commit (rule 4). The validator half of each landing runs in
the worktree layer through `memory_commit_refusal`, the one route entry point every memory commit route uses
(MIK-R22 rule 8); this module adds only what the validator does not check.

## Code Commentary

### Logic

- **`landing_refusal`** collects `_findings` and joins them under "the mandatory invariant gate (MIK-R09) refuses
  this landing of memory commit …"; a `SubprocessError` anywhere is one `knowledge-worklist-incomplete [git]` finding
  ("the landing is blocked until the trees can be read"). When a stale or unverifiable entry is among them, it names
  the remedy: a knowledge-maintenance leaf within this master (`knowledgeMaintenanceScope: true`) whose rows and
  re-anchors make them current.
- **`_history_closed`** (a request with `leaf_owner`): reads `knowledge/history/<leaf>.json` at the landed commit. A
  listed blob that cannot be read is an unreadable input, never "absent"; an absent or open file is
  `knowledge-history-not-closed` ("this commit is not a closed-out leaf's").
- **`net_stale_entries`** (a request with `code_base`): `_net_diff` lists the paths changed from the merge base of the
  parent line's code tip and the master's commit to that commit (`--no-renames`, `-z`), and the commit's tree; K_C is
  read from the landed memory commit and C opened once; each entry at a changed path is observed through
  `GateContext.entry_state`. Anything not `current` refuses (review R1 F4): `stale` → `knowledge-stale-at-landing`;
  `unverifiable` for a locator reason or a persistently unavailable object → `knowledge-unverifiable-at-landing`, naming
  why; a Git read that failed (`GitReadFailed`) → `knowledge-worklist-incomplete [git]`. An unreadable K_C, C or net
  diff blocks as an unreadable input.
- **Record landing checks the leaf's latest history file (L37 reopen ruling, review R1 F5).** `_history_closed`
  asks `_latest_history_path(request)`, which lists `knowledge/history/` in the landed memory commit (`ls-tree
  --name-only`) and takes the owner's highest attempt (`owner_history_attempt`), or the plain file when it has no
  attempt file. A listing Git cannot give is an `_unreadable` finding (`run-incomplete`: "the landed memory
  commit's history files cannot be listed"); it never falls back to the plain first file, which for a reopened
  leaf is the closed attempt 1 and would pass while attempt 2 is still open.

### Conventions

- A master's record landing gets the validator only: the staleness check needs the parent line's code tip from before
  the landing, which the after-the-fact route cannot know (accepted smaller choice, ruling 14:38:47).
- The request type, `LandingGateRequest`, lives in `worktrees/services.py`; the unconverted exemption is decided by the
  worktree layer's marker probe before it asks.

### Invariants And Boundaries

- **A master or checkpoint landing waits until no entry at a changed path is stale or unverifiable.** Realized by
  `net_stale_entries`; proved by `test_a_master_or_checkpoint_landing_waits_until_no_entry_at_a_changed_path_is_stale`
  (stale `RLZ-A00001` refuses; an unchanged `keep` is not stale; the re-anchor passes),
  `test_a_timed_out_blob_read_or_an_unverifiable_entry_refuses_a_master_landing`, and on real data by `closeout.txt`
  step 4 (the unmaintained master refuses `knowledge-stale-at-landing RLZ-CXH58B4W`; `integrate`'s dry run returns
  `(2, knowledge-gate-refused)`).
- **A leaf's record landing requires its closed history file.** Proved by
  `test_record_landing_checks_the_landed_memory_commit_is_closed_and_valid` and `closeout.txt` step 3.

### Todos

- None.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R09@v2` and `09_mandatory-invariant-closeout-gate.json`,
outside the repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: master routes and record landing. [1]
- The finding codes. [2]
- The refusal and the named remedy. [3]
- The closed history file in the landed commit. [4]
- The master's net staleness, refusing anything not current. [5]
- The master route test. [6]

- The leaf's latest history file in the landed commit; an unlistable directory is an unreadable input. [7]
- Record landing refuses when the landed history cannot be listed. [8]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary is crossed by this file.
