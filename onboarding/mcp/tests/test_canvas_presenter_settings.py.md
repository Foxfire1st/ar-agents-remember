# mcp/tests/test_canvas_presenter_settings.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Launch settings: the user file supplies the launch and its provenance, a repository row may not set permission authority but may supply a plain choice, and an unknown key fails loudly naming the file.

## Code Commentary

- Permission-bearing choices come only from the user's own settings.
- A repository row is named as a plain choice and cannot widen authority.

## Evidence

- The case `test_a_repository_row_may_not_set_permission_authority` protects this behaviour. 
- The case `test_an_unknown_orchestration_key_fails_loud_naming_the_file` protects this behaviour. 

- Retired at the fifth freeze d59c3493: mcp/tests/test_canvas_presenter_settings.py::test_a_repository_row_may_not_set_permission_authority - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976; mcp/tests/test_canvas_presenter_settings.py::test_an_unknown_orchestration_key_fails_loud_naming_the_file - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976. Retired means the anchor no longer stands, not that the cited subject was deleted.
