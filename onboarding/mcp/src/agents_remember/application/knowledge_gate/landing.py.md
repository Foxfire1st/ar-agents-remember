# mcp/src/agents_remember/application/knowledge_gate/landing.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The gate at the landing routes (MIK-R09 rules 3 and 4).** `landing_refusal(LandingGateRequest)` is the port's
landing answer: for a leaf's recorded landing, the leaf's history file must be `closed` in the landed memory commit
(rule 3); for a master or checkpoint landing, every entry of the master's memory tree at a path the master's **net**
code diff changed must be `current` at the master's code commit (rule 4). A landing that names a code base also
derives whether the documents its dependent records describe became stale; that count is part of the landing answer,
and only a master's end refuses for it (MIK-R124). The validator half of each landing runs in
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

- A master's recorded landing uses the recorded series code base for net staleness. All master landing routes also authenticate each newly closed history file against a landed leaf enclosure, recorded direct publication, or admitted crossing sync. The candidate file must be closed and byte-identical to that owner's publication; one failed file yields its named reason. A base-held closed file stays frozen, and no new history means no owner-contract/journal read. Unreadable enclosures, journals and Git inputs refuse. The earlier validator-only recorded-master limit is superseded.
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

## Dependent staleness at a landing (MIK-R124)

`document_staleness(request, *, full=False)` derives, at the landing, which documents its dependent records describe
are stale. It returns a `DocumentStaleness`: the documents this landing made stale, those already stale at its base,
the documents it examined, how many dependent record bodies it read, and any state it could not establish.

A document is stale when a link of its dependent record no longer holds the value the confirmation recorded: a file
or anchor link's recorded bytes differ from C, an anchor's locator no longer resolves, or a record link's revision
differs from the candidate's. Nothing about staleness is stored. The memory tree holds the links and the
confirmation they were taken at; the landing reads them against the code and derives the state each time.

Only the dependents a change can move are read: those with a link at a path the code range changed or at a record
whose file differs between the memory base and the tip. The changed paths are listed without rename detection, so a
rename names both the path that left and the path that arrived, and an anchor link counts at its file. The master's
end (`full`) reads every dependent of the tip instead, so debt a net-zero or intermediate change would hide is still
named. Git output is read as bytes and decoded with surrogate escapes, so a path whose bytes are not UTF-8 is
compared as the tree holds it.

The lookup is the layout marker's `dependent_links` index, which the writer builds. When that index does not name
exactly the dependent record files of the commit, the read is uncomputable rather than guessed, and a marker that
cannot be read or a record whose linked revision cannot be fetched is reported the same way.

The base is compared by the same rule. A document stale at the tip that was current at the base, or that had no
record there, is one this landing made stale; one already stale at the base is named separately and refuses nothing.

`DocumentStaleness.answer()` is the field the landing answer carries. It gives the count, the documents and the
`knowledge_read` view that returns them (`view=dependent`, `staleOnly=true`, memory root of the landing's tree), and
names any already-stale documents. An ordinary landing and a checkpoint leave the field out when the landing named no
document at all — neither one it made stale nor one already stale at its base. A master's end keeps the field while it
has inherited debt to name, answering `count: 0` beside `alreadyStale` rather than omitting it; with neither newly nor
inherited stale documents it omits the field as an ordinary landing does. A state that could not be established is
never answered as a current document: an uncomputable read returns its state and reason in place of the count, and an
unverifiable one returns its state, the reasons, the count and the documents — a failure answer therefore stands where
a zero count would otherwise be left out.

Only a master's end refuses. It adds `knowledge-dependents-stale-at-master-end` with the count, the documents, the
read and the remedy — a task of this master that changes the document or confirms it — or
`knowledge-worklist-incomplete` when the count cannot be computed, or `knowledge-unverifiable-at-landing` when a
document's state cannot be observed. A checkpoint and an ordinary landing disclose the same facts in their answer
and refuse nothing: the landing happens, and its answer says how many documents it made stale (rule 4; rule 8).

## Evidence


- Every newly closed master history file is authenticated against its owner publication. [9]



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
