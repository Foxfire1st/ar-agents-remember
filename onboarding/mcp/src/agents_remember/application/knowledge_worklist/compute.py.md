# mcp/src/agents_remember/application/knowledge_worklist/compute.py

## Governing Overview

[Nearest governing overview](../overview.md)

## Purpose

One worklist run. `compute_worklist(inputs)` takes the code trees B and C, the knowledge sides K_B and K_C,
the maintenance-scope flag, the declared effects, the route coverage and the coordination root, and returns
one `knowledge-worklist/v1` document. The run is a function of these inputs: equal inputs give equal items
and an equal digest. An input that cannot be read makes the document `incomplete`, naming the input, with
no items.

## Code Commentary

### The run (`_Run.document`)

1. **Changes.** `_changes` reads the changed paths from `tree_difference_observation` and the renames from
   `git_rename_inference`. An unavailable or partial inventory, or unavailable renames, raises
   `WorklistIncomplete` naming `B/C change inventory` or `B/C renames`.
2. **Read-ahead.** `inputs.code.warm(...)` reads the blobs of every changed text path on both sides in
   batches before any of them is asked for singly. It changes no answer and no failure: a blob it cannot
   read is read again, and fails, where it is used.
3. **Scope** (`_scope`). Every K_B entry at a changed path is classified, or every K_B entry when the
   leaf sets the maintenance scope. The knowledge-side changes between K_B and K_C are computed. Every K_B
   family that contains a touched invariant, or whose record changed, is reached, and every K_B entry of
   those families' members is classified once. What this last step finds raises items and reaches no
   further family.
4. **Items.** `touched_invariant` for every touched invariant, `stale_invariant` for every invariant with
   an entry that was stale at the base, `reached_family` for every reached family and for every family of
   a stale invariant, and the family route conditions.
5. **Planned effects.** `reconcile_planned_effects` marks invariant and family items `planned` or
   `unplanned` and raises `planned_untouched` for a declaration no row delivers.
6. **Linkage.** `_linkage` marks each hunk of each changed path `linked` or not. A hunk is linked when its
   changed lines on the B side hit a K_B entry's range there, or its changed lines on the C side hit a
   K_C entry's range there (`_linked`). A change without text hunks, and the mode fact of a mode change,
   are linked at file level, by an entry with a `file` locator at the path (`non_text_linked`).
7. **Unexplained changes and reconsideration.** `unexplained_items` raises an item for every unlinked hunk
   and non-text change; `reconsideration_candidates` raises one for each decision alternative whose linked
   target changed.

The document holds the pairing, the scope counts, the classified entries, the changes with their linkage,
the summaries of planned effects, unexplained changes and reconsideration, the items sorted by kind and
subject, the registered kinds and the digest.

### Failures

`compute_worklist` turns `WorklistIncomplete`, `CodeReadError` (named `C`) and any
`subprocess.SubprocessError` (named `git` by `git_failure`) into `incomplete_worklist(...)`: state
`incomplete`, one named input, no items, and a digest over that.

### Identity

`Item.id` is `item_id(kind, subject, identities)`; the identities of an item are the content facts that
make it a new item when they change. `worklist_digest` is the prefixed SHA-256 of the state, the items and
the incomplete entries.

## Evidence

- The module docstring: the eight steps and the incomplete rule. [33]
- What one run reads. [34]
- The one representation of unreadable input. [35]
- The entry point and the three failures it turns into an incomplete document. [36]
- The change inventory and the renames, each named when unavailable. [37]
- The run: changes, read-ahead, scope, items, planned effects, linkage, unexplained, reconsideration, document. [38]
- Classification, knowledge changes, reached families and their members, once. [39]
- A changed path's hunks with their linkage, or its file-level linkage. [40]
- A hunk is linked by changed lines on their own side only. [41]
- A non-text change is linked by a file-locator entry. [42]
- A failed or timed-out Git call is the input named git. [43]
- The read-ahead is one batch and never fails the run. [44]
