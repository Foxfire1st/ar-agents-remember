# mcp/tests/role_instruction_wording_support.py

## Governing Overview

[overview](overview.md)

## Purpose

The skill trees, the forbidden strings and the file readers the two wording case modules share, split out so the instruction-file cases and the handover cases read the same canonical tree and matcher.

## Code Commentary

`CANONICAL` is the checkout's `skills` tree and `PACKAGED` the runtime copy the capsule compiler reads. `FORBIDDEN` lists the host strings a role text may not name, including the removed tools and the earlier seat variables, and `forbidden_in` searches case folded. `REPORT_DIRECTORY` is the report segment a handover states. `LAUNCHER_ROLES` is derived from the launcher role arguments through `canonical_role`, `STARTERS` names the three starting roles, and `_NAMED_TOOL` matches a public tool in code font. `instruction_files` reads the lifecycle composition manifest and returns the router plus each launcher role's file and the operations that apply to those roles; `read` and `role_text` load a file and collapse a role file's whitespace. The module also holds the step tables and controls the instruction-file cases share: `RELOCATED_WORKING_STEPS` and `COORDINATION_ACTION_STEPS` name, per owning file and heading, the clauses that step must carry; `assert_nonstarter_role_boundary` requires the Reviewer's standing no-start restriction in its role file and a start-no-role sentence for the other non-starting seats; `assert_detail_link_provenance_controls` and `assert_memory_review_owner_link_controls` run the detail-link and memory-review owner-link checkers against planted mutants that must fail.

## Invariants And Boundaries

The forbidden search covers the report directory segment as part of the whole text, so a rename of that directory cannot leave an unchecked spelling. The packaged tree is read separately because a canonical rewrite is not live until the sync has run.

`assert_message_handover_delivery` requires the held-delivery clause (queued eventual delivery, no resend, a handover taken only on a reply naming the object, withdrawal by `withdraw_held_message_id`, no polling) in `core/authority.md` and, for each non-Bootstrap role, exactly once in its compiled orientation shared block, which must equal `core/every-role.md`; for Bootstrap it only requires that the message-handover pointer is absent. For every non-Bootstrap sender it then delivers that role's own message-handover action from `reference/message-handover.md` and checks the numbered full-store busy-refusal steps, reporting the second refusal through the role's route and never to oneself, the absence of semantic acceptance from a receipt, narrowest-task message filing and receipt scope; Bootstrap must not carry the detail pointer. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence
### Repo-Internal References

- The support module defines the forbidden vocabulary and its case-insensitive forbidden_in matcher. LAUNCHER_ROLES is deduplicated from canonicalized LauncherRole type arguments. [1]
- instruction_files reads the lifecycle composition manifest and returns its router, launcher-role files and sorted operations whose applies_to_roles intersects the launcher-role set. [2]


- `assert_message_handover_delivery` pins the held-delivery clause once in each non-Bootstrap role's compiled shared block (Bootstrap is only checked for an absent message-handover pointer) and checks each non-Bootstrap sender's own delivered message-handover action for the busy-refusal steps, receipt scope and no semantic acceptance from a receipt; these are source assertions, not a fresh invocation, host result or AR acceptance. [3]

- The relocated working steps name each owning file, heading and required clauses. [4]
- A repeated ordinary label is accepted while every detail-marker link must stay exact; planted mutants fail. [5]
- The coordination action steps name the pre-action pointers each owning step must carry. [6]
- A non-starting seat keeps its no-start boundary: the Reviewer's in its role file, the others by a start-no-role sentence. [7]
- The memory-review owner-link checker rejects a missing action, wrong owner or fragment, and a repeated link. [8]
