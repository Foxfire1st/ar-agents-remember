# mcp/tests/test_explainer_retirement_hooks.py

## Governing Overview

[Route overview](overview.md)

## Purpose

What AR's retirement does to a leaf's explainer: a preview retires nothing, master retirement and sprint archive retire and then reclaim, a failed retire keeps its pieces for the retry, and a leaf finalize leaves the environment alone.

## Code Commentary

- A dry run lists every environment and retires none; master retirement retires and reclaims the folder, counter, grades and receipts.
- A failed retire keeps the folder, counter, receipt and grades for the retry, and a pending receipt is finished by the next archive.
- An interrupted external deletion is attributed `alreadyAbsent` on the retry from the exact confined targets, and never for a path outside them.
- A symlink is held rather than followed, leaf finalize and the cleanup port do not retire, and the warmup never resumes an explainer seat.

## Evidence

- The case `test_a_dry_run_lists_every_environment_and_retires_nothing` protects a retirement preview listing without retiring. [1]
- The case `test_master_retirement_retires_and_reclaims_every_environment` protects master retirement reclaiming every environment. [2]
- The case `test_a_failed_retire_keeps_the_folder_counter_receipt_and_grades` protects a failed retire keeping what the retry needs. 
- The case `test_an_interrupted_external_deletion_is_attributed_already_absent_from_exact_targets` protects an externally deleted target being attributed already absent from the exact confined path only. [4]
- The case `test_the_warmup_never_resumes_an_explainer_seat` protects the warmup leaving an explainer seat alone. [5]

- Retired at the fifth freeze d59c3493: mcp/tests/test_explainer_retirement_hooks.py::test_a_failed_retire_keeps_the_folder_counter_receipt_and_grades - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.
