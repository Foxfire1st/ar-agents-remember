# dashboard/src/data/knowledgeReader.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/knowledgeReader.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:06:02+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`|
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `dashboard/src/data/overview.md` |

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

**The dashboard's adapter for the path-based knowledge reader (MIK-R29): the answer types of every view, the
shareable `#knowledge?…` address, and the reads of `/api/knowledge/reader/<view>`.** The reader browses one
repository's knowledge at one memory tree (`published` by default, any memory commit, or `leaf:<scope>`) and
needs no task. Every view is addressed by the same values its URL carries, so a view can be shared and every
link is a navigation (rule 5).

## Code Commentary

### Logic

- **Answer types.** One interface per view mirrors the backend's documents: `ReaderSelection` (with
  `codeTree`, `codeSource`, `codeNote` and `pinnedCommit`), `PathViewAnswer` (with the bounded directory's
  `children` and `subtree`), `SubtreeAnswer` (rows, per-page states, the page block and `continuation`),
  `TreeAnswer`, `RecordViewAnswer` (with `outgoingState`, the invariant, family, decision and facet parts, and
  the `Timeline` with per-source states), `DecisionView` (stored and derived status, alternatives with
  `reconsiderWhen` and `reconsiderOn`), `CensusAnswer`, `WithoutProofAnswer`, `CodeAnswer` and
  `SelectionOptions` (with `commitsState`).
- **The address.** `parseReaderHash` reads a `#knowledge?repo&commit&view&path|id|census|locator|blob` hash
  (anything else is `null`); the view defaults to `record` when an ID is named, else `path`, and the commit
  to `published`. `readerHash` writes it back with commit and path or ID always spelled out, and `view` only
  when it is not implied. The address lives in the hash because production serves only `/`.
- **Reads.** `readerGet` returns any JSON body with a string `state` whatever its HTTP status (a 400
  `invalid-request` is a typed answer too); only a transport failure or a body without a state (a 503 from a
  process composed without the reader) throws `ReaderTransportError`. The timeout is 120 s.
  `readAddress` sends an address's own view; `readSubtree` asks one subtree page, passing the previous page's
  `continuation`.
- **Code links.** `codeAddress` builds the code view's address for an anchor (its locator as JSON, and its
  recorded blob); `locatorLabel` names a symbol, a line range or the whole file.

### Conventions

- The panel only issues GETs through this module; nothing here writes.
- Keys are the backend's camelCase document keys, unchanged.

### Invariants And Boundaries

- **Rule 5: the URL encodes commit and path or ID.** Proved by the dashboard's navigation case
  (`KnowledgeReader.test.tsx`: the family link changes the hash to `id=FAM-QWVGDSYX`, the hash round-trips, a
  non-reader hash is `null`); the reviewer's hash-drops-commit mutation was killed.
- **A failed source is shown, never an empty result:** a typed refusal is returned as an answer, and a transport
  failure throws so the panel can name it.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the address and the typed answers. | "Answers are typed by" | dashboard/src/data/knowledgeReader.ts:1-13 |
| The hash prefix and the read timeout. | `KNOWLEDGE_HASH`; `READER_TIMEOUT_MS` | dashboard/src/data/knowledgeReader.ts:17-18 |
| The address a view is named by. | `ReaderAddress` | dashboard/src/data/knowledgeReader.ts:22-31 |
| The selection block: code tree, its source and note, and the pin. | `ReaderSelection` | dashboard/src/data/knowledgeReader.ts:36-52 |
| A decision as the reader shows it. | `DecisionView` | dashboard/src/data/knowledgeReader.ts:149-162 |
| The path view, bounded for a directory; a subtree page. | `PathViewAnswer`; `SubtreeAnswer` | dashboard/src/data/knowledgeReader.ts:181-195; dashboard/src/data/knowledgeReader.ts:207-216 |
| The timeline with per-source states; the truth view with `outgoingState`. | `Timeline`; `RecordViewAnswer` | dashboard/src/data/knowledgeReader.ts:266-269; dashboard/src/data/knowledgeReader.ts:276-300 |
| The selector's choices with `commitsState`. | `SelectionOptions` | dashboard/src/data/knowledgeReader.ts:345-359 |
| The shareable hash, read and written. | `parseReaderHash`; `readerHash` | dashboard/src/data/knowledgeReader.ts:384-397; dashboard/src/data/knowledgeReader.ts:400-409 |
| A typed answer returned whatever its status; only transport failures throw. | `ReaderTransportError`; `readerGet` | dashboard/src/data/knowledgeReader.ts:413-420; dashboard/src/data/knowledgeReader.ts:424-441 |
| An address's own read, and one subtree page. | `readAddress`; `readSubtree` | dashboard/src/data/knowledgeReader.ts:444-464; dashboard/src/data/knowledgeReader.ts:467-474 |
| The code address of an anchor, and its label. | `codeAddress`; `locatorLabel` | dashboard/src/data/knowledgeReader.ts:477-490; dashboard/src/data/knowledgeReader.ts:492-498 |
| The navigation case: links change the shareable hash, and the hash round-trips. | "navigates by URL: explorer and links change the shareable hash, and the hash round-trips" | dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx:340-340 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:06:02+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`; review R3 and post-sync pass-with-notes, with R3-1 and R3-2 fixed): created this card for the new adapter MIK-R29 adds, recording the shareable hash (rule 5), the typed answers of rulings 09:42:58 N1 (`codeSource`, `codeNote`), N2 (`pinnedCommit`), F2 (the bounded directory and subtree pages) and F11 (`commitsState`, `outgoingState`, source states). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
