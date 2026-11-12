# mcp/tests/test_request_logical_digests.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Refutations of request-local identity reuse on real SQLite inputs: equal endpoints share two scans
and never cross a request boundary, a WAL commit changes the visible inputs even when the main file
does not, identical endpoint bytes still do not share a scan, and a change-and-restore during the
scan never stores a result for the old inputs.

## Code Commentary

- `test_equal_endpoint_groups_share_two_scans_and_never_cross_request` shows seven reads of one
  endpoint and ten of another each run `logical_body` once, that a copied context retains no
  completed answer, and that a new request re-scans.
- `test_wal_commit_changes_visible_inputs_even_when_main_file_does_not` shows the digest moves with
  the connection-visible WAL image while the main file bytes stay equal, and then reuses the new
  answer.
- `test_identical_endpoint_bytes_still_do_not_share_a_scan` copies one endpoint image to a second
  origin: identical bytes do not share an answer, and each origin is scanned once.
- `test_change_and_restore_during_scan_never_stores_result_for_old_inputs` moves the endpoint during
  the scan; the result is not stored for the old inputs.

## Evidence

- Equal endpoints share two scans and never cross a request boundary. [1]
- A WAL commit changes the visible inputs even when the main file does not. [2]
- Identical endpoint bytes still do not share a scan. [3]
- A change-and-restore during the scan never stores the old inputs' result. [4]
