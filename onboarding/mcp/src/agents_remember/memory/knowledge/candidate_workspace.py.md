# mcp/src/agents_remember/memory/knowledge/candidate_workspace.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/candidate_workspace.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T14:20+02:00 |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l43-ar`, uncommitted; base `fb719f8936d337c4685f2758d4ba3731cd8b7fc5` |
| lastVerifiedCommitHash | `4ef4dddc9194930611db2b1dfbb6e02113f2226a`|
| lastVerifiedCommitDate | 2026-09-20T15:00:59+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

One candidate's local working state: **creation, resumption, cloning and disposal authority**.

A candidate is a *directory* holding one writable SQLite database, the immutable receipt that binds it to its
admission, and the database's own resource lock. An operation that owns the candidate may add its own local
record beside those two — the curator ingest writes the identities it has allocated into
`curator-allocation-journal.json` there — because that is the same kind of fact the receipt is: a local,
operation-scoped record of what this candidate is, never knowledge the repository holds. The layout is fixed,
not the file count: what `models/knowledge/snapshot.py` pins is which file is the working database, and a
sibling record an owner writes does not move that answer. That layout is fixed by `models/knowledge/snapshot.py` so the
admission that opens the candidate for writes and the publication that reads it cannot disagree about which file
is the working database — and so no absolute path is ever stored as knowledge.

Four properties are load-bearing:

1. **Two-phase creation.** The database and the receipt are built in a private staging directory and verified
   there; only then is the complete directory exposed at the admitted destination. A half-created candidate
   therefore never appears at the path a later lease would open.
2. **An existing destination is a resume attempt.** Creation refuses an occupied destination; the resume path
   reopens the same database, retains its journal/WAL state and verifies the receipt against the admission instead
   of overwriting the unpublished work it holds.
3. **A clone comes from a closed snapshot.** Cloning copies a *closed* representation produced by the same freeze
   procedure publication uses, so a clone can never inherit a WAL-dependent main file from the database it started
   from.
4. **Disposal is a verdict, not a deletion.** This module decides whether the authored work is provably retained
   or explicitly discarded; removing the directory belongs to the enclosure owner that already owns cleanup.

## Code Commentary

### Logic

**The two-phase creation path** (`_two_phase_create`, used by both `create_candidate` and `clone_candidate`).
An occupied destination is refused first (`_occupied_refusal` → `destination_occupied`, worded as "a resume
attempt rather than a creation target"). A private sibling directory is created (`_stage_directory`, named with
the pid and a uuid so two creators cannot collide), the builder produces the candidate inside it, then
`_expose_candidate` verifies the staged database, seals the receipt and installs the complete directory. A builder
that returns a refusal aborts before anything is exposed, and the `finally` removes the private directory unless
the expose succeeded. `created` is only ever reported after a **readback** through the ordinary resume path
(`_read_candidate`), so the reported identity and receipt are the ones a later open would see.

- `_build_empty_candidate` creates the declared schema and the repository row in the stage.
- `_build_cloned_candidate` opens the selected baseline, requires it to carry a repository row, and calls
  `freeze_closed_snapshot` into the stage's candidate database. The admission's namespace is enforced where the
  receipt is sealed, so a baseline bound elsewhere is refused with `candidate_binding_changed` rather than copied
  and relabelled. **No filesystem lock is taken on the baseline**: SQLite's own read transaction is what makes the
  copy consistent, a baseline that moved while it was frozen is caught by the identity comparison rather than
  serialized against, and a lock file beside a published snapshot would land inside a directory whose contents are
  captured as memory.
- `_expose_candidate` is the ordering that makes "created" honest: it reads the staged database
  (`_read_staged_candidate`: schema, namespace and identity from the database itself), builds the receipt from
  **those observed facts**, writes and reads it back, flushes the database with `fsync_file`, and only then
  `atomic_replace`s the stage onto the destination. A failure in the receipt/flush group returns
  `snapshot_incomplete` with nothing exposed — a candidate whose durability step failed can never be read back as
  created — while the expose itself reports `destination_occupied` (something appeared there after all) or
  `publication_failed`.

