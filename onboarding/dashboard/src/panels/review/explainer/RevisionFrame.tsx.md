# dashboard/src/panels/review/explainer/RevisionFrame.tsx

## Governing Overview

[Route overview](../../overview.md)

The first iframe load for a session sends the ordinary binding. A later load in that session is a departure that revokes that frame’s channel and reopens the saved revision. The dashboard owns its Effects preference, and the binding carries no effects field.

## Purpose

Shows one retained revision of the explanation in the isolated host's frame, sends that frame the trusted stale ids, and turns the page's own offers into tray picks without starting a model.

## Code Commentary

- The sandbox and the document address come from the session the host opened, and a message is accepted only from this frame's own window — never the top window, never a sibling.
- Supplied protocol, session, revision and comparison fields are checked for mismatches, and repeated string request ids are refused before forwarding. This precheck does not require optional fields to be present; the host protocol is the final validator.
- The stale envelope is bounded: ids must have the admitted bounded shape and must belong to the revision when a nonempty knownPartIds list is supplied; at most 32 travel, and the total stays the true count, with dropped and truncated counts reported.
- Document departure or a second load revokes only this frame's channel and reopens the saved revision, keyed by repository, master, leaf, revision and slot, so the sibling frame is untouched.
- A page may offer selections or request an explanation; both become tray picks, replaced rather than duplicated, and a forward the host refuses rolls its pick back.
- There is no start, no generate and no resume here: a frame is a channel, not a model turn.

## Evidence

- The stale envelope admits only valid part ids, caps what it sends, and reports what it dropped or truncated [1]
- One channel per revision and slot is opened, closed and reopened by key, and closed on disposal [3]
- Only a protocol refusal name from the host's own answer reaches the page's refusal line [5]
- The frame's shell states its revision, slot, dropped and truncated counts and last refusal [6]

Binding checks here reject mismatching supplied protocol/session/revision/comparison fields and repeated string request ids; they do not require each optional field to exist. The host protocol remains the final validator of a forwarded envelope. Trusted stale-part envelopes keep the true total while sending at most 32 valid ids and naming dropped/truncated items.

- The frame bounds the stale list and reports omitted or truncated parts. Forwarded messages reject mismatching supplied identities and repeated string request IDs. [7]

- Stale-part IDs have a bounded lowercase form and exclude page. A nonempty known-part set also constrains membership. [2]

- The listener accepts its own frame window, bounds forwarding, rejects mismatches in supplied identity fields and rejects repeated string request IDs. [4]

- The first iframe load for a session sends the ordinary binding. A later load in that session is a departure that revokes that frame’s channel and reopens the saved revision. The dashboard owns its Effects preference, and the binding carries no effects field. [8]
