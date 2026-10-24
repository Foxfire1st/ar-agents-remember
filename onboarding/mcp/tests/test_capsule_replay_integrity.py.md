# mcp/tests/test_capsule_replay_integrity.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

A saved launch is replayed from its frozen detail snapshots, so those snapshots must still be trustworthy when
it is sent: every frozen revision is checked against its own record, a missing or non-regular target is
refused, and a rebound report folder is refused even when the bytes are unchanged. The host boundary is a
stand-in, so no agent is created or opened.

## Code Commentary

### Logic

`leaf_preparation()` prepares a real leaf and restores its receipt, `_frozen_receipt()` writes a saved
receipt and `_validate()` runs the replay check. `_HostBoundaryReached` stops at the fake host seam, and
`saved_launch()` builds the saved start the last two cases replay.

- **Frozen, not current.** `test_replay_checks_every_frozen_revision_without_reading_the_current_corpus`
  proves each frozen revision is checked without the current corpus being read.
- **Refused shapes.** `test_replay_refuses_missing_or_nonregular_detail_targets`,
  `test_replay_refuses_a_rebound_report_folder_even_when_detail_bytes_are_unchanged` and
  `test_replay_refuses_incomplete_detail_references_instead_of_skipping_them` refuse a missing target, a
  rebound folder with matching bytes and an incomplete reference, and restore an absent valid legacy link.
- **Before the host.** `test_saved_start_replay_refuses_missing_details_before_the_host_call` refuses before
  the host is called, and `test_held_opening_refuses_changed_details_and_preserves_waiting_messages` refuses
  changed details on the delayed held-seat opening path while keeping the waiting messages.
- **Real preparation.** `test_real_leaf_preparation_restores_details_beside_local_handover` keeps frozen detail
  bytes across three role cases, with the Worker's detail supplied at the compiler seam.

### Conventions

The fixture closes its own override stack before unittest cleanup and checks the captured compiler identity
without undoing the shared pytest stack.

### Invariants And Boundaries

- A replay reads the frozen snapshot, never the current corpus.
- Bytes matching is not enough: a reference whose folder was rebound is refused.

## Evidence

- The replay checks every frozen revision without reading the current corpus. [1]
- The replay refuses missing or non-regular detail targets. [2]
- A rebound report folder is refused despite matching bytes, and an absent valid legacy link is restored. [3]
- Shape controls refuse mismatched detail names, given paths and malformed or non-sibling saved handover references. [4]
- A saved-start replay refuses missing details before the host call. [5]
- A held opening refuses changed details and preserves waiting messages. [6]
- Real local preparation and receipt restoration preserve frozen detail bytes for three role cases without launching a host. [7]
- The fixture closes its private override stack before cleanup and checks the captured compiler identity. [8]
