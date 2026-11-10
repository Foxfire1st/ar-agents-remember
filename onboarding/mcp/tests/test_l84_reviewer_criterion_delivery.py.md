# mcp/tests/test_l84_reviewer_criterion_delivery.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves that the public starters file a criterion-bound intake for a held Reviewer seat and deliver it at that seat's native opening, before any inspection, bound to the calling Manager.

## Code Commentary

The module builds on `FirstMessageMatrixBase` (`role_first_message_support`) and drives one fixture world through the public calls only.

- **Manager start.** `_start_manager` starts a Manager through `start_role`; its receipt, applied tool-server environment and agent binding agree on agent ID, request ID, report path and sprint/master references, with no task reference.
- **Held set.** `_held_leaf_set` calls `start_leaf_set` with the Manager's environment: the Worker runs, and the Reviewer and Curator seats are held and not opened; the Reviewer's parent agent is the Manager, and no host agent has been created for it yet. Its held opening asks for confirmation before inspection, tells it to ask its starter for the first `role_message` when no review mode is named, requires every applicable input, and links the review intake procedure in the packaged `operations/review.md`.
- **Opening delivery.** `send_role_message` sends a body and the two shipped criteria `criteria/code-seam.md` and `criteria/report-verification.md` as attachments to the held Reviewer. An observer on the fake host's `agent-create` checks the idempotency key `ar-role-launch:<requestId>`, that the prompt starts with the held opening, and that the filed intake names the recipient and the calling Manager agent. The answer is `accepted` with `openedHeldSeat`; the Reviewer receipt becomes `running`, the Curator stays `held`, and the send boundary reports nothing missing.
- **Filed intake.** `_filed_intake` follows the prompt's `Message file:` pointer to a file under the task's `notes/messages`, checks its SHA-256, finds the full body there and not in the prompt, and checks each attachment's source digest and its byte-identical copy beside the message. Dropping the pointer or zeroing the digest makes the check fail.
- **Limits.** The host and catalog are fixture doubles. The test proves delivery to the host boundary only, not model reading, criterion use or a review verdict; it prints a `NATIVE66_DELIVERY_EVIDENCE=` JSON witness for `pytest -rP`.

## Evidence

- The module states its fixture doubles and its delivery-only limit. [1]
- The filed intake is reached by pointer, digest-checked and carries copied attachments. [2]
- The Manager is started publicly and its binding matches its receipt. [3]
- The public set starter runs the Worker and holds the Reviewer and Curator seats. [4]
- The criterion-bound intake opens the held Reviewer seat before first inspection and mutants fail. [5]
