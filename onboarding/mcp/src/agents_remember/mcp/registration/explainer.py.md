# mcp/src/agents_remember/mcp/registration/explainer.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Declares the architect's one `explainer_control` tool — Update, Retire and claim over a master's explainers — as a declaration with no logic behind it.

## Code Commentary

- The declared arguments are the selection the sibling tools take: a repository id, the master folder's name and, for the two leaf actions, the leaf's id, plus a Retire's receipt id — never a path and never an agent id.
- The caller is this tool server's own agent binding, so the surface offers no argument by which a seat could name another agent; `claim` is described as open to any hosted architect seat while `update` and `retire` are accepted only from the seat the master-to-architect record names.
- The body is delegated through the lazy view to the payload builder, so registering this tool loads no payload builder and the refusals it can answer stand in the description rather than in code here. The explainer surface is four tools - `render`, `define_category`, `remove_category` and `grade` - and no tool that reads the workspace back: an answer names files on disk and is bounded, so a long answer or a picture is written to the workspace and cited rather than returned in full.

## Evidence

- One tool declares exactly the selection arguments and no agent identity [1]
- The declaration carries no behaviour: the payload builder is reached through the lazy view [2]
- The leaf is named by id for the two leaf actions [3]
