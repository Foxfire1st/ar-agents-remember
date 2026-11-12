# mcp/tests/test_paseo_frame.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Proves the dashboard frame is offered only to an origin the runtime settings list: the asking origin
selects its own `paseoRuntime.embed` base URL, the native server and workspace identity travel with it,
and a missing configuration, an unlisted origin or an unreachable identity each keep a named state
instead of a frame. The route-level cases drive the real HTTP route with the browser's `Origin` and
`Sec-Fetch-Site` headers.

## Code Commentary

### Logic

`frame_descriptor(config, origin, host=...)` is the unit under test: `runtime_settings()` builds three
embed entries (loopback, a tailnet host with a trailing slash and an explicit port, and a
differently-spelled pair), `reachable()` answers `HostFrameFacts(reachable=True, server_id=...)`, and
`FakeBridge` covers the bridge replies the health call may use.

- **The asking origin picks the base URL.** `test_frame_base_url_comes_from_the_embed_list_for_the_asking_origin`
  checks each listed origin gets its own frame URL — including one written with a trailing slash — and
  that the answer names no daemon home or credential.
- **Unlisted origins never reach the runtime.** Look-alikes that begin with or contain a listed origin
  (`http://127.0.0.1:97970`, `https://box.tailnet.ts.net.evil.test`, an origin in a query string) and a
  missing origin all answer `origin-not-listed`, and the `host` callback is never called for them.
- **Unavailability is named.** `test_unavailable_frame_names_not_configured_or_unreachable` keeps
  `not-configured` (no `paseoRuntime` block, naming the settings file) apart from `unreachable` with the
  connection, timeout or missing-server-id detail, and the answer carries no `frameBaseUrl`.
- **A missing workspace does not close the frame.** `test_frame_stays_available_without_a_projects_workspace`
  keeps the frame available with no workspace id and reports the workspace call's detail separately.
- **The route reads the caller's origin.** `test_route_reads_the_dashboard_origin_from_the_request`
  registers `role_launch_routes` on a FastAPI app and checks `/api/role-launch/frame` judges the
  `Origin` header when there is one — including a `null` origin, which is not replaced by the called
  host — and falls back to the request base URL otherwise.
- **Origins compare normally.** `test_origins_compare_without_case_or_default_ports` normalises case and
  the scheme's default port, so `HTTP://LocalHost:80` matches `http://localhost`.

### Conventions

Every case builds its settings and config in a temporary root through `runtime_config()`, which writes
the runtime block with `write_runtime_block` from `paseo_runtime_test_support`.

### Invariants And Boundaries

- An unlisted origin is answered before any runtime call is attempted.
- These are descriptor and request-plumbing cases: no browser embeds a frame and no provisioning runs.

## Evidence


- Origin selection, unlisted-origin refusal, the named unavailable states, workspace-less availability, route header handling and origin normalisation are asserted in this file. [1]


- The origin case pins `provisionCommand` to the active fixture settings file; the wired host-facts case copies that field from the answer, so command construction is asserted by the origin case alone. [2]