**The read and disposal paths.**

- `_read_candidate(operation, destination)` is the shared verification: both candidate inputs must be present
  (`_candidate_inputs` → `selected_input_unavailable` naming the exact missing file), the database opens
  (`_open_for_verification` maps `candidate_busy`, `unsupported_schema` and an unreadable file onto typed
  refusals), the receipt is compared with the admission (`_receipt_denial` → `receipt_binding_refusal`), and the
  identity is read from the live database. `open_candidate` is this path — the restart and branch-switch entry
  point — and it repairs and deletes nothing: the last committed batch is read straight out of the database
  through whatever journal or WAL state SQLite needs to recover.
- `authorize_candidate_disposal` is deliberately narrow. A `discard` disposition must name the identity the
  candidate holds **now**, so an authorization written for an earlier state cannot be replayed against newer
  unpublished work (`_disposal_identity_refusal` → `stale_precondition`). A `published` disposition must point at
  a database that reopens to that same logical identity (`_published_identity_refusal`), verified through a
  read-only connection — a stale published snapshot, a loose object or a successful read does not establish that
  no unique authored data remains. The result is a verdict (`disposable` with the identity it verified), not an
  action.

`_close_without_discarding_peers` closes the connection and leaves SQLite's own recovery files exactly where they
are. It is the same thing `OpenedKnowledgeStore.close` does today (that method no longer unlinks WAL/SHM peers),
and the helper exists so a later change to that method cannot quietly reintroduce an unlink underneath the
lifecycle without a test noticing.

### Conventions

- Every failure that a caller can act on is a **typed refusal returned inside the result**; `_refused` refuses a
  missing refusal value as a defect, so "refused with no reason" is not representable.
- `KnowledgeRefused` is raised internally where a helper deeper in the stack (the freeze procedure) needs to
  unwind, and is caught at the boundary and turned into the same typed result shape.
- Stage directories are this operation's own temporary output; `_discard_private_directory` removes only the
  directory this call created, with `ignore_errors=True` so cleanup cannot replace the caller's refusal.

### Invariants And Boundaries

- **A candidate is published only through its own directory.** Both write and publication derive their paths from
  the admitted candidate, so no caller can write into one database and publish another.
- **Creation never touches an occupied destination.** Refusing is the whole mechanism that keeps unpublished
  authored work from being overwritten by a routine re-run.
- **The receipt is derived from the database that exists**, never from the admission alone.
- **Nothing here deletes a journal or WAL peer of a real database.** Disposal is a verdict; the only files removed
  are a private stage this operation created and the stage's own peers (in the freeze procedure).
- **The layout is fixed elsewhere.** Both file names come from `models/knowledge/snapshot.py`; this module derives
  paths and never spells one out.
- **Boundary.** This module owns the candidate's local lifecycle. It does not publish a snapshot, take a
  destination lock, decide authority, or remove a candidate directory.

### Todos

