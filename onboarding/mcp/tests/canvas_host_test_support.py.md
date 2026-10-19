# mcp/tests/canvas_host_test_support.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Shared support for the canvas host cases: real published revisions, request helpers and isolated fixtures for consuming a proof record without the ignored dashboard build.

## Code Commentary

- It builds through the real publication path rather than a stub, which is why the published bytes in the cases are real.

- `proof_frontend` copies the proof consumer module into a temporary package and supplies a fabricated frontend. `proof_bundle` binds a copied record to that fixture with the real source-binding and policy-digest functions. Its observations are fabricated consumer input, not browser evidence; published-revision fixtures still use the real publication path.

## Evidence

- The support builds its published revisions through the real publication path. [1]

- Consumer proof fixtures use fabricated frontend bytes with real source bindings; they are not browser observations. [2]

- The consumer record is rebound to its fixture using the actual binding and digest functions. [3]
