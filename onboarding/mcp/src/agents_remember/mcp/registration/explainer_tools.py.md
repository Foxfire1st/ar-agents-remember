# mcp/src/agents_remember/mcp/registration/explainer_tools.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Declares the explainer's four tools — `render`, `define_category`, `remove_category` and `grade` — on the server the seat launch already built, and holds each answer to its own bound.

## Code Commentary

- The roster is exactly these four: `render` is the browser check and the publication into the task, and the three grade tools are the validated grades. No harness tool does either, and everything else the seat does — shell, file reads and writes, search, native Git, AR's general tools — is the harness's or the ordinary roster's, so nothing else is declared here.
- Registration adds the four to the instance the launch created instead of starting a server of its own, so a seat has one server carrying AR's general tools and these four, at one copy of each implementation.
- Every body resolves its implementation on the call, so declaring the tools loads no renderer, no browser runner and no grade store; the token counter loads on the first answer it sizes.
- `answered` turns a typed refusal into `{state, refusal, detail}`, so a refused call is data the agent can read and act on rather than a raised call that ends its turn.
- `bounded` holds each answer to its tool's own bound — 1,000 tokens for `render`, 150 for `define_category` and `remove_category`, 400 for `grade` — and an answer over that bound is written whole to `scratch/answers/` with the state, the refusal and that file's path left in the reply. Nothing is cut.
- `render_answer` builds the identity items first and never trims them: the run folder, its report, the picture, the interaction folder with its count, and the publication. The summary and then whole errors fill what the 1,000 tokens leave, and a reserve is held free so naming a part that did not fit can never pass the bound; `moved` names that part with the report that holds all of it. An error is never added cut.
- The judgment object is built on the first call and kept, because it carries the seat's identity and its fingerprints from construction and a per-call rebuild would be a different object.
- `grade` keeps each refused reference and its reason inline up to about 300 tokens; a longer list goes whole to `scratch/grades/` and the answer names the file, because the agent has to know which grades failed in order to fix them.

## Evidence

- The explainer's surface is supplied on the server the seat launch already built [1]
- A grade carries the binding it was made at and refuses when the environment left it [5]
