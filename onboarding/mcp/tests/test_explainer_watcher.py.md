# mcp/tests/test_explainer_watcher.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The moved watcher's measurement: what a notice names, when no notice is earned, that a planning leaf compares master tips and captures nothing, and that no path sends, holds or writes a message.

## Code Commentary

- The notice names the recorded comparison and its per-block count; an unrecorded capture reads as a new state, and a binding that has not moved earns nothing.
- An unreadable count is no notice at all, never a zero, and a leaf without an environment has no notice.
- A planning leaf shows the master tips and captures nothing, and a planned notice follows the contract the build declared without a fallback.
- The capture writes Git objects and no pin or record, and no path sends, holds or writes a message.

## Evidence

- The case `test_the_notice_names_the_recorded_comparison_and_its_block_count` protects the notice naming its comparison and per-block count. [1]
- The case `test_an_unreadable_count_is_no_notice_rather_than_a_zero` protects an unreadable count earning no notice and never a zero. [2]
- The case `test_a_planned_moved_notice_follows_the_builds_declared_contract_without_fallback` protects a planned notice following the declared master contract with no capture, message or record. [3]
- The case `test_no_path_sends_holds_or_writes_a_message` protects the watcher never sending, holding or writing a message. [4]
- The case `test_the_capture_writes_objects_and_no_ref_or_record` protects a capture writing objects and nothing that would claim a comparison. [5]


