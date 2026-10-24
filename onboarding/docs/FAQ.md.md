# docs/FAQ.md

## Current operative account — MIK-R199

- The answer to "How does an agent find the right memory?" keeps by-path retrieval as the
  deterministic mirror address (`src/foo/bar.ts` → `<memory-root>/onboarding/src/foo/bar.ts.md`)
  with "no ranking, embedding threshold, or index step", and describes the by-meaning and
  by-relationship routes in the past tense: semantic search "was the route; its provider is
  retired, so this route has no engine now", and a code graph "answered callers, callees, and
  dependencies; that provider is retired too" (`docs/FAQ.md:24-26`).
- The paragraph under that answer says by-path "needs nothing extra, and it is the route with an
  engine today", then sends the reader to Concepts and to the Providers page, which it calls "a
  retirement and old-install cleanup account" (`docs/FAQ.md:28`). The page itself carries no
  cleanup procedure; it delegates that to the linked page.
- In the vector-memory / graph-memory comparison the answer now opens "It isn't an alternative to
  them — it used them", says semantic search and a code-relationship graph "were first-class
  substrates for *finding* memory", that the providers are retired, and that by-path reads carry
  that job now (`docs/FAQ.md:124`).
- The closing "What This Is Not" paragraph says the former providers "built derived indexes *over*
  that memory and code to help find it", that they "never replaced it as the source of truth, and
  they are retired now" (`docs/FAQ.md:136`).
- Retired on this page: the semantic-search route, described as having no engine, and the
  code-graph route, described as retired too.
- The page states no provider install, prepare, seed, start, query, watch, provider-status or
  provider-lane obligation anywhere, and names no provider id, setting key or command
  (`docs/FAQ.md:1-136`).
- The memory-growth answer still speaks of "The optional semantic index" in the present tense: it
  "grows with the memory like any corpus, but it only helps *find* notes" (`docs/FAQ.md:40`). That is
  the one place the page describes a semantic index as present, and the page does not reconcile it
  with the retirement statements elsewhere.
- The page says nothing about leftover runtime folders, unused settings keys, stopping a leftover
  watcher, or any periodic safety check over provider leftovers (`docs/FAQ.md:1-136`).

### Superseded inventory

- Superseded by MIK-R199: "**By meaning** — when it knows the concept but not the file, semantic
  search over the memory returns candidate notes." The page now says that search "was the route;
  its provider is retired, so this route has no engine now" (`docs/FAQ.md:25`).
- Superseded by MIK-R199: "**By relationship** — when it knows an anchor but not its connections, a
  code graph answers callers, callees, and dependencies." The page now puts the graph in the past
  tense and adds "that provider is retired too" (`docs/FAQ.md:26`).
- Superseded by MIK-R199: "By-path needs nothing extra; meaning and relationship are opt-in
  providers." Replaced by the statement that by-path is "the route with an engine today" and by
  the pointer to the providers page as a retirement and cleanup account (`docs/FAQ.md:28`).
- Superseded by MIK-R199: "It isn't an alternative to them — it uses them. Semantic search over
  the memory and a code-relationship graph are first-class (opt-in) substrates for *finding*
  memory." Replaced by "it used them", the retirement of the providers, and by-path reads carrying
  that job (`docs/FAQ.md:124`).
- Superseded by MIK-R199: "The optional providers (semantic search, code graph) build derived
  indexes *over* that memory and code to help find it — they do not replace it as the source of
  truth." Replaced by the same claim in the past tense plus "they are retired now"
  (`docs/FAQ.md:136`).

### Source and authority bounds

- Document read in full: `docs/FAQ.md:1-136`.
- Changed regions read in the current file: `docs/FAQ.md:20-28`, `docs/FAQ.md:40`,
  `docs/FAQ.md:122-124`, `docs/FAQ.md:134-136`.
- Superseded wording was read from the supplied diff hunks for this exact path, not from a second
  copy of the document.
- These bounds record what the page states. They supply no build, test, publication, review or
  acceptance claim for the page or the product.

## Evidence

- By-meaning and by-relationship are described in the past tense as retired, with by-meaning left without an engine and by-path keeping the deterministic mirror address. [1]
- By-path is called "the route with an engine today" and the providers page is characterized as a retirement and old-install cleanup account. [2]
- The comparison answer says the product "used them" and that by-path reads now carry the finding job. [3]
- The former providers built derived indexes over memory and code, never replaced it as the source of truth, and are retired. [4]
- The memory-growth answer still describes an optional semantic index in the present tense. [5]
- The page names no provider command, setting key or provider id. [6]
