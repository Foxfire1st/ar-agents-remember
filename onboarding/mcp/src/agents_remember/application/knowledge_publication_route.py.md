# mcp/src/agents_remember/application/knowledge_publication_route.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The ordinary publication route: which location the curator's ordinary run publishes to, what it
admits is already there, and what a reader finds afterwards.** The write plane had a real writer and
a real publication owner before this module existed; what it did not have was a *route*. Until
`ICR-R20@v1`, `--publish-to` was whatever path the caller typed, so the ordinary run either invented
a destination or published nowhere, and the repository's published knowledge was a location two
conventions had to agree on by luck.

This module owns exactly three decisions and nothing else (`declared_publication_location` `:115-132`,
`admitted_destination` `:135-199`, `published_identity_read_back` `:202-250`):

- **Which location the ordinary route publishes to.** The one location the ordinary *read* route
  declares — `published_dataset_path` resolved for this enclosure through the same context owner the
  read side uses (`contract_context`). It computes no path and names no file name of its own, so the
  location the writer reaches and the location a later read selects cannot drift apart by a second
  convention agreeing today. Inside an enclosure that location is the contract's memory **worktree**,
  which is the only place a task's knowledge can be written and still land with the rest of its
  memory.
- **What the run admits is already at that location.** A publication may never overwrite a dataset the
  caller never admitted, and the ordinary route has no caller-typed identity to offer. It does not
  need one: the run read its own `--baseline` before anything could replace it, so when that baseline
  *is* the declared location, the identity those captured bytes hold is exactly the identity at the
  destination. That is what makes the ordinary update explicit rather than a hopeful overwrite.
- **What a reader finds afterwards.** The publication owner's own result says what it installed; this
  route reads the location back through `resolve_published_intent`, the owner the ordinary read route
  uses, and reports whether the dataset a *reader* will select is the one the write reported. Neither
  the process exit nor the writer's own return value is that proof.

## Code Commentary

### Logic

Module surface (ranges are this candidate's extents, derived from each construct's own span):

- `DeclaredPublicationLocation` (dataclass, lines 68-80) — the declared path **and** the
  `CoordinationContext` it was resolved in, travelling as one value. The pair is the reason the type
  exists: the read-back must be made in the scope the write was made in, because a path re-derived
  from a second context could name the official memory repository while the publication landed on
  this leaf's memory line, and the read-back would then report an absence the write never caused.
- `DestinationAdmission` (dataclass, lines 83-94) — `identity` is the exact logical identity the run
  read at the destination (so the destination is *expected* to hold it) or `None` for "nothing is
  admitted there"; `detail` states which of the two and on what fact, because "expected to be absent"
  has several causes and a caller that has to guess which one is being given a message rather than a
  result.
- `PublishedIdentityReadBack` (dataclass, lines 97-112) — the three states `confirmed` (the location
  holds exactly the dataset the publication reported), `mismatch` (it holds a different one) and
  `unavailable` (nothing readable is there), with the shipped refusal code carried beside the
  reader's own sentence in the third case. A caller branches on `state` and, for the third, on
  `refusal_code` — never on the prose.
- `declared_publication_location` (function, lines 115-132) — resolves the enclosure's coordination
  context and the declared dataset path in it. A context that cannot be resolved is **refused by
  name** rather than defaulted to a guessed path, because an unowned destination is the one thing a
  write must never acquire by falling back.
- `admitted_destination` (function, lines 135-199) — the four facts a run can hold before it writes,
  each stating only what it established: no baseline was named (`:163-167`); the named baseline could
  not be captured (`:168-175`); the named baseline is another path, so what the destination holds is
  not something this run admitted (`:176-183`); and the named baseline **is** the destination, where
  the bytes captured at the top of the run are the dataset standing there and their identity is the
  one the publication may replace (`:184-199`).
- `published_identity_read_back` (function, lines 202-250) — reads the location through
  `resolve_published_intent`, maps its named absence to `unavailable` (`:216-226`), builds the
  `SnapshotIdentity` the reader found (`:227-231`), and answers `confirmed` or `mismatch` by comparing
  it against the identity the publication reported (`:232-250`).

