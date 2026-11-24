# mcp/src/agents_remember/canvas/canvas-prospective-load.mjs

## Governing Overview

[Canvas route overview](overview.md)

## Purpose

Load one prospective revision in Chromium under the page policy and return a bounded observation for the Python admission owner to check.

## Code Commentary

The loopback server serves only the staged directory under the canvas-page prefix. Document and asset headers mirror the isolated frame. The ordinary browser load reports page and console errors and failed or outside requests. It observes rendered content, claims and basis references, DOM inventory, successfully loaded local assets and visible paint. Registered render takes the ordinary browser observation and any advisory sweep before its publication readiness decision. The subsequent static `check_page` enforces authored HTML media controls before publication. The suppression comparison shows visible information in the viewport.

The browser observes claim IDs and basis references separately during a bounded post-load window.

`observeInBrowser` returns these inventories alongside load and visible-content observations. Its two-second observation window says nothing about arbitrary later scripts. `answerAndExit` emits one JSON answer and exits; a browser failure returns `unavailable` rather than claiming the page was observed.

The prospective asset handler serves WebM and MP4 with their video media types.

## Evidence

- The prospective Chromium observation keeps basis references and claim ids separate through bounded post-load mutations; Python resolves both against the immutable packet. Load, isolation and paint observations establish no explanation correctness or arbitrary later-script behavior.

- The prospective server selects the WebM and MP4 MIME types from the same extension table as other assets. [1]

- The ordinary browser load reports page and console errors and failed or outside requests. It observes rendered content, claims and basis references, DOM inventory, successfully loaded local assets and visible paint. Registered render takes the ordinary browser observation and any advisory sweep before its publication readiness decision. The subsequent static `check_page` enforces authored HTML media controls before publication. [2]
