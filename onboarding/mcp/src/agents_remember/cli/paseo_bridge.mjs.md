# mcp/src/agents_remember/cli/paseo_bridge.mjs

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

The native Paseo bridge module the runtime serves.

## Code Commentary

The bridge module carries native host integration loaded beside the runtime. `closingText` concatenates the final trailing assistant messages, trims the assembled text and exposes the whole nonempty reply with `textTruncated: false`; it imposes no role-message character cut. The delivery policy layer owns settings-bound reply text and complete reply-file storage. The earlier retirement changed no bridge part; that historical observation is not a claim that this later reply transport changed nothing.

## Evidence

- The native bridge returns the assembled whole final reply without a character cut; the separate delivery policy owns truncation and filing. [1]
