# dashboard/src/data/knowledgeReader.ts

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

**The dashboard's adapter for the path-based knowledge reader (MIK-R29): the answer types of every view, the
shareable `#knowledge?…` address, and the reads of `/api/knowledge/reader/<view>`.** The reader browses one
repository's knowledge at one memory tree (`published` by default, any memory commit, or `leaf:<scope>`) and
needs no task. Every view is addressed by the same values its URL carries, so a view can be shared and every
link is a navigation (rule 5). MIK-R79 rule 3/6 adds the tree row's `hasKnowledge`, `hasOverview` and
`coverage` fields, which mark a row without presenting an unknown as false.

## Code Commentary

### Logic

- **Answer types.** One interface per view mirrors the backend's documents: `ReaderSelection` (with
  `codeTree`, `codeSource`, `codeNote` and `pinnedCommit`), `PathViewAnswer`, `SubtreeAnswer`,
  `TreeAnswer`, `RecordViewAnswer`, `DecisionView`, `CensusAnswer`, `WithoutProofAnswer`, `CodeAnswer`
  and `SelectionOptions`.
- **The tree row.** `TreeChild` carries the name, kind, `inCode`, `onboarding` and entry count. The
  MIK-R79 fields are optional because an unavailable memory enumeration has no answer:
  `hasKnowledge` and `hasOverview` are present only when the enumeration succeeded (a missing value
  is unknown, never `false`), and `coverage` is either `{state: 'counted', files, cards}` for a
  directory or `{state: 'unavailable', detail}` naming why the counts cannot be given.
- **The address.** `parseReaderHash` reads a `#knowledge?repo&commit&view&path|id|census|locator|blob`
  hash (anything else is `null`); the view defaults to `record` when an ID is named, else `path`, and
  the commit to `published`. `readerHash` writes it back.
- **Reads.** `readerGet` returns any JSON body with a string `state` whatever its HTTP status; only a
  transport failure or a body without a state throws `ReaderTransportError` (120 s timeout).
  `readAddress` sends an address's own view; `readSubtree` asks one page with the previous page's
  `continuation`.
- **Code links.** `codeAddress` builds the code view's address for an anchor (its locator and recorded
  blob); `locatorLabel` names a symbol, a line range or the whole file.

### Conventions

- The panel only issues GETs through this module; nothing here writes.
- Keys are the backend's camelCase document keys, unchanged.

### Invariants And Boundaries

- **The URL encodes commit and path or ID** (MIK-R29 rule 5).
- **A failed source is shown, never an empty result:** a typed refusal is returned as an answer, and a
  transport failure throws so the panel can name it.
- **An unknown knowledge presence is not `false`:** the optional tree fields exist so the tree can drop
  their claim instead of asserting a file has no card when the memory enumeration failed.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`, and
MIK-R79@v1 for the tree fields; they live outside the code and memory repositories, so they are named
here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The optional knowledge-presence and coverage fields of a tree row. [15]
- The shareable address, read and written. [16]
- A typed answer returned whatever its status; only transport failures throw. [17]
- The address a code citation opens. [18]
- The tree that renders the optional fields without claiming an unknown. [19]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
