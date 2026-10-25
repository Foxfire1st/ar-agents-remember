# mcp/tests/test_task_document_copies.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the copies a task document carries: each leaf role publishes a real leaf before the handover is
compiled, a public write refreshes only its own leaf in every existing enclosure, a failed publication restores
every copy and the canonical source, and cleanup removes the copies it made. Scope is bounded (MIK-R134): a
foreign contract is skipped and named, never loaded.

## Code Commentary

### Logic

`TaskDocumentCopyTests.selection()` and `.snapshot()` build the leaves and the snapshot a write reaches, and
`_write_requirement_fixture()` writes requirement files beside a leaf.

- **Publication.** `test_each_leaf_role_publishes_real_leaf_before_handover_compilation`,
  `test_public_writes_refresh_only_own_leaf_in_every_existing_enclosure` and
  `test_leaf_title_updates_canonical_master_but_copies_only_the_leaf` keep the canonical write and the copies
  distinct.
- **Rollback.** `test_failed_copy_publication_restores_every_copy_and_canonical_source` restores every copy and
  the canonical source after a failure.
- **Read-back.** `test_edits_to_copy_are_not_read_back_and_next_leaf_write_replaces_them` keeps an edit of a copy
  from being read back, and `test_cleanup_removes_copies_and_external_links_are_refused` cleans up while refusing
  an external link.
- **Requirements.** `test_requirement_files_are_copied_beside_the_leaf_and_nothing_else`,
  `test_missing_requirement_is_named_in_handover_lists_and_receipt_warning`,
  `test_write_adding_a_requirement_adds_its_copy`, `test_changed_source_is_named_and_next_write_refreshes` and
  `test_cleanup_removes_requirement_copies` cover a requirement's copy, its absence, its drift and its cleanup.
- **Scope.** `TaskDocumentCopyScopeTests` proves a foreign contract below a master's notes stops no write, that
  one in the changed task's enclosures is skipped and named, that a refresh loads only the changed task's
  contracts, and that the walk yields task enclosures and none below `notes`.
- **Membership.** `TaskDocumentCopyMembershipTests` keeps a sibling leaf's contract from being loaded while a
  broken sibling does not stop a real write, fails a destroyed own contract and restores the sources, succeeds a
  master write with enclosures present, treats a `..` alias escaping the repo's tasks as foreign, names the
  group in refresh and in heal, and — per the Architect ruling — names an unreadable file beside a refreshed own
  copy while failing closed when only the unreadable enclosure is own.

### Conventions

A case writes through the public task-document surface and reads the copies from disk, so what a seat receives
is what is asserted.

### Invariants And Boundaries

- A write refreshes exactly the copies of the document written; a foreign contract is skipped and named.
- A failed publication leaves the canonical source and every copy as they were.

## Evidence


- The module keeps preparation, publication and cleanup cases and adds scoped enumeration, physical membership and conditional unreadable-file controls. [1]


- Own-leaf copy controls include real non-symlink requirement bytes and digest rows, missing rows with a handover warning, exclusion of reference, master and sprint baggage, publication adding a requirement, source drift then refresh, and requirement-copy cleanup. [2]
