# mcp/src/agents_remember/mcp/registration/explainer_tools.py

## Governing Overview

[Route overview](overview.md)

The render answer keeps the publication identity and any inventory omission. Optional inventory and carried assets fit only as complete sections. A bounded answer can point to the full report.

## Purpose

Declares the explainer's four tools — `render`, `define_category`, `remove_category` and `grade` — on the server the seat launch already built, and holds each answer to its own bound.

## Code Commentary

- The roster is exactly these four: `render` is the browser check and the publication into the task, and the three grade tools are the validated grades. No harness tool does either, and everything else the seat does — shell, file reads and writes, search, native Git, AR's general tools — is the harness's or the ordinary roster's, so nothing else is declared here.
- Registration adds the four to the instance the launch created instead of starting a server of its own, so a seat has one server carrying AR's general tools and these four, at one copy of each implementation.
- Every body resolves its implementation on the call, so declaring the tools loads no renderer, no browser runner and no grade store; the token counter loads on the first answer it sizes.
- `answered` turns a typed refusal into `{state, refusal, detail}`, so a refused call is data the agent can read and act on rather than a raised call that ends its turn.
- `bounded` holds each answer to its tool's own bound — 1,000 tokens for `render`, 150 for `define_category` and `remove_category`, 400 for `grade` — and an answer over that bound is written whole to `scratch/answers/` with the state, the refusal and that file's path left in the reply. Nothing is cut.
- The reply first keeps core run, report, picture, interaction, publication and optional browser identity and any inventory omission. It then admits complete summary, inventory and carried-kit sections in order, followed by whole errors. A moved pointer names the complete section in the run report if the inline budget leaves anything out.
- The announce answer is passed through whole: a render that began no run carries its missing part and the one sentence, and there is no run folder to name. A publishing answer gains the load's `browser` record among its identity items, so the agent reads the Playwright version, the folder and whether this call fetched them.
- The judgment object is built on the first call and kept, because it carries the seat's identity and its fingerprints from construction and a per-call rebuild would be a different object.
- `grade` keeps each refused reference and its reason inline up to about 300 tokens; a longer list goes whole to `scratch/grades/` and the answer names the file, because the agent has to know which grades failed in order to fix them.

## Evidence

- The explainer's surface is supplied on the server the seat launch already built [1]

- A grade carries the binding it was made at and refuses when the environment left it [5]



- The announce answer passes through whole, with no run folder to name. [6]
- A publishing answer carries the browser its load ran with. [7]
- The render tool's own description tells the seat to say the sentence before the next call. [8]

- The reply first keeps core run, report, picture, interaction, publication and optional browser identity and any inventory omission. It then admits complete summary, inventory and carried-kit sections in order, followed by whole errors. A moved pointer names the complete section in the run report if the inline budget leaves anything out. [9]
