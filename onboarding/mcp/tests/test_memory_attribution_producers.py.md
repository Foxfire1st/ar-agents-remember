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

The file contains five tests. The source census checks that the key identifier and rendering are
owned by the one kernel module and that each `_PRODUCERS` entry reaches its shared renderer seam.
The five listed producers are ordinary external closeout, direct landing, prepared memory output,
carryover, and baseline adoption. This is a source census rather than proof that every route is
reachable or has executed.

The renderer case deliberately uses a multi-paragraph caller body whose final paragraph resembles
trailers. It checks preservation of that body, a separate final attribution block, and parsing of
the appended code commit rather than the lookalike in the body. Carryover receives a public memory
message; baseline generates its own adoption subject.

`_carryover_world` builds a real source/official code comparison and a separate source-memory
checkout. The carryover case supplies malformed cache bytes, applies the hostile body, verifies
exactly one real memory commit and both Git trailer readers, checks that the cache is untracked,
and repeats with the cache absent without creating another commit.

The baseline case creates the exact unborn default memory branch, supplies a malformed cache, and
first checks that public status reports `ready`. It then adopts through the application service,
checks that adoption creates one attributed memory-content commit, verifies the derived cache, and
removes the cache before a repeat that still returns `already-adopted` without another commit.

The same case then places a commit with a missing parent at the memory branch HEAD. The HEAD itself
resolves, but its ancestry cannot be walked. Public status and adoption both report `unavailable`
with `ok=false`, and the adoption refusal leaves every ref unchanged. This extends the existing
baseline test; the file still contains five test definitions. Retired ledger constructor options
and ledger-commit return fields are not part of either operation.

- **L37 (review R1 F2).** `test_carryover_never_writes_converted_memory_and_takes_the_cutover_lock` runs the real
  carryover world twice: with a converted sibling branch the unconverted target is locked, naming `branch
  converted-line` and the crossing sync; once the target itself is converted it is refused, naming the file
  writer. In both cases the target's `HEAD` and `git status` are unchanged.

### Conventions

Assertions intentionally mix source inspection with real Git object reads. The census is not a
runtime or certification guarantee, and its source-string checks cannot discover every hypothetical
producer style. SHA-shaped constants are independent trailer oracles; they are not evidence that a
code repository contains those objects. Fixture and behavioral assertions establish that separately.
Historical test counts, lane manifests, and old ledger-leg sites remain historical notes below;
they are not instructions to restore removed tests or runtime publication paths.

### Invariants And Boundaries

- Memory producers use the shared renderer; no second production trailer spelling is introduced.
- Caller-owned bodies survive unchanged when attribution is appended.
- The baseline and carryover operations create real attributed content commits, never ledger-only commits.
- Cached rows are checked as computed output, not accepted as commit or Git-operation authority.
- Unreadable ancestry behind a resolvable memory HEAD reports `unavailable`; the refusal leaves refs unchanged.
- A focused test or source census does not establish live execution or acceptance.

### Todos

No new file-local follow-up is established by this documentation pass.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

- The one-definition guard and explicit five-producer census. [1]
- The hostile-body case preserves the message and parses the final attribution. [2]
- The public carryover case verifies one commit and no extra repeat commit with absent cache. [3]
- The existing baseline case verifies unborn readiness, cache-independent reuse, and unavailable-history refusal. [4]
- The kernel owns the key and the single writer. [5]
- Closeout-shaped producers reach that writer through the effective input model. [6]

- Carryover never writes converted memory and takes the cutover lock. [7]

### Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

No additional configured cross-repository evidence is claimed.
