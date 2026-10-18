# mcp/tests/test_review_memory_watch.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Document the assertion and fixture obligations declared by this test source.

## Code Commentary

Native watch tests drive real async stream, ten edits/publication latency bound (the assertion is a three-second maximum over ten edits, with the asyncio waits bounded by the shared hang guard rather than a fixed per-call timeout), baseline registration race, cancellation during admission, shared real projector reconnection/no idle walks, unwired/native failure with ordinary stream still usable, real HTTP disconnect before shutdown and canonical live-memory admission. This source contains native behavior assertions; this helper did not execute them.

### Declared Assertions

- `test_native_open_review_ten_markers_and_close`
- `test_change_during_registration_is_not_swallowed_by_baseline`
- `test_cancel_during_root_admission_reaps_the_worker`
- `test_route_multiplexes_native_and_real_projector_and_reconnects`
- `test_existing_sse_route_accepts_review_context_and_refuses_unwired`
- `test_watch_refusal_or_native_failure_keeps_ordinary_stream_usable`
- `test_app_factory_passes_the_connection_root_port`
- `test_real_http_disconnect_retires_native_watch_before_server_shutdown`
- `test_dashboard_port_resolves_only_canonical_live_memory_without_capture`

This is a declaration inventory, not a collected parametrized-case total or execution result.

### Evidence Boundary

The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.

## Evidence

- Native watch tests drive real async stream, ten edits/publication latency bound (the assertion is a three-second maximum over ten edits, with the asyncio waits bounded by the shared hang guard rather than a fixed per-call timeout), baseline registration race, cancellation during admission, shared real projector reconnection/no idle walks, unwired/native failure with ordinary stream still usable, real HTTP disconnect before shutdown and canonical live-memory admission. This source contains native behavior assertions; this helper did not execute them. [1]
