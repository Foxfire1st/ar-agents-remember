# mcp/src/agents_remember/canvas/presenter_refusals.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The review-presenter capability's one refusal type, in a module that imports nothing, so a declaration module can catch it without loading the store, the frame or the evidence implementations behind it.

## Code Commentary

- `PresenterRefused` carries a reason and a detail, renders both into its message, and subclasses `ValueError`, so an `except ValueError` written against either spelling catches the same exception.
- The class lives here rather than in the store: the store pulls the frame, evidence and comparison implementations and, through them, the worktree packages, and a module that only needs to catch a refusal must load none of that.
- The store imports this class back and keeps its own public name for it, so `StartOutcomeUnknown` still subclasses the one type and no second refusal class exists to be caught instead.

## Evidence

- The refusal carries a nameable reason and an actionable detail, and is one class rather than two [1]
- The reason and detail are both the stored fields and the rendered message [2]
- The module's whole public surface is that one name, which is what keeps it importable from a declaration module [3]
