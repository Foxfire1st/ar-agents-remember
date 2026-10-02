# dashboard/src/data/knowledgeReader.ts

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
- **A link from a history row (L37, MIK-R29 rule 5).** `IncomingLink.sourceSubject` is the summary of the record
  a `history_row` source is about: a row has no page of its own, so the reader navigates to that record.
  `sourceRecord` stays the summary of a record source.

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

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement of the address and the typed answers. [1]
- The hash prefix and the read timeout. [2]
- The address a view is named by. [3]
- The selection block: code tree, its source and note, and the pin. [4]
- A decision as the reader shows it. [5]
- The path view, bounded for a directory; a subtree page. [6]
- The timeline with per-source states; the truth view with `outgoingState`. [7]
- The selector's choices with `commitsState`. [8]
- The shareable hash, read and written. [9]
- A typed answer returned whatever its status; only transport failures throw. [10]
- An address's own read, and one subtree page. [11]
- The code address of an anchor, and its label. [12]
- The navigation case: links change the shareable hash, and the hash round-trips. [13]

- An incoming link may carry the record its history-row source is about. [14]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
