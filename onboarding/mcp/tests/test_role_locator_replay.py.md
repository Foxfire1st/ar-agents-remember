# mcp/tests/test_role_locator_replay.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Replay and terminal cleanup read the request's locator as part of the saved launch state. A detailed receipt that lost only its alias is prepared again before the host sees the call; a locator already pointing at another folder refuses a real preparation before any artifact is written; and a terminal group pipeline reclaims each alias once while keeping every collected report byte.

## Code Commentary

The `detailed_receipt` fixture prepares a real worker hand-over, publishes its artifact and complete hand-over file, and freezes the bytes, inode and modification time of the artifact, the hand-over file and every instruction detail before writing a receipt. `test_detailed_receipt_rebuilds_only_its_lost_locator_before_host_replay` deletes the locator and executes the prepared launch from the persisted JSON alone: the alias is rebuilt at the artifact's folder, a second execution reuses the same inode, the saved opening reaches the host unchanged, the locator opens bytes matching the receipt's SHA-256, and every frozen file keeps its mode and identity. The same case then plants a locator aimed at a foreign folder and gets a 409 with no host call and no write there, and alters an instruction detail to show the frozen-detail refusal still holds. `test_real_detailed_preparation_refuses_a_collision_before_artifact_writes` pre-seeds a locator at a foreign directory with a kept marker and drives the real `prepare_role_handover`: it refuses, the foreign folder is untouched, and no detail, hand-over text or hand-over object appears anywhere under the coordination root. The parametrized `test_terminal_group_reclaims_each_alias_once_and_keeps_every_report` builds two and eight request folders, checks that group cleanup calls the remover exactly once per alias, leaves no alias standing, and compares every collected report relative to its collected root with the frozen bytes.

## Evidence

- A persisted detailed receipt rebuilds only its lost locator before host replay, and the next replay reuses the same link. [1]
- The rebuilt locator opens the artifact's exact bytes, the saved opening reaches the host unchanged, and every frozen detail keeps its mode and identity. [2]
- A locator that leads elsewhere refuses replay with a 409 before any host call, and an altered instruction detail is refused as not frozen. [3]
- A real detailed preparation refuses a locator collision before any artifact write and leaves the foreign folder and its contents as they stood. [4]
- A terminal group reclaims each alias exactly once and keeps every collected report byte at two and eight requests. [5]
