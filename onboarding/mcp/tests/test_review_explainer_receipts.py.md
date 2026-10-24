# mcp/tests/test_review_explainer_receipts.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The leaf's packet receipts: every requirement file the document names is receipted by its bytes, another leaf's document admits nothing, and a missing source is an unavailable receipt rather than a refusal.

## Code Commentary

- Every packet, document and reference file is receipted by its bytes, and a missing one is `unavailable` rather than a refusal.
- The leaf's own document is admitted by exact names and never by the task root, so another leaf's document admits no document files.
- An agreed revision's manifest joins the packet, and the receipts stay bounded.
- An own-document reread keeps an unchanged digest, returns a changed successor, and returns unavailable with no digest after loss or foreign-document replacement; explicit foreign-source admission remains refused.

## Evidence

- The case `test_every_packet_document_and_reference_file_is_receipted` protects every named source being receipted by its bytes. [1]
- The case `test_a_missing_packet_file_is_an_unavailable_receipt` protects a missing packet file being an unavailable receipt, not a refusal. [2]
- The case `test_a_document_that_is_not_this_leafs_admits_no_document_files` protects a foreign task document admitting no document files. [3]
- The case `test_an_agreed_revision_adds_its_manifest` protects an agreed revision's manifest joining the packet. [4]
- The case `test_an_own_task_document_receipt_rereads_through_the_admission` protects a re-read own-document receipt distinguishing unchanged, successor, loss and foreign. [5]
