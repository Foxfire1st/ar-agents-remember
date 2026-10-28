# dashboard/vite.config.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Build and development configuration for the dashboard: one backend target behind two prefixes, and the origin the browser is really on forwarded to the backend.

## Code Commentary

The dev server proxies two prefixes to one backend target, `/api` and `/canvas`, and both read the same `BACKEND` constant so a second prefix cannot drift from the first. `/canvas` is the backend's other surface rather than the app's: a revision frame is served at `/canvas/page/<session>/` and every asset of that frame hangs off the same prefix, so an unproxied request is answered by Vite itself with its own `index.html` and a 200, and the frame renders white while the backend sees nothing (F4). Behind the proxy the two admission facts conflict: the backend admits a request only when `Host` names its own bound address and port, and it builds a frame document's policy from the origin the page was loaded from, so with `changeOrigin` alone the policy names the proxy target and the browser blocks the frame's own `styles.css` (F5). The proxy therefore keeps `Host` for admission and states the browser's origin separately on `X-Forwarded-Host`, with `X-Forwarded-Proto` alongside it. The dashboard source fingerprint and the React plugin are unchanged by either prefix; test configuration lives in `vitest.config.ts`.

## Boundaries

This file runs only in development or a local build; the served application does not depend on the proxy. It does not decide the frame's policy, only which origin the backend is told about: `serving/canvas.py::_origin` validates the forwarded value as `host[:port]` and ignores anything carrying a scheme, path or whitespace, so a malformed header falls back to the request's own host rather than widening the policy.

## Evidence

- The dev server proxies both prefixes to one backend target: /api and /canvas read the same BACKEND constant, so a second prefix cannot drift from the first. [1]

- forwardedOrigin keeps the proxy's own Host for admission and states the browser's origin on X-Forwarded-Host with X-Forwarded-Proto, which is what lets the backend admit the request and still build the frame policy from the browser's origin. [2]

- _origin reads X-Forwarded-Host only in host[:port] shape and ignores anything carrying a scheme, path or whitespace, so a malformed forwarded value falls back to the request's own host rather than widening the frame policy. [3]
