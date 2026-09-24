# mcp/src/agents_remember/cli/knowledge_ingest_report.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_ingest_report.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T18:09+02:00 |
| lastVerifiedCommitHash | `0d7910f9d646161c414ed6543453536a3c749d49` |
| lastVerifiedCommitDate | 2026-09-24T08:10:24+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

**How one `knowledge-ingest` run is rendered — the report IS the product.** The ingest's outcome is a
report, not an exit code: a refusal per entry is a *result*, and a caller that branches on the process
status loses it. This module is the whole answer the run prints, in the two forms its caller may ask
for, and it was extracted from `cli/knowledge_ingest.py` when `ICR-R20@v1`'s ordinary publication
route added two more facts to that answer — the destination the run selected, and the identity a read
of it found back.

The split the extraction made is the module's boundary: the surface that decides **whether** a run may
proceed stays in the command module, and the shape of **what it says** lives here, so neither grows
past the rail by absorbing the other. `knowledge_ingest.py` is 692 lines and this module 205; before
the extraction the single file carried both responsibilities.

## Code Commentary

### Logic

- `summary` (function, lines 32-70) — the human-readable rendering: the mode and contract
  (`:42-42`), the candidate (`:43-43`), lane and repository (`:44-44`), the code tree and memory tree
  (`:45-47`), the batch state with its refusal when there is one (`:48-49`), the counts (`:50-50`),
  and **the run's publication route line** (`:51-51`), which is printed unconditionally because
  "this run named no destination" is itself the fact a reader needs. The publication result is added
  only when the report holds one (`:53-59`), the read-back only when the route made one (`:60-61`),
  the review baseline only when the handoff stated one (`:62-63`), and then one line per outcome
  (`:64-69`).
- `payload` (function, lines 73-118) — the machine-readable report and therefore *the contract*: every
  tuple becomes a list and every dataclass a mapping, nothing is summarised away, because a caller
  that has to re-read the database to learn what happened has been given a message rather than a
  result. `publicationRoute` (`:109-109`) is the run's own line about the destination it selected —
  the declared published location, a caller-named path, or the fact that it named none;
  `publishedIdentity` (`:113-113`) is the read-back, and it is `None` when this run published nothing
  to read back, which is a different fact from a read-back that found the wrong dataset.
- `_identity_line` (function, lines 121-127) — one read-back as the single line a reader scans it on:
  the state, the digest (or `-` when there is none), the path, and the refusal code when the state is
  `unavailable`.
- `_read_back_block` (function, lines 130-144) — the read-back as the smallest owned object, carrying
  the reader's own sentence in `detail` and, for `unavailable`, the shipped `refusalCode`.
- `_targets` (function, lines 147-151) — how one resolved target (path plus its symbol or line range)
  is rendered per entry.
- `_counts` (function, lines 154-168) — the entry arithmetic: the operation's own ten counters plus
  `committed` and `refused` (`:166-167`), which are the two figures that let a caller see a partial
  hand-off without re-deriving it from the lists.
- `_outcome` (function, lines 171-205) — one entry's whole outcome, including the state the operation
  itself assigned it and every route and target it touched.
- `__all__` (line 29) — `payload` and `summary` are the module's whole surface; everything else is
  private.

**Two fields are strings rather than booleans or objects, and for the same reason.** `reviewBaseline`
and `publicationRoute` both state what this run did about a handoff that can also have several reasons
for not happening. "Not placed" and "not selected" are not `false`; they are facts whose reason a
caller acts on, and a caller that has to guess which reason is being handed a message instead of a
result.

### Conventions

Follows the CLI package's conventions: a private `_`-prefixed helper per rendering concern, no
argument parsing and no operation logic, and public names declared in `__all__`. It imports the
operation's own report types rather than re-declaring them, so the renderer cannot drift from what the
operation produced.

### Invariants And Boundaries

- **The report is the result.** Nothing here infers anything from an exit status, and nothing rounds a
  partial outcome up: every entry appears in exactly one of `committed` / `rulings` / `refused`.
- **Rendering only.** This module decides no destination, runs no operation and performs no I/O beyond
  building strings and mappings; it is a pure function of the report plus the two facts the caller
  resolved.
