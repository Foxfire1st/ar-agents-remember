# mcp/src/agents_remember/serving/canvas.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Hosts retained generated revisions and their bounded frame-message sessions. The mounted application rejects the retired canvas authoring POSTs before these routes; the legacy presenter start/operation helpers remain in this module, while saved-page, asset and session viewing continues.

## Code Commentary

- `page` and `page_asset` serve only the document and admitted assets of the live session's own revision, with the existing policy headers. `_frame_scope` refuses a missing named frame directory instead of substituting another frame.
- `open_session` accepts the explicit target from the body or nested route parameters, with supplied body values taking precedence. An explicit positive revision opens that revision's retained manifest; without one, the saved ready revision opens. Neither viewing path starts a model.
- Explicit-revision sessions are pinned. Opening one replaces only channels matching repository, leaf, frame, revision and slot; opening without an explicit revision keeps whole-frame replacement. Distinct retained revisions can therefore remain open for comparison. Revocation clears the named channel's pin/slot bookkeeping.
- A pinned channel resolves evidence from its own retained manifest and remains current for its own revision while that manifest exists. An unpinned channel keeps the prior ready-pointer checks, so a moved ready revision refuses its old display messages and evidence lookup rather than borrowing the new revision.
- `session_message` retains debit-before-parse, binding, replay and rate checks before the extracted dispatcher. An admitted selection offer becomes one replaceable per-revision pick targeted at the explainer, with the question/choice strings preserved. The transient ordered selection map retains at most 64 keys.
- An admitted explanation request returns a separate removable explainer-targeted pick carrying the full question. Its diagnostic entry alone is shortened to 200 characters; optional presenter request recording reports whether it succeeded. Neither page-message operation sends the pick or starts a turn.
- The legacy `generate` helper still validates explicit activation and the attempt helpers retain their direct-call implementation. They do not restore the old mounted authoring route: `serving/app.py` registers `canvas-authoring-replaced` refusals before `register_canvas_routes`. `frame_state` remains the trusted saved-state read and `attempt_operation` retains its direct legacy operation dispatch. Retained nested session aliases and session-value page resources use this same host registry.

## Evidence

- The frame route serves one live session's own document and admitted assets. 
- A frame message is bound, bounded and refused by name before it is applied. [3]
- Both surfaces are registered before the static mount. 

- The direct legacy Generate helper validates explicit activation before preparing evidence. 
- An explicit positive revision opens only its retained manifest; absence opens the saved ready revision. [5]
- Pinned replacement matches revision and slot, while an unpinned opening replaces the frame's channels. [6]
- A selection offer preserves its text in one replaceable revision-scoped explainer pick and starts no model. [7]
- An explanation request returns its full question in a removable explainer pick without sending or starting. [8]
- A missing named frame directory refuses before another frame can supply bytes. [9]
- Evidence lookup reads the pinned revision's manifest or requires the unpinned ready revision to match. [10]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/canvas.py::page - the bytes it recorded now occur 19 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/serving/canvas.py::register_canvas_routes - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/serving/canvas.py::generate - the recorded locator no longer resolves at the candidate: the name is present in the file but not as the definition the note cited, so the anchor cannot be re-pointed by resemblance. Retired means the anchor no longer stands, not that the cited subject was deleted.
