# mcp/src/agents_remember/cli/paseo_bridge.mjs

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

The native Paseo bridge module the runtime serves.

## Code Commentary

The bridge module carries native host integration loaded beside the runtime. A provider catalog row that is still loading retains `modes`, `defaultModeId` and `fetchedAt` from the discovered provider entry, falling back to empty/null only when absent, alongside its empty models and loading error. Pending model listing does not discard mode offerings the host has already supplied. `closingText` concatenates the final trailing assistant messages, trims the assembled text and exposes the whole nonempty reply with `textTruncated: false`; it imposes no role-message character cut. The delivery policy layer owns settings-bound reply text and complete reply-file storage. The earlier retirement changed no bridge part; that historical observation is not a claim that this later reply transport changed nothing.

`agents-live` reads unarchived agent IDs through `daemon.fetchAgents`, at most ten pages of 200 entries. It reports `complete` only when the runtime explicitly says `hasMore: false`; a bound or missing next cursor ends the read without establishing absence. It neither resumes agents nor reads their timelines. Whole-reply transport remains separately owned by `closingText`.

## Evidence


## Current contract evidence

- The native bridge returns the assembled whole final reply without a character cut; the separate delivery policy owns truncation and filing. [1]
- `agents-live` reads unarchived agent IDs through `daemon.fetchAgents`, at most ten pages of 200 entries. It reports `complete` only when the runtime explicitly says `hasMore: false`; a bound or missing next cursor ends the read without establishing absence. It neither resumes agents nor reads their timelines. Whole-reply transport remains separately owned by `closingText`. [2]
- A still-loading provider row retains discovered mode/default-mode/fetched-at fields, defaulting only absent values. [3]
