# mcp/tests/test_canvas_kit_assets.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Kit files as revision assets: a page that names a kit file carries it under the contract path, a page renders offline, and an unshipped or tampered file is refused by name.

## Code Commentary

- The contract path a page names is the path the host serves.
- A tampered byte is refused rather than served, and a page with the kit needs no network.

## Evidence

- The case `test_a_named_kit_file_is_carried_under_its_contract_path` protects this behaviour. [1]
- The case `test_an_unshipped_or_tampered_kit_file_is_refused_by_name` protects this behaviour. [2]
- The case `test_a_page_that_carries_a_kit_file_is_ready_and_needs_no_network` protects this behaviour. [3]
