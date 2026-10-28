# mcp/src/agents_remember/canvas/explainer_worktrees.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The explainer's two ordinary detached Git worktrees, provisioned and removed by Git.

## Code Commentary

Both explainer trees are ordinary detached worktrees that Git owns: this module provisions and removes them and keeps no per-file copying, mode enforcement or alternate snapshot implementation of its own. Only the provisioning and removal destinations are confined; tracked symlinks are checked out normally, because Git is what decides them.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- checkout_tree provisions a detached worktree at the requested commit. [1]

- remove_checkout and prune_worktrees take the trees away through Git rather than by copying or deleting files. [2]
