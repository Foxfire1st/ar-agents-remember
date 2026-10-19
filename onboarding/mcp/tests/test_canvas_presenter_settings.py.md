# mcp/tests/test_canvas_presenter_settings.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Launch settings: the user file supplies the launch and its provenance, a repository row may not set permission authority but may supply a plain choice, and an unknown key fails loudly naming the file.

## Code Commentary

- Permission-bearing choices come only from the user's own settings.
- A repository row is named as a plain choice and cannot widen authority.

## Evidence

- The case `test_a_repository_row_may_not_set_permission_authority` protects this behaviour. [1]
- The case `test_an_unknown_orchestration_key_fails_loud_naming_the_file` protects this behaviour. [2]
