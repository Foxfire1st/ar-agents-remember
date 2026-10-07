# mcp/src/agents_remember/tasks/leaf_decisions.py

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

The strict lookup of a leaf's task document, and the answer whether a decision entry of that document
resolves. `strict_leaf_doc` fails closed on identity doubt: it never treats a document it cannot read as
"no document". It also decides which of the files it opened count as read for a caller that keeps a
result.

## Code Commentary

### The lookup

`strict_leaf_doc(task_root, leaf_id)` returns the leaf's one `(path, TaskDocument)`, `None` when the leaf
has no document, or raises `LeafDocumentUnresolved` (a `ValueError`).

- It asks `resolve_terminal_leaf_doc` first. Two documents that claim the leaf, and an unreadable document
  whose file stem is the leaf's, raise `TerminalLeafResolutionError`, which is raised again as
  `LeafDocumentUnresolved`.
- `_unreadable_claims` then reads every `*.json` directly in the task folder with `read_task_doc`. A file
  that fails to read while its raw JSON still names the leaf (`_names_leaf`: its `id`, or the `leafId` of
  an entry in `enclosures`; a document of kind `master` never counts) is the leaf's document in a broken
  state, and the lookup raises naming each such file with the first line of its error.
- A file that is not JSON, or that names no leaf, is ignored.

Every caller gets this behaviour: the worklist's maintenance scope and declared effects
(`application/knowledge_worklist/leaf.py`), the gate memo's key (`application/knowledge_gate/memo.py`), the
direct-landing gate (`application/knowledge_gate/direct.py`), the knowledge writer's open questions
(`application/knowledge_writer/open_questions.py`) and `leaf_decision_refusal`.

### What counts as read

The lookup opens every JSON file of the folder to rule out other claimants. It runs inside its own nested
recording block, and afterwards replays into the caller's recording only part of what it recorded:

- when the document is established: the rows of the leaf's own document, and every row whose identity is
  not a plain `sha256:` value, that is, a file that was absent, unreadable or read at two identities. A
  sibling that was read in full and ruled out leaves no row;
- when the leaf has no claimant: every row it opened — each sibling read in full and the exact direct
  JSON listing. The terminal task-root resolution is one of the admitted unrecorded B5 selectors, so no
  resolution row exists. A performed lookup that finds no claimant is evidence of absence: those
  files are inputs of the result, and a write to another leaf's document or a new sibling moves them;
- when the lookup raises: every row it recorded.

A caller that keeps a result with its recorded rows therefore depends on the leaf's own document. When the
lookup established a claimant it depends on no sibling it merely ruled out; when the lookup found no
claimant, every opened document and the exact listing are inputs. A sibling that starts to claim the leaf
changes the answer of the next lookup, which a keyed caller makes again before it uses what it kept.
Outside any recording block the lookup records nothing and its answers are the same. A caller that only
rechecks recorded rows — the moved-input check of the leaf-wide computation — performs no lookup and
records no such rows.

### Decisions

`leaf_decision_refusal(task_root, leaf_id, at)` returns `None` when the leaf's document holds exactly one
decision entry whose `at` equals the citation. Otherwise it returns the reason: the lookup's own doubt, no
task document, no entry at `at`, or several entries at `at`.

## Evidence

- The module docstring: the strict lookup and what it records as read. [9]
- The lookup inside a nested recording, and the rows it replays to the caller. [10]
- Every JSON file of the folder is read; a broken file that names the leaf is collected. [11]
- A raw document names the leaf by its id or an enclosure's leafId; a master never does. [12]
- Exactly one decision entry at the cited time resolves. [13]
- The recorded reads hold the leaf's document and not the master's; sibling writes leave a kept view in place. [14]
- A second claimant makes the next lookup ambiguous. [15]
- A sibling file that is read at two identities during the lookup stays recorded as a conflict, and the view is refused. [16]
