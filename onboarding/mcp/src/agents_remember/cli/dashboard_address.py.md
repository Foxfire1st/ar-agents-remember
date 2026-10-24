# mcp/src/agents_remember/cli/dashboard_address.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Answer where a started seat is continued: the dashboard's own address once its origin serves a page, and the host's own web route to that agent's chat.

## Code Commentary

`dashboard_address` spells the product's own UI address — loopback on the port the settings hold (`dashboard.port`). `dashboard_address_for` asks `serving.daemon.ensure`, the dashboard owner the MCP boot hook already calls, to adopt or start the dashboard, then asks the origin for its front page: a status under 400 is the proof, because a listener that answers with an error, or a port another process holds, would pass a connect check and fail the user. Only then is `dashboardAddress` published; otherwise the answer carries no address and a `dashboardAddressDetail` naming the observed origin status and the owner's action. `chat_address` builds the host's own web route for one agent from the first `paseoRuntime.embed` entry, so a start never invents a loopback URL for the host; no configured runtime, no agent, no reported server id or no embed entry each answer `None` with its own named reason. `chat_address_for` reads the server id through the bridge lazily and reports a bridge refusal the same way.

## Evidence

- The address is answered only after the origin answers with a page. [1]
- A dashboard that does not answer, and an owner that raises, are reported rather than published. [2]
- The owner's own report and the origin's own status decide the answer together. [3]
- The chat route is built from the configured embed entry and answers a named reason when it cannot. [4]
- The origin probe takes a status under 400 as served, not a TCP accept. [5]
