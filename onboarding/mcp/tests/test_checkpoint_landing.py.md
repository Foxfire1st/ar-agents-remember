# mcp/tests/test_checkpoint_landing.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Pin checkpoint/final landing cell differences, explicit candidate revalidation, and terminal abandon guards for an unfinished atomic master.

## Code Commentary

The self-contained fixture builds a sprint, one atomic master, an unfinished leaf task, and real code and memory repositories under an external-memory series contract. `_memory_repo` creates the memory side with the same remote-default shape as the code side so the terminal guard reads it like a real clone. The four classes are unchanged in intent: checkpoint versus final durable cells with cleanup left untouched by checkpoint, the same no-reclamation result through status projection, checkpoint versus final publication authority with stale-candidate refusal, and the landed-master abandon guard with the never-integrated terminal case permitted.

## Evidence

- Real memory repository backing the fixture [6]
- Fixture is an external-memory series contract over both repos [7]
- Checkpoint records state and leaves cleanup untouched [8]
- Checkpoint result keeps prior cleanup through status projection [9]
- Completed masters refused the weaker route; stale candidates refused [10]
- Landed masters cannot be abandoned; never-integrated terminal case allowed [11]
