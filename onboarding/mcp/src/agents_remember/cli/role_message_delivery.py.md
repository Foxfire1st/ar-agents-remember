# Role message delivery transaction

## Governing Overview

[Repository MCP overview](../../../overview.md)

## Purpose

Provide the shared text-limit, message-file/attachment/store/link, successor and long-reply helpers selected by the composed `paseo_role_tools` message flow. Filing primitives remain in `role_message_files`. The uncalled Attempt-4 duplicate delivery is removed with the tests that reached only it, and the module no longer holds a recipient resolver of its own: resolution, holding and delivery live in the composed facade (`paseo_role_tools`), which calls this module's shared refusal constructors such as `_refuse_over_limit` and `_archived_with_successor` on its public path.

## Contract

The remaining resolver accepts exactly one receipt-bound agent ID or a role plus selection references and refuses self, unfinished-start, absent and ambiguous recipients. Its refusal of unfinished starts is historical private-dispatch behavior, not the current facade’s holding path. Current public resolution holds an unfinished-start message when its recipient store is known; taskless and leaf-seat scans preserve their explicit ambiguity rules. Archived-ID advice names a same-selection successor without silently redirecting or unarchiving. Closed-session revive belongs to the facade, which calls `role_activity.resume_role_agent` with the receipt and publishes identity before native resume; this module carries no private resume of its own.

Only `text` counts against the supplied settings limit; over-limit text refuses with count/limit and `body`/`attach` alternatives. The resolved-recipient facade prologue uses shared attachment/link/store primitives to publish a complete file before its native-send path; link establishment can warn and continue without replacing an occupied path. The unfinished-start hold bypasses this prologue and does not establish its file/pointer guarantee. On filed branches, wake text names a path/hash rather than pasting body/attachment contents. Investigator admission precedes native send/resume. A capacity refusal is caught by the facade after filing and retains the refusal record, so no private pre-attempt cleanup contradicts it. Successful unheld delivery does not establish every composed branch’s behavior.

> **Retained historical source account — superseded by the current contract:**
> The current facade owns native closed-session revive under the scope verifier and upstream permission/busy holding under R100. Holding never answers a prompt; unexpected host replacement is disclosed rather than credited as intentional steering. The shared long-reply helper files a whole recipient-to-sender reply and carries its bounded prefix/file identity when the unheld dispatcher invokes it with a filed message. `_held_then_delivered` merges the held wait without invoking this helper, so its reply is not qualified by that cut/file behavior. Facade-local wait is outside the capacity lock. The Attempt-4 duplicate dispatch this account was written against no longer exists; these implementation gaps remain statements about the facade, not a promise that they are resolved.

## Boundaries

> **Retained historical source account — superseded by the current contract:**
> If a long wait reply cannot be filed, the prefix is still returned with truncation detail and a warning; do not claim the full reply was retained then. Report collection failure is separately owned by the facade and does not negate a taken message. Sender/recipient link warnings do not grant authority to replace existing paths. Successor naming does not grant the caller permission to start a role.

## Code Commentary

The reply-filing helper retains the complete waited.text in both successful filing and filing-failure paths, together with file identity or loss/truncation facts. It does not itself cut to the delivered prefix; downstream answer completion owns that fit. Failure of the separate reply file is not proof that all text was lost: whole-detail retention is a distinct, fallible path. Existing held-queue draining and helper-bypass qualifications remain unchanged.

## Evidence

- **Retained historical source account — superseded by the current contract:** Count only text and refuse excess without silently moving or truncating it. [1]
- **Retained historical source account — superseded by the current contract:** Archived id refusal names a same-selection live successor without changing recipient identity. [2]

- **Retained historical source account — superseded by the current contract:** When invoked with a filed message, the long-reply helper files the whole reply or discloses failed filing while returning the prefix; held-drain waits do not invoke it. [4]


## Current shared file publisher

- The composed facade calls this shared publisher to render/store the whole message; storage failure discards message-owned attachment copies and refuses before native send, while success returns the filed identity and wake payload. [5]


- The reply-filing helper retains the complete waited.text in both successful filing and filing-failure paths, together with file identity or loss/truncation facts. It does not itself cut to the delivered prefix; downstream answer completion owns that fit. Failure of the separate reply file is not proof that all text was lost: whole-detail retention is a distinct, fallible path. Existing held-queue draining and helper-bypass qualifications remain unchanged. [6]
