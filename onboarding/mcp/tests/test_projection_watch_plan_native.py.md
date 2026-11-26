# mcp/tests/test_projection_watch_plan_native.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

A test suite for projection watch plan native.py.md: it drives the behaviour the commentary states and asserts it.

## Code Commentary

The projection watch plan is exercised against the real watcher rather than a stand-in, so the inputs it names are the ones the watcher reports. A parametrized unit case (`test_held_watch_admits_receipts_and_ignores_taskless_message_artifacts`, `:143–199`) additionally exercises `projection_watch_plan`, `_watch_filter`, `_judge_planned_changes`, `is_held_receipt`, `plan.admits_file`, and `projection_domains_for_paths` across ordinary, earlier-`notes/`, and receipt-like coordination-root ancestors to prove real taskless and task-bound receipts (including under `tasks/messages/master`) are admitted to `ATTENTION_HELD` while taskless `messages/*`, `message-bindings/*`, and `history/*` artifacts are ignored.

## Boundaries

The obligations above are the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- The watch plan parks on the real condition and registers no synthetic early signal, so the inputs it names are the ones the watcher reports [1]
