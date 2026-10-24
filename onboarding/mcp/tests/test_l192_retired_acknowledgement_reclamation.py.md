# mcp/tests/test_l192_retired_acknowledgement_reclamation.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin the physical reclamation of acknowledgement rows that name a retired provider kind, including
the file that holds nothing else.

## Code Commentary

`AttentionDismissalRecord` refuses the retired kinds on read and admission, but the tolerant read
drops those raw lines before `reconcile` compares records with kept, so a file holding only retired
rows folded to nothing, compared empty against empty, and never triggered the rewrite: the bytes
stayed on disk and were re-read on every tick with no external input. The repair counts the raw
rows the fold did not read and forces the owner's rewrite when any were dropped. The cases hold the
repair to that boundary: an all-retired file is emptied at one row and at two hundred, a retired
row beside a live one goes while the live row keeps its acknowledgement, a clean file is not
rewritten a second time, and an incomplete observation still cannot reclaim a live row while a
complete one reclaims only the record it no longer observes.

## Evidence

- An all-retired file is emptied on disk at both sizes.
  `test_only_retired_rows_are_physically_removed`
- A live row beside a retired one survives the reclaim.
  `test_a_retired_row_beside_a_live_row_is_removed_and_the_live_row_survives`
- A settled file is not rewritten again; the observation rules are unchanged.
  `test_a_clean_file_settles_and_is_not_rewritten_again`,
  `test_an_incomplete_observation_still_cannot_reclaim_a_live_row`,
  `test_a_complete_observation_reclaims_only_what_it_no_longer_observes`
