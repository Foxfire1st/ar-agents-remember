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

The module contains source-census, renderer, carryover-refusal and converted baseline-adoption tests. The source census checks that the key identifier and rendering are
owned by the one kernel module and that each `_PRODUCERS` entry reaches its shared renderer seam.
The five listed producers are ordinary external closeout, direct landing, prepared memory output,
carryover, and baseline adoption. This is a source census rather than proof that every route is
reachable or has executed.

The renderer case deliberately uses a multi-paragraph caller body whose final paragraph resembles
trailers. It checks preservation of that body, a separate final attribution block, and parsing of
the appended code commit rather than the lookalike in the body. Carryover receives a public memory
message; baseline generates its own adoption subject.

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
- Converted baseline adoption creates a real attributed content commit, never a ledger-only commit; this candidate's public carryover tests refuse rather than publish memory.
- Cached rows are checked as computed output, not accepted as commit or Git-operation authority.
- Unreadable ancestry behind a resolvable memory HEAD reports `unavailable`; the refusal leaves refs unchanged.
- A focused test or source census does not establish live execution or acceptance.

### Todos

No new file-local follow-up is established by this documentation pass.

## MIK-R46 R8: legacy carryover returns; converted refusal still raises

The public unconverted carryover case now receives a returned result rather than expecting an exception: `ok=false`, code `legacy-format`, a short `did not run` message, conversion guidance in `detail`, and presence of `nextAction`. Its complete before/after ref, HEAD, status, staged-entry and byte-tree comparison is retained. The sibling-line case uses the returned legacy envelope and checks branch/crossing-sync text in `detail`; after converting the target, it still requires the converted-target file-writer `RuntimeError`. That distinction preserves the original no-write observations without widening carryover permission or hiding unrelated runtime errors.


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

- The one-definition guard and explicit five-producer census. [1]
- The hostile-body case preserves the message and parses the final attribution. [2]
- Public unconverted carryover asserts conversion guidance and no observed ref, index, cache or content mutation; the prior successful-attribution test is retired [3]
- The existing baseline case verifies unborn readiness, cache-independent reuse, and unavailable-history refusal. [4]
- The kernel owns the key and the single writer. [5]
- Closeout-shaped producers reach that writer through the effective input model. [6]
- Carryover never writes converted memory and takes the cutover lock. [7]

- Unconverted carryover returns the legacy-format envelope and preserves the complete observed state population. [8]
