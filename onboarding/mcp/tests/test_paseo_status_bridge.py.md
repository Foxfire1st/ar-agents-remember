# mcp/tests/test_paseo_status_bridge.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Runs the bridge's `agent-state` and `agent-resume` commands as the real script against a scripted
daemon client, and composes the document-chat tree and developer-seat list over the same listings. It
proves an agent's state is read without its timeline, that paged listings report when they did not end,
and that a recorded agent a listing never reached is unknown to the tree rather than gone.

## Code Commentary

### Logic

- **State reads.** `AgentStateScriptTests.test_agent_state_reports_an_agent_without_reading_its_timeline`
  and `test_agent_state_reads_how_the_last_turn_of_an_idle_agent_ended` separate an identity read from a
  timeline read, and an idle agent's last turn from the agent itself.
- **Paged listings.** The fake client enforces the host's limit of 200 entries per page
  (`fetchAgents` throws above it) and can end a listing on `hasMore` with no next cursor;
  `test_agents_live_lists_in_pages_and_says_when_the_listing_did_not_end` pins the requested pages
  `{limit: 200}`, `{limit: 200, cursor: "200"}`, `{limit: 200, cursor: "400"}` and the incomplete-listing
  answer.
- **Unknown is not gone.** `test_a_recorded_agent_a_listing_did_not_reach_is_unknown_to_the_tree_and_not_gone`
  composes `document_chat_tree` and `seat_list` over the listing: an agent past the page the listing
  reached stays unknown to the tree, while an archived id is reported as archived.
- **Resume.** `test_agent_resume_opens_a_closed_session_and_leaves_every_other_agent_alone` resumes one
  closed session and records no call for the others; a `NO_ROLLOUT` resume error is answered as a named
  failure rather than a silent success.

### Conventions

Every case starts the real script through the fixture's `call()` helper against the scenario's runtime
(`runtime()`), then asserts on what the fake client recorded (`recorded()`) as well as on the answer.

### Invariants And Boundaries

- A listing that announces more agents without naming a page is incomplete, and an incomplete listing
  never turns a recorded agent into a gone one.
- Resume touches one agent; the rest of the fleet's state is untouched.

## Evidence

- State reads without a timeline, pagination bounds, archived filtering and resume are covered here. [1]
- The scripted daemon client enforces 200-entry pages, `hasMore` without a cursor, archived filtering and the ten-page bound. [2]
- Complete and incomplete listings are applied to the document tree and the developer seat list alike. [3]
- The native listing's page and termination bounds. [4]
