# mcp/src/agents_remember/worktrees/review_note.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

Returns the landing-answer sentence when a committed closed owner history either lacks a passed memory review fact or records a `verdictRef` outside collected `notes/reports/<rel>` form.

## Evidence


- A readable closed history without `review` returns `NO_PASS_SENTENCE`, one whose `review.verdictRef` fails `is_collected_report_ref` returns `unmapped_verdict_ref_note(verdict_ref)`, and missing, open, unreadable, or collected-ref histories return empty string. [1]
