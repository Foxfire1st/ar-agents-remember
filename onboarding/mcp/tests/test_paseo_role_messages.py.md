# mcp/tests/test_paseo_role_messages.py

## Current paired source contract — scoped assertions and incoming catalogs

Composed controlled-runtime cases hold permission/start-unfinished/unwritable-turn messages and deliver waiting work in order; two live leaf occupants refuse ambiguity and completed holders retain the seat until archived. Non-holdable failed resumes retain undelivered message files. Busy holding is not a general undelivered-file refusal or a sender-retry instruction. Current fixtures patch facade-local native/resolve owners; files, sender-line composition, limits, wait and independent report collection remain source assertions, not live host proof.

This section supersedes contrary earlier prose only for these changed seams; retained evidence and useful unaffected accounts are not deleted or promoted to new proof.

- Composed controlled-runtime cases hold permission/start-unfinished/unwritable-turn messages and deliver waiting work in order; two live leaf occupants refuse ambiguity and completed holders retain the seat until archived. Non-holdable failed resumes retain undelivered message files. Busy holding is not a general undelivered-file refusal or a sender-retry instruction. Current fixtures patch facade-local native/resolve owners; files, sender-line composition, limits, wait and independent report collection remain source assertions, not live host proof. [3]


## Message transport contract coverage

Controlled-runtime cases now require one timestamp/sender/recipient message file and returned SHA-256, preserving unchanged bodyless delivered text and existing receipts. Busy and failed-resume attempts retain undelivered audit records. The refusal vocabulary adds message-too-long, message-file-failed and settings-invalid. Lookup, capacity, revival, wait/timeout and independent collection-error behavior remain; these are stub-controlled filesystem assertions, not live host execution.


## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

Recipients come from this line's receipts and exact role/task selection; multiple candidates and missing binding refuse, including two live occupants of the same leaf seat. Pending permissions instead hold messages without answering the prompt. Unfinished starts and unwritable active turns use the same held store; a fresh message remains behind waiting work even after the host becomes writable. Closed sessions pass Revive scope checks before send. Wait tracks the consuming turn, and timeout leaves the message delivered rather than causing duplicate send or turn cancellation. An R71 case proves delivery proceeds despite collection errors with per-agent isolation and the failure returned separately.

## Hold, single-copy, answered-batch and steer-or-hold cases

`RoleMessageTests` holds the cases this change adds. `test_a_running_turn_is_steered_or_held_by_its_provider_and_never_cut_off` steers a running turn only for a provider marked as taking one and holds the message as `recipient-in-turn` for the other, whose turn keeps running. `test_the_hosts_own_activity_record_holds_a_message_the_snapshot_calls_idle` holds a message the agent snapshot calls idle when the host's publication says `in-turn`, steers for a provider known to take one, and delivers the held message when that record says the turn ended. `test_an_unknown_send_outcome_is_not_delivered_twice` and `test_a_copy_the_recipient_already_holds_is_not_sent_again` keep one copy: the second sends nothing when the recipient's timeline already carries the attempted id, without a host that deduplicates. `test_a_delivery_that_takes_held_messages_answers_ok` answers `accepted` with no `turnId`, and `RoleMessageResponse` validates it. `test_a_held_batch_preserves_the_reported_replacement_and_warning` keeps `taken` `replaced` with the plain replacement warning through the same answer model. These are the controlled fixture's assertions, not live host execution.

## Evidence


- The scoped current source carries the module/document behavior described above. [1]


- Controlled-runtime cases now require one timestamp/sender/recipient message file and returned SHA-256, preserving unchanged bodyless delivered text and existing receipts. [2]
