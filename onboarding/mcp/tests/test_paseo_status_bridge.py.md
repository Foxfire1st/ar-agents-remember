# mcp/tests/test_paseo_status_bridge.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

The bridge asks the native client for agent state and the last idle turn without reading unrelated timeline data. Resume opens only a closed target session and leaves every other agent alone. Controlled native-client responses supply state/event fixtures.

The real Node bridge script also runs against a scripted daemon client that enforces 200-entry listing pages. Cases pin complete pagination, archived-ID filtering, the ten-page bound and `hasMore` without a next cursor. A tree-reader composition proves missing IDs from an incomplete census stay `agents: null`, while a completed listing resolves the recorded live/archived agents. This is native-script/controlled-client evidence, not installed-host consumption.

## Evidence


## Current contract evidence

- The scoped current source carries the module/document behavior described above. [1]
- The real Node bridge script also runs against a scripted daemon client that enforces 200-entry listing pages. Cases pin complete pagination, archived-ID filtering, the ten-page bound and `hasMore` without a next cursor. A tree-reader composition proves missing IDs from an incomplete census stay `agents: null`, while a completed listing resolves the recorded live/archived agents. This is native-script/controlled-client evidence, not installed-host consumption. [2]

## Developer seats use the completed listing

The recorded-agent case also composes `seat_list` over the same paged native-script fixture: a complete listing includes the Manager on page two and returns `complete: true`; a cursorless truncated listing returns no seats and `complete: false`. This extends the controlled census evidence to the developer's recipient list without turning an unreached agent into a proven absent one. It remains controlled-client evidence, with no installed-host consumption asserted.

- The same complete/incomplete census is applied to the document tree and developer seat list. [3]
- The scripted native listing retains its page and termination bounds. [4]
