# mcp/tests/test_canvas_serving.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The serving surface: the panel reads a saved page and starts nothing, one explicit start runs once, and a channel is revoked without an effect when it is disposed.

## Code Commentary

- The saved-first read starts no model and resumes no session.
- A session serves its own document and assets only; a replacement revokes the old channel.
- The protocol route refuses replayed and foreign requests by name.

- Script-serving consumer cases use a fabricated frontend-bound record. A separate shipped-record case expects an inert result without the built frontend and a proven result with it; neither fixture is a fresh browser proof.
- Both HTTP and HTTPS cases check omitted and explicit default ports, foreign names, wrong ports and a mismatching explicit bound port.

## Evidence

- The case `test_the_panel_reads_a_saved_page_and_starts_nothing` protects this behaviour. [1]
- The case `test_a_session_serves_its_own_document_and_assets_only` protects this behaviour. [2]
- The case `test_revocation_ends_the_channel_without_an_effect` protects this behaviour. [3]

- The shipped record is inert without the built frontend and must prove the available built frontend. [4]

- Omitted ASGI ports are normalized without admitting a foreign host or mismatching port. [5]
