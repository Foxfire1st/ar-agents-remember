# mcp/tests/test_memory_attribution_producers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_attribution_producers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:16 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935` |
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The one-definition guard and explicit five-producer census. | L56-L64; L87-L117; L120-L138 | [mcp/tests/test_memory_attribution_producers.py](mcp/tests/test_memory_attribution_producers.py) |
| The hostile-body case preserves the message and parses the final attribution. | L141-L163 | [mcp/tests/test_memory_attribution_producers.py](mcp/tests/test_memory_attribution_producers.py) |
| The public carryover case verifies one commit and no extra repeat commit with absent cache. | L238-L300 | [mcp/tests/test_memory_attribution_producers.py](mcp/tests/test_memory_attribution_producers.py) |
| The existing baseline case verifies unborn readiness, cache-independent reuse, and unavailable-history refusal. | L303-L387 | [mcp/tests/test_memory_attribution_producers.py](mcp/tests/test_memory_attribution_producers.py) |
| The kernel owns the key and the single writer. | L51-L51; L67-L92 | [mcp/src/agents_remember/kernel/memory_attribution.py](mcp/src/agents_remember/kernel/memory_attribution.py) |
| Closeout-shaped producers reach that writer through the effective input model. | L144-L162 | [mcp/src/agents_remember/models/closeout/input.py](mcp/src/agents_remember/models/closeout/input.py) |

## Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No additional configured cross-repository evidence is claimed. | — | — |

## Update History

- 2026-09-15T01:16 UTC — Documented the added assertions inside the existing public baseline case: unborn ready status, unavailable ancestry from a missing-parent commit, failed status/adoption results, and unchanged refs. No new test definition or case budget is claimed. Working candidate verified against the formatted source; real commit metadata and earlier history remain unchanged.


- 2026-09-15T00:51 UTC — Reconciled the retained five tests and producer census with the two-leg runtime: baseline/carryover now assert one attributed content commit, malformed-cache tolerance, untracked computed output, and no extra repeat commit; obsolete ledger-only site/lane claims are no longer current prose. Working candidate verified by source inspection; real last-touch commit metadata retained, with no future commit hash or certification claim.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (provenance repair): the gate could not compare
  this claim with its verification provenance because one or more of its anchors resolved more than
  once at the verification commit, so no historical location was unique. Repaired the citation, not
  the claim: each anchor that named a construct by bare name now names its exact declaration text,
  which resolves once in the code tree, and any range that had drifted off its construct was re-read
  at the declaration. The claim wording is unchanged, and the construct each range covers is the one
  the claim is about. Verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 2
  claim(s) whose anchor no longer sat in its cited range and normalised 8 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`,
  base `5bb124d4`): created this one-to-one sidecar for the leaf's new test module, which is the census
  the leaf is really about. Recorded the corrected census (5 producers, 0 untrailered, with the
  producer→commit-site→renderer→code-commit table), both corrections to the master's 2026-09-13T22:05
  decision (`closeout_recovery.py` is the recovery route's CODE leg, not a producer; the missed producer
  is `preparation/memory_output.py:92`), and the trailerless-by-rule table with a reason per site. Stated
  the durable rule the module enforces — the key is declared once and never spelled as a quoted literal
  in a second production module, and the trailer is appended as its own final block rather than woven
  into the caller's body, because carryover and baseline take that body as a public argument that may be
  multi-paragraph — together with the residual gap the census cannot close (a third-way producer, and the
  prepared leg having no behavioural case). Verification metadata is intentionally blank: the candidate
  is uncommitted and no commit contains this file yet, so closeout owns the stamp.