None recorded for this slice. The disposal verdict names the enclosure owner as the remover by design; a leaf that
wants automatic reclamation should add it there rather than here.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The four public operations this module owns. | `create_candidate`; `clone_candidate`; `open_candidate`; `authorize_candidate_disposal` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:85-98; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:100-126; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:129-138; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:141-173 |
| The two-phase creation and the ordering that makes `created` honest. | `_two_phase_create` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:179-221 |
| The empty-schema builder and the baseline clone that reuses the publication freeze. | `_build_empty_candidate`; `_build_cloned_candidate` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:224-243; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:246-291 |
| The expose step: verify staged database, seal and read back the receipt, flush, then install. | `_expose_candidate`; `_read_staged_candidate` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:306-357; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:360-392 |
| The shared verification path a resume and a disposal both take. | `_read_candidate`; `_candidate_inputs`; `_receipt_denial`; `_open_for_verification` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:398-427; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:430-454; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:457-474; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:477-502 |
| The two narrow disposal grounds, each naming the identity it was measured against. | `_disposal_identity_refusal`; `_published_identity_refusal` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:505-521; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:524-575 |
| The occupied-destination refusal and the private stage directory. | `_occupied_refusal`; `_stage_directory` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:581-597; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:600-613 |
| The close that deliberately leaves SQLite's own recovery files in place. | `_close_without_discarding_peers` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:622-632 |
| The receipt write/read/binding comparison this lifecycle depends on. | `build_receipt_for_candidate`; `read_candidate_receipt`; `receipt_binding_refusal` | mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:89-99; mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:61-86; mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:102-160 |
| The freeze procedure a clone reuses, and its closed-file guarantee. | `freeze_closed_snapshot` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:66-109 |
| The result vocabulary these operations return. | `CandidateResult`; `CandidateDisposalResult`; `CandidateDisposition` | mcp/src/agents_remember/models/knowledge/snapshot.py:188-221; mcp/src/agents_remember/models/knowledge/snapshot.py:357-375; mcp/src/agents_remember/models/knowledge/snapshot.py:351-354 |
| The new refusal codes the lifecycle introduced, including the honest durability code. | `selected_input_unavailable_refusal`; `snapshot_incomplete_refusal`; `publication_durability_unconfirmed_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:882-902; mcp/src/agents_remember/memory/knowledge/refusals.py:951-974; mcp/src/agents_remember/memory/knowledge/refusals.py:1020-1039 |
| The nodes that protect the lifecycle's load-bearing behaviours. | "test_a_live_reader_does_not_let_the_write_boundarys_close_lose_the_commit"; "test_a_crash_restart_keeps_the_committed_batch_and_drops_the_abandoned_one"; "test_a_failed_candidate_flush_is_refused_before_the_directory_is_exposed" | mcp/tests/test_knowledge_candidate_workspace.py:206-246; mcp/tests/test_knowledge_candidate_workspace.py:286-316; mcp/tests/test_knowledge_candidate_workspace.py:403-425 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator (uncommitted change set on `ar/260915-ks-l43-ar`, code base `fb719f89`): **the module's docstring now records that an owning operation may keep its own local record in the candidate directory, and this card carries the same fact.** The change is documentation-only in this file — `application/knowledge_curator_ingest.py` is what writes `curator-allocation-journal.json` beside `candidate-receipt.json` — but it is a fact about *this* module's contract, because this module is where the candidate's layout is defined, and a reader who took "the layout is fixed" to mean "these are the only files" would be wrong. The body paragraph now says which part is fixed (which file is the working database, so the admission that opens the candidate for writes and the publication that reads it cannot disagree) and which part is not (a sibling local record an owning operation writes, of the same kind as the receipt). No claim was weakened, no range moved, and the verification pair is retained exactly as recorded. No commit was made.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): clamped mcp/src/agents_remember/memory/knowledge/refusals.py:1020-1040 to mcp/src/agents_remember/memory/knowledge/refusals.py:1020-1039, the range the cited construct now occupies
- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): created this one-to-one card for the new candidate lifecycle. It records the four load-bearing properties (two-phase creation that never exposes a half-built candidate, occupied-destination-as-resume, clone-from-a-closed-snapshot, and disposal as a verdict rather than a deletion), the expose ordering that makes `created` honest (verify → seal → read back → flush → install → read back through the ordinary resume path), why a baseline clone deliberately takes no filesystem lock, and the two narrow disposal grounds. It also records that `_close_without_discarding_peers` exists so a later change to `OpenedKnowledgeStore.close` cannot quietly reintroduce a peer unlink underneath the lifecycle. Verification metadata remains empty until closeout stamps the code commit.
