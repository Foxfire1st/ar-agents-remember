# mcp/tests/test_memory_attribution_producers.py

## Governing Overview

[Nearest governing overview](overview.md)

Working-candidate verification: source inspected at 2026-09-15T01:16 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Keeps the memory-content producer census and shared attribution renderer visible, and exercises
baseline adoption and carryover through their real application tools on disposable repositories.

## Code Commentary

### Logic

The module contains source-census, renderer, historical-rewriter, unconverted-carryover refusal and converted baseline-adoption tests. The three content routes are external closeout, direct landing and baseline adoption. `models/closeout/input.py` carries the shared renderer; `kernel/memory_backfill.py` is the exact-path historical rewriter, not a new-content route. The AST census follows actual calls, including directly imported aliases, assignment-alias propagation and literal getattr bindings, rejects unlisted callers and returned retired names, and is tested with copied-producer, returned-name and three indirect-caller negative controls. It is not proof that every route has executed.

The renderer case deliberately uses a multi-paragraph caller body whose final paragraph resembles
trailers. It checks preservation of that body, a separate final attribution block, and parsing of
the appended code commit rather than the lookalike in the body. Baseline generates its own adoption subject. Carryover writes into an open recovery worktree without a standalone commit; it accepts no CarryoverCommitMessages argument.

`_carryover_world` builds a real source/official code comparison and a separate source-memory checkout, using unconverted fixture memory by default. `test_carryover_apply_refuses_unconverted_memory_with_the_conversion_step` supplies malformed cache bytes and requires the central `legacy-format` refusal with conversion guidance. Code/memory refs, memory HEAD, status, cached diff, staged entry inventory and file bytes are unchanged. Successful legacy carryover publication/replay is retired, not current attribution coverage. Converted carryover behavior remains the separately scoped MIK-R56 obligation.

The baseline case creates the exact unborn default memory branch with the converted layout marker, supplies a malformed cache, and
first checks that public status reports `ready`. It then adopts through the application service,
checks that adoption creates one attributed memory-content commit, verifies the derived cache, and
removes the cache before a repeat that still returns `already-adopted` without another commit.

The same case then places a commit with a missing parent at the memory branch HEAD. The HEAD itself
resolves, but its ancestry cannot be walked. Public status and adoption both report `unavailable`
with `ok=false`, and the adoption refusal leaves every ref unchanged. This extends the existing
baseline test; no collection or execution count is claimed here. Retired ledger constructor options
and ledger-commit return fields are not part of either operation.

`test_carryover_takes_the_unconverted_memory_cutover_lock` retains returned legacy-format refusal and unchanged observed target HEAD and status, including converted-sibling crossing-sync guidance. The obsolete converted-target file-writer refusal is removed. `test_the_named_history_rewriter_replays_the_original_tree` rebuilds from the original tree and preserves parents and author/committer identity/timestamps, despite a different staged checkout, without moving HEAD or the observed index tree.

### Conventions

Assertions intentionally mix source inspection with real Git object reads. The census is not a
runtime or certification guarantee, and its AST call census is bounded to the recognized call/import forms, not every hypothetical
producer style. SHA-shaped constants are independent trailer oracles; they are not evidence that a
code repository contains those objects. Fixture and behavioral assertions establish that separately.
Historical test counts, lane manifests, and old ledger-leg sites remain historical notes below;
they are not instructions to restore removed tests or runtime publication paths.

### Invariants And Boundaries

- Memory producers use the shared renderer; no second production trailer spelling is introduced.
- Caller-owned bodies survive unchanged when attribution is appended.
- Converted baseline adoption creates a real attributed content commit, never a ledger-only commit; this module retains unconverted carryover refusal; separate converted-pair tests write without committing and leave ordinary closeout to publish memory.
- Cached rows are checked as computed output, not accepted as commit or Git-operation authority.
- Unreadable ancestry behind a resolvable memory HEAD reports `unavailable`; the refusal leaves refs unchanged.
- A focused test or source census does not establish live execution or acceptance.

### Todos

No new file-local follow-up is established by this documentation pass.

## Legacy carryover returns without writing

The public unconverted carryover case now receives a returned result rather than expecting an exception: `ok=false`, code `legacy-format`, a short `did not run` message, conversion guidance in `detail`, and presence of `nextAction`. Its complete before/after ref, HEAD, status, staged-entry and byte-tree comparison is retained. The sibling-line case uses the returned legacy envelope and checks branch/crossing-sync text in `detail`; the retired converted-target file-writer RuntimeError half no longer exists. The full refs/staged/byte-tree frame belongs to the first case; the sibling case observes target HEAD and status only; converted carryover permission is protected separately.


## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.





### Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

No additional configured cross-repository evidence is claimed.

### Current Source-Inspection References


- One-definition attribution guard and exact three-content-route AST census retain copied/returned-name negatives and add assignment-alias and literal-getattr caller negatives; the original-tree backfill witness is separate. [1]

- The hostile-body case preserves the message and parses the final attribution. [2]

- Public unconverted carryover asserts conversion guidance and no observed ref, index, cache or content mutation; the prior successful-attribution test is retired [3]

- The existing baseline case verifies unborn readiness, cache-independent reuse, and unavailable-history refusal. [4]

- The kernel declares the attribution key and appends its shared renderer trailer; its docstring names only surviving content routes and the separate original-tree historical rewriter. [5]

- Closeout-shaped producers reach that writer through the effective input model. [6]

- Converted-sibling cutover returns legacy-format with branch/crossing guidance and preserves the observed target HEAD/status pair. [7]



- Unconverted carryover returns the legacy-format envelope and preserves the complete observed state population. [8]
