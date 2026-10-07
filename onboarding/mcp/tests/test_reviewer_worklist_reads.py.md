# mcp/tests/test_reviewer_worklist_reads.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Tests of what the reviewer's leaf-wide view and the invariant gate record as read, and of how a kept
result follows those reads. Real child processes read task documents, settings, contracts, requirement
packets, root directories and a ledger while the test changes them, and the tests check the rows that
reach the parent, the answer the reader gets, and that nothing wrong is kept. The module is in the
`integration` lane.

## Code Commentary

### Helpers

- `_fresh_memo` (applied to every test) clears the leaf-view memo before and after each test.
- `_child_script(script)` replaces only the launch of the child module with `python -P -c <script>`.
  `_observations()` wraps the parent's `_reply` and collects every validated reply of a child.
- `_task_document`, `_settings`, `_retarget`, `_subjects` and `_packet_inputs` build task documents,
  settings files, symbolic links, item-subject lists and a decision with a `reconsider_on` link to a
  requirement packet.

### One long case over real reads

`test_child_consumed_task_bytes_survive_aba_conflict_absence_and_read_errors` runs these parts in order.

- **The leaf's task document.** In the child the document is changed and restored (the row holds the
  changed bytes), read at two identities (`conflicting reads`), changed and then removed (the row holds
  the changed bytes), or unreadable (`unreadable (PermissionError)`). Each read is refused naming the
  document, the row reaches the parent's `moved_inputs`, and nothing is kept. A stable document then
  answers and is kept.
- `_settings_reads`: for the Markdown and the JSON settings of the memory worktree, a same-size change
  that is restored during the read is recorded with the changed bytes and refused; a read that fails is
  recorded as unreadable and refused. `_settings_selection` checks the rows of the settings selection
  directly: an absent higher-priority file, an absent JSON sibling and the consumed file; a file that
  appears is a change; an invalid JSON file is still recorded with its bytes.
- `_fallback_reads`: a contract that is changed and restored while the fallback context loads it is
  recorded with the bytes parsed and refused; a sibling task file read at two identities is recorded as a
  conflict.
- `_packet_reads`: a packet changed and restored during its read, and a packet link retargeted during the
  read, are recorded under the link's path with the bytes read; a manifest read that fails is recorded as
  unreadable.
- `selection_reads` then runs five parts, each in a fresh world:
  - `_packet_confinement`: a packet link is retargeted outside the task, to the packet, and outside again,
    with identical bytes. Each state is computed once and then served from the memo; the reconsideration
    item appears only while the link points at the packet; the gate passes, refuses and passes; the reply
    holds the `resolve:` row of the link; outside the task no packet byte is read or recorded.
  - `_contract_alias`: a contract link retargeted during the read is recorded as a conflict on its
    `resolve:` row and refused; the next read is fresh and kept.
  - `_root_selections`: the absent external memory root is recorded; retargeting the root link between
    settings directories recomputes each time, also to a directory with identical settings bytes; a
    repository-sidecar root that exists is refused by name with its path, and its presence, absence and
    retargeting are recorded. `_root_errors`: a root probe that raises is recorded as unreadable, refused,
    and nothing is kept.
  - `_external_ledger`: with a cross-repository allowance that includes memory, the other repository's
    ledger is recorded with its raw bytes; a change recomputes with an identical body; a change restored
    during the read is refused; an absent ledger is recorded as absent; a failed read is refused.
  - `_gate_failed_selector`: when the contract read behind the gate's settings resolution fails, the gate
    returns the same verdict as before, the row is `unreadable (PermissionError)`, and two evaluations keep
    nothing in the gate memo.
- At the end, a task document that the owner refuses gives an `incomplete` worklist naming
  `leaf task document`, served as `trees` and not kept.

### The view depends only on what it read

- `test_a_kept_view_ignores_every_task_document_it_did_not_read`: the child's reads hold the leaf's
  document and not the master's `task.json`. Another leaf's document that appears, is edited and is
  removed, and a newline added to `task.json`, each leave the body and the child count unchanged. An edit
  of the leaf's own document computes again.
- `test_a_document_that_begins_to_claim_the_leaf_is_not_hidden_by_a_kept_view`: a second document with the
  leaf's ID makes the next read compute again and answer an `incomplete` worklist; the memo still holds
  only the first view.
- `test_a_task_document_changing_while_the_view_is_computed_is_computed_again`: a child that writes the
  document once before it computes leads to two computations and an answer that is kept; a child that
  writes new content every time leads to exactly two computations and the refusal `inputs_changing`
  naming the document, nothing kept, and a normal answer afterwards.
- `test_a_worklist_that_reads_no_task_document_is_not_refused_as_changed`: a child whose worklist does not
  apply answers the view with source `absent`.
- `test_moved_inputs_tells_not_read_from_changed_and_unidentified`: with a key that names one document,
  no read and a read with the same bytes report nothing; other bytes, a conflict, and a document the key
  does not name are each reported.
- `test_the_gates_warm_pass_becomes_the_refusal_when_a_packet_locator_is_retargeted`: the gate passes while
  a packet link points outside the task and the pass is kept; after the link is retargeted to the packet,
  which has the same bytes, the next evaluation refuses with `knowledge-item-open`.

## Evidence

- The long case: the leaf's document, then settings, contract, packet, root, ledger and gate parts. [1]
- The launch replacement for faulty children. [2]
- Settings changed, restored and unreadable during the child's read. [3]
- The rows of the settings selection. [4]
- The fallback contract read and a sibling read at two identities. [5]
- Packet bytes, a link retargeted during the read, and a failed manifest read. [6]
- The packet link outside, inside and outside again, for the view and the gate. [7]
- A contract link retargeted during the read. [8]
- Root absence, retargeting, the removed sidecar root, and probe errors. [9]
- The external ledger's bytes, change, absence and failure. [10]
- A failed contract read behind the gate keeps nothing. [11]
- Documents the view did not read do not invalidate it. [12]
- A second claimant is computed again. [13]
- One recomputation, then inputs_changing. [14]
- No task document read is not a change. [15]
- The judgments of moved_inputs. [16]
- The gate's warm pass becomes the refusal. [17]