- **`None` and "wrong" are different facts.** An absent `publishedIdentity` means this run published
  nothing to read back; a present one whose `state` is `mismatch` means the location holds a different
  dataset. Both are printed as what they are.
- **The JSON payload is the contract.** The human summary may be extended; the payload's keys are what
  a curator and the canonical carrier instructions consume, and a key is added rather than renamed.
- **Both entry points take the same two extra facts positionally-in-name.** `publicationRoute` and
  `publishedIdentity` are keyword-only on both renderers (`:35-37`, `:76-78`), so a caller cannot
  supply one and forget the other.

### Todos

None requested of this card. One fact a later reader may want to know rather than re-derive: the
counts block gained `committed` and `refused` in this same change, because the requirement's boundary
case — a hand-off with both committed and refused entries — must be readable from the report's own
arithmetic and not only from the two lists.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The human rendering, including the one line that is printed whether or not anything was published.** | `summary` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:32-70 |
| **The machine-readable report, and the two new facts: the destination the run selected and the identity an independent read found there.** | `payload`; `publicationRoute`; `publishedIdentity` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:73-118 |
| The entry arithmetic, including the explicit `committed` / `refused` counts the boundary case reads. | `_counts` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:154-168 |
| One read-back as a scannable line, and as the smallest owned object carrying the reader's own sentence. | `_identity_line`; `_read_back_block` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:63-127; mcp/src/agents_remember/cli/knowledge_ingest_report.py:220-234 |
| One entry's whole outcome, and how a resolved target is rendered per entry. | `_outcome`; `_targets` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:121-205; mcp/src/agents_remember/cli/knowledge_ingest_report.py:266-270 |
| The declared exports that make this module's two renderings its public surface. | `__all__` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:29-29 |
| **The caller that supplies both facts, and the surface that stayed behind in the command module: whether a run may proceed at all.** | `_print_report`; `_publication_route`; `run` | mcp/src/agents_remember/cli/knowledge_ingest.py:626-657; mcp/src/agents_remember/cli/knowledge_ingest.py:602-615; mcp/src/agents_remember/cli/knowledge_ingest.py:660-692 |
| The operation's own report types this module renders rather than re-declares. | `IngestReport`; `EntryOutcome` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:451-499; mcp/src/agents_remember/application/knowledge_curator_ingest.py:413-424 |
| **The read-back value the payload carries, whose three states are the reader's own vocabulary rather than this module's.** | `PublishedIdentityReadBack` | mcp/src/agents_remember/application/knowledge_publication_route.py:97-112 |
| The subparser registration that makes `knowledge-ingest` the ninth CLI subcommand whose report this module prints. | "knowledge-ingest" | mcp/src/agents_remember/cli/__main__.py:35-43 |

## Cross-Repo References

No meaningful cross-repo references found: this module renders one command's report and touches no
repository boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **the report renders both planes.** `payload` gained a `family` block and a `sources` block and `summary` gained one line for each, and every plane carries its **own** state — `recorded`, `projected` or `not-recorded` — so a run that wrote nothing reports null counts rather than zeroes that would read as measured. The source block claims a path and a digest only for the state that actually wrote the manifest.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.

- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): created this one-to-one card for the new module. The 135-line report renderer moved out of `cli/knowledge_ingest.py` when `ICR-R20@v1` added two facts to the run's answer, and the extraction is what keeps both files under the repository's size rail: the command module keeps the *decision* surface (which invocation may proceed, which destination it selected) and this module owns the *shape* of what it says. The card records the two new payload fields and why `publishedIdentity`'s absence is a different fact from a `mismatch`, the unconditional publication-route line in the human rendering, the two explicit counts the requirement's boundary case reads, and the string-not-boolean rule the module's own docstring states for `reviewBaseline` and `publicationRoute`. Every range was derived from its construct's own extent in this candidate rather than carried. **Verification metadata:** the card names the production line it was read against — `71a4433e686b3380af97a0836bb82bab2c8f2aad`, this leaf's base — because the module exists only in this leaf's uncommitted candidate, so no commit contains the content a stamp would claim to have verified. That is a statement of *what the reading was against*; the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates, and that remains the real stamp.
