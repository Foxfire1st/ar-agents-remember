# dashboard/src/cockpit/document-chat/knownChats.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Keeps bounded, explicitly known document-chat answers so a known selection switches before its fresh server answer arrives.

## Code Commentary

The store keeps at most 512 selections, moving a renewed answer to the newest position and dropping the oldest on overflow. One tree request names at most 256 canonical selections; oversize trees prioritize the viewed master's group and sprint without inventing an absence for omitted documents. Fresh valid arrays, including confirmed empty arrays, supersede stored knowledge; unknown/malformed batch entries preserve it. Exact just-started requests remain outside cache substitution.

The tree is asked on first visible use, a changed selection population, and every thirty seconds after the previous answer while both pane and browser tab are shown. Hidden pane/tab aborts an in-flight request and clears its timer. A cancelled answer learns nothing; reopening resumes at its genuine due time rather than issuing a request for every visibility toggle. A failed or older backend leaves the existing store usable and the selected-document read retains authority.

## Invariants And Boundaries

Cached knowledge optimizes switching, not existence authority: a fresh empty answer can invalidate it. Hidden tabs perform no polling. The batch's cap and storage bound are separate; overflow is unknown and falls back to the ordinary document read, never an inferred no-chat.

## Evidence

- The bounded store drops oldest answers after renewal and overflow. [1]
- One bounded request preserves group order and prioritizes nearby selections. [2]
- Polling requires visible pane and tab; abort and cleanup prevent stale learning. [3]
- Fresh document truth supersedes stored knowledge; an exact launched request is not substituted. [4]
