# mcp/tests/test_previous_host_removed.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds PNT-R08: the build names its previous host nowhere and serves and reads nothing of it. It scans every
tracked file for the host's name outside an allow-list, proves a settings file carrying the former block
loads as if the block were absent, and keeps the dashboard's routes distinct from the former paths.

## Code Commentary

### Logic

`git()` runs Git on the repository at a given root and no other, `tracked_files()` and `content_of()` read
each tracked file — a link's target text included — and `named_in()` reports where a file names the previous
host outside the allow-list. `words_of()` matches the name as a word.

- **The tree.** `test_no_tracked_file_names_the_previous_host_outside_the_allow_list` scans the tracked
  tree; `test_the_allow_list_holds_unrelated_words_and_the_tests_that_must_name_the_host` keeps the
  allow-list narrow, and `test_the_search_finds_each_kind_of_name_and_passes_only_what_is_listed` plus
  `test_the_tree_search_reads_tracked_files_links_included` prove the search finds each kind of name —
  a symlink's target included — and passes only what is listed.
- **Leftover settings.** `test_a_settings_file_with_the_former_block_loads_as_if_the_block_were_absent`
  loads a settings file that still carries the former block as if it were absent.
- **Routes.** `test_the_launcher_registers_its_eleven_routes_and_answers_404_on_the_former_paths` registers the
  launcher's eleven routes and answers 404 on each former path, and
  `test_no_route_of_the_dashboard_application_matches_a_former_path` checks the dashboard application's
  routes against `FORMER_ROUTES`.
- **Previous line on disk.** `PreviousLineReceiptTests` leaves a previous line's receipts and reports
  unread and unchanged, and refuses a receipt under the former schema name at this line's address.

### Conventions

`ROUTES` and `FORMER_ROUTES` are the two inventories a route case needs; `METHODS` fixes the methods a
former path is probed with.

### Invariants And Boundaries

- The previous host's name survives only in the allow-list, which holds unrelated words and the tests that
  must name it.
- A previous line's on-disk state is neither read as a receipt nor rewritten.

## Evidence


- The tracked tree names the previous host nowhere outside the allow-list, and the former block loads as absent. [1]


- Eleven current launcher routes include GET /api/role-launch/warmup and GET /api/role-launch/saved-catalog while every former-path 404 check remains. [2]