**An admission is not a publication claim, and that distinction is load-bearing.** The module's own
docstring says what no case states: whether anything *was* published is a fact only the run's own
report holds, because a planning run and a batch that committed no entry both select a destination
and publish nothing. The detail string therefore stops at what was established ("no baseline was
named, so the destination is admitted as holding nothing") and the *caller* completes the line from
the report — `cli/knowledge_ingest.py`'s `_publication_route`. A detail reading "this is a first
publication on this line" would be the one field in the report that overstated the run, which is the
failure this whole route exists to prevent.

**Nothing here writes, publishes, or decides an outcome.** The batch and publication authorities stay
with `application/knowledge_curator_ingest` and the snapshot publication owner it calls; this module
resolves a destination, admits what is there, and reads back what a reader sees. `__all__`
(`:58-65`) declares exactly those three types and three functions as this module's public surface.

### Conventions

The module follows the route's conventions: frozen dataclasses for values that travel together,
functions that answer with a value or raise a *named* refusal instead of returning a sentinel, no MCP
or protocol types, and public names declared in `__all__`. Its docstring is the module contract — the
three decisions it owns, and the two owners it deliberately does not displace.

### Invariants And Boundaries

- **The destination is resolved, never defaulted.** There is no fallback path, no working-directory
  guess and no `HEAD`-style substitution: an enclosure whose memory layer cannot be resolved raises a
  named `ValueError`, and the CLI turns that into the invocation refusal it is.
- **One spelling, owned once.** The location comes from `published_dataset_path`; this module names no
  file name of its own, so the write side and the read side cannot disagree about where the
  repository's published knowledge lives.
- **The admission is derived, never typed.** The identity at the destination comes from bytes this run
  read from that same path before it could publish over it, because a caller-typed identity can be
  stale or wrong.
- **The read-back is an independent read, in the same scope.** It goes through the reader's own owner
  and the context that travelled with the path, and it never raises: `resolve_published_intent`
  answers with named states, so a read-back can never cost a run the report it already has.
- **A refused publication is read back not at all.** Nothing was established about the destination,
  and reporting an identity for it would be the fabricated success the requirement forbids; that
  decision belongs to the caller, which gates the read-back on the report's own publication result.
- **This module is read-only with respect to the dataset.** It opens nothing for writing and installs
  nothing.

### Todos

None requested of this card. One boundary worth naming for a later reader rather than carrying as an
open task: the read-back is bound to the **declared** route, so a caller-named `--publish-to` keeps
its previous shape and is not read back through this module. That is deliberate — a caller-named path
is not the repository's publication, so there is no declared location to read and no reader route to
bind it to — and it is recorded in the CLI card and in the leaf's own risk list.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` in the memory
layer reads "No entries configured yet", so it carries no `Domain Documentation` category). The
statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The one location the ordinary route publishes to, resolved through the enclosure's own coordination context exactly as the read side resolves it; an unresolvable memory layer is refused by name rather than guessed.** [1]
- **The admission as four ordered facts, each stating only what it established, and the ordinary update as the fourth: the destination holds the dataset this run forked from, read from that path before the run could publish over it.** [2]
- **The read-back through the reader's own owner, its three states, and the refusal code carried beside the reader's own sentence when nothing readable is there.** [3]
- The declared exports that make those six names this module's public surface. [4]
- **The declaration this module resolves against — the read route's one published-dataset location, which is what makes the write side reach the place the read side selects.** [5]
- **The reader's owner the read-back goes through, and the named absence it answers with instead of raising.** [6]
- The context owner that decides *which* memory root this location is, shared with the read side. [7]
- **The bytes the admission is derived from, captured at the top of the run, and the read that turns them into a dataset identity or a reason they are not one.** [8]
- The identity type both the admission and the read-back are expressed in. [9]
- **The caller that owns the destination *selection* and completes the admission's line from its own report — the split that keeps this module's detail from ever claiming a publication.** [10]
- The production owner whose closed write path and publication result this route hands to and reads back from. [11]
- **The cases that drive this route through the shipped CLI over a production-shaped enclosure.** [12]

### Cross-Repo References

No meaningful cross-repo references found: every behaviour this card describes is inside this
repository's own write plane and its own read route.

No meaningful cross-repo references found.
